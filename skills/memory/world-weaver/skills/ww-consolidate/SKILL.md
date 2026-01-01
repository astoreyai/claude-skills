---
name: ww-consolidate
description: Trigger and manage World Weaver memory consolidation
version: 1.0.0
allowed-tools: ['Bash', 'Read']
---

# WW Consolidate Skill

Manage memory consolidation in World Weaver - the process of organizing, clustering, and optimizing stored memories.

## Purpose

Memory consolidation mirrors biological memory processes:
- **Clustering**: Group similar episodes into themes
- **Strengthening**: Reinforce frequently co-accessed memories
- **Decay**: Apply FSRS stability decay
- **Extraction**: Identify new entities and skills from episodes
- **Pruning**: Remove orphaned or stale memories

## When to Use

Invoke this skill when:
- Many new episodes accumulated (>50)
- Memory search feels slow or noisy
- User requests consolidation
- Before archiving old memories
- After major project milestone

## MCP Tools Used

```
mcp__ww-memory__consolidate_now    - Run consolidation
mcp__ww-memory__memory_stats       - Get system metrics
mcp__ww-memory__get_provenance     - Check memory lineage
```

## Consolidation Types

### Light Consolidation
Fast, safe, run frequently.

**Operations**:
1. Update FSRS stability scores
2. Apply Hebbian strengthening to co-accessed pairs
3. Normalize relationship weights (fan-out correction)
4. Prune orphaned relationships

**Duration**: 2-10 seconds
**Frequency**: Daily or after 20+ new episodes

### Full Consolidation
Thorough, compute-intensive, run weekly.

**Operations**:
All of light consolidation, plus:
1. HDBSCAN clustering of episode embeddings
2. Entity extraction from episode content
3. Skill inference from successful patterns
4. Duplicate entity merging
5. Knowledge graph reindexing

**Duration**: 30-120 seconds
**Frequency**: Weekly or after 100+ new episodes
**Requirement**: HDBSCAN library installed

## Consolidation Workflow

### Pre-Consolidation Checks
```
1. Get current stats: mcp__ww-memory__memory_stats()
2. Check episode count since last consolidation
3. Verify HDBSCAN available (for full consolidation)
4. Estimate consolidation duration
```

### Light Consolidation Process
```
1. Load all episodes from Qdrant
2. For each episode pair accessed together:
   - Calculate co-access score
   - Update relationship weight in Neo4j
3. Apply FSRS decay to all episodes:
   - R(t, S) = (1 + 0.9 * t/S)^(-0.5)
4. Normalize fan-out weights:
   - Prevent hub nodes from dominating
5. Prune relationships with weight < 0.1
```

### Full Consolidation Process
```
1. Run light consolidation first
2. Extract episode embeddings
3. Apply stratified sampling if >5000 episodes
4. Run HDBSCAN clustering:
   - min_cluster_size=3
   - metric="cosine"
5. Assign non-sampled episodes to nearest cluster
6. For each cluster:
   - Extract common entities (rule-based or LLM)
   - Identify successful patterns
   - Generate candidate skills
7. Merge duplicate entities:
   - Same name, similar embedding
8. Rebuild Neo4j indexes
```

## Running Consolidation

### Via MCP Tool
```
mcp__ww-memory__consolidate_now(
  consolidation_type="light",  # or "full"
  dry_run=false,               # true to preview only
  session_filter=null          # null for all, or specific session_id
)
```

### Response Format
```json
{
  "status": "completed",
  "type": "light",
  "duration_seconds": 4.2,
  "stats": {
    "episodes_processed": 47,
    "relationships_strengthened": 23,
    "relationships_pruned": 5,
    "stability_updates": 35
  },
  "errors": []
}
```

## Monitoring Consolidation Health

### Check Stats Before
```
mcp__ww-memory__memory_stats()

Returns:
{
  "episodes": {"total": 47, "this_session": 12, "avg_stability": 0.72},
  "entities": {"total": 156, "orphaned": 3},
  "skills": {"total": 23, "active": 20},
  "relationships": {"total": 312, "avg_weight": 0.54},
  "last_consolidation": "2025-11-27T10:00:00",
  "episodes_since_consolidation": 15
}
```

### Interpret Metrics
| Metric | Healthy | Needs Attention |
|--------|---------|-----------------|
| Episodes since consolidation | < 50 | > 100 |
| Orphaned entities | < 5 | > 20 |
| Average relationship weight | 0.3-0.7 | < 0.2 or > 0.9 |
| Average stability | > 0.5 | < 0.3 |

## Error Handling

### HDBSCAN Not Available
```
If full consolidation requested but HDBSCAN not installed:
1. Log warning
2. Fall back to light consolidation
3. Report that clustering was skipped
4. Suggest: pip install hdbscan
```

### Memory Error
```
If HDBSCAN runs out of memory:
1. Catch MemoryError
2. Return all episodes as single cluster
3. Log warning about dataset size
4. Suggest reducing hdbscan_max_samples
```

### Database Errors
```
If Neo4j/Qdrant operations fail:
1. Log specific error
2. Continue with remaining operations
3. Report partial completion
4. Do not lose data
```

## Output Format

### Success Report
```markdown
## Consolidation Complete

**Type**: Light
**Duration**: 4.2s

### Changes
| Metric | Before | After | Delta |
|--------|--------|-------|-------|
| Episodes | 47 | 47 | 0 |
| Relationships | 312 | 307 | -5 (pruned) |
| Avg Weight | 0.48 | 0.54 | +0.06 |
| Avg Stability | 0.68 | 0.65 | -0.03 (decay) |

### Actions Taken
- Strengthened 23 relationship pairs
- Pruned 5 weak relationships
- Updated 47 stability scores

### Recommendations
- Consider full consolidation (15 new entities detected)
```

### Dry Run Report
```markdown
## Consolidation Preview (Dry Run)

### Would Process
- 47 episodes
- 312 relationships
- 156 entities

### Would Strengthen
- Neo4j ↔ Cypher: 0.7 → 0.82
- Testing ↔ pytest: 0.5 → 0.65

### Would Prune
- 5 relationships with weight < 0.1

### Would Extract (Full Only)
- 3 potential new entities
- 1 potential new skill

*No changes made*
```

## Integration

This skill is called by:
- `/consolidate` command
- Scheduled maintenance (cron)
- SessionEnd hook (optionally)
- `ww-memory` agent for maintenance tasks

## Best Practices

1. **Run light consolidation frequently** - Low cost, keeps memory healthy
2. **Run full consolidation weekly** - More thorough but slower
3. **Monitor orphaned entities** - Sign of extraction issues
4. **Watch stability decay** - If too low, episodesm are being forgotten
5. **Check after major imports** - Large data loads need consolidation
