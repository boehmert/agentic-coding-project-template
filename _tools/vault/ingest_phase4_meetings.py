"""Phase 4: Create meeting distillates from selected transcripts and write to Vault."""

import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[2]))

from pathlib import Path
from _tools.vault.ingest_to_vault import (
    slugify,
    WORKSPACE,
    TODAY,
)

VAULT_ROOT = Path(
    r"C:\Users\user\OneDrive - your organization\Dokumente"
    r"\User\knowledge-base\Obsidian Vault\curated"
)


def build_meeting_frontmatter(
    kb_id: str,
    title: str,
    meeting_date: str,
    tags: list[str],
    source_path: str,
    strategic_intent: str,
    participants: str,
    language: str = "en",
) -> str:
    tags_str = ", ".join(f'"{t}"' for t in tags)
    return f"""---
id: {kb_id}
title: "{title}"
document_type: Meeting Distillate
target_index: Team-Expert_curated

# --- Taxonomy & Connectivity ---
tags: [{tags_str}]
aPerson-Bses: []
up: "[[MOC_Start]]"
predecessor: []
successor: []
related: []

# --- Provenance & Traceability ---
framework_version: 1.2.0
created_by: "User Name (AI-destilliert)"
created_at: "{TODAY}"
source_origin: "{source_path}"
meeting_date: "{meeting_date}"
participants: "{participants}"
strategic_intent: "{strategic_intent}"
language: "{language}"

# --- Cognitive Layer ---
cognitive_intent: "Destillat aus Meeting-Transkript: Kernaussagen, Entscheidungen, Action Items."
transfer_score: 7

# --- Quality ---
quality_status: Draft
confidence: 6
---

"""


