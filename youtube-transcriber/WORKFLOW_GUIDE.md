# YouTube Transcriber - Workflow Integration Guide

## One Command: `/transcribe`

The skill provides a single, unified command that intelligently assesses and handles any YouTube input:

```bash
/transcribe INPUT [OPTIONS]
```

It automatically:
1. **Detects** input type (single URL, file, playlist, channel)
2. **Assesses** what needs to be done
3. **Expands** playlists/channels if needed
4. **Downloads** all transcripts
5. **Organizes** output

## Real-World Workflows

### Workflow 1: Educational Content Curation

**Scenario**: Build learning resource from multiple educators

```bash
# Create source file
cat > educators.txt << EOF
# Math channel
https://www.youtube.com/@3blue1brown

# Physics channel
https://www.youtube.com/@veritasium

# Educational playlist
https://www.youtube.com/playlist?list=PLcourse123

# Individual video
https://www.youtube.com/watch?v=dQw4w9WgXcQ
EOF

# One command: assess → expand → download all
/transcribe educators.txt --output-dir courses

# Result:
# - 3Blue1Brown: 100+ uploads → 100+ transcripts
# - Veritasium: 200+ uploads → 200+ transcripts
# - Playlist: 50 videos → 50 transcripts
# - Individual: 1 video → 1 transcript
# Total: 351 transcripts, organized in courses/
```

### Workflow 2: Research Literature + Video Content

**Scenario**: Combine academic papers with relevant video material

```bash
# Create file with research sources
cat > research.txt << EOF
# Video sources
https://www.youtube.com/watch?v=research_video_1
https://www.youtube.com/watch?v=research_video_2

# Research playlist
https://www.youtube.com/playlist?list=PLresearch

# Expert channel
https://www.youtube.com/@researcher
EOF

# Get all transcripts
/transcribe research.txt --format md --output-dir research_data

# Agent then:
# 1. Reads all transcripts from research_data/
# 2. Analyzes video content
# 3. Combines with paper analysis
# 4. Generates comprehensive research report
```

### Workflow 3: Quick Single Lookup

**Scenario**: User needs one video's transcript immediately

```bash
# Just paste the URL
/transcribe https://youtu.be/VIDEO_ID

# Done! Transcript available in transcripts/ directory
```

### Workflow 4: Batch Research from Mixed Sources

**Scenario**: Process everything at once, no manual decisions

```bash
# File with everything mixed (videos, playlists, channels, IDs)
/transcribe all_sources.txt --inspect
# → Shows: 5 videos, 3 playlists, 2 channels, 4 IDs
# → Total: Would process ~400 videos

# Download all
/transcribe all_sources.txt --output-dir research
# ✅ All transcripts ready for analysis agents
```

## Workflow Integration Points

### With Research Assistant

```
User Input: URLs (any mix)
    ↓
/transcribe urls.txt                    (assess + expand + download)
    ↓
research-assistant skill reads transcripts directory
    ↓
Agents analyze for:
  - Key findings
  - Quotes and evidence
  - Citations
  - Themes
    ↓
Generate research report
```

### With Kymera Integrator

```
Mixed URLs received
    ↓
/transcribe urls.txt --inspect          (check scope)
    ↓
/transcribe urls.txt --output-dir data  (process everything)
    ↓
kymera-integrator reads transcript directory
    ↓
Feed to downstream agents:
  - Content analysis
  - Metadata extraction
  - Integration with other tools
```

### With Custom Agents

```
Agent receives: List of YouTube URLs
    ↓
Agent calls: /transcribe urls.txt --format md
    ↓
Agent reads result directory
    ↓
Agent processes each transcript for:
  - Sentiment analysis
  - Key topic extraction
  - Summarization
  - Classification
    ↓
Agent outputs: Analysis report
```

## Smart Behavior Examples

### Example 1: Single Video
```bash
/transcribe https://youtu.be/ABC123

# Assessment:
# - Detects: Single video URL
# - Action: Download immediately
# - Time: 1-3 seconds

# Result: transcript_ABC123.md + .txt
```

### Example 2: Playlist
```bash
/transcribe https://www.youtube.com/playlist?list=PL123

# Assessment:
# - Detects: Playlist URL
# - Scope: 50 videos in playlist
# - Action: Expand → Download all 50

# Result: 50 transcript files
```

### Example 3: Channel
```bash
/transcribe https://www.youtube.com/@creator

# Assessment:
# - Detects: Channel URL
# - Scope: 150 uploads from channel
# - Action: Expand → Download all 150

# Result: 150 transcript files
```

