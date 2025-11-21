---
name: memory-keeper
description: Updates Aaron's Core Memory (CLAUDE.md) with session notes, project status, and development patterns
allowed-tools: ['Read', 'Write', 'Edit', 'Bash', 'Grep', 'Glob']
---

# Memory Keeper Skill

Maintains and updates Aaron's Core Memory file (`~/.claude/CLAUDE.md`) with project updates, session notes, and observed development patterns.

## Purpose

This skill automates the maintenance of Aaron's persistent context by:
- Analyzing recent work and conversations
- Updating project status sections
- Recording major developments in session notes
- Tracking development patterns and observations
- Ensuring project metadata stays current

## When to Use

Invoke this skill when:
1. **After major project milestones** - Phase completions, releases, significant commits
2. **End of work sessions** - Capture what was accomplished
3. **Project status changes** - Version bumps, status updates, new phases
4. **User explicitly requests** - "Update my memory", "Record this in CLAUDE.md"
5. **Significant infrastructure changes** - New tools, scripts, workflows

## What Gets Updated

### Project Sections
For each active project (xai, cc-flow, stoch, screener, etc.):
- **Version/Status**: Current version tags, phase completions
- **Recent Achievements**: Latest completed work (last 3-7 days)
- **Key Metrics**: Test coverage, documentation stats, quality scores
- **File Locations**: Important files added or moved
- **Next Milestones**: Upcoming phases or goals

### Session Notes
Updates the "Session Notes" section with:
- **Major Developments**: Date-stamped significant events
- **Patterns Observed**: New workflows, productivity insights, technical patterns
- **Project Status Summary**: Current state of all active projects
- **Infrastructure Updates**: New scripts, tools, configurations

### Metadata
- **Last Updated**: Current date timestamp
- **Quick Commands**: New or updated command patterns
- **Recovery Procedures**: Lessons learned from incidents

## Analysis Process

### Step 1: Gather Context
```bash
# Analyze recent git activity
git -C <project-path> log --oneline --since="7 days ago"
git -C <project-path> describe --tags

# Check project status files
find <project-path> -name "STATUS*.md" -o -name "PHASE_*.md" -o -name "README.md"

# Analyze conversation history
python ~/cc-flow/tools/workspace-manager/src/claude-conversation-viewer.py stats
python ~/cc-flow/tools/workspace-manager/src/claude-conversation-viewer.py list --limit 10 --sort date
```

### Step 2: Identify Changes
- New tags/versions (git describe output changes)
- Completed phases (new PHASE_*_COMPLETE.md files)
- Recent commits (git log analysis)
- Large conversations (indicates major work sessions)
- New files/directories (project structure changes)

### Step 3: Update CLAUDE.md

**For Project Updates:**
- Read current project section from CLAUDE.md
- Compare with latest git status, tags, and documentation
- Update version, status, achievements, and key files
- Preserve all existing information, only augment

**For Session Notes:**
- Read current Session Notes section
- Add new major developments with date stamps
- Update patterns if new workflows emerged
- Update project status summary
- Add infrastructure updates if tools/scripts created

**For Metadata:**
- Update "Last Updated" timestamp
- Add new quick commands if applicable

### Step 4: Formatting Rules

**Date Formats:**
- Session notes header: `Session Notes (Nov 12-20, 2025)`
- Major developments: `**Nov 20**: Description`
- Project sections: `(2025-11-20)` or `Nov 20, 2025`

**Markdown Conventions:**
- Use `✅` for completed items
- Use `**bold**` for emphasis
- Use code blocks for commands
- Use `- ` for bullet lists
- Preserve existing structure and formatting

**Conciseness:**
- Keep entries factual and brief
- Focus on outcomes, not process
- Include metrics when relevant (LOC, test count, file sizes)
- Use present tense for current status

## Example Updates

### Example 1: After stoch beta1 release
```markdown
**Current Status** (2025-11-18 - Beta1 Release):
- ✅ Beta1 released (v2.0.0-beta1) - Nov 18, 2025
- ✅ Complete documentation (~4,500 lines: README, API ref, migration guide)
- ✅ 149 tests passing, zero warnings
- ✅ Git tagged: v2.0.0-beta1
```

### Example 2: Session note addition
```markdown
**Major Developments**:
...
- **Nov 20**: sudo askpass helper created - SSH/Termux compatible, kdialog GUI, /dev/tty fallback
```

### Example 3: Pattern observation
```markdown
**Patterns Observed**:
...
- Rapid multi-model integration: 3 AI backends integrated in single 4-hour session
```

## Safety Guidelines

1. **Always Read First**: Never update CLAUDE.md without reading current content
2. **Preserve Everything**: Only add/augment, never delete unless explicitly instructed
3. **Maintain Structure**: Keep existing section headers and organization
4. **Verify Dates**: Ensure date stamps are accurate and consistent
5. **Check References**: Verify file paths and references exist before adding
6. **No Assumptions**: Base updates only on verifiable evidence (git logs, files, conversation history)

## Integration with Slash Command

When invoked via `/update-memory`:
1. Analyze recent work (last 7 days unless specified)
2. Identify significant changes across all projects
3. Update CLAUDE.md with findings
4. Report what was updated to user

## Workflow Example

```bash
# User invokes: /update-memory

# Skill executes:
# 1. Read current CLAUDE.md
# 2. Check git activity for all active projects
# 3. Analyze recent conversations
# 4. Find new documentation files
# 5. Update relevant sections
# 6. Report changes made

Output:
"Updated CLAUDE.md with:
- stoch: Version updated to v2.0.0-beta1+28 (28 post-beta commits)
- Session notes: Added Nov 20 developments (askpass helper, cc-term deletion)
- Patterns: Added project pruning observation
- Last Updated: 2025-11-20"
```

## Error Handling

- If CLAUDE.md is corrupted, back up to `~/.claude/CLAUDE.md.backup.$(date +%s)` before editing
- If uncertain about project status, ask user for clarification
- If dates are ambiguous, default to current date
- If sections are missing, add them following existing structure

## Quality Checks

Before finalizing updates:
- ✅ All file paths referenced actually exist
- ✅ Version tags match git describe output
- ✅ Dates are chronologically consistent
- ✅ Markdown formatting is valid
- ✅ No duplicate entries
- ✅ All active projects have current status
