# System Health Check & Cleanup Skill

Automated system diagnostics and performance optimization for Claude Code.

## Quick Start

**Check system health** (read-only):
```bash
/system-health
```

**Full cleanup** (automated fixes):
```bash
/system-cleanup
```

## What It Does

### Diagnostics (`/system-health`)
- Memory, disk, CPU usage
- Top resource consumers
- Failed systemd services
- Services in crash loops
- Stale processes (>15 min)
- Cache bloat (pip, go-build, mozilla, etc)

**Output**: Human-readable report with recommendations

### Cleanup (`/system-cleanup`)
Automatically fixes:
1. ✅ Disables crashing services (backend-api, orphaned services)
2. ✅ Kills old claude/python processes (>15 min)
3. ✅ Cleans caches:
   - pip (~18GB typical)
   - go-build (~3.3GB typical)
   - mozilla/firefox (~1.5GB typical)
   - playwright, electron, waveterm
4. ✅ Optimizes systemd journal
5. ✅ Reloads systemd configuration

**Output**: Summary with before/after metrics

## Real Impact

**Before**: System glitching, 25GB cache, load spike, crash loop
**After**: Smooth operation, 2GB cache (23GB freed), optimal load

## Installation

Already registered in `~/.claude.json`. No additional setup needed.

Use via:
```bash
claude code
/system-health
/system-cleanup
```

## Parameters

### `/system-health`
- `--verbose`: Show all processes
- `--format json`: Machine-readable output

### `/system-cleanup`
- `--keep-caches`: Skip cache cleanup
- `--dry-run`: Show what would be deleted

## Technical Details

### Sudo Authentication
Uses `~/.local/bin/claude-askpass` for passwordless sudo.
- Automatically configured
- Falls back to interactive prompt if needed

### Safe Operations
- Only deletes **development caches** (pip, go-build, etc)
- Caches **regenerate automatically** on next use
- Only kills **user-owned processes** (not system services)
- Confirmed via process status before killing

### Service Handling
- Detects crash loops (repeated failures in systemd logs)
- Safely disables missing/broken services
- Reloads systemd after changes

## Troubleshooting

**Q: Can I trust the cache cleanup?**
A: Yes. Development caches (pip, go-build, mozilla) regenerate automatically. You'll see a small delay on first use after cleanup, then it's faster.

**Q: Will it break my development environment?**
A: No. It only cleans caches, doesn't touch:
- Virtual environments
- Project code
- Configuration files
- Dependencies

**Q: What if I have custom services?**
A: The skill only disables known crashing services (backend-api). Custom services are not affected.

## Files

- `SKILL.md` - Full documentation
- `system_health_agent.py` - Implementation
- `commands/system-health.md` - Slash command for diagnostics
- `commands/system-cleanup.md` - Slash command for cleanup
- `README.md` - This file

## License

MIT (Part of astoreyai/claude-skills distribution)
