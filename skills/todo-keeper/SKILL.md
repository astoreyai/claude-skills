# Todo Keeper Skill

## Description

Comprehensive task management system that integrates Claude Code's TodoWrite tool with Obsidian daily notes and CLAUDE.md project tracking. Provides unified task visibility across all systems.

## Purpose

This skill enables seamless task management across multiple contexts:
- Session-based tasks (Claude TodoWrite)
- Daily task lists (Obsidian daily notes)
- Project-level tasks (CLAUDE.md)
- Code-linked tasks (specific files/functions)

## When to Invoke

**Auto-Invoke** (proactive):
- When user mentions "TODO", "task", "need to", "should"
- When completing significant work (suggest marking task done)
- At session start (show pending tasks)
- At session end (sync tasks to daily note)

**Manual Invoke** (explicit):
- User types `/todo` command
- User asks to "show tasks", "list todos", "what's pending"
- User wants to add, complete, or organize tasks

## Core Capabilities

### 1. Unified Task View

Aggregate tasks from multiple sources into single view:

**Sources**:
- Claude TodoWrite (session tasks)
- Today's daily note (`~/Documents/Obsidian/Aaron/Daily/YYYY-MM-DD.md`)
- CLAUDE.md project tasks
- Git commit TODOs in code

**Display Format**:
```
📋 All Tasks (8 total)

🔄 In Progress (2):
1. Create todo-keeper skill [obsidian-keeper project]
2. Review stoch beta1 performance [stoch project]

📝 Pending (5):
3. Add to claude-skills plugin
4. Test /todo command
5. Update documentation
6. Fix type errors in attribution methods [xai project]
7. Performance benchmarking [stoch project]

✅ Completed Today (1):
✓ Obsidian zip analysis

Progress: 12% (1/8)
```

### 2. Task Operations

**Add Task**:
```
/todo add Review PhD committee feedback --project xai --priority high
```
- Adds to TodoWrite
- Adds to daily note `## 🎯 Focus`
- Links to project in CLAUDE.md if specified
- Supports priority levels (high/normal/low)

**Complete Task**:
```
/todo complete 1
```
- Marks as completed in TodoWrite
- Checks off in daily note
- Logs completion time
- Archives to daily note `## ✅ Completed`

**Start Task**:
```
/todo start 3
```
- Marks as in_progress in TodoWrite
- Updates daily note status
- Logs start time

**Delete Task**:
```
/todo delete 5
```
- Removes from TodoWrite
- Removes from daily note
- Confirms deletion

### 3. Task Organization

**By Project**:
```
/todo project xai
```
Shows all tasks related to xai project:
- From CLAUDE.md Active Projects
- From daily notes tagged with project
- From TodoWrite with project context

**By Priority**:
```
/todo priority high
```
Shows high-priority tasks only.

**By Status**:
```
/todo pending
/todo in-progress
/todo completed
```

### 4. Daily Note Integration

**Auto-sync with Daily Notes**:

When daily note created (via `/daily-note`):
- Read `## 🎯 Focus` tasks
- Add to TodoWrite if not present
- Sync status bidirectionally

**Task Sections in Daily Note**:
```markdown
## 🎯 Focus
- [x] Completed task
- [ ] Pending task
- [🔄] In progress task

## ✅ Completed
- Task finished at 14:30
```

**Sync Process**:
1. Read daily note checkboxes
2. Compare with TodoWrite state
3. Update both to match
4. Preserve manual edits in daily note

### 5. CLAUDE.md Project Tasks

**Extract from CLAUDE.md**:

Read project sections like:
```markdown
### xai - PhD Dissertation
**Next Steps**:
- [ ] Experiment 6.2 with demographic analysis
- [ ] Performance benchmarking
```

**Sync to TodoWrite**:
- Add as tasks with project context
- Link back to CLAUDE.md section
- Update CLAUDE.md when completed

### 6. Context-Aware Task Suggestions

**Smart Detection**:

When working in a directory:
```bash
pwd: ~/projects/xai
```
- Suggest xai-related tasks
- Filter task list to xai project
- Auto-tag new tasks with "xai"

