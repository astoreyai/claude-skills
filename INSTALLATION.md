# Installation Guide - Claude Code Productivity Skills

Complete installation instructions for the astoreyai-productivity-skills plugin.

## Prerequisites

- Claude Code (latest version)
- Python 3.7+
- Git

## Installation Methods

### Method 1: Claude CLI (Recommended)

```bash
# Add the marketplace
claude marketplace add https://github.com/astoreyai/claude-skills

# Install the plugin
claude plugin add astoreyai-productivity-skills
```

### Method 2: Manual Git Clone

```bash
# Clone to plugins directory
git clone https://github.com/astoreyai/claude-skills.git \
  ~/.claude/plugins/marketplaces/astoreyai-productivity

# Claude Code will auto-discover the plugin
```

### Method 3: Download ZIP

1. Download latest release from GitHub
2. Extract to `~/.claude/plugins/marketplaces/astoreyai-productivity/`
3. Restart Claude Code

## Verification

Check that the plugin is installed:

```bash
claude plugin list
# Should show: astoreyai-productivity-skills v1.0.0
```

Check that skills are available:

```bash
# List skills
claude skills list | grep memory-keeper
# Should show: memory-keeper
```

## Configuration

### Auto-Run Setup (Optional but Recommended)

The plugin automatically configures the SessionEnd hook. To verify:

```bash
# Check settings.json
cat ~/.claude/settings.json | grep -A10 "hooks"
```

Expected output:
```json
"hooks": {
  "SessionEnd": [
    {
      "matcher": "*",
      "hooks": [
        {
          "type": "command",
          "command": "python3 ${PLUGIN_DIR}/skills/memory-keeper/auto_update.py",
          "timeout": 30
        }
      ]
    }
  ]
}
```

If not present, the plugin will add it on first use.

### Manual Configuration

If you prefer manual control:

1. Edit `~/.claude/settings.json`
2. Remove the `"hooks"` section to disable auto-run
3. Use `/update-memory` command manually when needed

## Testing

### Test the Slash Command

```bash
# In Claude Code, type:
/update-memory
```

Expected: Skill activates and analyzes recent work.

### Test Auto-Run Script

```bash
# Simulate SessionEnd hook
echo '{"session_id": "test-install"}' | \
  python3 ~/.claude/plugins/marketplaces/astoreyai-productivity/skills/memory-keeper/auto_update.py
```

Expected output:
```json
{
  "continue": true,
  "suppressOutput": false,
  "systemMessage": "Memory already current (2025-11-20)"
}
```

### Check Logs

```bash
# View auto-run logs
tail ~/.claude/logs/memory-keeper.log
```

## Troubleshooting

### Plugin Not Found

```bash
# Check installation path
ls -la ~/.claude/plugins/marketplaces/astoreyai-productivity

# Re-clone if missing
git clone https://github.com/astoreyai/claude-skills.git \
  ~/.claude/plugins/marketplaces/astoreyai-productivity
```

### Hook Not Running

```bash
# Check script permissions
chmod +x ~/.claude/plugins/marketplaces/astoreyai-productivity/skills/memory-keeper/auto_update.py

# Verify Python available
which python3

# Test script manually
echo '{}' | python3 ~/.claude/plugins/marketplaces/astoreyai-productivity/skills/memory-keeper/auto_update.py
```

### Skill Not Appearing

```bash
# Restart Claude Code
claude restart

# Rebuild skill cache
claude skills refresh
```

## Uninstallation

### Remove Plugin

```bash
claude plugin remove astoreyai-productivity-skills
```

### Manual Removal

```bash
# Remove directory
rm -rf ~/.claude/plugins/marketplaces/astoreyai-productivity

# Remove from settings.json (if added manually)
# Edit ~/.claude/settings.json and remove "hooks" section
```

### Clean Logs

```bash
# Optional: Remove logs
rm -f ~/.claude/logs/memory-keeper.log
```

## Updating

### Auto-Update (Claude CLI)

```bash
claude plugin update astoreyai-productivity-skills
```

### Manual Update

```bash
cd ~/.claude/plugins/marketplaces/astoreyai-productivity
git pull origin main
```

## Next Steps

After installation:

1. **Read the README**: `skills/memory-keeper/README.md`
2. **Try the command**: `/update-memory`
3. **Check auto-run logs**: `tail ~/.claude/logs/memory-keeper.log`
4. **Review usage guide**: `skills/memory-keeper/USAGE.md`

## Support

- **Issues**: https://github.com/astoreyai/claude-skills/issues
- **Email**: astoreyai@gmail.com

---

**Version**: 1.0.0 | **Last Updated**: 2025-11-20
