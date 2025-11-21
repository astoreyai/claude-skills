# Obsidian Memory Keeper - README

## Overview

The **obsidian-memory-keeper** skill provides automated daily note management and knowledge base synchronization for Aaron's Obsidian vault (`~/Documents/Obsidian/Aaron/`).

## Features

- **Daily Note Creation**: Auto-create daily notes from template
- **Session Tracking**: Record Claude Code sessions with context
- **CLAUDE.md Sync**: Bidirectional synchronization
- **Weekly Reviews**: Automated weekly summaries (Sundays)
- **Git Integration**: Track file modifications automatically
- **Knowledge Linking**: Auto-link to projects and topics

## Installation

### Prerequisites

1. Obsidian vault at `~/Documents/Obsidian/Aaron/`
2. Daily-Note template in vault
3. Python 3.11+
4. Claude Code CLI

### Setup Steps

1. **Skill is already installed** at `~/.claude/skills/obsidian-memory-keeper/`

2. **Slash command registered** at `~/.claude/commands/daily-note.md`

3. **Optional: Enable SessionEnd hook** for auto-tracking

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
            "command": "python3 ~/.claude/skills/memory-keeper/auto_update.py",
            "timeout": 30
          },
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

## Usage

### Manual Invocation

Type `/daily-note` in Claude Code to:
- Create/update today's daily note
- Add current session summary
- Sync with CLAUDE.md (if requested)
- Generate weekly review (if Sunday)

### Auto-Invocation

If SessionEnd hook is enabled:
- Session entry auto-created when you exit Claude Code
- Git changes captured automatically
- Daily note updated with timestamp and context

### Common Commands

```bash
# View today's daily note
cat ~/Documents/Obsidian/Aaron/Daily/$(date +%Y-%m-%d).md

# Check recent sessions
tail -20 ~/Documents/Obsidian/Aaron/Daily/$(date +%Y-%m-%d).md

# View logs
tail -20 ~/.claude/logs/obsidian-memory-keeper.log

# Open vault in Obsidian
obsidian://open?vault=Aaron
```

## Daily Note Structure

Each daily note follows this template:

```markdown
# YYYY-MM-DD

## Morning Review
- [ ] Check CLAUDE.md status
- [ ] Review active projects
- [ ] Plan today's priorities

## Session Notes

### Session 1: HH:MM
**Project**: /path/to/project
**Focus**: What you're working on

**Completed**:
- Task 1
- Task 2

**Files Modified**: X files
**Decisions**: Key decisions made
**Next**: Next steps

## Accomplishments
- Daily wins

## Learnings
- Insights gained

## Tomorrow
- [ ] Priority 1
- [ ] Priority 2

## Links
- [[Projects]]
- [[CLAUDE.md]]

---
Tags: #daily-note #YYYY #MM
```

## Integration with CLAUDE.md

The skill synchronizes bidirectionally with `~/.claude/CLAUDE.md`:

**CLAUDE.md → Obsidian**:
- Project milestones → Daily notes
- Session notes → Detailed entries
- Metrics → Project notes

**Obsidian → CLAUDE.md**:
- Session summaries → Session notes section
- Learnings → Patterns observed
- Project updates → Active projects

## Weekly Reviews

Every Sunday, `/daily-note` generates a weekly review:

**Location**: `~/Documents/Obsidian/Aaron/Daily/Weekly-Reviews/YYYY-WXX.md`

**Contents**:
- Week's accomplishments aggregated
- Project progress from CLAUDE.md
- Lessons learned
- Next week priorities
- Links to all 7 daily notes

## Logs

All operations logged to:
```bash
~/.claude/logs/obsidian-memory-keeper.log
```

**Log entries include**:
- Session ID and timestamp
- Working directory
- Files modified count
- Daily note path updated
- Errors (if any)

**View logs**:
```bash
tail -f ~/.claude/logs/obsidian-memory-keeper.log
```

## Troubleshooting

### Vault Not Found

**Error**: `Aaron vault not found at ~/Documents/Obsidian/Aaron/`

**Solution**:
```bash
# Verify vault exists
ls -la ~/Documents/Obsidian/Aaron/

# If missing, run migration
bash ~/execute-obsidian-migration.sh
```

### Template Missing

**Error**: Daily note created without template structure

**Solution**:
```bash
# Check template exists
cat ~/Documents/Obsidian/Aaron/Templates/Daily-Note.md

# If missing, recreate from migration script
```

### Hook Not Running

**Error**: No session entries auto-created

**Check**:
1. Hook registered: `cat ~/.claude/settings.json | grep obsidian-memory-keeper`
2. Script executable: `chmod +x ~/.claude/skills/obsidian-memory-keeper/auto_session.py`
3. Python available: `which python3`
4. Logs: `cat ~/.claude/logs/obsidian-memory-keeper.log`

**Test manually**:
```bash
echo '{"session_id":"test-123","cwd":"'$(pwd)'"}' | \
  python3 ~/.claude/skills/obsidian-memory-keeper/auto_session.py
```

### Git Status Not Working

**Error**: Session shows "0 files modified" but you changed files

**Cause**: Not in a git repository

**Solution**: Initialize git in project:
```bash
cd ~/projects/your-project
git init
git add .
git commit -m "Initial commit"
```

## Configuration

### Customize Daily Note Template

Edit: `~/Documents/Obsidian/Aaron/Templates/Daily-Note.md`

Add your own sections, checklists, or formatting.

### Change Vault Location

If you move the Aaron vault, update the path in:
- `auto_session.py` (line: `vault_path = ...`)
- `/daily-note` command documentation

### Adjust Session Entry Format

Edit `create_session_entry()` function in `auto_session.py` to customize:
- Session timestamp format
- Git diff truncation limit (default 500 chars)
- Entry structure

## Safety Features

- **Non-Destructive**: Only appends to daily notes, never deletes
- **Preserves Edits**: Your manual edits preserved
- **Error Handling**: Gracefully handles missing vault/templates
- **Logging**: All operations logged for audit
- **Exit 0**: Errors don't block SessionEnd

## Related Skills

- **memory-keeper**: Updates `~/.claude/CLAUDE.md` (timestamp, session notes)
- **obsidian-memory-keeper**: Updates Obsidian vault (this skill)

Use both for complete memory management.

## Files

```
~/.claude/skills/obsidian-memory-keeper/
├── SKILL.md              # Full skill specification
├── auto_session.py       # SessionEnd hook script
├── README.md             # This file
└── USAGE.md              # Usage examples and workflows

~/.claude/commands/
└── daily-note.md         # Slash command for manual invocation

~/.claude/logs/
└── obsidian-memory-keeper.log  # Operation logs
```

## Next Steps

1. **Test the skill**: Type `/daily-note` to create today's note
2. **Review the entry**: Open `~/Documents/Obsidian/Aaron/Daily/YYYY-MM-DD.md`
3. **Enable auto-run**: Add SessionEnd hook to settings.json
4. **Customize template**: Edit Daily-Note template to fit your workflow
5. **Open in Obsidian**: View your vault with all the linked notes

## Support

For issues or questions:
- Check logs: `~/.claude/logs/obsidian-memory-keeper.log`
- Review USAGE.md for examples
- Verify vault structure matches migration output
- Test hook manually with echo command above

## Version

**Version**: 1.0.0
**Created**: 2025-11-20
**Vault**: ~/Documents/Obsidian/Aaron/
**Synced with**: memory-keeper v1.0.0
