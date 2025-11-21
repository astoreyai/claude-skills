# Obsidian Memory Keeper Skill

## Description

Manages daily notes, session tracking, and knowledge base synchronization for Aaron's Obsidian vault located at `~/Documents/Obsidian/Aaron/`.

## Purpose

This skill provides automated daily note creation, session summaries, and bidirectional synchronization between CLAUDE.md and Obsidian vault content. It ensures Aaron's personal knowledge base stays current and organized.

## When to Invoke

**Auto-Invoke** (proactive):
- Daily note doesn't exist for today
- Session summary requested
- After significant development milestones
- Weekly review periods (Sundays)

**Manual Invoke** (explicit):
- User types `/daily-note` command
- User requests Obsidian integration
- User asks to "update daily notes", "sync Obsidian", or similar

## Core Capabilities

### 1. Daily Note Management

Create or update daily notes in Obsidian vault following the Daily-Note template:

**Location**: `~/Documents/Obsidian/Aaron/Daily/YYYY-MM-DD.md`

**Template Structure**:
```markdown
# YYYY-MM-DD

## Morning Review
- [ ] Check CLAUDE.md status
- [ ] Review active projects
- [ ] Plan today's priorities

## Session Notes

### Session 1: [Time]
**Project**:
**Focus**:

### Session 2: [Time]
**Project**:
**Focus**:

## Accomplishments
-

## Learnings
-

## Tomorrow
- [ ]
- [ ]

## Links
- [[Projects]]
- [[CLAUDE.md]]

---
Tags: #daily-note #YYYY #MM
```

**Daily Note Creation Rules**:
- Create new daily note at first session of the day
- Use ISO 8601 date format (YYYY-MM-DD)
- Auto-link to related project notes in Aaron vault
- Add session summaries as conversations occur
- Timestamp each session entry
- Include tags for searchability

### 2. Session Tracking

Track Claude Code sessions with context:

**What to Capture**:
- Session start/end time
- Working directory / project
- Key tasks completed
- Files modified (from git status if available)
- Significant decisions or insights
- Errors encountered and solutions

**How to Capture**:
1. Read git status in current working directory
2. Analyze conversation history for key activities
3. Extract file modifications, test results, commands
4. Summarize as bullet points under session heading
5. Append to today's daily note

**Example Session Entry**:
```markdown
### Session 3: 14:30-16:15
**Project**: ~/projects/xai (PhD Dissertation)
**Focus**: Experimental validation sprint Week 2

**Completed**:
- Ran Experiment 6.1 with n=500 samples (GPU cluster)
- Fixed type errors in attribution methods (3 files)
- Updated test suite (12 new tests added)
- Compiled thesis PDF (479 pages, no errors)

**Files Modified**:
- src/attribution/methods.py (+45, -12)
- tests/test_attribution.py (+150, -0)
- outputs/thesis/chapters/chapter6.tex (+23, -8)

**Decisions**: Chose SHAP over LIME for efficiency on n=500

**Next**: Week 3 - Experiment 6.2 with demographic analysis
```

### 3. CLAUDE.md Synchronization

Bidirectional sync between CLAUDE.md and Obsidian vault:

**CLAUDE.md → Obsidian**:
- Extract active projects from CLAUDE.md
- Create/update project notes in `~/Documents/Obsidian/Aaron/Projects/`
- Link projects to daily notes
- Sync session notes to daily notes
- Update project status in vault

**Obsidian → CLAUDE.md**:
- Extract insights from daily notes
- Update session notes in CLAUDE.md
- Add learnings to infrastructure/patterns
- Sync project status changes
- Preserve CLAUDE.md structure

**Sync Process**:
1. Read both CLAUDE.md and latest daily notes
2. Identify differences (new sessions, project updates, learnings)
3. Apply changes bidirectionally
4. Maintain consistency (Last Updated timestamp, project metrics)
5. Log sync operations

### 4. Knowledge Base Integration

Connect daily notes to Aaron's broader knowledge base:

