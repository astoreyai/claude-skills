# Claude Code Commands - YouTube Transcriber

These commands would be added to Claude Code CLI to make the pipeline easily accessible.

## Installation

Add these command files to your Claude Code configuration:

```bash
mkdir -p ~/.claude/commands/youtube-transcriber
```

## Command Files

### 1. `/run-youtube-transcriber` - Complete Pipeline

**File**: `~/.claude/commands/youtube-transcriber/run.md`

```bash
#!/usr/bin/env python3
# Complete YouTube Transcriber workflow

import subprocess
import sys
from pathlib import Path

# Get transcript path from argument
transcript_path = sys.argv[1] if len(sys.argv) > 1 else None
if not transcript_path:
    print("Usage: /run-youtube-transcriber <transcript_path>")
    sys.exit(1)

# Run workflow
result = subprocess.run([
    sys.executable,
    "~/github/astoreyai/claude-skills/workflow_runner.py",
    "--transcript", transcript_path
])

sys.exit(result.returncode)
```

**Usage**:
```bash
/run-youtube-transcriber ~/Downloads/ml-lecture.txt
```

---

### 2. `/extract-transcript-facts` - Phase 1 Only

**File**: `~/.claude/commands/youtube-transcriber/extract.md`

Extracts facts from a transcript using Claude API (via Claude Code).

**Usage**:
```bash
/extract-transcript-facts ~/Downloads/transcript.txt
```

