# Claude Skills Library

![License](https://img.shields.io/badge/license-MIT-green)
![Skills](https://img.shields.io/badge/skills-13-blue)
![Status](https://img.shields.io/badge/status-stable-green)

Personal collection of Claude Code skills for enhanced AI-assisted workflows across development, research, organization, and productivity tasks.

---

## 📚 Skills Catalog

### Review & Analysis

| Skill | Version | Description |
|-------|---------|-------------|
| [**Paper Reviewer**](skills/review/paper-reviewer/) | v2.0.0 | Multi-venue peer review system for NeurIPS and IEEE publications |

### Organization & Management

| Skill | Version | Description |
|-------|---------|-------------|
| [**File Organizer**](skills/organization/file-organizer/) | v1.0.0 | Intelligent file and folder organization with duplicate detection |

### Obsidian Integration (4 skills)

| Skill | Version | Description |
|-------|---------|-------------|
| [**Knowledge Capture**](skills/obsidian/obsidian-knowledge-capture/) | v1.0.0 | Transform conversations into structured Obsidian notes |
| [**Meeting Prep**](skills/obsidian/obsidian-meeting-prep/) | v1.0.0 | Gather context and prepare comprehensive meeting materials |
| [**Research Synthesis**](skills/obsidian/obsidian-research-synthesis/) | v1.0.0 | Search vault and synthesize research into comprehensive reports |
| [**Spec to Implementation**](skills/obsidian/obsidian-spec-to-implementation/) | v1.0.0 | Convert specifications into actionable implementation plans |

### Google Workspace (4 skills)

| Skill | Version | Description |
|-------|---------|-------------|
| [**Calendar Sync**](skills/google/google-calendar-sync/) | v1.0.0 | Automated event scheduling and calendar management |
| [**Docs Collaboration**](skills/google/google-docs-collaboration/) | v1.0.0 | Create and manage Google Docs, Sheets, and Slides |
| [**Drive Management**](skills/google/google-drive-management/) | v1.0.0 | Automated file operations and Drive organization |
| [**Gmail Integration**](skills/google/google-gmail-integration/) | v1.0.0 | Email automation, templates, and inbox management |

### Utilities (3 skills)

| Skill | Version | Description |
|-------|---------|-------------|
| [**Claude Code Service**](skills/utility/claude-code-service/) | v1.0.0 | Web service integration with Gemini and OpenAI APIs |
| [**Smart Screenshot**](skills/utility/smart-screenshot/) | v1.0.0 | Screenshot capture with OCR and context extraction |
| [**STT Transcription**](skills/utility/stt-transcription/) | v1.0.0 | Speech-to-text transcription supporting 99+ languages |

---

## 🔗 Related Projects

These comprehensive pipelines have been moved to separate repositories:

- [**Thesis Pipeline**](https://github.com/astoreyai/thesis-pipeline) - Complete PhD dissertation workflow system with 21 embedded skills
- [**Project Manager Pipeline**](https://github.com/astoreyai/project-manager-pipeline) - PMBOK-aligned project management system
- [**Paper Creation Pipeline**](https://github.com/astoreyai/paper-creation-pipeline) - Research paper reproducibility framework

---

## 🚀 Quick Start

### Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/astoreyai/claude-skills.git
   cd claude-skills
   ```

2. **Browse available skills:**
   ```bash
   ls skills/
   ```

3. **Copy skills to Claude Code:**
   ```bash
   # Copy all skills
   cp -r skills/ ~/.claude/skills/

   # Or copy specific category
   cp -r skills/obsidian/ ~/.claude/skills/
   ```

### Using a Skill

1. Navigate to a relevant directory for your task
2. Invoke Claude Code
3. Reference the skill by name or description
4. Follow the skill's workflow and prompts

**Example:**
```bash
cd ~/Documents
# Invoke Claude Code
# "Help me organize my files" → triggers File Organizer skill
```

---

## 📖 Documentation

### For Users

- [**Skill Template Guide**](docs/SKILL_TEMPLATE.md) - How to create new skills
- [**Version Management**](docs/VERSION_GUIDE.md) - Semantic versioning guidelines
- [**Contributing**](CONTRIBUTING.md) - Personal workflow for adding skills

### Templates

- [README Template](docs/README_TEMPLATE.md) - Standard documentation format
- [CHANGELOG Template](docs/CHANGELOG_TEMPLATE.md) - Version history format

---

## 🎯 Use Cases

### Academic Research
- **Paper Reviewer**: Conduct systematic peer reviews for conferences/journals
- **Research Synthesis**: Aggregate research notes into comprehensive reports
- **Thesis Pipeline**: Complete dissertation workflow (separate repo)

### Development & Projects
- **Spec to Implementation**: Convert requirements into implementation plans
- **Project Manager Pipeline**: Full project management lifecycle (separate repo)
- **File Organizer**: Maintain clean project directory structures

### Productivity & Automation
- **Knowledge Capture**: Transform discussions into structured documentation
- **Meeting Prep**: Automatic context gathering and agenda creation
- **Google Workspace**: Automated document creation and email management

### Content & Media
- **Smart Screenshot**: Extract text and context from images
- **STT Transcription**: Convert audio/video to text (99+ languages)
- **Docs Collaboration**: Automated report and presentation generation

---

## 🏗️ Repository Structure

```
claude_skills/
├── LICENSE                    # MIT License
├── README.md                  # This file
├── .gitignore                # Git ignore rules
├── CONTRIBUTING.md            # Contribution guidelines
├── skills/                    # All skills organized by category
│   ├── obsidian/             # Obsidian integration skills (4)
│   ├── google/               # Google Workspace skills (4)
│   ├── utility/              # Utility skills (3)
│   ├── review/               # Review and analysis skills (1)
│   └── organization/         # Organization skills (1)
└── docs/                      # Documentation and templates
    ├── README_TEMPLATE.md
    ├── CHANGELOG_TEMPLATE.md
    ├── SKILL_TEMPLATE.md
    └── VERSION_GUIDE.md
```

---

## 🔄 Version History

This is a personal skill library maintained at version 1.0.0. Individual skills have their own version numbers - see each skill's CHANGELOG.md for details.

### Repository Releases

- **v1.0.0** (2025-11-05) - Initial organized release with 13 skills

---

## 📝 Creating New Skills

Want to add a new skill? Follow these steps:

1. Review the [Skill Template Guide](docs/SKILL_TEMPLATE.md)
2. Use provided templates for README, CHANGELOG, and SKILL.md
3. Place in appropriate category directory
4. Follow versioning guidelines
5. Update this main README with new skill entry

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed workflow.

---

## 🔍 Skill Selection Guide

**Not sure which skill to use?** Here's a quick guide:

| If you want to... | Use this skill |
|-------------------|----------------|
| Review an academic paper | Paper Reviewer |
| Organize messy files/folders | File Organizer |
| Save conversation insights to Obsidian | Knowledge Capture |
| Prepare for an upcoming meeting | Meeting Prep |
| Synthesize research notes | Research Synthesis |
| Turn specs into implementation steps | Spec to Implementation |
| Schedule events automatically | Calendar Sync |
| Create Google Docs/Sheets/Slides | Docs Collaboration |
| Manage Drive files | Drive Management |
| Automate email tasks | Gmail Integration |
| Integrate with other AI services | Claude Code Service |
| Extract text from images | Smart Screenshot |
| Transcribe audio/video | STT Transcription |

---

## 🛠️ Requirements

### Core Requirements
- **Claude Code** - Latest version
- **Operating System** - Linux, macOS, or Windows with WSL

### Skill-Specific Requirements
Some skills have additional dependencies:

- **Google Workspace Skills**: Google API credentials
- **Obsidian Skills**: Obsidian vault configured
- **STT Transcription**: FFmpeg for audio processing
- **Claude Code Service**: API keys for Gemini/OpenAI (optional)

See individual skill READMEs for detailed requirements.

---

## 🐛 Troubleshooting

### Common Issues

**Skill not activating:**
- Verify skill is copied to `~/.claude/skills/`
- Check SKILL.md has correct front matter
- Ensure Claude Code is latest version

**Dependencies missing:**
- Review skill's README.md for required dependencies
- Install language-specific requirements (requirements.txt, package.json)
- Configure API keys if needed (.env.template provided)

**Unexpected behavior:**
- Check skill version compatibility
- Review CHANGELOG for recent changes
- Ensure environment variables are set correctly

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

You are free to:
- ✅ Use skills for personal or commercial projects
- ✅ Modify and adapt skills to your needs
- ✅ Share and distribute skills
- ✅ Create derivative works

---

## 👤 Author

**Aaron Storey** ([@astoreyai](https://github.com/astoreyai))

Personal skill library for Claude Code. Feel free to fork and adapt for your own use!

---

## 🌟 Acknowledgments

- Built for [Claude Code](https://docs.anthropic.com/claude/docs/claude-code) by Anthropic
- Inspired by the Claude Code skills ecosystem
- Semantic versioning following [SemVer](https://semver.org/)
- Changelog format based on [Keep a Changelog](https://keepachangelog.com/)

---

## 📬 Feedback & Contributions

This is a personal library, but feedback and suggestions are welcome:

- **Issues**: Feel free to open issues for bugs or suggestions
- **Forks**: Fork and adapt for your own needs
- **Pull Requests**: Not actively accepting PRs, but happy to review ideas

---

**Last Updated**: 2025-11-05 | **Total Skills**: 13 | **Repository Version**: 1.0.0
