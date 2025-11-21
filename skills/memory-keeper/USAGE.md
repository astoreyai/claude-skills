# Memory Keeper - Usage Guide

Quick reference for using the memory-keeper skill and /update-memory command.

## Basic Usage

### Method 1: Slash Command (Recommended)
```
/update-memory
```
This is the easiest way to invoke the skill.

### Method 2: Direct Skill Invocation
Use the Skill tool with skill name: `memory-keeper`

## What Happens

When you run `/update-memory`, the skill:

1. **Analyzes Recent Activity** (last 7 days by default)
   - Git commits for all active projects
   - Conversation history statistics
   - New documentation files
   - Version tag changes

2. **Updates CLAUDE.md Sections**
   - Project status (versions, phases, achievements)
   - Session notes (major developments)
   - Patterns observed (workflows, insights)
   - Infrastructure updates (tools, scripts)
   - Last Updated timestamp

3. **Reports Changes**
   - Lists what was updated
   - Summarizes key changes
   - Notes any issues

## Active Projects Tracked

The skill automatically monitors these projects:

1. **xai** - `~/projects/xai/` (PhD Dissertation)
2. **Research Assistant** - `~/github/astoreyai/ai_scientist/`
3. **cc-flow** - `~/cc-flow/` (Kymera AI Desktop)
4. **astoreyai** - `~/github/astoreyai/`
5. **emotional_intelligence_llm** - `~/projects/emotional_intelligence_llm/`
6. **stoch** - `~/projects/stoch/` (Stock Scanner)
7. **screener** - `~/github/astoreyai/screener/`

## Example Scenarios

### Scenario 1: After Project Release
```
You: I just released stoch v2.0.0 with bug fixes
/update-memory
```

**Skill does:**
- Checks `git -C ~/projects/stoch describe --tags` → v2.0.0
- Finds new commits since beta1
- Updates stoch section with new version
- Adds session note: "Nov 20: stoch v2.0.0 released"

### Scenario 2: Weekly Review
```
/update-memory
```

**Skill does:**
- Scans all 7 projects for changes
- Identifies cc-flow had 15 commits
- Updates cc-flow achievements
- Adds pattern observation if new workflow detected

### Scenario 3: After Major Milestone
```
You: PhD defense scheduled for Jan 28, 2026
/update-memory
```

**Skill does:**
- Updates xai project section with defense date
- Adds to session notes: "Nov 20: PhD defense scheduled"
- Updates PhD Critical Actions section if needed

## Expected Output

```
Updated CLAUDE.md with:
- xai: No changes (last update Nov 12)
- cc-flow: No changes (last update Nov 17)
- stoch: Version v2.0.0-beta1 → v2.0.0
  - Added 35 bug fixes since beta1
  - Updated status to "Production Ready"
- Session notes: Added Nov 20 development
  - stoch v2.0.0 final release
- Last Updated: 2025-11-20

Sections updated: 2
```

## When to Use

**Good Times:**
- ✅ End of work session (daily)
- ✅ After releases/milestones
- ✅ Weekly review (every 5-7 days)
- ✅ Before taking a break
- ✅ After infrastructure changes

**Not Necessary:**
- ❌ After every single commit
- ❌ Multiple times per hour
- ❌ When no work was done

## Advanced Usage

### Focus on Specific Project
```
/update-memory
"Only check stoch status, ignore others"
```

### Extended Time Range
```
/update-memory
"Check last 14 days of activity"
```

### Dry Run
```
/update-memory
"Show what would be updated without modifying CLAUDE.md"
```

### With Context
```
/update-memory
"I completed Phase 5 of cc-flow with 200 LOC, 50 tests"
```

## Troubleshooting

### No Changes Detected
**Possible reasons:**
- No commits in last 7 days
- No version tags changed
- No new documentation files

**Solution:** Provide context or extend time range

### Skill Asks for Clarification
**Why:** Ambiguous dates, missing version info, or unclear status

**How to respond:**
- Provide specific version: "stoch is now v2.0.0"
- Clarify date: "This happened on Nov 20"
- Specify project: "Update only the stoch section"

### Updates Missing Information
**Check:**
- Are changes committed to git?
- Are status files up to date?
- Is conversation history current?

## Files Modified

The skill only modifies one file:
- `~/.claude/CLAUDE.md`

It **preserves all existing content** and only adds/augments.

## Safety Features

✅ **Reads first** - Always reads current state before editing
✅ **Preserves content** - Never deletes unless explicitly told
✅ **Verifies paths** - Checks file references exist
✅ **Validates dates** - Ensures chronological consistency
✅ **Backups on error** - Creates .backup file if issues detected
✅ **Asks when uncertain** - Prompts for clarification

## Integration with Git

The skill uses these git commands:
```bash
# Get current version tag
git -C <project-path> describe --tags

# Get recent commits
git -C <project-path> log --oneline --since="7 days ago"

# Check if repo is clean
git -C <project-path> status --porcelain
```

## Integration with Conversation History

Uses workspace-manager tools:
```bash
# Get stats
python ~/cc-flow/tools/workspace-manager/src/claude-conversation-viewer.py stats

# List recent conversations
python ~/cc-flow/tools/workspace-manager/src/claude-conversation-viewer.py list --limit 10 --sort date
```

## Tips

1. **Run regularly** - Daily or after significant work
2. **Provide context** - Help the skill understand what changed
3. **Review output** - Check what was updated
4. **Trust the skill** - It's designed to preserve your memory safely

## Support Files

- **SKILL.md** - Complete skill specification (technical details)
- **README.md** - Quick start guide
- **USAGE.md** - This file (detailed usage)

## Questions?

The skill is self-documenting. Read SKILL.md for complete technical details.
