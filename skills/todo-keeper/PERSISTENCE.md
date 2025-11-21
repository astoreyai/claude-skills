# Todo Persistence - Implementation Guide

## Overview

The todo-keeper skill now includes **automatic todo persistence** across Claude Code sessions using SessionStart and SessionEnd hooks.

## How It Works

### SessionEnd Hook (Save)
When you exit Claude Code:
1. `save_todos.py` captures all tasks from TodoWrite
2. Converts to markdown format
3. Saves to `~/Documents/Obsidian/Aaron/todo.md`
4. Logs operation to `~/.claude/logs/todo-keeper.log`

### SessionStart Hook (Load)
When you start Claude Code:
1. `load_todos.py` reads `~/Documents/Obsidian/Aaron/todo.md`
2. Parses tasks by status (in_progress, pending, completed)
3. Shows summary message with active tasks
4. Logs operation

## File Format

**Location**: `~/Documents/Obsidian/Aaron/todo.md`

**Format**:
```markdown
---
type: todo-list
last_updated: 2025-11-21T13:24:51.527605
---

# Active Tasks

**Total**: 4 tasks (2 completed, 1 in progress, 1 pending)

## 🔄 In Progress

- [🔄] Task description

## 📝 Pending

- [ ] Task description

## ✅ Completed

- [x] Task description

---

*Last saved: 2025-11-21 13:24:51*
```

## Configuration

### Hooks Already Configured

File: `~/.claude/settings.json`

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/skills/todo-keeper/load_todos.py",
            "timeout": 10
          }
        ]
      }
    ],
    "SessionEnd": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/skills/memory-keeper/auto_update.py",
            "timeout": 30
          },
          {
            "type": "command",
            "command": "python3 ~/.claude/skills/todo-keeper/save_todos.py",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

### Files Created

```
~/.claude/skills/todo-keeper/
├── save_todos.py       # SessionEnd hook (persists tasks)
├── load_todos.py       # SessionStart hook (loads tasks)
├── SKILL.md            # Skill specification
├── README.md           # Usage guide
└── PERSISTENCE.md      # This file

~/Documents/Obsidian/Aaron/
└── todo.md             # Persisted tasks (auto-generated)

~/.claude/logs/
└── todo-keeper.log     # Operation logs
```

## Usage

### Automatic (Hooks)

**No manual action needed!**

- When you **exit** Claude Code → Tasks automatically saved to `todo.md`
- When you **start** Claude Code → Tasks automatically loaded and summarized

### What You'll See

**On Session Start**:
```
📋 Loaded 2 active tasks from previous session:

🔄 In Progress:
  • Test todo persistence across sessions

📝 Pending:
  • Update todo-keeper documentation

✅ 2 completed tasks archived

Type '/todo' to see all tasks or manage them with TodoWrite.
```

### Manual Operations

**View persisted tasks**:
```bash
cat ~/Documents/Obsidian/Aaron/todo.md
```

**View logs**:
```bash
tail ~/.claude/logs/todo-keeper.log
```

**Test save manually**:
```bash
echo '{"session_id":"test","todos":[...]}' | python3 ~/.claude/skills/todo-keeper/save_todos.py
```

**Test load manually**:
```bash
echo '{"session_id":"test"}' | python3 ~/.claude/skills/todo-keeper/load_todos.py
```

## Integration with Obsidian

### Viewing in Obsidian

1. Open Obsidian
2. Navigate to vault: `Aaron`
3. Open file: `todo.md` (in root directory)
4. See all persisted tasks with status indicators

### Editing in Obsidian

You can **manually edit** `todo.md` in Obsidian:
- Add new tasks: `- [ ] New task description`
- Mark complete: Change `[ ]` to `[x]`
- Mark in progress: Change `[ ]` to `[🔄]`

**Note**: Manual edits will be loaded on next SessionStart, but will be **overwritten** on next SessionEnd. For best results, use TodoWrite during sessions and let hooks manage persistence.

## Sync with Daily Notes

The todo.md file is **separate** from daily notes:

- **todo.md**: Cross-session task persistence (all active tasks)
- **Daily notes**: Day-specific tasks and session logs

You can sync between them using `/todo sync` command (when implemented).

## Troubleshooting

### Tasks Not Persisting

1. **Check hooks are registered**:
   ```bash
   cat ~/.claude/settings.json | grep -A 5 SessionEnd
   ```

2. **Check scripts are executable**:
   ```bash
   ls -l ~/.claude/skills/todo-keeper/*.py
   ```
   Should show `-rwxr-xr-x` permissions

3. **Check logs**:
   ```bash
   tail -20 ~/.claude/logs/todo-keeper.log
   ```

### Tasks Not Loading on Start

1. **Check todo.md exists**:
   ```bash
   ls -l ~/Documents/Obsidian/Aaron/todo.md
   ```

2. **Check file format**:
   Should have `## 🔄 In Progress`, `## 📝 Pending`, etc.

3. **Run load script manually**:
   ```bash
   echo '{"session_id":"manual-test"}' | python3 ~/.claude/skills/todo-keeper/load_todos.py
   ```

### Hooks Not Running

1. **Verify Claude Code hook support**:
   Hooks require Claude Code CLI version with hook support

2. **Check timeout**:
   Default is 10s for todo hooks, 30s for memory-keeper
   Increase if scripts are slow

3. **Check Python version**:
   ```bash
   python3 --version  # Should be 3.11+
   ```

## Best Practices

1. **Use TodoWrite during sessions** - Let hooks handle persistence
2. **Don't manually edit todo.md** while Claude Code is running
3. **Review todo.md in Obsidian** between sessions
4. **Check logs regularly** to ensure hooks are working
5. **Keep completed tasks short-term** - Archive old completed tasks periodically

## Advanced: Archiving Old Completed Tasks

To prevent todo.md from growing too large:

```bash
# Create archive directory
mkdir -p ~/Documents/Obsidian/Aaron/Archive/todos/

# Move completed tasks older than 7 days
# (Manual process - can be automated with script)
```

Future enhancement: Auto-archive completed tasks older than N days.

## Logs

All operations logged to: `~/.claude/logs/todo-keeper.log`

**Log format**:
```
[2025-11-21T13:24:51.527535] SessionEnd hook triggered (session: abc123)
[2025-11-21T13:24:51.527591] Saving 4 tasks
[2025-11-21T13:24:51.527640] Saved 4 tasks to /home/aaron/Documents/Obsidian/Aaron/todo.md
[2025-11-21T13:24:57.109983] SessionStart hook triggered (session: def456)
[2025-11-21T13:24:57.110092] Parsed 4 tasks from todo.md
[2025-11-21T13:24:57.110114] Loaded 4 todos, showing summary to user
```

## Version

**Version**: 1.0.0
**Created**: 2025-11-21
**Hook Support**: SessionStart, SessionEnd
**File Location**: `~/Documents/Obsidian/Aaron/todo.md`