### Example 4: Mixed File
```bash
/transcribe urls.txt

# Assessment:
# - Line 1: Video → Download
# - Line 2: Playlist → Expand to 50 videos, download
# - Line 3: Channel → Expand to 100 videos, download
# - Line 4: Video ID → Download
# Total: 152 videos

# Result: 152 transcript files
```

### Example 5: Inspect First
```bash
/transcribe huge_playlist.txt --inspect

# Assessment (no download):
# - Detects: 3 playlists, 2 channels, 5 videos
# - Scope: Would expand to 500+ videos
# - Output: Shows what would be processed

# Decision: User sees it's large, maybe reduces scope
# or proceeds with full download
```

## Command Variations

### Markdown Only (Faster)
```bash
/transcribe urls.txt --format md
# → No text generation
# → Faster processing
# → Clean output
```

### Custom Location
```bash
/transcribe urls.txt --output-dir my_research
# → Saves to my_research/ instead of transcripts/
```

### Disable Expansion (Skip Playlists/Channels)
```bash
/transcribe urls.txt --no-expand
# → Only downloads individual videos
# → Skips playlists/channels with warnings
# → Useful for testing single videos
```

### Inspect Only (No Download)
```bash
/transcribe urls.txt --inspect
# → Shows assessment
# → No download
# → Good for checking scope before processing
```

## Typical Workflow Steps

### Step 1: Prepare
```bash
# Gather all your URLs (any format)
cat > sources.txt << EOF
https://www.youtube.com/watch?v=VIDEO_1
https://www.youtube.com/playlist?list=...
https://www.youtube.com/@creator
EOF
```

### Step 2: Inspect (Optional)
```bash
# See what will be processed
/transcribe sources.txt --inspect
# → Shows: 2 videos, 1 playlist, 1 channel
# → Estimated: 50+ videos to download
```

### Step 3: Process
```bash
# One command handles everything
/transcribe sources.txt --output-dir transcripts
# → Detects each URL type
# → Expands playlists/channels automatically
# → Downloads all transcripts
# → Saves to transcripts/
```

### Step 4: Use Results
```bash
# Your agent reads the transcript directory
# and processes however needed:
# - Analysis
# - Summarization
# - Extraction
# - Classification
# - Whatever your workflow requires
```

## Error Handling

### Graceful Failures
```bash
/transcribe urls.txt
# → Processes all URLs
# → Some fail? Continues on
# → Shows summary:
#   ✓ 48 successful
#   ✗ 2 failed (transcript not available)
#   → Results still available in output-dir/
```

### Large Playlist Handling
```bash
/transcribe huge_list.txt --inspect
# → Shows: "Would process 1000+ videos"

# Options:
# 1. Proceed with full download
# 2. Edit file to reduce scope
# 3. Process in batches
```

## Performance Considerations

| Scenario | Time | Notes |
|----------|------|-------|
| Single video | 1-3 sec | Immediate |
| Small playlist (50) | 15 sec expand + 2 min | Fast |
| Large playlist (500) | 2-5 min expand + 20 min | Plan accordingly |
| Channel (100+ uploads) | 1+ min expand + 5+ min | Depends on upload count |
| Batch (100 videos) | 2-5 minutes | Files already listed |

## Integration Checklist

- ✅ Supports any URL format (videos, playlists, channels, IDs)
- ✅ Auto-detects input type
- ✅ Auto-expands playlists/channels
- ✅ Handles mixed input seamlessly
- ✅ Graceful error handling
- ✅ Progress feedback
- ✅ Multiple output formats
- ✅ Works with stdin/files
- ✅ Agent-callable via Python
- ✅ Production-ready

## Example: Complete Research Workflow

```bash
#!/bin/bash
# End-to-end: URLs → Transcripts → Analysis → Report

SOURCES="research_sources.txt"
TRANSCRIPTS="transcripts"
OUTPUT="research_report.md"

echo "Step 1: Assess sources..."
/transcribe $SOURCES --inspect

echo "Step 2: Download transcripts..."
/transcribe $SOURCES --output-dir $TRANSCRIPTS --format md

echo "Step 3: Count results..."
COUNT=$(ls $TRANSCRIPTS/*.md 2>/dev/null | wc -l)
echo "Downloaded $COUNT transcripts"

echo "Step 4: Analyze with agent..."
# Agent processes $TRANSCRIPTS directory

echo "Step 5: Generate report..."
# Report generation script

echo "Complete! Check $OUTPUT"
```

## Bottom Line

**One command**. Input anything. It figures out what to do.

```bash
/transcribe INPUT [OPTIONS]
```

- Single URL? → Downloads immediately
- Playlist URL? → Expands and downloads all
- Channel URL? → Expands and downloads all uploads
- File with mixed? → Detects each, expands as needed, downloads all

Perfect for workflows that need YouTube transcripts at any scale.
