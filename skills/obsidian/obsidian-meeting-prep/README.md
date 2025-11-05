# Obsidian Meeting Prep

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Status](https://img.shields.io/badge/status-stable-green)
![License](https://img.shields.io/badge/license-MIT-green)

## Description

Comprehensive meeting preparation by gathering context from your Obsidian vault and creating structured meeting materials.

This skill searches your vault for relevant project notes, previous meetings, specs, and decisions, then generates both internal prep notes with background information and external-facing agendas with meeting structure. Perfect for ensuring you're fully prepared with all context needed for effective meetings.

## Features

- ✅ Automated context gathering from vault using filesystem search and grep
- ✅ Intelligent search across projects, meetings, specs, tasks, and decisions
- ✅ Internal prep notes with comprehensive background and stakeholder perspectives
- ✅ External-facing agendas with professional structure and time allocations
- ✅ Bidirectional linking between prep notes, agendas, and source materials
- ✅ Support for multiple meeting types (decision, status, brainstorming, planning, demos)
- ✅ Integration with Dataview for dynamic meeting tracking
- ✅ Post-meeting integration with outcomes and action items

## Installation

### Prerequisites

- Claude Code installed
- Obsidian vault with accessible filesystem path
- Basic knowledge of filesystem search and grep commands

### Setup

1. Copy this skill to your Claude Code skills directory:
   ```bash
   cp -r obsidian-meeting-prep ~/.claude/skills/
   ```

2. Configure your vault path:
   ```bash
   export OBSIDIAN_VAULT_PATH="/path/to/your/vault"
   ```

3. Organize your vault with standard directories (or customize):
   ```
   vault/
   ├── projects/
   ├── meetings/
   ├── specs/
   ├── tasks/
   └── decisions/
   ```

## Usage

### Basic Usage

Ask Claude to prepare for an upcoming meeting:

```
"Prepare materials for tomorrow's Project Alpha planning meeting"
"Create meeting prep for the client demo on Friday"
"I have a status update meeting - gather relevant context"
```

Claude will:
1. Search your vault for related content
2. Read relevant notes and extract key information
3. Create comprehensive prep note with background
4. Generate external-facing agenda
5. Link all documents appropriately

### Meeting Types and Focus

| Meeting Type | Focus | Prep Includes |
|--------------|-------|---------------|
| Decision Meeting | Options, trade-offs | Research alternatives, data, analysis |
| Status Update | Progress, blockers | Metrics, issues, timeline changes |
| Brainstorming | Ideas, possibilities | Examples, constraints, desired outcomes |
| Planning Session | Timeline, resources | Current state, dependencies, capacity |
| Customer Demo | Features, value | Demo script, talking points, Q&A prep |
| Problem-Solving | Issue resolution | Problem analysis, attempted solutions, data |

### Configuration Options

The skill searches multiple locations:

| Search Target | Purpose | Example Path |
|---------------|---------|--------------|
| Project notes | Current state | `projects/project-name/` |
| Previous meetings | Historical context | `meetings/project-name/` |
| Specifications | Requirements | `specs/feature-name.md` |
| Decision records | Past decisions | `decisions/` |
| Tasks and issues | Outstanding work | `tasks/` |

## Examples

### Example 1: Decision Meeting Prep

**Input:**
```
"Prepare for meeting to decide on database technology - meeting is tomorrow at 2pm"
```

**Output:**
- Internal prep note with:
  - Background on database requirements
  - Previous discussions and decisions
  - Options analysis (PostgreSQL vs MongoDB vs etc.)
  - Team perspectives and recommendations
- External agenda with:
  - Decision objectives
  - Discussion points with time allocations
  - Desired outcomes

### Example 2: Client Demo Preparation

**Input:**
```
"Create prep materials for Thursday's client demo of the new dashboard feature"
```

**Output:**
- Prep note gathering:
  - Feature specifications
  - Current implementation status
  - Demo talking points
  - Anticipated client questions
- Clean agenda for sharing with client

## Troubleshooting

### Common Issues

**Issue 1: Can't find relevant context**
- **Cause**: Search terms too specific or vault organization differs
- **Solution**: Broaden search, check vault structure, provide explicit paths

**Issue 2: Too much information gathered**
- **Cause**: Broad search terms match many files
- **Solution**: Specify project name, date ranges, or specific focus areas

**Issue 3: Prep note vs agenda confusion**
- **Cause**: Unclear distinction between internal and external
- **Solution**: Prep notes contain all context (internal), agendas are high-level (external)

## Dependencies

- Filesystem access for searching Markdown files
- Optional: grep for content search
- Optional: Obsidian Dataview plugin for meeting queries

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
- [Obsidian Research Synthesis](../obsidian-research-synthesis/) - Research workflows
- [Obsidian Spec to Implementation](../obsidian-spec-to-implementation/) - Implementation planning

## Additional Resources

- [Obsidian Documentation](https://help.obsidian.md/)
- [Meeting Facilitation Best Practices](https://www.lucidmeetings.com/)
- [Effective Agenda Writing](https://hbr.org/2015/03/how-to-design-an-agenda-for-an-effective-meeting)
