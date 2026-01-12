#!/usr/bin/env python3
"""
checkpoint.py - Unified Worklog Synthesis

Scans session checkpoints and state files, synthesizes into clean
daily/weekly markdown worklogs for Discord #progress sharing.

Usage:
    python3 checkpoint.py              # Today's summary
    python3 checkpoint.py --morning    # Yesterday's comprehensive rollup (for morning standup)
    python3 checkpoint.py --weekly     # Weekly rollup
    python3 checkpoint.py --yesterday  # Yesterday's summary
    python3 checkpoint.py --date 2026-01-10  # Specific date
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

# Paths
HOME = Path.home()
CHECKPOINTS_DIR = HOME / ".claude" / "checkpoints"
SESSION_STATE_DIR = HOME / ".claude" / "session-state"
OBSIDIAN_LOGS = HOME / "Documents" / "Obsidian" / "Aaron" / "Session-Logs"
WORKLOG_DIR = HOME / "worklog"

# Days of week for display
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Synthesize worklog from session data")
    parser.add_argument("--morning", action="store_true",
                       help="Morning rollup: comprehensive summary of yesterday across ALL sessions")
    parser.add_argument("--weekly", action="store_true", help="Generate weekly rollup")
    parser.add_argument("--yesterday", action="store_true", help="Generate yesterday's summary")
    parser.add_argument("--date", type=str, help="Specific date (YYYY-MM-DD)")
    parser.add_argument("--no-write", action="store_true", help="Print only, don't write file")
    parser.add_argument("--slack", action="store_true", help="Output Slack/Discord-optimized format")
    return parser.parse_args()


def get_date_range(args) -> tuple[datetime, datetime, bool]:
    """Determine date range based on arguments. Returns (start, end, is_morning)."""
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    is_morning = False

    if args.morning:
        # Morning rollup = yesterday, comprehensive
        start = today - timedelta(days=1)
        end = today
        is_morning = True
    elif args.weekly:
        # Monday to today
        days_since_monday = today.weekday()
        start = today - timedelta(days=days_since_monday)
        end = today + timedelta(days=1)
    elif args.yesterday:
        start = today - timedelta(days=1)
        end = today
    elif args.date:
        start = datetime.strptime(args.date, "%Y-%m-%d")
        end = start + timedelta(days=1)
    else:
        start = today
        end = today + timedelta(days=1)

    return start, end, is_morning


def scan_checkpoints(start: datetime, end: datetime) -> list[dict]:
    """Scan checkpoint files within date range."""
    checkpoints = []

    if not CHECKPOINTS_DIR.exists():
        return checkpoints

    # Scan project subdirectories and root
    scan_dirs = [CHECKPOINTS_DIR] + [d for d in CHECKPOINTS_DIR.iterdir() if d.is_dir()]

    for scan_dir in scan_dirs:
        for f in scan_dir.glob("checkpoint-*.json"):
            try:
                match = re.search(r"checkpoint-(\d{8})-(\d{6})\.json", f.name)
                if not match:
                    continue

                file_date = datetime.strptime(match.group(1), "%Y%m%d")
                if start <= file_date < end:
                    with open(f) as fp:
                        data = json.load(fp)
                        data["_source_file"] = str(f)
                        data["_file_date"] = file_date
                        data["_source_type"] = "checkpoint"
                        # Extract project from path if not in data
                        if "project" not in data and scan_dir != CHECKPOINTS_DIR:
                            data["project"] = scan_dir.name
                        checkpoints.append(data)
            except (json.JSONDecodeError, ValueError):
                continue

    return checkpoints


def scan_session_state(start: datetime, end: datetime) -> list[dict]:
    """Scan session state files within date range."""
    states = []

    if not SESSION_STATE_DIR.exists():
        return states

    # Scan project subdirectories and root
    scan_dirs = [SESSION_STATE_DIR] + [d for d in SESSION_STATE_DIR.iterdir() if d.is_dir()]

    for scan_dir in scan_dirs:
        if not scan_dir.is_dir():
            continue

        for f in scan_dir.glob("session-*.json"):
            try:
                match = re.search(r"session-(\d{8})-(\d{6})\.json", f.name)
                if not match:
                    continue

                file_date = datetime.strptime(match.group(1), "%Y%m%d")
                if start <= file_date < end:
                    with open(f) as fp:
                        data = json.load(fp)
                        data["_source_file"] = str(f)
                        data["_file_date"] = file_date
                        data["_source_type"] = "session_state"
                        # Extract project from path if not in data
                        if "project" not in data and scan_dir != SESSION_STATE_DIR:
                            data["project"] = scan_dir.name
                        states.append(data)
            except (json.JSONDecodeError, ValueError):
                continue

    return states


def scan_obsidian_logs(start: datetime, end: datetime) -> list[dict]:
    """Scan Obsidian session logs within date range."""
    logs = []

    if not OBSIDIAN_LOGS.exists():
        return logs

    for project_dir in OBSIDIAN_LOGS.iterdir():
        if not project_dir.is_dir():
            continue

        for f in project_dir.glob("session-*.md"):
            try:
                match = re.search(r"session-(\d{8})-(\d{6})\.md", f.name)
                if not match:
                    continue

                file_date = datetime.strptime(match.group(1), "%Y%m%d")
                if start <= file_date < end:
                    content = f.read_text()
                    logs.append({
                        "_source_file": str(f),
                        "_file_date": file_date,
                        "_source_type": "obsidian",
                        "project": project_dir.name,
                        "content": content
                    })
            except (ValueError, IOError):
                continue

    return logs


def scan_worklog_entries(start: datetime, end: datetime) -> list[dict]:
    """Scan existing worklog files for entries (from SessionEnd auto-append)."""
    entries = []

    if not WORKLOG_DIR.exists():
        return entries

    current = start
    while current < end:
        worklog_file = WORKLOG_DIR / f"{current.strftime('%Y-%m-%d')}.md"
        if worklog_file.exists():
            try:
                content = worklog_file.read_text()
                # Parse session entries from worklog
                for match in re.finditer(r'### (\d{2}:\d{2}) - (\S+)\n(.*?)(?=\n### |\n---|\Z)', content, re.DOTALL):
                    time_str, project, body = match.groups()
                    entry = {
                        "_source_file": str(worklog_file),
                        "_file_date": current,
                        "_source_type": "worklog",
                        "_time": time_str,
                        "project": project,
                    }

                    # Parse completed tasks
                    completed = re.findall(r'\*\*Completed:\*\*\n((?:- .+\n?)+)', body)
                    if completed:
                        entry["completed"] = [t.strip('- \n') for t in completed[0].strip().split('\n') if t.strip('- \n')]

                    # Parse in-progress tasks
                    in_progress = re.findall(r'\*\*In Progress:\*\*\n((?:- .+\n?)+)', body)
                    if in_progress:
                        entry["in_progress"] = [t.strip('- \n') for t in in_progress[0].strip().split('\n') if t.strip('- \n')]

                    # Parse modified files
                    modified = re.findall(r'\*\*Modified:\*\* (.+)', body)
                    if modified:
                        entry["files_modified"] = [f.strip() for f in modified[0].split(',')]

                    entries.append(entry)
            except IOError:
                pass
        current += timedelta(days=1)

    return entries


def normalize_task(task: str) -> str:
    """Normalize task string for deduplication."""
    # Lowercase, strip whitespace, remove common variations
    normalized = task.lower().strip()
    # Remove trailing punctuation
    normalized = re.sub(r'[.!?]+$', '', normalized)
    # Remove percentage indicators for comparison
    normalized = re.sub(r'\s*\(\d+%?\)$', '', normalized)
    # Remove common prefixes
    normalized = re.sub(r'^(completed|done|finished|fixed|added|updated|created):\s*', '', normalized)
    return normalized


def deduplicate_tasks(tasks: list[str]) -> list[str]:
    """Deduplicate tasks using normalized comparison."""
    seen = {}
    result = []

    for task in tasks:
        normalized = normalize_task(task)
        if normalized and normalized not in seen:
            seen[normalized] = task
            result.append(task)

    return result


def extract_items(data: list[dict], dedupe: bool = True) -> dict:
    """Extract and optionally deduplicate items from all sources."""
    items = {
        "completed": [],
        "in_progress": [],
        "files_modified": [],
        "decisions": [],
        "blockers": [],
        "projects": set(),
        "sessions": [],  # Track individual sessions for morning rollup
        "narratives": []
    }

    for entry in data:
        project = entry.get("project", "unknown")
        items["projects"].add(project)

        # Track session info
        session_info = {
            "project": project,
            "time": entry.get("_time", entry.get("timestamp", "")[:16] if entry.get("timestamp") else ""),
            "source": entry.get("_source_type", "unknown"),
            "completed": [],
            "in_progress": []
        }

        # Extract completed tasks
        for task in entry.get("completed", []):
            if isinstance(task, str) and task.strip():
                items["completed"].append(task.strip())
                session_info["completed"].append(task.strip())
            elif isinstance(task, dict):
                task_str = task.get("task") or task.get("content") or str(task)
                if task_str:
                    items["completed"].append(task_str)
                    session_info["completed"].append(task_str)

        # Extract from todos array (richer format)
        for todo in entry.get("todos", []):
            if isinstance(todo, dict):
                content = todo.get("content", "")
                status = todo.get("status", "")
                if content:
                    if status == "completed":
                        items["completed"].append(content)
                        session_info["completed"].append(content)
                    elif status == "in_progress":
                        items["in_progress"].append(content)
                        session_info["in_progress"].append(content)

        # Extract in-progress tasks
        for task in entry.get("in_progress", []):
            if isinstance(task, str) and task.strip():
                items["in_progress"].append(task.strip())
                session_info["in_progress"].append(task.strip())
            elif isinstance(task, dict):
                task_str = task.get("task") or task.get("content") or str(task)
                pct = task.get("percent", "")
                if pct:
                    task_str = f"{task_str} ({pct}%)"
                if task_str:
                    items["in_progress"].append(task_str)
                    session_info["in_progress"].append(task_str)

        # Extract from open_tasks (session state format)
        for task in entry.get("open_tasks", []):
            if isinstance(task, str) and task.strip():
                items["in_progress"].append(task.strip())
                session_info["in_progress"].append(task.strip())

        # Extract files modified
        for f in entry.get("files_modified", []):
            if isinstance(f, str) and f.strip():
                items["files_modified"].append(f.strip())
            elif isinstance(f, dict):
                path = f.get("path", str(f))
                items["files_modified"].append(path)

        # Extract from git_status
        git_status = entry.get("git_status", {})
        for proj in git_status.get("uncommitted_projects", []):
            items["files_modified"].append(f"{proj} (uncommitted)")

        # Extract decisions
        for d in entry.get("decisions", []):
            if isinstance(d, str) and d.strip():
                items["decisions"].append(d.strip())

        # Extract blockers
        for b in entry.get("blockers", []):
            if isinstance(b, str) and b.lower() not in ["none", "n/a", ""] and b.strip():
                items["blockers"].append(b.strip())

        # Extract narrative/summary
        narrative = entry.get("narrative") or entry.get("summary", "")
        if narrative and len(narrative) > 30:
            items["narratives"].append({
                "project": project,
                "text": narrative[:500]
            })

        # Parse Obsidian markdown content
        content = entry.get("content", "")
        if content:
            parse_obsidian_content(content, items, session_info)

        if session_info["completed"] or session_info["in_progress"]:
            items["sessions"].append(session_info)

    # Deduplicate if requested
    if dedupe:
        items["completed"] = deduplicate_tasks(items["completed"])
        items["in_progress"] = deduplicate_tasks(items["in_progress"])
        items["files_modified"] = list(dict.fromkeys(items["files_modified"]))  # Preserve order, remove dupes
        items["decisions"] = deduplicate_tasks(items["decisions"])
        items["blockers"] = deduplicate_tasks(items["blockers"])

    return items


def parse_obsidian_content(content: str, items: dict, session_info: dict) -> None:
    """Parse Obsidian markdown for structured data."""
    # Extract completed tasks (- [x] items)
    for match in re.finditer(r"- \[x\] (.+)", content):
        task = match.group(1).strip()
        items["completed"].append(task)
        session_info["completed"].append(task)

    # Extract in-progress tasks (- [ ] items)
    for match in re.finditer(r"- \[ \] (.+)", content):
        task = match.group(1).strip()
        items["in_progress"].append(task)
        session_info["in_progress"].append(task)

    # Extract files from tables
    for match in re.finditer(r"\| ([^\|]+\.[a-z]+) \|", content):
        items["files_modified"].append(match.group(1).strip())

    # Extract decisions from ## Key Decisions section
    decisions_match = re.search(r'## Key Decisions\s*\n((?:[-*\d.].+\n?)+)', content)
    if decisions_match:
        for line in decisions_match.group(1).strip().split('\n'):
            decision = re.sub(r'^[-*\d.]+\s*', '', line).strip()
            if decision:
                items["decisions"].append(decision)


def generate_daily_markdown(date: datetime, items: dict) -> str:
    """Generate daily worklog markdown."""
    day_name = DAYS[date.weekday()]
    date_str = date.strftime("%Y-%m-%d")

    lines = [f"# {date_str} ({day_name})", ""]

    # Projects touched
    if items["projects"]:
        projects = ", ".join(sorted(items["projects"]))
        lines.append(f"**Projects**: {projects}")
        lines.append("")

    # Completed
    if items["completed"]:
        lines.append("## Completed")
        for task in items["completed"]:
            lines.append(f"- {task}")
        lines.append("")

    # In Progress
    if items["in_progress"]:
        lines.append("## In Progress")
        for task in items["in_progress"]:
            lines.append(f"- {task}")
        lines.append("")

    # Files Modified (top 15)
    if items["files_modified"]:
        lines.append("## Files Modified")
        for f in items["files_modified"][:15]:
            f_display = f.replace(str(HOME), "~")
            lines.append(f"- `{f_display}`")
        if len(items["files_modified"]) > 15:
            lines.append(f"- ... and {len(items['files_modified']) - 15} more")
        lines.append("")

    # Decisions
    if items["decisions"]:
        lines.append("## Decisions")
        for d in items["decisions"]:
            lines.append(f"- {d}")
        lines.append("")

    # Blockers
    lines.append("## Blockers")
    if items["blockers"]:
        for b in items["blockers"]:
            lines.append(f"- {b}")
    else:
        lines.append("- None")
    lines.append("")

    # Footer
    lines.append("---")
    lines.append(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*")

    return "\n".join(lines)


def generate_morning_markdown(date: datetime, items: dict) -> str:
    """Generate comprehensive morning rollup markdown."""
    day_name = DAYS[date.weekday()]
    date_str = date.strftime("%Y-%m-%d")

    lines = [f"# Morning Rollup: {date_str} ({day_name})", ""]

    # Summary stats
    num_sessions = len(items["sessions"])
    num_completed = len(items["completed"])
    num_in_progress = len(items["in_progress"])
    num_projects = len(items["projects"])

    lines.append("## Summary")
    lines.append(f"- **Sessions**: {num_sessions}")
    lines.append(f"- **Completed**: {num_completed} tasks")
    lines.append(f"- **In Progress**: {num_in_progress} tasks")
    lines.append(f"- **Projects**: {num_projects}")
    lines.append("")

    # By Project
    if items["projects"]:
        lines.append("## By Project")

        # Group tasks by project
        project_tasks = defaultdict(lambda: {"completed": [], "in_progress": []})
        for session in items["sessions"]:
            proj = session["project"]
            project_tasks[proj]["completed"].extend(session["completed"])
            project_tasks[proj]["in_progress"].extend(session["in_progress"])

        for project in sorted(items["projects"]):
            lines.append(f"### {project}")

            # Deduplicate within project
            proj_completed = deduplicate_tasks(project_tasks[project]["completed"])
            proj_in_progress = deduplicate_tasks(project_tasks[project]["in_progress"])

            if proj_completed:
                lines.append("**Completed:**")
                for task in proj_completed[:10]:
                    lines.append(f"- {task}")

            if proj_in_progress:
                lines.append("**In Progress:**")
                for task in proj_in_progress[:5]:
                    lines.append(f"- {task}")

            if not proj_completed and not proj_in_progress:
                # Check for narratives
                proj_narratives = [n for n in items["narratives"] if n["project"] == project]
                if proj_narratives:
                    lines.append(f"- {proj_narratives[0]['text'][:100]}...")
                else:
                    lines.append("- Session activity recorded")

            lines.append("")

    # All Completed (deduplicated across sessions)
    if items["completed"]:
        lines.append("## All Completed Tasks")
        for task in items["completed"]:
            lines.append(f"- {task}")
        lines.append("")

    # Still In Progress
    if items["in_progress"]:
        lines.append("## Still In Progress")
        for task in items["in_progress"]:
            lines.append(f"- {task}")
        lines.append("")

    # Key Decisions
    if items["decisions"]:
        lines.append("## Key Decisions")
        for d in items["decisions"]:
            lines.append(f"- {d}")
        lines.append("")

    # Blockers
    if items["blockers"]:
        lines.append("## Blockers")
        for b in items["blockers"]:
            lines.append(f"- {b}")
        lines.append("")

    # Footer
    lines.append("---")
    lines.append(f"*Morning rollup generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*")

    return "\n".join(lines)


def generate_weekly_markdown(start: datetime, end: datetime, items: dict, daily_data: dict) -> str:
    """Generate weekly rollup markdown."""
    week_num = start.isocalendar()[1]
    year = start.year
    start_str = start.strftime("%b %d")
    end_str = (end - timedelta(days=1)).strftime("%b %d")

    lines = [f"# Week {week_num}, {year} ({start_str} - {end_str})", ""]

    # Summary stats
    active_days = len([d for d in daily_data if daily_data[d]["completed"]])
    total_completed = len(items["completed"])
    total_projects = len(items["projects"])

    lines.append("## Summary")
    lines.append(f"- **Active Days**: {active_days}")
    lines.append(f"- **Tasks Completed**: {total_completed}")
    lines.append(f"- **Projects Touched**: {total_projects}")
    lines.append("")

    # By project
    if items["projects"]:
        lines.append("## By Project")
        for project in sorted(items["projects"]):
            lines.append(f"### {project}")
            project_tasks = [n["text"][:200] for n in items["narratives"] if n["project"] == project]
            if project_tasks:
                for t in project_tasks[:3]:
                    lines.append(f"- {t}...")
            else:
                lines.append("- Session work recorded")
            lines.append("")

    # All completed (deduplicated)
    if items["completed"]:
        lines.append("## All Completed")
        for task in items["completed"]:
            lines.append(f"- {task}")
        lines.append("")

    # Key decisions
    if items["decisions"]:
        lines.append("## Key Decisions")
        for d in items["decisions"]:
            lines.append(f"- {d}")
        lines.append("")

    # Footer
    lines.append("---")
    lines.append(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*")

    return "\n".join(lines)


def generate_discord_output(date: datetime, items: dict, is_morning: bool = False, weekly: bool = False) -> str:
    """Generate Discord-optimized output."""
    if weekly:
        week_num = date.isocalendar()[1]
        lines = [f"**Week {week_num} Progress**", ""]
    elif is_morning:
        lines = [f"**Morning Rollup: {date.strftime('%Y-%m-%d')}**", ""]
    else:
        lines = [f"**{date.strftime('%Y-%m-%d')} Progress**", ""]

    if items["completed"]:
        lines.append("**Completed:**")
        for task in items["completed"][:15]:
            lines.append(f"  - {task}")
        if len(items["completed"]) > 15:
            lines.append(f"  - ... and {len(items['completed']) - 15} more")

    if items["in_progress"]:
        lines.append("**In Progress:**")
        for task in items["in_progress"][:8]:
            lines.append(f"  - {task}")

    if items["blockers"]:
        lines.append("**Blockers:**")
        for b in items["blockers"]:
            lines.append(f"  - {b}")

    return "\n".join(lines)


def main():
    args = parse_args()
    start, end, is_morning = get_date_range(args)

    # Ensure worklog directory exists
    WORKLOG_DIR.mkdir(parents=True, exist_ok=True)

    # Collect all data from multiple sources
    all_data = []
    all_data.extend(scan_checkpoints(start, end))
    all_data.extend(scan_session_state(start, end))
    all_data.extend(scan_obsidian_logs(start, end))
    all_data.extend(scan_worklog_entries(start, end))

    if not all_data:
        print(f"No session data found for {start.strftime('%Y-%m-%d')} to {(end - timedelta(days=1)).strftime('%Y-%m-%d')}")
        print(f"Searched:")
        print(f"  - {CHECKPOINTS_DIR}")
        print(f"  - {SESSION_STATE_DIR}")
        print(f"  - {OBSIDIAN_LOGS}")
        print(f"  - {WORKLOG_DIR}")
        sys.exit(0)

    # Extract items with deduplication
    items = extract_items(all_data, dedupe=True)

    # Generate output based on mode
    if args.weekly:
        daily_data = {}
        current = start
        while current < end:
            day_data = [d for d in all_data if d.get("_file_date", datetime.min).date() == current.date()]
            daily_data[current.strftime("%Y-%m-%d")] = extract_items(day_data)
            current += timedelta(days=1)

        markdown = generate_weekly_markdown(start, end, items, daily_data)
        filename = f"week-{start.strftime('%Y-W%W')}.md"
    elif is_morning:
        markdown = generate_morning_markdown(start, items)
        filename = f"morning-{start.strftime('%Y-%m-%d')}.md"
    else:
        markdown = generate_daily_markdown(start, items)
        filename = f"{start.strftime('%Y-%m-%d')}.md"

    # Write file
    if not args.no_write:
        output_path = WORKLOG_DIR / filename
        output_path.write_text(markdown)
        print(f"Wrote: {output_path}")
        print()

    # Output
    if args.slack:
        print(generate_discord_output(start, items, is_morning, args.weekly))
    else:
        print(markdown)


if __name__ == "__main__":
    main()
