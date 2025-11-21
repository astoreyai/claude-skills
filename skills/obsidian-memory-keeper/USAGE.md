# Obsidian Memory Keeper - Usage Guide

## Quick Start

### First Time Setup

1. **Verify vault exists**:
   ```bash
   ls ~/Documents/Obsidian/Aaron/
   ```

2. **Create your first daily note**:
   Type `/daily-note` in Claude Code

3. **View the result**:
   ```bash
   cat ~/Documents/Obsidian/Aaron/Daily/$(date +%Y-%m-%d).md
   ```

4. **Open in Obsidian**:
   Open Obsidian → Select Aaron vault → Navigate to Daily/

## Usage Patterns

### Pattern 1: End of Day Summary

**When**: At the end of your work day

**Action**: Type `/daily-note` in Claude Code

**What Happens**:
1. Creates today's daily note (if missing)
2. Analyzes your session:
   - Working directory
   - Files modified (from git)
   - Tasks completed (from conversation)
3. Adds formatted session entry
4. Reports status

**Example Output**:
```
Daily note updated: 2025-11-20.md (Session 3 added)
- Project: ~/projects/xai
- Files modified: 5
- Session focus: Experimental validation sprint
```

### Pattern 2: Weekly Review (Sunday)

**When**: Sunday evening

**Action**: Type `/daily-note` in Claude Code

**What Happens**:
1. Detects it's Sunday
2. Gathers daily notes from Monday-Sunday
3. Extracts accomplishments and learnings
4. Creates weekly review in `Weekly-Reviews/YYYY-WXX.md`
5. Links to all 7 daily notes

**Example Weekly Review**:
```markdown
# Week 47 (Nov 18-24, 2025)

## Summary

Completed PhD experimental validation Week 2, released stoch v2.0.0-beta1,
and migrated knowledge base to Obsidian.

## Project Progress

### xai - PhD Dissertation
- **Status**: Defense readiness 85/100 → 88/100 (+3 points)
- **Accomplishments**:
  - Experiment 6.1 completed (n=500 samples)
  - 12 new tests added to attribution methods
  - Thesis compiled (479 pages, no errors)

### stoch - Trading Scanner
- **Status**: v2.0.0-beta1 → v2.0.0-beta1+28
- **Accomplishments**:
  - Released beta1 (Nov 18)
  - Fixed 4 critical bugs post-beta
  - 149 tests passing

## Lessons Learned

- Git initialization critical for session tracking
- Beta releases require rapid bug fix cycles
- Obsidian vault structure improves knowledge retention

## Next Week Priorities

- [ ] xai: Experiment 6.2 with demographic analysis
- [ ] stoch: Performance benchmarking with IB Gateway
- [ ] Obsidian: Clean up and organize migrated notes

## Daily Notes

- [[2025-11-18]] - Beta1 release day
- [[2025-11-19]] - Obsidian migration
- [[2025-11-20]] - Skill creation day
- [[2025-11-21]] - Week 2 experiments
- [[2025-11-22]] - Testing and validation
- [[2025-11-23]] - Documentation updates
- [[2025-11-24]] - Weekly review

---
Tags: #weekly-review #2025 #W47
```

### Pattern 3: Full Sync with CLAUDE.md

**When**: After major milestones or weekly

**Action**: Type `/daily-note sync` in Claude Code

**What Happens**:
1. Reads CLAUDE.md session notes
2. Reads all recent daily notes
3. Compares content bidirectionally
4. Merges differences:
   - CLAUDE.md → Obsidian: Milestones, metrics
   - Obsidian → CLAUDE.md: Detailed sessions, learnings
5. Updates Last Updated timestamps
6. Reports conflicts (if any)

**Example Sync**:
```
Synced 8 daily notes with CLAUDE.md:
- Added PhD breakthrough (Nov 12) to daily note
- Added 14 session summaries from Obsidian to CLAUDE.md
- Updated project metrics in both systems
- 0 conflicts detected
```

### Pattern 4: Auto-Tracking (SessionEnd Hook)

**When**: Every time you exit Claude Code (automatic)

**Setup**: Add hook to `~/.claude/settings.json`:
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

**What Happens**:
1. SessionEnd triggered when you exit
2. Script captures:
   - Session ID
   - Working directory
   - Git status
   - Git diff stats
3. Creates session entry automatically
4. Appends to today's daily note
5. Logs to `~/.claude/logs/obsidian-memory-keeper.log`

**No manual action needed** - just exit Claude Code normally.

## Real-World Workflows

### Workflow 1: PhD Research Day

