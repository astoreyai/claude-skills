# Skill Template Guide

This guide provides a template for creating new Claude Code skills that follow the standardization conventions of this repository.

## Skill Directory Structure

```
skill-name/
├── SKILL.md              # Main skill definition (Claude Code reads this)
├── README.md             # Human-readable documentation
├── CHANGELOG.md          # Version history
├── VERSION               # Version number file (optional)
├── LICENSE               # Copy of MIT license
├── requirements.txt      # Python dependencies (if applicable)
├── package.json          # Node.js dependencies (if applicable)
├── .env.template         # Environment variable template (if needed)
├── components/           # Sub-skills or modular components (optional)
│   ├── component1.md
│   └── component2.md
├── templates/            # Output templates (optional)
│   ├── template1.md
│   └── template2.md
├── tools/                # Utility scripts (optional)
│   └── helper.py
└── examples/             # Usage examples (optional)
    └── example1.md
```

## SKILL.md Format

The SKILL.md file is what Claude Code reads to understand your skill. It should be written as instructions for the AI.

```markdown
# [Skill Name] Skill

You are a specialized assistant for [skill purpose].

## Purpose

[Clear description of what this skill does and when to use it]

## Core Capabilities

1. **[Capability 1]**: [Description]
2. **[Capability 2]**: [Description]
3. **[Capability 3]**: [Description]

## Workflow

When this skill is invoked:

1. **[Step 1 Name]**
   - [Action to take]
   - [What to look for]
   - [Output to produce]

2. **[Step 2 Name]**
   - [Action to take]
   - [What to analyze]
   - [Decision points]

3. **[Step 3 Name]**
   - [Final actions]
   - [Deliverables]

## Tools and Resources

- Use [specific tool] for [purpose]
- Access [resource] when [condition]
- Reference [template] for [output type]

## Output Format

Provide results in the following format:

\`\`\`
[Expected output structure]
\`\`\`

## Quality Checklist

Before completing, verify:
- [ ] [Quality criterion 1]
- [ ] [Quality criterion 2]
- [ ] [Quality criterion 3]

## Examples

### Example 1: [Use Case]
**Input:**
[Example input]

**Process:**
[Steps taken]

**Output:**
[Expected result]

## Notes

- [Important consideration 1]
- [Limitation or caveat]
- [Best practice]
```

## README.md Format

Follow the template in `docs/README_TEMPLATE.md`. Key sections:

1. **Title with badges** (version, status, license)
2. **Description** (what, why, who)
3. **Features** (bulleted list)
4. **Installation** (setup steps)
5. **Usage** (basic and advanced examples)
6. **Configuration** (options table)
7. **Examples** (real-world use cases)
8. **Troubleshooting** (common issues)
9. **Dependencies** (external requirements)
10. **Links** (changelog, license, related skills)

## CHANGELOG.md Format

Follow the template in `docs/CHANGELOG_TEMPLATE.md`. Use semantic versioning:

- **MAJOR.MINOR.PATCH** (e.g., 1.0.0)
- Start at 1.0.0 for initial stable release
- Use 0.x.x for pre-release development

## Naming Conventions

### Skill Names
- Use kebab-case: `paper-reviewer`, `file-organizer`
- Be descriptive but concise
- Avoid version numbers in names

### File Names
- Markdown: Use kebab-case with `.md` extension
- Scripts: Use snake_case for Python, camelCase for JavaScript
- Templates: Descriptive names with context (e.g., `email-template.md`)

### Directory Names
- Use kebab-case
- Organize by function: `components/`, `templates/`, `tools/`, `examples/`

## Versioning Guidelines

### When to Bump Versions

**MAJOR (X.0.0)** - Breaking changes:
- Incompatible workflow changes
- Removed functionality
- Changed core behavior that breaks existing usage

**MINOR (0.X.0)** - New features:
- Added new capabilities
- New components or templates
- Enhanced existing features (backwards compatible)

**PATCH (0.0.X)** - Bug fixes:
- Fixed errors or bugs
- Updated documentation
- Minor improvements

### Version File

Optionally include a `VERSION` file:
```
1.0.0
```

Or specify in README.md badge:
```markdown
![Version](https://img.shields.io/badge/version-1.0.0-blue)
```

## Dependencies

### Python Skills
Create `requirements.txt`:
```
requests>=2.28.0
python-dotenv>=0.21.0
anthropic>=0.3.0
```

### Node.js Skills
Create `package.json`:
```json
{
  "name": "skill-name",
  "version": "1.0.0",
  "description": "Brief description",
  "dependencies": {
    "anthropic": "^0.6.0"
  }
}
```

### Environment Variables
Create `.env.template`:
```
# API Keys
SKILL_API_KEY=your_api_key_here
SKILL_ENDPOINT=https://api.example.com

# Configuration
SKILL_TIMEOUT=30
SKILL_DEBUG=false
```

## Documentation Standards

### Writing Style
- Be concise and clear
- Use active voice
- Provide concrete examples
- Include error scenarios

### Code Examples
- Use triple backticks with language specification
- Show both input and output
- Explain non-obvious steps

### Markdown Formatting
- Use headers hierarchically (h1 → h2 → h3)
- Use tables for structured data
- Use lists for sequential items
- Use code blocks for commands/code

## Testing Your Skill

Before considering a skill complete:

1. **Functionality**: Test all core capabilities
2. **Documentation**: Verify all examples work
3. **Dependencies**: Check all requirements install correctly
4. **Error Handling**: Test with invalid inputs
5. **Compatibility**: Verify works with Claude Code

## Skill Categories

Organize skills into logical categories:

- **obsidian/** - Obsidian integration skills
- **google/** - Google Workspace skills
- **utility/** - General utility skills
- **review/** - Review and analysis skills
- **organization/** - Organization and management skills
- **[custom]/** - Create category as needed

## Quality Checklist

Before publishing a skill, verify:

- [ ] SKILL.md provides clear instructions for Claude
- [ ] README.md follows template with all sections
- [ ] CHANGELOG.md tracks version history
- [ ] LICENSE file present (copy from root)
- [ ] Version badge matches current version
- [ ] All examples tested and working
- [ ] Dependencies documented in requirements.txt/package.json
- [ ] .env.template provided if environment variables needed
- [ ] No secrets or API keys committed
- [ ] Cross-links to related skills added
- [ ] Follows naming conventions

## Additional Resources

- [Keep a Changelog](https://keepachangelog.com/)
- [Semantic Versioning](https://semver.org/)
- [Markdown Guide](https://www.markdownguide.org/)
- [Claude Code Documentation](https://docs.anthropic.com/claude/docs)
