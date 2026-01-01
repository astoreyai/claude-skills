---
name: ww-context
description: Build comprehensive memory context from World Weaver for current task
version: 1.0.0
allowed-tools: ['Bash', 'Read']
---

# WW Context Skill

Build comprehensive context from World Weaver memories tailored to the current task, project, and working directory.

## Purpose

This skill synthesizes memories from all three subsystems (episodic, semantic, procedural) into actionable context for Claude. Unlike raw retrieval, it:
- Prioritizes relevance to current work
- Removes redundancy
- Highlights applicable skills
- Identifies knowledge gaps

## When to Use

Invoke this skill when:
- Starting work on a task and need background
- User asks "what do we know about X?"
- Context seems missing from conversation
- Switching between projects
- Before making significant decisions

## MCP Tools Used

```
mcp__ww-memory__recall_episodes    - Recent relevant episodes
mcp__ww-memory__semantic_recall    - Related entities
mcp__ww-memory__spread_activation  - Entity connections
mcp__ww-memory__recall_skill       - Applicable procedures
mcp__ww-memory__memory_stats       - System metrics
```

## Context Building Workflow

### Step 1: Gather Environmental Context
```bash
# Current directory
pwd

# Project identification
basename $(pwd)
git remote get-url origin 2>/dev/null || echo "Not a git repo"

# Recent activity
git log --oneline -5 2>/dev/null
git status --short 2>/dev/null
```

### Step 2: Query Memory Systems

**Episodic Query**:
```
mcp__ww-memory__recall_episodes(
  query="[project name] [current task keywords]",
  limit=10,
  time_filter={after: "7 days ago"}
)
```

**Semantic Query**:
```
mcp__ww-memory__semantic_recall(
  query="[project name] [topic]",
  limit=15,
  include_relationships=true
)
```

**Skill Query**:
```
mcp__ww-memory__recall_skill(
  query="how to [task] in [project]",
  limit=5,
  check_preconditions=true,
  context={project, cwd}
)
```

### Step 3: Synthesize Context

Combine results into structured context:

```markdown
## Memory Context for [Task/Topic]

### Project: [Name]
- Directory: [path]
- Last activity: [date]
- Current state: [from git status]

### Relevant History
[Summarized episodes - what happened before]
- [Episode 1 summary]
- [Episode 2 summary]

### Key Knowledge
[Entities and their relationships]
- **[Entity A]**: [summary] → connected to [B, C]
- **[Entity B]**: [summary]

### Applicable Skills
[Procedures that match current context]
1. **[Skill name]**: [what it does]
   - Preconditions: [met/not met]
   - Steps: [brief outline]

### Gaps
[What's missing from memory]
- No recent episodes about [X]
- No skill for [Y]

### Recommendations
[Suggested actions based on context]
```

### Step 4: Prioritize and Filter

Apply these filters:
1. **Recency**: Weight recent episodes higher
2. **Relevance**: Score against current task keywords
3. **Diversity**: Include different memory types
4. **Actionability**: Highlight immediately useful info

## Output Formats

### Brief Context (for quick reference)
```markdown
**Context**: Working on [project], [task].
**Recent**: [1-2 relevant episodes]
**Know**: [2-3 key entities]
**Can use**: [1-2 skills]
```

### Standard Context (default)
```markdown
## Context: [Topic]

### Recent Work (3-5 episodes)
- [Episode summaries with dates]

### Key Knowledge (5-10 entities)
- [Entity name]: [summary]

### Skills (2-3 applicable)
- [Skill]: [brief description]

### Suggestions
- [Based on patterns in memory]
```

### Deep Context (for complex tasks)
```markdown
## Deep Context: [Topic]

### Timeline
[Chronological narrative of relevant work]

### Knowledge Graph
[Entity relationships visualized]
```
[A] --uses--> [B]
[A] --relates--> [C]
```

### Full Skill Details
[Complete procedure for top skill]

### Pattern Analysis
[Recurring themes from episodes]

### Open Questions
[Uncertainties and gaps]
```

## Context Quality Guidelines

### Include
- Directly relevant episodes (score > 0.7)
- Entities connected to current project
- Skills matching preconditions
- Recent decisions and their outcomes

### Exclude
- Old episodes (> 30 days) unless highly relevant
- Entities with no project connection
- Skills with unmet preconditions
- Redundant/duplicate information

### Highlight
- Failures and lessons learned
- Successful patterns
- Unfinished work from previous sessions
- High-importance events

## Examples

### Example 1: Starting Work on Testing
```
Context request: "Build context for improving test coverage"

Output:
## Context: Test Coverage Improvement

### Recent Work
- [Nov 27] Fixed UUID import in benchmark test - success
- [Nov 26] Added pytest markers for HDBSCAN tests - success
- [Nov 25] Implemented session isolation tests - success

### Key Knowledge
- **pytest**: Test framework for Python
  - Connected to: coverage, markers, fixtures
- **Session Isolation**: Testing pattern for multi-tenant
  - Related: Neo4j, Qdrant, session_id

### Applicable Skills
1. **run-ww-tests**: Execute test suite
   - Steps: activate venv → pytest tests/ -v
   - Preconditions: Met (in WW directory)

2. **add-test-markers**: Mark tests for selective running
   - Steps: Add @pytest.mark decorator
   - Preconditions: Met

### Suggestions
- Current coverage: 79% - consider targeting uncovered modules
- Recent focus: integration tests - unit tests may need attention
```

### Example 2: Debugging Issue
```
Context request: "Build context for Neo4j connection issues"

Output:
## Context: Neo4j Connection Debugging

### Recent Work
- [Nov 26] Fixed batch query parameter - changed $id to id
- [Nov 25] Investigated N+1 query pattern
- [Nov 24] Added connection pooling (50 connections)

### Key Knowledge
- **Neo4j**: Graph database, bolt://localhost:7687
  - Related: Cypher, Connection Pooling, Batch Queries
- **Connection Pooling**: 50 max connections
  - Config: pool_size in neo4j_store.py

### Applicable Skills
1. **debug-neo4j**: Check Neo4j connectivity
   - Test: curl http://localhost:7474
   - Logs: docker logs neo4j

### Suggestions
- Recent $id bug suggests parameter naming issues
- Check if variable vs parameter in Cypher
- Verify pool not exhausted
```

## Integration

This skill is called by:
- `/ww-context` command
- `ww-synthesizer` agent
- SessionStart hook (for initial context)
- Other skills needing memory context
