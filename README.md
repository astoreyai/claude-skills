# Claude Skills Library

![License](https://img.shields.io/badge/license-MIT-green)
![Skills](https://img.shields.io/badge/skills-32-blue)
![Version](https://img.shields.io/badge/version-1.4.0-orange)
![Status](https://img.shields.io/badge/status-stable-green)

Personal collection of Claude Code skills for enhanced AI-assisted workflows across trading, research, development, organization, and productivity tasks.

---

## Skills Catalog

### Trading & Finance (3 skills)

| Skill | Version | Description |
|-------|---------|-------------|
| [**Trading Analysis**](trading-analysis/) | v1.0.0 | CSV statement parsing, performance metrics, risk analysis, LaTeX/PDF reports |
| [**Portfolio Analysis Agent**](portfolio-analysis-agent/) | v1.0.0 | Comprehensive portfolio performance analysis and projections |
| [**Forecasting Agent**](forecasting-agent/) | v1.0.0 | Financial forecasting and Monte Carlo simulations |

### Kymera Integration (6 skills)

| Skill | Version | Description |
|-------|---------|-------------|
| [**Portfolio Checker**](kymera-portfolio-checker/) | v1.0.0 | Validates portfolio 90% win rate claims, identifies risk violations |
| [**MR Optimizer**](kymera-mr-optimizer/) | v1.0.0 | Mean reversion strategy parameter optimization |
| [**Strategy Integrator**](kymera-integrator/) | v1.0.0 | Bidirectional portfolio/MR data flow management |
| [**Risk Monitor**](kymera-risk-monitor/) | v1.0.0 | Real-time position monitoring, -5% stop enforcement |
| [**Tax Optimizer**](kymera-tax-optimizer/) | v1.0.0 | Quarterly tax calculation, tax-loss harvesting |
| [**Brand Skill**](kymera-brand-skill/) | v1.0.0 | Kymera branding guidelines and assets |

### Session Management (4 skills)

| Skill | Version | Description |
|-------|---------|-------------|
| [**Memory Keeper**](skills/memory-keeper/) | v1.0.0 | Automated CLAUDE.md context management |
| [**Obsidian Memory Keeper**](skills/obsidian-memory-keeper/) | v1.0.0 | Daily notes and session tracking for Obsidian |
| [**Todo Keeper**](skills/todo-keeper/) | v1.0.0 | Task persistence with SessionStart/End hooks |
| [**Vault Keeper**](skills/vault-keeper/) | v1.0.0 | Obsidian vault structure validation and cleanup |

### Content & Media Processing (6 skills)

| Skill | Version | Description |
|-------|---------|-------------|
| [**YouTube Transcriber**](youtube-transcriber/) | v1.0.0 | YouTube video transcription extraction |
| [**YouTube Transcript Extractor**](youtube-transcript-extractor/) | v1.0.0 | Complete 4-skill pipeline: Extract facts, Format notes, Integrate Obsidian, Archive |
| [**Transcript Archiver**](transcript-archiver/) | v1.0.0 | Archive and organize transcripts |
| [**Transcript to Logseq**](transcript-to-logseq/) | v1.0.0 | Convert transcripts to Logseq format |
| [**Transcript to Obsidian**](transcript-to-obsidian/) | v1.0.0 | Convert transcripts to Obsidian notes |
| [**STT Transcription**](skills/utility/stt-transcription/) | v1.0.0 | Speech-to-text supporting 99+ languages |

### Review & Analysis (3 skills)

| Skill | Version | Description |
|-------|---------|-------------|
| [**Paper Reviewer**](skills/review/paper-reviewer/) | v2.0.0 | Multi-venue peer review for NeurIPS/IEEE publications |
| [**LaTeX Check**](skills/review/latex-check/) | v1.0.0 | LaTeX document validation and error checking |
| [**Text Metrics**](skills/utility/text-metrics/) | v1.0.0 | Text analysis and readability metrics |

### Organization & Management (1 skill)

| Skill | Version | Description |
|-------|---------|-------------|
| [**File Organizer**](skills/organization/file-organizer/) | v1.0.0 | Intelligent file/folder organization with duplicate detection |

### Obsidian Integration (4 skills)

| Skill | Version | Description |
|-------|---------|-------------|
| [**Knowledge Capture**](skills/obsidian/obsidian-knowledge-capture/) | v1.0.0 | Transform conversations into structured Obsidian notes |
| [**Meeting Prep**](skills/obsidian/obsidian-meeting-prep/) | v1.0.0 | Gather context and prepare meeting materials |
| [**Research Synthesis**](skills/obsidian/obsidian-research-synthesis/) | v1.0.0 | Search vault and synthesize research reports |
| [**Spec to Implementation**](skills/obsidian/obsidian-spec-to-implementation/) | v1.0.0 | Convert specifications into implementation plans |

### Google Workspace (4 skills)

| Skill | Version | Description |
|-------|---------|-------------|
| [**Calendar Sync**](skills/google/google-calendar-sync/) | v1.0.0 | Automated event scheduling and calendar management |
| [**Docs Collaboration**](skills/google/google-docs-collaboration/) | v1.0.0 | Create and manage Google Docs, Sheets, Slides |
| [**Drive Management**](skills/google/google-drive-management/) | v1.0.0 | Automated file operations and Drive organization |
| [**Gmail Integration**](skills/google/google-gmail-integration/) | v1.0.0 | Email automation, templates, inbox management |

### System Tools (2 skills)

| Skill | Version | Description |
|-------|---------|-------------|
| [**System Health Check**](system-health-check/) | v1.0.0 | System diagnostics and health monitoring |
| [**Smart Screenshot**](skills/utility/smart-screenshot/) | v1.0.0 | Screenshot capture with OCR and context extraction |

---

## Related Projects

These comprehensive pipelines have been moved to separate repositories:

- [**Research Assistant**](https://github.com/astoreyai/ai_scientist) - 22 research skills, 10 agents for academic workflows
- [**Thesis Pipeline**](https://github.com/astoreyai/thesis-pipeline) - Complete PhD dissertation workflow system
- [**Project Manager Pipeline**](https://github.com/astoreyai/project-manager-pipeline) - PMBOK-aligned project management
- [**Paper Creation Pipeline**](https://github.com/astoreyai/paper-creation-pipeline) - Research paper reproducibility framework

---

## Quick Start

### Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/astoreyai/claude-skills.git
   cd claude-skills
   ```

2. **Browse available skills:**
   ```bash
   ls skills/
   ls *.md  # Root-level skill directories
   ```

3. **Copy skills to Claude Code:**
   ```bash
   # Copy all skills
   cp -r skills/ ~/.claude/skills/

   # Copy root-level skills
   cp -r trading-analysis/ ~/.claude/skills/
   cp -r kymera-*/ ~/.claude/skills/

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
cd ~/portfolio
# Invoke Claude Code
# "Analyze my trading performance" -> triggers Trading Analysis skill
```

---

## Repository Structure

```
claude-skills/
├── LICENSE                    # MIT License
├── README.md                  # This file
├── CHANGELOG.md              # Version history
├── .claude-plugin/           # Plugin manifest
│   └── plugin.json           # v1.4.0
├── commands/                  # Slash commands (9)
├── skills/                    # Category-organized skills
│   ├── memory-keeper/        # Session management
│   ├── obsidian-memory-keeper/
│   ├── todo-keeper/
│   ├── vault-keeper/
│   ├── obsidian/             # Obsidian integration (4)
│   ├── google/               # Google Workspace (4)
│   ├── utility/              # Utilities (3)
│   ├── review/               # Review skills (2)
│   └── organization/         # Organization (1)
├── trading-analysis/          # Trading analysis
├── portfolio-analysis-agent/  # Portfolio analysis
├── forecasting-agent/         # Financial forecasting
├── kymera-*/                  # Kymera integration (6)
├── youtube-*/                 # YouTube processing (2)
├── transcript-*/              # Transcript tools (3)
├── system-health-check/       # System diagnostics
└── docs/                      # Documentation
```

---

## Skill Selection Guide

| If you want to... | Use this skill |
|-------------------|----------------|
| Analyze trading performance | Trading Analysis |
| Monitor portfolio risk | Risk Monitor |
| Optimize mean reversion | MR Optimizer |
| Calculate taxes | Tax Optimizer |
| Transcribe YouTube videos | YouTube Transcriber |
| Review academic papers | Paper Reviewer |
| Organize messy files | File Organizer |
| Save insights to Obsidian | Knowledge Capture |
| Prepare for meetings | Meeting Prep |
| Manage Google Drive | Drive Management |
| Check system health | System Health Check |
| Track session todos | Todo Keeper |
| Update CLAUDE.md automatically | Memory Keeper |

---

## Version History

### Repository Releases

- **v1.4.0** (2025-11-25) - Added 19 skills: Kymera integration, trading analysis, session management
- **v1.0.0** (2025-11-05) - Initial organized release with 13 skills

---

## Requirements

### Core Requirements
- **Claude Code** - Latest version
- **Operating System** - Linux, macOS, or Windows with WSL

### Skill-Specific Requirements
- **Google Workspace Skills**: Google API credentials, OAuth setup
- **Obsidian Skills**: Obsidian vault configured
- **Trading Skills**: CSV trade statements, Interactive Brokers format
- **STT Transcription**: FFmpeg for audio processing

See individual skill READMEs for detailed requirements.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Author

**Aaron Storey** ([@astoreyai](https://github.com/astoreyai))

Personal skill library for Claude Code. Feel free to fork and adapt for your own use!

---

**Last Updated**: 2025-11-25 | **Total Skills**: 32 | **Repository Version**: 1.4.0
