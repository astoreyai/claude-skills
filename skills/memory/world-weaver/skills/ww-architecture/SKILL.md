---
name: ww-architecture
description: Architecture documentation generation and maintenance for World Weaver
version: 1.0.0
allowed-tools: ['Bash', 'Read', 'Write', 'Grep', 'Glob']
---

# WW Architecture Skill

Architecture documentation generation and maintenance for World Weaver.

## Purpose

This skill provides architecture documentation capabilities:
1. **Generate Docs**: Auto-generate architecture documentation from code
2. **Update Docs**: Keep documentation in sync with code changes
3. **Visualize**: Create diagrams from code structure
4. **Validate**: Check documentation accuracy against implementation

## When to Use

Invoke this skill when:
- User asks "document the architecture"
- User asks "generate a diagram"
- User asks "what's the system structure"
- Code changes require doc updates
- Architecture review is needed

## Documentation Generation Workflows

### 1. Module Documentation

Parse Python modules and generate docs:

```bash
# Find all modules
find /home/aaron/ww/src/ww -name "*.py" -not -name "__init__.py"

# Extract docstrings
python -c "
import ast
import sys

with open(sys.argv[1]) as f:
    tree = ast.parse(f.read())

module_doc = ast.get_docstring(tree)
print(f'# Module: {sys.argv[1]}')
print(module_doc or 'No module docstring')

for node in ast.walk(tree):
    if isinstance(node, ast.ClassDef):
        print(f'## Class: {node.name}')
        print(ast.get_docstring(node) or 'No class docstring')
    elif isinstance(node, ast.FunctionDef):
        print(f'### Function: {node.name}')
        print(ast.get_docstring(node) or 'No function docstring')
" "$file"
```

### 2. Dependency Graph

Generate module dependency graph:

```python
import ast
from pathlib import Path

def extract_imports(file_path):
    with open(file_path) as f:
        tree = ast.parse(f.read())

    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append(node.module)
    return imports

# Build dependency graph
dependencies = {}
for py_file in Path('/home/aaron/ww/src/ww').rglob('*.py'):
    module = str(py_file.relative_to('/home/aaron/ww/src'))
    dependencies[module] = extract_imports(py_file)
```

### 3. Mermaid Diagram Generation

Generate architecture diagrams:

```markdown
## System Architecture

\`\`\`mermaid
graph TB
    subgraph Plugin["WW Plugin"]
        Skills[Skills]
        Commands[Commands]
        Hooks[Hooks]
        Agents[Agents]
    end

    subgraph MCP["MCP Server"]
        Gateway[Gateway]
        Episodic[Episodic Store]
        Semantic[Semantic Store]
        Procedural[Procedural Store]
    end

    subgraph Storage["Storage Layer"]
        Neo4j[(Neo4j)]
        Qdrant[(Qdrant)]
    end

    Plugin --> Gateway
    Gateway --> Episodic
    Gateway --> Semantic
    Gateway --> Procedural
    Episodic --> Qdrant
    Semantic --> Neo4j
    Semantic --> Qdrant
    Procedural --> Neo4j
\`\`\`
```

### 4. API Documentation

Generate API docs from MCP tools:

```python
# Extract MCP tool definitions
tools = [
    ("create_episode", "Store autobiographical event"),
    ("recall_episodes", "Search episodes by query"),
    ("create_entity", "Add knowledge graph node"),
    ("semantic_recall", "Search knowledge graph"),
    ("create_skill", "Store procedural pattern"),
    # ... etc
]

# Generate OpenAPI-style docs
for name, description in tools:
    print(f"""
### mcp__ww-memory__{name}

**Description**: {description}

**Parameters**:
| Name | Type | Required | Description |
|------|------|----------|-------------|
| ... | ... | ... | ... |

**Returns**: ...

**Example**:
\`\`\`python
mcp__ww-memory__{name}(...)
\`\`\`
""")
```

## Documentation Templates

### Component Documentation

```markdown
# {Component Name}

## Overview
{Brief description}

## Responsibilities
- {Responsibility 1}
- {Responsibility 2}

## Dependencies
- {Dependency 1}: {Why needed}
- {Dependency 2}: {Why needed}

## Interfaces

### Public API
\`\`\`python
{method signatures}
\`\`\`

### Events Emitted
- {Event 1}: {When/why}

### Events Consumed
- {Event 1}: {From where}

## Data Structures

### {Structure Name}
\`\`\`python
{structure definition}
\`\`\`

## Configuration
| Key | Type | Default | Description |
|-----|------|---------|-------------|
| ... | ... | ... | ... |

## Error Handling
{Error handling strategy}

## Testing
{Testing approach}
```

### Architecture Decision Record (ADR)

```markdown
# ADR-{number}: {Title}

## Status
{Proposed | Accepted | Deprecated | Superseded}

## Context
{What is the issue that we're seeing that is motivating this decision?}

## Decision
{What is the change that we're proposing and/or doing?}

## Consequences
{What becomes easier or more difficult to do because of this change?}

### Positive
- {Benefit 1}

### Negative
- {Drawback 1}

### Neutral
- {Tradeoff 1}
```

## Output Locations

Generated documentation:
- `/home/aaron/ww/docs/architecture/` - Architecture docs
- `/home/aaron/ww/docs/api/` - API reference
- `/home/aaron/ww/docs/adr/` - Decision records
- `/home/aaron/mem/WW_ARCHITECTURE.md` - Overview

## Validation

Check documentation accuracy:

```bash
# Find undocumented public functions
grep -r "^def " /home/aaron/ww/src/ww --include="*.py" | while read line; do
    # Check if docstring exists
    ...
done

# Find stale documentation references
# Check if mentioned files still exist
grep -r "src/ww/" /home/aaron/ww/docs/ | while read line; do
    path=$(echo "$line" | grep -oP 'src/ww/\S+\.py')
    if [ ! -f "/home/aaron/ww/$path" ]; then
        echo "Stale reference: $path"
    fi
done
```

## Integration

This skill integrates with:
- **ww-analyze**: Provides code structure data
- **ww-visualize**: Renders diagrams
- **Session hooks**: Can auto-update docs on changes

## Error Handling

If documentation generation fails:
1. Log partial results
2. Identify parsing errors
3. Continue with other files
4. Report incomplete status
