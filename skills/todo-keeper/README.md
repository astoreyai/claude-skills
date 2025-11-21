# Todo Keeper - README

## Overview

The **todo-keeper** skill provides unified task management across Claude Code sessions, Obsidian daily notes, and CLAUDE.md project tracking.

## Features

- **Unified Task View**: See all tasks from TodoWrite, daily notes, and CLAUDE.md in one place
- **Smart Sync**: Bidirectional synchronization across all task sources
- **Context-Aware**: Suggests tasks based on current project/directory
- **Daily Note Integration**: Auto-sync with Obsidian daily notes
- **Project Linking**: Connect tasks to specific projects
- **Task Analytics**: Track completion rates and productivity metrics

## Installation

### Prerequisites

1. Obsidian vault at `~/Documents/Obsidian/Aaron/`
2. Daily note template with task sections
3. CLAUDE.md with project structure
4. Claude Code CLI

### Setup

**Already installed** at `~/.claude/skills/todo-keeper/`

Slash command registered at `~/.claude/commands/todo.md`

## Quick Start

### Basic Commands

```bash
# Show all tasks
/todo

# Add a task
/todo add Review PhD committee feedback

# Add task with project
/todo add Fix bug in scanner --project stoch

# Add high-priority task
/todo add Urgent deadline --priority high

# Complete a task
/todo complete 1

# Start working on a task
/todo start 2

# Show tasks for specific project
/todo project xai

# Sync all task sources
/todo sync
```

### Task Status Indicators

- `[ ]` - Pending
- `[🔄]` - In Progress
- `[x]` - Completed
- `[!]` - High Priority

## Usage Examples

### Example 1: Daily Workflow

**Morning**:
```bash
/todo
# Shows: pending tasks from yesterday + today's daily note
```

**During Work**:
```bash
/todo start 1
# Marks task #1 as in progress

# ... work on task ...

/todo complete 1
# Marks done, logs completion time
```

**Evening**:
```bash
/todo sync
# Syncs all completed tasks to daily note
```

### Example 2: Project-Based Tasks

**Add project task**:
```bash
/todo add Experiment 6.2 execution --project xai
```

**View project tasks**:
```bash
/todo project xai
# Shows: All xai-related tasks from all sources
```

**Update CLAUDE.md when done**:
Task completion automatically syncs to CLAUDE.md project section.

### Example 3: Priority Management

**High-priority tasks**:
```bash
/todo priority high
# Shows only high-priority tasks
```

**Add urgent task**:
```bash
/todo add Fix production bug ASAP --priority high
# Auto-detects "ASAP" as high priority
```

## Integration

### With Obsidian Daily Notes

**Daily note format**:
```markdown
## 🎯 Focus
- [ ] Task from /todo
- [🔄] In progress task
- [x] Completed task

## ✅ Completed
- Task finished at 14:30 (duration: 2h)
```

**Auto-sync**: Tasks automatically sync when you run `/daily-note`

### With CLAUDE.md

**Project tasks in CLAUDE.md**:
```markdown
### xai - PhD Dissertation
**Next Steps**:
- [ ] Experiment 6.2
- [ ] Performance benchmarking
```

Tasks from CLAUDE.md appear in `/todo` output with project context.

### With TodoWrite

The skill uses Claude's built-in TodoWrite tool for session-based tracking:
- Tasks added via `/todo add` appear in TodoWrite
- TodoWrite tasks sync to daily notes
- Bidirectional sync maintains consistency

## Task Sources

Tasks are aggregated from:

1. **Claude TodoWrite**: Session tasks (temporary)
2. **Daily Notes**: `~/Documents/Obsidian/Aaron/Daily/YYYY-MM-DD.md`
3. **CLAUDE.md**: Project-level tasks in "Next Steps" sections
4. **Code TODOs**: (optional) TODO comments in code files

## Advanced Features

### Context Detection

When working in a project directory:
```bash
cd ~/projects/stoch
/todo
# Automatically filters to stoch-related tasks
```

### Smart Suggestions

The skill detects phrases like:
- "need to" → suggests creating task
- "done with" → suggests marking complete
- "working on" → suggests marking in_progress

### Batch Operations

```bash
# Complete multiple tasks
/todo complete 1 2 3

# Add multiple tasks
/todo add Task 1; Task 2; Task 3
```

### Task Analytics

```bash
/todo stats
# Shows completion rates, time tracking, project breakdown
```

## Configuration

### Custom Priorities

Default priorities: `high`, `normal`, `low`

Keywords that trigger high priority:
- urgent, asap, critical, important, deadline

### Daily Note Template

Ensure your daily note template includes:
```markdown
## 🎯 Focus
- [ ]

## ✅ Completed
-
```

### SessionEnd Hook (Optional)

Auto-sync tasks at session end:

Add to `~/.claude/settings.json`:
```json
{
  "hooks": {
    "SessionEnd": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/skills/todo-keeper/auto_sync.py",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

## Troubleshooting

### Tasks Not Syncing

1. Check vault exists: `ls ~/Documents/Obsidian/Aaron/`
2. Check daily note exists: `ls ~/Documents/Obsidian/Aaron/Daily/$(date +%Y-%m-%d).md`
3. Run manual sync: `/todo sync`

### Duplicate Tasks

Run deduplication:
```bash
/todo sync --dedupe
```

### Task Missing from Daily Note

The task may only be in TodoWrite (session-based). Run:
```bash
/todo sync
```
to copy to daily note.

## Best Practices

1. **Use `/todo` at session start** to see pending tasks
2. **Mark tasks in_progress** when starting work
3. **Complete tasks promptly** for accurate time tracking
4. **Sync regularly** to keep all systems current
5. **Link to projects** for better organization
6. **Use priorities** for important/urgent tasks

## Files

```
~/.claude/skills/todo-keeper/
├── SKILL.md              # Full specification
├── README.md             # This file
├── auto_sync.py          # SessionEnd hook (optional)
└── USAGE.md              # Detailed examples

~/.claude/commands/
└── todo.md               # Slash command
```

## Related Skills

- **obsidian-memory-keeper**: Daily note management
- **memory-keeper**: CLAUDE.md updates
- Built-in **TodoWrite**: Session tracking

## Version

**Version**: 1.0.0
**Created**: 2025-11-21
**Integrated with**: obsidian-memory-keeper v1.0.0
