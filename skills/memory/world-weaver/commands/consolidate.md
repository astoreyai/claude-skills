# /consolidate Command

Trigger World Weaver memory consolidation.

## Usage

```
/consolidate              # Light consolidation
/consolidate --full       # Full consolidation (slower)
/consolidate --stats      # Show consolidation stats only
```

## Arguments

- `--full`: Run full consolidation including entity extraction and skill inference
- `--light`: Run light consolidation only (default)
- `--stats`: Show memory statistics without running consolidation
- `--dry-run`: Show what would be consolidated without executing

## What Consolidation Does

### Light Consolidation
- Cluster similar episodes
- Strengthen co-accessed entity relationships
- Update memory stability scores (FSRS decay)
- Prune orphaned relationships

### Full Consolidation
All of light consolidation, plus:
- Extract new entities from episode content
- Infer procedural skills from successful patterns
- Merge duplicate entities
- Build knowledge graph indices

## Workflow

When `/consolidate` is invoked:

1. **Check Memory Stats**
   - Count episodes, entities, skills
   - Identify consolidation candidates

2. **Run Clustering** (if HDBSCAN available)
   - Cluster similar episodes
   - Identify recurring themes

3. **Strengthen Relationships**
   - Apply Hebbian learning to co-accessed memories
   - Normalize fan-out weights

4. **Update Stability**
   - Apply FSRS decay to episode stability
   - Update retrievability scores

5. **Report Results**
   - Show what was consolidated
   - Report any issues

## Examples

### Light Consolidation
```
User: /consolidate

Claude: Running light consolidation...

## Consolidation Report

### Episodes
- Total: 47
- Clustered: 12 into 3 groups
- Updated stability: 35

### Relationships
- Strengthened: 23 pairs
- Normalized: 156 weights

### Health
- Orphaned entities removed: 2
- Stale relationships pruned: 5

Duration: 2.3s
```

### Full Consolidation
```
User: /consolidate --full

Claude: Running full consolidation (this may take a minute)...

## Full Consolidation Report

### Episodes
- Total: 47
- Clustered: 12 into 3 groups
- New themes identified: 2

### Entity Extraction
- Scanned: 47 episodes
- New entities created: 8
- Duplicates merged: 3

### Skill Inference
- Patterns analyzed: 15
- New skills inferred: 2
  - "debug-neo4j-queries" (from 4 similar episodes)
  - "run-integration-tests" (from 6 similar episodes)

### Relationships
- Strengthened: 45 pairs
- New relations: 12
- Graph density: 0.34 → 0.38

### Health
- Memory footprint: 12.4MB
- Index rebuilt: Yes

Duration: 34.2s
```

### Stats Only
```
User: /consolidate --stats

Claude:
## Memory Statistics

### Counts
| Type | Count | Avg Age | Avg Stability |
|------|-------|---------|---------------|
| Episodes | 47 | 4.2 days | 0.72 |
| Entities | 156 | 12.3 days | 0.85 |
| Skills | 23 | 8.1 days | 0.91 |
| Relations | 312 | - | 0.54 |

### Consolidation Status
- Last run: 2 hours ago
- Episodes since: 5
- Recommended: Light (12 new episodes)

### Storage
- Neo4j nodes: 226
- Qdrant vectors: 226
- Total size: ~15MB
```

### Dry Run
```
User: /consolidate --dry-run

Claude:
## Consolidation Preview (Dry Run)

### Would Cluster
- 8 episodes about "testing" → 1 cluster
- 4 episodes about "Neo4j debugging" → 1 cluster

### Would Strengthen
- "Neo4j" ↔ "Cypher": 0.7 → 0.82
- "Testing" ↔ "pytest": 0.5 → 0.65

### Would Extract
- Potential entity: "HDBSCAN" (mentioned 3x)
- Potential entity: "Session Isolation" (mentioned 4x)

### Would Infer
- Potential skill: "run-ww-tests" (pattern seen 6x)

No changes made (dry run).
```

## When to Consolidate

- After many episodes accumulated (>50)
- Before starting new major task
- Weekly maintenance
- When memory search feels slow

## Implementation Notes

Consolidation uses the MCP tool:
```
mcp__ww-memory__consolidate_now(
  consolidation_type="light|full",
  dry_run=false
)
```

Full consolidation requires HDBSCAN. If not available, falls back to
simple clustering algorithms.
