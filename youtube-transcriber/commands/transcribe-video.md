# Download Single Video Transcript

Download YouTube transcript for a single video with automatic timestamp formatting.

## Usage

```
/transcribe-video <URL> [OPTIONS]
```

## Arguments

- `URL` - YouTube video URL or video ID (required)
  - Examples: `https://www.youtube.com/watch?v=VIDEO_ID`
  - `https://youtu.be/VIDEO_ID`
  - `VIDEO_ID`

## Options

- `--format {md|txt}` - Output format (default: md)
- `--output FILE` - Output file path (auto-generated if omitted)

## Examples

```
/transcribe-video https://www.youtube.com/watch?v=dQw4w9WgXcQ
/transcribe-video https://youtu.be/dQw4w9WgXcQ --format txt
/transcribe-video VIDEO_ID --output my_transcript.md
```

## Output

Markdown file with transcript and timestamps:
```
# YouTube Transcript

**Video ID**: dQw4w9WgXcQ
**Downloaded**: 2024-01-15 10:30:45

## Transcript

**[00:00:00]** First line of transcript

**[00:05:30]** Second line of transcript
```

## Notes

- Automatic timestamp formatting (HH:MM:SS)
- Preserves video metadata
- Default output: `transcript_VIDEO_ID.md`
- Supports all YouTube URL formats
