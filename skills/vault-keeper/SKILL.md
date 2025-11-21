# vault-keeper

Maintains Obsidian vault organization and structure according to established conventions.

## Description

The vault-keeper skill ensures the Obsidian vault at `~/Documents/Obsidian/Aaron/` maintains its organizational structure and follows established naming conventions. It enforces the numbered folder hierarchy (00_Navigation/, 01_Academic/, etc.) and keeps the root level clean.

## Capabilities

### Structure Enforcement
- Monitors root-level files and ensures only allowed files remain at root
- Validates numbered folder hierarchy (00-08)
- Prevents clutter by auto-organizing misplaced files
- Maintains consistent folder structure across sessions

### File Organization Rules
**Root Level (4 files only)**:
- `Home.md` - Main vault dashboard
- `CLAUDE.md` - Vault guidance for Claude Code
- `README.md` - Vault metadata and information
- (NO other .md files at root)

**Numbered Folder Hierarchy**:
- `00_Navigation/` - Dashboards and Maps of Content
  - `Dashboards/` - All dashboard files (*-Dashboard.md)
  - `Maps-of-Content/` - All MOC files (*MOC.md)
- `01_Academic/` - Research notes, coursework, dissertation
- `02_Professional/` - Business ventures (KYMERA Holdings)
- `03_Technical/` - Commands, prompts, configurations
- `04_Finance/` - Stock market, trading strategies
- `05_Mobile/` - Mobile quick references
- `06_Archive/` - Historical content and backups
- `07_System/` - System files, indexes, references
  - `Indexes/` - Tags Index, Unlinked Mentions, Daily Notes
- `08_Enso/` - Sync scripts and Enso-related content

**Non-Numbered Folders** (allowed):
- `Daily/` - Daily notes with sessions/meetings
- `Projects/` - Active project notes (xai, stoch, cc-flow, trading)
- `Knowledge/` - Reference library (Academic, Prompts)
- `Templates/` - Obsidian note templates

### Task Management
**Canonical Source**: `00_Navigation/Dashboards/Todo-Dashboard.md`
- All task tracking happens in Todo-Dashboard.md
- No duplicate task files (todo.md, Todo List.md) permitted
- SessionEnd hook auto-saves tasks

### Validation Actions
When invoked, vault-keeper:
1. Scans root directory for .md files
2. Identifies files that don't belong at root
3. Suggests proper locations based on file type/name
4. Optionally moves files to correct locations
5. Reports on vault health and structure compliance

## Usage

```bash
# Invoke skill to check vault structure
/vault-keeper check

# Auto-organize misplaced files
/vault-keeper organize

# Report vault statistics
/vault-keeper stats

# Validate numbered folder structure
/vault-keeper validate-structure
```

## File Type Detection

The skill uses these heuristics to organize files:

**Dashboards** (`*-Dashboard.md`) → `00_Navigation/Dashboards/`
**MOCs** (`* MOC.md`) → `00_Navigation/Maps-of-Content/`
**Indexes** (`*Index.md`, `*Mentions.md`) → `07_System/Indexes/`
**Daily Notes** (`YYYY-MM-DD.md`) → `Daily/`
**Academic Content** (course names, research keywords) → `01_Academic/`
**Technical Reports** (technical keywords) → `03_Technical/`
**Personal References** (`Places.md`, `Restaurants.md`) → `05_Mobile/` or delete

## Integration

### SessionEnd Hook
Auto-validates vault structure on session exit:
```python
#!/usr/bin/env python3
import os
from pathlib import Path

VAULT = Path.home() / "Documents/Obsidian/Aaron"
ALLOWED_ROOT = {"Home.md", "CLAUDE.md", "README.md"}

def validate():
    root_files = set(f.name for f in VAULT.glob("*.md"))
    violations = root_files - ALLOWED_ROOT
    if violations:
        print(f"⚠️  Vault structure violation: {len(violations)} files at root")
        print(f"Files: {', '.join(violations)}")
        return False
    print("✅ Vault structure: OK")
    return True

if __name__ == "__main__":
    validate()
```

## Configuration

### vault-keeper.yaml
```yaml
vault_path: ~/Documents/Obsidian/Aaron
allowed_root_files:
  - Home.md
  - CLAUDE.md
  - README.md
numbered_folders:
  - 00_Navigation
  - 01_Academic
  - 02_Professional
  - 03_Technical
  - 04_Finance
  - 05_Mobile
  - 06_Archive
  - 07_System
  - 08_Enso
auto_organize: false  # Set to true for automatic file moves
```

## Examples

### Example 1: Detecting Root Clutter
```
User creates new file: ~/Documents/Obsidian/Aaron/random-note.md

vault-keeper check:
⚠️  Found 1 file at root that doesn't belong:
  - random-note.md (no clear category)

Suggestions:
  - Move to Projects/ if project-related
  - Move to 05_Mobile/ if quick reference
  - Move to appropriate numbered folder based on content
```

### Example 2: Auto-Organizing Dashboard
```
User creates: ~/Documents/Obsidian/Aaron/Finance-Dashboard.md

vault-keeper organize:
✅ Moved Finance-Dashboard.md → 00_Navigation/Dashboards/
Reason: Matches *-Dashboard.md pattern
```

### Example 3: Vault Health Report
```
vault-keeper stats:

📊 Vault Health Report
Root files: 3/3 (compliant)
Numbered folders: 9/9 (complete)
Total files: 185 markdown files
Recent changes: 12 files modified in last 24h

Structure: ✅ HEALTHY
Task management: ✅ Consolidated (Todo-Dashboard.md only)
Archives: ✅ Clean (06_Archive/ contains dated backup)
```

## Maintenance Commands

```bash
# Check vault structure
python ~/.claude/skills/vault-keeper/validate_structure.py

# Auto-organize misplaced files
python ~/.claude/skills/vault-keeper/auto_organize.py

# Generate vault report
python ~/.claude/skills/vault-keeper/vault_report.py
```

## Notes

- Respects user's numbered folder system philosophy
- Prevents root-level clutter by design
- Integrates with existing SessionEnd hooks
- Non-destructive by default (suggests moves, doesn't execute without confirmation)
- Maintains compatibility with Obsidian's graph view and backlinks

## See Also

- `obsidian-memory-keeper` - Daily notes and session tracking
- `todo-keeper` - Task persistence and management
- `memory-keeper` - CLAUDE.md updates
