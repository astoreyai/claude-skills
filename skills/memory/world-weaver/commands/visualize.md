# /ww-visualize Command

Generate visualizations of World Weaver memory systems and architecture.

## Usage

```
/ww-visualize [type] [options]
```

## Arguments

- `type`: Visualization type
  - `graph` - Knowledge graph diagram
  - `timeline` - Memory timeline
  - `architecture` - System architecture
  - `bugs` - Bug distribution chart
  - `flow` - Data flow sequence diagram
  - `learning` - Learning progress chart

## Options

- `--limit N` - Max items to include (default: 50)
- `--days N` - Lookback days for timeline (default: 7)
- `--min-weight N` - Min relationship weight for graph (default: 0.3)
- `--format FMT` - Output format (mermaid, ascii, dot)
- `--output PATH` - Save to file

## Examples

```bash
# Show knowledge graph
/ww-visualize graph

# Show last week's timeline
/ww-visualize timeline --days 7

# Show architecture diagram
/ww-visualize architecture

# Show bug distribution from audit
/ww-visualize bugs

# Show data flow
/ww-visualize flow
```

## Output

Visualizations are:
1. Displayed inline (Mermaid format)
2. Optionally saved to `/home/aaron/mem/WW_VIZ_{type}_{timestamp}.md`

## Supported Formats

- **Mermaid**: Markdown-embeddable diagrams
- **ASCII**: Terminal-friendly text diagrams
- **DOT**: Graphviz format for external rendering
