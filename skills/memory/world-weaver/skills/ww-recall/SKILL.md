---
name: ww-recall
description: Recall memories from World Weaver using multi-strategy retrieval
version: 1.0.0
allowed-tools: ['Bash', 'Read']
---

# WW Recall Skill

Multi-strategy memory retrieval from World Weaver's tripartite memory system.

## Purpose

Search and retrieve relevant memories from:
1. **Episodic Memory**: Past experiences and events
2. **Semantic Memory**: Knowledge graph entities and relationships
3. **Procedural Memory**: Skills and how-to patterns

## When to Use

Invoke this skill when:
- User asks "what did we do before?", "do you remember?"
- Need context from previous sessions
- Looking for relevant past experiences
- Searching for applicable skills
- Building context for a new task

## MCP Tools Available

```
mcp__ww-memory__recall_episodes    - Search episodic memory
mcp__ww-memory__semantic_recall    - Search knowledge graph
mcp__ww-memory__spread_activation  - Graph traversal from seed
mcp__ww-memory__recall_skill       - Find applicable skills
mcp__ww-memory__query_at_time      - Point-in-time queries
```

## Retrieval Strategies

### Strategy 1: Semantic Search (Default)
Best for: General queries, finding similar content

```
mcp__ww-memory__recall_episodes(
  query: "your search query",
  limit: 10,
  session_filter: null  # All sessions, or specific session_id
)
```

Returns episodes ranked by:
- Semantic similarity to query (40%)
- Recency decay (25%)
- Outcome weight (20%)
- Importance/valence (15%)

### Strategy 2: Temporal Search
Best for: "What did we do last week?", time-bounded queries

```
mcp__ww-memory__recall_episodes(
  query: "project work",
  limit: 10,
  time_filter: {
    after: "2025-11-20T00:00:00",
    before: "2025-11-27T23:59:59"
  }
)
```

### Strategy 3: Knowledge Graph Search
Best for: Finding entities and their relationships

```
mcp__ww-memory__semantic_recall(
  query: "concept or entity name",
  limit: 10,
  include_relationships: true
)
```

### Strategy 4: Spread Activation
Best for: Exploring connections from a known starting point

```
mcp__ww-memory__spread_activation(
  seed_entities: ["Entity A", "Entity B"],
  max_depth: 2,
  min_weight: 0.3
)
```

Returns entities connected to seeds, weighted by relationship strength.

### Strategy 5: Skill Matching
Best for: "How do I...?", finding applicable procedures

```
mcp__ww-memory__recall_skill(
  query: "how to run tests",
  limit: 5,
  check_preconditions: true,
  context: {
    project: "ww",
    working_directory: "/home/aaron/ww"
  }
)
```

### Strategy 6: Point-in-Time Query
Best for: "What did we know at time X?"

```
mcp__ww-memory__query_at_time(
  query: "project status",
  as_of: "2025-11-15T12:00:00"
)
```

## Multi-Strategy Retrieval Workflow

For comprehensive recall, combine strategies:

### 1. Analyze Query
Determine what the user is looking for:
- Past events → Episodic (Strategy 1, 2)
- Concepts/entities → Semantic (Strategy 3, 4)
- How-to procedures → Procedural (Strategy 5)
- Historical state → Temporal (Strategy 6)

### 2. Execute Searches
Run appropriate strategies in parallel:
```
episodes = mcp__ww-memory__recall_episodes(query, limit=5)
entities = mcp__ww-memory__semantic_recall(query, limit=5)
skills = mcp__ww-memory__recall_skill(query, limit=3)
```

### 3. Merge Results
Combine results, removing duplicates by ID.

### 4. Rank Results
Re-rank by overall relevance:
- Query similarity
- Recency
- Source diversity (mix of episode/entity/skill)

### 5. Format Output
Present as structured context:

