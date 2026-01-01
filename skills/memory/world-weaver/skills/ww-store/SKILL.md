---
name: ww-store
description: Store memories in World Weaver's tripartite memory system (episodes, entities, skills)
version: 1.0.0
allowed-tools: ['Bash', 'Read', 'Write']
---

# WW Store Skill

Store information in World Weaver's tripartite memory system using the MCP gateway.

## Purpose

This skill stores three types of memories:
1. **Episodes**: Autobiographical events (what happened, when, outcome)
2. **Entities**: Knowledge graph nodes (concepts, people, places)
3. **Skills**: Procedural patterns (how to do things)

## When to Use

Invoke this skill when:
- User says "remember this", "store this", "save for later"
- A significant milestone is reached
- An important decision is made
- A new concept or entity is encountered
- A successful pattern emerges that could be reused

## MCP Tools Available

The World Weaver MCP server (`ww-memory`) provides these tools:

```
mcp__ww-memory__create_episode     - Store autobiographical event
mcp__ww-memory__create_entity      - Add knowledge graph node
mcp__ww-memory__create_relation    - Link entities
mcp__ww-memory__create_skill       - Store procedural pattern
```

## Episode Storage Workflow

When storing an episode:

### 1. Extract Context
Gather from current environment:
```bash
# Working directory
pwd

# Current project (from git or directory name)
basename $(pwd)

# Recent git activity
git log --oneline -3 2>/dev/null || echo "Not a git repo"
```

### 2. Classify Outcome
Determine outcome from conversation:
- **success**: Task completed, goal achieved
- **failure**: Task failed, error occurred
- **partial**: Some progress, incomplete
- **neutral**: Informational, no specific outcome

### 3. Assess Importance
Rate emotional valence (0.0 to 1.0):
- 1.0: Critical milestone, major breakthrough
- 0.7-0.9: Important achievement, significant learning
- 0.4-0.6: Normal work, routine task
- 0.1-0.3: Minor note, low importance

### 4. Store Episode
Call MCP tool:
```
mcp__ww-memory__create_episode(
  content: "Full description of what happened",
  outcome: "success|failure|partial|neutral",
  emotional_valence: 0.0-1.0,
  context: {
    project: "project-name",
    working_directory: "/path/to/project",
    tool: "tool-used-if-any",
    file: "file-modified-if-any"
  }
)
```

## Entity Storage Workflow

When creating an entity:

### 1. Classify Entity Type
- **CONCEPT**: Abstract idea, technology, pattern
- **PERSON**: Individual (collaborator, author, etc.)
- **PLACE**: Location (server, environment, path)
- **EVENT**: Specific occurrence (release, meeting)
- **OBJECT**: Concrete thing (file, repository, tool)
- **SKILL**: Capability or procedure

### 2. Generate Summary
Create 1-2 sentence description of the entity.

### 3. Store Entity
```
mcp__ww-memory__create_entity(
  name: "Entity Name",
  entity_type: "CONCEPT|PERSON|PLACE|EVENT|OBJECT|SKILL",
  summary: "Brief description of the entity",
  details: "Optional longer description"
)
```

### 4. Create Relations
Link to existing entities:
```
mcp__ww-memory__create_relation(
  source_name: "Entity A",
  target_name: "Entity B",
  relation_type: "RELATES_TO|PART_OF|USED_BY|DEPENDS_ON",
  properties: {
    context: "How they relate"
  }
)
```

## Skill Storage Workflow

When storing a procedural skill:

### 1. Extract Procedure
Document the steps that worked:
```
1. First, do X
2. Then, do Y
3. Finally, do Z
```

### 2. Define Parameters
What inputs does this skill need?
```json
{
  "param1": {"type": "string", "description": "What it's for"},
  "param2": {"type": "number", "description": "What it controls"}
}
```

### 3. Define Conditions
- **Preconditions**: What must be true before executing
- **Postconditions**: What will be true after executing

### 4. Store Skill
```
mcp__ww-memory__create_skill(
  name: "skill-name",
  description: "What this skill does",
  procedure: "Step by step instructions",
  parameters: {...},
  preconditions: ["condition1", "condition2"],
  postconditions: ["result1", "result2"],
  tags: ["tag1", "tag2"]
)
```

## Examples

### Example 1: Store Episode After Bug Fix
```
User: "Remember that I fixed the batch query bug"

Action:
1. Extract: cwd=/home/aaron/ww, project=ww
2. Outcome: success (bug fixed)
3. Valence: 0.7 (important fix)
4. Store:
   mcp__ww-memory__create_episode(
     content="Fixed batch query bug in Neo4j store. Changed $id to id for UNWIND variable, fixed return structure to use other_id and nested properties.",
     outcome="success",
     emotional_valence=0.7,
     context={project: "ww", working_directory: "/home/aaron/ww"}
   )
```

### Example 2: Store New Concept Entity
```
User: "Remember what Hebbian learning is"

Action:
1. Type: CONCEPT
2. Summary: Neural learning rule where connections strengthen through co-activation
3. Store:
   mcp__ww-memory__create_entity(
     name="Hebbian Learning",
     entity_type="CONCEPT",
     summary="Neural learning principle: neurons that fire together wire together. Connections strengthen when nodes are co-activated.",
     details="Used in World Weaver semantic memory to strengthen relationships between co-retrieved entities."
   )
```

### Example 3: Store Procedural Skill
```
User: "Remember how to run the WW tests"

Action:
1. Procedure: activate venv, run pytest
2. Parameters: test path, markers
3. Store:
   mcp__ww-memory__create_skill(
     name="run-ww-tests",
     description="Run World Weaver test suite",
     procedure="1. source .venv/bin/activate\n2. pytest tests/ -v\n3. Check output for failures",
     parameters={
       "path": {"type": "string", "default": "tests/", "description": "Test path"},
       "markers": {"type": "string", "default": "", "description": "Pytest markers"}
     },
     preconditions=["In WW project directory", "Virtual environment exists"],
     postconditions=["Test results displayed", "Coverage report generated"],
     tags=["testing", "pytest", "ww"]
   )
```

## Quality Checklist

Before storing:
- [ ] Content is specific and actionable
- [ ] Outcome classification is accurate
- [ ] Importance rating reflects actual significance
- [ ] Context includes relevant project/file info
- [ ] Entity types are correctly classified
- [ ] Relations link to existing entities where possible

## Error Handling

If MCP tool fails:
1. Check if ww-memory server is running
2. Verify Neo4j/Qdrant are accessible
3. Fall back to logging the memory request for later storage
