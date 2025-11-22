# Expand Playlists/Channels to Video List

Extract all video URLs from playlists and channels. Useful for converting a single playlist into a list of individual videos for batch processing.

## Usage

```
/transcribe-expand <FILE> [OPTIONS]
```

## Arguments

- `FILE` - Path to file with playlist/channel URLs or mixed URLs

## Options

- `--output-file FILE` - Output file for expanded URLs (default: expanded_urls.txt)

## Input Format

```
# File can contain any mix of:

# Individual videos (kept as-is)
https://www.youtube.com/watch?v=VIDEO_ID1
https://youtu.be/VIDEO_ID2

# Playlists (expanded to all videos)
https://www.youtube.com/playlist?list=PLtqRgJ_TIq8Y6YG8G

# Channels (expanded to all uploads)
https://www.youtube.com/@creator
https://www.youtube.com/user/username

# Direct IDs (kept as-is)
dQw4w9WgXcQ
```

## Examples

```
# Expand playlists in file
/transcribe-expand playlists.txt

# Custom output file
/transcribe-expand sources.txt --output-file all_videos.txt

# Two-step workflow
/transcribe-expand urls.txt --output-file expanded.txt
# Then use with /transcribe-batch expanded.txt
```

## Output Format

Plain text file, one URL per line:
```
https://www.youtube.com/watch?v=VIDEO_ID1
https://www.youtube.com/watch?v=VIDEO_ID2
https://www.youtube.com/watch?v=VIDEO_ID3
...
```

## Return Information

Shows:
- Original URL count
- Expanded video count
- Output file location
- Any errors during expansion

## URL Expansion

**Playlists:**
- Input: `https://www.youtube.com/playlist?list=PLAYLIST_ID`
- Output: All videos in playlist (can be 10-1000+)

**Channels:**
- Input: `https://www.youtube.com/@username`
- Output: All uploads from channel

**Videos:**
- Input: `https://www.youtube.com/watch?v=VIDEO_ID`
- Output: Kept as-is (no expansion)

## Use Cases

### 1. Convert Playlist to Batch File
```
/transcribe-expand playlist.txt --output-file videos.txt
/transcribe-batch videos.txt
```

### 2. Combine Multiple Sources
```
# Create file with playlists and channels
cat > sources.txt << EOF
https://www.youtube.com/playlist?list=PL1
https://www.youtube.com/@creator1
https://www.youtube.com/@creator2
EOF

# Expand all to individual videos
/transcribe-expand sources.txt --output-file all_videos.txt

# Download all transcripts
/transcribe-batch all_videos.txt
```

### 3. Inspect Expansion Results
```
# See how many videos will be processed
/transcribe-expand playlists.txt

# Check output before batch processing
head -20 expanded_urls.txt
wc -l expanded_urls.txt
```

## Notes

- Large playlists (100+ videos) may take time to expand
- Channel expansion extracts uploads only (not custom playlists)
- Errors for individual playlists don't stop processing
- All URL formats automatically supported
