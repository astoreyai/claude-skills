# Update Memory Command

Invokes the memory-keeper skill to update Aaron's Core Memory (CLAUDE.md) with recent developments, project status changes, and session notes.

## Instructions

Use the **memory-keeper** skill to analyze recent work and update `~/.claude/CLAUDE.md`.

### Analysis Scope

By default, analyze the last **7 days** of activity. This includes:
- Git commits across all active projects
- Recent conversation history
- New documentation files
- Status file updates
- Version tag changes

### Step-by-Step Process

1. **Activate the memory-keeper skill**
   ```
   Use the Skill tool to invoke "memory-keeper"
   ```

2. **The skill will automatically:**
   - Read the current CLAUDE.md file
   - Analyze git activity for all active projects:
     - `~/projects/xai/` (PhD dissertation)
     - `~/cc-flow/` (Kymera AI desktop)
     - `~/projects/stoch/` (Stock scanner)
     - `~/github/astoreyai/screener/` (Trading scanner)
     - `~/github/astoreyai/ai_scientist/` (Research assistant)
   - Check conversation statistics via workspace-manager tools
   - Identify new phase completions, releases, or major milestones
   - Find new documentation (PHASE_*.md, STATUS*.md, README.md updates)

3. **Update CLAUDE.md with:**
   - **Project Status**: Version updates, phase completions, achievement summaries
   - **Session Notes**: Date-stamped major developments
   - **Patterns Observed**: New workflows, productivity insights
   - **Infrastructure Updates**: New scripts, tools, configurations
   - **Last Updated**: Current timestamp

4. **Report what was updated:**
   - List all sections modified
   - Summarize key changes
   - Note any issues or uncertainties

## Usage Examples

### Basic Usage
```
/update-memory
```
Analyzes last 7 days and updates CLAUDE.md.

### With Context
```
/update-memory
"I just completed stoch v2.0.0 final release with 35 bug fixes"
```
Focuses on specific project and includes user-provided context.

### After Major Milestone
```
/update-memory
"PhD defense date confirmed for Jan 28, 2026. Committee expanded to 6 members."
```
Records critical PhD milestone information.

## What Gets Updated

### Active Projects (Current: 6)
1. **xai** - PhD Dissertation
2. **Research Assistant** - Academic workflow automation
3. **cc-flow** - Kymera AI Desktop Assistant
4. **astoreyai** - Personal AI projects
5. **emotional_intelligence_llm** - EQ research
6. **stoch** - Stock scanner
7. **screener** - Trading scanner (planning phase)

### Update Types

**Version/Status Changes:**
- Git tags: `git describe --tags`
- Phase completions: New `PHASE_*_COMPLETE.md` files
- Status updates: Changes in STATUS files
- Version bumps in package.json, setup.py, etc.

**Major Developments:**
- Releases (alpha, beta, production)
- Phase completions (cc-flow phases)
- Significant commits (>100 LOC changes)
- New features or modules
- Infrastructure additions

**Patterns Observed:**
- Productivity insights (peak days, parallel workflows)
- Development patterns (agent usage, stripping workflows)
- Recovery procedures (from incidents)
- New techniques or approaches

## Safety Features

The memory-keeper skill follows these safety rules:

✅ **Read First**: Always reads current CLAUDE.md before editing
✅ **Preserve Content**: Only adds/augments, never deletes
✅ **Verify Paths**: Checks that all referenced files exist
✅ **Accurate Dates**: Validates date chronology
✅ **Backup on Error**: Creates backup if corruption detected
✅ **Ask if Uncertain**: Prompts user for clarification when needed

## Expected Output

After running `/update-memory`, you should see:

```
Updated CLAUDE.md with:
- xai: No changes detected (last update Nov 12)
- cc-flow: No changes detected (last update Nov 17)
- stoch: Version updated to v2.0.0-beta1+28 (28 commits since beta1)
- Session notes: Added Nov 20 developments
  - sudo askpass helper created
  - cc-term project deletion (2.1GB)
- Patterns: Added "Project pruning" observation
- Infrastructure: Documented askpass helper and sudo wrapper
- Last Updated: 2025-11-20

Total sections updated: 3
No issues detected.
```

## When to Use

**Recommended frequency:**
- **End of work session**: Capture what was accomplished
- **After major milestones**: Releases, phase completions, breakthroughs
- **Weekly review**: Every 5-7 days to stay current
- **Before long breaks**: Ensure context preserved

**Good triggers:**
- "Just tagged v2.0.0"
- "Completed Phase 5"
- "Submitted paper for review"
- "New infrastructure deployed"
- "Significant bug fixes committed"

## Integration Points

This command works with:
- **Git repositories**: All active projects tracked via git
- **Conversation history**: `~/cc-flow/tools/workspace-manager/`
- **CLAUDE.md**: `~/.claude/CLAUDE.md` (primary memory file)
- **Project docs**: Status files, phase docs, READMEs

## Troubleshooting

**If updates seem incomplete:**
- Ensure git repositories are up to date (git fetch)
- Check that status files are committed
- Verify conversation history is current

**If skill asks for clarification:**
- Provide specific context about recent work
- Confirm version numbers or dates
- Specify which projects to focus on

**If CLAUDE.md formatting breaks:**
- Skill creates automatic backup before editing
- Restore from `~/.claude/CLAUDE.md.backup.*` if needed

## Advanced Usage

**Focus on specific project:**
```
/update-memory
"Only update stoch status - ignore other projects"
```

**Longer time window:**
```
/update-memory
"Analyze last 14 days for all projects"
```

**Dry run (report only):**
```
/update-memory
"Analyze what would be updated but don't modify CLAUDE.md"
```

---

**Note**: This command is designed to be run proactively by Claude or invoked by the user. The memory-keeper skill handles all the analysis and updating logic automatically.
