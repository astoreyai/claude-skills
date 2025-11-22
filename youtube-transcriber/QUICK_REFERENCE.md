# YouTube Transcriber - Quick Reference Card

## Installation

Skill is registered with `claude-skills` plugin (v1.0.0).

## Usage

### Shell Script (Direct)
```bash
cd ~/projects/youtube-transcriber
./youtube-transcriber.sh urls.txt [OPTIONS]
```

### CLI Commands (In Claude Code)
```bash
/transcribe-video URL [--format md|txt]
/transcribe-batch FILE [--output-dir DIR] [--format md|txt|both] [--expand]
/transcribe-expand FILE [--output-file FILE]
```

## Input Formats

| Format | Example | Processing |
|--------|---------|------------|
| Video | `https://www.youtube.com/watch?v=ABC123` | Download directly |
| Short | `https://youtu.be/ABC123` | Download directly |
| Video ID | `ABC123` | Download directly |
| Playlist | `https://www.youtube.com/playlist?list=PL123` | Expand (--expand) |
| Channel | `https://www.youtube.com/@creator` | Expand (--expand) |
| Mixed file | One URL per line | Auto-detect each |

## Output Files

```
transcript_VIDEO_ID.md       # Markdown with timestamps
transcript_VIDEO_ID.txt      # Plain text with timestamps
```

Example Markdown:
```markdown
# YouTube Transcript

**Video ID**: dQw4w9WgXcQ
**Downloaded**: 2024-01-15 10:30:45

## Transcript

**[00:00:00]** Transcript text

**[00:05:30]** More text
```

## Common Tasks

### Download Single Video
```bash
youtube-transcriber.sh urls.txt  # (with one URL)
# or
/transcribe-video https://youtu.be/VIDEO_ID
```

### Batch Download (Mixed Types)
```bash
# Create file
cat > urls.txt << EOF
https://www.youtube.com/watch?v=VIDEO1
https://www.youtube.com/playlist?list=PL123
https://www.youtube.com/@creator
EOF

# Process (auto-expands playlists/channels)
youtube-transcriber.sh urls.txt --expand
```

### Expand Only (Inspect First)
```bash
youtube-transcriber.sh urls.txt --expand --output-file all_videos.txt
# Check results
wc -l all_videos.txt
# Then batch
youtube-transcriber.sh all_videos.txt
```

### Custom Output
```bash
youtube-transcriber.sh urls.txt \
  --output-dir my_transcripts \
  --format md
```

### Markdown Only (Faster)
```bash
youtube-transcriber.sh urls.txt --format md --expand
```

### From Stdin
```bash
cat playlist_urls.txt | youtube-transcriber.sh -
```

## Options

| Option | Values | Default |
|--------|--------|---------|
| `--output-dir` | PATH | `transcripts` |
| `--format` | md, txt, both | `both` |
| `--expand` | flag | `true` |
| `--no-expand` | flag | - |
| `--timestamps` | flag | `true` |
| `--no-timestamps` | flag | - |

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | No valid URLs |
| 2 | Invalid arguments |
| 3 | Execution failed |

## Performance

| Task | Time |
|------|------|
| Single video | 1-3 sec |
| Small playlist (50 videos) | 5-15 sec |
| Large playlist (500 videos) | 60-120 sec |
| Batch download (100 videos) | 2-5 min |

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "No transcript found" | Video may not have captions; check manually on YouTube |
| "Could not extract playlist" | URL may not be recognized; verify playlist is public |
| "Transcript access denied" | YouTube disabled transcripts for this video |
| Script not found | Run from `~/projects/youtube-transcriber/` |
| No venv | Script auto-creates venv on first run |

## Example Workflows

### Research Paper + Video Content
```bash
# 1. Create file with educational playlists
echo "https://www.youtube.com/playlist?list=PL123" > sources.txt
echo "https://www.youtube.com/@edchannel" >> sources.txt

# 2. Expand and download all
youtube-transcriber.sh sources.txt --expand --output-dir research

# 3. Use transcripts for analysis
# (Feed research/ directory to analysis agent)
```

### Quick Single Download
```bash
/transcribe-video https://youtu.be/VIDEO_ID --format md
```

### Batch Research
```bash
youtube-transcriber.sh urls.txt --format both --expand
# Outputs both .md and .txt versions
# Automatically expands playlists/channels
```

## Key Features

✅ **Auto-Expansion**: Playlists/channels → individual videos
✅ **Mixed Input**: Handle videos, playlists, channels in one file
✅ **Timestamps**: Automatic HH:MM:SS formatting
✅ **Multiple Formats**: Markdown or plain text
✅ **No Auth**: No API keys needed
✅ **Error Handling**: Graceful failures, continues on errors
✅ **Progress Tracking**: Real-time feedback
✅ **Stdin Support**: Can pipe from other commands

## Integration

### With Research Assistant
```
Playlists → youtube-transcriber → Transcripts → literature-reviewer
```

### With Agents
```
User URLs → youtube-transcriber → Transcript Directory → Agent Processing
```

### In Workflows
```
Mixed URLs → expand & download → Processed Transcripts → Analysis → Report
```

## Quick Alias

Add to `~/.zshrc` or `~/.bashrc`:
```bash
alias transcribe="~/projects/youtube-transcriber/youtube-transcriber.sh"
```

Then use:
```bash
transcribe urls.txt --expand
transcribe urls.txt --output-dir research
```

## Documentation

- **SKILL.md**: Full capability overview
- **WORKFLOW_GUIDE.md**: Integration examples and patterns
- **Project README**: Complete usage guide
- **Command docs**: /transcribe-video, /transcribe-batch, /transcribe-expand

## Location

```
Project:      ~/projects/youtube-transcriber/
Script:       ~/projects/youtube-transcriber/youtube-transcriber.sh
Skill:        ~/github/astoreyai/claude-skills/youtube-transcriber/
Commands:     ~/.claude/commands/transcribe-*
```

## Version

1.0.0 - Initial release with full playlist/channel support

---

**Quick Help**: `youtube-transcriber.sh --help`
**Project**: https://github.com/astoreyai/youtube-transcriber
