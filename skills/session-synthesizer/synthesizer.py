#!/usr/bin/env python3
"""
synthesizer.py - Core synthesis logic for session-synthesizer skill.
Handles extraction, synthesis, and sync operations.
"""

import subprocess
import re
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple

# Paths
HOME = Path.home()
VAULT_PATH = HOME / "Documents" / "Obsidian" / "Aaron"
CLAUDE_MD = HOME / ".claude" / "CLAUDE.md"
DAILY_DIR = VAULT_PATH / "Daily"
TODO_FILE = VAULT_PATH / "00_Navigation" / "Dashboards" / "Todo-Dashboard.md"
LOG_DIR = HOME / ".claude" / "logs"

# Active projects to check
ACTIVE_PROJECTS = [
    HOME / "projects" / "xai",
    HOME / "projects" / "world-model",
    HOME / "cc-flow",
    HOME / "github" / "astoreyai" / "claude-skills",
]


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

    def log(self, message: str):
        """Log message to file."""
        LOG_DIR.mkdir(parents=True, exist_ok=True)
        with open(self.log_file, "a") as f:
            f.write(f"[{self.timestamp.isoformat()}] {message}\n")

    def run(self) -> Dict[str, Any]:
        """Execute full synthesis pipeline."""
        self.log(f"SessionEnd synthesis started (session: {self.session_id})")

        # 1. EXTRACT
        git_status = self._check_git_status()
        todo_stats = self._analyze_todos()

        # 2. SYNTHESIZE
        session_summary = self._generate_session_summary(git_status, todo_stats)
        self._update_daily_note(session_summary)
        self._update_claude_md()

        # 3. SYNC
        self._save_todos()
        self._cleanup_vault()
        sync_result = self._trigger_sync()

        # 4. OUTPUT
        return self._build_output(git_status, todo_stats, sync_result)

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
                # Check for uncommitted changes
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
        """Generate session summary text."""
        lines = []
        lines.append(f"### Session {self.timestamp.strftime('%H:%M')}")
        lines.append(f"- **Working Dir**: `{self.cwd}`")

        if todo_stats["completed"] > 0:
            lines.append(f"- **Completed**: {todo_stats['completed']} tasks")

        if todo_stats["in_progress"] > 0:
            lines.append(f"- **In Progress**: {todo_stats['in_progress']} tasks")

        if git_status["uncommitted"]:
            lines.append(f"- **Uncommitted**: {', '.join(git_status['uncommitted'])}")

        # Add completed task details
        completed_tasks = [t for t in self.todos if t.get("status") == "completed"]
        if completed_tasks:
            lines.append("\n**Completed:**")
            for task in completed_tasks[:10]:  # Max 10
                lines.append(f"- {task.get('content', 'Unknown task')}")

        return "\n".join(lines)

    def _update_daily_note(self, session_summary: str):
        """Update or create daily note with session summary."""
        DAILY_DIR.mkdir(parents=True, exist_ok=True)
        today = self.timestamp.strftime("%Y-%m-%d")
        daily_file = DAILY_DIR / f"{today}.md"

        if daily_file.exists():
            # Append to existing
            with open(daily_file, "r") as f:
                content = f.read()

            # Add session under Sessions section
            if "## Sessions" in content:
                # Insert before the next ## or at end
                parts = content.split("## Sessions", 1)
                if len(parts) == 2:
                    rest = parts[1]
                    # Find next section
                    next_section = re.search(r'\n## [^#]', rest)
                    if next_section:
                        insert_pos = next_section.start()
                        new_rest = rest[:insert_pos] + f"\n\n{session_summary}\n" + rest[insert_pos:]
                    else:
                        new_rest = rest + f"\n\n{session_summary}\n"
                    content = parts[0] + "## Sessions" + new_rest
            else:
                # Add Sessions section at end
                content += f"\n\n## Sessions\n\n{session_summary}\n"

            with open(daily_file, "w") as f:
                f.write(content)
        else:
            # Create new daily note
            content = f"""---
date: {today}
type: daily-note
---

# {self.timestamp.strftime('%A, %B %d, %Y')}

## Sessions

{session_summary}

## Notes

## Tasks

"""
            with open(daily_file, "w") as f:
                f.write(content)

        self.messages.append(f"Daily note updated: {today}.md")
        self.log(f"Updated daily note: {daily_file}")

    def _update_claude_md(self):
        """Update CLAUDE.md Last Updated timestamp."""
        if not CLAUDE_MD.exists():
            self.log(f"CLAUDE.md not found at {CLAUDE_MD}")
            return

        today = self.timestamp.strftime("%Y-%m-%d")

        with open(CLAUDE_MD, "r") as f:
            content = f.read()

        # Update Last Updated line
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

        # Group by status
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
            for task in completed[-20:]:  # Keep last 20 completed
                content += f"- [x] {task.get('content', '')}\n"
            content += "\n"

        content += f"\n---\n*Last synced: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}*\n"

        with open(TODO_FILE, "w") as f:
            f.write(content)

        self.log(f"Saved {len(self.todos)} todos to {TODO_FILE}")

    def _cleanup_vault(self):
        """Clean up vault structure violations."""
        ALLOWED_ROOT = {"Home.md", "CLAUDE.md", "README.md"}

        # Remove root todo.md if exists (dashboard is canonical)
        root_todo = VAULT_PATH / "todo.md"
        if root_todo.exists():
            root_todo.unlink()
            self.log("Removed root todo.md (dashboard is canonical)")

        # Check for other violations
        root_files = set(f.name for f in VAULT_PATH.glob("*.md"))
        violations = root_files - ALLOWED_ROOT

        if violations:
            self.warnings.append(f"Root violations: {', '.join(violations)}")
            self.log(f"Vault violations: {violations}")

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
                timeout=120  # 2 minute timeout
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

    def _build_output(self, git_status: Dict, todo_stats: Dict, sync_ok: bool) -> Dict[str, Any]:
        """Build final output for Claude Code."""
        summary_parts = []

        # Todo summary
        if todo_stats["completed"] > 0:
            summary_parts.append(f"{todo_stats['completed']} completed")

        # Sync status
        if sync_ok:
            summary_parts.append("synced")

        # Warnings
        if self.warnings:
            summary_parts.append(f"warnings: {len(self.warnings)}")

        summary = f"Session saved ({', '.join(summary_parts)})" if summary_parts else "Session saved"

        if self.warnings:
            summary += f"\n{''.join(self.warnings)}"

        return {
            "continue": True,
            "suppressOutput": False,
            "systemMessage": summary
        }
