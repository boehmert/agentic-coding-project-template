---
description: "Prüft ARCHITECTURE.md und copilot-instructions.md gegen den aktuellen Workspace-Stand. Schlägt gezielte Updates vor — nur veraltete oder fehlende Abschnitte."
mode: agent
---

# Refresh Docs

Prüfe `ARCHITECTURE.md` und `.github/copilot-instructions.md` auf Aktualität und Vollständigkeit.
Schlage gezielte Änderungen vor — keine Komplettüberarbeitung, nur was tatsächlich veraltet oder unvollständig ist.

**Regel: Nichts schreiben ohne explizite Freigabe.**

---

## Schritt 0 — Aktuellen Stand laden

Lese parallel:

1. `ARCHITECTURE.md` (komplett)
2. `.github/copilot-instructions.md` (komplett)
3. `.github/instructions/` — Verzeichnisliste (Dateinamen)
4. `.github/prompts/` — Verzeichnisliste (Dateinamen)
5. `.github/agents/` — Verzeichnisliste (Dateinamen)
6. `_tools/` — Verzeichnisstruktur (1 Ebene tief)
7. `tasks/` — Verzeichnisstruktur (1 Ebene tief, falls vorhanden)
8. Root-Level `*.py` Dateien — Dateinamen
9. `requirements.txt` (falls vorhanden)

---

## Schritt 1 — ARCHITECTURE.md prüfen

Vergleiche den Inhalt von `ARCHITECTURE.md` gegen den tatsächlichen Workspace-Zustand.

### 1a. Folder Structure

Prüfe jeden dokumentierten Ordner:
- Existiert er noch?
- Stimmt die Beschreibung?
- Fehlt ein wichtiger Ordner, der inzwischen existiert? (z.B. `Planning-PI17/`, `governance/`, neue `_tools/`-Unterordner)

### 1b. Tech Stack

Prüfe gegen `requirements.txt` und tatsächliche Imports:
- Werden Libraries genannt, die nicht mehr im Einsatz sind?
- Fehlen Libraries, die inzwischen genutzt werden?
- Stimmt die Python-Version noch?

### 1c. Key Flows

Prüfe ob die beschriebenen Flows noch der Realität entsprechen:
- Gibt es neue Workflow-Muster, die nicht dokumentiert sind?
- Sind beschriebene Patterns veraltet?

### 1d. Key Boundaries

Prüfe ob Grenzziehungen noch stimmen:
- Werden Boundaries in der Praxis eingehalten?
- Gibt es neue Boundary-Regeln, die fehlen?

---

## Schritt 2 — copilot-instructions.md prüfen

### 2a. MCP-Server-Tabelle

Vergleiche gegen `.vscode/mcp.json`:
- Sind alle konfigurierten Server dokumentiert?
- Fehlen Server oder sind welche entfernt worden?

### 2b. Regelschichtung

Prüfe das Schichtungsdiagramm am Ende der Datei:
- Stimmen die aufgelisteten Instruction-Files mit `.github/instructions/` überein?
- Fehlen neue Instruction-Files?
- Sind entfernte Files noch gelistet?

### 2c. Prompt- und Agent-Katalog

Referenziert `copilot-instructions.md` den Katalog korrekt?
Prüfe ob `prompt-catalog.instructions.md` aktuell ist:
- Neue Prompts in `.github/prompts/`, die nicht gelistet sind?
- Neue Agents in `.github/agents/`, die nicht gelistet sind?

### 2d. Rolle, Source of Truth, Kernregeln

Sind diese Abschnitte noch korrekt und vollständig?

---

## Schritt 3 — Änderungsvorschlag formulieren

Erstelle einen strukturierten Bericht:

```markdown
## Refresh-Docs Bericht

### ARCHITECTURE.md

#### Korrekt (keine Änderung nötig)
- [Liste der geprüften Abschnitte, die stimmen]

#### Änderungen vorgeschlagen
| Abschnitt | Problem | Vorgeschlagene Änderung |
|-----------|---------|------------------------|
| ...       | ...     | ...                     |

### copilot-instructions.md

#### Korrekt (keine Änderung nötig)
- [Liste]

#### Änderungen vorgeschlagen
| Abschnitt | Problem | Vorgeschlagene Änderung |
|-----------|---------|------------------------|
| ...       | ...     | ...                     |

### Weitere betroffene Dateien
(z.B. prompt-catalog.instructions.md, falls veraltet)
```

---

## Schritt 4 — Freigabe einholen

Präsentiere den Bericht und frage:

> Welche der vorgeschlagenen Änderungen soll ich umsetzen? Alle, eine Auswahl, oder keine?

**Erst nach expliziter Bestätigung** die genehmigten Änderungen schreiben.
Jede Änderung einzeln mit `replace_string_in_file` umsetzen — keine Datei komplett überschreiben.

