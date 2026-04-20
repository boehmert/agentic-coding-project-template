---
description: "Zeigt alle verfügbaren Prompts, Skills und Instructions als Katalog. Nützlich wenn unklar ist, was für eine Aufgabe existiert."
---

Die folgende Aufgabe soll bearbeitet werden:

${input:task:Aufgabe beschreiben...}

---

## Schritt 0: Active Context laden

Lies `/memories/repo/active-context.md` (Memory-Tool, Befehl `view`). Dieser Kontext enthält:
- Aktuellen Arbeitsfokus aus vorherigen Sessions
- Letzte Entscheidungen mit Denkprozess
- Offene Fragen und nächste Schritte

Wenn die Datei existiert: Prüfe ob die Aufgabe an bestehende Arbeit anknüpft und nutze den Kontext.
Wenn die Datei nicht existiert oder leer ist: Weiter mit Schritt 1.

---

Bevor du beginnst, prüfe systematisch ob bereits Guardrails, Prompts oder Skills vorhanden sind, die genutzt werden sollen.

## Schritt 1: Aufgabe einordnen

Ordne die Aufgabe einer oder mehreren Kategorien zu:

| Kategorie | Schlüsselwörter |
|---|---|
| Jira | Ticket, Issue, Backlog, DoR, Sprint |
| Confluence | Seite, Space, Doku, Wiki, Audit |
| Dokument | Review, Analyse, Spezifikation, ADR, Workorder |
| Text/Schreiben | Formulieren, Schreiben, E-Mail, Kommentar, Zusammenfassung |
| Code | Python, Script, Task, Tool, `_tools/`, `tasks/` |
| Strategie/Kontext | PI, Ziele, Roadmap, Workday Goals |
| Wissenssuche | Suchen, Finden, Nachschlagen (intern) |

## Schritt 2: Passende Ressourcen prüfen

### Verfügbare Prompts (`/`-Befehle)

| Prompt | Wann verwenden |
|---|---|
| `/jira-review` | Jira-Ticket auf DoR + Template prüfen |
| `/jira-enhance-to-dor` | Unvollständiges Ticket auf DoR-Niveau bringen |
| `/document-review` | Dokument, Spezifikation oder Anforderung reviewen |
| `/confluence-space-audit` | Confluence-Spaces auditieren |
| `/create-workorder` | Neue Workorder-Spezifikation erstellen |
| `/meeting-summary` | Strukturierte Meeting-Zusammenfassung erstellen |
| `/document-comparison` | Dokument-Vergleich und Gap-Analyse |
| `/requirements-analysis` | Anforderungen auf Vollständigkeit und Testbarkeit prüfen |
| `/workday-goal-awareness` | Aufgabe gegen Workday Goals 2026 abgleichen |
| `/cognitive-continuity-context-transfer` | Kontext zwischen Sessions übertragen |
| `/save-session` | Ergebnisse + Denkprozess für nächste Session speichern |
| `/remember` | Learnings persistent als Memory speichern |

### Verfügbare Skills (automatisch aktiv, aber explizit nennbar)

| Skill | Wann relevant |
|---|---|
| `knowledge-retrieval` | Interne Suche: Confluence, Jira, SharePoint, OneDrive |
| `schreibstil` | Jeder Text, der User zugeordnet wird |

### Vault Knowledge Base (MCP: `vault-mcp`)

Bei Fragen zu SHACL, Spec-Driven Development oder domänenspezifischen Themen **zuerst den Vault durchsuchen** (`vault_search` / `vault_context`), bevor Confluence oder Jira angesteuert werden.

### Verfügbare Agents (`@`-Befehle)

| Agent | Wann verwenden |
|---|---|
| `@architect` | Architekturentscheidungen, ADRs, NFRs, Systemkonsistenz |
| `@developer` | Implementierung, Code schreiben, Tests |
| `@critical-thinker` | Annahmen hinterfragen, blinde Flecken aufdecken, Reflexion erzwingen |
| `@doublecheck` | AI-Output auf Faktengenauigkeit prüfen, Quellen finden, Risiken flaggen |
| `@adr-generator` | ADR-Dokumente nach Schema erstellen |

### Automatisch aktive Instructions (immer geladen)

| Instruction | Scope |
|---|---|
| `response-style` | Alle Antworten — Sprache, Struktur, Ton |
| `spec-driven` | Workorders, ADRs, Reports — Frontmatter + Versioning |
| `jira-integration` | Alle Jira-Aktionen via MCP |
| `confluence-integration` | Alle Confluence-Aktionen via MCP |
| `python` | Alle `.py`-Dateien |
| `markdown` | Alle `.md`-Dateien |
| `context-engineering` | Generelle Copilot-Kontextregeln |
| `copilot-customization` | Standards für Prompt/Agent/Instruction/Skill-Dateien |

## Schritt 3: Empfehlung ausgeben

Gib eine kurze Empfehlung:

- **Passen Prompts zur Aufgabe?** → Nenne sie. Frage: "Soll ich mit `/prompt-name` arbeiten?"
- **Brauchen wir Domänenwissen?** → Vault zuerst (`vault_search`), dann Confluence/Jira
- **Brauchen wir Kontext aus Jira/Confluence?** → Hinweis auf `knowledge-retrieval` + Jira/Confluence MCP
- **Ist Text für User zu formulieren?** → `schreibstil`-Skill aktivieren
- **Nichts passt** → Direkt starten, Pfad und Ausgabeort nennen

## Schritt 4: Starten oder abklären

Wenn alles klar ist: Aufgabe direkt angehen.
Wenn etwas fehlt: Eine gezielte Frage stellen.

