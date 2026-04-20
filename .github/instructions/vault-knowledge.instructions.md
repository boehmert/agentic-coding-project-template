---
description: "Recherche-Reihenfolge, Vault-Tools, wiki/-Regeln und Referenzdokumente für die Knowledge Base."
applyTo: "**"
priority: recommended
---

# Vault Knowledge Base & Recherche

Regeln für Wissensrecherche im Workspace — Vault, wiki/, Workspace-Dateien und externe Systeme.

---

## 1. Recherche-Reihenfolge (Pflicht)

1. `vault_search` / `vault_context` — Vault zuerst
2. `wiki/` — LLM-generierte Wissens-Snippets mit Provenance (durchsuchen via `grep_search` oder `file_search`)
3. Workspace-Dateien (`context/`) — lokales Wissen

---

## 2. Vault-MCP-Server (`vault-mcp`)

Kuratierter Obsidian-Vault mit Dokumenten zu Prozessen, Agent-Definitionen und Spec-Driven Development.

### Vault-Tools

| Tool | Verwendung |
|---|---|
| `vault_search` | Volltext-Suche (Stichwörter auf Englisch effektiver) |
| `vault_context` | Aufbereiteter Kontext-Block für Prompt-Anreicherung |
| `vault_get` | Einzeldokument per `doc_id` laden |
| `vault_list` | Alle Dokumente auflisten, filterbar nach Tag/Typ |
| `vault_related` | Verlinkte Dokumente traversieren (`related:` / `up:`) |

### Nutzungsregeln

- Suchanfragen auf Englisch formulieren (Vault ist überwiegend englischsprachig)
- Immer **Dokument-ID und Titel** als Quelle nennen
- Bei `Draft`-Dokumenten auf Unsicherheiten hinweisen
- Widersprüche Vault ↔ Workspace-Dateien: **Workspace hat Vorrang** (aktueller)
- **Nicht fragen, ob der Vault durchsucht werden soll** — einfach tun

---

## 3. wiki/-Regeln

- `wiki/` enthält LLM-generierte Snippets — immer `status` und `confidence` aus dem Frontmatter beachten
- `status: draft` + `reviewed_by: null` = **ungeprüft**. Nur zur Orientierung, nicht als Fakt zitieren
- `status: reviewed` oder `stable` = geprüft, verlässlich
- Widersprüche wiki/ ↔ context/: **context/ hat Vorrang** (manuell kuratiert, stabiler)
- Index-Einstieg: `wiki/_INDEX.md` für schnellen Überblick
- Neue Snippets nur via `/wiki-write`-Prompt erstellen — nie manuell

