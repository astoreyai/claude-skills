#!/usr/bin/env python3
"""
Obsidian Vault Structure Validator
Ensures vault maintains organizational standards
"""

import sys
from pathlib import Path
from datetime import datetime

VAULT = Path.home() / "Documents/Obsidian/Aaron"
ALLOWED_ROOT = {"Home.md", "CLAUDE.md", "README.md"}
REQUIRED_NUMBERED = [
    "00_Navigation",
    "01_Academic",
    "02_Professional",
    "03_Technical",
    "04_Finance",
    "05_Mobile",
    "06_Archive",
    "07_System",
    "08_Enso"
]

def validate_root_files():
    """Check root level only has allowed files"""
    root_files = set(f.name for f in VAULT.glob("*.md"))
    violations = root_files - ALLOWED_ROOT

    if violations:
        print(f"⚠️  Root structure violation: {len(violations)} files don't belong at root")
        for f in sorted(violations):
            print(f"   - {f}")
        return False

    print(f"✅ Root files: {len(root_files)}/{len(ALLOWED_ROOT)} (compliant)")
    return True

def validate_numbered_folders():
    """Check numbered folder structure exists"""
    missing = []
    for folder in REQUIRED_NUMBERED:
        folder_path = VAULT / folder
        if not folder_path.exists():
            missing.append(folder)

    if missing:
        print(f"⚠️  Missing numbered folders: {', '.join(missing)}")
        return False

    print(f"✅ Numbered folders: {len(REQUIRED_NUMBERED)}/{len(REQUIRED_NUMBERED)} (complete)")
    return True

def validate_navigation_structure():
    """Check 00_Navigation/ has proper subfolders"""
    nav = VAULT / "00_Navigation"
    if not nav.exists():
        print("⚠️  00_Navigation/ folder missing")
        return False

    required_subdirs = ["Dashboards", "Maps-of-Content"]
    missing = [d for d in required_subdirs if not (nav / d).exists()]

    if missing:
        print(f"⚠️  00_Navigation/ missing: {', '.join(missing)}")
        return False

    # Check dashboards are in right place
    dashboards = list((nav / "Dashboards").glob("*-Dashboard.md"))
    mocs = list((nav / "Maps-of-Content").glob("* MOC.md"))

    print(f"✅ Navigation structure: {len(dashboards)} dashboards, {len(mocs)} MOCs")
    return True

def validate_system_structure():
    """Check 07_System/ has Indexes subfolder"""
    system = VAULT / "07_System"
    if not system.exists():
        print("⚠️  07_System/ folder missing")
        return False

    indexes = system / "Indexes"
    if not indexes.exists():
        print("⚠️  07_System/Indexes/ missing")
        return False

    index_files = list(indexes.glob("*.md"))
    print(f"✅ System structure: {len(index_files)} index files")
    return True

def check_task_duplicates():
    """Ensure no duplicate task files exist"""
    forbidden = ["todo.md", "Todo List.md"]
    found = []

    for f in forbidden:
        if (VAULT / f).exists():
            found.append(f)

    if found:
        print(f"⚠️  Duplicate task files found: {', '.join(found)}")
        print("   Canonical source: 00_Navigation/Dashboards/Todo-Dashboard.md")
        return False

    print("✅ Task management: Consolidated (no duplicates)")
    return True

def vault_stats():
    """Print vault statistics"""
    total_md = len(list(VAULT.rglob("*.md")))
    root_md = len(list(VAULT.glob("*.md")))

    print(f"\n📊 Vault Statistics")
    print(f"Total markdown files: {total_md}")
    print(f"Root-level files: {root_md}")
    print(f"Last validation: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    """Run all validation checks"""
    print("=" * 60)
    print("OBSIDIAN VAULT STRUCTURE VALIDATION")
    print(f"Vault: {VAULT}")
    print("=" * 60)
    print()

    checks = [
        ("Root Files", validate_root_files),
        ("Numbered Folders", validate_numbered_folders),
        ("Navigation Structure", validate_navigation_structure),
        ("System Structure", validate_system_structure),
        ("Task Management", check_task_duplicates),
    ]

    results = []
    for name, check in checks:
        try:
            result = check()
            results.append(result)
        except Exception as e:
            print(f"❌ {name}: Error - {e}")
            results.append(False)
        print()

    vault_stats()

    print()
    print("=" * 60)
    if all(results):
        print("✅ VAULT STRUCTURE: HEALTHY")
        print("=" * 60)
        return 0
    else:
        failed = sum(1 for r in results if not r)
        print(f"⚠️  VAULT STRUCTURE: {failed}/{len(results)} checks failed")
        print("=" * 60)
        return 1

if __name__ == "__main__":
    sys.exit(main())