**Morning**:
- Open daily note in Obsidian
- Review Morning Review checklist
- Plan today's priorities

**During work**:
- Work in Claude Code (experiments, writing, coding)
- (Optional) Exit/restart sessions as needed
- SessionEnd hook auto-tracks each session

**Evening**:
- Type `/daily-note` for final summary
- Review daily note in Obsidian
- Add manual notes to "Learnings" section
- Check off accomplishments

**Result**: Complete record of PhD work with session details

### Workflow 2: Multi-Project Development

**Context**: Working on xai, stoch, and cc-flow in one day

**Approach**:
- Each project session tracked separately
- Sessions show different working directories
- Git changes tracked per-project

**Daily Note Shows**:
```markdown
## Session Notes

### Session 1: 09:00
**Project**: ~/projects/xai
**Focus**: Experiment 6.1 execution
...

### Session 2: 11:30
**Project**: ~/projects/stoch
**Focus**: Beta1 bug fixes
...

### Session 3: 14:00
**Project**: ~/cc-flow
**Focus**: Phase 5 planning
...
```

**Benefit**: Clear separation of work across projects

### Workflow 3: Weekly Planning Cycle

**Sunday**:
- Type `/daily-note` → Weekly review generated
- Review last week's accomplishments
- Set next week priorities

**Monday-Saturday**:
- Daily notes auto-created
- Sessions tracked throughout week
- Manual edits for insights/learnings

**Next Sunday**:
- Previous weekly review linked
- New weekly review created
- Progress tracked week-over-week

**Result**: Structured weekly rhythm with historical record

### Workflow 4: Knowledge Base Building

**As you work**:
- Daily notes accumulate sessions and learnings
- Auto-linking to Projects/ and Knowledge/ notes

**Weekly**:
- Review week's learnings
- Create new Knowledge/ notes for important concepts
- Link from daily notes to knowledge notes

**Monthly**:
- Create MOCs (Maps of Content) in Knowledge/
- Archive completed projects
- Refactor note structure

**Result**: Organized, searchable knowledge base

## Command Reference

### /daily-note

Basic usage - creates/updates today's daily note:
```
/daily-note
```

With sync - synchronizes with CLAUDE.md:
```
/daily-note sync
```

Force weekly review (any day):
```
/daily-note weekly
```

### Manual Script Execution

Test SessionEnd hook:
```bash
echo '{"session_id":"test-123","cwd":"'$(pwd)'"}' | \
  python3 ~/.claude/skills/obsidian-memory-keeper/auto_session.py
```

Check script output:
```bash
echo '{"session_id":"manual","cwd":"'$(pwd)'"}' | \
  python3 ~/.claude/skills/obsidian-memory-keeper/auto_session.py | \
  python3 -m json.tool
```

View logs in real-time:
```bash
tail -f ~/.claude/logs/obsidian-memory-keeper.log
```

## File Locations

### Daily Notes
```
~/Documents/Obsidian/Aaron/Daily/
├── 2025-11-18.md
├── 2025-11-19.md
├── 2025-11-20.md
└── Weekly-Reviews/
    ├── 2025-W46.md
    └── 2025-W47.md
```

### Project Notes
```
~/Documents/Obsidian/Aaron/Projects/
├── xai.md
├── stoch.md
├── cc-flow.md
└── research-assistant.md
```

### Knowledge Base
```
~/Documents/Obsidian/Aaron/Knowledge/
├── Python.md
├── Git.md
├── PhD-Process.md
└── Trading-Indicators.md
```

### Templates
```
~/Documents/Obsidian/Aaron/Templates/
└── Daily-Note.md
```

## Tips and Tricks

### Tip 1: Link Everything

Use `[[WikiLinks]]` liberally in manual edits:
- Link project names → `[[xai]]`, `[[stoch]]`
- Link concepts → `[[Git]]`, `[[Python]]`
- Link dates → `[[2025-11-20]]`

Obsidian will show backlinks automatically.

### Tip 2: Use Tags Strategically

Add tags to session entries:
- `#experiment` for experimental work
- `#bug-fix` for debugging sessions
- `#milestone` for major achievements
- `#learning` for insights

Search by tag in Obsidian: Click tag or search `tag:#experiment`

### Tip 3: Customize Session Template

Edit `auto_session.py` to match your style:
- Add fields (Duration, Energy Level, Mood)
- Change formatting (emoji, headers, lists)
- Include custom git commands

### Tip 4: Create Session Shortcuts

