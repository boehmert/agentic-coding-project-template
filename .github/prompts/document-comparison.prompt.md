---
description: "Vergleicht zwei Dokumente oder Versionen und erstellt eine Gap-Analyse mit Handlungsempfehlung."
---

Vergleiche die folgenden Dokumente und erstelle einen strukturierten Vergleichsbericht.

## Dokumente

{{documents}}

## Ausgabeformat

```markdown
## Document Comparison Report

### Documents Compared
- **Document A:** [Name, Version, Datum]
- **Document B:** [Name, Version, Datum]

### Structural Differences
- [Sektion hinzugefügt/entfernt/umbenannt]

### Content Changes

#### Added in B
- [Sektion/Konzept mit Referenz]

#### Removed from A
- [Sektion/Konzept mit Referenz]

#### Modified
- **Thema:** [Was sich geändert hat]
  - Vorher: [Zusammenfassung]
  - Nachher: [Zusammenfassung]
  - Impact: [Bedeutung]

### Consistency Issues
- [Terminologie-Konflikte]
- [Widersprüche]

### Recommendation
[Welche Version bevorzugen und warum, oder Merge-Strategie]
```

## Regeln

1. Strukturelle Änderungen vor inhaltlichen
2. Bei jeder Änderung den Impact bewerten
3. Terminologie-Konflikte und Widersprüche explizit benennen
4. Handlungsempfehlung mit Begründung

