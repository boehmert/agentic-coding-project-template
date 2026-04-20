"""
Validate Output – Kombinierter Qualitäts-Check
================================================
Führt Frontmatter-Validierung, Terminologie-Check und
AI-Style-Check auf Workspace-Dateien aus.

Verwendung:
    python tasks/validate-output/run.py                    # Alle Checks
    python tasks/validate-output/run.py --check frontmatter
    python tasks/validate-output/run.py --check terminology
    python tasks/validate-output/run.py --check ai-style
    python tasks/validate-output/run.py --path output/reports/
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Workspace-Root erkennen
WORKSPACE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(WORKSPACE))

from _tools.validate.frontmatter_check import (
    validate_directory as fm_validate_dir,
    validate_file as fm_validate_file,
    format_report as fm_format_report,
    ValidationResult,
)
from _tools.validate.terminology_check import (
    check_directory as term_check_dir,
    check_file as term_check_file,
    format_report as term_format_report,
    load_glossary,
    TermResult,
)


def _run_frontmatter(target: Path, single_file: bool) -> int:
    """Frontmatter-Validierung ausführen."""
    print("=" * 60)
    print("  FRONTMATTER-VALIDIERUNG")
    print("=" * 60)

    if single_file:
        result = ValidationResult(findings=fm_validate_file(target))
    else:
        result = fm_validate_dir(target)

    print(fm_format_report(result))
    return 1 if result.has_errors else 0


def _run_terminology(target: Path, single_file: bool) -> int:
    """Terminologie-Check ausführen."""
    print("\n" + "=" * 60)
    print("  TERMINOLOGIE-KONSISTENZ")
    print("=" * 60)

    glossary = load_glossary()

    if single_file:
        result = TermResult(findings=term_check_file(target, glossary))
    else:
        result = term_check_dir(target, glossary)

    print(term_format_report(result))
    return 1 if result.findings else 0


def _run_ai_style(target: Path, single_file: bool) -> int:
    """AI-Style-Check via ai_detect ausführen."""
    print("\n" + "=" * 60)
    print("  AI-STYLE-CHECK")
    print("=" * 60)

    try:
        from _tools.ai_detect.detector import AITextDetector
    except ImportError:
        print("⚠️  _tools.ai_detect nicht verfügbar, überspringe AI-Style-Check.")
        return 0

    detector = AITextDetector()
    threshold = 0.6
    issues = 0

    if single_file:
        files = [target]
    else:
        files = sorted(target.rglob("*.md"))

    for md_file in files:
        if md_file.name.startswith(".") or "_archive" in md_file.parts:
            continue
        text = md_file.read_text(encoding="utf-8")
        if len(text) < detector.min_text_length:
            continue
        result = detector.analyze(text)
        if result.ai_probability > threshold:
            issues += 1
            rel = md_file.relative_to(WORKSPACE).as_posix()
            prob = f"{result.ai_probability:.0%}"
            model = result.top_model
            print(f"- 🟡 `{rel}`: AI-Wahrscheinlichkeit {prob} ({model})")

    if issues == 0:
        print("✅ Keine auffälligen AI-Muster gefunden.")
    else:
        print(f"\n🟡 {issues} Datei(en) über Schwelle ({threshold:.0%}).")

    return 1 if issues > 0 else 0


def main() -> int:
    """CLI-Einstiegspunkt."""
    parser = argparse.ArgumentParser(
        description="Kombinierter Qualitäts-Check für Agentic-Workspace-Dateien",
    )
    parser.add_argument(
        "--path", type=Path, default=None,
        help="Verzeichnis oder Datei zum Prüfen",
    )
    parser.add_argument(
        "--check", choices=["frontmatter", "terminology", "ai-style", "all"],
        default="all",
        help="Welchen Check ausführen (Standard: all)",
    )
    args = parser.parse_args()

    checks = args.check
    exit_code = 0

    # Frontmatter: Standard-Pfad .github/
    if checks in ("all", "frontmatter"):
        fm_target = args.path or (WORKSPACE / ".github")
        single = fm_target.is_file()
        exit_code |= _run_frontmatter(fm_target, single)

    # Terminologie: Standard-Pfad output/
    if checks in ("all", "terminology"):
        term_target = args.path or (WORKSPACE / "output")
        single = term_target.is_file()
        exit_code |= _run_terminology(term_target, single)

    # AI-Style: Standard-Pfad output/
    if checks in ("all", "ai-style"):
        ai_target = args.path or (WORKSPACE / "output")
        single = ai_target.is_file()
        exit_code |= _run_ai_style(ai_target, single)

    print("\n" + "=" * 60)
    if exit_code:
        print("  ❌ Validierung abgeschlossen mit Findings.")
    else:
        print("  ✅ Alle Checks bestanden.")
    print("=" * 60)

    return exit_code


if __name__ == "__main__":
    sys.exit(main())

