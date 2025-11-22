# YouTube Transcriber Skill - Workflow Integration Guide

Complete guide for using the YouTube Transcriber skill in Claude Code workflows and with autonomous agents.

## Quick Start

### For Users (Claude Code)

**One-line transcription:**
```bash
youtube-transcriber.sh urls.txt
```

**With options:**
```bash
youtube-transcriber.sh urls.txt --output-dir research --format both --expand
```

**From stdin:**
```bash
cat playlist_urls.txt | youtube-transcriber.sh -
```

### For Agents (Workflow Context)

```
Agent receives: ["https://youtube.com/watch?v=...", "https://youtube.com/playlist?list=..."]
  ↓
Call: transcribe_batch(urls_file, output_dir="transcripts", expand=True)
  ↓
Returns: {success_count: 15, error_count: 0, files: [...]}
  ↓
Agent processes: transcripts for analysis/summarization
```

## Real-World Workflow Examples

### Example 1: Research Literature Review + YouTube Content

**Scenario:** Combine academic papers with educational video transcripts

```
Workflow:
1. User provides: Mix of paper PDFs and YouTube playlist URLs
2. Research Assistant extracts: Paper summaries
3. YouTube Transcriber expands: Playlist → 50 video URLs
4. YouTube Transcriber downloads: 50 transcripts
5. Research Assistant analyzes: All content together
6. Output: Comprehensive research document with citations
```

**Implementation:**
```python
# In agent workflow
urls_file = create_temp_file(mixed_urls)
result = transcribe_batch(urls_file, format="md", expand=True)

transcripts = load_from_dir(result["output_dir"])
summaries = analyze_transcripts(transcripts)  # Next agent

report = compile_research_report(papers + transcripts + summaries)
```

### Example 2: Educational Content Curation

**Scenario:** Build comprehensive learning resource from educational channels/playlists

```
Workflow:
1. User provides: List of educational channels and playlists
2. YouTube Transcriber expands: Channels/playlists → 200+ videos
3. YouTube Transcriber downloads: All transcripts
4. Summarizer agent: Creates summaries for each topic
5. Organizer agent: Groups by topic/difficulty level
6. Output: Structured learning guide with transcripts
```

**Pseudo-code:**
```
urls = [
    "https://youtube.com/@edchannel1",
    "https://youtube.com/playlist?list=...",
    "https://youtube.com/@edchannel2"
]

expanded = expand_urls(urls)  # 200+ videos
transcripts = batch_download(expanded)

by_topic = organize_by_metadata(transcripts)
summaries = summarize_each(transcripts)

course = create_learning_path(summaries, by_topic)
```

### Example 3: Market Research from Video Content

**Scenario:** Extract insights from interview/analysis videos

```
Workflow:
1. User provides: List of YouTube video URLs (interviews, analysis)
2. YouTube Transcriber downloads: All transcripts with timestamps
3. Analysis agent: Extracts key quotes and insights
4. Synthesis agent: Identifies patterns and themes
5. Output: Research report with quoted evidence
```

### Example 4: Content Review Workflow

**Scenario:** Review educational material quality and accuracy

```
Workflow:
1. Curator provides: Channel URL with 100+ videos
2. YouTube Transcriber expands: → 100 video URLs
3. YouTube Transcriber downloads: All transcripts
4. QA Agent: Checks transcript completeness
5. Content Agent: Reviews accuracy and quality
6. Report Agent: Flags issues, rates each video
7. Output: Quality assurance report for all videos
```

## Integrating with Specific Agents

### With Research Assistant

```markdown
## Workflow: Convert Educational Video Series to Research Document

Agent Chain:
1. **youtube-transcriber** skill
   - Expand playlist → 50 videos
   - Download transcripts
   - Output: 50 markdown files with timestamps

2. **literature-reviewer** agent (research assistant)
   - Read transcript directory
   - Extract key findings
   - Organize by theme

3. **manuscript-writer** agent
   - Combine transcripts + analysis
   - Format as academic document
   - Generate citations

Output: Comprehensive research paper with video sources
```

### With Kymera Integrator

