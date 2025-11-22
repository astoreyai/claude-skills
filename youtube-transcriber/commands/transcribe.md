# Download YouTube Transcripts

One command for everything: single videos, batch files, playlists, channels. Automatically detects input and handles all processing.

## Usage

```bash
/transcribe INPUT [OPTIONS]
```

## Input Types (Auto-Detected)

| Input | Example | Behavior |
|-------|---------|----------|
| Video URL | `https://youtu.be/VIDEO_ID` | Download immediately |
| Playlist URL | `https://www.youtube.com/playlist?list=...` | Expand to all videos, download |
| Channel URL | `https://www.youtube.com/@creator` | Expand to all uploads, download |
| File | `urls.txt` | Auto-detect each line, expand playlists/channels, download all |
| Video ID | `dQw4w9WgXcQ` | Download immediately |

## Options

```
--format {md|txt|both}   Output format (default: both)
--output-dir DIR         Output directory (default: transcripts)
--expand/--no-expand     Auto-expand playlists/channels (default: on)
--inspect                Show what will be processed (no download)
```

## Examples

### Single Video
```bash
/transcribe https://youtu.be/VIDEO_ID
/transcribe VIDEO_ID
# → Downloads transcript, saves as markdown + text
```

### Playlist (Auto-Expands All Videos)
```bash
/transcribe https://www.youtube.com/playlist?list=PLtqRgJ_TIq8Y6YG8G
# → Detects playlist
# → Expands to all 50 videos
# → Downloads all 50 transcripts
# → Saves to: transcripts/transcript_ID1.md, transcript_ID2.md, ...
```

### Channel (Auto-Expands All Uploads)
```bash
/transcribe https://www.youtube.com/@creator
# → Detects channel
# → Expands to all uploads (100+)
# → Downloads all transcripts
```

### Batch File (Mixed URLs)
```bash
# File content:
# https://www.youtube.com/watch?v=VIDEO_1
# https://www.youtube.com/watch?v=VIDEO_2
# https://www.youtube.com/playlist?list=PL123
# https://www.youtube.com/@channel
# VIDEO_ID

/transcribe urls.txt
# → Detects 5 items (2 videos, 1 playlist, 1 channel, 1 ID)
# → Expands: playlist → 50 videos, channel → 100 videos
# → Total: 152 videos to download
# → Downloads all transcripts
```

### Inspect Before Processing
```bash
/transcribe urls.txt --inspect
# → Shows what will be processed
# → No download
# → Useful for large playlists to verify count
```

### Custom Output
```bash
/transcribe urls.txt --format md --output-dir research
# → Markdown only (no text files, faster)
# → Saves to: research/
```

### Markdown Only
```bash
/transcribe urls.txt --format md
# → Faster processing (no text generation)
# → Cleaner output
```

## Output

Each video generates:
- `transcript_VIDEO_ID.md` - Formatted markdown with timestamps
- `transcript_VIDEO_ID.txt` - Plain text with timestamps

Format:
```
**[00:00:00]** Transcript text here
**[00:05:30]** More transcript content
```

## Input File Format

One URL per line, comments and blanks supported:

```
# Videos
https://www.youtube.com/watch?v=VIDEO_1
https://www.youtube.com/watch?v=VIDEO_2

# Playlists (auto-expanded)
https://www.youtube.com/playlist?list=PL123

# Channels (auto-expanded)
https://www.youtube.com/@creator

# Direct IDs
VIDEO_ID123456789AB
```

## Supported URL Formats

- Standard: `https://www.youtube.com/watch?v=VIDEO_ID`
- Short: `https://youtu.be/VIDEO_ID`
- With timestamp: `https://www.youtube.com/watch?v=VIDEO_ID&t=10s`
- Playlist: `https://www.youtube.com/playlist?list=PLAYLIST_ID`
- Channel (@): `https://www.youtube.com/@username`
- Channel (user): `https://www.youtube.com/user/username`
- Channel (ID): `https://www.youtube.com/channel/CHANNEL_ID`
- Direct ID: `VIDEO_ID` (11 characters)

## Smart Behavior

- **Single URL**: Downloads immediately
- **Playlist URL**: Auto-expands, downloads all
- **Channel URL**: Auto-expands, downloads all uploads
- **Mixed file**: Detects each type, expands as needed
- **Errors**: Graceful handling, continues on failures

## Typical Workflow

```bash
# Step 1: Create file with mixed URLs
echo "https://www.youtube.com/watch?v=VIDEO_ID" > sources.txt
echo "https://www.youtube.com/playlist?list=..." >> sources.txt
echo "https://www.youtube.com/@creator" >> sources.txt

# Step 2: Inspect (optional)
/transcribe sources.txt --inspect
# → Shows: 1 video, 1 playlist (50 videos), 1 channel (100 videos)
# → Total: 151 to process

# Step 3: Download all transcripts
/transcribe sources.txt --output-dir transcripts
# → Auto-expands playlists/channels
# → Downloads all 151 transcripts
# → Organizes in transcripts/ directory
```

## Notes

- Large playlists (500+ videos) may take time to expand
- Channel expansion extracts uploads only (not custom playlists)
- Some videos may not have transcripts available
- No API keys or authentication required
