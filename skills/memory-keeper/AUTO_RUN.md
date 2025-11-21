# Memory Keeper - Auto-Run Configuration

The memory-keeper skill can run automatically at the end of each Claude Code session.

## Current Status

✅ **ENABLED** - SessionEnd hook configured in `~/.claude/settings.json`

## How It Works

When you exit Claude Code, the SessionEnd hook automatically:
1. Triggers `auto_update.py` script
2. Checks if CLAUDE.md needs updating
3. Updates "Last Updated" timestamp if needed
4. Logs execution to `~/.claude/logs/memory-keeper.log`
5. Returns success/failure status

## Configuration

**Location**: `~/.claude/settings.json`

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
          }
        ]
      }
    ]
  }
}
```

**Key Parameters**:
- **matcher**: `"*"` = runs for all session ends
- **timeout**: 30 seconds max execution time
- **command**: Path to auto-update script

## What Gets Auto-Updated

Currently, the auto-run script performs minimal updates:
- **Last Updated** timestamp (only if date changed)

**Future enhancements** (run `/update-memory` manually for these):
- Project status changes
- Session notes additions
- Pattern observations
- Infrastructure updates

## Why Minimal Auto-Updates?

**Philosophy**: Auto-run should be **lightweight and non-intrusive**.

- ✅ Updates timestamp (safe, always correct)
- ❌ Doesn't analyze git repos (could be slow)
- ❌ Doesn't modify project sections (requires human review)
- ❌ Doesn't add session notes (needs context)

**For comprehensive updates**, use `/update-memory` manually when needed.

## Logging

Every auto-run execution is logged:

**Log file**: `~/.claude/logs/memory-keeper.log`

**Example log entry**:
```
[2025-11-20T22:30:15] SessionEnd hook triggered
  Session ID: abc123
  Working dir: /home/aaron/projects/xai
  Updated Last Updated to 2025-11-20
```

**View logs**:
```bash
tail -20 ~/.claude/logs/memory-keeper.log
```

## Testing

**Test the hook manually**:
```bash
# Simulate hook input
echo '{"session_id": "test-123", "cwd": "/home/aaron"}' | \
  python3 ~/.claude/skills/memory-keeper/auto_update.py
```

**Expected output**:
```json
{
  "continue": true,
  "suppressOutput": false,
  "systemMessage": "Memory updated: Last Updated → 2025-11-20"
}
```

**Check logs**:
```bash
cat ~/.claude/logs/memory-keeper.log
```

## Verify Hook Registration

```bash
# Check if hook is registered (requires Claude Code CLI)
claude /hooks

# Should show:
# SessionEnd:
#   - auto_update.py (timeout: 30s)
```

## Enabling/Disabling

### Disable Auto-Run

**Option 1**: Remove from settings.json
```bash
# Edit ~/.claude/settings.json and remove the "hooks" section
```

**Option 2**: Comment out (JSON doesn't support comments, so use Option 1)

### Re-enable Auto-Run

Add the hook configuration back to `~/.claude/settings.json` (see Configuration section above).

## Manual vs Auto-Run

| Feature | Manual `/update-memory` | Auto-Run SessionEnd |
|---------|------------------------|---------------------|
| **Trigger** | User invoked | Automatic on session end |
| **Scope** | Full analysis (7 days) | Minimal (timestamp only) |
| **Git analysis** | Yes | No |
| **Project updates** | Yes | No |
| **Session notes** | Yes | No |
| **Speed** | ~10-30 seconds | ~1 second |
| **Use case** | Weekly reviews, after milestones | Daily timestamp maintenance |

**Recommendation**: Use both!
- Auto-run keeps timestamp current effortlessly
- Manual updates capture significant developments

## Advanced Configuration

### Increase Timeout

If auto_update.py needs more time:
```json
{
  "timeout": 60  // 60 seconds instead of 30
}
```

### Add Logging Verbosity

Modify `auto_update.py` to log more details:
```python
with open(log_file, "a") as f:
    f.write(f"  Current content hash: {hash(content)}\n")
    f.write(f"  Modified: {claude_md.stat().st_mtime}\n")
```

### Chain Multiple Hooks

Run multiple commands on SessionEnd:
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
            "command": "bash ~/.claude/scripts/backup-session.sh",
            "timeout": 15
          }
        ]
      }
    ]
  }
}
```

## Troubleshooting

### Hook Not Running

**Check**:
1. Settings file valid JSON: `python3 -m json.tool ~/.claude/settings.json`
2. Script executable: `chmod +x ~/.claude/skills/memory-keeper/auto_update.py`
3. Python3 available: `which python3`
4. Logs directory exists: `mkdir -p ~/.claude/logs`

**Test manually**:
```bash
echo '{"session_id":"test"}' | python3 ~/.claude/skills/memory-keeper/auto_update.py
```

### Permission Errors

```bash
chmod +x ~/.claude/skills/memory-keeper/auto_update.py
chmod 644 ~/.claude/CLAUDE.md
```

### Hook Timing Out

Increase timeout in settings.json:
```json
"timeout": 60  // Increase from 30 to 60 seconds
```

### No Log Output

Ensure logs directory exists:
```bash
mkdir -p ~/.claude/logs
touch ~/.claude/logs/memory-keeper.log
```

## Safety Features

The auto-update script is designed to be **safe and non-destructive**:

✅ **Read-first**: Always reads CLAUDE.md before modifying
✅ **Minimal changes**: Only updates timestamp field
✅ **Error handling**: Logs errors, doesn't crash session end
✅ **Idempotent**: Safe to run multiple times per day
✅ **Atomic writes**: File written completely or not at all
✅ **Logging**: All executions logged for audit

## Future Enhancements

Potential additions to auto-run (not yet implemented):
- [ ] Analyze last 1-2 git commits only (quick check)
- [ ] Detect new tags and add to session notes
- [ ] Track conversation count statistics
- [ ] Backup CLAUDE.md to versioned storage
- [ ] Send desktop notification on update

**For now**: Keep auto-run minimal, use `/update-memory` for comprehensive updates.

## Integration with Other Systems

The SessionEnd hook can integrate with:
- **Git**: Auto-commit CLAUDE.md changes
- **Syncthing**: Trigger sync after update
- **Notifications**: Desktop notification on update
- **Backup**: Copy to timestamped backup location

**Example**: Auto-commit CLAUDE.md on session end:
```json
{
  "hooks": {
    "SessionEnd": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/skills/memory-keeper/auto_update.py && cd ~/.claude && git add CLAUDE.md && git commit -m 'Auto-update: Session end' 2>/dev/null || true",
            "timeout": 45
          }
        ]
      }
    ]
  }
}
```

## Summary

**Current Setup**:
- ✅ SessionEnd hook enabled
- ✅ Auto-updates timestamp daily
- ✅ Logs all executions
- ✅ Safe, minimal, non-intrusive

**Usage**:
- Auto-run handles daily timestamp maintenance
- Use `/update-memory` manually for comprehensive updates
- Check logs: `~/.claude/logs/memory-keeper.log`
- Disable: Remove "hooks" from settings.json

**Philosophy**: Let automation handle routine maintenance, keep human oversight for significant updates.
