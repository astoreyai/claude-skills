---
name: worklog
description: >
  Unified worklog system. Synthesizes session work into daily markdown files
  with clean bullet points. Supports weekly rollups for Slack #progress sharing.
  Replaces fragmented checkpoint/session-state/weekly-notes systems.
version: 1.0.0
author: Aaron Storey
user-invocable: true
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
---

# /worklog - Unified Worklog System

One command to rule them all. Synthesizes your Claude sessions into shareable daily worklogs.

## Usage

```
/worklog              # Today's work summary (aggregated across all sessions)
/worklog --morning    # Yesterday's comprehensive rollup (for morning standup)
/worklog --weekly     # Weekly rollup since last Monday
/worklog --yesterday  # Yesterday's summary
/worklog --slack      # Discord/Slack-optimized format
```

## What It Does

### Automatic (SessionEnd Hook)
Every session end automatically appends to `~/worklog/YYYY-MM-DD.md`:
- Completed tasks from todo list
- In-progress tasks
- Modified files (uncommitted git changes)

### Manual (`/worklog` command)
1. **Scans** session checkpoints and state files for the target date(s)
2. **Extracts** files modified, tasks completed, decisions made, blockers
3. **Synthesizes** into clean, human-readable bullet points
4. **Writes** to `~/worklog/YYYY-MM-DD.md`
5. **Outputs** Slack-ready summary for #progress

## Output Format

### Daily (`/worklog`)

```markdown
# 2026-01-12 (Sunday)

## Completed
- Built unified /worklog skill for worklog system
- Investigated hook configurations across plugins

## In Progress
- PhD thesis experiments (85% ready)

## Files Modified
- ~/.claude/skills/worklog/SKILL.md
- ~/.claude/skills/worklog/worklog.py

## Decisions
- Consolidated 3 overlapping systems into single worklog

## Blockers
- None
```

### Weekly (`/worklog --weekly`)

```markdown
# Week 2, 2026 (Jan 6-12)

## Summary
5 days active, 23 tasks completed, 3 projects touched

## By Project
### xai
- Thesis experiments 6.1-6.3 in progress
- Committee feedback incorporated

### ww
- Memory consolidation tests passing

## Key Decisions
- ...

## Next Week
- ...
```

## Configuration

**Worklog Location**: `~/worklog/` (git-tracked)
**Source Data**:
- `~/.claude/worklogs/{project}/worklog-*.json`
- `~/.claude/session-state/{project}/session-*.json`
- `~/Documents/Obsidian/Aaron/Session-Logs/`

## Discord Integration (Automated)

Cron job posts to Discord #progress at 5pm daily:
```
0 17 * * * python3 ~/.claude/skills/worklog/post_to_discord.py
```

### Setup Discord Webhook
```bash
python3 ~/.claude/skills/worklog/post_to_discord.py --setup
```

### Manual Post
```bash
python3 ~/.claude/skills/worklog/post_to_discord.py           # Today
python3 ~/.claude/skills/worklog/post_to_discord.py --yesterday  # Yesterday
python3 ~/.claude/skills/worklog/post_to_discord.py --dry-run    # Preview
```

### Config
Webhook URL: `~/.config/worklog/discord-webhook`
