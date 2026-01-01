#!/usr/bin/env python3
"""
World Weaver SessionStart Hook

Loads relevant memory context at the start of each Claude Code session.
Fetches recent episodes, related entities, and applicable skills based
on the current working directory and project context.

Output is injected into the session as context for Claude.
"""

import json
import os
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any


# Configuration (can be overridden by environment variables)
CONFIG = {
    "max_episodes": int(os.environ.get("WW_MAX_EPISODES", "10")),
    "max_entities": int(os.environ.get("WW_MAX_ENTITIES", "15")),
    "max_skills": int(os.environ.get("WW_MAX_SKILLS", "5")),
    "lookback_days": int(os.environ.get("WW_LOOKBACK_DAYS", "7")),
    "mcp_server": os.environ.get("WW_MCP_SERVER", "ww-memory"),
}


def get_project_context() -> dict[str, str]:
    """Extract project context from current environment."""
    cwd = os.getcwd()
    project = os.path.basename(cwd)

    # Try to get project from git
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            cwd=cwd,
            timeout=5
        )
        if result.returncode == 0:
            project = os.path.basename(result.stdout.strip())
    except Exception:
        pass

    # Try to get git branch
    branch = None
    try:
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True,
            text=True,
            cwd=cwd,
            timeout=5
        )
        if result.returncode == 0:
            branch = result.stdout.strip()
    except Exception:
        pass

    return {
        "cwd": cwd,
        "project": project,
        "branch": branch,
    }


def call_mcp_tool(tool: str, params: dict[str, Any]) -> dict[str, Any] | None:
    """
    Call a World Weaver MCP tool.

    This uses the MCP protocol to communicate with the ww-memory server.
    For hooks, we use a simplified approach via environment inspection.
    """
    # In a real implementation, this would use the MCP client protocol
    # For now, we'll try to call the Python API directly if available
    try:
        # Try direct Python import (works if ww is installed)
        from ww.memory.episodic import EpisodicMemory
        from ww.memory.semantic import SemanticMemory
        from ww.memory.procedural import ProceduralMemory

        session_id = os.environ.get("WW_SESSION_ID", "default")

        if tool == "recall_episodes":
            memory = EpisodicMemory(session_id)
            # Note: This is synchronous wrapper for hook use
            import asyncio
            loop = asyncio.new_event_loop()
            try:
                loop.run_until_complete(memory.initialize())
                results = loop.run_until_complete(
                    memory.recall(
                        query=params.get("query", ""),
                        limit=params.get("limit", 10),
                    )
                )
                return {"episodes": [r.item.__dict__ for r in results]}
            finally:
                loop.run_until_complete(memory.close())
                loop.close()

        elif tool == "semantic_recall":
            memory = SemanticMemory(session_id)
            import asyncio
            loop = asyncio.new_event_loop()
            try:
                loop.run_until_complete(memory.initialize())
                results = loop.run_until_complete(
                    memory.recall(
                        query=params.get("query", ""),
                        limit=params.get("limit", 10),
                    )
                )
                return {"entities": [r.item.__dict__ for r in results]}
            finally:
                loop.run_until_complete(memory.close())
                loop.close()

        elif tool == "recall_skill":
            memory = ProceduralMemory(session_id)
            import asyncio
            loop = asyncio.new_event_loop()
            try:
                loop.run_until_complete(memory.initialize())
                results = loop.run_until_complete(
                    memory.recall(
                        query=params.get("query", ""),
                        limit=params.get("limit", 5),
                    )
                )
                return {"skills": [r.item.__dict__ for r in results]}
            finally:
                loop.run_until_complete(memory.close())
                loop.close()

    except ImportError:
        # WW not installed, return empty
        return None
    except Exception as e:
        # Log error but don't fail the hook
        print(f"WW Hook Warning: {e}", file=sys.stderr)
        return None

    return None


def format_episodes(episodes: list[dict]) -> str:
    """Format episodes for display."""
    if not episodes:
        return "_No recent episodes found_"

    lines = []
    for ep in episodes[:CONFIG["max_episodes"]]:
        date = ep.get("timestamp", "")[:10] if ep.get("timestamp") else "Unknown"
        content = ep.get("content", "")[:100]
        outcome = ep.get("outcome", "neutral")
        outcome_icon = {"success": "+", "failure": "-", "partial": "~"}.get(outcome, " ")
        lines.append(f"- [{outcome_icon}] **{date}**: {content}...")

    return "\n".join(lines)


def format_entities(entities: list[dict]) -> str:
    """Format entities for display."""
    if not entities:
        return "_No related entities found_"

    lines = []
    for ent in entities[:CONFIG["max_entities"]]:
        name = ent.get("name", "Unknown")
        etype = ent.get("entity_type", "CONCEPT")
        summary = ent.get("summary", "")[:80]
        lines.append(f"- **{name}** ({etype}): {summary}")

    return "\n".join(lines)


def format_skills(skills: list[dict]) -> str:
    """Format skills for display."""
    if not skills:
        return "_No applicable skills found_"

    lines = []
    for skill in skills[:CONFIG["max_skills"]]:
        name = skill.get("name", "Unknown")
        desc = skill.get("description", "")[:60]
        lines.append(f"- **{name}**: {desc}")

    return "\n".join(lines)


def get_memory_context() -> str:
    """Fetch and format memory context from World Weaver."""
    context = get_project_context()
    project = context["project"]
    cwd = context["cwd"]

    # Calculate lookback date
    lookback = datetime.now() - timedelta(days=CONFIG["lookback_days"])

    # Fetch memories
    episodes_result = call_mcp_tool("recall_episodes", {
        "query": f"working on {project}",
        "limit": CONFIG["max_episodes"],
    })

    entities_result = call_mcp_tool("semantic_recall", {
        "query": project,
        "limit": CONFIG["max_entities"],
    })

    skills_result = call_mcp_tool("recall_skill", {
        "query": f"how to work with {project}",
        "limit": CONFIG["max_skills"],
    })

    # Extract results
    episodes = episodes_result.get("episodes", []) if episodes_result else []
    entities = entities_result.get("entities", []) if entities_result else []
    skills = skills_result.get("skills", []) if skills_result else []

    # Check if we have any memories
    if not episodes and not entities and not skills:
        return ""  # No context to inject

    # Format output
    output = f"""
## World Weaver Memory Context

**Project**: {project}
**Directory**: {cwd}
**Lookback**: {CONFIG['lookback_days']} days

### Recent Episodes ({len(episodes)} found)
{format_episodes(episodes)}

### Related Knowledge ({len(entities)} entities)
{format_entities(entities)}

### Applicable Skills ({len(skills)} found)
{format_skills(skills)}

---
"""
    return output.strip()


def main():
    """Main hook entry point."""
    try:
        context = get_memory_context()
        if context:
            print(context)
        else:
            # Silent if no memories - don't clutter output
            pass
    except Exception as e:
        # Hooks should not fail hard - log and continue
        print(f"WW SessionStart Hook Error: {e}", file=sys.stderr)
        sys.exit(0)  # Exit cleanly even on error


if __name__ == "__main__":
    main()
