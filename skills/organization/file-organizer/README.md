# File Organizer

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Status](https://img.shields.io/badge/status-stable-green)
![License](https://img.shields.io/badge/license-MIT-green)

## Description

Intelligently organizes your files and folders across your computer by understanding context, finding duplicates, suggesting better structures, and automating cleanup tasks. Reduces cognitive load and keeps your digital workspace tidy without manual effort.

This skill acts as your personal organization assistant, helping you maintain a clean, logical file structure across your computer without the mental overhead of constant manual organization.

## Features

- ✅ Analyzes current file and folder structures
- ✅ Finds duplicate files across your system
- ✅ Suggests logical organization schemes
- ✅ Automates cleanup with user approval
- ✅ Context-aware decisions based on file types, dates, and content
- ✅ Identifies old/unused files for archival

## Installation

### Prerequisites

- Claude Code installed

### Setup

This skill is ready to use once copied to your Claude Code skills directory.

## Usage

### Basic Usage

From your home directory or any target location:

```bash
cd ~/Downloads
# Then invoke Claude Code with organization requests
```

**Examples:**
- "Help me organize my Downloads folder"
- "Find duplicate files in my Documents folder"
- "Review my project directories and suggest improvements"

### Common Use Cases

#### Organize Downloads Folder
Ask Claude to analyze your Downloads folder and suggest organization by file type, project, or date.

#### Find Duplicates
Identify duplicate files that are wasting disk space across multiple directories.

#### Restructure Project Directories
Review existing project organization and get suggestions for better structure.

#### Clean Up Old Files
Identify files that haven't been accessed recently for potential archival or deletion.

## When to Use This Skill

- Your Downloads folder is a chaotic mess
- You can't find files because they're scattered everywhere
- You have duplicate files taking up space
- Your folder structure doesn't make sense anymore
- You want to establish better organization habits
- You're starting a new project and need a good structure
- You're cleaning up before archiving old projects

## Configuration Options

This skill works out-of-the-box with no configuration needed. All organization actions require user approval before execution.

## Examples

### Example 1: Organizing Downloads

**Request:**
```
Organize my Downloads folder
```

**Process:**
1. Analyzes files in Downloads
2. Groups by type (documents, images, archives, etc.)
3. Suggests folder structure
4. Awaits approval before moving files

### Example 2: Finding Duplicates

**Request:**
```
Find duplicate files in ~/Documents
```

**Process:**
1. Scans all files in Documents directory
2. Identifies duplicates by content hash
3. Lists duplicate groups with file paths
4. Suggests which duplicates to keep/remove

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Author

Aaron Storey (@astoreyai)

## Related Skills

- [Paper Reviewer](../../review/paper-reviewer/) - For reviewing academic papers