```markdown
## Memory Context

### Recent Episodes (3 found)
1. **[2025-11-27]** Fixed batch query bug in Neo4j store
   - Outcome: success
   - Relevance: 0.92

2. **[2025-11-26]** Implemented session isolation tests
   - Outcome: success
   - Relevance: 0.85

### Related Knowledge (2 entities)
1. **Neo4j** (CONCEPT)
   - Graph database used for relationships
   - Connected to: Qdrant, Cypher, World Weaver

2. **Batch Queries** (CONCEPT)
   - Optimization pattern for N+1 elimination

### Applicable Skills (1 found)
1. **run-ww-tests**
   - Run World Weaver test suite
   - Preconditions: In WW directory, venv exists
```

## Retrieval Parameters

### Common Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `query` | string | Search query text |
| `limit` | int | Max results (default: 10) |
| `session_filter` | string | Filter by session ID |
| `time_filter` | object | After/before timestamps |

### Episode-Specific

| Parameter | Type | Description |
|-----------|------|-------------|
| `outcome_filter` | string | success/failure/partial/neutral |
| `min_valence` | float | Minimum importance (0-1) |

### Entity-Specific

| Parameter | Type | Description |
|-----------|------|-------------|
| `entity_type` | string | CONCEPT/PERSON/PLACE/etc |
| `include_relationships` | bool | Include connected entities |

### Skill-Specific

| Parameter | Type | Description |
|-----------|------|-------------|
| `check_preconditions` | bool | Verify preconditions met |
| `min_success_rate` | float | Minimum skill success rate |

## Examples

### Example 1: General Recall
```
User: "What have we worked on recently?"

Action:
mcp__ww-memory__recall_episodes(
  query="recent work projects tasks",
  limit=10,
  time_filter={after: "7 days ago"}
)

Output:
Found 8 recent episodes:
1. [Nov 27] Plugin architecture planning for World Weaver
2. [Nov 27] Fixed batch query bugs, session isolation
3. [Nov 26] Implemented HDBSCAN memory clustering
...
```

### Example 2: Skill Lookup
```
User: "How do I run the integration tests?"

Action:
mcp__ww-memory__recall_skill(
  query="run integration tests",
  limit=3,
  check_preconditions=true
)

Output:
Found skill: run-ww-tests
Steps:
1. source .venv/bin/activate
2. pytest tests/integration/ -v -m integration
3. Check output for failures
```

### Example 3: Entity Exploration
```
User: "What do we know about Neo4j?"

Action:
1. mcp__ww-memory__semantic_recall(query="Neo4j", limit=1)
2. mcp__ww-memory__spread_activation(seed_entities=["Neo4j"], max_depth=2)

Output:
## Neo4j (CONCEPT)
Graph database for relationship storage.

### Connected Entities:
- Cypher (query language) - strength: 0.9
- Qdrant (co-storage) - strength: 0.8
- World Weaver (uses) - strength: 0.95
- Batch Queries (optimization) - strength: 0.7
```

### Example 4: Time-Bounded Search
```
User: "What did we do last week on the PhD project?"

Action:
mcp__ww-memory__recall_episodes(
  query="PhD dissertation xai",
  limit=10,
  time_filter={
    after: "2025-11-20",
    before: "2025-11-27"
  }
)

Output:
Found 4 episodes from Nov 20-27:
1. [Nov 25] Committee meeting preparation
2. [Nov 23] VGGFace2 dataset removal analysis
3. [Nov 21] Article C IEEE T-BIOM submission
4. [Nov 20] Experiment 6.1 planning
```

## Quality Guidelines

When presenting recall results:
- [ ] Show relevance scores when available
- [ ] Include timestamps for temporal context
- [ ] Link related entities when relevant
- [ ] Highlight applicable skills
- [ ] Indicate result source (episodic/semantic/procedural)

## Error Handling

If recall fails:
1. Check MCP server connectivity
2. Try simpler query (fewer filters)
3. Fall back to keyword-based grep of local files
4. Inform user what memories are unavailable
