---
name: session-initializer
description: Comprehensive SessionStart hook showing PhD countdown, project status, uncommitted changes, and loaded todos.
version: 1.0.0
author: Aaron Storey
---

# Session Initializer

Unified SessionStart hook providing instant situational awareness.

## Features

1. **PhD Status** - Defense countdown, readiness score
2. **Project Status** - Uncommitted changes across active projects
3. **Todos** - Load persisted tasks from previous session

## Output Example

```
╭─ Session Start ─────────────────────────────╮
│ 📅 PhD Defense: 63 days (Jan 28, 2026)      │
│ 📊 Readiness: 85/100                        │
│ ⚠️  Uncommitted: xai, world-model           │
│ 📋 3 active tasks loaded                    │
╰─────────────────────────────────────────────╯
```

## Configuration

Replaces `todo-keeper/load_todos.py` in settings.json.
