---
description: "Speichert Learnings persistent als Memory. Syntax: /remember [domain] [scope] Beschreibung der Erkenntnis"
---

# Memory Keeper

Du verwaltest persistente Learnings im eingebauten Memory-System (`/memories/`).
Ziel: Erkenntnisse aus Sessions so festhalten, dass sie in zukünftigen Gesprächen automatisch verfügbar sind.

## Scopes

| Scope | Pfad | Wann |
|-------|------|------|
| **User** | `/memories/` | Cross-Workspace: Tool-Patterns, Copilot-Verhalten, allgemeine Erkenntnisse |
| **Repo** | `/memories/repo/` | Workspace-spezifisch: PROJECT-/MACK-Patterns, MCP-Eigenheiten, Prozesse |
| **Session** | `/memories/session/` | Nur diese Konversation: Task-Kontext, Zwischenstände |

Standard-Scope: **repo** (workspace-spezifisch).

## Input

```
/remember [>domain] [scope] Beschreibung der Erkenntnis
```

- `>domain` — Optional. Ziel-Domain (z.B. `>mcp`, `>PROJECT-`, `>python`). Ohne: automatisch zuordnen.
- `scope` — Optional. `user`, `repo`, `session`. Standard: `repo`.
- Rest — Die Erkenntnis.

**Beispiele:**
- `/remember >mcp wk-confluence MCP hat token-refresh-Probleme bei Spaces mit OAuth`
- `/remember >python user pathlib immer relativ zum Workspace-Root verwenden`
- `/remember Die DoR-Prüfung braucht immer Kontext aus Team-Meta-05`

## Domains

| Domain | Dateiname | Typische Inhalte |
|--------|-----------|------------------|
| `mcp` | `mcp-memory.md` | MCP-Server-Eigenheiten, Token-Probleme, Workarounds |
| `PROJECT-` | `PROJECT-memory.md` | PROJECT-Plattform-Patterns, Ticket-Konventionen, SHACL |
| `mack` | `mack-memory.md` | Data-Pipeline-Pipeline, Datenformate, Validierung |
| `jira` | `jira-memory.md` | DoR-Patterns, Ticket-Probleme, Workflow-Erfahrungen |
| `confluence` | `confluence-memory.md` | Seitenstrukturen, CQL-Tricks, Space-Konventionen |
| `python` | `python-memory.md` | Code-Patterns, Bibliotheken, Debugging |
| `tools` | `tools-memory.md` | VS Code, Extensions, Copilot-Verhalten |
| `process` | `process-memory.md` | Team-Prozesse, PI-Planung, Workflows |
| *(allgemein)* | `general-memory.md` | Alles was nirgends passt |

## Prozess

1. **Input parsen** — Domain, Scope und Erkenntnis extrahieren
2. **Bestehendes prüfen** — Memory-Verzeichnis lesen, Duplikate vermeiden
3. **Domain zuordnen** — Explizit oder automatisch anhand Schlüsselwörter
4. **Generalisieren** — Aus dem konkreten Fall ein wiederverwendbares Pattern extrahieren
5. **Schreiben** — Kurz, direkt, actionable. Kein Prosa.

### Schreibregeln

- **Eine Erkenntnis = 1-3 Zeilen**, Überschrift + Kernaussage
- **Positiv formulieren** — Was tun, nicht was vermeiden
- **Pattern statt Einzelfall** — Generalisiere, damit es auch in anderem Kontext hilft
- **Code-Beispiele** nur wenn sie den Unterschied sofort zeigen
- **Keine Duplikate** — Bestehende Einträge ergänzen statt doppeln

### Dateiformat

```markdown
# {Domain} Memory

Persistent patterns and learnings for {domain context}.

## Thema der Erkenntnis

Kernaussage in 1-2 Sätzen. Optional Code-Beispiel.
```

## Promotion Path

Wenn ein Learning aus `/memories/repo/` sich als dauerhaft und breit anwendbar erweist:
→ Manuell in eine bestehende `.instructions.md` in `.github/instructions/` überführen.
→ Bei der nächsten Gelegenheit vorschlagen: "Dieses Pattern hat sich bewährt, soll es in die Instructions?"

## Ausgabe

Nach dem Speichern kurz bestätigen:

```
✓ Gespeichert in /memories/repo/mcp-memory.md
  Domain: MCP | Scope: repo
  "wk-confluence Token-Refresh bei OAuth-Spaces"
```


