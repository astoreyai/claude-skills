# Memory Keeper Skill

Automated maintenance of Aaron's Core Memory (`~/.claude/CLAUDE.md`).

## Quick Start

```bash
# Via slash command (easiest)
/update-memory

# Via skill invocation
# Use Skill tool with: "memory-keeper"
```

## What It Does

Analyzes last 7 days of work and updates CLAUDE.md with:
- Project status changes (versions, phases, achievements)
- Session notes (major developments, patterns)
- Infrastructure updates (new tools, scripts)
- Current timestamp

## Files

- **SKILL.md** - Complete skill specification and instructions
- **README.md** - This quick reference

## Integration

**Slash Command**: `~/.claude/commands/update-memory.md`
- Invokes this skill automatically
- Provides user-friendly interface

**Skill Location**: `~/.claude/skills/memory-keeper/`
- Auto-discovered by Claude Code
- Can be invoked directly via Skill tool

## Safety

✅ Always reads before editing
✅ Preserves all existing content
✅ Verifies file paths
✅ Creates backups on error
✅ Asks for clarification when uncertain

## Projects Tracked

1. xai (PhD dissertation)
2. Research Assistant (academic workflow)
3. cc-flow (Kymera AI desktop)
4. astoreyai (personal AI projects)
5. emotional_intelligence_llm (EQ research)
6. stoch (stock scanner)
7. screener (trading scanner)

## Example Output

```
Updated CLAUDE.md with:
- stoch: Version updated to v2.0.0-beta1+28
- Session notes: Added Nov 20 developments
- Patterns: Added project pruning observation
- Last Updated: 2025-11-20
```

## When to Use

- End of work session
- After major milestones
- Weekly reviews (every 5-7 days)
- Before long breaks

## Support

See **SKILL.md** for complete documentation including:
- Detailed analysis process
- Update examples
- Error handling
- Quality checks
