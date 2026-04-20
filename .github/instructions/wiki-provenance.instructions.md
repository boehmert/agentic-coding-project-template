---
description: "Provenance-Schema und Qualitätsregeln für alle Dateien in wiki/**."
applyTo: "wiki/**"
---

# Wiki Provenance Standards

Alle Dateien in `wiki/` sind **LLM-generierte Wissens-Snippets** mit vollständiger Herkunftsdokumentation.

## Pflicht-Frontmatter

Jede Wiki-Datei muss diese YAML-Felder enthalten:

```yaml
---
id: KB-YYYY-NNN                  # Pflicht. Format: KB-{Jahr}-{3-stellige Nummer}
title: "Exakter Titel"            # Pflicht. Entspricht H1 im Dokument
domain: agentic-coding            # Pflicht. Werte: agentic-coding | your-project | your-domain | team-process | personal
source_type: llm-generated        # Pflicht. Werte: human | llm-generated | deep-research | meeting-extract | jira-export
confidence: medium                # Pflicht. Werte: high | medium | low | uncertain
created: YYYY-MM-DD               # Pflicht. ISO-Datum
created_by: copilot               # Pflicht. Werte: User | copilot | deep-research | {agent-name}
session_context: "..."            # Pflicht. Kurzbeschreibung der Session/des Anlasses
related_to: []                    # Optional. Liste von KB-IDs oder WO-IDs
sources: []                       # Optional aber empfohlen. URLs, Dateipfade, Confluence-Seiten
reviewed_by: null                 # null = draft, User = vom Menschen geprüft
status: draft                     # Werte: draft | reviewed | stable | outdated
---
```

## Bedeutung der Felder

### `source_type`

| Wert | Bedeutung |
|---|---|
| `human` | User hat den Inhalt selbst geschrieben |
| `llm-generated` | Copilot hat den Inhalt aus einer Session destilliert |
| `deep-research` | Basiert auf Deep Research (Perplexity, Notebook LM, o.ä.) |
| `meeting-extract` | Aus Transkripten oder Meeting-Notizen extrahiert |
| `jira-export` | Aus Jira-Daten abgeleitet |

### `confidence`

| Wert | Bedeutung |
|---|---|
| `high` | Gut belegte Fakten aus zuverlässigen Quellen |
| `medium` | Plausibel, aber nicht vollständig verifiziert |
| `low` | Annahmen oder schwach belegte Informationen |
| `uncertain` | Ausdrücklich unsicher — braucht Verifikation |

### `status`-Workflow

```
draft         ← Standard bei Erstellung
  ↓ User liest und prüft
reviewed      ← reviewed_by: User gesetzt
  ↓ Inhalte stabil über Zeit
stable        ← Langfristig verlässlich
  ↓ Neue Information macht alt
outdated      ← Nicht mehr aktuell, nicht löschen (historischer Wert)
```

## Qualitätsregeln

1. **Keine Chat-Referenzen** — kein "wie oben erwähnt", "in dieser Session", "du hast gefragt"
2. **Eigenständig lesbar** — Snippet muss ohne Session-Kontext verständlich sein
3. **Kurz und direkt** — Kernaussage in ≤3 Sätzen, Details darunter
4. **Quellen benennen** — Mindestens Confluence-Seite, URL oder Dateipfad
5. **`reviewed_by: null` = Achtung** — Inhalt ist LLM-generiert und ungeprüft

## Neue Snippets erstellen

Verwende `/wiki-write [domain] [Titel]` — nie manuell eine KB-Datei anlegen.

## Index pflegen

Nach jedem `/wiki-write` wird `wiki/_INDEX.md` automatisch aktualisiert.
Manuell nur anfassen wenn der LLM das vergessen hat.

