---
name: ww-analyze
description: Deep analysis workflows for World Weaver memory systems, code, and architecture
version: 1.0.0
allowed-tools: ['Bash', 'Read', 'Write', 'Grep', 'Glob']
---

# WW Analyze Skill

Deep analysis workflows for World Weaver memory systems, code quality, and architecture.

## Purpose

This skill provides comprehensive analysis capabilities:
1. **Code Analysis**: Audit WW codebase for bugs, patterns, and improvements
2. **Memory Analysis**: Analyze memory contents, patterns, and health
3. **Architecture Analysis**: Evaluate system design and propose improvements
4. **Performance Analysis**: Profile and identify bottlenecks

## When to Use

Invoke this skill when:
- User asks "analyze the memory system"
- User wants to understand memory patterns
- Code quality audit is needed
- Performance issues are suspected
- Architecture review is requested

## Analysis Workflows

### 1. Bug Hunting Workflow

Orchestrate specialized bug-hunting agents:

```bash
# Run all bug hunters in sequence
paths=(
  "src/ww/learning/"
  "src/ww/memory/"
  "src/ww/storage/"
  "src/ww/mcp/"
  "src/ww/core/"
)

for path in "${paths[@]}"; do
  echo "Analyzing: $path"
done
```

Agent orchestration:
1. **ww-bio-auditor** - Check biological plausibility
2. **ww-race-hunter** - Find concurrency bugs
3. **ww-leak-hunter** - Detect memory leaks
4. **ww-hinton-validator** - Validate learning theory
5. **ww-cache-analyzer** - Check cache coherence
6. **ww-trace-debugger** - Debug eligibility traces

### 2. Memory Pattern Analysis

Analyze stored memories for patterns:

```python
# Query memory statistics
mcp__ww-memory__memory_stats()

# Analyze episode distribution
mcp__ww-memory__recall_episodes(
  query="*",
  limit=1000,
  include_metadata=True
)

# Analyze entity graph
mcp__ww-memory__semantic_recall(
  query="*",
  include_connections=True
)
```

Output analysis:
- Episode count by outcome (success/failure/partial)
- Entity type distribution
- Relationship density
- Temporal patterns
- Importance distribution

### 3. Architecture Analysis

Evaluate system architecture:

```bash
# File structure analysis
find /home/aaron/ww/src -name "*.py" | wc -l

# Dependency analysis
grep -r "^from ww" /home/aaron/ww/src --include="*.py" | cut -d: -f2 | sort | uniq -c | sort -rn

# Test coverage check
cd /home/aaron/ww && pytest --cov=src/ww --cov-report=term-missing
```

Architecture metrics:
- Module coupling (import analysis)
- Test coverage by module
- Cyclomatic complexity
- Code duplication

### 4. Performance Analysis

Profile system performance:

```python
import cProfile
import pstats

# Profile memory operations
profiler = cProfile.Profile()
profiler.enable()
# ... memory operations ...
profiler.disable()

stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(20)
```

Performance metrics:
- Query latency (p50, p95, p99)
- Memory usage over time
- CPU utilization
- I/O operations

## Analysis Report Format

```markdown
## WW Analysis Report

**Type**: {Bug Hunt | Memory Pattern | Architecture | Performance}
**Date**: {timestamp}
**Scope**: {paths analyzed}

### Summary
{High-level findings}

### Metrics
| Metric | Value | Status |
|--------|-------|--------|
| Files analyzed | N | - |
| Issues found | N | {OK/WARNING/CRITICAL} |
| Test coverage | N% | {OK if >80%} |

### Findings

#### Critical (P0)
{List of critical issues}

#### High (P1)
{List of high priority issues}

#### Medium (P2)
{List of medium priority issues}

### Recommendations
1. {Priority action items}

### Visualizations
{Embedded diagrams or links to generated visualizations}
```

## Integration with Agents

This skill orchestrates bug-hunting agents:

```
/ww-analyze bugs src/ww/learning/
  → Spawns: ww-bio-auditor, ww-hinton-validator, ww-trace-debugger

/ww-analyze concurrency src/ww/mcp/
  → Spawns: ww-race-hunter, ww-leak-hunter, ww-cache-analyzer

/ww-analyze full src/ww/
  → Spawns: All 6 agents in parallel
```

## MCP Extensions

Proposed MCP endpoints for analysis:

```
mcp__ww-memory__analyze_patterns    - Analyze memory patterns
mcp__ww-memory__analyze_health      - Check system health
mcp__ww-memory__analyze_performance - Profile operations
mcp__ww-memory__generate_report     - Create analysis report
```

## Quality Checklist

Before completing analysis:
- [ ] All target paths scanned
- [ ] All agents completed successfully
- [ ] Findings categorized by severity
- [ ] Recommendations are actionable
- [ ] Report saved to /home/aaron/mem/

## Error Handling

If analysis fails:
1. Log partial results
2. Identify failing component
3. Continue with remaining analyses
4. Report incomplete status
