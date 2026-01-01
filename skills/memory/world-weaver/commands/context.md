# /ww-context Command

Show current World Weaver memory context.

## Usage

```
/ww-context              # Show full memory context
/ww-context --brief      # Condensed summary
/ww-context --stats      # Memory statistics only
```

## Arguments

- `--brief`: Show condensed one-line summaries
- `--stats`: Show only memory system statistics
- `--session [id]`: Show context for specific session

## Workflow

When `/ww-context` is invoked:

1. **Gather Context**
   - Get current working directory
   - Identify project from git/directory

2. **Query Memories**
   - Recent episodes (last 7 days, limit 5)
   - Related entities (from current project)
   - Applicable skills (matching project context)

3. **Get Statistics**
   - Total episodes, entities, skills
   - Session-specific counts
   - Storage metrics

4. **Format Output**
   - Group by memory type
   - Show relevance to current context
   - Include quick stats

## Examples

### Full Context
```
User: /ww-context

Claude:
## World Weaver Memory Context

**Project**: ww (World Weaver)
**Session**: default
**Working Directory**: /home/aaron/ww

### Recent Episodes (5)
| Date | Summary | Outcome |
|------|---------|---------|
| Nov 27 | Plugin architecture implementation | success |
| Nov 27 | Documentation cleanup | success |
| Nov 27 | Test fixes (UUID import) | success |
| Nov 26 | HDBSCAN optional dependency | success |
| Nov 26 | Batch query optimization | success |

### Related Entities (8)
- **World Weaver** (CONCEPT) - This project
- **Neo4j** (CONCEPT) - Graph storage
- **Qdrant** (CONCEPT) - Vector storage
- **MCP Gateway** (CONCEPT) - Interface layer
- **Plugin Architecture** (CONCEPT) - Current focus
- **Session Isolation** (CONCEPT) - Recent work
- **Batch Queries** (CONCEPT) - Optimization
- **HDBSCAN** (CONCEPT) - Clustering algorithm

### Applicable Skills (3)
1. **run-ww-tests** - Run test suite
2. **start-ww-services** - Start Neo4j/Qdrant
3. **deploy-mcp-server** - Deploy MCP gateway

### Statistics
- Episodes: 47 total (12 this session)
- Entities: 156 total
- Skills: 23 total
- Last consolidation: 2 hours ago
```

### Brief Context
```
User: /ww-context --brief

Claude:
## WW Context (Brief)
Project: ww | Session: default
Recent: 5 episodes (all success)
Entities: 8 related | Skills: 3 applicable
Stats: 47 eps, 156 ents, 23 skills
```

### Statistics Only
```
User: /ww-context --stats

Claude:
## World Weaver Statistics

### Counts
| Type | Total | This Session | This Week |
|------|-------|--------------|-----------|
| Episodes | 47 | 12 | 28 |
| Entities | 156 | 8 | 34 |
| Skills | 23 | 2 | 5 |
| Relations | 312 | 15 | 67 |

### Storage
- Neo4j nodes: 226
- Neo4j relationships: 312
- Qdrant vectors: 226
- Embedding cache: 1.2MB

### Health
- MCP server: connected
- Neo4j: connected (50ms latency)
- Qdrant: connected (12ms latency)
- Last consolidation: 2h ago
```

## Implementation Notes

This command provides a quick overview of memory state. For detailed
searches, use `/recall`. For memory operations, use `/remember` or
the `ww-store`/`ww-recall` skills directly.
