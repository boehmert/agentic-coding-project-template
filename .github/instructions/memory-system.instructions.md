---
description: "Copilot Memory-System: Scopes, Active Context, Session-Workflow und Designentscheidungen."
applyTo: "**"
priority: recommended
---

# Copilot Memory System

Regeln für das eingebaute Memory-System von VS Code Copilot im Team-Workspace.

---

## 1. Übersicht

Das Memory-System speichert Informationen in einem **virtuellen Dateisystem** unter `/memories/`. Die Dateien sind **nicht** im Git-Repo enthalten und **nicht** über den Datei-Explorer sichtbar — Zugriff erfolgt ausschließlich über das Memory-Tool (`view`, `create`, `str_replace`, `insert`, `delete`).

**Physischer Speicherort:** VS Code Workspace Storage (`%APPDATA%/Code/User/workspaceStorage/`). Nicht portabel — wenn der Workspace auf einem anderen Rechner geöffnet wird, fehlen die Repo-Memories dort.

---

## 2. Scopes

| Scope | Pfad | Lebensdauer | Auto-Inject |
|---|---|---|---|
| **User** | `/memories/` | Persistent über alle Workspaces | Ja (erste 200 Zeilen) |
| **Repo** | `/memories/repo/` | Persistent, workspace-gebunden | Nein (manuell lesen) |
| **Session** | `/memories/session/` | Nur aktuelle Konversation | Nein (manuell lesen) |

---

## 3. Aktuelle Dateien in `/memories/repo/`

| Datei | Zweck | Geschrieben von |
|---|---|---|
| `active-context.md` | Arbeitsstand zwischen Sessions: Fokus, Entscheidungen, Denkprozess, offene Fragen | `/save-session` Prompt |
| `mcp-memory.md` | MCP-Server-Eigenheiten, Token-Probleme, Workarounds | `/remember` Prompt |
| `process-memory.md` | Team-Prozesse, PI-Planung, Workflow-Erkenntnisse | `/remember` Prompt |
| `tools-memory.md` | VS Code, Extensions, Copilot-Verhalten | `/remember` Prompt |

---

## 4. Session-Kontinuität (Workflow)

```text
Session-Ende:  /save-session  →  active-context.md aktualisieren
Session-Start: /start {task}  →  Schritt 0 liest active-context.md
Einzellearning: /remember      →  Schreibt in domain-spezifische Memory-Datei
```

**Regel:** Bei komplexen Aufgaben `/memories/repo/active-context.md` lesen (Memory-Tool, `view`). Enthält Arbeitsfokus, letzte Entscheidungen mit Denkprozess und offene Fragen aus vorherigen Sessions. Am Session-Ende bei Bedarf `/save-session` vorschlagen.

---

## 5. Designentscheidung (2026-04-03)

Active Context liegt bewusst in `/memories/repo/` (virtuell) statt als physische Datei im Repo:

- **Pro:** Automatisch im Copilot-Ökosystem, kein Git-Noise, kein Risiko für versehentliches Commit von Arbeitsständen
- **Contra:** Nicht portabel, nicht versioniert, nicht im Backup
- **Mitigation:** Dauerhafte Erkenntnisse werden über `/remember` in Memory-Dateien überführt oder via Promotion-Path in `.instructions.md` befördert. Das Schwergewicht `/cognitive-continuity-context-transfer` steht für vollständige Kontextmigration zur Verfügung.

---

## 6. Konfiguration ändern

Falls der Speicherort in Zukunft geändert werden soll (z.B. auf physische Datei im Repo):

1. Neue Datei anlegen (z.B. `.github/context/active-context.md`)
2. `/save-session` Prompt anpassen: Ziel von Memory-Tool auf `create_file`/`replace_string_in_file` ändern
3. `/start` Prompt anpassen: Schritt 0 von Memory-`view` auf `read_file` ändern
4. Pflichtregeln in `copilot-instructions.md` aktualisieren
5. `.gitignore` prüfen (soll die Datei committed werden oder nicht?)

