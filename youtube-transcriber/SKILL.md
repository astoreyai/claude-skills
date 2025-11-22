# YouTube Transcriber Skill

Extract transcripts from YouTube videos, playlists, and channels with automatic intelligent processing.

## Overview

One unified command that intelligently assesses input and handles everything—single videos, batch files, playlist expansion, channel extraction. No need to choose between commands; it figures out what to do.

## Capabilities

- **Auto-Detect Input**: Single URL, file of URLs, playlist, channel
- **Smart Expansion**: Automatically expands playlists/channels to individual videos
- **Batch Processing**: Process 1-1000+ videos from mixed input file
- **Timestamps**: Automatic HH:MM:SS formatting on every line
- **Multiple Formats**: Markdown (.md) or plain text (.txt)
- **Error Handling**: Graceful failures, continues on errors

## Quick Usage

```bash
# Single video
/transcribe https://www.youtube.com/watch?v=VIDEO_ID

# Playlist (auto-expands, downloads all)
/transcribe https://www.youtube.com/playlist?list=PL123

# Channel (auto-expands, downloads all uploads)
/transcribe https://www.youtube.com/@creator

# Batch file (auto-detects each URL type, expands if needed)
/transcribe urls.txt

# With options
/transcribe urls.txt --format md --output-dir research
```

## One Command, Many Inputs

| Input | Behavior |
|-------|----------|
| Video URL | Download transcript immediately |
| Playlist URL | Expand to all videos, download transcripts |
| Channel URL | Expand to all uploads, download transcripts |
| File (mixed) | Detect each line, expand playlists/channels, download all |
| File (videos only) | Batch download all transcripts |
| Video ID | Download transcript immediately |

## How It Works

```
Input Assessment
  ↓
├─ Single URL?
│  ├─ Video → Download immediately
│  ├─ Playlist → Expand + Download
│  └─ Channel → Expand + Download
│
└─ File?
   ├─ Detect each line
   ├─ Expand playlists/channels
   └─ Download all transcripts
     ↓
  Output Directory (with all transcripts)
```

## Options

```bash
/transcribe INPUT [OPTIONS]

Options:
  --format {md|txt|both}     Output format (default: both)
  --output-dir DIR           Output directory (default: transcripts)
  --expand/--no-expand       Auto-expand playlists/channels (default: on)
  --inspect                  Show what will be done (no download)
```

## Examples

### Single Video
```bash
/transcribe https://youtu.be/dQw4w9WgXcQ
# → Creates: transcripts/transcript_dQw4w9WgXcQ.md
#           transcripts/transcript_dQw4w9WgXcQ.txt
```

### Playlist (Auto-Expansion)
```bash
/transcribe https://www.youtube.com/playlist?list=PLtqRgJ_TIq8Y6YG8G
# → Expands to all 50 videos
# → Downloads all 50 transcripts
# → Creates: transcripts/transcript_ID1.md, transcript_ID2.md, ...
```

### Batch File (Mixed URLs)
```bash
# Create file:
cat > urls.txt << EOF
# Videos
https://www.youtube.com/watch?v=VIDEO_1
https://www.youtube.com/watch?v=VIDEO_2

# Playlist
https://www.youtube.com/playlist?list=PL123

# Channel
https://www.youtube.com/@creator

# Direct ID
dQw4w9WgXcQ
EOF

# Process:
/transcribe urls.txt
# → Detects all 4 items
# → Expands playlist → 50 videos
# → Expands channel → 100 uploads
# → Downloads all 152 transcripts
```

### Inspect Before Processing
```bash
/transcribe urls.txt --inspect
# → Shows what will be processed
# → No download, just analysis
# → Useful for large playlists
```

### Custom Format/Location
```bash
/transcribe urls.txt --format md --output-dir research
# → Markdown only (faster)
# → Saves to: research/
```

## Output Format

### Markdown (.md)
```markdown
# YouTube Transcript

**Video ID**: dQw4w9WgXcQ
**Downloaded**: 2024-01-15 10:30:45

## Transcript

**[00:00:00]** Never gonna give you up

**[00:05:30]** Never gonna let you down
```

### Plain Text (.txt)
```
YouTube Transcript: dQw4w9WgXcQ
Downloaded: 2024-01-15 10:30:45
------------------------------------------------------------

[00:00:00] Never gonna give you up
[00:05:30] Never gonna let you down
```

## Input File Format

One URL per line, comments and blanks ignored:

```
# Section 1: Videos
https://www.youtube.com/watch?v=EPqKVUJVftY
https://www.youtube.com/watch?v=m2GxmZky__M

# Section 2: Playlists (auto-expanded)
https://www.youtube.com/playlist?list=PLtqRgJ_TIq8Y6YG8G

# Section 3: Channels (auto-expanded)
https://www.youtube.com/@farshadnoravesh

# Direct IDs
dQw4w9WgXcQ
```

## Supported URL Formats

- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `VIDEO_ID` (direct 11-character ID)
- `https://www.youtube.com/watch?v=VIDEO_ID&t=10s` (with timestamp)
- `https://www.youtube.com/playlist?list=PLAYLIST_ID` (auto-expands)
- `https://www.youtube.com/@username` (auto-expands)
- `https://www.youtube.com/user/username` (legacy, auto-expands)
- `https://www.youtube.com/channel/CHANNEL_ID` (auto-expands)

## Use Cases

### Research Workflow
```bash
# Create file with educational playlists and channels
echo "https://www.youtube.com/playlist?list=PL..." > sources.txt
echo "https://www.youtube.com/@educator" >> sources.txt

# One command: expand, download, ready for analysis
/transcribe sources.txt --output-dir research
```

### Content Curation
```bash
# Download transcripts from multiple creators
/transcribe creators.txt --format md
# → All uploads from all channels
# → Organized transcripts ready for processing
```

### Quick Lookup
```bash
# Just need one video's transcript
/transcribe https://youtu.be/VIDEO_ID
```

### Batch Research
```bash
# Process everything at once
/transcribe mixed_urls.txt --output-dir analysis
# → Auto-detects each line
# → Auto-expands playlists/channels
# → Downloads all transcripts
# → Organized in output-dir
```

## Integration with Agents

### In Workflow
```
Agent receives: List of YouTube URLs (mixed types)
  ↓
/transcribe urls.txt --inspect          (check what will process)
  ↓
/transcribe urls.txt --output-dir data  (download all transcripts)
  ↓
Agent reads transcript directory
  ↓
Agent processes/analyzes transcripts
  ↓
Agent generates report
```

### Function Call (Python)
```python
from skill import transcribe

result = transcribe(
    input="urls.txt",
    format="md",
    output_dir="transcripts",
    expand=True,
    inspect=False
)

# Returns:
# {
#   "success": True,
#   "processed": 150,
#   "output_dir": "transcripts",
#   "files": ["transcript_ID1.md", ...]
# }
```

## Limitations

- YouTube must allow transcripts for the video
- Some videos may have restricted captions
- Large playlists (500+ videos) expand slowly
- Language support depends on available transcripts (default: English)

## Requirements

- `youtube-transcript-api` (0.6.2)
- `yt-dlp` (≥2024.7.1)
- `click` (8.1.7)

## Author

Aaron Storey | Research & Development (Nov 2025)

## Version

1.1.0 - Unified single-command interface with automatic assessment