```
Workflow: Content Processing Pipeline

1. User input: File with video URLs (any mix)

2. youtube-transcriber skill:
   - Expand playlists/channels
   - Download all transcripts
   - Save to directory

3. kymera-integrator agent:
   - Read transcript directory
   - Process each transcript
   - Store metadata
   - Integration with other tools

4. Downstream processing:
   - kymera-mr-optimizer: Extract strategy discussions
   - risk-monitor: Extract risk-related content
   - portfolio-checker: Extract performance analysis
```

## Command Usage in Workflows

### Single Video (Quick Lookup)

```bash
# Get transcript for one video
/transcribe-video https://www.youtube.com/watch?v=VIDEO_ID --format md

# Use in agent:
transcript = get_transcript(url)
summary = agent.summarize(transcript)
```

### Batch Processing (Main Use Case)

```bash
# Create file with mixed URLs
cat > sources.txt << EOF
https://www.youtube.com/watch?v=VIDEO_1
https://www.youtube.com/playlist?list=PLAYLIST_1
https://www.youtube.com/@channel1
EOF

# Download all transcripts (playlists auto-expanded)
/transcribe-batch sources.txt --output-dir transcripts --format both

# Agent processes all transcripts from directory
for file in transcripts/*.md:
    content = read(file)
    process(content)
```

### Expansion Only (For Inspection)

```bash
# See how many videos you're about to process
/transcribe-expand playlists.txt --output-file all_videos.txt

# Check results before batch download
wc -l all_videos.txt           # How many videos?
head -10 all_videos.txt        # Sample URLs?

# Then batch download
/transcribe-batch all_videos.txt
```

## Data Flow Diagrams

### Simple Flow: Single Video

```
User Input (Video URL)
    ↓
youtube-transcriber.sh
    ↓
Extract Transcript
    ↓
Format (MD/TXT)
    ↓
Output File (transcript_ID.md)
    ↓
Agent Reads & Processes
```

### Complex Flow: Mixed URLs with Expansion

```
User Input (Mixed URLs)
    ├─ Videos (kept as-is)
    ├─ Playlists (→ expand to videos)
    └─ Channels (→ expand to uploads)
         ↓
    Flattened Video List
         ↓
    Download All Transcripts
         ↓
    Output Directory
    ├─ transcript_ID1.md
    ├─ transcript_ID2.md
    ├─ transcript_ID3.md
    └─ ...
         ↓
    Agent Processes Directory
    ├─ Read all files
    ├─ Extract metadata
    ├─ Analyze content
    └─ Generate report
```

### Agent Workflow: Research Pipeline

```
User provides URLs
    ↓
youtube-transcriber (expand & download)
    ↓
Transcripts Directory
    ↓
research-assistant:literature-reviewer (analyze)
    ↓
research-assistant:manuscript-writer (compose)
    ↓
Output Document
```

## Error Handling & Recovery

### Common Issues in Workflows

**Issue: Playlist Not Expanding**
```python
# Check if URL is valid
result = expand_urls(["https://www.youtube.com/playlist?list=..."])
if result["expanded_count"] == 0:
    # Handle: URL may be private or deleted
    log_error("Playlist expansion failed")
    notify_user("Check playlist is public")
```

**Issue: Some Videos Missing Transcripts**
```python
# Tool handles gracefully - continues on errors
result = batch_transcripts(urls)

success = result["success_count"]
failed = result["error_count"]

if failed > 0:
    log_warning(f"Failed to transcribe {failed} videos")
    # Continue with successful transcripts
```

**Issue: Large Playlist (1000+ videos)**
```python
# Expansion takes time for very large playlists
# Solution: Use --no-expand, manually expand first
# Then batch in smaller chunks

result = expand_urls(huge_playlist)
# Returns: 500 video URLs

# Process in batches
for batch in chunk(result["output_file"], size=100):
    transcribe_batch(batch, output_dir=f"batch_{i}")
```

## Performance Considerations

### Expansion Times
- Small playlist (10-50 videos): 2-5 seconds
- Medium playlist (50-200 videos): 5-15 seconds
- Large playlist (200-500 videos): 15-60 seconds
- Channel (300+ videos): 30-120 seconds

