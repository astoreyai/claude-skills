# Contributing to Claude Skills Library

This is a personal skill library for Claude Code. This document outlines my workflow for adding new skills and maintaining the library.

---

## Adding a New Skill

### 1. Determine Category

Place the skill in the appropriate category:

- `skills/obsidian/` - Obsidian integration skills
- `skills/google/` - Google Workspace automation
- `skills/utility/` - General utility skills
- `skills/review/` - Review and analysis skills
- `skills/organization/` - Organization and management skills

Create a new category if none of the existing ones fit.

### 2. Create Skill Directory

```bash
mkdir -p skills/[category]/[skill-name]
cd skills/[category]/[skill-name]
```

**Naming conventions:**
- Use kebab-case (lowercase with hyphens)
- Be descriptive but concise
- Examples: `paper-reviewer`, `file-organizer`, `stt-transcription`

### 3. Create Core Files

#### SKILL.md (Required)

This is what Claude Code reads. Use the template:

```bash
cp ../../../docs/SKILL_TEMPLATE.md SKILL.md
# Edit SKILL.md with skill-specific content
```

Include:
- Clear description of what the skill does
- When to use it
- Step-by-step workflow
- Expected inputs and outputs
- Examples

#### README.md (Required)

Human-readable documentation:

```bash
cp ../../../docs/README_TEMPLATE.md README.md
# Customize README for this skill
```

Include:
- Version badge (start at 1.0.0)
- Description and features
- Installation and setup
- Usage examples
- Configuration options
- Troubleshooting

#### CHANGELOG.md (Required)

Track version history:

```bash
cp ../../../docs/CHANGELOG_TEMPLATE.md CHANGELOG.md
# Add initial release entry
```

Start with v1.0.0 and date of creation.

#### LICENSE (Required)

Copy the MIT license:

```bash
cp ../../../LICENSE LICENSE
```

### 4. Add Supporting Directories (Optional)

```bash
mkdir -p components/     # Sub-skills or modular components
mkdir -p templates/      # Output templates
mkdir -p examples/       # Usage examples
mkdir -p reference/      # Reference materials
mkdir -p scripts/        # Helper scripts
```

### 5. Add Dependencies (If Needed)

**Python dependencies:**
```bash
# Create requirements.txt
echo "requests>=2.28.0" > requirements.txt
echo "python-dotenv>=0.21.0" >> requirements.txt
```

**Node.js dependencies:**
```bash
# Create package.json
npm init -y
npm install anthropic --save
```

**Environment variables:**
```bash
# Create .env.template
cat > .env.template << 'EOF'
SKILL_API_KEY=your_api_key_here
SKILL_CONFIG_OPTION=default_value
EOF
```

### 6. Test the Skill

1. Copy skill to Claude Code directory:
   ```bash
   cp -r . ~/.claude/skills/[skill-name]
   ```

2. Test with Claude Code:
   - Invoke Claude Code in a test directory
   - Try to trigger the skill
   - Verify it works as expected
   - Test edge cases

3. Fix any issues and update documentation

### 7. Update Main README

Add your skill to the main repository README:

```bash
vim ../../README.md
```

Add entry to appropriate category table:
```markdown
| [**Skill Name**](skills/category/skill-name/) | v1.0.0 | Brief description |
```

### 8. Commit Changes

```bash
git add .
git commit -m "Add [skill-name] skill v1.0.0

Description of what the skill does and key features.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

## Updating an Existing Skill

### 1. Determine Version Bump

Follow [Semantic Versioning](https://semver.org/):

- **MAJOR** (X.0.0) - Breaking changes
- **MINOR** (0.X.0) - New features (backwards compatible)
- **PATCH** (0.0.X) - Bug fixes

See [docs/VERSION_GUIDE.md](docs/VERSION_GUIDE.md) for detailed guidance.

### 2. Update CHANGELOG.md

Add new version entry:

```markdown
## [1.1.0] - 2025-11-06

### Added
- New feature X
- Support for Y

### Fixed
- Bug in Z

