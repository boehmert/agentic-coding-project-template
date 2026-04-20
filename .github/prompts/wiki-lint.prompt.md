---
name: Wiki Lint
description: "Health-Check für wiki/: Inkonsistenzen finden, Lücken identifizieren, neue Snippet-Kandidaten vorschlagen. Empfohlen: monatlich."
mode: agent
---

# Wiki Lint

Führe einen strukturierten Qualitäts-Check über die gesamte `wiki/` durch.

## Wann verwenden?

- Monatlich als Routine-Check
- Nach größeren Sessions mit vielen neuen Snippets
- Wenn der Verdacht besteht, dass Inhalte veraltet oder inkonsistent sind

---

## Schritte

### 1. Index lesen

Lese `wiki/_INDEX.md` — Gesamtüberblick aller Snippets.

### 2. Snippets stichprobenartig prüfen

Lese 10-15 Snippets (bevorzugt ältere und solche mit `status: draft`) und prüfe:

**Duplikat-Check:**
- Gibt es zwei Snippets zum gleichen Thema?
- Können sie zusammengeführt werden?

**Aktualitäts-Check:**
- Sind Fakten noch korrekt? (z.B. Framework-Versionen, Team-Prozesse)
- Snippets älter als 6 Monate mit `status: draft` → auf `outdated` setzen?

**Konsistenz-Check:**
- Widersprechen sich zwei Snippets inhaltlich?
- Fehlende `related_to`-Verweise zwischen offensichtlich verwandten Snippets?

**Vollständigkeits-Check:**
- Fehlen wichtige Quellen oder Beispiele?
- Sind `sources` befüllt?

### 3. Lücken identifizieren

Aus den vorhandenen Snippets: Welche Themen werden oft referenziert (`related_to`, `sources`), haben aber noch keinen eigenen Snippet?

### 4. Neue Snippet-Kandidaten vorschlagen

Schlage 3-5 neue Snippets vor, die sich aus vorhandenen Inhalten ergeben:
- Verbindungen zwischen bisher unverbundenen Snippets
- Vertiefungen von `confidence: low`-Snippets
- Nächste Schritte aus offenen Erkenntnissen

### 5. Ergebnis schreiben

Erstelle `wiki/_LINT_REPORT.md`:

```markdown
---
generated: YYYY-MM-DD
checked_snippets: N
---

# Wiki Lint Report – YYYY-MM-DD

## Zusammenfassung
- Geprüfte Snippets: N
- Gefundene Probleme: N
- Vorgeschlagene neue Snippets: N

## Probleme

### Duplikate
...

### Veraltete Snippets
...

### Inkonsistenzen
...

### Fehlende Links
...

## Neue Snippet-Kandidaten

1. **[Titel]** — Domain: X — Begründung: ...
2. ...

## Empfohlene Aktionen
...
```

### 6. Abschluss

Frage den User, ob vorgeschlagene Änderungen direkt angewendet werden sollen.

