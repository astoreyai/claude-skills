#!/usr/bin/env python3
"""
session_end.py - Main SessionEnd hook for session-synthesizer skill.
Unified hook that replaces memory-keeper, todo-keeper, and vault-keeper.
"""

import json
import sys
from pathlib import Path

# Add skill directory to path for imports
SKILL_DIR = Path(__file__).parent
sys.path.insert(0, str(SKILL_DIR))

from synthesizer import SessionSynthesizer


def main():
    """Main execution for SessionEnd hook."""

    # Read hook input from stdin
    try:
        stdin_data = sys.stdin.read()
        hook_input = json.loads(stdin_data) if stdin_data.strip() else {}
    except Exception as e:
        hook_input = {}

    # Extract session data
    session_id = hook_input.get("session_id", "unknown")
    cwd = hook_input.get("cwd", str(Path.home()))
    todos = hook_input.get("todos", [])

    # Run synthesizer
    try:
        synthesizer = SessionSynthesizer(session_id, cwd, todos)
        output = synthesizer.run()
    except Exception as e:
        # Fail gracefully - don't block session end
        output = {
            "continue": True,
            "suppressOutput": False,
            "systemMessage": f"Session synthesis error: {str(e)[:100]}"
        }

    # Output result
    print(json.dumps(output))
    sys.exit(0)


if __name__ == "__main__":
    main()