### Changed
- Improved performance of A
```

### 3. Update Version Badge

In README.md:
```markdown
![Version](https://img.shields.io/badge/version-1.1.0-blue)
```

### 4. Update Documentation

- Update README.md if usage changes
- Add new examples if applicable
- Update SKILL.md if workflow changes

### 5. Test Changes

```bash
cp -r . ~/.claude/skills/[skill-name]
# Test thoroughly
```

### 6. Commit with Version Tag

```bash
git add .
git commit -m "Update [skill-name] to v1.1.0

Changes:
- Added feature X
- Fixed bug Y
- Improved Z

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"

git tag -a [skill-name]-v1.1.0 -m "Release v1.1.0"
```

---

## Organizing Workflow

### Directory Structure Standards

```
skills/
└── [category]/
    └── [skill-name]/
        ├── SKILL.md           # Claude Code reads this
        ├── README.md          # Human documentation
        ├── CHANGELOG.md       # Version history
        ├── LICENSE            # MIT License
        ├── requirements.txt   # Python deps (if needed)
        ├── package.json       # Node deps (if needed)
        ├── .env.template      # Env vars (if needed)
        ├── components/        # Sub-skills (optional)
        ├── templates/         # Output templates (optional)
        ├── examples/          # Usage examples (optional)
        ├── reference/         # Reference docs (optional)
        └── scripts/           # Helper scripts (optional)
```

### File Naming Conventions

- **Markdown files**: Use UPPERCASE for core files (README.md, CHANGELOG.md), kebab-case for others
- **Python files**: Use snake_case (.py files)
- **JavaScript files**: Use camelCase (.js files)
- **Directories**: Use kebab-case for skill names, lowercase for standard directories

### Documentation Standards

1. **Be Clear and Concise**
   - Use active voice
   - Provide concrete examples
   - Explain the "why" not just the "what"

2. **Use Consistent Formatting**
   - Follow the provided templates
   - Use code blocks with language tags
   - Include table of contents for long docs

3. **Keep Examples Realistic**
   - Show actual use cases
   - Include expected outputs
   - Demonstrate edge cases

4. **Maintain Version History**
   - Update CHANGELOG with every change
   - Follow semantic versioning strictly
   - Date all entries

---

## Quality Checklist

Before considering a skill complete:

- [ ] SKILL.md provides clear instructions for Claude
- [ ] README.md has complete documentation
- [ ] CHANGELOG.md tracks version history
- [ ] LICENSE file present
- [ ] Version badge in README matches actual version
- [ ] All examples tested and working
- [ ] Dependencies documented (requirements.txt, package.json)
- [ ] Environment variables in .env.template (if needed)
- [ ] No secrets or API keys committed
- [ ] Cross-links to related skills added
- [ ] Main repository README updated
- [ ] Git commit with appropriate message
- [ ] Skill tested in Claude Code environment

---

## Git Workflow

### Branch Strategy

**For personal library**: Work directly on `main` branch

For experimental features:
```bash
git checkout -b feature/new-skill-name
# Develop and test
git checkout main
git merge feature/new-skill-name
```

### Commit Message Format

```
<type>: <short description>

<detailed description of changes>

<optional footer with tags>
```

**Types:**
- `feat:` - New skill or feature
- `fix:` - Bug fix
- `docs:` - Documentation only
- `refactor:` - Code refactoring
- `test:` - Adding tests
- `chore:` - Maintenance tasks

**Examples:**
```bash
git commit -m "feat: Add STT transcription skill

Supports 99+ languages with automatic language detection.
Includes examples for audio and video transcription.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

### Tagging Releases

Tag individual skill releases:
```bash
git tag -a paper-reviewer-v2.0.0 -m "Paper Reviewer v2.0.0 - Multi-venue support"
git push origin paper-reviewer-v2.0.0
```

Tag repository releases:
```bash
git tag -a v1.0.0 -m "Initial organized release with 13 skills"
git push origin v1.0.0
```

---

## Maintenance Tasks

### Regular Maintenance

**Monthly:**
- Review and update outdated skills
- Check for deprecated dependencies
- Update documentation as needed
- Clean up old/unused skills

**As Needed:**
- Respond to issues (if accepting them)
- Update for new Claude Code features
- Refactor for better organization
- Add new skills as requirements arise

### Deprecation Process

When removing a skill:

1. Mark as deprecated in README (1 month notice)
2. Add deprecation notice to SKILL.md
3. Suggest alternative skills
4. After notice period, move to ARCHIVE/
5. Update main README

---

## Resources

### Templates
- [Skill Template](docs/SKILL_TEMPLATE.md)
- [README Template](docs/README_TEMPLATE.md)
- [CHANGELOG Template](docs/CHANGELOG_TEMPLATE.md)

### Guides
- [Version Management](docs/VERSION_GUIDE.md)
- [Semantic Versioning](https://semver.org/)
- [Keep a Changelog](https://keepachangelog.com/)

### Claude Code Documentation
- [Claude Code Docs](https://docs.anthropic.com/claude/docs/claude-code)
- [Skills Documentation](https://docs.anthropic.com/claude/docs/claude-code/skills)

---

## Questions or Issues?

This is a personal library, but if you have questions:

1. Check existing skill documentation
2. Review the templates and guides
3. Refer to Claude Code official documentation
4. Open an issue on GitHub (if accepting issues)

---

**Remember**: This is a personal tool. Prioritize what works for your workflow over strict adherence to conventions. These guidelines are here to maintain consistency and make future maintenance easier.

---

Last Updated: 2025-11-05
