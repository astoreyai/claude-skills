# /remember Command

Store a memory in World Weaver.

## Usage

```
/remember                     # Store summary of recent conversation
/remember Fixed the bug       # Store specific content
/remember --important         # Mark as high importance
/remember --skill            # Store as procedural skill
```

## Arguments

- `content` (optional): What to remember. If omitted, summarizes recent conversation.
- `--important`: Set high emotional valence (0.9)
- `--skill`: Store as procedural skill instead of episode
- `--entity`: Store as knowledge graph entity

## Workflow

When `/remember` is invoked:

1. **Parse Arguments**
   - If content provided, use it directly
   - If `--important` flag, set valence=0.9
   - If `--skill` flag, invoke ww-store skill in skill mode
   - If `--entity` flag, invoke ww-store skill in entity mode

2. **Gather Context**
   - Current working directory
   - Project name (from git or directory)
   - Recent conversation summary if no content

3. **Determine Outcome**
   - Look for success/failure indicators in content
   - Default to "neutral" if unclear

4. **Store Memory**
   - Call `mcp__ww-memory__create_episode` (or create_skill/create_entity)
   - Include full context

5. **Confirm Storage**
   - Report what was stored
   - Show memory ID for reference

## Examples

### Quick Store (Summarize Recent)
```
User: /remember

Claude: Summarizing recent conversation...
Stored episode: "Discussed World Weaver plugin architecture, designed
skills and hooks structure, created implementation plan."
- ID: ep-abc123
- Outcome: success
- Valence: 0.7
```

### Store Specific Content
```
User: /remember Fixed the batch query parameter bug in Neo4j store

Claude: Stored episode: "Fixed the batch query parameter bug in Neo4j store"
- ID: ep-def456
- Outcome: success (detected from "Fixed")
- Valence: 0.5
- Context: project=ww, cwd=/home/aaron/ww
```

### Store Important Milestone
```
User: /remember --important Completed Phase 1 of plugin implementation

Claude: Stored high-importance episode: "Completed Phase 1 of plugin implementation"
- ID: ep-ghi789
- Outcome: success
- Valence: 0.9 (marked important)
```

### Store as Skill
```
User: /remember --skill To run WW tests, activate venv and run pytest

Claude: Stored procedural skill: "run-ww-tests"
- ID: sk-jkl012
- Steps: 1. Activate venv 2. Run pytest tests/ -v
- Tags: testing, ww
```

### Store as Entity
```
User: /remember --entity HDBSCAN is a clustering algorithm used for memory consolidation

Claude: Stored entity: "HDBSCAN" (CONCEPT)
- ID: en-mno345
- Summary: Clustering algorithm used for memory consolidation
- Type: CONCEPT
```

## Implementation Notes

This command uses the `ww-store` skill internally. The command is a convenience
wrapper that:
1. Parses simple flags
2. Infers context automatically
3. Provides user-friendly confirmation

For complex memory storage with full control over parameters, use the
`ww-store` skill directly.