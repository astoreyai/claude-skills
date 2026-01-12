#!/usr/bin/env python3
"""
synthesizer.py - Core synthesis logic for session-synthesizer skill.

Enhanced for Context Amnesia Prevention System v2 (Project-Scoped):
- Saves checkpoints to project-specific subdirectories
- Merges checkpoint data from autonomous checkpoints
- Consolidates Session-Logs into daily note summaries
- Handles both checkpoint-initiated and manual session ends
- Ensures multiple tmux sessions don't overwrite each other

Uses shared ClaudeMd library for CLAUDE.md operations and auto-archiving.
"""

import subprocess
import re
import sys
import json
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional

# Add lib to path for ClaudeMd import
sys.path.insert(0, str(Path.home() / ".claude"))

try:
    from lib.claude_md import ClaudeMd
except ImportError:
    ClaudeMd = None

# Paths
HOME = Path.home()
VAULT_PATH = HOME / "Documents" / "Obsidian" / "Aaron"
CLAUDE_MD = HOME / ".claude" / "CLAUDE.md"
DAILY_DIR = VAULT_PATH / "Daily"
SESSION_LOGS_DIR = VAULT_PATH / "Session-Logs"
TODO_FILE = VAULT_PATH / "00_Navigation" / "Dashboards" / "Todo-Dashboard.md"
LOG_DIR = HOME / ".claude" / "logs"
SESSION_STATE_DIR = HOME / ".claude" / "session-state"
CHECKPOINTS_DIR = HOME / ".claude" / "checkpoints"
UPLOAD_LOCKFILE = SESSION_STATE_DIR / ".upload.lock"
WORKLOG_DIR = HOME / "worklog"

# Known project roots for mapping cwd to project names
# Use resolved paths to handle symlinks correctly
PROJECT_ROOTS = {
    str(Path("/mnt/projects/xai").resolve()): "xai",
    str(Path(HOME / "kymera").resolve()): "kymera",
    str(Path(HOME / "github" / "astoreyai" / "ccflow").resolve()): "cc-flow",
    str(Path(HOME / "projects" / "ww").resolve()): "ww",
    str(Path(HOME / "github" / "astoreyai").resolve()): "astoreyai",
    str(Path(HOME / "projects" / "iam").resolve()): "iam",
    str(Path(HOME / "projects" / "kb").resolve()): "kb",
}

# Active projects to check for uncommitted changes
ACTIVE_PROJECTS = [
    Path("/mnt/projects/xai"),
    HOME / "kymera",
    HOME / "cc-flow",
    HOME / "github" / "astoreyai" / "claude-skills",
    HOME / "projects" / "ww",
]


def get_project_name(cwd: str) -> str:
    """
    Extract project name from current working directory.

    Checks against known project roots, falls back to directory name.
    """
    cwd_path = Path(cwd).resolve()
    cwd_str = str(cwd_path)

    # Check known project roots
    for root, name in PROJECT_ROOTS.items():
        if cwd_str.startswith(root):
            return name

    # Fall back to immediate directory name, sanitized
    name = cwd_path.name or "home"
    # Sanitize for filesystem
    return "".join(c if c.isalnum() or c in "-_" else "_" for c in name)


