---
name: session-synthesizer
description: Comprehensive SessionEnd hook that syncs and synthesizes all daily completions, notes, todos, and conversation data into unified daily notes and knowledge bases.
version: 1.0.0
author: Aaron Storey
---

# Session Synthesizer

Unified SessionEnd hook that consolidates memory-keeper, todo-keeper, and vault-keeper into a single comprehensive synthesis system.

## Features

1. **Extract** - Gather session data
   - Todos (completed, in progress, pending)
   - Git status across active projects
   - Working directory context
   - Session metadata

2. **Synthesize** - Generate summaries
   - Session summary for daily note
   - Update CLAUDE.md session notes
   - Update project dashboards if significant

3. **Sync** - Persist and synchronize
   - Save todos to Obsidian vault
   - Trigger obsidian-sync (Google Drive)
   - Warn on uncommitted git changes

4. **Output** - Report to user
   - Brief session summary
   - Sync status
   - Any warnings

## Configuration

Replaces these hooks in settings.json:
- `memory-keeper/auto_update.py`
- `todo-keeper/save_todos.py`
- `vault-keeper/auto_cleanup.py`

## Usage

Automatically triggered on SessionEnd. No manual invocation needed.

## Files

- `session_end.py` - Main hook entry point
- `synthesizer.py` - Core synthesis logic
