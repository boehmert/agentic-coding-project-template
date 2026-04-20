---
name: Wiki Write
description: "Schreibt einen destillierten Wissens-Snippet aus der aktuellen Session in wiki/ zurück. Syntax: /wiki-write [domain] [Titel]"
mode: agent
---

# Wiki Write

Destilliere eine Erkenntnis aus der Session und persistiere sie als Wissens-Snippet in `wiki/` — mit vollständiger Provenance.

## Wann verwenden?

Verwende diesen Prompt wenn eine Erkenntnis:
- **nicht nur sessionspezifisch** ist (→ dafür: `/save-session`)
- **kein reines Tool-Pattern** ist (→ dafür: `/remember`)
- sondern **wiederverwendbares Domänenwissen** darstellt, das zukünftige Sessions bereichert

## Input

```
/wiki-write [domain] [Titel]
```

**Domains:** `agentic-coding` | `your-project` | `your-domain` | `team-process` | `personal`

**Beispiele:**
- `/wiki-write agentic-coding Vibe Engineering Zutaten (Caudal)`
- `/wiki-write your-project SHACL Validierungspattern für Controlled Vocabularies`

---

## Schritte

### 1. Nächste freie ID ermitteln

Lese `wiki/_INDEX.md` und ermittle die nächste freie ID im Format `KB-YYYY-NNN`.

### 2. Inhalt destillieren

Extrahiere aus dem Gesprächsverlauf den Kern der Erkenntnis:
- Keine Chat-Kontext-Referenzen ("wie oben erwähnt...")
- Kein Padding
- Direkt verwendbar als Nachschlage-Snippet
- Mit konkreten Beispielen oder Quellen wo vorhanden

### 3. Datei erstellen

Erstelle `wiki/{domain}/KB-{YYYY}-{NNN}_{slug}.md` mit folgendem Aufbau:

```markdown
---
id: KB-YYYY-NNN
title: "Exakter Titel"
domain: {domain}
source_type: llm-generated        # human | llm-generated | deep-research | meeting-extract | jira-export
confidence: medium                 # high | medium | low | uncertain
created: YYYY-MM-DD
created_by: copilot                # User | copilot | deep-research | agent-name
session_context: "Kurze Beschreibung der Session/des Anlasses"
related_to: []                     # [KB-YYYY-NNN, WOxx]
sources: []                        # URLs, Confluence-Seiten, Dateipfade
reviewed_by: null                  # null = draft / User = geprüft
status: draft                      # draft | reviewed | stable | outdated
---

# {Titel}

## Kernaussage

[1-3 Sätze: Was ist die zentrale Erkenntnis?]

## Details

[Ausführlichere Erklärung, Kontext, Beispiele]

## Relevanz für Team-

[Warum ist das für Users Arbeit relevant?]

## Quellen

[Links, Confluence-Seiten, Dateipfade]
```

### 4. Index aktualisieren

Füge den neuen Snippet in `wiki/_INDEX.md` ein:
- Tabelle „Alle Snippets" um eine Zeile ergänzen
- Domain-Zähler in der Domain-Tabelle hochsetzen

### 5. Abschluss

Zeige dem User:
```
✓ KB-YYYY-NNN erstellt: wiki/{domain}/KB-YYYY-NNN_{slug}.md
  Status: draft — setze reviewed_by: User nach Prüfung
```

