# YouTube Transcript Downloader Skill

Extract transcripts from YouTube videos with timestamps. Supports individual videos, playlists, and channels with automatic expansion to all videos.

## Overview

This skill provides a unified interface for downloading YouTube transcripts from any URL format (videos, playlists, channels). Useful for research, content analysis, and workflow automation. No authentication required.

## Capabilities

- **Single Video Download**: Extract transcript from one video with timestamps
- **Batch Processing**: Download transcripts from multiple videos in a file
- **Playlist Expansion**: Automatically extract all videos from playlists
- **Channel Expansion**: Automatically extract all uploads from channels
- **Multiple Formats**: Output as Markdown (.md) or plain text (.txt)
- **Flexible Input**: Handle mixed URL types in batch files
- **Error Handling**: Graceful handling for invalid URLs and restricted videos

## Use Cases

### 1. Download Single Video Transcript
```
/transcribe-video https://www.youtube.com/watch?v=VIDEO_ID
```
Extracts transcript with timestamps, saves as markdown.

### 2. Batch Download from File
```
/transcribe-batch urls.txt
```
Downloads transcripts from all URLs in file (videos, playlists, channels).

### 3. Expand Playlist/Channel
```
/transcribe-expand playlist.txt
```
Extracts all video URLs from playlists and channels, outputs as list.

### 4. In Workflow Context
```
Agent receives: list of YouTube URLs (mixed types)
  ↓
Skill processes: expand playlists/channels if needed
  ↓
Skill outputs: transcripts in markdown format
  ↓
Agent uses: transcripts for analysis, summarization, etc.
```

## Installation

The skill is registered with `claude-skills` plugin. Available commands:
- `/transcribe-video` - Single video
- `/transcribe-batch` - Batch processing
- `/transcribe-expand` - Playlist/channel expansion

## URL Format Support

### Direct Videos (Downloaded)
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `VIDEO_ID` (11-character string)
- With timestamps: `...watch?v=VIDEO_ID&t=10s`
- With playlist: `...watch?v=VIDEO_ID&list=PLAYLIST_ID`

### Playlists (Expanded)
- `https://www.youtube.com/playlist?list=PLAYLIST_ID`
- `https://www.youtube.com/playlist?list=ID&index=5`

### Channels (Expanded)
- New style: `https://www.youtube.com/@username`
- With tabs: `https://www.youtube.com/@username/playlists`
- Legacy: `https://www.youtube.com/user/username`
- Channel ID: `https://www.youtube.com/channel/CHANNEL_ID`
- Custom name: `https://www.youtube.com/c/customname`

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

Create text file with one URL per line. Comments and blank lines supported:

```
# Section 1: Videos
https://www.youtube.com/watch?v=EPqKVUJVftY
https://www.youtube.com/watch?v=m2GxmZky__M

# Section 2: Playlists (auto-expanded)
https://www.youtube.com/playlist?list=PLtqRgJ_TIq8Y6YG8G

# Section 3: Channels (auto-expanded)
https://www.youtube.com/@creator

# Direct IDs
dQw4w9WgXcQ
```

## Skill Functions

### transcribe_single(url: str, format: str = "md") → str
Download transcript for a single video.

**Parameters:**
- `url`: YouTube URL or video ID
- `format`: "md" or "txt" (default: "md")

**Returns:** Transcript text

**Example:**
```python
transcript = transcribe_single("https://youtu.be/VIDEO_ID", format="md")
```

### transcribe_batch(file_path: str, output_dir: str = "transcripts", format: str = "both", expand: bool = True) → dict
Download transcripts from file with mixed URL types.

**Parameters:**
- `file_path`: Path to file with URLs
- `output_dir`: Directory for transcript files
- `format`: "md", "txt", or "both"
- `expand`: Auto-expand playlists/channels (default: True)

**Returns:**
```python
{
    "success_count": 15,
    "error_count": 2,
    "output_dir": "/path/to/transcripts",
    "files": ["transcript_ID1.md", "transcript_ID2.md", ...]
}
```

### expand_urls(file_path: str, output_file: str = "expanded_urls.txt") → dict
Extract all video URLs from playlists and channels.

**Parameters:**
- `file_path`: Path to file with URLs
- `output_file`: Output file path

**Returns:**
```python
{
    "original_count": 5,
    "expanded_count": 150,
    "output_file": "/path/to/expanded_urls.txt",
    "errors": ["Playlist X: error message"]
}
```

## Integration with Other Skills

### Research Assistant
Use with `/analyze-research` to:
1. Expand educational playlists
2. Download transcripts
3. Summarize content
4. Generate citations

### Kymera Integrator
Use with workflow automation:
1. Feed list of URLs (mixed types)
2. Auto-expand and download
3. Process transcripts for analysis
4. Archive results

## Configuration

**Project Location:** `~/projects/youtube-transcriber/`

**Shell Script:** `youtube-transcriber.sh`
```bash
# Direct usage
~/projects/youtube-transcriber/youtube-transcriber.sh urls.txt

# With options
youtube-transcriber.sh urls.txt --output-dir my_folder --format md --expand
```

**Key Files:**
- `src/transcriber.py`: Core transcript fetching
- `src/playlist_parser.py`: Playlist/channel expansion
- `src/cli.py`: Command-line interface
- `youtube-transcriber.sh`: Shell wrapper

## Limitations

- YouTube must allow transcript access (some videos restricted)
- Playlist expansion may be slow for large playlists (100+ videos)
- Channel expansion extracts uploads only (not custom playlists)
- Language support depends on available transcripts (default: English)

## Troubleshooting

**"No transcript found"**
- Video may not have captions
- Check manually on YouTube if captions available

**"Could not extract playlist/channel"**
- URL format may not be recognized
- Verify playlist/channel is public

**"Transcript access denied"**
- YouTube disabled transcripts for this video
- Try another similar video for comparison

## Requirements

- `youtube-transcript-api` (0.6.2): Download transcripts
- `yt-dlp` (≥2024.7.1): Extract playlist/channel videos
- `click` (8.1.7): CLI framework
- `pytest` (7.4.3): Testing

## Author

Aaron Storey | Research & Development (Nov 2025)

## Version

1.0.0 - Initial release with playlist/channel expansion
