"""
Frontmatter-Validator für Copilot-Konfigurationsdateien
========================================================
Prüft YAML-Frontmatter in .prompt.md, .agent.md, .instructions.md,
SKILL.md, Workorders und ADRs gegen die definierten Schemata.

Verwendung:
    python -m _tools.validate.frontmatter_check [--path .github/]
    python -m _tools.validate.frontmatter_check --file .github/prompts/start.prompt.md

Schemata basieren auf:
    - .github/instructions/copilot-customization.instructions.md
    - .github/instructions/spec-driven.instructions.md
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


# ── Schemata ─────────────────────────────────────────────────────────────────

SCHEMAS: dict[str, dict[str, Any]] = {
    "prompt": {
        "required": ["description"],
        "optional": ["name", "applyTo", "mode", "tools", "agent"],
        "rules": {
            "description": {"type": str, "min_len": 20, "max_len": 200},
            "mode": {"type": str, "enum": ["agent", "ask", "edit"]},
            "tools": {"type": list},
            "agent": {"type": str},
        },
    },
    "agent": {
        "required": ["description"],
        "optional": ["name", "tools"],
        "rules": {
            "description": {"type": str, "min_len": 20, "max_len": 200},
            "tools": {"type": list},
        },
    },
    "instruction": {
        "required": ["description", "applyTo"],
        "optional": ["name", "priority"],
        "rules": {
            "description": {"type": str, "min_len": 20, "max_len": 200},
            "applyTo": {"type": str},
            "priority": {"type": str, "enum": ["core", "recommended", "optional"]},
        },
    },
    "skill": {
        "required": ["name", "description"],
        "optional": ["metadata", "license"],
        "rules": {
            "description": {"type": str, "min_len": 20},
            "name": {"type": str},
        },
    },
    "workorder": {
        "required": ["id", "title", "version", "status", "created", "created_by"],
        "optional": [
            "reviewed_by", "parent_spec", "priority", "estimated_effort",
            "depends_on", "related_to",
        ],
        "rules": {
            "id": {"type": str, "pattern": r"^WO\d{2,}$"},
            "version": {"type": str, "pattern": r"^\d+\.\d+\.\d+$"},
            "status": {
                "type": str,
                "enum": ["PLANNED", "IN_PROGRESS", "REVIEW", "DONE", "BLOCKED"],
            },
            "priority": {
                "type": str,
                "enum": ["LOW", "MEDIUM", "HIGH", "CRITICAL"],
            },
        },
    },
    "adr": {
        "required": ["id", "title", "version", "status", "created", "created_by"],
        "optional": ["reviewed_by", "supersedes", "superseded_by"],
        "rules": {
            "id": {"type": str, "pattern": r"^ADR-\d{3,}$"},
            "version": {"type": str, "pattern": r"^\d+\.\d+\.\d+$"},
            "status": {
                "type": str,
                "enum": ["PROPOSED", "ACCEPTED", "DEPRECATED", "SUPERSEDED"],
            },
        },
    },
}


# ── Ergebnis ─────────────────────────────────────────────────────────────────

@dataclass
class Finding:
    """Ein einzelnes Validierungsergebnis."""
    file: Path
    severity: str       # 🔴 | 🟡 | 🟢
    field: str
    message: str


@dataclass
class ValidationResult:
    """Sammel-Ergebnis aller Prüfungen."""
    findings: list[Finding] = field(default_factory=list)

    @property
    def has_errors(self) -> bool:
        return any(f.severity == "🔴" for f in self.findings)

    @property
    def summary(self) -> str:
        critical = sum(1 for f in self.findings if f.severity == "🔴")
        important = sum(1 for f in self.findings if f.severity == "🟡")
        minor = sum(1 for f in self.findings if f.severity == "🟢")
        return f"🔴 {critical}  🟡 {important}  🟢 {minor}"


# ── Frontmatter extrahieren ──────────────────────────────────────────────────

_FM_PATTERN = re.compile(
    r"\A---\s*\n((?:(?!---\s*$)[^\n]*\n)*)---\s*\n",
    re.MULTILINE,
)


def extract_frontmatter(path: Path) -> dict[str, Any] | None:
    """Extrahiert YAML-Frontmatter aus einer Markdown-Datei."""
    text = path.read_text(encoding="utf-8")
    m = _FM_PATTERN.match(text)
    if not m:
        return None
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return None


# ── Dateityp erkennen ────────────────────────────────────────────────────────

def detect_file_type(path: Path) -> str | None:
    """Bestimmt den Schema-Typ anhand des Dateinamens."""
    name = path.name.lower()
    if name.endswith(".prompt.md"):
        return "prompt"
    if name.endswith(".agent.md"):
        return "agent"
    if name.endswith(".instructions.md"):
        return "instruction"
    if name == "skill.md":
        return "skill"
    # Workorders: workorders/WOxx_*.md
    if path.parent.name == "workorders" and re.match(r"wo\d+", name):
        return "workorder"
    # ADRs: docs/adr/ADR-xxx_*.md
    if "adr" in str(path.parent).lower() and name.startswith("adr-"):
        return "adr"
    return None


# ── Einzelfeld validieren ────────────────────────────────────────────────────

def _validate_field(
    path: Path,
    field_name: str,
    value: Any,
    rules: dict[str, Any],
) -> list[Finding]:
    """Prüft ein einzelnes Feld gegen seine Regeln."""
    findings: list[Finding] = []
    rule = rules.get(field_name, {})

    # Typ-Check
    expected_type = rule.get("type")
    if expected_type and not isinstance(value, expected_type):
        findings.append(Finding(
            path, "🔴", field_name,
            f"Erwarteter Typ {expected_type.__name__}, gefunden {type(value).__name__}",
        ))
        return findings  # Weitere Checks sinnlos bei falschem Typ

    # String-spezifische Checks
    if isinstance(value, str):
        min_len = rule.get("min_len")
        if min_len and len(value) < min_len:
            findings.append(Finding(
                path, "🟡", field_name,
                f"Zu kurz ({len(value)} Zeichen, Minimum {min_len})",
            ))

        max_len = rule.get("max_len")
        if max_len and len(value) > max_len:
            findings.append(Finding(
                path, "🟡", field_name,
                f"Zu lang ({len(value)} Zeichen, Maximum {max_len})",
            ))

        pattern = rule.get("pattern")
        if pattern and not re.match(pattern, value):
            findings.append(Finding(
                path, "🔴", field_name,
                f"Entspricht nicht dem Muster {pattern}",
            ))

        enum = rule.get("enum")
        if enum and value not in enum:
            findings.append(Finding(
                path, "🔴", field_name,
                f"Ungültiger Wert '{value}'. Erlaubt: {', '.join(enum)}",
            ))

    return findings


# ── Datei validieren ─────────────────────────────────────────────────────────

def validate_file(path: Path) -> list[Finding]:
    """Validiert eine einzelne Datei gegen ihr Schema."""
    findings: list[Finding] = []

    file_type = detect_file_type(path)
    if not file_type:
        return findings  # Kein bekannter Dateityp

    schema = SCHEMAS[file_type]
    fm = extract_frontmatter(path)

    if fm is None:
        findings.append(Finding(
            path, "🔴", "frontmatter",
            "Kein gültiges YAML-Frontmatter gefunden",
        ))
        return findings

    # Pflichtfelder prüfen
    for req_field in schema["required"]:
        if req_field not in fm or fm[req_field] is None:
            findings.append(Finding(
                path, "🔴", req_field,
                f"Pflichtfeld '{req_field}' fehlt",
            ))
        elif req_field in fm:
            findings.extend(_validate_field(path, req_field, fm[req_field], schema["rules"]))

    # Optionale Felder validieren (wenn vorhanden)
    for opt_field in schema.get("optional", []):
        if opt_field in fm and fm[opt_field] is not None:
            findings.extend(_validate_field(path, opt_field, fm[opt_field], schema["rules"]))

    # Unbekannte Felder warnen
    all_known = set(schema["required"]) | set(schema.get("optional", []))
    for key in fm:
        if key not in all_known:
            findings.append(Finding(
                path, "🟢", key,
                f"Unbekanntes Frontmatter-Feld '{key}'",
            ))

    return findings


# ── Verzeichnis scannen ──────────────────────────────────────────────────────

def validate_directory(root: Path) -> ValidationResult:
    """Scannt ein Verzeichnis rekursiv und validiert alle erkannten Dateien."""
    result = ValidationResult()
    for md_file in sorted(root.rglob("*.md")):
        if md_file.name.startswith(".") or "_archive" in md_file.parts:
            continue
        file_type = detect_file_type(md_file)
        if file_type:
            result.findings.extend(validate_file(md_file))
    return result


# ── Report ───────────────────────────────────────────────────────────────────

def format_report(result: ValidationResult) -> str:
    """Erzeugt einen Markdown-Report aus dem Validierungsergebnis."""
    lines = [
        "# Frontmatter-Validierungsbericht\n",
        f"**Ergebnis:** {result.summary}\n",
    ]

    if not result.findings:
        lines.append("✅ Alle Dateien sind konform.\n")
        return "\n".join(lines)

    # Gruppiert nach Datei
    by_file: dict[Path, list[Finding]] = {}
    for f in result.findings:
        by_file.setdefault(f.file, []).append(f)

    for file_path, findings in sorted(by_file.items()):
        rel = file_path.as_posix()
        lines.append(f"\n## `{rel}`\n")
        for f in findings:
            lines.append(f"- {f.severity} **{f.field}:** {f.message}")

    return "\n".join(lines)


# ── CLI ──────────────────────────────────────────────────────────────────────

def main() -> int:
    """CLI-Einstiegspunkt."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Frontmatter-Validator für Copilot-Konfigurationsdateien",
    )
    parser.add_argument(
        "--path", type=Path, default=Path(".github"),
        help="Verzeichnis zum Scannen (Standard: .github/)",
    )
    parser.add_argument(
        "--file", type=Path, default=None,
        help="Einzelne Datei validieren",
    )
    parser.add_argument(
        "--strict", action="store_true",
        help="Exit-Code 1 bei 🔴 oder 🟡 Findings",
    )
    args = parser.parse_args()

    if args.file:
        findings = validate_file(args.file)
        result = ValidationResult(findings=findings)
    else:
        result = validate_directory(args.path)

    report = format_report(result)
    print(report)

    if args.strict:
        has_important = any(f.severity in ("🔴", "🟡") for f in result.findings)
        return 1 if has_important else 0

    return 1 if result.has_errors else 0


if __name__ == "__main__":
    sys.exit(main())
