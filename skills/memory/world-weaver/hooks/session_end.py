#!/usr/bin/env python3
"""
World Weaver SessionEnd Hook

Stores session summary as an episode in World Weaver.
Extracts completed tasks, git activity, and key decisions
to create an autobiographical memory of the session.

This hook integrates with existing session-synthesizer if present.
"""

import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any
from uuid import uuid4


# Configuration
CONFIG = {
    "auto_store": os.environ.get("WW_AUTO_STORE", "true").lower() == "true",
    "extract_entities": os.environ.get("WW_EXTRACT_ENTITIES", "true").lower() == "true",
    "min_duration_minutes": int(os.environ.get("WW_MIN_DURATION", "5")),
    "session_id": os.environ.get("WW_SESSION_ID", "default"),
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

    return {
        "cwd": cwd,
        "project": project,
    }


def get_git_activity() -> dict[str, Any]:
    """Get git activity from the session."""
    activity = {
        "commits": [],
        "modified_files": [],
        "branch": None,
    }

    cwd = os.getcwd()

    # Get current branch
    try:
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True,
            text=True,
            cwd=cwd,
            timeout=5
        )
        if result.returncode == 0:
            activity["branch"] = result.stdout.strip()
    except Exception:
        pass

    # Get recent commits (last hour)
    try:
        result = subprocess.run(
            ["git", "log", "--oneline", "--since=1.hour.ago"],
            capture_output=True,
            text=True,
            cwd=cwd,
            timeout=5
        )
        if result.returncode == 0 and result.stdout.strip():
            activity["commits"] = result.stdout.strip().split("\n")[:5]
    except Exception:
        pass

    # Get modified files
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True,
            cwd=cwd,
            timeout=5
        )
        if result.returncode == 0 and result.stdout.strip():
            lines = result.stdout.strip().split("\n")
            activity["modified_files"] = [
                line[3:] for line in lines[:10]  # Limit to 10 files
            ]
    except Exception:
        pass

    return activity


def get_todo_summary() -> dict[str, Any]:
    """Get todo/task completion summary from this session."""
    # This would integrate with TodoWrite state if accessible
    # For now, return placeholder
    return {
        "completed": 0,
        "in_progress": 0,
        "pending": 0,
        "items": []
    }


def determine_outcome(git_activity: dict, todos: dict) -> str:
    """Determine session outcome based on activity."""
    # Has commits = likely success
    if git_activity.get("commits"):
        return "success"

    # Has completed todos = success
    if todos.get("completed", 0) > 0:
        return "success"

    # Has work in progress
    if git_activity.get("modified_files") or todos.get("in_progress", 0) > 0:
        return "partial"

    # Minimal activity
    return "neutral"


def calculate_importance(git_activity: dict, todos: dict) -> float:
    """Calculate emotional valence (importance) of session."""
    score = 0.3  # Base score

    # Commits add importance
    commit_count = len(git_activity.get("commits", []))
    score += min(commit_count * 0.1, 0.3)

    # Completed todos add importance
    completed = todos.get("completed", 0)
    score += min(completed * 0.1, 0.3)

    # Cap at 0.9 (1.0 reserved for explicit --important)
    return min(score, 0.9)


def format_session_content(
    context: dict,
    git_activity: dict,
    todos: dict
) -> str:
    """Format session data into episode content."""
    parts = []

    # Project and time
    parts.append(f"Session in {context['project']} project.")

    # Git activity
    commits = git_activity.get("commits", [])
    if commits:
        parts.append(f"Commits: {', '.join(commits[:3])}")

    modified = git_activity.get("modified_files", [])
    if modified:
        parts.append(f"Modified files: {', '.join(modified[:5])}")

    # Todos
    if todos.get("completed", 0) > 0:
        parts.append(f"Completed {todos['completed']} tasks.")

    if todos.get("items"):
        completed_items = [t for t in todos["items"] if t.get("status") == "completed"]
        if completed_items:
            parts.append(f"Tasks: {', '.join(t['content'] for t in completed_items[:3])}")

    # If nothing captured, note that
    if len(parts) == 1:
        parts.append("General work session.")

    return " ".join(parts)


