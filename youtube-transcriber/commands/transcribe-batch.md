# Batch Download Transcripts from File

Download transcripts from multiple YouTube videos, playlists, and channels. Automatically expands playlists/channels to individual videos.

## Usage

```
/transcribe-batch <FILE> [OPTIONS]
```

## Arguments

- `FILE` - Path to file with YouTube URLs (one per line)

## Options

- `--output-dir DIR` - Output directory (default: transcripts)
- `--format {md|txt|both}` - Output format (default: both)
- `--timestamps/--no-timestamps` - Include timestamps (default: true)
- `--expand/--no-expand` - Expand playlists/channels (default: true)

## Input File Format

```
# Comments and blank lines are ignored

# Individual videos
https://www.youtube.com/watch?v=EPqKVUJVftY
https://www.youtube.com/watch?v=m2GxmZky__M

# Playlists (auto-expanded)
https://www.youtube.com/playlist?list=PLtqRgJ_TIq8Y6YG8G

# Channels (auto-expanded)
https://www.youtube.com/@creator

# Direct video IDs
dQw4w9WgXcQ
```

## Examples

```
# Basic: download all videos
/transcribe-batch urls.txt

# Custom output directory
/transcribe-batch urls.txt --output-dir my_transcripts

# Markdown only (no expansion)
/transcribe-batch urls.txt --format md --no-expand

# Both formats with custom directory
/transcribe-batch mixed_urls.txt --output-dir research --format both
```

## Processing Logic

1. **Parse input file**: Skip comments (#) and blank lines
2. **Identify URL types**: Detect videos, playlists, channels
3. **Expand (optional)**: Convert playlists/channels to individual videos
4. **Download**: Fetch transcripts for all videos
5. **Save**: Write files to output directory

## Output

For each video, creates file: `transcript_VIDEO_ID.[md|txt]`

Example Markdown output:
```
# YouTube Transcript

**Video ID**: dQw4w9WgXcQ
**Downloaded**: 2024-01-15 10:30:45

## Transcript

**[00:00:00]** Transcript text here

**[00:05:30]** More transcript content
```

## Exit Codes

- `0` - All videos processed successfully
- `1` - No valid URLs found
- `2` - Invalid arguments
- `3` - Execution failed

## Notes

- Supports mixed URL types in single file
- Auto-detects and skips invalid URLs with warnings
- Progress bar shows download status
- Large playlists may take time to expand
