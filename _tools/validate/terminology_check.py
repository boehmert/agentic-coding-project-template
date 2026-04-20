"""
Terminologie-Konsistenz-Check für PROJECT/MACK-Dokumente
=======================================================
Prüft Markdown-Dateien auf korrekte Verwendung kanonischer Begriffe.

Verwendung:
    python -m _tools.validate.terminology_check --path output/
    python -m _tools.validate.terminology_check --file output/reports/example.md

Glossar: _tools/validate/glossary.yaml
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

# ── Glossar laden ────────────────────────────────────────────────────────────

GLOSSARY_PATH = Path(__file__).parent / "glossary.yaml"


def load_glossary(path: Path = GLOSSARY_PATH) -> dict[str, dict[str, Any]]:
    """Lädt das Terminologie-Glossar."""
    text = path.read_text(encoding="utf-8")
    return yaml.safe_load(text) or {}


# ── Ergebnis ─────────────────────────────────────────────────────────────────

@dataclass
class TermFinding:
    """Ein Terminologie-Fund."""
    file: Path
    line_no: int
    found: str
    canonical: str
    severity: str = "🟡"


@dataclass
class TermResult:
    """Sammel-Ergebnis."""
    findings: list[TermFinding] = field(default_factory=list)

    @property
    def summary(self) -> str:
        return f"🟡 {len(self.findings)} Terminologie-Abweichungen"


# ── Prüflogik ────────────────────────────────────────────────────────────────

def _build_variant_map(glossary: dict[str, dict[str, Any]]) -> list[tuple[re.Pattern[str], str, str]]:
    """Baut aus dem Glossar eine Liste (pattern, canonical, found_variant)."""
    patterns: list[tuple[re.Pattern[str], str, str]] = []

    for _key, entry in glossary.items():
        canonical = entry.get("canonical", "")
        for variant in entry.get("variants", []):
            # Nur abweichende Varianten prüfen
            if variant == canonical:
                continue
            # Wort-Grenzen für sauberes Matching
            escaped = re.escape(variant)
            pat = re.compile(rf"\b{escaped}\b")
            patterns.append((pat, canonical, variant))

    return patterns


def check_file(path: Path, glossary: dict[str, dict[str, Any]]) -> list[TermFinding]:
    """Prüft eine Datei auf Terminologie-Abweichungen."""
    findings: list[TermFinding] = []
    variant_map = _build_variant_map(glossary)
    lines = path.read_text(encoding="utf-8").splitlines()

    for line_no, line in enumerate(lines, start=1):
        # Frontmatter und Code-Blöcke überspringen
        if line.strip().startswith("```") or line.strip() == "---":
            continue

        for pattern, canonical, variant in variant_map:
            if pattern.search(line):
                findings.append(TermFinding(
                    file=path,
                    line_no=line_no,
                    found=variant,
                    canonical=canonical,
                ))

    return findings


def check_directory(root: Path, glossary: dict[str, dict[str, Any]]) -> TermResult:
    """Scannt ein Verzeichnis rekursiv."""
    result = TermResult()
    for md_file in sorted(root.rglob("*.md")):
        if md_file.name.startswith(".") or "_archive" in md_file.parts:
            continue
        result.findings.extend(check_file(md_file, glossary))
    return result


# ── Report ───────────────────────────────────────────────────────────────────

def format_report(result: TermResult) -> str:
    """Erzeugt einen Markdown-Report."""
    lines = [
        "# Terminologie-Konsistenz-Bericht\n",
        f"**Ergebnis:** {result.summary}\n",
    ]

    if not result.findings:
        lines.append("✅ Keine Terminologie-Abweichungen gefunden.\n")
        return "\n".join(lines)

    by_file: dict[Path, list[TermFinding]] = {}
    for f in result.findings:
        by_file.setdefault(f.file, []).append(f)

    for file_path, findings in sorted(by_file.items()):
        rel = file_path.as_posix()
        lines.append(f"\n## `{rel}`\n")
        for f in findings:
            lines.append(
                f"- 🟡 Zeile {f.line_no}: `{f.found}` → verwende `{f.canonical}`"
            )

    return "\n".join(lines)


# ── CLI ──────────────────────────────────────────────────────────────────────

def main() -> int:
    """CLI-Einstiegspunkt."""
    import argparse

    parser = argparse.ArgumentParser(
        description="PROJECT/MACK Terminologie-Konsistenz-Check",
    )
    parser.add_argument(
        "--path", type=Path, default=Path("output"),
        help="Verzeichnis zum Scannen (Standard: output/)",
    )
    parser.add_argument(
        "--file", type=Path, default=None,
        help="Einzelne Datei prüfen",
    )
    parser.add_argument(
        "--glossary", type=Path, default=GLOSSARY_PATH,
        help="Pfad zum Glossar (Standard: _tools/validate/glossary.yaml)",
    )
    args = parser.parse_args()

    glossary = load_glossary(args.glossary)

    if args.file:
        findings = check_file(args.file, glossary)
        result = TermResult(findings=findings)
    else:
        result = check_directory(args.path, glossary)

    report = format_report(result)
    print(report)

    return 1 if result.findings else 0


if __name__ == "__main__":
    sys.exit(main())

