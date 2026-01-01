---
name: ww-diagnose
description: Problem diagnosis for World Weaver memory systems - identify root causes and suggest fixes
version: 1.0.0
allowed-tools: ['Bash', 'Read', 'Write', 'Grep', 'Glob']
---

# WW Diagnose Skill

Problem diagnosis for World Weaver memory systems - identify root causes and suggest fixes.

## Purpose

This skill provides diagnostic capabilities for:
1. **Learning Issues**: Why isn't learning improving?
2. **Memory Issues**: Why can't I find memories?
3. **Performance Issues**: Why is it slow?
4. **Integration Issues**: Why isn't MCP working?
5. **Consistency Issues**: Why is data corrupted?

## When to Use

Invoke this skill when:
- User reports "learning isn't working"
- User reports "can't find my memories"
- User reports "it's very slow"
- User reports "getting errors"
- User reports "data seems wrong"

## Diagnostic Decision Tree

### Symptom: Learning Not Improving

```
1. Check neuromodulators
   → Are DA/NE/ACh returning non-zero values?
   → Run: ww-bio-auditor

2. Check eligibility traces
   → Is decay happening correctly?
   → Run: ww-trace-debugger

3. Check weight updates
   → Is strengthen_relationship() implemented?
   → Is three-factor learning complete?

4. Check learning rates
   → Episodic LR >> Semantic LR?
   → CLS ratio correct?
```

### Symptom: Memory Not Found

```
1. Check storage
   → Was memory actually stored?
   → Query: mcp__ww-memory__recall_episodes(query="*", limit=5)

2. Check embeddings
   → Is vector index populated?
   → Query: Check Qdrant collection

3. Check retrieval
   → Is query embedding computed?
   → Is similarity threshold too high?

4. Check session
   → Is session ID correct?
   → Is there a session mismatch?
```

### Symptom: Slow Performance

```
1. Check database connections
   → Is Neo4j responding?
   → Is Qdrant responding?

2. Check query patterns
   → Are there N+1 queries?
   → Is there missing indexing?

3. Check memory usage
   → Is there unbounded growth?
   → Run: ww-leak-hunter

4. Check caching
   → Is cache being used?
   → Is cache invalidation correct?
   → Run: ww-cache-analyzer
```

### Symptom: Data Corruption

```
1. Check race conditions
   → Is there concurrent access?
   → Run: ww-race-hunter

2. Check cache coherence
   → Is stale data being served?
   → Run: ww-cache-analyzer

3. Check transaction integrity
   → Are writes atomic?
   → Is there rollback on failure?

4. Check type consistency
   → Are IDs consistent (str vs int)?
   → Are timestamps consistent?
```

## Diagnostic Commands

### Quick Health Check

```bash
# Check service health
curl http://localhost:7474  # Neo4j
curl http://localhost:6333/collections  # Qdrant

# Check MCP server
ps aux | grep ww.mcp

# Check logs
tail -50 /tmp/ww-*.log
```

### Database Diagnostics

```python
# Neo4j query analysis
PROFILE MATCH (e:Episode) RETURN count(e)

# Check indexes
SHOW INDEXES

# Check constraints
SHOW CONSTRAINTS
```

### Memory System Diagnostics

```python
# Check memory stats
mcp__ww-memory__memory_stats()

# Check recent episodes
mcp__ww-memory__recall_episodes(
  query="*",
  limit=10,
  time_filter={"after": "2024-01-01"}
)

# Check entity graph
mcp__ww-memory__semantic_recall(
  query="*",
  limit=10
)
```

## Diagnostic Report Format

```markdown
## WW Diagnostic Report

**Symptom**: {User-reported problem}
**Date**: {timestamp}
**Session**: {session_id}

### Quick Checks
| Check | Status | Notes |
|-------|--------|-------|
| Neo4j | {UP/DOWN} | {latency} |
| Qdrant | {UP/DOWN} | {latency} |
| MCP Server | {UP/DOWN} | {pid} |

### Root Cause Analysis

**Primary Cause**: {Identified root cause}

**Evidence**:
\`\`\`
{Diagnostic output showing the issue}
\`\`\`

**Contributing Factors**:
1. {Factor 1}
2. {Factor 2}

### Recommended Fix

**Immediate Action**:
\`\`\`bash
{Command to fix immediately}
\`\`\`

**Code Fix** (if needed):
\`\`\`python
# File: {path}
# Line: {number}
{code change}
\`\`\`

**Prevention**:
{How to prevent this in future}

### Verification

After fix, verify with:
\`\`\`bash
{verification command}
\`\`\`
```

## Agent Integration

Diagnosis may spawn specialized agents:

| Symptom | Agents |
|---------|--------|
| Learning issues | ww-bio-auditor, ww-trace-debugger, ww-hinton-validator |
| Memory issues | ww-memory (direct query) |
| Performance | ww-leak-hunter, ww-cache-analyzer |
| Corruption | ww-race-hunter, ww-cache-analyzer |

## Common Issues Quick Reference

### Issue: "strengthen_relationship not found"
```
Root cause: Method missing in neo4j_store.py
Fix: Implement the method (see bio-memory audit)
```

### Issue: "Neuromodulators always return 0"
```
Root cause: Hardcoded return values
Fix: Implement actual computation (see bio-memory audit)
```

### Issue: "Eligibility traces exploding"
```
Root cause: Missing decay or wrong decay order
Fix: Apply decay before accumulation
```

### Issue: "Cache returning stale data"
```
Root cause: Missing invalidation on write
Fix: Add cache.pop() after database write
```

### Issue: "KeyError on dict access"
```
Root cause: TOCTOU race condition
Fix: Use dict.get() instead of key check + access
```

## Error Handling

If diagnosis cannot identify root cause:
1. Collect all diagnostic data
2. Note what was ruled out
3. Suggest further investigation steps
4. Recommend manual debugging approach