### Download Times
- Single video: 1-3 seconds
- 10 videos: 10-30 seconds
- 100 videos: 2-5 minutes
- 1000 videos: 20-50 minutes

### Optimization Tips
1. **Expand separately** if you need to inspect URLs before downloading
2. **Batch small** for long playlists (chunk into 100-200 videos)
3. **Use `--format md`** instead of `both` for faster processing
4. **Skip timestamps** with `--no-timestamps` for text format if not needed

## Integration Points

### With Other Skills

**research-assistant skills:**
- Provide transcripts for literature review
- Feed into manuscript writing
- Supply source material for analysis

**kymera skills:**
- Content processing
- Data extraction
- Integration workflows

**custom agents:**
- Any agent that needs text content
- Agents processing educational material
- Analysis and summarization agents

### File System Integration

```
Input: ~/sources.txt (URLs)
       ~/playlists.txt (playlists)

Process: youtube-transcriber.sh

Output: ~/transcripts/ (default directory)
        ├─ transcript_ID1.md
        ├─ transcript_ID1.txt
        ├─ transcript_ID2.md
        ├─ transcript_ID2.txt
        └─ ...
```

## Best Practices

### For Agents

1. **Always expand first** if using playlists/channels
2. **Check output directory** before feeding to next agent
3. **Handle errors gracefully** (some videos may fail)
4. **Log file count** before/after for verification
5. **Set reasonable timeouts** for large expansions

### For Users

1. **Test with small file first** (5-10 URLs)
2. **Use expansion separately** to verify URL count
3. **Choose format wisely** (MD for humans, TXT for processing)
4. **Check output directory** to verify success
5. **Archive results** if needed for later reference

### For Workflows

1. **Always validate input** before batch processing
2. **Use proper error handling** for failed transcripts
3. **Monitor file counts** through pipeline
4. **Consider chunking** for very large playlists (1000+)
5. **Plan storage** for large transcript directories

## Example: Complete Research Workflow

```bash
#!/bin/bash
# Complete workflow: URLs → Transcripts → Analysis → Report

SOURCES="sources.txt"
EXPANDED="expanded.txt"
TRANSCRIPTS="transcripts"
REPORT="research_report.md"

# Step 1: Expand all playlists/channels
echo "Expanding playlists and channels..."
youtube-transcriber.sh $SOURCES --expand --output-file $EXPANDED

# Step 2: Count videos
TOTAL=$(wc -l < $EXPANDED)
echo "Found $TOTAL videos to transcribe"

# Step 3: Download all transcripts
echo "Downloading transcripts..."
youtube-transcriber.sh $EXPANDED --output-dir $TRANSCRIPTS --format both

# Step 4: Verify
DOWNLOADED=$(ls $TRANSCRIPTS/*.md 2>/dev/null | wc -l)
echo "Downloaded $DOWNLOADED transcripts"

# Step 5: Process with agent
echo "Analyzing content..."
# (Call agent script to process $TRANSCRIPTS)

# Step 6: Generate report
echo "Generating report..."
# (Call report generation script)

echo "Complete! Check $REPORT"
```

## Troubleshooting Workflows

### Debugging Failed Batches

```bash
# Create test file with single URL
echo "https://www.youtube.com/watch?v=TEST_ID" > test.txt

# Test expansion
youtube-transcriber.sh test.txt --expand --output-file test_expanded.txt

# Test download
youtube-transcriber.sh test_expanded.txt --output-dir test_output

# Check results
ls -la test_output/
```

### Verifying Large Batches

```bash
# Count original URLs
wc -l sources.txt

# Count after expansion
wc -l expanded.txt

# Monitor download progress
watch -n 1 'ls transcripts/*.md | wc -l'

# Check for errors
tail -20 transcripts/*.txt  # if --no-timestamps
```

## Conclusion

The YouTube Transcriber skill is a powerful tool for:
- ✅ Research workflows (combine video + academic content)
- ✅ Educational content curation (organize video material)
- ✅ Content analysis (extract insights from videos)
- ✅ Batch processing (handle 100s of videos)
- ✅ Agent automation (feed transcripts to analysis agents)

Perfect for any workflow that needs to extract content from YouTube at scale.