When conversation mentions:
- "need to" → suggest creating task
- "done with" → suggest marking complete
- "working on" → suggest marking in_progress

**Code Context**:

When editing file with TODO comments:
```python
# TODO: Implement SHAP attribution method
```
- Detect TODO in code
- Suggest adding to task list
- Link task to file:line

### 7. Task Analytics

**Daily Statistics**:
```
📊 Task Metrics (2025-11-21)

Completed: 3 tasks
Added: 5 tasks
Completion rate: 60%
Average time: 45 minutes/task
Most productive: Morning (2 tasks)

Projects:
- xai: 2 tasks (1 complete)
- stoch: 2 tasks (1 complete)
- obsidian: 1 task (1 complete)
```

**Weekly Summary**:
```
📊 Week 47 Task Summary

Total completed: 18 tasks
Total added: 22 tasks
Completion rate: 82%
Top project: xai (8 tasks)
Longest task: "Experiment 6.1" (3 days)
```

### 8. Task Sync

**Bidirectional Sync**:

```
/todo sync
```

Synchronizes:
1. TodoWrite ↔ Daily note
2. Daily note ↔ CLAUDE.md
3. Resolves conflicts (newest wins)
4. Reports changes

**Conflict Resolution**:
- Same task in multiple places → deduplicate
- Different status → use most recent
- User edits in daily note → preserve always

## Analysis Process

**Step 1: Gather All Tasks**

```python
def gather_tasks():
    tasks = []

    # 1. From TodoWrite (if active)
    todowrite_tasks = get_todowrite_state()

    # 2. From today's daily note
    daily_note = read_daily_note(today())
    daily_tasks = parse_checkboxes(daily_note)

    # 3. From CLAUDE.md projects
    claude_md = read_file("~/.claude/CLAUDE.md")
    project_tasks = parse_project_next_steps(claude_md)

    # 4. From code TODOs (optional)
    code_todos = scan_code_todos(pwd())

    return merge_tasks([
        todowrite_tasks,
        daily_tasks,
        project_tasks,
        code_todos
    ])
```

**Step 2: Deduplicate**

```python
def deduplicate_tasks(tasks):
    by_description = {}
    for task in tasks:
        # Normalize description
        desc = normalize(task.description)

        if desc in by_description:
            # Merge, keeping most complete info
            by_description[desc] = merge_task_info(
                by_description[desc],
                task
            )
        else:
            by_description[desc] = task

    return list(by_description.values())
```

**Step 3: Format Output**

```python
def format_task_list(tasks):
    # Group by status
    in_progress = [t for t in tasks if t.status == 'in_progress']
    pending = [t for t in tasks if t.status == 'pending']
    completed = [t for t in tasks if t.status == 'completed']

    output = f"📋 All Tasks ({len(tasks)} total)\n\n"

    if in_progress:
        output += "🔄 In Progress:\n"
        for i, task in enumerate(in_progress, 1):
            output += f"{i}. [🔄] {task.description}"
            if task.project:
                output += f" [{task.project}]"
            output += "\n"

    # ... similar for pending and completed
    return output
```

## Update Rules

### Safety Rules

**Never**:
- Delete tasks without confirmation
- Modify user-written descriptions
- Override manual edits in daily notes
- Lose task context when syncing

**Always**:
- Preserve task history
- Log all task state changes
- Sync bidirectionally
- Confirm destructive operations
- Maintain task links to projects/files

### Update Frequency

**Auto-sync**:
- At session start (read all sources)
- At session end (write to daily note)
- After `/todo` command execution
- After TodoWrite updates

**Manual sync**:
- `/todo sync` - full bidirectional sync
- `/daily-note` - sync with daily note
- `/update-memory` - sync with CLAUDE.md

## Examples

### Example 1: Show All Tasks

**Input**: `/todo`

**Actions**:
1. Read TodoWrite state
2. Read today's daily note
3. Read CLAUDE.md project tasks
4. Merge and deduplicate
5. Format output

**Output**:
```
📋 All Tasks (5 total, 40% complete)

🔄 In Progress (1):
1. Create todo-keeper skill [obsidian project]

📝 Pending (3):
2. Add to claude-skills plugin
3. Test /todo command
4. Update documentation

✅ Completed Today (1):
✓ Create /todo slash command

Next: Type `/todo start 2` to begin next task
```

