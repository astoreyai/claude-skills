# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-20

### Added
- Memory Keeper skill for automated CLAUDE.md management
- Auto-run SessionEnd hook for timestamp updates
- `/update-memory` slash command for comprehensive updates
- Complete documentation suite (README, USAGE, AUTO_RUN, SKILL)
- Git integration for project tracking
- Conversation history analysis
- Session notes management
- Development pattern observation
- Auto-update script with logging
- Plugin packaging for distribution

### Features
- Tracks 7+ project types automatically
- Safe, read-first modification strategy
- Validates dates and file paths
- Creates backups on error
- Comprehensive logging system
- Manual and automatic update modes

### Documentation
- Installation guide
- Quick start guide
- Usage examples
- Troubleshooting guide
- Complete skill specification
- Auto-run configuration guide

### Safety
- Read-before-write safety
- Content preservation (never deletes)
- Path verification
- Date validation
- Error backups
- Audit logging

## [1.4.0] - 2025-11-25

### Added
- **Trading & Finance** (3 skills)
  - Trading Analysis: CSV statement parsing, performance metrics, risk analysis, LaTeX/PDF reports
  - Portfolio Analysis Agent: Portfolio performance analysis and projections
  - Forecasting Agent: Financial forecasting and Monte Carlo simulations

- **Kymera Integration** (6 skills)
  - Portfolio Checker: Validates 90% win rate claims, identifies risk violations
  - MR Optimizer: Mean reversion strategy parameter optimization
  - Strategy Integrator: Bidirectional portfolio/MR data flow management
  - Risk Monitor: Real-time position monitoring, -5% stop enforcement
  - Tax Optimizer: Quarterly tax calculation, tax-loss harvesting
  - Brand Skill: Kymera branding guidelines and assets

- **Session Management** (4 skills)
  - Memory Keeper: Automated CLAUDE.md context management
  - Obsidian Memory Keeper: Daily notes and session tracking
  - Todo Keeper: Task persistence with SessionStart/End hooks
  - Vault Keeper: Obsidian vault structure validation

- **Content & Media** (6 skills)
  - YouTube Transcriber, YouTube Transcript Extractor
  - Transcript Archiver, Transcript to Logseq, Transcript to Obsidian
  - STT Transcription

- **System Tools** (2 skills)
  - System Health Check: System diagnostics and monitoring
  - Smart Screenshot: OCR and context extraction

### Changed
- Updated plugin.json to v1.4.0
- Reorganized README with 8 skill categories
- Added skill selection guide
- Updated repository structure documentation

### Total Skills: 32

## [Unreleased]

### Planned
- Google Workspace OAuth automation
- Skill dependency management
- Cross-skill workflows

---

**Format**: [Keep a Changelog](https://keepachangelog.com)
**Versioning**: [Semantic Versioning](https://semver.org)
