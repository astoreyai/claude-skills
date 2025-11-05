# Version Management Guide

This guide explains how to version skills in the Claude Skills library using Semantic Versioning.

## Semantic Versioning Overview

Version format: **MAJOR.MINOR.PATCH** (e.g., 2.1.3)

- **MAJOR**: Incompatible changes that break existing usage
- **MINOR**: New features added in a backwards-compatible manner
- **PATCH**: Backwards-compatible bug fixes

## When to Bump Versions

### MAJOR Version (X.0.0)

Increment the MAJOR version when you make incompatible changes:

**Examples:**
- Change core workflow that requires users to update their integration
- Remove existing functionality or features
- Change skill invocation method
- Modify output format in breaking ways
- Change required dependencies in incompatible ways

**Before:** v1.5.3 → **After:** v2.0.0

### MINOR Version (0.X.0)

Increment the MINOR version when you add functionality in a backwards-compatible manner:

**Examples:**
- Add new capabilities or features
- Add new optional parameters
- Add new components or templates
- Improve performance without changing API
- Add new output formats alongside existing ones
- Deprecate features (but don't remove them yet)

**Before:** v1.5.3 → **After:** v1.6.0

### PATCH Version (0.0.X)

Increment the PATCH version for backwards-compatible bug fixes:

**Examples:**
- Fix bugs or errors
- Update documentation
- Fix typos
- Improve internal code without changing behavior
- Security patches
- Dependency updates (for security)

**Before:** v1.5.3 → **After:** v1.5.4

## Special Versions

### Pre-release Versions (0.x.x)

Use versions starting with 0 during initial development:

- **0.1.0**: First working version
- **0.2.0**: Added major features during development
- **0.x.x**: Development continues
- **1.0.0**: First stable public release

### Release Candidates

For testing before major releases:

- **2.0.0-rc.1**: Release candidate 1
- **2.0.0-rc.2**: Release candidate 2
- **2.0.0**: Final stable release

## Version Management Workflow

### 1. Development Cycle

```
1.0.0 (stable)
  ↓
[Make changes]
  ↓
Update CHANGELOG.md (Unreleased section)
  ↓
[Ready for release]
  ↓
Decide version bump (MAJOR/MINOR/PATCH)
  ↓
Update version numbers
  ↓
Move CHANGELOG Unreleased → New version
  ↓
1.1.0 (new stable)
```

### 2. Updating Version Numbers

When releasing a new version, update in:

1. **README.md badge:**
   ```markdown
   ![Version](https://img.shields.io/badge/version-1.1.0-blue)
   ```

2. **CHANGELOG.md header:**
   ```markdown
   ## [1.1.0] - 2025-11-05
   ```

3. **VERSION file** (if present):
   ```
   1.1.0
   ```

4. **package.json** (for Node.js skills):
   ```json
   {
     "version": "1.1.0"
   }
   ```

### 3. CHANGELOG.md Maintenance

Always maintain the CHANGELOG with upcoming changes:

```markdown
# Changelog

## [Unreleased]

### Added
- New feature X that does Y
- Support for Z format

### Fixed
- Bug in component A

## [1.1.0] - 2025-11-05

### Added
- Feature from previous release

...
```

When releasing, move Unreleased items to the new version section.

## Version Decision Matrix

| Change Type | Examples | Version Bump |
|-------------|----------|--------------|
| Breaking change | Remove feature, change API | MAJOR |
| New feature | Add capability, new template | MINOR |
| Bug fix | Fix error, correct typo | PATCH |
| Documentation | Update README, add examples | PATCH |
| Deprecation | Mark feature as deprecated | MINOR |
| Security fix | Patch vulnerability | PATCH* |

*Security fixes may warrant MINOR or even MAJOR depending on severity and impact.

## Examples

### Example 1: Adding a New Feature

**Current Version:** 1.2.3

**Changes:**
- Added new component for email template generation
- Updated README with new examples

**Decision:** MINOR bump (new feature, backwards compatible)

**New Version:** 1.3.0

**CHANGELOG Entry:**
```markdown
## [1.3.0] - 2025-11-05

### Added
- Email template generation component
- Examples for email workflows in README

### Changed
- Enhanced documentation clarity
```

---

### Example 2: Fixing a Bug

**Current Version:** 2.1.4

**Changes:**
- Fixed parsing error in data extraction
- Corrected typo in documentation

**Decision:** PATCH bump (bug fixes only)

**New Version:** 2.1.5

**CHANGELOG Entry:**
```markdown
## [2.1.5] - 2025-11-05

### Fixed
- Data extraction parsing error for edge cases
- Documentation typos in installation section
```

---

### Example 3: Breaking Change

**Current Version:** 1.8.2

**Changes:**
- Completely rewrote core workflow
- Changed skill invocation method
- Removed deprecated legacy components

**Decision:** MAJOR bump (breaking changes)

**New Version:** 2.0.0

**CHANGELOG Entry:**
```markdown
## [2.0.0] - 2025-11-05

### Changed
- **BREAKING**: Completely rewrote core workflow for better performance
- **BREAKING**: New skill invocation method (see migration guide)

### Removed
- **BREAKING**: Removed deprecated legacy components from v1.x

### Added
- Migration guide from v1.x to v2.0
- Improved error messages
```

---

### Example 4: Pre-release to Stable

**Current Version:** 0.9.0

**Changes:**
- Final testing complete
- Documentation finalized
- Ready for first stable release

**Decision:** MAJOR bump to 1.0.0 (first stable release)

**New Version:** 1.0.0

**CHANGELOG Entry:**
```markdown
## [1.0.0] - 2025-11-05

### Added
- Initial stable release
- Core functionality for [list features]
- Comprehensive documentation
- Example use cases
```

## Git Tagging

When releasing versions, create git tags:

```bash
# Create annotated tag
git tag -a v1.1.0 -m "Release version 1.1.0"

# Push tag to remote
git push origin v1.1.0

# List all tags
git tag -l
```

## Release Notes

For significant releases, consider creating release notes beyond CHANGELOG:

**RELEASE_NOTES_1.1.0.md:**
```markdown
# Release Notes: Version 1.1.0

Release Date: 2025-11-05

## Highlights

- New email template generation component
- 30% performance improvement in parsing
- Enhanced error messages

## Breaking Changes

None

## Migration Guide

No migration needed - fully backwards compatible

## What's Next

- Planned for v1.2.0: Calendar integration
- Planned for v2.0.0: Complete API redesign
```

## Deprecation Strategy

When planning to remove features:

1. **Version X.Y.0**: Deprecate feature (add warning, mark in docs)
   ```markdown
   ### Deprecated
   - Feature X is deprecated and will be removed in v2.0.0
   - Use Feature Y instead (see migration guide)
   ```

2. **Version (X+1).0.0**: Remove feature
   ```markdown
   ### Removed
   - **BREAKING**: Removed deprecated Feature X
   - Use Feature Y (see migration guide)
   ```

## Version History Format

Maintain links at bottom of CHANGELOG:

```markdown
[Unreleased]: https://github.com/astoreyai/claude-skills/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/astoreyai/claude-skills/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/astoreyai/claude-skills/releases/tag/v1.0.0
```

## Best Practices

1. **Document Everything**: Update CHANGELOG with every change
2. **Be Conservative**: When in doubt, bump MINOR instead of PATCH
3. **Communicate Breaking Changes**: Clearly mark breaking changes in CHANGELOG
4. **Test Before Release**: Verify all functionality before version bump
5. **Keep History**: Never delete old CHANGELOG entries
6. **Date Your Releases**: Always include release date
7. **Link Versions**: Provide comparison links in CHANGELOG
8. **Follow Conventions**: Stick to semantic versioning strictly

## Quick Reference

```
Breaking change?     → MAJOR (X.0.0)
New feature?         → MINOR (0.X.0)
Bug fix?             → PATCH (0.0.X)
Documentation only?  → PATCH (0.0.X)
First stable?        → 1.0.0
Still developing?    → 0.X.Y
```

## Resources

- [Semantic Versioning Specification](https://semver.org/)
- [Keep a Changelog](https://keepachangelog.com/)
- [Git Tagging](https://git-scm.com/book/en/v2/Git-Basics-Tagging)
