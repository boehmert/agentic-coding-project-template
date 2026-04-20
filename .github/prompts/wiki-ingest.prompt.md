---
name: Wiki Ingest
description: "Liest eine Quelldatei aus inbox/ und destilliert daraus 1-3 Wissens-Snippets in wiki/. Die Karpathy raw/ → wiki/ Pipeline. Syntax: /wiki-ingest [Pfad] [domain]"
mode: agent
---

# Wiki Ingest

Verarbeite eine Quelldatei und extrahiere daraus destillierte, wiederverwendbare Wissens-Snippets für `wiki/`.

## Wann verwenden?

Wenn eine Quelldatei in `inbox/` relevantes Wissen enthält, das:
- zu groß oder zu roh ist um es direkt zu nutzen
- wiederholt referenziert werden wird
- durch Destillation an Nützlichkeit gewinnt

**Typische Quellen:**
- Artikel aus `inbox/docs/` (Word, Markdown, PDF-Extrakte)
- Transkripte aus `inbox/Transcripts/` oder `inbox/Team-Meetings_md/`
- Forschungsergebnisse, externe Reports
- Confluence-Seiteninhalte die lokal verfügbar gemacht wurden

## Input

```
/wiki-ingest [Pfad zur Quelldatei] [domain]
```

**Beispiele:**
- `/wiki-ingest inbox/docs/karpathy-llm-wiki.md agentic-coding`
- `/wiki-ingest inbox/Team-Meetings_md/2026-04-sprint-review.md Team-process`
- `/wiki-ingest inbox/rdf-shacl/shacl-patterns.md PROJECT-`

---

## Schritte

### 1. Quelldatei lesen

Lese die angegebene Datei vollständig.

**Sofort prüfen:**
- Enthält die Datei personenbezogene Daten (Namen, E-Mail-Adressen außer Users)? → Anonymisieren oder hinweisen
- Enthält sie interne WK-Daten, die nicht in Git gehören? → `status: draft` + Hinweis an User

### 2. Snippet-Kandidaten identifizieren

Analysiere den Inhalt: Welche Abschnitte sind **wiki-würdig**?

Kriterien:
- Wiederverwendbar in zukünftigen Sessions
- Eigenständig verständlich ohne die Quelldatei
- Nicht rein sessionspezifisch oder ephemer

**Grenzwert:** 1-3 Snippets pro Quelldatei. Lieber zu wenig als zu viele schwache Snippets.

Wenn keine wiki-würdigen Inhalte gefunden → klar kommunizieren und abbrechen.

### 3. source_type bestimmen

| Quelldateityp | source_type |
|---|---|
| Transkript, Meeting-Notizen | `meeting-extract` |
| Externes Paper, Artikel | `deep-research` |
| Jira-Export, Confluence-Export | `jira-export` |
| Manuell geschriebenes Dokument | `human` |
| LLM-generiertes Dokument | `llm-generated` |

### 4. Snippets erstellen

Für jeden Kandidaten:

1. Nächste freie ID aus `wiki/_INDEX.md` ermitteln
2. Datei anlegen: `wiki/{domain}/KB-{YYYY}-{NNN}_{slug}.md`
3. Frontmatter setzen — insbesondere:
   - `source_type` aus Schritt 3
   - `sources: [Pfad zur Quelldatei]`
   - `session_context: "Ingest von {Dateiname}, {Datum}"`
   - `confidence: medium` (Standard für Ingests — User entscheidet ob high)
   - `status: draft`
   - `reviewed_by: null`
4. Inhalt schreiben: Kernaussage, Details, Relevanz für Team-

### 5. Index aktualisieren

Alle neuen Snippets in `wiki/_INDEX.md` eintragen.

### 6. Sensibilitätsprüfung

Vor Abschluss explizit melden:
- Wurden personenbezogene Daten gefunden und behandelt?
- Gibt es Inhalte die **nicht in Git** committed werden sollten? (wiki/ ist bereits in .gitignore)
- Empfehlung: Snippets erst reviewen (`reviewed_by: User` setzen) bevor sie aktiv als Wissensquelle genutzt werden

### 7. Abschluss

```
✓ Ingest abgeschlossen: {N} Snippets erstellt
  Quelle: {Pfad}
  Erstellt: KB-YYYY-NNN, KB-YYYY-NNN+1, ...
  Status: draft — reviewed_by: User setzen nach Prüfung

⚠ Sensibilitätshinweis: {falls relevant}
```

---

## Hinweis zur Qualität

Ingest-Snippets sind oft `confidence: medium`. Das ist korrekt — die Quelldatei ist der Beweis, nicht das Wissen selbst. Erst nach Users Review auf `reviewed` oder `stable` setzen.

