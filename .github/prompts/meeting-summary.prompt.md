---
description: "Erstellt eine strukturierte Meeting-Zusammenfassung mit Entscheidungen, Action Items und offenen Fragen."
---

Erstelle eine strukturierte Zusammenfassung des folgenden Meetings / der folgenden Diskussion.

## Input

{{input}}

## Ausgabeformat

```markdown
## Meeting Summary
**Date:** [YYYY-MM-DD]
**Participants:** [Liste, falls bekannt]
**Context:** [1-2 Sätze]

### Key Decisions
- [Entscheidung 1]
- [Entscheidung 2]

### Action Items
- [ ] [Aktion] – Owner: [Name], Due: [Datum falls genannt]

### Open Questions
- [Frage 1]

### Next Steps
- [Schritt 1]
```

## Regeln

1. Entscheidungen separat von Diskussionen extrahieren
2. Action Items mit Checkboxen und Owner markieren
3. Offene Fragen explizit flaggen
4. 80% Signal, 20% Kontext — keine Wiederholung von Diskussionsverläufen
5. Kritische Zitate mit Zuschreibung erhalten
6. Sprache des Inputs matchen (Deutsch → Deutsch, Englisch → Englisch)