DISTILLATES = [
    {
        "kb_id": "KB-202604150044",
        "title": "PROJECT- Presentation — User erklaert PROJECT- fuer Tech Forum",
        "meeting_date": "2024-10-18",
        "source": "inbox/Team-Meetings_md/2024-10-18_PROJECT-presentation_transcript.md",
        "tags": ["Team-/PROJECT-", "Team-/presentation", "Team-/onboarding", "Team-/meeting-distillate"],
        "strategic_intent": "Didaktische PROJECT-Erklaerung: MAC vs PROJECT-, Artemis, PCING, Release-Prozess, Team-Struktur.",
        "participants": "User Name, Kees-Jan, Florist (Moderator), Tech Forum (~25 Teilnehmer)",
        "language": "en",
        "content": """# PROJECT- Presentation — Tech Forum, 18.10.2024

> Destillat aus: `2024-10-18_PROJECT-presentation_transcript.md` (32 Min)

## Kontext

User praesentiert PROJECT- beim woechtentlichen Tech Forum fuer die Entwicklungsteams der Vision App.
Empfohlen als Onboarding-Material ("should be part of the onboarding" — Teilnehmer-Feedback).

## Kernaussagen

### Was ist PROJECT-?

- PROJECT- = Content-Standard, der spezifiziert, welche Informationen die Vision App und Legal Intelligence benoetigen
- Metapher: PROJECT- ist das "Protokoll auf der Telefonvermittlung" zwischen Content und Produkt
- PROJECT- verbindet Content in Apollo mit Produkt-Features in Vision App durch standardisierte Informationslinien

### PROJECT- vs. MAC vs. C2

| Standard | Fokus | Dient |
|---|---|---|
| **MAC** (Model for Apollo Content Knowledge) | Editorial — wie Content erstellt wird | Apollo CMS |
| **PROJECT-** | Produkt — wie Content konsumiert wird | GPS / Vision App |
| **C2** (Global Platform) | Speicherung und Verarbeitung | Plattform-Infrastruktur |

- Paradigmenwechsel MAC → PROJECT-: "Wir haben Content" → "Wir haben Funktionalitaet"
- Artemis uebersetzt MAC-Content in PROJECT-Standard (Pipeline)

### PROJECT-Komponenten

1. **Functional Patterns** — User Experience im Produkt (UI-Drafts)
2. **Local Content** — Aktuelle Organisation und Konfiguration
3. **Product Platform Architecture** — C2-Standard als Zielformat
4. **PCING Framework** — Globales Framework mit Ontologien fuer RDF-Markup

### PROJECT-Prinzipien

1. **Lean** — Nur was vom Produkt gebraucht wird (keine ungenutzten Felder)
2. **Flexible** — Funktionales UND semantisches Wissen
3. **Integration** — Technische Spezifikationen (C2) fuer Content Delivery

### Release-Prozess

- PROJECT- arbeitet in PIs (3 Sprints Modellierung + 2 Sprints Release/Dokumentation)
- PROJECT- muss der Vision-App-Entwicklung voraus sein
- Neue Requirements → PROJECT- Release → C2/Artemis Anpassung → Content-Anpassung
- Lead Time: Monate zwischen Feature-Request und Produktverfuegbarkeit

### Team-Struktur (Stand Oktober 2024)

- Manager: Sven
- Analysten: Lis, Ute (Studio-Team: Autom, User, Es)
- Architekten: Christian, Katarina, Mo
- MAC-Team: Truda, Mara

## Empfohlene Weiterbildung (Users Tipps)

- FRBR-Grundlagen (Work/Expression/Manifestation)
- PCING-Trainings von Jamie/Jessica (RDF, RDFS, RDF-Star Videos, je ~25 Min)
- CHO vs CHM Differenzierung

## Teilnehmer-Feedback

- "Should be part of the onboarding" — sofort als Referenz empfohlen
- Praesentation auf Confluence Tech Forum Seite hinterlegt
""",
    },
    {
        "kb_id": "KB-202604150045",
        "title": "Team- IPM Mai 2025 — CodeGames, AI-in-Action, Root Cause Review",
        "meeting_date": "2025-05-22",
        "source": "inbox/Team-Meetings_md/2025-05-22_Team-ipm_may_2025_transcript.md",
        "tags": ["Team-/ipm", "Team-/ai-adoption", "Team-/codegames", "Team-/team", "Team-/meeting-distillate"],
        "strategic_intent": "Team- Ganztags-IPM: AI-Arbeitsmethoden, CodeGames-Learnings, Christian AI-Schulung, Root Cause Review.",
        "participants": "User, Sven, Iris, Ute, Christian (Hart), Team",
        "language": "de",
        "content": """# Team- IPM Mai 2025

> Destillat aus: `2025-05-22_Team-ipm_may_2025_transcript.md` (113 KB, Ganztags-Session)

## Kontext

In-Person Meeting des Team-Teams. Agenda von User + Copilot vorbereitet.
3-Stunden-Slot mit mehreren Themenblöcken.

## Agenda

1. **Svens Content Protection Projekt** — Bericht ueber Herausforderungen
2. **CodeGames-Debrief** — Users Output und AI-Arbeitsweise im Hackathon
3. **AI in Action** — Christian Hart: AI-Features in Euro, praktische Anwendung
4. **Root Cause Review** — Team-weite Analyse (laengerer Block am Ende)

## Kernaussagen

### Arbeitsmethoden

- User hat Agenda erstmals mit Copilot vorbereitet ("Copilot and I prepared an agenda")
- Meeting Notes in Teams-Notizen (Uebergang zu Copilot-gestuetzten Notes als kuenftiges Thema)
- Sven betont: AI-in-Action-Diskussion als wertvollstes Thema, flexibel Zeitboxen

### CodeGames-Learings

- Nicht so sehr das Ergebnis, sondern der Weg dorthin war lehrreich
- "Learned a lot about how a different working with AI could be in such a project"

### Team-Dynamik

- Iris uebernimmt Timekeeper-Rolle
- Wunsch nach physischen Treffen mit Mittagspause ("maybe once in some future we will have that back again")

## Relevanz fuer Workday Goals

- Goal 1 (AI-Adoption): IPM als Forum fuer AI-Erfahrungsaustausch
- Goal 2 (Scrum Master): User moderiert und strukturiert, Sven gibt strategische Priorisierung
""",
    },
    {
        "kb_id": "KB-202604150046",
        "title": "PI-14 Planning Teil 1 — Business Goals und Prioritaeten",
        "meeting_date": "2025-06-25",
        "source": "inbox/Team-Meetings_md/2025-06-25_pi-planning_pi_14_Team--_teil_1_transcript.md",
        "tags": ["Team-/pi-planning", "Team-/pi14", "Team-/PROJECT-", "Team-/meeting-distillate"],
        "strategic_intent": "PI-14 Planning: Business-Prioritaeten (Belgien, KLI, NL), Kapazitaet, Sprint-Struktur.",
        "participants": "User, Sven, Magdalena (GPOS), Marian, Christian, Ute, Person-B (neu), Moe",
        "language": "en",
        "content": """# PROJECT- PI-14 Planning — Teil 1: Business Goals & Prioritaeten

> Destillat aus: `2025-06-25_pi-planning_pi_14_Team--_teil_1_transcript.md`

## Kontext

Erstes PI-14 Planning-Meeting des PROJECT-Teams. Magdalena (GPOS) praesentiert Business-Prioritaeten.
Person-B Nouwen nimmt erstmals teil — Sven gibt Willkommens-Briefing zum Team-Arbeitsmodell.

## Kapazitaet

- **Load:** 55 Story Points
- **Capacity:** 53 Story Points (bei Standard-3-Sprint-Modell)
- Release soll bis 8. August verfuegbar sein → nur 2 Sprints a 2 Wochen moeglich

## Business-Prioritaeten (Magdalena)

### 1. Belgien — Commercial Go-Live (hoechste Prio)
- 2 Tickets fuer finalen Commercial Release (Ende 2025)
- Jurisprudenz-Excerpts auf Search Result Page fuer Magazin-Issues
- Editorial Boost / Content Highlight Feld (Suchranking, spaeter AI-nutzbar)

### 2. Legal Intelligence
- Content Push Big Four
- Pipeline-Stabilitaet + Synonyme fuer niederlaendische Gesetze

### 3. KLI Properties (neuer Joiner)
- Nischenbereiche: Arbitration, Competition, IP Law
- Neue Properties: Jurisdiction, Parties, NS Code, Organization Roles
- 5 Tickets (urspruenglich 6, eins gemergt)

### 4. NL-Produkte (niedrigere Prio)
- ParPerson-Bmentary History
- Neue InfoTypes fuer Title Pages

## Sprint-Entscheidung

- **Option A:** 2 Sprints a 2 Wochen = 43 SP (knapp fuer 45 SP Load)
- **Option B:** 2. Sprint auf 3 Wochen verlaengern = 53 SP, aber nur 1 Woche Review-Buffer (Risiko)
- **Entscheidung:** Option A — 2 Standard-Sprints, letzte 3 Tickets als Stretch Goals

## Svens Briefing fuer Person-B (Team-Arbeitsmodell)

- PI-Struktur flexibel: 2-3 Analyse-Sprints + D-Sprint (SHACL Release, Modell Release, Dokumentation, MAC Release, C2 Release)
- Voellig anders als Rest der Vision-App-Welt
- "We have API planning that is not regular every six weeks"
""",
    },
    {
        "kb_id": "KB-202604150047",
        "title": "PI-14 Planning Teil 2 — Sprint-Zuweisung und Ticket-Verteilung",
        "meeting_date": "2025-06-25",
        "source": "inbox/Team-Meetings_md/2025-06-25__pi-planning_pi_14_Team--_teil_2_transcript.md",
        "tags": ["Team-/pi-planning", "Team-/pi14", "Team-/PROJECT-", "Team-/meeting-distillate"],
        "strategic_intent": "PI-14 Planning Teil 2: Ticket-Zuweisung, Stretch Goals, Miro-Board-Arbeit.",
        "participants": "User, Christian, Ute, Moe, Person-B",
        "language": "en",
        "content": """# PROJECT- PI-14 Planning — Teil 2: Sprint-Zuweisung

> Destillat aus: `2025-06-25__pi-planning_pi_14_Team--_teil_2_transcript.md`

## Kontext

Zweite Session des PI-14 Plannings. Ticket-Zuweisung auf Sprints, Miro-Board-Arbeit.

## Entscheidungen

- **2-Sprint-Modell bestaetigt** (Users Einschaetzung aus Teil 1 akzeptiert)
- **Letzte 3 Tickets (10 SP) als Stretch Goals** — verbleiben im Backlog, werden nicht aktiv eingeplant
- **Kein Patch noetig** — Belgien arbeitet mit 6.7/6.8-Kompatibilitaet (Utes Bestätigung)
  - Spart 2 Story Points (reserviert fuer Patch-Erstellung)
- **Keine internen Tickets in diesem PI** — volle Kapazitaet fuer Business-Tickets

## Operative Details

- 45 SP Load vs. 43 SP Kapazitaet — "Promise and overdeliver" (Moe)
- D-Sprint (Release-Erstellung) zaehlt nicht zur Velocity
- Confluence-Prioritaetenliste bereinigt und sortiert

## Team-Dynamik

- PO-Priorisierung (Marian, Magdalena) verlief reibungslos
- "I was happy that the POs made up their minds on the priorities" — User
""",
    },
    {
        "kb_id": "KB-202604150048",
        "title": "KTeam- ADAPT-Diskussion — Architekturentscheidung Onboarding",
        "meeting_date": "2025-02-18",
        "source": "inbox/Team-Meetings_md/2025-02-18_KTeam-transcript.md",
        "tags": ["Team-/architecture", "Team-/adapt", "Team-/PROJECT-", "Team-/onboarding", "Team-/meeting-distillate"],
        "strategic_intent": "Architekturentscheidung: ADAPT-Definition fuer PROJECT-, SLA fuer neue Laender, Breaking Changes.",
        "participants": "Christian Dirschl, Moe Barati, Paul Hanrath, Ute Steinbeck, User",
        "language": "en",
        "content": """# KTeam- — ADAPT-Diskussion: Was bedeutet Adoption fuer PROJECT-?

> Destillat aus: `2025-02-18_KTeam-transcript.md`

## Kontext

Knowledge & Knowledge Management Team (KTeam-) Diskussion ueber die ADAPT-Problematik.
Ausgeloest durch ungarische Onboarding-Erfahrung: Tickets als "adopt" klassifiziert,
aber bei Delivery stellte sich heraus, dass Modell-Aenderungen noetig sind.

## Kernproblem

- Neue Laender/Content-Sets werden als "adopt" eingestuft (= keine PROJECT-Aenderungen noetig)
- In der Praxis treten trotzdem Aenderungsbedarfe auf (z.B. neue Properties, Breaking Changes)
- Es fehlt eine klare Definition was ADOPT fuer PROJECT- bedeutet
- Christian: "We are not prepared for that. And this is something that we definitely need to do."

## Positionen

### Christian Dirschl (Architect)
- ADAPT muss fuer PROJECT- definiert werden — was ist adopt, was ist extend, was ist new?
- Breaking Changes koennen ueberall auftreten — ADAPT garantiert keine Stabilitaet
- Referenz: Capability-Team hatte fruehre Definitionen (adopt/extended/new)
- Missbrauch des Modells ("abuse of solutions") muss als separates Thema adressiert werden

### Paul Hanrath
- SLA-Ansatz: "adopt with no changes unless..."
- Risiko muss kommuniziert werden — Delivery kann immer auf Probleme stossen
- Frage: wann im Ticket-Lifecycle kann man den Impact auf das Gesamtsystem erkennen?

### Ute Steinbeck
- Pragmatischer Ansatz: Out-of-bounds-Tickets zurueck an Business mit "costs you extra"
- Budget-Druck als natuerlicher Regulierungsmechanismus
- "Telling them it is going to cost you is often a good way of making people reconsider"

### Moe Barati (Svens Input)
- Sven schlaegt vor: ADAPT-Verstaendnis schriftlich definieren → GPOS zur Abstimmung

## Entscheidung

- **Naechster Schritt:** PROJECT-eigene ADAPT-Definition erarbeiten
- **Kommunikation:** An GPOS senden zur Bestaetigung/Anpassung
- **Langfristig:** SLA fuer neue Content-Sets mit explizitem Risiko-Hinweis

## Architektur-Relevanz

Diese Diskussion definiert die Governance-Grenze zwischen "Content passt auf die Plattform"
und "Content benoetigt Plattform-Aenderungen" — zentral fuer das Onboarding-Modell
kuenftiger Laender (USK, Li, etc.).
""",
    },
    {
        "kb_id": "KB-202604150049",
        "title": "PI-16 Planning — Design Sprint und Velocity",
        "meeting_date": "2025-11-27",
        "source": "inbox/Team-Meetings_md/2025-11-27_Team- PI-Planning PI-16.md",
        "tags": ["Team-/pi-planning", "Team-/pi16", "Team-/design-sprint", "Team-/meeting-distillate"],
        "strategic_intent": "PI-16 Planning: Design Sprint Ankuendigung, Personalumplanung (Iris, Katarina), Velocity-Diskussion.",
        "participants": "Sven, User, Ute, Team",
        "language": "en",
        "content": """# PROJECT- PI-16 Planning — Design Sprint und Velocity

> Destillat aus: `2025-11-27_Team- PI-Planning PI-16.md` (53 Min)

## Kontext

PI-16 Planning-Session. Sven kuendigt einen strategischen Design Sprint an,
der erhebliche Personalverschiebungen im PROJECT-Team verursacht.

## Design Sprint (Svens Ankuendigung)

### Was
- Advisory Board genehmigt (hohe Wahrscheinlichkeit) einen Design Sprint
- Ziel: "How can we speed up the onboarding of new countries / content sets that are not MACified?"
- Interdisziplinaeres Team aus verschiedenen Vision-App-Streams

### Wer wird abgezogen
- **Katarina** — als Knowledge Architect
- **Iris** — als Business Analyst (IVNL nahe Abschluss, kennt ungarischen Content)

### Auswirkung auf PROJECT-
- Zwei Schluesselrollen temporaer nicht verfuegbar
- Kapazitaet fuer PI-16 reduziert

### Vertraulichkeit
- "Not to go out to the world and tell everyone of design sprints after this meeting"
- Offizielle Ankuendigung am naechsten Tag durch Advisory Board

## Velocity-Thema

- Diskussion ueber PTO-Abdeckung (Analyst-Vertretung bei Urlaub)
- Sven fordert: kein Zeitraum ohne mindestens einen verfuegbaren Analysten
- Ostern und Weihnachten als kritische Perioden identifiziert

## Strategische Bedeutung

Der Design Sprint adressiert das fundamentale Onboarding-Problem (vgl. ADAPT-Diskussion KB-202604150048)
und signalisiert, dass die Organisation das Thema "nicht-MACifizierter Content" als strategisch priorisiert.
""",
    },
    {
        "kb_id": "KB-202604150050",
        "title": "PI-17 Planning Teil 1 — Product Milestones und Prioritaeten",
        "meeting_date": "2026-03-03",
        "source": "inbox/Team-Meetings_md/2026-03-03_Team- PROJECT- PI-17 planning, part-1_2 (Business Goals & Priorities) (1).md",
        "tags": ["Team-/pi-planning", "Team-/pi17", "Team-/PROJECT-", "Team-/milestones", "Team-/meeting-distillate"],
        "strategic_intent": "PI-17 Planning: Marians Product Milestones, NVLE/KLI/Belgien Go-Lives, PROJECT-Prioritaeten.",
        "participants": "Marian Moehren, Magdalena Sowula, User, Ute, Person-B, Christian, Nitin, Team",
        "language": "en",
        "content": """# PROJECT- PI-17 Planning — Teil 1: Product Milestones & Prioritaeten

> Destillat aus: `2026-03-03_Team- PROJECT- PI-17 planning, part-1_2 (Business Goals & Priorities) (1).md`

## Kontext

Erstes PI-17 Planning-Meeting. Marian (Product) praesentiert Milestones, Magdalena (GPOS)
erklaert Business-Prioritaeten.

## Product Milestones (Marian)

### Bereits erreicht (Anfang 2026)
- Beta Launch Text & Commentor Netherlands — Kunden auf Prod-Endpoint seit Januar
- Commercial Go-Live Belgian Legal (Notare als erstes Kundensegment)

### PI-17 Ziele (Maerz-April 2026)
- **Full Commercial Go-Live Text & Commentor NL** — Maerz (erste Haelfte)
- **Full Commercial Go-Live Belgian Legal** — 26. Maerz
- **Technical Readiness Dutch NVLE** (Kundenmigration in PI-18)
- **Beta Go-Live KLI Competition** — Tech Readiness bis Ende PI-17
- **Initial adot Belgium Text** — Ende PI-17
- **Lex My Notify (Polen)** — Alerting-Portal, Ende PI-17

### Legal Intelligence (nicht auf Marians Slide)
- Launch: Juni 2026
- Lokales Team entwickelt, aber PROJECT-Aenderungen muessen in naechste Version
- Hohe Prioritaet trotz fehlender Sichtbarkeit auf Roadmap-Slide

## Prioritaeten-Liste (Magdalena + Marian)

1. **Search on Site Subscription (NVLE Belgium)** — fuer 2. Commercial Go-Live am 26.3.
2. **Content Highlight / Editorial Boost** — Suchranking, spaeter AI-nutzbar
3. **Legal Intelligence** — Content Push Big Four, Synonyme
4. **KLI Properties** — Jurisdiction, Parties, NS Code
5. **NL Remaining** — ParPerson-Bmentary History, Title Pages (niedrigere Prio)

## Strategische Einordnung

Die Dichte an Go-Lives in PI-17 ist ungewoehnlich hoch (5+ Produkt-Meilensteine).
PROJECT- muss bei allen als Enabler liefern. Legal Intelligence als "unsichtbare" aber
hoechst wichtige Prioritaet — externer Druck ohne sichtbare Roadmap-Verankerung.
""",
    },
    {
        "kb_id": "KB-202604150051",
        "title": "PI-17 Planning Teil 2 — VA-Planning Bericht und Naechste Schritte",
        "meeting_date": "2026-03-03",
        "source": "inbox/Team-Meetings_md/2026-03-03_Team- PROJECT- PI-17 planning, part-1_2 (Business Goals & Priorities) (2).md",
        "tags": ["Team-/pi-planning", "Team-/pi17", "Team-/PROJECT-", "Team-/meeting-distillate"],
        "strategic_intent": "PI-17 Planning Teil 2: VA-Planning-Bericht, Partner-Team, Data-Pipeline-Parallelen, Kommunikation an POs.",
        "participants": "User, Christian, Ute, Person-B, Nitin",
        "language": "en",
        "content": """# PROJECT- PI-17 Planning — Teil 2: VA-Planning Bericht

> Destillat aus: `2026-03-03_Team- PROJECT- PI-17 planning, part-1_2 (Business Goals & Priorities) (2).md`

## Kontext

Zweite PI-17 Planning-Session. User berichtet von den uebergeordneten Vision-App
Planning-Events. Nitin (KLI) mit begrenzter Verfuegbarkeit (30 Min).

## VA-Planning Bericht (User)

- PROJECT- wurde in keiner Risk & Dependency Session erwaehnt — keine externen Abhaengigkeiten
- Person-A praesentierte Partner-Team-Fortschritt (aehnlich Data-Pipeline-Ansatz, aber breiterer Scope)
- Architecture Runway Session fiel aus (Casian nicht verfuegbar)
- Person-B bemerkt Parallelen zwischen Astra und Data-Pipeline

## Naechste Schritte

- User hat PI-17 Planning-Ergebnisse zusammengefasst
- Wartet auf Input von Sven bevor Kommunikation an Marian/Magdalena
- Deadline: Ende PI (= Montag)
- Christians Empfehlung: "Can you wait until tomorrow?" — Qualitaet vor Schnelligkeit

## Data-Pipeline-Kontext

Person-Bs Beobachtung ueber Astra/Data-Pipeline-Parallelen ist strategisch relevant:
Beide Ansaetze adressieren das Problem "heterogenen Content in standardisierte Formate bringen",
aber mit unterschiedlichem Scope und Automatisierungsgrad.
""",
    },
    {
        "kb_id": "KB-202604150052",
        "title": "Strategy Thursday A2M — Data-Pipeline Mapping Industrialized",
        "meeting_date": "2026-03-05",
        "source": "inbox/Team-Meetings_md/2026-03-05_Team-Strategy_Thursday_A2M.md",
        "tags": ["Team-/Data-Pipeline", "Team-/strategy", "Team-/ai-pipeline", "Team-/presentation", "Team-/meeting-distillate"],
        "strategic_intent": "Users Data-Pipeline-Praesentation: Industrialisiertes Mapping, KLI-Learnings, AI-Pipeline-Ansatz.",
        "participants": "User, Sven, Ute, Christian Dirschl, Moe Barati, Gianluigi Masera",
        "language": "en",
        "content": """# Strategy Thursday — Data-Pipeline: Mapping Industrialized

> Destillat aus: `2026-03-05_Team-Strategy_Thursday_A2M.md` (42 KB)

## Kontext

Users Praesentation des industrialisierten Data-Pipeline-Mapping-Ansatzes im Team- Strategy Thursday.
Ausgeloest durch KLI-Mapping-Erfahrung 2024.

## Problemanalyse (aus KLI-Projekt 2024)

### Situation
- User nahm an monatelanger Meeting-Serie fuer KLI-Content-Mapping teil
- Excel-basierter Prozess mit vielen Iterationsrunden
- **Beobachtete Probleme:**
  - Gleiche Fragen immer wieder (z.B. "Was bedeutet pub_date — Druckdatum oder Release-Datum?")
  - Teilnehmer nicht vorbereitet
  - Wiederholte semantische Verhandlungen
  - Wissen lebt in Koepfen, kein Transfer

### Root Cause (aus Transkript-Analyse)
- User analysierte Meeting-Transkripte auf wiederkehrende Issues
- Kernproblem: "Knowledge lives in people's heads. There's no transfer."
- Strukturelles Problem: Wissen ist disconnected

## Loesung: Industrialisiertes Mapping

### Ansatz
- AI-gestuetzte Pipeline statt manueller Excel-Runden
- Analyse der Quelldaten + automatisches Vorschlagen von Mappings
- Praesentation fokussiert auf Methodik, nicht auf Code

### Seitliches Thema
- First: Personalankuendigung — Marcel Fonder verlaesst Benelux (Sven)
  - Peter Emming und Marlon Mertens uebernehmen interim
- Ticket-Splitting auf Team-Mitglieder als zweites Thema geplant

## Strategische Bedeutung

- Direkte Umsetzung von Workday Goal 3 (Productize Data-Pipeline)
- KLI-Erfahrung als Katalysator: manueller Prozess → AI-Pipeline
- Grundlage fuer "usable and understandable" Mapping-Ergebnisse
""",
    },
    {
        "kb_id": "KB-202604150053",
        "title": "PI-17 Vorbereitung — Backlog-Priorisierung und interne Epics",
        "meeting_date": "2026-02-26",
        "source": "inbox/Team-Meetings_md/2026-02-26_Team- Weekly Strategy Thursday.md",
        "tags": ["Team-/pi-planning", "Team-/pi17", "Team-/backlog", "Team-/strategy", "Team-/meeting-distillate"],
        "strategic_intent": "PI-17 Vorbereitung: Sizing abgeschlossen, interne Epics priorisieren, Strategy Thursday → Planning-Modus.",
        "participants": "User, Sven, Christian Dirschl, Moe Barati, Team",
        "language": "en",
        "content": """# PI-17 Vorbereitung — Strategy Thursday als Planning-Session

> Destillat aus: `2026-02-26_Team- Weekly Strategy Thursday.md` (37 KB)

## Kontext

Regulaerer Strategy Thursday wird zu PI-17-Vorbereitungssession umfunktioniert.
Sizing der externen Tickets (Ute, Person-B) abgeschlossen. PI-Planning auf Dienstag + Mittwoch naechste Woche.

## Status

- Letztes Sizing: Utes und Person-Bs Tickets fertig
- Pipeline leer — keine neuen Business-Tickets im Sizing-Backlog
- Strategy Thursday entfaellt zugunsten PI-Arbeit

## Aufgabe der Session

- **Interne Tickets priorisieren** — "we can't prioritize the external ones, which we do with Magdalena/Marian"
- Christian: "We have the three epics we talked about. The question is what else?"
- Sven: "We should have a good understanding of why we do what in the next Pi for us"

## Arbeitsweise (Scrum-Master-Perspektive)

Users Moderation zeigt das Zusammenspiel:
1. Externe Prios → GPOS (Magdalena/Marian) entscheidet
2. Interne Prios → Team entscheidet gemeinsam
3. User fragt aktiv: "Was wollen wir heute genau machen?"
4. Sven gibt strategische Richtung, Team fuellt mit Inhalt
""",
    },
]


def main() -> None:
    before = len(list(VAULT_ROOT.glob("*.md")))
    print(f"Vault before: {before} files\n")

    for d in DISTILLATES:
        kb_id = d["kb_id"]
        title = d["title"]
        slug = slugify(title)
        vault_filename = f"{kb_id}_{slug}.md"
        vault_path = VAULT_ROOT / vault_filename

        if vault_path.exists():
            print(f"  SKIP (exists): {vault_filename}")
            continue

        frontmatter = build_meeting_frontmatter(
            kb_id=kb_id,
            title=title,
            meeting_date=d["meeting_date"],
            tags=d["tags"],
            source_path=d["source"],
            strategic_intent=d["strategic_intent"],
            participants=d["participants"],
            language=d["language"],
        )

        vault_path.write_text(frontmatter + d["content"].lstrip("\n"), encoding="utf-8")
        print(f"  OK: {vault_filename}")

    after = len(list(VAULT_ROOT.glob("*.md")))
    print(f"\nVault after: {after} files (+{after - before} new)")


if __name__ == "__main__":
    main()



