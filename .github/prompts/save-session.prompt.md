---
description: "Session-Ergebnisse und Denkprozess persistent speichern — leichtgewichtige Brücke zur nächsten Session."
---

# Save Session

Sichere den Arbeitsstand dieser Session als persistenten Kontext für die nächste Session.

## Was du tust

1. **Active Context aktualisieren** — Schreibe `/memories/repo/active-context.md` mit dem aktuellen Stand
2. **Thought Process protokollieren** — Erfasse nicht nur WAS, sondern WARUM

## Vorgehen

### Schritt 1: Session analysieren

Gehe den bisherigen Gesprächsverlauf durch und extrahiere:

- **Ergebnisse:** Was wurde konkret erreicht? (Dateien, Entscheidungen, Erkenntnisse)
- **Denkprozess:** Welche Alternativen wurden erwogen? Warum wurde X statt Y gewählt?
- **Offene Fragen:** Was ist ungeklärt, braucht Follow-up oder User-Entscheidung?
- **Nächste Schritte:** Was sollte als nächstes passieren?

### Schritt 2: Active Context schreiben

Aktualisiere `/memories/repo/active-context.md` mit folgendem Format:

```markdown
# Active Context

Persistenter Arbeitskontext zwischen Sessions. Wird von `/save-session` geschrieben und von `/start` gelesen.

## Aktueller Fokus

- [2-4 Bullet Points: Woran wird gerade gearbeitet?]

## Letzte Ergebnisse

### Session {DATUM}: {Thema}
- **Entscheidung:** [Kernentscheidung in einem Satz]
- **Denkprozess:** [Warum so und nicht anders? Welche Alternativen verworfen?]
- **Artefakte:** [Welche Dateien erstellt/geändert?]

[Vorherige Sessions beibehalten, neueste oben, älteste unten. Kein Rotationslimit.]

## Offene Fragen

- [Ungeklärte Punkte, die Follow-up brauchen]

## Nächste Schritte

- [Konkrete nächste Aktionen]
```

### Schritt 3: Learnings extrahieren

Prüfe ob einzelne Erkenntnisse aus der Session als dauerhafte Learnings geeignet sind:
- **Ja** → Zusätzlich via `/remember`-Logik in die passende Memory-Domain schreiben
- **Nein** → Active Context reicht als Brücke

### Schritt 4 (optional): Wiki-Rückschrieb vorschlagen

Prüfe den Session-Inhalt: Gibt es Erkenntnisse, die ...
- **nicht nur sessionspezifisch** sind (≠ active-context)
- **kein reines Tool-/Prozess-Pattern** sind (≠ /remember)
- sondern **wiederverwendbares Domänenwissen** darstellen — etwas, das man in 6 Monaten noch nachschlagen will?

Wenn ja → Schlage explizit vor:
```
→ /wiki-write [domain] [Titel] — [1-Satz-Begründung warum es Wiki-würdig ist]
```

Wenn nein → Schritt überspringen, kein Kommentar.

**Dreiteilung der Write-Ziele:**
| Was | Tool | Ziel |
|---|---|---|
| Session-Stand, Denkprozess, offene Fragen | `/save-session` | `active-context.md` (flüchtig, rotiert) |
| Tool-Patterns, MCP-Eigenheiten, Prozesse | `/remember` | `*-memory.md` (persistent, auto-loaded) |
| Destilliertes Domänenwissen mit Provenance | `/wiki-write` | `wiki/**` (akkumulierend, durchsuchbar) |

### Regeln

- **Kürze über Vollständigkeit:** Active Context ist kein Transcript. Max. 10 Zeilen pro Session-Eintrag.
- **Denkprozess ist Pflicht:** Jede Entscheidung braucht ein "Warum". Ohne Begründung fehlt der Transfer-Wert.
- **Keine Rotation:** Alle Session-Einträge bleiben erhalten. Neueste oben, älteste unten. Die Datei wächst — das ist gewollt.
- **Keine Secrets:** Keine Tokens, Passwörter oder personenbezogene Daten.
- **Sofort schreiben:** Nicht fragen ob geschrieben werden soll — einfach tun. Der User hat `/save-session` explizit aufgerufen.

## Abschluss

Nach dem Schreiben: Kurze Bestätigung was gespeichert wurde. Kein Prosa.

