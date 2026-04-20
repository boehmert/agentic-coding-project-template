---
description: "Analysiert Anforderungen auf Vollständigkeit, Testbarkeit, Klarheit und Risiken."
---

Analysiere die folgenden Anforderungen und erstelle einen strukturierten Analysebericht.

## Anforderungen

{{requirements}}

## Ausgabeformat

```markdown
## Requirements Analysis

### Coverage Check
- [ ] Funktionale Anforderungen definiert?
- [ ] Nicht-funktionale Anforderungen (Performance, Security)?
- [ ] Benutzerrollen und Berechtigungen klar?
- [ ] Datenanforderungen spezifiziert?
- [ ] Integrationspunkte identifiziert?
- [ ] Fehlerbehandlungs-Szenarien abgedeckt?

### Quality Assessment

#### Testability
⚠️ **Nicht testbar:**
- [Anforderung mit vager Formulierung]
- Vorschlag: [Wie testbar machen]

✅ **Gut definiert:**
- [Gutes Beispiel]

#### Completeness
Fehlende Elemente:
- [Lücke 1 mit Impact]

#### Clarity
Mehrdeutige Begriffe:
- "[Begriff]" in Sektion X – könnte bedeuten: [Interpretation 1] oder [Interpretation 2]

### Risk Assessment
- 🔴 **High Risk:** [Element mit Begründung]
- 🟡 **Medium Risk:** [Element mit Begründung]
- 🟢 **Low Risk:** [Element]

### Recommendations
1. [Kritischste Lücke]
2. [Wichtigste Verbesserung]
3. [Nice-to-have Klärung]
```

## Regeln

1. Jede Anforderung auf Testbarkeit prüfen — vage Formulierungen flaggen
2. Fehlende Elemente mit konkretem Business-Impact benennen
3. Mehrdeutige Begriffe mit möglichen Interpretationen auflisten
4. Risiken priorisiert (🔴 → 🟡 → 🟢) darstellen
5. Empfehlungen nach Priorität sortieren

