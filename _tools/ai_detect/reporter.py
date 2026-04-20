"""
Markdown-Report-Generator für AI-Detektor
==========================================
Erzeugt einen lesbaren Markdown-Report aus den Analyseergebnissen.

Verwendung:
    from _tools.ai_detect.reporter import generate_report, FileResult
    from pathlib import Path

    results = [FileResult(path=Path("sample.txt"), result=detection_result)]
    md = generate_report(results)
    Path("output/ai-detect/report.md").write_text(md, encoding="utf-8")
"""

from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional
from datetime import datetime

from _tools.ai_detect.detector import DetectionResult


# ── Datenklasse für Datei-Ergebnis ─────────────────────────────────────────

@dataclass
class FileResult:
    """Ergebnis der Analyse einer einzelnen Datei."""
    path: Path
    result: Optional[DetectionResult]
    error: Optional[str] = None


# ── Modell-Anzeigenamen ────────────────────────────────────────────────────

MODEL_LABELS = {
    "claude":  "Claude (Anthropic)",
    "chatgpt": "ChatGPT / GPT-4 (OpenAI)",
    "copilot": "GitHub Copilot (Microsoft)",
    "gemini":  "Gemini (Google)",
    "unknown": "Unbekannt / nicht erkannt",
}

CONFIDENCE_EMOJI = {
    "hoch":    "🟢 hoch",
    "mittel":  "🟡 mittel",
    "niedrig": "🔴 niedrig",
}


# ── Haupt-Funktion ──────────────────────────────────────────────────────────

def generate_report(
    file_results: List[FileResult],
    title: str = "AI-Text-Detektions-Report",
) -> str:
    """
    Erzeugt einen vollständigen Markdown-Report aus den Analyseergebnissen.

    Args:
        file_results: Liste von FileResult-Objekten.
        title:        Titel des Reports.

    Returns:
        Den Report als Markdown-String.
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    sections: List[str] = []

    # ── Header ───────────────────────────────────────────────────────────────
    sections.append(f"# {title}\n")
    sections.append(f"**Erstellt:** {now}  ")
    sections.append(f"**Analysierte Dateien:** {len(file_results)}\n")

    # ── Zusammenfassungs-Tabelle ──────────────────────────────────────────────
    sections.append("---\n")
    sections.append("## Zusammenfassung\n")
    sections.append(_build_summary_table(file_results))

    # ── Detail-Abschnitte je Datei ────────────────────────────────────────────
    sections.append("\n---\n")
    sections.append("## Detailanalyse\n")

    for fr in file_results:
        sections.append(_build_file_section(fr))

    # ── Hinweis zur Interpretation ────────────────────────────────────────────
    sections.append("\n---\n")
    sections.append(_build_footer())

    return "\n".join(sections)


# ── Interne Hilfsfunktionen ─────────────────────────────────────────────────

def _build_summary_table(file_results: List[FileResult]) -> str:
    """Erzeugt die Zusammenfassungs-Tabelle."""
    header = (
        "| Datei | Sprache | KI-Wahrsch. | Wahrsch. Modell | Konfidenz |\n"
        "|-------|---------|-------------|-----------------|-----------|"
    )
    rows = [header]

    for fr in file_results:
        filename = fr.path.name
        if fr.error:
            rows.append(f"| `{filename}` | — | — | ❌ Fehler: {fr.error} | — |")
            continue

        r = fr.result
        lang_label = "Deutsch 🇩🇪" if r.language == "de" else "Englisch 🇬🇧"
        prob_pct = f"{r.ai_probability * 100:.0f} %"
        model_label = MODEL_LABELS.get(r.top_model, r.top_model)
        conf_label = CONFIDENCE_EMOJI.get(r.confidence, r.confidence)

        rows.append(
            f"| `{filename}` | {lang_label} | {prob_pct} | {model_label} | {conf_label} |"
        )

    return "\n".join(rows)


def _build_file_section(fr: FileResult) -> str:
    """Erzeugt den Detail-Abschnitt für eine Datei."""
    filename = fr.path.name
    lines: List[str] = []

    lines.append(f"\n### `{filename}`\n")

    if fr.error:
        lines.append(f"> **Fehler beim Lesen:** {fr.error}\n")
        return "\n".join(lines)

    r = fr.result

    # Kernergebnis
    lang_label = "Deutsch" if r.language == "de" else "Englisch"
    model_label = MODEL_LABELS.get(r.top_model, r.top_model)
    conf_label = CONFIDENCE_EMOJI.get(r.confidence, r.confidence)

    lines.append(f"- **Sprache erkannt:** {lang_label}")
    lines.append(f"- **KI-Wahrscheinlichkeit:** {r.ai_probability * 100:.0f} %")
    lines.append(f"- **Wahrscheinlichstes Modell:** {model_label}")
    lines.append(f"- **Konfidenz:** {conf_label}")
    lines.append("")

    # Score-Balken
    if any(v > 0 for v in r.model_scores.values()):
        lines.append("**Modell-Scores:**\n")
        lines.append("| Modell | Score | Balken |")
        lines.append("|--------|-------|--------|")
        for model in ["claude", "chatgpt", "copilot", "gemini"]:
            score = r.model_scores.get(model, 0.0)
            bar = _score_bar(score)
            label = MODEL_LABELS.get(model, model)
            marker = " ◀ **Top**" if model == r.top_model and r.top_model != "unknown" else ""
            lines.append(f"| {label} | {score:.1f} | {bar}{marker} |")
        lines.append("")

    # Strukturhinweise
    if r.structure_hints:
        lines.append("**Strukturelle Auffälligkeiten:**\n")
        for hint in r.structure_hints:
            lines.append(f"- {hint}")
        lines.append("")

    # Gefundene Belege
    if r.evidence:
        lines.append("**Gefundene Fingerprints:**\n")
        # Max. 15 Belege anzeigen, um Report übersichtlich zu halten
        shown = r.evidence[:15]
        for ev in shown:
            lines.append(f"- `{ev}`")
        if len(r.evidence) > 15:
            lines.append(f"- *... und {len(r.evidence) - 15} weitere*")
        lines.append("")

    return "\n".join(lines)


def _score_bar(score: float, width: int = 20) -> str:
    """Erzeugt einen ASCII-Balken für einen Score (0–100)."""
    filled = round((score / 100) * width)
    empty = width - filled
    return f"{'█' * filled}{'░' * empty} {score:.0f}"


def _build_footer() -> str:
    """Erzeugt den Hinweis-Abschnitt am Ende des Reports."""
    return (
        "## Hinweise zur Interpretation\n\n"
        "- **KI-Wahrscheinlichkeit** gibt an, wie stark der Text insgesamt "
        "KI-typische Merkmale zeigt (Phrasen + Struktur kombiniert).\n"
        "- **Modell-Scores** basieren auf stylometrischen Fingerprints "
        "(charakteristische Phrasen je Modell). Scores sind relativ zueinander.\n"
        "- **Konfidenz:**\n"
        "  - 🟢 **hoch** — deutlicher Abstand zwischen Top-Modell und allen anderen\n"
        "  - 🟡 **mittel** — erkennbare Tendenz, aber nicht eindeutig\n"
        "  - 🔴 **niedrig** — kein klares Modell erkennbar (evtl. menschlicher Text, "
        "paraphrasiert oder sehr kurz)\n"
        "- Diese Analyse ist **heuristisch** und kein Beweis. "
        "Falsch-Positive und Falsch-Negative sind möglich.\n"
        "- Sehr kurze Texte (< 100 Zeichen) werden als 'nicht auswertbar' markiert.\n"
    )

