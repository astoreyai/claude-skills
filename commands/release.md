---
description: Automate version releases - bump version, update CHANGELOG, commit, and tag
arguments:
  - name: type
    description: Release type (patch, minor, major)
    required: true
  - name: message
    description: Optional release message
    required: false
---

# Release Command

Automate the release process for the current project.

## Usage

```
/release patch          # 1.4.0 → 1.4.1
/release minor          # 1.4.0 → 1.5.0
/release major          # 1.4.0 → 2.0.0
/release patch "Bug fixes for scanner"
```

## Process

When invoked, perform these steps:

### 1. Detect Version File
Look for version in (priority order):
- `package.json` → `"version": "x.y.z"`
- `.claude-plugin/plugin.json` → `"version": "x.y.z"`
- `pyproject.toml` → `version = "x.y.z"`
- `setup.py` → `version="x.y.z"`
- `VERSION` file

### 2. Bump Version
Based on argument:
- `patch`: x.y.z → x.y.(z+1)
- `minor`: x.y.z → x.(y+1).0
- `major`: x.y.z → (x+1).0.0

### 3. Update CHANGELOG.md
Add entry at top of changelog (after ## [Unreleased] if present):

```markdown
## [NEW_VERSION] - YYYY-MM-DD

### Changed
- [User message or "Version bump"]
```

### 4. Git Operations
```bash
git add -A
git commit -m "Release vNEW_VERSION: MESSAGE"
git tag vNEW_VERSION
```

### 5. Output
Report:
- Previous version → New version
- Files modified
- Git tag created
- Remind user to `git push && git push --tags` if desired

## Example Output

```
Release v1.4.1

📦 Version: 1.4.0 → 1.4.1
📝 Updated: package.json, CHANGELOG.md
🏷️  Tagged: v1.4.1

Run `git push && git push --tags` to publish.
```

## Safety
- Abort if working directory has uncommitted changes (other than version files)
- Abort if version file not found
- Never auto-push (user must confirm)
