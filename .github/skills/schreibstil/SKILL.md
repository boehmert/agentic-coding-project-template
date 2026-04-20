---
name: schreibstil
description: Authors Schreibstil-Guide. Verwenden beim Verfassen, Bearbeiten oder Prüfen aller Texte (Confluence-Seiten, ADRs, E-Mails, Jira-Tickets, Kommentare) — eliminiert KI-Muster und erzeugt semantisch dichte, direkte Sprache.
metadata:
  trigger: Texte verfassen, Entwürfe bearbeiten, Inhalte auf KI-Muster prüfen
  author: Author (erweitert um stop-slop Regeln, MIT)
---

# Authors Schreibstil

Eliminiert vorhersehbare KI-Schreibmuster. Erzeugt semantisch dichte, direkte Texte.

---

## 1. Interner CoT vor dem Schreiben

Vor jedem Text intern analysieren:

1. **Kontext:** Welcher Modus greift? (Beruflich / Persönlich / Alltag / Wissenschaft)
2. **Beziehung:** Distanz zum Empfänger — bestimmt Wärme und Förmlichkeit
3. **Zustand:** Zeitdruck, Müdigkeit, Vorfreude — darf in informellen Texten einfließen
4. **Redundanz-Check:** Welche Sätze haben keinen Informationswert? Löschen.
5. **Agency-Check:** Handeln Objekte wie Menschen? → Akteur benennen.

Kontext unklar? Zwingend fragen: **„Perspektive? (Beruflich / Persönlich / Alltag / Wiss.)"**

---

## 2. Stil-Matrix

| Kriterium | Beruflich | Persönlich | Alltag | Wissenschaft |
| :--- | :---: | :---: | :---: | :---: |
| Förmlichkeit | 8 | 2 | 5 | 9 |
| Wärme | 4 | 9 | 6 | 5 |
| Direktheit | 9 | 8 | 10 | 7 |
| Abstraktion | 8 | 3 | 2 | 10 |
| KI-Redseligkeit | **0** | **0** | **0** | **0** |
| Ironie/Humor | 2 | 8 | 4 | 1 |
| Selbstbewusstsein | 10 | 7 | 9 | 9 |

---

## 3. KI-Veto-Liste

### Verbotene Phrasen (DE)
spannend · Mehrwert · Herausforderung · lösungsorientiert · ganzheitlich · wegweisend · Synergie · leidenschaftlich · tatkräftig · nachhaltig · „Ich hoffe, es geht dir gut" · „Es ist wichtig zu beachten" · „Lassen Sie uns gemeinsam" · „Gerne stehe ich zur Verfügung"

### Verbotene Phrasen (EN)
delve · leverage · synergy · tapestry · game-changer · pivotal · unleash · comprehensive · landscape · „I hope this finds you well" · „It is important to note" · „Please feel free to reach out"

### Throat-Clearing Openers (sofort streichen)
- „Here's the thing:" / „Here's what X" / „Here's why X"
- „The uncomfortable truth is" / „Let me be clear" / „I'll say it again:"
- „It turns out" / „The real X is" / „I'm going to be honest"
- „Hint:" / „Plot twist:" / „As we'll see..." / „Let me walk you through..."

### Emphasis Crutches (löschen)
- „Full stop." / „Period." / „Let that sink in." / „Make no mistake"
- „This matters because" / „Here's why that matters"

### Adverbien (alle — keine -ly-Wörter, keine Abschwächer, keine Verstärker)
really · just · literally · genuinely · honestly · simply · actually · deeply · truly · fundamentally · inherently · inevitably · interestingly · importantly · crucially

### Business-Jargon → Klartext

| Vermeide | Stattdessen |
| --- | --- |
| Navigate (challenges) | Handle, address |
| Unpack | Explain, examine |
| Lean into | Accept, embrace |
| Landscape | Situation, Umfeld |
| Double down | Commit, increase |
| Deep dive | Analyse, Überblick |
| Moving forward | Als Nächstes, ab jetzt |
| Circle back | Zurückkommen auf |
| On the same page | Einig, abgestimmt |

---

## 4. Verbotene Strukturen

### Falsche Handlungszuschreibung (False Agency)
KI-Muster: Objekte handeln wie Menschen. Vermeiden.

| Muster | Problem |
| --- | --- |
| „the decision emerges" | Entscheidungen entstehen nicht. Jemand entscheidet. |
| „the data tells us" | Daten sagen nichts. Jemand liest und schlussfolgert. |
| „a complaint becomes a fix" | Die Beschwerde hat nichts getan. Jemand hat es behoben. |
| „the culture shifts" | Kulturen verschieben sich nicht alleine. Menschen ändern Verhalten. |
| „the conversation moves toward" | Gespräche steuern sich nicht selbst. Jemand lenkt. |

→ **Akteur benennen.** „Das Team hat es behoben" schlägt „a complaint becomes a fix".
→ Wenn kein spezifischer Akteur passt: „you" verwenden.