class SessionSynthesizer:
    """Main synthesizer class for SessionEnd processing."""

    def __init__(self, session_id: str, cwd: str, todos: List[Dict]):
        self.session_id = session_id
        self.cwd = Path(cwd) if cwd else HOME
        self.todos = todos or []
        self.timestamp = datetime.now()
        self.log_file = LOG_DIR / "session-synthesizer.log"
        self.messages: List[str] = []
        self.warnings: List[str] = []

        # Get project name from cwd
        self.project = get_project_name(str(self.cwd))

    def log(self, message: str):
        """Log message to file."""
        LOG_DIR.mkdir(parents=True, exist_ok=True)
        with open(self.log_file, "a") as f:
            f.write(f"[{self.timestamp.isoformat()}] {message}\n")

    def run(self) -> Dict[str, Any]:
        """Execute full synthesis pipeline."""
        self.log(f"SessionEnd synthesis started (session: {self.session_id}, project: {self.project})")

        # 1. EXTRACT
        git_status = self._check_git_status()
        todo_stats = self._analyze_todos()

        # 2. CHECK FOR EXISTING PROJECT CHECKPOINTS (from autonomous checkpoint)
        existing_checkpoint = self._find_project_checkpoint()

        # 3. SYNTHESIZE
        if existing_checkpoint:
            # Merge checkpoint data - don't duplicate work
            session_summary = self._generate_summary_from_checkpoint(existing_checkpoint)
            self.log(f"Using existing checkpoint for {self.project} session summary")
        else:
            # Generate minimal summary (no checkpoint exists)
            session_summary = self._generate_session_summary(git_status, todo_stats)

        # 4. UPDATE DAILY NOTE (consolidate all session logs)
        self._consolidate_daily_sessions()

        # 5. UPDATE CLAUDE.MD
        self._update_claude_md()

        # 6. SAVE SESSION STATE (if no checkpoint exists) - PROJECT SCOPED
        if not existing_checkpoint:
            session_state = self._save_project_session_state(session_summary, git_status, todo_stats)
        else:
            session_state = existing_checkpoint
            self.log(f"Skipping session state save - checkpoint already exists for {self.project}")

        # 7. SYNC
        self._save_todos()
        self._cleanup_vault()
        sync_result = self._trigger_sync()

        # 8. UPLOAD TO CLOUD
        if session_state and isinstance(session_state, (str, Path)):
            self._upload_session_state(Path(session_state))

        # 9. APPEND TO WORKLOG
        self._append_to_worklog(git_status, todo_stats)

        # 10. OUTPUT
        return self._build_output(git_status, todo_stats, sync_result)

    def _find_project_checkpoint(self) -> Optional[Dict]:
        """
        Find existing checkpoint from this session for THIS PROJECT.

        Returns checkpoint data if found within last 2 hours, else None.
        """
        project_state_dir = SESSION_STATE_DIR / self.project

        # Also check legacy flat structure
        dirs_to_check = [project_state_dir, SESSION_STATE_DIR]

        cutoff = self.timestamp - timedelta(hours=2)

        for state_dir in dirs_to_check:
            if not state_dir.exists():
                continue

            try:
                sessions = sorted(state_dir.glob("session-*.json"), reverse=True)

                for session_file in sessions[:10]:
                    with open(session_file) as f:
                        data = json.load(f)

                    # For legacy flat dir, check project matches
                    if state_dir == SESSION_STATE_DIR:
                        file_project = data.get("project", "")
                        if file_project != self.project:
                            continue

                    file_time = datetime.fromisoformat(data.get("timestamp", ""))

                    if file_time < cutoff:
                        break

                    # Check if this has a narrative (indicates autonomous checkpoint)
                    if data.get("narrative") and len(data.get("narrative", "")) > 100:
                        self.log(f"Found existing checkpoint: {session_file.name}")
                        return data

            except Exception as e:
                self.log(f"Error finding checkpoint in {state_dir}: {e}")

        return None

    def _generate_summary_from_checkpoint(self, checkpoint: Dict) -> str:
        """Generate session summary from existing checkpoint data."""
        lines = []
        lines.append(f"### Session {self.timestamp.strftime('%H:%M')}")

        project = checkpoint.get("project", self.project)
        lines.append(f"- **Project**: {project}")
        lines.append(f"- **Working Dir**: `{checkpoint.get('cwd', str(self.cwd))}`")

        if checkpoint.get("completed"):
            completed = checkpoint["completed"]
            lines.append(f"- **Completed**: {len(completed)} tasks")

        if checkpoint.get("in_progress"):
            in_progress = checkpoint["in_progress"]
            if isinstance(in_progress, list) and in_progress:
                if isinstance(in_progress[0], dict):
                    tasks = [f"{t.get('task', '')} ({t.get('percent', 0)}%)" for t in in_progress[:3]]
                else:
                    tasks = in_progress[:3]
                lines.append(f"- **In Progress**: {', '.join(tasks)}")

        obsidian_log = checkpoint.get("obsidian_log", "")
        if obsidian_log:
            lines.append(f"- **Full Log**: [[{obsidian_log}]]")

        return "\n".join(lines)

    def _consolidate_daily_sessions(self):
        """Consolidate all session logs from today into daily note summary."""
        today = self.timestamp.strftime("%Y-%m-%d")
        daily_file = DAILY_DIR / f"{today}.md"

        if not SESSION_LOGS_DIR.exists():
            return

        today_logs = []

        # Check both project subdirs and flat structure
        patterns = [
            SESSION_LOGS_DIR / "*" / f"session-{today.replace('-', '')}*.md",  # Project subdirs
            SESSION_LOGS_DIR / f"session-{today.replace('-', '')}*.md",  # Flat structure
        ]

        for pattern in patterns:
            for log_file in SESSION_LOGS_DIR.glob(str(pattern).replace(str(SESSION_LOGS_DIR) + "/", "")):
                try:
                    with open(log_file) as f:
                        content = f.read()

                    time_match = re.search(r'time:\s*"?(\d{2}:\d{2})"?', content)
                    project_match = re.search(r'project:\s*(\S+)', content)

                    narrative_match = re.search(r'## Work Narrative\s*\n\n(.+?)(?:\n\n|\n##)', content, re.DOTALL)

                    # Determine relative path for Obsidian link
                    rel_path = log_file.relative_to(SESSION_LOGS_DIR)

                    log_info = {
                        "file": str(rel_path),
                        "time": time_match.group(1) if time_match else "00:00",
                        "project": project_match.group(1) if project_match else "unknown",
                        "summary": narrative_match.group(1)[:200] if narrative_match else ""
                    }
                    today_logs.append(log_info)

                except Exception as e:
                    self.log(f"Error parsing session log {log_file}: {e}")

        if not today_logs:
            return

        # Remove duplicates based on file path
        seen = set()
        unique_logs = []
        for log_info in today_logs:
            if log_info["file"] not in seen:
                seen.add(log_info["file"])
                unique_logs.append(log_info)
        today_logs = unique_logs

        # Sort by time
        today_logs.sort(key=lambda x: x["time"])

        # Generate consolidated sessions section
        sessions_content = "## Sessions\n\n"
        for log_info in today_logs:
            sessions_content += f"### {log_info['time']} - {log_info['project']}\n"
            if log_info['summary']:
                summary_line = log_info['summary'].replace('\n', ' ')[:100]
                sessions_content += f"**Summary**: {summary_line}...\n"
            # Remove .md extension for Obsidian link
            link_path = log_info['file'].replace('.md', '')
            sessions_content += f"**Full Log**: [[Session-Logs/{link_path}|View Details]]\n\n"

        DAILY_DIR.mkdir(parents=True, exist_ok=True)

        if daily_file.exists():
            with open(daily_file, 'r') as f:
                content = f.read()

            if "## Sessions" in content:
                pattern = r'## Sessions\n\n.*?(?=\n## [^#]|\Z)'
                new_content = re.sub(pattern, sessions_content.rstrip() + "\n\n", content, flags=re.DOTALL)
            else:
                if "## Notes" in content:
                    new_content = content.replace("## Notes", sessions_content + "## Notes")
                else:
                    new_content = content + "\n" + sessions_content

            with open(daily_file, 'w') as f:
                f.write(new_content)
        else:
            content = f"""---
date: {today}
type: daily-note
---

# {self.timestamp.strftime('%A, %B %d, %Y')}

{sessions_content}
## Notes

## Tasks

"""
            with open(daily_file, 'w') as f:
                f.write(content)

        self.log(f"Consolidated {len(today_logs)} session logs into daily note")
        self.messages.append(f"Consolidated {len(today_logs)} sessions into daily note")

    def _check_git_status(self) -> Dict[str, Any]:
        """Check git status across active projects."""
        results = {"uncommitted": [], "clean": [], "not_git": []}

        for project in ACTIVE_PROJECTS:
            if not project.exists():
                continue

            git_dir = project / ".git"
            if not git_dir.exists():
                results["not_git"].append(project.name)
                continue

            try:
                result = subprocess.run(
                    ["git", "-C", str(project), "status", "--porcelain"],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                if result.stdout.strip():
                    results["uncommitted"].append(project.name)
                else:
                    results["clean"].append(project.name)
            except Exception as e:
                self.log(f"Git check failed for {project}: {e}")
                results["not_git"].append(project.name)

        if results["uncommitted"]:
            self.warnings.append(f"Uncommitted changes in: {', '.join(results['uncommitted'])}")

        return results

    def _analyze_todos(self) -> Dict[str, int]:
        """Analyze todo statistics."""
        stats = {
            "total": len(self.todos),
            "completed": sum(1 for t in self.todos if t.get("status") == "completed"),
            "in_progress": sum(1 for t in self.todos if t.get("status") == "in_progress"),
            "pending": sum(1 for t in self.todos if t.get("status") == "pending"),
        }
        return stats

    def _generate_session_summary(self, git_status: Dict, todo_stats: Dict) -> str:
        """Generate minimal session summary (when no checkpoint exists)."""
        lines = []
        lines.append(f"### Session {self.timestamp.strftime('%H:%M')}")
        lines.append(f"- **Project**: {self.project}")
        lines.append(f"- **Working Dir**: `{self.cwd}`")

        if todo_stats["completed"] > 0:
            lines.append(f"- **Completed**: {todo_stats['completed']} tasks")

        if todo_stats["in_progress"] > 0:
            lines.append(f"- **In Progress**: {todo_stats['in_progress']} tasks")

        if git_status["uncommitted"]:
            lines.append(f"- **Uncommitted**: {', '.join(git_status['uncommitted'])}")

        completed_tasks = [t for t in self.todos if t.get("status") == "completed"]
        if completed_tasks:
            lines.append("\n**Completed:**")
            for task in completed_tasks[:10]:
                lines.append(f"- {task.get('content', 'Unknown task')}")

        return "\n".join(lines)

    def _update_claude_md(self):
        """Update CLAUDE.md Last Updated timestamp and auto-archive old notes."""
        if ClaudeMd is not None:
            try:
                claude = ClaudeMd()
                if not claude.exists():
                    self.log(f"CLAUDE.md not found at {CLAUDE_MD}")
                    return

                today = self.timestamp.strftime("%Y-%m-%d")

                if claude.set_last_updated():
                    self.log(f"Updated CLAUDE.md timestamp to {today}")

                archived = claude.archive_old_notes(days=7)
                if archived > 0:
                    self.log(f"Archived {archived} old session notes")
                    self.messages.append(f"Archived {archived} old session notes")

                return
            except Exception as e:
                self.log(f"ClaudeMd error: {e}, falling back to legacy")

        # Legacy fallback
        if not CLAUDE_MD.exists():
            self.log(f"CLAUDE.md not found at {CLAUDE_MD}")
            return

        today = self.timestamp.strftime("%Y-%m-%d")

        with open(CLAUDE_MD, "r") as f:
            content = f.read()

        pattern = r'\*\*Last Updated\*\*: \d{4}-\d{2}-\d{2}'
        if re.search(pattern, content):
            new_content = re.sub(
                pattern,
                f"**Last Updated**: {today}",
                content
            )
            if new_content != content:
                with open(CLAUDE_MD, "w") as f:
                    f.write(new_content)
                self.log(f"Updated CLAUDE.md timestamp to {today}")

    def _save_todos(self):
        """Save todos to Obsidian dashboard."""
        TODO_FILE.parent.mkdir(parents=True, exist_ok=True)

        in_progress = [t for t in self.todos if t.get("status") == "in_progress"]
        pending = [t for t in self.todos if t.get("status") == "pending"]
        completed = [t for t in self.todos if t.get("status") == "completed"]

        content = f"""---
type: todo-dashboard
last_updated: {self.timestamp.isoformat()}
---

# Todo Dashboard

**Total**: {len(self.todos)} tasks ({len(completed)} completed, {len(in_progress)} in progress, {len(pending)} pending)

"""
        if in_progress:
            content += "## In Progress\n\n"
            for task in in_progress:
                content += f"- [ ] {task.get('content', '')}\n"
            content += "\n"

        if pending:
            content += "## Pending\n\n"
            for task in pending:
                content += f"- [ ] {task.get('content', '')}\n"
            content += "\n"

        if completed:
            content += "## Completed\n\n"
            for task in completed[-20:]:
                content += f"- [x] {task.get('content', '')}\n"
            content += "\n"

        content += f"\n---\n*Last synced: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}*\n"

        with open(TODO_FILE, "w") as f:
            f.write(content)

        self.log(f"Saved {len(self.todos)} todos to {TODO_FILE}")

    def _cleanup_vault(self):
        """Clean up vault structure violations and old files."""
        ALLOWED_ROOT = {"Home.md", "CLAUDE.md", "README.md"}

        root_todo = VAULT_PATH / "todo.md"
        if root_todo.exists():
            root_todo.unlink()
            self.log("Removed root todo.md (dashboard is canonical)")

        root_files = set(f.name for f in VAULT_PATH.glob("*.md"))
        violations = root_files - ALLOWED_ROOT

        if violations:
            self.warnings.append(f"Root violations: {', '.join(violations)}")
            self.log(f"Vault violations: {violations}")

        # Clean up old session logs per project (keep last 50 per project)
        if SESSION_LOGS_DIR.exists():
            # Project subdirs
            for project_dir in SESSION_LOGS_DIR.iterdir():
                if project_dir.is_dir():
                    logs = sorted(project_dir.glob("session-*.md"), reverse=True)
                    for old_log in logs[50:]:
                        try:
                            old_log.unlink()
                            self.log(f"Cleaned old session log: {old_log}")
                        except Exception:
                            pass

            # Legacy flat structure (keep last 100 total)
            logs = sorted(SESSION_LOGS_DIR.glob("session-*.md"), reverse=True)
            for old_log in logs[100:]:
                try:
                    old_log.unlink()
                    self.log(f"Cleaned old session log: {old_log.name}")
                except Exception:
                    pass

        # Clean up old session state per project (keep last 30 per project)
        if SESSION_STATE_DIR.exists():
            for project_dir in SESSION_STATE_DIR.iterdir():
                if project_dir.is_dir() and project_dir.name != ".upload.lock":
                    sessions = sorted(project_dir.glob("session-*.json"), reverse=True)
                    for old_session in sessions[30:]:
                        try:
                            old_session.unlink()
                        except Exception:
                            pass

            # Legacy flat structure (keep last 50)
            sessions = sorted(SESSION_STATE_DIR.glob("session-*.json"), reverse=True)
            for old_session in sessions[50:]:
                try:
                    old_session.unlink()
                except Exception:
                    pass

    def _trigger_sync(self) -> bool:
        """Trigger obsidian-sync to Google Drive."""
        sync_script = HOME / ".local" / "bin" / "obsidian-sync"

        if not sync_script.exists():
            self.log("obsidian-sync script not found, skipping")
            return False

        try:
            result = subprocess.run(
                [str(sync_script)],
                capture_output=True,
                text=True,
                timeout=120
            )
            if result.returncode == 0:
                self.messages.append("Obsidian synced to Google Drive")
                self.log("Obsidian sync completed successfully")
                return True
            else:
                self.log(f"Obsidian sync failed: {result.stderr}")
                return False
        except subprocess.TimeoutExpired:
            self.log("Obsidian sync timed out")
            return False
        except Exception as e:
            self.log(f"Obsidian sync error: {e}")
            return False

    def _save_project_session_state(self, summary: str, git_status: Dict, todo_stats: Dict) -> Optional[Path]:
        """Save session state to PROJECT-SPECIFIC JSON for context amnesia prevention."""
        project_state_dir = SESSION_STATE_DIR / self.project
        project_state_dir.mkdir(parents=True, exist_ok=True)

        # Extract full task content for richer worklog synthesis
        completed_tasks = [
            t.get("content", "")
            for t in self.todos
            if t.get("status") == "completed" and t.get("content")
        ]

        in_progress_tasks = [
            t.get("content", "")
            for t in self.todos
            if t.get("status") == "in_progress" and t.get("content")
        ]

        pending_tasks = [
            t.get("content", "")
            for t in self.todos
            if t.get("status") == "pending" and t.get("content")
        ]

        # Legacy format for backwards compatibility
        open_tasks = [
            t.get("content", "")[:100]
            for t in self.todos
            if t.get("status") in ("in_progress", "pending")
        ]

        files_modified = git_status.get("uncommitted", [])

        session_data = {
            "timestamp": self.timestamp.isoformat(),
            "session_id": self.session_id,
            "cwd": str(self.cwd),
            "project": self.project,
            "hostname": subprocess.getoutput("hostname"),
            "summary": summary[:500] if summary else "",
            # Rich task data for worklog synthesis
            "completed": completed_tasks[:20],
            "in_progress": in_progress_tasks[:10],
            "pending": pending_tasks[:10],
            # Full todos array for maximum flexibility
            "todos": [
                {"content": t.get("content", ""), "status": t.get("status", "")}
                for t in self.todos
                if t.get("content")
            ][:30],
            # Legacy fields
            "open_tasks": open_tasks[:10],
            "files_modified": files_modified[:10],
            "todo_stats": todo_stats,
            "git_status": {
                "uncommitted_count": len(git_status.get("uncommitted", [])),
                "uncommitted_projects": git_status.get("uncommitted", [])[:5]
            }
        }

        safe_timestamp = self.timestamp.strftime("%Y%m%d-%H%M%S")
        session_file = project_state_dir / f"session-{safe_timestamp}.json"

        try:
            with open(session_file, "w") as f:
                json.dump(session_data, f, indent=2)

            session_file.chmod(0o600)

            self.log(f"Session state saved to {session_file}")
            self.messages.append(f"Session state saved ({self.project})")

            return session_file

        except Exception as e:
            self.log(f"Failed to save session state: {e}")
            return None

    def _upload_session_state(self, session_file: Optional[Path]) -> bool:
        """Upload session state to Google Drive via rclone with lockfile."""
        if session_file is None or not session_file.exists():
            return False

        try:
            result = subprocess.run(["which", "rclone"], capture_output=True)
            if result.returncode != 0:
                self.log("rclone not installed, skipping cloud upload")
                return False
        except Exception:
            return False

        import time
        max_wait = 5

        for _ in range(max_wait):
            if UPLOAD_LOCKFILE.exists():
                time.sleep(1)
            else:
                break
        else:
            self.log("Upload lock held too long, skipping")
            return False

        try:
            UPLOAD_LOCKFILE.touch()

            # Upload to project-specific cloud folder
            result = subprocess.run(
                [
                    "rclone", "copy",
                    str(session_file),
                    f"gdrive:claude-sessions/{self.project}/"
                ],
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode == 0:
                self.log(f"Session state uploaded to gdrive:claude-sessions/{self.project}/")
                self.messages.append("Uploaded to Google Drive")
                return True
            else:
                self.log(f"rclone upload failed: {result.stderr}")
                return False

        except subprocess.TimeoutExpired:
            self.log("rclone upload timed out")
            return False
        except Exception as e:
            self.log(f"rclone upload error: {e}")
            return False
        finally:
            try:
                UPLOAD_LOCKFILE.unlink()
            except Exception:
                pass

    def _append_to_worklog(self, git_status: Dict, todo_stats: Dict):
        """Append session entry to daily worklog file."""
        WORKLOG_DIR.mkdir(parents=True, exist_ok=True)

        today = self.timestamp.strftime("%Y-%m-%d")
        day_name = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][self.timestamp.weekday()]
        worklog_file = WORKLOG_DIR / f"{today}.md"

        # Build session entry
        time_str = self.timestamp.strftime("%H:%M")
        entry_lines = [
            f"### {time_str} - {self.project}",
        ]

        # Add completed tasks
        completed_tasks = [t for t in self.todos if t.get("status") == "completed"]
        if completed_tasks:
            entry_lines.append("**Completed:**")
            for task in completed_tasks[:10]:
                entry_lines.append(f"- {task.get('content', 'Task')}")

        # Add in-progress tasks
        in_progress_tasks = [t for t in self.todos if t.get("status") == "in_progress"]
        if in_progress_tasks:
            entry_lines.append("**In Progress:**")
            for task in in_progress_tasks[:5]:
                entry_lines.append(f"- {task.get('content', 'Task')}")

        # Add files with uncommitted changes
        if git_status.get("uncommitted"):
            entry_lines.append(f"**Modified:** {', '.join(git_status['uncommitted'][:5])}")

        entry_lines.append("")  # Blank line between entries

        entry = "\n".join(entry_lines)

        # Create or append to worklog file
        if worklog_file.exists():
            with open(worklog_file, "r") as f:
                content = f.read()

            # Check if this session time already exists (avoid duplicates)
            if f"### {time_str} - {self.project}" in content:
                self.log(f"Worklog entry for {time_str} already exists, skipping")
                return

            # Append before the footer if it exists
            if "---\n*Generated:" in content:
                content = re.sub(
                    r'\n---\n\*Generated:.*$',
                    f"\n{entry}\n---\n*Updated: {self.timestamp.strftime('%Y-%m-%d %H:%M')}*",
                    content,
                    flags=re.DOTALL
                )
            else:
                content += f"\n{entry}"

            with open(worklog_file, "w") as f:
                f.write(content)
        else:
            # Create new worklog file
            content = f"""# {today} ({day_name})

{entry}
---
*Generated: {self.timestamp.strftime('%Y-%m-%d %H:%M')}*
"""
            with open(worklog_file, "w") as f:
                f.write(content)

        self.log(f"Appended session to worklog: {worklog_file}")
        self.messages.append("Worklog updated")

    def _build_output(self, git_status: Dict, todo_stats: Dict, sync_ok: bool) -> Dict[str, Any]:
        """Build final output for Claude Code."""
        summary_parts = [self.project]

        if todo_stats["completed"] > 0:
            summary_parts.append(f"{todo_stats['completed']} completed")

        if sync_ok:
            summary_parts.append("synced")

        if self.warnings:
            summary_parts.append(f"warnings: {len(self.warnings)}")

        summary = f"Session saved ({', '.join(summary_parts)})"

        if self.warnings:
            summary += f"\n{''.join(self.warnings)}"

        return {
            "continue": True,
            "suppressOutput": False,
            "systemMessage": summary
        }
