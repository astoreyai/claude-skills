---
name: ww-visualize
description: Memory visualization and diagramming for World Weaver systems
version: 1.0.0
allowed-tools: ['Bash', 'Read', 'Write', 'Grep', 'Glob']
---

# WW Visualize Skill

Memory visualization and diagramming for World Weaver systems.

## Purpose

This skill provides visualization capabilities:
1. **Memory Graphs**: Visualize knowledge graph structure
2. **Timeline Views**: Show memory evolution over time
3. **Architecture Diagrams**: System component diagrams
4. **Analysis Charts**: Bug distributions, metrics
5. **Learning Curves**: Training progress visualization

## When to Use

Invoke this skill when:
- User asks "show me the memory graph"
- User asks "visualize the architecture"
- User wants to see memory patterns
- Analysis results need visualization
- Documentation needs diagrams

## Visualization Types

### 1. Knowledge Graph Visualization

Generate Mermaid diagram of entity relationships:

```python
def generate_knowledge_graph(entities, relationships):
    """Generate Mermaid graph from WW semantic memory."""
    lines = ["graph LR"]

    # Add entities
    for entity in entities:
        node_id = entity['name'].replace(' ', '_')
        lines.append(f"    {node_id}[{entity['name']}]")

    # Add relationships
    for rel in relationships:
        src = rel['source'].replace(' ', '_')
        tgt = rel['target'].replace(' ', '_')
        label = rel['type']
        weight = rel.get('weight', 1.0)

        # Thicker line for stronger relationships
        if weight > 0.7:
            lines.append(f"    {src} =={label}==> {tgt}")
        else:
            lines.append(f"    {src} --{label}--> {tgt}")

    return '\n'.join(lines)
```

Output:
```mermaid
graph LR
    Hebbian_Learning[Hebbian Learning]
    STDP[STDP]
    Eligibility_Traces[Eligibility Traces]

    Hebbian_Learning ==USES==> STDP
    STDP --REQUIRES--> Eligibility_Traces
```

### 2. Memory Timeline

Generate timeline of episodes:

```python
def generate_timeline(episodes):
    """Generate Mermaid timeline from episodes."""
    lines = ["gantt", "    title Memory Timeline", "    dateFormat YYYY-MM-DD"]

    # Group by project
    by_project = defaultdict(list)
    for ep in episodes:
        project = ep.get('context', {}).get('project', 'Unknown')
        by_project[project].append(ep)

    for project, eps in by_project.items():
        lines.append(f"    section {project}")
        for ep in eps:
            date = ep['timestamp'][:10]
            outcome = ep['outcome']
            icon = "crit" if outcome == "failure" else ""
            lines.append(f"    {ep['content'][:30]} :{icon} {date}, 1d")

    return '\n'.join(lines)
```

### 3. Architecture Component Diagram

```mermaid
flowchart TB
    subgraph Plugin["Claude Code Plugin"]
        direction TB
        Skills["Skills<br/>store, recall, context, consolidate<br/>analyze, diagnose, visualize, architecture"]
        Commands["Commands<br/>/remember, /recall, /consolidate<br/>/ww-audit, /ww-visualize"]
        Hooks["Hooks<br/>SessionStart, SessionEnd"]
        Agents["Agents<br/>memory, retriever, synthesizer<br/>bio-auditor, race-hunter, leak-hunter<br/>hinton-validator, cache-analyzer, trace-debugger"]
    end

    subgraph MCP["MCP Server"]
        direction TB
        Gateway["Request Gateway"]
        Memory["Memory Manager"]
        Learning["Learning System"]
        Consolidation["Consolidation Engine"]
    end

    subgraph Core["Core Systems"]
        direction TB
        Episodic["Episodic Store<br/>Fast learning, autobiographical"]
        Semantic["Semantic Store<br/>Slow learning, knowledge graph"]
        Procedural["Procedural Store<br/>Skills, patterns"]
    end

    subgraph Storage["Storage"]
        Neo4j[(Neo4j<br/>Graph DB)]
        Qdrant[(Qdrant<br/>Vector DB)]
    end

    Plugin --> MCP
    MCP --> Core
    Core --> Storage
```

### 4. Bug Distribution Chart

```python
def generate_bug_chart(bugs):
    """Generate bug distribution visualization."""
    by_severity = defaultdict(int)
    by_type = defaultdict(int)

    for bug in bugs:
        by_severity[bug['severity']] += 1
        by_type[bug['type']] += 1

    # Mermaid pie chart
    lines = ["pie showData", "    title Bug Distribution by Severity"]
    for severity, count in by_severity.items():
        lines.append(f'    "{severity}" : {count}')

    return '\n'.join(lines)
```

```mermaid
pie showData
    title Bug Distribution by Severity
    "CRITICAL" : 133
    "HIGH" : 180
    "MEDIUM" : 212
    "LOW" : 145
```

### 5. Learning Progress

```python
def generate_learning_curve(metrics):
    """Generate learning progress chart."""
    lines = [
        "xychart-beta",
        "    title Learning Progress",
        '    x-axis ["Step 1", "Step 2", "Step 3", "Step 4", "Step 5"]',
        f'    y-axis "Loss" 0 --> 1',
        f'    line [{", ".join(str(m["loss"]) for m in metrics)}]'
    ]
    return '\n'.join(lines)
```

### 6. Memory System Flow

```mermaid
sequenceDiagram
    participant User
    participant Plugin
    participant MCP
    participant Episodic
    participant Semantic
    participant Storage

    User->>Plugin: /remember "Fixed bug"
    Plugin->>MCP: create_episode()
    MCP->>Episodic: store()
    Episodic->>Storage: insert(Neo4j)
    Episodic->>Storage: embed(Qdrant)
    Storage-->>MCP: success
    MCP-->>Plugin: episode_id
    Plugin-->>User: Stored!
```

## Output Formats

Visualizations can be generated as:
1. **Mermaid** - For markdown embedding
2. **ASCII** - For terminal display
3. **JSON** - For web rendering
4. **DOT** - For Graphviz

## Commands

```bash
# Generate knowledge graph
/ww-visualize graph --limit 50 --min-weight 0.3

# Generate timeline
/ww-visualize timeline --days 7

# Generate architecture
/ww-visualize architecture

# Generate bug chart
/ww-visualize bugs --from /home/aaron/mem/MASTER_BUG_LIST.md
```

## Integration

This skill integrates with:
- **ww-analyze**: Visualize analysis results
- **ww-diagnose**: Show diagnostic flowcharts
- **ww-architecture**: Embed in documentation
- **MCP server**: Query memory data

## Output Locations

Generated visualizations:
- `/home/aaron/mem/WW_GRAPH_{timestamp}.md` - Knowledge graphs
- `/home/aaron/mem/WW_TIMELINE_{timestamp}.md` - Timelines
- `/home/aaron/mem/WW_ARCHITECTURE_{timestamp}.md` - Architecture
- `/home/aaron/ww/docs/diagrams/` - Persistent diagrams

## Error Handling

If visualization fails:
1. Check data availability
2. Fall back to simpler visualization
3. Provide raw data if rendering fails
4. Log error with context