def extract_entities_from_content(content: str) -> list[dict]:
    """
    Extract potential entities from session content.

    This is a simple rule-based extraction. For better results,
    use LLM-based extraction in the main conversation.
    """
    entities = []

    # Look for capitalized words that might be entities
    words = content.split()
    for i, word in enumerate(words):
        # Skip common words
        if word.lower() in ["the", "a", "an", "in", "on", "at", "to", "for", "of", "and", "or"]:
            continue

        # Look for potential project/tool names
        if word[0].isupper() and len(word) > 2:
            # Check if it's a file extension or path
            if "." in word or "/" in word:
                continue

            entities.append({
                "name": word.strip(".,;:!?"),
                "entity_type": "CONCEPT",
                "summary": f"Mentioned in session: {word}",
            })

    # Deduplicate by name
    seen = set()
    unique_entities = []
    for ent in entities:
        if ent["name"] not in seen:
            seen.add(ent["name"])
            unique_entities.append(ent)

    return unique_entities[:5]  # Limit to 5 entities


def store_episode(content: str, outcome: str, valence: float, context: dict) -> dict | None:
    """Store episode in World Weaver."""
    try:
        from ww.memory.episodic import EpisodicMemory
        from ww.core.types import Episode, Outcome
        import asyncio

        session_id = CONFIG["session_id"]
        memory = EpisodicMemory(session_id)

        # Map outcome string to enum
        outcome_map = {
            "success": Outcome.SUCCESS,
            "failure": Outcome.FAILURE,
            "partial": Outcome.PARTIAL,
            "neutral": Outcome.NEUTRAL,
        }

        episode = Episode(
            id=uuid4(),
            session_id=session_id,
            content=content,
            timestamp=datetime.now(),
            outcome=outcome_map.get(outcome, Outcome.NEUTRAL),
            emotional_valence=valence,
            context={
                "project": context.get("project"),
                "working_directory": context.get("cwd"),
                "source": "session_end_hook",
            }
        )

        loop = asyncio.new_event_loop()
        try:
            loop.run_until_complete(memory.initialize())
            result = loop.run_until_complete(memory.store(episode))
            return {"episode_id": str(result.id)}
        finally:
            loop.run_until_complete(memory.close())
            loop.close()

    except ImportError:
        return None
    except Exception as e:
        print(f"WW Store Error: {e}", file=sys.stderr)
        return None


def store_entities(entities: list[dict]) -> list[dict]:
    """Store extracted entities in World Weaver."""
    if not entities:
        return []

    try:
        from ww.memory.semantic import SemanticMemory
        from ww.core.types import Entity, EntityType
        import asyncio

        session_id = CONFIG["session_id"]
        memory = SemanticMemory(session_id)

        stored = []
        loop = asyncio.new_event_loop()
        try:
            loop.run_until_complete(memory.initialize())

            for ent_data in entities:
                try:
                    entity = Entity(
                        id=uuid4(),
                        name=ent_data["name"],
                        entity_type=EntityType.CONCEPT,
                        summary=ent_data.get("summary", ""),
                    )
                    result = loop.run_until_complete(memory.store(entity))
                    stored.append({"entity_id": str(result.id), "name": ent_data["name"]})
                except Exception:
                    # Skip entities that fail (may already exist)
                    pass

            return stored
        finally:
            loop.run_until_complete(memory.close())
            loop.close()

    except ImportError:
        return []
    except Exception as e:
        print(f"WW Entity Store Error: {e}", file=sys.stderr)
        return []


def main():
    """Main hook entry point."""
    if not CONFIG["auto_store"]:
        return

    try:
        # Gather session data
        context = get_project_context()
        git_activity = get_git_activity()
        todos = get_todo_summary()

        # Determine outcome and importance
        outcome = determine_outcome(git_activity, todos)
        valence = calculate_importance(git_activity, todos)

        # Format content
        content = format_session_content(context, git_activity, todos)

        # Store episode
        result = store_episode(content, outcome, valence, context)

        if result:
            print(f"WW: Stored session episode ({outcome}, valence={valence:.1f})")

            # Extract and store entities
            if CONFIG["extract_entities"]:
                entities = extract_entities_from_content(content)
                if entities:
                    stored = store_entities(entities)
                    if stored:
                        print(f"WW: Stored {len(stored)} entities")
        else:
            # WW not available - silent
            pass

    except Exception as e:
        # Hooks should not fail hard
        print(f"WW SessionEnd Hook Error: {e}", file=sys.stderr)
        sys.exit(0)


if __name__ == "__main__":
    main()
