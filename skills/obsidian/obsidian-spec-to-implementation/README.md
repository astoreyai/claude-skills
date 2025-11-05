# Obsidian Spec to Implementation

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Status](https://img.shields.io/badge/status-stable-green)
![License](https://img.shields.io/badge/license-MIT-green)

## Description

Transform product or technical specifications into concrete implementation plans and task notes within Obsidian.

This skill locates spec notes in your vault, extracts requirements, breaks them down into structured implementation plans with linked task notes, and manages the complete development workflow from requirements to completion using markdown files and frontmatter.

## Features

- ✅ Automated spec discovery and parsing from vault
- ✅ Requirement extraction (functional, non-functional, acceptance criteria)
- ✅ Structured implementation plan generation with phases and milestones
- ✅ Bidirectional linking between specs, plans, and task notes
- ✅ Progress tracking with status updates and completion percentages
- ✅ Multiple task breakdown strategies (by component, feature slice, priority)
- ✅ Dataview integration for dynamic progress dashboards
- ✅ Graph view visualization of dependencies

## Installation

### Prerequisites

- Claude Code installed
- Obsidian vault with specifications or requirements documents
- Basic understanding of project management workflows

### Setup

1. Copy this skill to your Claude Code skills directory:
   ```bash
   cp -r obsidian-spec-to-implementation ~/.claude/skills/
   ```

2. Configure your vault path:
   ```bash
   export OBSIDIAN_VAULT_PATH="/path/to/your/vault"
   ```

3. Organize vault with recommended structure:
   ```
   vault/
   ├── specs/
   ├── plans/
   ├── tasks/
   └── projects/
   ```

## Usage

### Basic Usage

Ask Claude to create implementation plan from a spec:

```
"Create implementation plan for the user authentication spec"
"Break down the dashboard feature spec into tasks"
"Generate tasks from the API versioning specification"
```

Claude will:
1. Locate the specification in your vault
2. Parse requirements and acceptance criteria
3. Create structured implementation plan
4. Generate individual task notes
5. Link all documents bidirectionally
6. Set up progress tracking

### Task Breakdown Strategies

| Strategy | Organization | Best For |
|----------|--------------|----------|
| By Component | Database → API → Frontend | Clear architecture layers |
| By Feature Slice | Vertical end-to-end features | User-centric development |
| By Priority | P0 → P1 → P2 | Critical path first |

### Configuration Options

| Option | Description | Default |
|--------|-------------|---------|
| task_size | Estimated completion time | 1-2 days |
| vault_structure | Folder organization | Separate folders |
| link_style | Bidirectional or forward | Bidirectional |
| progress_format | Tracking method | Checkboxes + percentages |

## Examples

### Example 1: API Feature Implementation

**Input:**
```
"Create implementation plan for the RESTful API authentication spec"
```

**Output:**
- Implementation plan at `plans/api-auth-implementation.md`
- Task notes for each component (schema, endpoints, middleware, tests)
- All linked to original spec
- Progress tracking initialized

### Example 2: UI Component Implementation

**Input:**
```
"Break down the dashboard component spec into tasks"
```

**Output:**
- Structured plan with frontend phases
- Tasks for design, implementation, testing
- Dependencies mapped
- Milestone tracking setup

## Troubleshooting

### Common Issues

**Issue 1: Can't find spec**
- **Cause**: Spec not in expected location or naming doesn't match
- **Solution**: Search by tag `#spec`, check folder structure, or provide explicit path

**Issue 2: Spec unclear or ambiguous**
- **Cause**: Incomplete specification document
- **Solution**: Note ambiguities in plan, create clarification tasks

**Issue 3: Tasks too large**
- **Cause**: Insufficient breakdown granularity
- **Solution**: Further decompose complex tasks into subtasks

## Dependencies

- Filesystem access for reading and writing Markdown files
- Optional: Obsidian Dataview plugin for progress dashboards
- Optional: Obsidian Tasks plugin for enhanced task management

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
- [Obsidian Research Synthesis](../obsidian-research-synthesis/) - Research workflows

## Additional Resources

- [Obsidian Documentation](https://help.obsidian.md/)
- [Agile User Stories](https://www.atlassian.com/agile/project-management/user-stories)
- [Requirements Engineering](https://www.reqview.com/)
