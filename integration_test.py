"""
Integration tests for the YouTube Transcriber pipeline.

Validates that all 4 skills can be imported and work together:
1. Extract facts from transcripts (Phase 1: TranscriptExtractor)
2. Format to Logseq atomic notes (Phase 2: LogseqFormatter)
3. Integrate to Obsidian vault (Phase 3: ObsidianIntegrator)
4. Archive transcripts (Phase 4: TranscriptArchiver)

This test validates:
- All 4 skills can be imported
- Each skill can be instantiated
- Basic functionality works (file I/O, path handling)
"""

import sys
import tempfile
from pathlib import Path

# Add skills to path
SKILLS_DIR = Path(__file__).parent
sys.path.insert(0, str(SKILLS_DIR / "youtube-transcript-extractor" / "src"))
sys.path.insert(0, str(SKILLS_DIR / "transcript-to-logseq" / "src"))
sys.path.insert(0, str(SKILLS_DIR / "transcript-to-obsidian" / "src"))
sys.path.insert(0, str(SKILLS_DIR / "transcript-archiver" / "src"))


def test_phase_1_import():
    """Test Phase 1: TranscriptExtractor can be imported."""
    try:
        from extractor import TranscriptExtractor
        extractor = TranscriptExtractor()
        assert extractor is not None
        print("✓ Phase 1: TranscriptExtractor imported and instantiated")
        return True
    except Exception as e:
        print(f"✗ Phase 1: {e}")
        return False


def test_phase_2_import():
    """Test Phase 2: LogseqFormatter can be imported."""
    try:
        from logseq_formatter import LogseqFormatter
        formatter = LogseqFormatter()
        assert formatter is not None
        print("✓ Phase 2: LogseqFormatter imported and instantiated")
        return True
    except Exception as e:
        print(f"✗ Phase 2: {e}")
        return False


def test_phase_3_import():
    """Test Phase 3: ObsidianIntegrator can be imported."""
    try:
        from integrator import ObsidianIntegrator
        with tempfile.TemporaryDirectory() as tmp_dir:
            integrator = ObsidianIntegrator(vault_path=Path(tmp_dir) / "vault")
            assert integrator is not None
            assert integrator.vault_path == Path(tmp_dir) / "vault"
        print("✓ Phase 3: ObsidianIntegrator imported and instantiated")
        return True
    except Exception as e:
        print(f"✗ Phase 3: {e}")
        return False


def test_phase_4_import():
    """Test Phase 4: TranscriptArchiver can be imported."""
    try:
        from archiver import TranscriptArchiver
        with tempfile.TemporaryDirectory() as tmp_dir:
            archiver = TranscriptArchiver(archive_dir=Path(tmp_dir) / "archive")
            assert archiver is not None
            assert archiver.archive_dir == Path(tmp_dir) / "archive"
        print("✓ Phase 4: TranscriptArchiver imported and instantiated")
        return True
    except Exception as e:
        print(f"✗ Phase 4: {e}")
        return False


def test_phase_3_integration():
    """Test Phase 3: Basic integration functionality."""
    try:
        from integrator import ObsidianIntegrator
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            vault_path = tmp_path / "vault"

            # Create test files
            notes_dir = tmp_path / "notes"
            notes_dir.mkdir()
            (notes_dir / "test.md").write_text("# Test\nContent")

            integrator = ObsidianIntegrator(vault_path=vault_path)
            result = integrator.integrate(notes_dir, dry_run=True)

            assert result["success"] is True
            print("✓ Phase 3: Integration dry-run successful")
            return True
    except Exception as e:
        print(f"✗ Phase 3 Integration: {e}")
        return False


def test_phase_4_archiver():
    """Test Phase 4: Archiver functionality."""
    try:
        from archiver import TranscriptArchiver
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)

            # Create test files
            transcripts_dir = tmp_path / "transcripts"
            transcripts_dir.mkdir()
            (transcripts_dir / "test.md").write_text("# Test\nContent")

            archiver = TranscriptArchiver(archive_dir=tmp_path / "archive")
            result = archiver.archive(transcripts_dir, verify_only=True)

            assert result["success"] is True
            assert result["file_count"] == 1
            print("✓ Phase 4: Archiver verification successful")
            return True
    except Exception as e:
        print(f"✗ Phase 4 Archiver: {e}")
        return False


def run_integration_tests():
    """Run all integration tests."""
    print("\n" + "=" * 70)
    print("YouTube Transcriber Pipeline - Integration Tests")
    print("=" * 70 + "\n")

    tests = [
        ("Phase 1 Import", test_phase_1_import),
        ("Phase 2 Import", test_phase_2_import),
        ("Phase 3 Import", test_phase_3_import),
        ("Phase 4 Import", test_phase_4_import),
        ("Phase 3 Integration", test_phase_3_integration),
        ("Phase 4 Archiver", test_phase_4_archiver),
    ]

    results = {}
    for test_name, test_func in tests:
        results[test_name] = test_func()

    print("\n" + "=" * 70)
    print("Test Summary")
    print("=" * 70 + "\n")

    passed = sum(1 for v in results.values() if v)
    total = len(results)

    print(f"Passed: {passed}/{total}")

    if passed == total:
        print("\n✓ ALL INTEGRATION TESTS PASSED")
        print("  Pipeline architecture validated")
        print("  All 4 skills functional")
        print("=" * 70 + "\n")
        return 0
    else:
        print("\n✗ SOME TESTS FAILED")
        print("=" * 70 + "\n")
        return 1


if __name__ == "__main__":
    sys.exit(run_integration_tests())
