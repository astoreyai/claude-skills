#!/usr/bin/env python3
"""
SessionEnd hook to persist TodoWrite tasks to Obsidian vault.
Saves tasks to ~/Documents/Obsidian/Aaron/todo.md for cross-session persistence.
"""

import json
import sys
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

def save_todos_to_file(todos):
    """
    Save todos to todo.md in Obsidian vault.

    Format:
    # Active Tasks

    ## In Progress
    - [🔄] Task description (activeForm)

    ## Pending
    - [ ] Task description

    ## Completed
    - [x] Task description

    Last updated: YYYY-MM-DD HH:MM:SS
    """

    # Ensure vault exists
    if not VAULT_PATH.exists():
        log(f"ERROR: Vault not found at {VAULT_PATH}")
        return False

    # Group tasks by status
    in_progress = [t for t in todos if t.get('status') == 'in_progress']
    pending = [t for t in todos if t.get('status') == 'pending']
    completed = [t for t in todos if t.get('status') == 'completed']

    # Build markdown content
    content = f"""---
type: todo-list
last_updated: {datetime.now().isoformat()}
---

# Active Tasks

**Total**: {len(todos)} tasks ({len(completed)} completed, {len(in_progress)} in progress, {len(pending)} pending)

"""

    if in_progress:
        content += "## 🔄 In Progress\n\n"
        for task in in_progress:
            content += f"- [🔄] {task['content']}\n"
        content += "\n"

    if pending:
        content += "## 📝 Pending\n\n"
        for task in pending:
            content += f"- [ ] {task['content']}\n"
        content += "\n"

    if completed:
        content += "## ✅ Completed\n\n"
        for task in completed:
            content += f"- [x] {task['content']}\n"
        content += "\n"

    content += f"---\n\n*Last saved: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n"

    # Write to file
    try:
        with open(TODO_FILE, 'w') as f:
            f.write(content)
        log(f"Saved {len(todos)} tasks to {TODO_FILE}")
        return True
    except Exception as e:
        log(f"ERROR: Failed to save todos: {e}")
        return False

def main():
    """Main execution for SessionEnd hook."""

    # Read hook input from stdin
    try:
        stdin_data = sys.stdin.read()
        hook_input = json.loads(stdin_data) if stdin_data.strip() else {}
    except Exception as e:
        hook_input = {}
        log(f"WARNING: Failed to parse hook input: {e}")

    session_id = hook_input.get("session_id", "unknown")
    log(f"SessionEnd hook triggered (session: {session_id})")

    # Get todos from hook input
    todos = hook_input.get("todos", [])

    if not todos:
        log("No todos to save (empty list)")
        # Still write empty file to clear previous tasks
        save_todos_to_file([])
    else:
        log(f"Saving {len(todos)} tasks")
        save_todos_to_file(todos)

    # Output for Claude Code
    output = {
        "continue": True,
        "suppressOutput": True,
        "systemMessage": f"Saved {len(todos)} tasks to todo.md"
    }
    print(json.dumps(output))
    sys.exit(0)

if __name__ == "__main__":
    main()
