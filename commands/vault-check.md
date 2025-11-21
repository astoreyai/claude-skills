You are being asked to validate the Obsidian vault structure.

Run the vault structure validation script:

```bash
python3 ~/.claude/skills/vault-keeper/validate_structure.py
```

This will check:
- Root files (should be exactly: Home.md, CLAUDE.md, README.md)
- Numbered folder structure (00_Navigation through 08_Enso)
- Navigation organization (Dashboards and Maps-of-Content)
- System structure (Indexes folder)
- Task management (no duplicates)

If any violations are found, report them to the user with suggestions for fixing.
