# Obsidian Research Synthesis

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Status](https://img.shields.io/badge/status-stable-green)
![License](https://img.shields.io/badge/license-MIT-green)

## Description

Comprehensive research workflows within Obsidian: search for information across your vault, analyze and synthesize findings from multiple notes, and create well-structured research documentation with proper citations.

This skill enables deep research by searching across your entire vault using filesystem search, grep, and Dataview queries, then synthesizing findings into cohesive research reports with proper wiki-link citations and cross-referencing.

## Features

- ✅ Powerful vault-wide search using filesystem tools and grep
- ✅ Multi-note synthesis with automated citation linking
- ✅ Multiple output formats (summary, comprehensive report, literature review, synthesis note)
- ✅ Dataview query integration for dynamic research tracking
- ✅ Citation patterns with conflict handling and source attribution
- ✅ Network and temporal analysis of knowledge connections
- ✅ Gap analysis to identify missing information
- ✅ Quality checks for research completeness

## Installation

### Prerequisites

- Claude Code installed
- Obsidian vault with accessible filesystem path
- Basic knowledge of grep and filesystem search
- Optional: Obsidian Dataview plugin

### Setup

1. Copy this skill to your Claude Code skills directory:
   ```bash
   cp -r obsidian-research-synthesis ~/.claude/skills/
   ```

2. Configure your vault path:
   ```bash
   export OBSIDIAN_VAULT_PATH="/path/to/your/vault"
   ```

3. Ensure grep is available on your system (pre-installed on most Unix systems)

## Usage

### Basic Usage

Ask Claude to research a topic across your vault:

```
"Research everything in my vault about microservices architecture"
"Synthesize findings on event-driven design from my notes"
"Create a literature review on the API versioning discussions"
```

Claude will:
1. Search your vault using multiple strategies
2. Read and extract relevant information from found notes
3. Analyze patterns and connections
4. Synthesize findings into structured documentation
5. Add proper citations with wiki-links

### Research Output Formats

| Format | Use Case | Length |
|--------|----------|--------|
| Research Summary | Quick overview | 1-2 pages |
| Comprehensive Report | Full analysis | 5-10 pages |
| Literature Review | Academic-style | 3-5 pages |
| Synthesis Note | Integration of sources | 2-4 pages |

### Configuration Options

| Search Strategy | Method | Best For |
|-----------------|--------|----------|
| Topic-based | Keywords | Broad exploration |
| Tag-based | Frontmatter tags | Categorized notes |
| Date-based | File modification time | Recent developments |
| Link-based | Backlinks | Connected concepts |

## Examples

### Example 1: Topic Research Summary

**Input:**
```
"Research database design patterns in my vault and create a summary"
```

**Output:**
Research summary note with:
- Executive summary of findings
- Key themes across multiple notes
- Citations to source notes with [[wiki-links]]
- Identified gaps in knowledge
- Further research questions

### Example 2: Comprehensive Report

**Input:**
```
"Create a comprehensive report on our authentication strategy discussions"
```

**Output:**
Detailed report including:
- Background and context
- Findings organized by theme
- Analysis with evidence from sources
- Conclusions and recommendations
- Complete references section

## Troubleshooting

### Common Issues

**Issue 1: Too many search results**
- **Cause**: Overly broad search terms
- **Solution**: Add more specific keywords, filter by date range or folder

**Issue 2: Results not relevant**
- **Cause**: Search terms don't match content
- **Solution**: Try synonyms, search by links instead of content

**Issue 3: Missing key information**
- **Cause**: Information not yet documented
- **Solution**: Note gaps in research document, create follow-up tasks

## Dependencies

- Filesystem access for reading Markdown files
- grep (or ripgrep) for content search
- Optional: Obsidian Dataview plugin for advanced queries

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and updates.

## Contributing

This is a personal skill library. Feel free to fork and adapt for your needs.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Author

Aaron Storey (@astoreyai)

## Related Skills

- [Obsidian Knowledge Capture](../obsidian-knowledge-capture/) - Capture insights
- [Obsidian Meeting Prep](../obsidian-meeting-prep/) - Meeting preparation
- [Obsidian Spec to Implementation](../obsidian-spec-to-implementation/) - Implementation planning

## Additional Resources

- [Obsidian Documentation](https://help.obsidian.md/)
- [Research Synthesis Methods](https://methods.sagepub.com/reference/encyclopedia-of-research-design)
- [Zettelkasten Research Method](https://zettelkasten.de/)
