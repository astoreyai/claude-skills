#!/usr/bin/env python3
"""
session_start.py - Unified SessionStart hook for session-initializer skill.
Shows PhD countdown, project status, and loads todos.
"""

import json
import sys
import re
import subprocess
from pathlib import Path
from datetime import datetime, date

# Paths
HOME = Path.home()
VAULT_PATH = HOME / "Documents" / "Obsidian" / "Aaron"
TODO_FILE = VAULT_PATH / "00_Navigation" / "Dashboards" / "Todo-Dashboard.md"
LOG_FILE = HOME / ".claude" / "logs" / "session-initializer.log"

# PhD Configuration
PHD_DEFENSE_DATE = date(2026, 1, 28)
PHD_READINESS = 85  # Update via CLAUDE.md or make dynamic later

# Active projects to check
ACTIVE_PROJECTS = [
    HOME / "projects" / "xai",
    HOME / "projects" / "world-model",
    HOME / "cc-flow",
    HOME / "github" / "astoreyai" / "claude-skills",
]


def log(message: str):
    """Log to file."""
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().isoformat()
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")


def get_phd_status() -> dict:
    """Get PhD defense countdown and readiness."""
    today = date.today()
    days_remaining = (PHD_DEFENSE_DATE - today).days

    return {
        "days": days_remaining,
        "date": PHD_DEFENSE_DATE.strftime("%b %d, %Y"),
        "readiness": PHD_READINESS
    }


def check_uncommitted() -> list:
    """Check for uncommitted changes in active projects."""
    uncommitted = []

    for project in ACTIVE_PROJECTS:
        if not project.exists():
            continue

        git_dir = project / ".git"
        if not git_dir.exists():
            continue

        try:
            result = subprocess.run(
                ["git", "-C", str(project), "status", "--porcelain"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.stdout.strip():
                uncommitted.append(project.name)
        except Exception:
            pass

    return uncommitted


def parse_todos() -> list:
    """Parse todos from Todo-Dashboard.md."""
    if not TODO_FILE.exists():
        # Try legacy location
        legacy = VAULT_PATH / "todo.md"
        if not legacy.exists():
            return []
        todo_path = legacy
    else:
        todo_path = TODO_FILE

    try:
        with open(todo_path, 'r') as f:
            content = f.read()
    except Exception:
        return []

    todos = []
    current_status = None

    for line in content.split('\n'):
        # Detect sections (handle both old and new formats)
        line_lower = line.lower()
        if 'in progress' in line_lower:
            current_status = 'in_progress'
        elif 'pending' in line_lower:
            current_status = 'pending'
        elif 'completed' in line_lower:
            current_status = 'completed'
        elif line.strip().startswith('- ['):
            match = re.match(r'^- \[.*?\] (.+)$', line.strip())
            if match and current_status:
                todos.append({
                    "content": match.group(1).strip(),
                    "status": current_status
                })

    return todos


def format_output(phd: dict, uncommitted: list, todos: list) -> str:
    """Format the session start message."""
    lines = []

    # PhD Status
    if phd["days"] > 0:
        urgency = "🔴" if phd["days"] < 30 else "🟡" if phd["days"] < 90 else "🟢"
        lines.append(f"{urgency} PhD Defense: {phd['days']} days ({phd['date']})")
        lines.append(f"   Readiness: {phd['readiness']}/100")

    # Uncommitted changes
    if uncommitted:
        lines.append(f"⚠️  Uncommitted: {', '.join(uncommitted)}")

    # Todos
    active = [t for t in todos if t['status'] in ('in_progress', 'pending')]
    in_progress = [t for t in todos if t['status'] == 'in_progress']

    if active:
        lines.append(f"📋 {len(active)} active tasks")
        if in_progress:
            for task in in_progress[:3]:
                lines.append(f"   → {task['content'][:50]}")

    return "\n".join(lines) if lines else "Session ready."


def main():
    """Main execution for SessionStart hook."""

    # Read hook input
    try:
        stdin_data = sys.stdin.read()
        hook_input = json.loads(stdin_data) if stdin_data.strip() else {}
    except Exception:
        hook_input = {}

    session_id = hook_input.get("session_id", "unknown")
    log(f"SessionStart triggered (session: {session_id})")

    # Gather data
    phd = get_phd_status()
    uncommitted = check_uncommitted()
    todos = parse_todos()

    # Format output
    message = format_output(phd, uncommitted, todos)

    log(f"PhD: {phd['days']} days, Uncommitted: {uncommitted}, Todos: {len(todos)}")

    output = {
        "continue": True,
        "suppressOutput": False,
        "systemMessage": message
    }

    print(json.dumps(output))
    sys.exit(0)


if __name__ == "__main__":
    main()