**What it does**:
- Loads transcript file
- Calls Claude 3.5 Sonnet API (uses Claude Code's configured key)
- Extracts facts with categories
- Outputs JSON with fact metadata

**Output**:
```json
{
  "facts": [
    {
      "id": "fact_001",
      "text": "Machine learning is a subset of AI",
      "category": "scientific_fact",
      "confidence": 0.95,
      "tags": ["ML", "AI"]
    }
  ],
  "topics": ["Machine Learning", "AI Fundamentals"],
  "accuracy": 0.92
}
```

---

### 3. `/format-transcript-notes` - Phase 2 Only

**File**: `~/.claude/commands/youtube-transcriber/format.md`

Formats extracted facts as atomic notes.

**Usage**:
```bash
/format-transcript-notes ~/Downloads/facts.json --output ./notes
```

**What it does**:
- Reads JSON facts from Phase 1
- Creates one markdown file per fact
- Adds wiki-links [[Topic]]
- Builds hierarchical directory structure
- Creates topic indices

**Output Structure**:
```
./notes/
├── Machine-Learning/
│   ├── Fundamentals/
│   │   ├── fact_001_ml_subset_ai.md
│   │   ├── fact_002_three_types_ml.md
│   │   └── index.md
│   └── Applications/
│       ├── fact_003_computer_vision.md
│       └── index.md
└── index.md
```

---

### 4. `/integrate-obsidian-vault` - Phase 3 Only

**File**: `~/.claude/commands/youtube-transcriber/integrate.md`

Integrates formatted notes into Obsidian vault.

**Usage**:
```bash
# Default vault path
/integrate-obsidian-vault ./notes/

# Custom vault path
/integrate-obsidian-vault ./notes/ --vault-path ~/Documents/Obsidian/Aaron
```

**Options**:
- `--vault-path` - Path to Obsidian vault (default: ~/Documents/Obsidian/Aaron)
- `--dry-run` - Test without making changes
- `--backup-first` - Create backup before integrating (default: true)

**What it does**:
- Creates backup of vault
- Copies notes preserving structure
- Generates backlinks between notes
- Creates master index
- Verifies all links

**Output**:
```
✓ Vault path: ~/Documents/Obsidian/Aaron
✓ Notes integrated: 12
✓ Backlinks created: 8
✓ Index created: Knowledge/Video-Transcripts/index.md
```

---

### 5. `/archive-transcripts` - Phase 4 Only

**File**: `~/.claude/commands/youtube-transcriber/archive.md`

Archives original transcripts safely.

**Usage**:
```bash
# Verify without archiving
/archive-transcripts ~/Downloads/transcript.txt --verify-only

# Create archive without cleanup
/archive-transcripts ~/Downloads/transcript.txt

# Create archive and cleanup originals
/archive-transcripts ~/Downloads/transcript.txt --cleanup
```

**Options**:
- `--verify-only` - Check integrity without archiving
- `--cleanup` - Delete originals after successful archive
- `--archive-dir` - Custom archive directory

**What it does**:
- Verifies files with MD5 checksums
- Compresses to tar.gz
- Creates metadata.json
- Optional cleanup
- Safe, non-destructive verification

**Output**:
```
✓ Files archived: 1
✓ Archive: ~/youtube-transcriber/transcripts-archive/transcripts_20251122_143200.tar.gz
✓ Size: 45.2 KB
✓ Checksums verified
```

---

## Usage Examples

### Example 1: Complete Workflow

```bash
# Step 1: Extract facts (Phase 1)
/extract-transcript-facts ~/Downloads/ml-lecture.txt > facts.json

# Step 2: Format as notes (Phase 2)
/format-transcript-notes facts.json --output ./notes

# Step 3: Integrate to Obsidian (Phase 3)
/integrate-obsidian-vault ./notes/

# Step 4: Archive transcript (Phase 4)
/archive-transcripts ~/Downloads/ml-lecture.txt
```

### Example 2: One-Command Pipeline

```bash
# Everything in one go
/run-youtube-transcriber ~/Downloads/ml-lecture.txt
```

### Example 3: Safe Testing

```bash
# Test extraction without archiving
/extract-transcript-facts ~/Downloads/transcript.txt

# Format and test with dry-run
/integrate-obsidian-vault ./notes/ --dry-run

# Verify without archiving
/archive-transcripts ~/Downloads/transcript.txt --verify-only
```

---

## How It Works with Claude Code

### No Manual API Key Setup Needed

When you use `/extract-transcript-facts` in Claude Code:

```
Claude Code CLI
    ↓
Reads your configured ANTHROPIC_API_KEY
    ↓
Passes to Phase 1 (Transcript Extractor)
    ↓
Claude 3.5 Sonnet API extracts facts
    ↓
Returns structured data
```

**No environment variables needed!** Claude Code handles authentication automatically.

---

## Future: Ollama Integration

```bash
# Future version with Ollama (local models, no API key needed)
/extract-transcript-facts ~/Downloads/ml-lecture.txt \
  --llm-backend ollama \
  --model mistral-7b
```

Benefits when Ollama integration is added:
- ✅ Zero API costs
- ✅ Completely offline
- ✅ Full data privacy
- ✅ Instant local processing

---

## Combining with Claude Code Features

### Use in scripts
```bash
# Extract facts from multiple transcripts
for file in ~/Downloads/*.txt; do
  /extract-transcript-facts "$file" >> all_facts.json
done

# Integrate all at once
/integrate-obsidian-vault ./notes/
```

### Use with other skills
```bash
# Extract, format, and integrate
/extract-transcript-facts ~/Downloads/lecture.txt | \
  /format-transcript-notes | \
  /integrate-obsidian-vault
```

### Use in workflows
```bash
# Create a complete knowledge base workflow
/extract-transcript-facts ~/Downloads/*.txt
/format-transcript-notes ./facts/ --output ./notes
/integrate-obsidian-vault ./notes/ --vault-path ~/Obsidian
/archive-transcripts ~/Downloads/*.txt
```

---

## Status: Ready for Claude Code Integration

- ✅ All 4 phases fully tested
- ✅ Integration tests passing
- ✅ Works with Claude Code API key management
- ✅ No manual setup needed
- ✅ Ready for Ollama swap (future)

**Next step**: Add these commands to your Claude Code configuration and start using!

```bash
# Copy to Claude Code
cp -r ~/github/astoreyai/claude-skills/ ~/.claude/skills/youtube-transcriber
```
