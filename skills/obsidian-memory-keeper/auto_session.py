#!/usr/bin/env python3
"""
Auto-session script for obsidian-memory-keeper skill.
Triggered by SessionEnd hook to create/update daily notes automatically.
"""

import json
import sys
import subprocess
from pathlib import Path
from datetime import datetime
import os

def get_git_status(cwd):
    """Get git status summary from working directory."""
    try:
        result = subprocess.run(
            ['git', 'status', '--short'],
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            files = result.stdout.strip().split('\n')
            return [f.strip() for f in files if f.strip()]
        return []
    except Exception:
        return []

def get_git_diff_stats(cwd):
    """Get git diff statistics."""
    try:
        result = subprocess.run(
            ['git', 'diff', '--stat'],
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            return result.stdout.strip()
        return ""
    except Exception:
        return ""

def get_project_name(cwd):
    """Extract project name from working directory."""
    path = Path(cwd)

    # Check if it's in known project locations
    if 'projects' in path.parts:
        idx = path.parts.index('projects')
        if idx + 1 < len(path.parts):
            return path.parts[idx + 1]
    elif 'github' in path.parts:
        if 'astoreyai' in path.parts:
            idx = path.parts.index('astoreyai')
            if idx + 1 < len(path.parts):
                return path.parts[idx + 1]

    # Default to last directory name
    return path.name

def create_session_entry(session_id, cwd, git_status, git_diff):
    """Create a session entry for daily note."""
    session_time = datetime.now().strftime("%H:%M")
    project_name = get_project_name(cwd)

    entry = f"\n### Session: {session_time}\n"
    entry += f"**Project**: `{cwd}`\n"
    entry += f"**Session ID**: {session_id}\n"
    entry += "\n**Activity**:\n"

    if git_status:
        entry += f"- Modified {len(git_status)} files\n"
    else:
        entry += "- Claude Code session completed\n"

    if git_diff:
        entry += "\n**Changes**:\n```\n"
        entry += git_diff[:500]  # Limit to 500 chars
        if len(git_diff) > 500:
            entry += "\n... (truncated)"
        entry += "\n```\n"

    entry += f"\n**Next**: Continue work on {project_name}\n"

    return entry

def append_to_daily_note(vault_path, entry):
    """Append session entry to today's daily note."""
    today = datetime.now().strftime("%Y-%m-%d")
    daily_note = vault_path / "Daily" / f"{today}.md"

    # Ensure Daily directory exists
    daily_note.parent.mkdir(parents=True, exist_ok=True)

    # Create daily note from template if doesn't exist
    if not daily_note.exists():
        template = vault_path / "Templates" / "Daily-Note.md"
        if template.exists():
            with open(template, 'r') as f:
                content = f.read()
            # Replace date placeholder
            content = content.replace("YYYY-MM-DD", today)
            year, month, _ = today.split('-')
            content = content.replace("#YYYY", f"#{year}")
            content = content.replace("#MM", f"#{month}")
            with open(daily_note, 'w') as f:
                f.write(content)
        else:
            # Create minimal daily note
            with open(daily_note, 'w') as f:
                f.write(f"# {today}\n\n## Session Notes\n")

    # Append session entry
    with open(daily_note, 'a') as f:
        f.write(entry)

    return daily_note

def main():
    """Main execution function for SessionEnd hook."""

    # Read hook input from stdin
    try:
        stdin_data = sys.stdin.read()
        hook_input = json.loads(stdin_data) if stdin_data.strip() else {}
    except Exception as e:
        hook_input = {}

    session_id = hook_input.get("session_id", "unknown")
    cwd = hook_input.get("cwd", str(Path.home()))

    # Paths
    vault_path = Path.home() / "Documents" / "Obsidian" / "Aaron"
    log_file = Path.home() / ".claude" / "logs" / "obsidian-memory-keeper.log"

    # Ensure logs directory exists
    log_file.parent.mkdir(parents=True, exist_ok=True)

    # Log execution
    timestamp = datetime.now().isoformat()
    with open(log_file, "a") as f:
        f.write(f"\n[{timestamp}] SessionEnd hook triggered\n")
        f.write(f"  Session ID: {session_id}\n")
        f.write(f"  Working dir: {cwd}\n")

    # Check if vault exists
    if not vault_path.exists():
        error_msg = f"Aaron vault not found at {vault_path}"
        try:
            with open(log_file, "a") as f:
                f.write(f"  ERROR: {error_msg}\n")
        except:
            pass

        output = {
            "continue": True,
            "suppressOutput": True,
            "systemMessage": f"Obsidian keeper: {error_msg}"
        }
        print(json.dumps(output))
        sys.exit(0)

    # Get git status if in git repo
    git_status = get_git_status(cwd)
    git_diff = get_git_diff_stats(cwd) if git_status else ""

    # Create session entry
    entry = create_session_entry(session_id, cwd, git_status, git_diff)

    # Append to daily note
    try:
        daily_note = append_to_daily_note(vault_path, entry)

        with open(log_file, "a") as f:
            f.write(f"  Appended session to {daily_note}\n")
            if git_status:
                f.write(f"  Files modified: {len(git_status)}\n")

        message = f"Daily note updated: {daily_note.name}"
    except Exception as e:
        with open(log_file, "a") as f:
            f.write(f"  ERROR: {str(e)}\n")
        message = f"Daily note update failed: {str(e)}"

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
