---
name: ai-content-check
description: "KI-Text-Erkennung und -Bereinigung: Stylometrische Analyse, Modell-Attribution, Fingerprint-Datenbank. Aktiviert bei AI-Detection, KI-Erkennung, Text-Prüfung auf KI-Urheberschaft."
metadata:
  trigger: AI-Text erkennen, KI-Erkennung, stylometrische Analyse, AI-Detection, Text prüfen auf KI, Fingerprint
  author: Author
---

# AI Content Check

Lokales Toolkit zur stylometrischen Analyse von Texten auf KI-Urheberschaft. Erkennt Modell-Fingerprints (Claude, ChatGPT, Copilot, Gemini) ohne API-Zugriff.

---

## 1. Modul-Übersicht

| Modul | Pfad | Zweck |
|---|---|---|
| **detector** | `_tools/ai_detect/detector.py` | Analyse-Engine: Text → DetectionResult |
| **fingerprints** | `_tools/ai_detect/fingerprints.py` | Fingerprint-Datenbank (Regex-Patterns je Modell/Sprache) |
| **reader** | `_tools/ai_detect/reader.py` | Text-Extraktion aus .txt, .md, .docx |
| **reporter** | `_tools/ai_detect/reporter.py` | Markdown-Report-Generator |

---

## 2. Schnelleinstieg

```python
from _tools.ai_detect.detector import AITextDetector
from _tools.ai_detect.reader import TextReader
from _tools.ai_detect.reporter import generate_report, FileResult
from pathlib import Path

# Einzelnen Text analysieren
detector = AITextDetector()
result = detector.analyze("Certainly, I'd be happy to explain this...")
print(result.top_model)       # "claude"
print(result.ai_probability)  # 0.87
print(result.confidence)      # "hoch"
print(result.evidence)        # ["[claude/en] 'certainly' (Gewicht 2.0)", ...]

# Datei lesen + analysieren
reader = TextReader()
text = reader.read(Path("inbox/ai-detect/sample.md"))
result = detector.analyze(text)

# Report generieren
results = [FileResult(path=Path("sample.md"), result=result)]
md = generate_report(results)
Path("output/ai-detect/report.md").write_text(md, encoding="utf-8")
```

---

## 3. DetectionResult — Ergebnis-Felder

| Feld | Typ | Beschreibung |
|---|---|---|
| `model_scores` | `dict[str, float]` | Score je Modell (0–100) |
| `top_model` | `str` | Wahrscheinlichstes Modell (`claude`, `chatgpt`, `copilot`, `gemini`, `unknown`) |
| `confidence` | `str` | `hoch`, `mittel`, `niedrig` |
| `ai_probability` | `float` | KI-Wahrscheinlichkeit (0.0–1.0) |
| `evidence` | `list[str]` | Gefundene Fingerprints als lesbare Belege |
| `language` | `str` | Erkannte Sprache: `en`, `de`, `unknown` |
| `structure_hints` | `list[str]` | Strukturelle Auffälligkeiten (Satzlänge, Bullet-Ratio) |

---

## 4. Fingerprint-Datenbank

### Erkannte Modelle

| Modell | Sprachen | Typische Marker |
|---|---|---|
| **Claude** | EN, DE | "certainly", "I'd be happy to", "nuanced", "comprehensive overview" |
| **ChatGPT** | EN, DE | "delve into", "as of my update", "Absolutely!", "Great question!" |
| **Copilot** | EN, DE | Code-Kommentar-Muster, "// TODO", technischer Stil |
| **Gemini** | EN, DE | "that's a great question", Google-spezifische Phrasen |
| **Generic AI** | EN, DE | Modellübergreifende Muster (übermäßige Höflichkeit, Throat-Clearing) |

### Analyse-Methodik
- **70% Phrasen-Score:** Regex-basierter Abgleich gegen Fingerprint-DB
- **30% Struktur-Score:** Satzlängen-Verteilung, Bullet-Ratio, Absatzstruktur
- **Mindestlänge:** 100 Zeichen für sinnvolle Analyse

---

## 5. Unterstützte Input-Formate

| Format | Endung | Methode |
|---|---|---|
| Plain Text | `.txt` | Direktes UTF-8-Lesen |
| Markdown | `.md` | Syntax bereinigt (Links, Code, HTML entfernt) |
| Word | `.docx` | python-docx (Absätze extrahiert) |

---

## 6. Synergie mit Schreibstil-Skill

Der `ai-content-check` Skill ergänzt den `schreibstil` Skill:

| Schritt | Tool | Zweck |
|---|---|---|
| 1. Erkennung | `ai-content-check` | Prüfen ob Text KI-generiert ist + welches Modell |
| 2. Bereinigung | `schreibstil` Skill | KI-Muster eliminieren, direkte Sprache erzeugen |
| 3. Validierung | `ai-content-check` | Erneut prüfen ob KI-Marker reduziert wurden |

---

## 7. Referenzen

| Thema | Pfad |
|---|---|
| Detector Engine | `_tools/ai_detect/detector.py` |
| Fingerprint-DB | `_tools/ai_detect/fingerprints.py` |
| Text Reader | `_tools/ai_detect/reader.py` |
| Report Generator | `_tools/ai_detect/reporter.py` |
| Schreibstil-Skill | `.github/skills/schreibstil/SKILL.md` |


