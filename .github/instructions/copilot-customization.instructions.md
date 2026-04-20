---
description: "Qualitätsstandards für Prompt-, Agent-, Instruction- und Skill-Dateien im Team-Workspace."
applyTo: "**/*.prompt.md, **/*.agent.md, **/*.instructions.md, **/SKILL.md"
priority: optional
---

# Copilot Customization Standards

Standards für alle Copilot-Konfigurationsdateien in diesem Workspace. Destilliert aus GitHub Copilot Docs, Awesome Copilot Best Practices und Projekt-Erfahrung.

---

## 1. Datei-Typen und Orte

| Typ | Endung | Ort | Zweck |
|-----|--------|-----|-------|
| Prompt | `.prompt.md` | `.github/prompts/` | Wiederverwendbare Aufgaben (`/name`) |
| Agent | `.agent.md` | `.github/agents/` | Spezialisierte Rollen (`@name`) |
| Instruction | `.instructions.md` | `.github/instructions/` | Automatisch aktive Regeln per `applyTo` |
| Skill | `SKILL.md` | `.github/skills/<name>/` | Domänenwissen mit Assets |

---

## 2. Frontmatter (Pflicht)

### Prompts
```yaml
---
description: "Kurze Beschreibung der Aufgabe (50-150 Zeichen)"
---
```

### Agents
```yaml
---
description: "Rolle und Kernkompetenz (50-150 Zeichen)"
name: "Display Name"
tools: [read/readFile, search/textSearch, web/fetch]
---
```

### Instructions
```yaml
---
description: "Was diese Regeln tun (50-150 Zeichen)"
applyTo: "**/*.py"
---
```

### Regeln
- `description` ist Pflicht, in Anführungszeichen
- `applyTo` nutzt Glob-Patterns: `**/*.py`, `**/*.md`, `**`
- `tools` nur die tatsächlich benötigten auflisten (Least Privilege)
- `name` bei Agents optional, aber empfohlen

---

## 3. Prompt-Qualität

### Struktur
- **Imperativ verwenden:** "Analysiere", "Prüfe", "Erstelle" — nicht "Du könntest..."
- **Ein Ziel pro Prompt:** Nicht mehrere unabhängige Aufgaben bündeln
- **Phasen/Schritte nummerieren** wenn der Workflow sequentiell ist
- **Kontext vor Aktion:** Erst laden was gebraucht wird, dann handeln

### Klarheit
- **Spezifisch statt abstrakt:** Konkrete Dateipfade, Feldnamen, Beispiele
- **Grenz-Bedingungen definieren:** Was ist in-scope, was nicht
- **Ausgabeformat beschreiben:** Wie soll das Ergebnis aussehen
- **Erfolgskriterien benennen:** Wann ist die Aufgabe erledigt

### Vermeiden
- Vage Formulierungen ("sollte", "vielleicht", "bei Bedarf")
- Widersprüchliche Anweisungen innerhalb einer Datei
- Referenzen auf nicht-existierende Dateien oder Tools
- Überlange Dateien (>200 Zeilen → aufteilen oder kürzen)

---

## 4. Agent-Design

### Rollenklarheit
- **Eine Rolle pro Agent.** Nicht Analyst + Developer + Reviewer in einem.
- **Abgrenzung definieren:** Was ist NICHT Verantwortung dieses Agents
- **Ergänzung statt Überlappung:** Prüfe gegen bestehende Agents vor Erstellung

### Tool-Auswahl
- Nur Tools listen, die der Agent tatsächlich braucht
- Read-only Agents: `read/readFile`, `search/*`, `web/fetch`
- Write-Agents: zusätzlich `edit/editFiles`, `execute/runInTerminal`
- MCP-Tools: `your-jira/*`, `your-confluence/*` nur wenn Jira/Confluence-Zugriff nötig

### Kontext-Management
- Relevante Workspace-Dateien im Agent-Body referenzieren (nicht im Frontmatter)
- `context/your-project/`, `context/your-domain/` für Domänenwissen
- `context/team/dor/` für Prozesswissen

---

## 5. Instructions-Design

### Scope per applyTo
- `**` → gilt für alle Dateien (sparsam verwenden)
- `**/*.py` → nur Python-Dateien
- `**/*.md` → nur Markdown
- `**/*.agent.md, **/*.prompt.md` → nur Copilot-Konfiguration

### Inhalt
- Kurze, scanbare Regeln (Bullet Points)
- Positive Formulierung bevorzugen ("Verwende X" statt "Vermeide Y")
- Konkrete Beispiele (Good/Bad) wo nötig
- Kein Tutorial-Stil — nur Regeln und Patterns

---

## 6. Namenskonventionen

| Element | Format | Beispiel |
|---------|--------|----------|
| Prompt-Datei | `kebab-case.prompt.md` | `jira-review.prompt.md` |
| Agent-Datei | `kebab-case.agent.md` | `critical-thinker.agent.md` |
| Instruction-Datei | `kebab-case.instructions.md` | `python.instructions.md` |
| Skill-Ordner | `kebab-case/SKILL.md` | `knowledge-retrieval/SKILL.md` |

---

## 7. Wartung

- Prompts prüfen wenn sich referenzierte Dateien ändern
- Veraltete Referenzen (Pfade, Tool-Namen) sofort korrigieren
- `/start`-Prompt aktualisieren wenn Prompts/Agents hinzukommen oder entfallen
- Bei >15 Prompts oder >5 Agents: Konsolidierung prüfen

