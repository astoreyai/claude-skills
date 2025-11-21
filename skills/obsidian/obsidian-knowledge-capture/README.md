# Obsidian Knowledge Capture

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Status](https://img.shields.io/badge/status-stable-green)
![License](https://img.shields.io/badge/license-MIT-green)

## Description

Transform conversations, discussions, and insights into structured documentation within your Obsidian vault.

This skill captures knowledge from chat context, formats it with appropriate templates and frontmatter, and saves it with proper organization, tags, and links for easy discovery. Perfect for building a searchable knowledge base from conversations, meetings, and collaborative discussions.

## Features

- ✅ Extract insights from conversations and transform into structured notes
- ✅ Multiple content types: concepts, how-tos, decisions, FAQs, meetings, patterns
- ✅ Automatic frontmatter generation with metadata and tags
- ✅ Intelligent vault organization with flexible folder structures
- ✅ Bidirectional linking and Map of Content (MOC) integration
- ✅ Consistent tagging strategy for discoverability
- ✅ Dataview query support for dynamic note organization
- ✅ Template-based content structuring

## Installation

### Prerequisites

- Claude Code installed
- Obsidian vault with accessible filesystem path
- Basic understanding of Markdown and Obsidian conventions

### Setup

1. Copy this skill to your Claude Code skills directory:
   ```bash
   cp -r obsidian-knowledge-capture ~/.claude/skills/
   ```

2. Configure your vault path:
   ```bash
   # Set your Obsidian vault location
   export OBSIDIAN_VAULT_PATH="/path/to/your/vault"
   ```

3. (Optional) Customize templates in `reference/content-types.md`

## Usage

### Basic Usage

Ask Claude to capture knowledge from your conversation:

```
"Save this discussion about microservices architecture to my Obsidian vault"
"Create a how-to guide for deploying to production from this conversation"
"Document this decision about choosing PostgreSQL over MongoDB"
```

Claude will:
1. Extract key information from the conversation
2. Determine the appropriate content type
3. Apply the right template structure
4. Choose the optimal vault location
5. Create the note with proper frontmatter
6. Add tags and links for discoverability

### Content Types

**Concept Note** - Explaining what something is
**How-To Guide** - Step-by-step instructions
**Decision Record** - Important decisions with rationale
**FAQ Entry** - Common questions and answers
**Meeting Summary** - Meeting notes and outcomes
**Learning/Post-Mortem** - Lessons from experience
**Reference Documentation** - Technical or factual reference
**Pattern** - Reusable solution or approach

### Configuration Options

Content can be organized in multiple ways:

| Structure | Use Case | Location |
|-----------|----------|----------|
| General KB | Cross-project knowledge | `vault/knowledge/` |
| Project-specific | Project documentation | `vault/projects/project-name/docs/` |
| Team wiki | Team processes | `vault/team/` |
| Domain-organized | By expertise area | `vault/domains/engineering/` |

## Examples

### Example 1: Capture Concept from Discussion

**Input:**
```
User: "Claude, explain event-driven architecture"
Claude: [provides detailed explanation]
User: "Save this as a concept note in my vault"
```

**Output:**
```markdown
---
type: concept
tags: [concept, architecture, event-driven]
created: 2025-11-05
---

# Concept: Event-Driven Architecture

## Overview
A software design pattern where...
[full structured content]
```

### Example 2: Create How-To from Conversation

**Input:**
Discussion about troubleshooting database connection issues.

**Output:**
Structured how-to guide saved at `vault/knowledge/how-to/troubleshoot-db-connections.md` with step-by-step instructions, prerequisites, and troubleshooting tips.

## Troubleshooting

### Common Issues

**Issue 1: Vault path not found**
- **Cause**: `OBSIDIAN_VAULT_PATH` not set or incorrect
- **Solution**: Set the environment variable or provide path explicitly

**Issue 2: Note already exists**
- **Cause**: Similar content was previously captured
- **Solution**: Search vault first, update existing note if found

**Issue 3: Missing context**
- **Cause**: Insufficient information in conversation
- **Solution**: Provide more details or ask clarifying questions

## Dependencies

- Access to filesystem for writing Markdown files
- Optional: Obsidian Dataview plugin for dynamic queries
- Optional: Obsidian Templates plugin for enhanced templating

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and updates.

## Contributing

This is a personal skill library. Feel free to fork and adapt for your needs.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Author

Aaron Storey (@astoreyai)

## Related Skills

- [Obsidian Meeting Prep](../obsidian-meeting-prep/) - Prepare meeting materials
- [Obsidian Research Synthesis](../obsidian-research-synthesis/) - Research workflows
- [Obsidian Spec to Implementation](../obsidian-spec-to-implementation/) - Specification workflows

## Additional Resources

- [Obsidian Documentation](https://help.obsidian.md/)
- [Dataview Plugin](https://blacksmithgu.github.io/obsidian-dataview/)
- [Zettelkasten Method](https://zettelkasten.de/)
