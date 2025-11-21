#!/usr/bin/env python3
"""
SessionStart hook to load persisted todos from Obsidian vault.
Reads tasks from ~/Documents/Obsidian/Aaron/todo.md and suggests recreating them.
"""

import json
import sys
import re
from pathlib import Path
from datetime import datetime

# Paths
VAULT_PATH = Path.home() / "Documents" / "Obsidian" / "Aaron"
TODO_FILE = VAULT_PATH / "todo.md"
LOG_FILE = Path.home() / ".claude" / "logs" / "todo-keeper.log"

def log(message):
    """Log to todo-keeper log file."""
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().isoformat()
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def parse_todo_file():
    """
    Parse todo.md and extract tasks.

    Returns list of dicts: [{"content": "...", "status": "..."}]
    """

    if not TODO_FILE.exists():
        log(f"No todo.md found at {TODO_FILE}")
        return []

    try:
        with open(TODO_FILE, 'r') as f:
            content = f.read()
    except Exception as e:
        log(f"ERROR: Failed to read {TODO_FILE}: {e}")
        return []

    todos = []
    current_status = None

    for line in content.split('\n'):
        # Detect status sections
        if line.startswith('## 🔄 In Progress'):
            current_status = 'in_progress'
        elif line.startswith('## 📝 Pending'):
            current_status = 'pending'
        elif line.startswith('## ✅ Completed'):
            current_status = 'completed'
        # Parse task lines
        elif line.strip().startswith('- ['):
            # Extract task content
            # Formats: - [ ] content, - [x] content, - [🔄] content
            match = re.match(r'^- \[.*?\] (.+)$', line.strip())
            if match and current_status:
                task_content = match.group(1).strip()
                todos.append({
                    "content": task_content,
                    "status": current_status
                })

    log(f"Parsed {len(todos)} tasks from todo.md")
    return todos

def format_todo_summary(todos):
    """Format todos as a summary message."""

    if not todos:
        return "No persisted tasks found."

    in_progress = [t for t in todos if t['status'] == 'in_progress']
    pending = [t for t in todos if t['status'] == 'pending']
    completed = [t for t in todos if t['status'] == 'completed']

    # Don't show completed in summary (can be many)
    active_todos = in_progress + pending

    summary = f"📋 Loaded {len(active_todos)} active tasks from previous session:\n\n"

    if in_progress:
        summary += "🔄 In Progress:\n"
        for task in in_progress[:5]:  # Show max 5
            summary += f"  • {task['content']}\n"
        if len(in_progress) > 5:
            summary += f"  ... and {len(in_progress) - 5} more\n"
        summary += "\n"

    if pending:
        summary += "📝 Pending:\n"
        for task in pending[:5]:  # Show max 5
            summary += f"  • {task['content']}\n"
        if len(pending) > 5:
            summary += f"  ... and {len(pending) - 5} more\n"

    if completed:
        summary += f"\n✅ {len(completed)} completed tasks archived\n"

    summary += f"\nType '/todo' to see all tasks or manage them with TodoWrite."

    return summary

def main():
    """Main execution for SessionStart hook."""

    # Read hook input from stdin
    try:
        stdin_data = sys.stdin.read()
        hook_input = json.loads(stdin_data) if stdin_data.strip() else {}
    except Exception as e:
        hook_input = {}
        log(f"WARNING: Failed to parse hook input: {e}")

    session_id = hook_input.get("session_id", "unknown")
    log(f"SessionStart hook triggered (session: {session_id})")

    # Parse todo.md
    todos = parse_todo_file()

    if not todos:
        log("No todos loaded")
        output = {
            "continue": True,
            "suppressOutput": True
        }
    else:
        # Format summary message
        summary = format_todo_summary(todos)
        log(f"Loaded {len(todos)} todos, showing summary to user")

        # Output for Claude Code
        output = {
            "continue": True,
            "suppressOutput": False,
            "systemMessage": summary
        }

    print(json.dumps(output))
    sys.exit(0)

if __name__ == "__main__":
    main()
