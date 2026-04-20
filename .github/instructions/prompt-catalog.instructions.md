---
description: "Katalog aller verfügbaren Prompts, Agents und Skills im Workspace."
applyTo: "**"
priority: optional
---

# Prompt, Agent & Skill Katalog

Übersicht aller Copilot-Erweiterungen in diesem Workspace. Für Qualitätsstandards der Dateien selbst siehe `copilot-customization.instructions.md`.

---

## 1. Prompts (`.github/prompts/`)

Aufruf via `/name` im Chat.

| Prompt | Zweck |
|---|---|
| `/jira-review` | Jira-Ticket gegen DoR-Checkliste und Team-Template prüfen |
| `/jira-enhance-to-dor` | Unvollständiges Jira-Ticket auf DoR-Niveau bringen |
| `/document-review` | Dokument/Spezifikation als Review-Partner prüfen |
| `/document-comparison` | Zwei Dokumente/Versionen vergleichen, Gap-Analyse erstellen |
| `/requirements-analysis` | Anforderungen auf Vollständigkeit, Testbarkeit, Klarheit prüfen |
| `/meeting-summary` | Strukturierte Meeting-Zusammenfassung erstellen |
| `/create-workorder` | Neue Workorder-Spezifikation erstellen (interaktiver Wizard) |
| `/wiki-write` | Wissens-Snippet aus Session in wiki/ zurückschreiben |
| `/wiki-ingest` | Quelldatei aus inbox/ destillieren → wiki/-Snippets |
| `/wiki-lint` | Health-Check für wiki/ |
| `/save-session` | Session-Ergebnisse + Denkprozess für nächste Session speichern |
| `/start` | Alle verfügbaren Prompts, Skills und Instructions als Katalog anzeigen |
| `/remember` | Einzelnes Learning persistent als Memory speichern |
| `/cognitive-continuity-context-transfer` | Strukturiertes Kontext-Transfer-Artefakt (CCCTP) für Session-Handover |
| `/refresh-docs` | ARCHITECTURE.md und copilot-instructions.md gegen Workspace prüfen, Updates vorschlagen |

---

## 2. Agents (`.github/agents/`)

Aufruf via `@name` im Chat.

| Agent | Rolle |
|---|---|
| `@developer` | Implementiert Workorders, schreibt Code und Tests |
| `@architect` | System-Architektur, Technologie-Entscheidungen, ADRs |
| `@critical-thinker` | Hinterfragt Annahmen, deckt blinde Flecken auf — schreibt keinen Code |
| `@doublecheck` | Prüft AI-Outputs auf Faktengenauigkeit, flaggt Risiken |

---

## 3. Skills (`.github/skills/`)

Werden automatisch oder per Agent aktiviert.

| Skill | Zweck |
|---|---|
| `knowledge-retrieval` | Wissen aus Confluence, Jira, SharePoint, Vault abrufen |
| `schreibstil` | Schreibstil-Guide — eliminiert KI-Muster, erzeugt direkte Sprache |
| `rdf-shacl` | RDF/SHACL-Arbeits-Skill: Formate, Shape-Syntax, Workspace-Tools |
| `document-pipeline` | Dokumenten-Konvertierung: Word/PDF/Excel/PPTX/HTML → Markdown |
| `ai-content-check` | KI-Text-Erkennung: Stylometrische Analyse, Modell-Attribution |

---

## 4. Instructions (`.github/instructions/`)

Werden automatisch per `applyTo`-Pattern aktiviert.

| Instruction | Zweck | Scope |
|---|---|---|
| `vibecoding-core` | Vibecoding-Loop, 70%-Risiko, Context-Management | `**` |
| `vibecoding-extended` | Projekt-Guardrails: Security, Architektur, Code-Qualität, Tests | `**` |
| `context-engineering` | Context-Optimierung für Copilot | `**` |
| `copilot-customization` | Standards für .prompt.md, .agent.md, .instructions.md | Copilot-Dateien |
| `markdown` | Markdown-Standards | `**/*.md` |
| `memory-system` | Memory-Scopes, Active Context, Session-Workflow | `**` |
| `prompt-catalog` | Dieser Katalog | `**` |
| `python` | Python-Konventionen | `**/*.py` |
| `response-style` | Kommunikation, Sprache, Severity Levels | `**` |
| `spec-driven` | Workorder/ADR-Lifecycle | `**` |
| `vault-knowledge` | Recherche-Reihenfolge, Vault, wiki/ | `**` |
| `wiki-provenance` | wiki/-Provenance-Schema | `wiki/**` |

