# YouTube Transcriber - Quick Reference

**One command. Everything handled.**

## Installation

Skill registered with `claude-skills` plugin (v1.1.0).

## One Command: `/transcribe`

```bash
/transcribe INPUT [--format md|txt|both] [--output-dir DIR] [--inspect]
```

## Input Types (Auto-Detected)

| Input | Example | What Happens |
|-------|---------|--------------|
| Video | `https://youtu.be/ABC123` | Download |
| Playlist | `https://www.youtube.com/playlist?list=PL123` | Expand + Download all |
| Channel | `https://www.youtube.com/@creator` | Expand + Download all |
| File | `urls.txt` (mixed) | Detect each, expand if needed, download all |
| Video ID | `ABC123def456789` | Download |

## Quick Examples

```bash
# Single video
/transcribe https://youtu.be/VIDEO_ID

# Playlist (auto-expands all, downloads all)
/transcribe https://www.youtube.com/playlist?list=PL123

# Channel (auto-expands all uploads, downloads all)
/transcribe https://www.youtube.com/@creator

# Batch file (auto-detects each line, expands playlists/channels, downloads all)
/transcribe urls.txt

# Inspect first (see what will be processed)
/transcribe urls.txt --inspect

# Custom output
/transcribe urls.txt --format md --output-dir research
```

## Options

| Option | Values | Default | Use |
|--------|--------|---------|-----|
| `--format` | md, txt, both | both | Output format |
| `--output-dir` | PATH | transcripts | Output directory |
| `--expand` | (flag) | on | Auto-expand playlists/channels |
| `--no-expand` | (flag) | - | Disable expansion |
| `--inspect` | (flag) | - | Show what will process (no download) |

## Supported URLs

- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/watch?v=VIDEO_ID&t=10s`
- `https://www.youtube.com/playlist?list=PLAYLIST_ID`
- `https://www.youtube.com/@username`
- `https://www.youtube.com/user/username`
- `https://www.youtube.com/channel/CHANNEL_ID`
- `VIDEO_ID` (direct 11-character ID)

## Input File Format

```
# Comments start with #
# Blank lines ignored

# Videos (downloaded as-is)
https://www.youtube.com/watch?v=VIDEO_1
https://www.youtube.com/watch?v=VIDEO_2

# Playlists (auto-expanded to all videos)
https://www.youtube.com/playlist?list=PL123

# Channels (auto-expanded to all uploads)
https://www.youtube.com/@creator

# Direct IDs
VIDEO_ID123456789AB
```

## Output

For each video:
- `transcript_VIDEO_ID.md` - Markdown with timestamps
- `transcript_VIDEO_ID.txt` - Plain text with timestamps

Example:
```
**[00:00:00]** Transcript text here
**[00:05:30]** More content here
```

## Common Tasks

### Download 1 Video
```bash
/transcribe https://youtu.be/ABC123
```

### Download Playlist (All Videos)
```bash
/transcribe https://www.youtube.com/playlist?list=PL123
# → Auto-expands
# → Downloads all videos
```

### Batch Download (Mixed)
```bash
# File with videos, playlists, channels mixed
/transcribe urls.txt
# → Auto-detects each line
# → Expands playlists/channels
# → Downloads all
```

### Check Before Processing
```bash
/transcribe urls.txt --inspect
# → Shows what will be processed
# → No download
```

### Markdown Only
```bash
/transcribe urls.txt --format md
# → Faster
# → Markdown only
```

### Custom Location
```bash
/transcribe urls.txt --output-dir my_transcripts
```

## Performance

| Task | Time |
|------|------|
| Single video | 1-3 sec |
| Playlist (50 videos) | 5-15 sec expand + 2 min download |
| Channel (100+ videos) | 30+ sec expand + 5+ min download |
| Batch (100 videos) | 2-5 minutes |

## Smart Behavior

✅ Single URL? → Detects type → Downloads

✅ Playlist URL? → Expands → Downloads all

✅ Channel URL? → Expands → Downloads all

✅ File with mixed? → Detects each → Expands → Downloads all

✅ Error? → Continues on failures → Shows summary

## Troubleshooting

| Issue | Fix |
|-------|-----|
| "No transcript found" | Video may not have captions |
| "Could not extract playlist" | Verify URL is public |
| "Transcript access denied" | YouTube disabled transcripts |
| Large playlist slow | Use `--inspect` to check count first |

## Workflow Example

```bash
# Step 1: Create file with your sources
cat > sources.txt << EOF
https://www.youtube.com/watch?v=VIDEO_1
https://www.youtube.com/playlist?list=PL123
https://www.youtube.com/@creator
EOF

# Step 2: Inspect (optional)
/transcribe sources.txt --inspect

# Step 3: Download all
/transcribe sources.txt --output-dir transcripts
# → Auto-detects: 1 video, 1 playlist (50), 1 channel (100)
# → Expands: playlist & channel
# → Downloads: 151 transcripts to transcripts/
```

## Integration Points

✅ **Shell Script**: `~/projects/youtube-transcriber/youtube-transcriber.sh`

✅ **Claude Code Command**: `/transcribe`

✅ **Python Function**: `transcribe(input, format, output_dir, expand, inspect)`

✅ **Agents**: Feed transcript directory to analysis agents

## Key Features

✅ One command for everything
✅ Auto-detects input type
✅ Auto-expands playlists/channels
✅ Handles mixed URLs
✅ No API keys needed
✅ Timestamps automatic
✅ Multiple formats
✅ Error handling

## Docs

- **SKILL.md**: Full capability overview
- **WORKFLOW_GUIDE.md**: Integration examples
- **commands/transcribe.md**: Complete command reference
- **Project README**: Full documentation

## Quick Alias

```bash
alias yt="cd ~/projects/youtube-transcriber && ./youtube-transcriber.sh"
```

Then:
```bash
yt urls.txt --expand
yt urls.txt --format md
```

---

**That's it.** One command, handles everything.

`/transcribe INPUT [OPTIONS]`
