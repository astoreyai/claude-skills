# /recall Command

Search World Weaver memories.

## Usage

```
/recall [query]              # Search all memory types
/recall Neo4j queries        # Search for specific topic
/recall --episodes [query]   # Only episodic memories
/recall --entities [query]   # Only knowledge graph
/recall --skills [query]     # Only procedural skills
/recall --recent            # Last 7 days only
/recall --limit 20          # Return more results
```

## Arguments

- `query`: Search terms (required unless using flags that imply a query)
- `--episodes`: Search only episodic memory
- `--entities`: Search only semantic memory (knowledge graph)
- `--skills`: Search only procedural memory
- `--recent`: Filter to last 7 days
- `--limit N`: Maximum results (default: 10)
- `--session [id]`: Filter to specific session

## Workflow

When `/recall` is invoked:

1. **Parse Query and Flags**
   - Extract search terms
   - Determine which memory subsystems to search
   - Apply filters (time, session, limit)

2. **Execute Searches**
   - If no subsystem specified, search all three
   - Run searches in parallel where possible

3. **Merge and Rank**
   - Combine results from all sources
   - Re-rank by relevance
   - Deduplicate

4. **Format Output**
   - Group by memory type
   - Show relevance scores
   - Include timestamps and context

## Examples

### General Search
```
User: /recall batch queries

Claude: Searching World Weaver memories...

## Memory Results for "batch queries"

### Episodes (3 found)
1. **[Nov 27, 0.94]** Fixed batch query bug in Neo4j store
   - Changed $id to id for UNWIND variable
   - Outcome: success

2. **[Nov 26, 0.82]** Implemented batch relationship queries
   - Added get_relationships_batch method
   - Outcome: success

3. **[Nov 25, 0.71]** Investigated N+1 query pattern
   - Analyzed performance bottleneck
   - Outcome: partial

### Entities (2 found)
1. **Batch Queries** (CONCEPT, 0.91)
   - Optimization pattern for N+1 elimination
   - Related: Neo4j, Cypher, UNWIND

2. **N+1 Query Pattern** (CONCEPT, 0.78)
   - Anti-pattern causing performance issues

### Skills (1 found)
1. **optimize-neo4j-queries** (0.85)
   - How to batch Neo4j queries using UNWIND
   - Success rate: 100%
```

### Episodes Only
```
User: /recall --episodes testing

Claude: Searching episodic memory...

### Episodes (5 found)
1. **[Nov 27]** All 1259 tests passing (0.95)
2. **[Nov 27]** Fixed UUID import in benchmark test (0.88)
3. **[Nov 26]** Session isolation tests implemented (0.82)
4. **[Nov 25]** Added pytest markers for HDBSCAN (0.79)
5. **[Nov 24]** Integration tests refactored (0.71)
```

### Skills Only
```
User: /recall --skills run tests

Claude: Searching procedural memory...

### Skills (2 found)
1. **run-ww-tests** (0.93)
   Steps:
   1. source .venv/bin/activate
   2. pytest tests/ -v
   3. Check for failures
   Preconditions: In WW directory, venv exists

2. **run-integration-tests** (0.81)
   Steps:
   1. Ensure Neo4j/Qdrant running
   2. pytest tests/integration/ -m integration
   Preconditions: Services running
```

### Recent Only
```
User: /recall --recent

Claude: Searching last 7 days...

### Recent Activity (8 episodes)
- [Nov 27] Plugin architecture planning
- [Nov 27] Documentation cleanup
- [Nov 27] Test fixes
- [Nov 26] HDBSCAN optional dependency
- [Nov 26] Batch query optimization
- [Nov 25] Session isolation fixes
- [Nov 24] Memory system refactoring
- [Nov 23] Initial Neo4j integration
```

### Entity Exploration
```
User: /recall --entities World Weaver

Claude: Searching knowledge graph...

### World Weaver (CONCEPT)
Tripartite neural memory system for Claude Code.

**Related Entities:**
- Neo4j (stores graphs) - strength: 0.95
- Qdrant (stores vectors) - strength: 0.95
- Episodic Memory (subsystem) - strength: 0.90
- Semantic Memory (subsystem) - strength: 0.90
- Procedural Memory (subsystem) - strength: 0.90
- MCP Gateway (interface) - strength: 0.85
- Hebbian Learning (algorithm) - strength: 0.80
```

## Output Format

Results are formatted as:
```
### [Memory Type] (N found)
1. **[Identifier]** Title/Summary (relevance_score)
   - Key detail 1
   - Key detail 2
   - Outcome/Type/Status
```

Relevance scores are 0.0-1.0, with 1.0 being perfect match.

## Implementation Notes

This command uses the `ww-recall` skill internally. For complex retrieval
strategies like spread activation or point-in-time queries, use the
`ww-recall` skill directly with full parameter control.
