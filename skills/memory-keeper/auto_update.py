#!/usr/bin/env python3
"""
Auto-update script for memory-keeper skill.
Triggered by SessionEnd hook to update CLAUDE.md automatically.
"""

import json
import sys
import subprocess
from pathlib import Path
from datetime import datetime
import os

def main():
    """Main execution function for SessionEnd hook."""

    # Read hook input from stdin
    try:
        hook_input = json.loads(sys.stdin.read())
    except:
        hook_input = {}

    session_id = hook_input.get("session_id", "unknown")
    cwd = hook_input.get("cwd", str(Path.home()))

    # Paths
    claude_md = Path.home() / ".claude" / "CLAUDE.md"
    log_file = Path.home() / ".claude" / "logs" / "memory-keeper.log"

    # Ensure logs directory exists
    log_file.parent.mkdir(parents=True, exist_ok=True)

    # Log execution
    timestamp = datetime.now().isoformat()
    with open(log_file, "a") as f:
        f.write(f"\n[{timestamp}] SessionEnd hook triggered\n")
        f.write(f"  Session ID: {session_id}\n")
        f.write(f"  Working dir: {cwd}\n")

    # Check if CLAUDE.md exists
    if not claude_md.exists():
        error_msg = f"CLAUDE.md not found at {claude_md}"
        with open(log_file, "a") as f:
            f.write(f"  ERROR: {error_msg}\n")

        output = {
            "continue": True,
            "suppressOutput": True,
            "systemMessage": f"Memory keeper: {error_msg}"
        }
        print(json.dumps(output))
        sys.exit(1)

    # Get current timestamp for Last Updated field
    today = datetime.now().strftime("%Y-%m-%d")

    # Read current CLAUDE.md
    with open(claude_md, "r") as f:
        content = f.read()

    # Check if Last Updated needs updating
    last_updated_line = None
    for line in content.split('\n'):
        if line.startswith("**Last Updated**:"):
            last_updated_line = line
            break

    # Only update if needed (not already today)
    if last_updated_line and today not in last_updated_line:
        # Update Last Updated timestamp
        new_content = content.replace(
            last_updated_line,
            f"**Last Updated**: {today} | **System**: Debian Linux (6.1.0-41-amd64)"
        )

        # Write back
        with open(claude_md, "w") as f:
            f.write(new_content)

        with open(log_file, "a") as f:
            f.write(f"  Updated Last Updated to {today}\n")

        message = f"Memory updated: Last Updated → {today}"
    else:
        message = f"Memory already current ({today})"
        with open(log_file, "a") as f:
            f.write(f"  No update needed, already current\n")

    # Successful completion
    output = {
        "continue": True,
        "suppressOutput": False,
        "systemMessage": message
    }
    print(json.dumps(output))
    sys.exit(0)


if __name__ == "__main__":
    main()
