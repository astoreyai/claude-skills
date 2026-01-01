# /ww-stats Command

Display detailed statistics about World Weaver memory systems.

## Usage

```
/ww-stats [section] [options]
```

## Arguments

- `section`: Statistics section (default: all)
  - `all` - All statistics
  - `episodes` - Episodic memory stats
  - `entities` - Semantic memory stats
  - `skills` - Procedural memory stats
  - `health` - System health metrics
  - `performance` - Performance metrics

## Options

- `--json` - Output as JSON
- `--csv` - Output as CSV
- `--days N` - Lookback period (default: 30)

## Examples

```bash
# Show all stats
/ww-stats

# Show episode stats
/ww-stats episodes

# Show health metrics
/ww-stats health

# Export as JSON
/ww-stats all --json
```

## Output Format

```
## World Weaver Statistics

### Episodic Memory
- Total episodes: N
- Success rate: N%
- Average importance: N

### Semantic Memory
- Total entities: N
- Total relationships: N
- Graph density: N

### Procedural Memory
- Total skills: N
- Active skills: N
- Average success rate: N%

### System Health
- Neo4j: UP (latency: Nms)
- Qdrant: UP (latency: Nms)
- Memory usage: N MB
- Last consolidation: {timestamp}

### Performance
- Avg query time: Nms
- Cache hit rate: N%
- Active sessions: N
```

## MCP Integration

Calls these MCP tools:
- `mcp__ww-memory__memory_stats`
- `mcp__ww-memory__recall_episodes` (with metadata)
- `mcp__ww-memory__semantic_recall` (with graph stats)