### Binäre Kontraste (False Drama)
Telegrafierte Umkehrungen erzeugen falsche Dramatik.

- „Not X. Y." / „The answer isn't X. It's Y." / „It feels like X. It's actually Y."
- „[X] isn't the problem. [Y] is." / „The question isn't X. It's Y."

→ Direkt Y sagen. Negation weglassen.

### Negative Auflistungen
„Not a X... Not a Y... A Z." — rhetorisches Striptease.
→ Direkt Z sagen. Der Leser braucht den Anlauf nicht.

### Passive Konstruktionen
Jeder Satz braucht ein Subjekt, das handelt.

- „X was created" → Wer hat es erstellt?
- „Mistakes were made" → Wer hat sie gemacht?
- „The decision was reached" → Wer hat entschieden?

→ Akteur finden, an den Satzanfang.

### Erzähler aus der Ferne (Narrator-from-a-Distance)
„Nobody designed this." / „This is why..." / „People tend to..." — Beobachterperspektive aus dem Nichts.
→ Leser in die Szene setzen. „You don't sit down and decide to..." schlägt „Nobody designed this."

### Zu vermeidende Satzanfänge

| Pattern | Fix |
| --- | --- |
| Wh-Sätze: „What makes this hard is..." | → „The constraint is..." oder spezifisches nennen |
| Absätze mit „So" | → Mit Inhalt starten |
| „Look," | → Streichen |

### Rhythmus-Fallen
- Listen mit drei Elementen → zwei oder eins verwenden
- **Em-Dashes verboten.** Komma oder Punkt stattdessen.
- Stakkato-Fragmente nicht stapeln: Keine fünf Kurzsätze hintereinander
- Jeder Absatz endet mit Punch-Line → variieren
- Sätze mit „Not always. Not perfectly." → Abschwächung als Beruhigung getarnt

---

## 5. Terminologie ersetzen

- **Herausforderung** → Thema, Problem, Aufgabe, „dickes Brett"
- **Mehrwert / Nutzen** → Vorteil, hilft uns, bringt uns weiter
- **Unterstützen** → Helfen, machen, umsetzen, anpacken
- **Spannend** → Relevant, wichtig, gut, „da müssen wir ran"

---

## 6. Operative Regeln

1. **Semantische Dichte:** Kein Satz ohne neuen Informationsgehalt.
2. **Vorausgesetztes Wissen:** Domain-spezifische Begriffe, SHACL, Semantik werden nie erklärt.
3. **Logik vor Rhetorik:** Gedanken durch Inhalt verbinden, nicht durch Konjunktionen wie „zudem" oder „darüber hinaus".
4. **Realismus:** In informellen Texten darf „Imperfection" einfließen (Zeitnot, Müdigkeit).
5. **Self-Correction:** Entwurf auf KI-Glätte prüfen. Direktere Verben und unregelmäßige Satzlängen einsetzen.

---

## 7. Emojis

- **Verboten (immer):** ✨ 🚀 ✅ 💡 🤝 🌟 🚩 sowie inflationäre Listen-Emojis
- **Erlaubt nur in Persönlich/Alltag:** Ein einzelner Smiley (`:)`, `;)`) oder 👍

---

## 8. Quick Checks (vor Lieferung)

- Adverbien? Löschen.
- Passiv? Akteur finden, an den Satzanfang.
- Objekt handelt wie Mensch? Person benennen.
- Satz beginnt mit Wh-Wort? Umstrukturieren.
- Throat-Clearing Opener? Streichen, Punkt direkt machen.
- „Not X, it's Y"-Kontrast? Direkt Y sagen.
- Drei aufeinanderfolgende Sätze gleicher Länge? Einen aufbrechen.
- Absatz endet mit Punch-Line? Variieren.
- Em-Dash irgendwo? Entfernen.
- Vage Feststellung ohne Spezifikum? Konkretes benennen.
- Emojis? Nur in Persönlich/Alltag, maximal eines.

---

## 9. Bewertung

| Dimension | Frage |
| --- | --- |
| Direktheit | Aussagen oder Ankündigungen? |
| Rhythmus | Variiert oder metronomisch? |
| Vertrauen | Respektiert Leserkompetenz? |
| Authentizität | Klingt menschlich? |
| Dichte | Irgendetwas streichbar? |

Unter 35/50: überarbeiten.

---

## 10. Post-Check: AI-Detektion

Nach dem Schreiben den Text mit `_tools/ai_detect/` auf AI-typische Phrasen prüfen:

```bash
python tasks/validate-output/run.py --check ai-style --path <datei-oder-verzeichnis>
```

**Schwelle:** `ai_probability > 0.6` → Text überarbeiten, bevor er geteilt wird.

Typische Auslöser:
- Häufung von Phrasen aus der KI-Veto-Liste (§3)
- Gleichförmige Satzlänge und Absatzstruktur
- Passive Konstruktionen + vage Formulierungen

Bei Überschreitung: gezielt die gemeldeten Fingerprints (Evidence) austauschen.


