#!/usr/bin/env python3
"""
YouTube Transcriber - Complete End-to-End Workflow Runner

This script executes the full 4-phase pipeline:
1. Extract facts from YouTube transcript
2. Format as atomic notes
3. Integrate into Obsidian vault
4. Archive original transcripts

Usage:
    python workflow_runner.py --transcript <path> --vault-path <path>
"""

import sys
import os
import json
import tempfile
from pathlib import Path
from typing import Optional

# Add skills to path
SKILLS_DIR = Path(__file__).parent
sys.path.insert(0, str(SKILLS_DIR / "youtube-transcript-extractor" / "src"))
sys.path.insert(0, str(SKILLS_DIR / "transcript-to-logseq" / "src"))
sys.path.insert(0, str(SKILLS_DIR / "transcript-to-obsidian" / "src"))
sys.path.insert(0, str(SKILLS_DIR / "transcript-archiver" / "src"))


class YouTubeTranscriberWorkflow:
    """Execute complete YouTube Transcriber workflow."""

    def __init__(self, transcript_path: Path, vault_path: Optional[Path] = None, output_dir: Optional[Path] = None):
        """Initialize workflow with paths."""
        self.transcript_path = Path(transcript_path)
        self.vault_path = vault_path or Path.home() / "Documents/Obsidian/Aaron"
        self.output_dir = output_dir or Path(tempfile.mkdtemp(prefix="yt-transcriber-"))
        self.results = {}

    def run(self):
        """Execute complete workflow: Phase 1 → 2 → 3 → 4."""
        print("\n" + "=" * 70)
        print("YouTube Transcriber - Complete Workflow Execution")
        print("=" * 70)
        print(f"\nTranscript: {self.transcript_path}")
        print(f"Output Dir: {self.output_dir}")
        print(f"Vault Path: {self.vault_path}\n")

        # Phase 1: Extract facts
        print("=" * 70)
        print("PHASE 1: Extracting facts from transcript...")
        print("=" * 70)
        try:
            from extractor import TranscriptExtractor

            if not self.transcript_path.exists():
                print(f"❌ Transcript not found: {self.transcript_path}")
                return False

            with open(self.transcript_path, 'r') as f:
                transcript_content = f.read()

            print(f"✓ Transcript loaded ({len(transcript_content)} chars)")

            extractor = TranscriptExtractor()
            print("✓ TranscriptExtractor initialized")

            # Extract facts
            print("\n⏳ Calling Claude API to extract facts...")
            print("   (This requires ANTHROPIC_API_KEY environment variable)")

            extraction_result = extractor.extract_facts(
                transcript_content,
                video_title=self.transcript_path.stem,
                video_id=f"vid_{self.transcript_path.stem}"
            )

            facts_count = len(extraction_result.facts)
            topics_count = len(extraction_result.topics)

            print(f"✓ Facts extracted: {facts_count}")
            print(f"✓ Topics identified: {topics_count}")
            print(f"✓ Accuracy: {extraction_result.accuracy:.2%}")

            self.results["phase_1"] = {
                "success": True,
                "facts_extracted": facts_count,
                "topics": extraction_result.topics,
                "accuracy": extraction_result.accuracy,
                "extraction_result": extraction_result
            }

        except Exception as e:
            print(f"\n❌ Phase 1 Failed: {e}")
            print("\nNote: Phase 1 requires ANTHROPIC_API_KEY environment variable")
            print("      Set it with: export ANTHROPIC_API_KEY='sk-ant-...'")
            self.results["phase_1"] = {"success": False, "error": str(e)}
            return False

        # Phase 2: Format as atomic notes
        print("\n" + "=" * 70)
        print("PHASE 2: Formatting facts as atomic notes...")
        print("=" * 70)
        try:
            from logseq_formatter import LogseqFormatter

            formatter = LogseqFormatter()
            print("✓ LogseqFormatter initialized")

            notes_dir = self.output_dir / "notes"
            notes_dir.mkdir(parents=True, exist_ok=True)

            print(f"\n⏳ Formatting {facts_count} facts into atomic notes...")

            format_result = formatter.format_extraction(
                self.results["phase_1"]["extraction_result"],
                output_dir=notes_dir
            )

            notes_created = format_result.get("notes_created", 0)
            topics = format_result.get("topics", [])

            print(f"✓ Atomic notes created: {notes_created}")
            print(f"✓ Topics structured: {len(topics)}")
            print(f"✓ Output directory: {notes_dir}")

            # Show sample file structure
            md_files = list(notes_dir.rglob("*.md"))
            if md_files:
                print(f"\n  Sample files created:")
                for mf in sorted(md_files)[:3]:
                    rel_path = mf.relative_to(notes_dir)
                    size = mf.stat().st_size
                    print(f"    • {rel_path} ({size} bytes)")
                if len(md_files) > 3:
                    print(f"    ... and {len(md_files) - 3} more files")

            self.results["phase_2"] = {
                "success": format_result.get("success", True),
                "notes_created": notes_created,
                "topics": topics,
                "output_dir": str(notes_dir)
            }

        except Exception as e:
            print(f"\n❌ Phase 2 Failed: {e}")
            self.results["phase_2"] = {"success": False, "error": str(e)}
            return False

        # Phase 3: Integrate into Obsidian
        print("\n" + "=" * 70)
        print("PHASE 3: Integrating into Obsidian vault...")
        print("=" * 70)
        try:
            from integrator import ObsidianIntegrator

            integrator = ObsidianIntegrator(vault_path=self.vault_path)
            print("✓ ObsidianIntegrator initialized")
            print(f"✓ Vault path: {self.vault_path}")

            print(f"\n⏳ Integrating {notes_created} notes into vault...")

            integration_result = integrator.integrate(
                notes_dir,
                dry_run=False  # Actually integrate (not dry-run)
            )

            if integration_result.get("success"):
                notes_integrated = integration_result.get("notes_integrated", 0)
                backlinks = integration_result.get("backlinks_created", 0)

                print(f"✓ Notes integrated: {notes_integrated}")
                print(f"✓ Backlinks created: {backlinks}")

                # Check for index
                index_path = self.vault_path / "Knowledge" / "Video-Transcripts" / "index.md"
                if index_path.exists():
                    print(f"✓ Index created: {index_path}")

                self.results["phase_3"] = {
                    "success": True,
                    "notes_integrated": notes_integrated,
                    "backlinks_created": backlinks,
                    "vault_path": str(self.vault_path)
                }
            else:
                raise Exception(integration_result.get("error", "Unknown error"))

        except Exception as e:
            print(f"\n❌ Phase 3 Failed: {e}")
            self.results["phase_3"] = {"success": False, "error": str(e)}
            return False

        # Phase 4: Archive transcripts
        print("\n" + "=" * 70)
        print("PHASE 4: Archiving transcripts...")
        print("=" * 70)
        try:
            from archiver import TranscriptArchiver

            archiver = TranscriptArchiver()
            print("✓ TranscriptArchiver initialized")

            # Create transcript archive directory
            transcripts_dir = self.output_dir / "transcripts"
            transcripts_dir.mkdir(parents=True, exist_ok=True)

            # Copy original transcript to archive dir
            import shutil
            archived_transcript = transcripts_dir / self.transcript_path.name
            shutil.copy2(self.transcript_path, archived_transcript)
            print(f"✓ Transcript staged for archival: {archived_transcript}")

            print(f"\n⏳ Creating compressed archive...")

            archive_result = archiver.archive(
                transcripts_dir,
                cleanup=False,  # Don't delete originals
                verify_only=False
            )

            if archive_result.get("success"):
                archive_path = archive_result.get("archive_path", "")
                files_archived = archive_result.get("files_archived", 0)

                if archive_path:
                    archive_size = Path(archive_path).stat().st_size / 1024
                    print(f"✓ Archive created: {archive_path}")
                    print(f"✓ Archive size: {archive_size:.1f} KB")
                    print(f"✓ Files archived: {files_archived}")

                self.results["phase_4"] = {
                    "success": True,
                    "archive_path": archive_path,
                    "files_archived": files_archived
                }
            else:
                raise Exception(archive_result.get("error", "Unknown error"))

        except Exception as e:
            print(f"\n❌ Phase 4 Failed: {e}")
            self.results["phase_4"] = {"success": False, "error": str(e)}
            return False

        return True

    def print_summary(self):
        """Print workflow summary."""
        print("\n" + "=" * 70)
        print("WORKFLOW SUMMARY")
        print("=" * 70 + "\n")

        phase_names = {
            "phase_1": "Fact Extraction",
            "phase_2": "Note Formatting",
            "phase_3": "Obsidian Integration",
            "phase_4": "Transcript Archival"
        }

        all_success = True
        for phase_key, phase_name in phase_names.items():
            if phase_key not in self.results:
                print(f"{phase_name}: ⏭️  SKIPPED")
                continue

            phase_result = self.results[phase_key]
            success = phase_result.get("success", False)
            status = "✅ PASS" if success else "❌ FAIL"
            print(f"{phase_name}: {status}")

            if success:
                for key, value in phase_result.items():
                    if key not in ["success", "extraction_result"]:
                        if isinstance(value, (int, float, bool)):
                            print(f"  • {key}: {value}")
                        elif isinstance(value, str) and len(value) < 80:
                            print(f"  • {key}: {value}")
            else:
                error = phase_result.get("error", "Unknown error")
                print(f"  • Error: {error}")
                all_success = False

        print("\n" + "=" * 70)
        if all_success:
            print("✅ WORKFLOW COMPLETE - ALL PHASES SUCCESSFUL")
            print("\nNext steps:")
            print(f"  1. Check Obsidian vault: {self.vault_path}")
            print(f"  2. Review notes in: {self.results.get('phase_2', {}).get('output_dir')}")
            print(f"  3. Archive stored at: {self.results.get('phase_4', {}).get('archive_path')}")
        else:
            print("⚠️  WORKFLOW INCOMPLETE - CHECK ERRORS ABOVE")

        print("=" * 70 + "\n")


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="YouTube Transcriber Complete Workflow"
    )
    parser.add_argument(
        "--transcript",
        required=True,
        help="Path to transcript file"
    )
    parser.add_argument(
        "--vault-path",
        help="Path to Obsidian vault (default: ~/Documents/Obsidian/Aaron)"
    )
    parser.add_argument(
        "--output-dir",
        help="Output directory for workflow artifacts"
    )

    args = parser.parse_args()

    # Create and run workflow
    workflow = YouTubeTranscriberWorkflow(
        transcript_path=args.transcript,
        vault_path=Path(args.vault_path) if args.vault_path else None,
        output_dir=Path(args.output_dir) if args.output_dir else None
    )

    success = workflow.run()
    workflow.print_summary()

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