### Example 2: Add Task with Project

**Input**: `/todo add Fix ATR calculation in indicators.py --project stoch --priority high`

**Actions**:
1. Parse command
2. Add to TodoWrite with priority
3. Add to daily note under `## 🎯 Focus`
4. Link to stoch project in CLAUDE.md
5. Confirm

**Output**:
```
✅ Task added: "Fix ATR calculation in indicators.py"

Details:
- Project: stoch
- Priority: high
- Added to: TodoWrite + Daily note + CLAUDE.md

Task #6 created.
Type `/todo 6` to see details.
```

### Example 3: Complete Task

**Input**: `/todo complete 1`

**Actions**:
1. Find task #1 in TodoWrite
2. Mark as completed
3. Update daily note: `- [x] Create todo-keeper skill`
4. Move to `## ✅ Completed` section
5. Log completion time
6. Update progress

**Output**:
```
✅ Task completed: "Create todo-keeper skill"

Completed at: 14:30
Duration: ~1 hour
Project: obsidian

Progress: 60% (3/5 tasks complete)
Remaining: 2 tasks

Next task: "Add to claude-skills plugin"
```

### Example 4: Sync Tasks

**Input**: `/todo sync`

**Actions**:
1. Read all task sources
2. Identify conflicts
3. Resolve (newest wins)
4. Write updates to all locations
5. Report changes

**Output**:
```
🔄 Syncing tasks across systems...

Sources:
- TodoWrite: 5 tasks
- Daily note: 4 tasks
- CLAUDE.md: 3 project tasks

Changes:
✓ Added "Fix ATR calculation" to daily note
✓ Marked "Zip analysis" complete in CLAUDE.md
✓ Updated "Review beta1" priority to high

Conflicts resolved: 0
All systems in sync ✅
```

### Example 5: Project Tasks

**Input**: `/todo project xai`

**Actions**:
1. Filter tasks by project="xai"
2. Include tasks from CLAUDE.md xai section
3. Show project context
4. Display progress

**Output**:
```
📋 xai Project Tasks (4 total)

🔄 In Progress (1):
1. Experiment 6.2 with demographic analysis

📝 Pending (2):
2. Performance benchmarking with GPU cluster
3. Update thesis Chapter 6

✅ Completed (1):
✓ Experiment 6.1 execution (n=500)

Project Status:
- Defense readiness: 85/100
- Week: 2 of experimental sprint
- Next milestone: Week 3 (Nov 25)

Source: ~/.claude/CLAUDE.md
```

## Integration Points

### Slash Command

**File**: `~/.claude/commands/todo.md`

Invokes this skill with user arguments.

### SessionEnd Hook (Optional)

Can auto-sync tasks to daily note at session end:

```python
# ~/.claude/skills/todo-keeper/auto_sync.py
def session_end_hook():
    tasks = get_todowrite_state()
    daily_note = get_daily_note_path(today())

    # Sync completed tasks
    sync_completed_to_daily_note(tasks, daily_note)

    # Add pending tasks
    sync_pending_to_daily_note(tasks, daily_note)
```

### Daily Note Template

Daily notes include task sections:
```markdown
## 🎯 Focus
- [ ] Task from /todo
- [🔄] In progress

## ✅ Completed
- Completed task (14:30)
```

## Dependencies

- Claude TodoWrite tool (built-in)
- Obsidian vault at `~/Documents/Obsidian/Aaron/`
- CLAUDE.md at `~/.claude/CLAUDE.md`
- Daily note template with task sections
- Python 3.11+ for sync scripts

## Files Created by This Skill

- `~/.claude/skills/todo-keeper/SKILL.md` (this file)
- `~/.claude/skills/todo-keeper/README.md` (usage guide)
- `~/.claude/skills/todo-keeper/auto_sync.py` (optional SessionEnd hook)
- `~/.claude/commands/todo.md` (slash command)

## Related Skills

- **obsidian-memory-keeper**: Daily note management
- **memory-keeper**: CLAUDE.md updates
- Built-in **TodoWrite**: Session task tracking

Together these provide complete task and memory management.