Add to your `.zshrc`:
```bash
alias dn='cat ~/Documents/Obsidian/Aaron/Daily/$(date +%Y-%m-%d).md'
alias dnl='ls -lt ~/Documents/Obsidian/Aaron/Daily/*.md | head -10'
alias dne='vim ~/Documents/Obsidian/Aaron/Daily/$(date +%Y-%m-%d).md'
```

Usage:
- `dn` - View today's note
- `dnl` - List recent notes
- `dne` - Edit today's note

### Tip 5: Sync with Git

Track your vault in git:
```bash
cd ~/Documents/Obsidian/Aaron
git init
git add .
git commit -m "Initial commit"

# Auto-commit daily notes
crontab -e
# Add: 0 23 * * * cd ~/Documents/Obsidian/Aaron && git add Daily/ && git commit -m "Daily notes: $(date +%Y-%m-%d)" || true
```

## Customization

### Customize Daily Note Template

Edit: `~/Documents/Obsidian/Aaron/Templates/Daily-Note.md`

Example additions:
```markdown
## Energy Levels
Morning: ⚡⚡⚡⚡⚡
Afternoon: ⚡⚡⚡
Evening: ⚡⚡

## Focus Time
🍅 Pomodoros: 0
⏱️ Deep Work: 0h 0m

## Gratitude
1.
2.
3.
```

### Customize Session Entry Format

Edit `auto_session.py` function `create_session_entry()`:

```python
def create_session_entry(session_id, cwd, git_status, git_diff):
    """Create a session entry for daily note."""
    session_time = datetime.now().strftime("%H:%M")
    project_name = get_project_name(cwd)

    # Your custom format here
    entry = f"\n### 🚀 Session: {session_time}\n"
    entry += f"**📁 Project**: `{project_name}`\n"
    entry += f"**📍 Path**: `{cwd}`\n"
    # ... add your fields
```

### Add Custom Git Commands

In `auto_session.py`, add functions:

```python
def get_commit_count_today(cwd):
    """Get number of commits today."""
    try:
        result = subprocess.run(
            ['git', 'log', '--since=midnight', '--oneline'],
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            return len(result.stdout.strip().split('\n'))
        return 0
    except Exception:
        return 0
```

Then use in session entry:
```python
commits_today = get_commit_count_today(cwd)
entry += f"**Commits Today**: {commits_today}\n"
```

## Troubleshooting

### Issue: Daily notes not auto-created

**Solution**: Check hook is registered:
```bash
cat ~/.claude/settings.json | grep -A 10 SessionEnd
```

### Issue: Git status always empty

**Solution**: Initialize git in project:
```bash
cd ~/projects/your-project
git init
```

### Issue: Session entries duplicated

**Solution**: Check if hook runs multiple times:
```bash
grep "SessionEnd hook triggered" ~/.claude/logs/obsidian-memory-keeper.log | \
  tail -10
```

If duplicates, you may have hook registered twice in settings.json.

### Issue: Template not applied to new daily notes

**Solution**: Verify template exists:
```bash
cat ~/Documents/Obsidian/Aaron/Templates/Daily-Note.md
```

If missing, recreate:
```bash
bash ~/execute-obsidian-migration.sh
```

## Advanced Usage

### Integration with memory-keeper

Run both skills together for complete sync:

**settings.json**:
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

**Result**: CLAUDE.md timestamp updated + Obsidian session tracked

### Obsidian Plugin Integration

Install Obsidian plugins for enhanced functionality:
- **Dataview**: Query daily notes programmatically
- **Calendar**: Visual calendar of daily notes
- **Templater**: Advanced template features
- **Git**: Auto-commit from within Obsidian

### Dataview Queries

Add to daily note or separate dashboard:

```dataview
TABLE
  file.mtime AS "Last Modified",
  length(file.outlinks) AS "Links"
FROM "Daily"
WHERE file.name >= "2025-11-01"
SORT file.name DESC
LIMIT 30
```

Shows last 30 days of daily notes with metadata.

## Resources

- **Skill Documentation**: `~/.claude/skills/obsidian-memory-keeper/SKILL.md`
- **Installation Guide**: `~/.claude/skills/obsidian-memory-keeper/README.md`
- **Logs**: `~/.claude/logs/obsidian-memory-keeper.log`
- **Vault**: `~/Documents/Obsidian/Aaron/`
- **CLAUDE.md**: `~/.claude/CLAUDE.md`

## Next Steps

1. Type `/daily-note` to create your first daily note
2. Open the note in Obsidian to see the structure
3. Enable SessionEnd hook for auto-tracking
4. Customize the Daily-Note template to fit your workflow
5. Start building your knowledge base with linked notes

Happy note-taking! 📝