**Auto-Linking**:
- Link project names to `~/Documents/Obsidian/Aaron/Projects/` notes
- Link tech concepts to `~/Documents/Obsidian/Aaron/Knowledge/` notes
- Create backlinks from projects to daily notes
- Tag notes appropriately (#daily-note, #project-name, #tech-stack)

**Content Organization**:
- Archive completed project notes to `~/Documents/Obsidian/Aaron/Archive/`
- Create indexes (MOCs - Maps of Content) for major topics
- Maintain clean folder structure (Daily, Projects, Knowledge, Archive)
- Remove duplicate content

### 5. Weekly Review Automation

Every Sunday, create weekly review note:

**Location**: `~/Documents/Obsidian/Aaron/Daily/Weekly-Reviews/YYYY-WXX.md`

**Content**:
- Summary of week's accomplishments
- Project progress (from CLAUDE.md metrics)
- Lessons learned
- Next week priorities
- Links to all daily notes from the week

**Process**:
1. Aggregate all daily notes from Monday-Sunday
2. Extract accomplishments and learnings
3. Pull project metrics from CLAUDE.md
4. Generate weekly summary
5. Create links to individual daily notes
6. Update CLAUDE.md session notes with weekly insights

## Analysis Process

**Step 1: Environment Check**
```bash
# Verify Obsidian vault exists
if [ ! -d ~/Documents/Obsidian/Aaron ]; then
    echo "ERROR: Aaron vault not found. Run migration first."
    exit 1
fi

# Check daily notes directory
mkdir -p ~/Documents/Obsidian/Aaron/Daily/

# Get today's date
TODAY=$(date +%Y-%m-%d)
```

**Step 2: Daily Note Creation/Update**
```bash
# Check if today's note exists
DAILY_NOTE=~/Documents/Obsidian/Aaron/Daily/$TODAY.md

if [ ! -f "$DAILY_NOTE" ]; then
    # Create from template
    cp ~/Documents/Obsidian/Aaron/Templates/Daily-Note.md "$DAILY_NOTE"
    # Replace date placeholders
    sed -i "s/YYYY-MM-DD/$TODAY/g" "$DAILY_NOTE"
fi
```

**Step 3: Session Analysis**
```bash
# Analyze current working directory
CWD=$(pwd)
PROJECT=$(basename $CWD)

# Get git status if in git repo
if [ -d .git ]; then
    GIT_STATUS=$(git status --short)
    FILES_MODIFIED=$(echo "$GIT_STATUS" | wc -l)
fi

# Capture session context
SESSION_TIME=$(date +%H:%M)
```

**Step 4: Content Extraction**

From conversation history, extract:
- Commands executed
- Files read/written
- Tests run (results)
- Decisions made
- Errors encountered

**Step 5: Note Formatting**

Format session entry as markdown:
```markdown
### Session N: HH:MM
**Project**: $CWD
**Focus**: [extracted from conversation context]

**Completed**:
- [bullet points from task list]
- [file modifications]
- [test results]

**Files Modified**: [from git status]
**Decisions**: [from conversation analysis]
**Next**: [from todo list or user intent]
```

**Step 6: Append to Daily Note**

```bash
# Find "## Session Notes" section
# Append new session entry
# Increment session counter
```

**Step 7: Sync with CLAUDE.md**

```python
# Read CLAUDE.md
with open(os.path.expanduser('~/.claude/CLAUDE.md'), 'r') as f:
    claude_md = f.read()

# Extract session notes section
# Compare with Obsidian daily notes
# Apply bidirectional updates
# Write back to CLAUDE.md
```

## Update Rules

### Safety Rules

**Never**:
- Delete user content without explicit confirmation
- Overwrite manually edited notes without backup
- Modify dates on existing daily notes
- Remove tags or links set by user
- Change vault structure (folder organization)

**Always**:
- Preserve manual edits in daily notes
- Create backups before major sync operations
- Log all modifications
- Verify vault structure before operations
- Exit gracefully if vault not found

### Update Frequency

**Auto-Updates** (SessionEnd hook):
- Daily note creation (once per day)
- Session entry addition (per session)
- CLAUDE.md timestamp update (daily)

**Manual Updates** (/daily-note command):
- Full sync with CLAUDE.md
- Weekly review generation (Sundays)
- Knowledge base reorganization
- Project note updates

### Conflict Resolution

When conflicts arise between CLAUDE.md and Obsidian:

1. **Timestamps**: Most recent wins
2. **Project status**: CLAUDE.md is source of truth
3. **Session notes**: Merge both (append)
4. **User edits**: Preserve always
5. **Metrics**: CLAUDE.md canonical

## Examples

### Example 1: Create Daily Note (First Session)

**Input**: User starts Claude Code at 9:00 AM, Nov 20, 2025
**Context**: No daily note exists for today

**Actions**:
1. Check if `~/Documents/Obsidian/Aaron/Daily/2025-11-20.md` exists
2. Create from template if missing
3. Replace date placeholders
4. Initialize session notes section
5. Log creation

**Output**: Daily note created, ready for session tracking

### Example 2: Add Session Entry

**Input**: User completes work on stoch project at 2:30 PM
**Context**: Daily note exists, need to add session summary

**Actions**:
1. Analyze conversation history since last session
2. Extract tasks completed (git commits, test results, files modified)
3. Format session entry with timestamp
4. Append to daily note under "## Session Notes"
5. Increment session counter

**Output**:
```markdown
### Session 2: 14:30
**Project**: ~/projects/stoch
**Focus**: Beta1 bug fixes - Rules 3-4, BB Width, ATR calculation

**Completed**:
- Fixed Bollinger Band width calculation (commit a30c58d)
- Corrected ATR implementation in technical indicators
- Updated Rules 3-4 logic for signal generation
- All 149 tests passing

**Files Modified**:
- src/indicators.py (+34, -12)
- src/rules.py (+18, -5)

**Decisions**: Used pandas rolling std for BB width consistency
**Next**: Performance benchmarking with real IB Gateway data
```

### Example 3: Weekly Review (Sunday)

**Input**: User invokes `/daily-note` on Sunday, Nov 24, 2025
**Context**: Week of Nov 18-24 complete

**Actions**:
1. Identify all daily notes from 2025-11-18 to 2025-11-24
2. Extract accomplishments from each day
3. Pull project metrics from CLAUDE.md
4. Generate weekly summary
5. Create `~/Documents/Obsidian/Aaron/Daily/Weekly-Reviews/2025-W47.md`
6. Link to individual daily notes

**Output**: Weekly review note with aggregated insights

### Example 4: Sync CLAUDE.md with Obsidian

**Input**: User types `/update-memory` and wants Obsidian sync
**Context**: Both CLAUDE.md and daily notes have new content

**Actions**:
1. Read CLAUDE.md session notes (Nov 12-20)
2. Read all daily notes from same period
3. Compare content:
   - CLAUDE.md has PhD breakthrough (Nov 12)
   - Daily notes have detailed session logs
4. Merge bidirectionally:
   - Add PhD breakthrough to daily note 2025-11-12
   - Add detailed session logs to CLAUDE.md if not present
5. Update Last Updated timestamp in both
6. Log sync completion

**Output**: Both files synchronized, no conflicts

## Integration Points

### Slash Command

**File**: `~/.claude/commands/daily-note.md`

```markdown
You are the obsidian-memory-keeper skill handler.

**Task**: Manage daily notes and Obsidian vault synchronization.

**Actions**:
1. Check if today's daily note exists
2. Create or update with current session
3. Sync with CLAUDE.md if requested
4. Generate weekly review if Sunday

**User Intent**: {{USER_MESSAGE}}
```

### SessionEnd Hook (Optional)

Can be configured to auto-create daily note entry:

```json
{
  "hooks": {
    "SessionEnd": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/skills/obsidian-memory-keeper/auto_session.py",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

## Dependencies

- Obsidian vault at `~/Documents/Obsidian/Aaron/`
- Daily-Note template in `~/Documents/Obsidian/Aaron/Templates/`
- CLAUDE.md at `~/.claude/CLAUDE.md`
- Python 3.11+ for automation scripts
- Git (for file modification tracking)

## Files Created by This Skill

- `~/.claude/skills/obsidian-memory-keeper/SKILL.md` (this file)
- `~/.claude/skills/obsidian-memory-keeper/auto_session.py` (SessionEnd hook script)
- `~/.claude/commands/daily-note.md` (slash command)
- `~/.claude/skills/obsidian-memory-keeper/README.md` (installation guide)
- `~/.claude/skills/obsidian-memory-keeper/USAGE.md` (examples and workflows)

## Related Skills

- **memory-keeper**: Updates CLAUDE.md (complementary)
- **obsidian-memory-keeper**: Updates Obsidian vault (this skill)

Together these provide complete memory management across both systems.
