---
id: KB-2026-013
title: "/fleet – Parallele Agent-Orchestrierung in Copilot CLI (Nicht-Entscheidung 2026-04)"
domain: agentic-coding
source_type: blog_post + hands-on-evaluation
source_ref: "Matt Nigh, GitHub Blog, April 2026 – /fleet in Copilot CLI"
created: 2026-04-15
author: copilot
reviewed_by: Author
status: stable
confidence: high
tags: [fleet, parallel-agents, copilot-cli, background-agents, orchestration]
---

# /fleet – Parallele Agent-Orchestrierung (Nicht-Entscheidung 2026-04)

## Was ist /fleet?

`/fleet` ist ein Slash-Command im **GitHub Copilot CLI** (Terminal), der echte Parallelarbeit durch mehrere Sub-Agenten ermöglicht.

**Funktionsprinzip:**
1. Orchestrator zerlegt den Task in unabhängige Arbeitseinheiten
2. Identifiziert welche Einheiten parallel laufen können vs. sequenziell warten müssen
3. Dispatcht unabhängige Items gleichzeitig als Background Sub-Agenten
4. Pollt auf Abschluss, dispatcht die nächste Welle
5. Verifiziert Outputs und synthetisiert finale Artefakte

Sub-Agenten teilen das Filesystem, teilen aber **kein** Kontextfenster — nur der Orchestrator koordiniert.

**Aufruf:**
```bash
copilot -p "/fleet <OBJECTIVE>" --no-ask-user
```

## Voraussetzungen

- GitHub Copilot CLI installiert
- `.github/agents/`-Dateien für Custom Agent Specialization (optional, aber empfohlen)
- GitHub-Account mit Zugang zur `/fleet`-Preview
- `github.copilot.chat.backgroundAgent.enabled: true` in VS Code Settings

## VS Code Äquivalent: Background Agents

In VS Code Chat gibt es **Copilot Coding Agents** als Chat-natives Pendant:
- Task im Chat starten → Copilot dispatcht als Background Agent
- Status im `/tasks`-Panel sichtbar
- Dieselben `.github/agents/`-Dateien werden genutzt
- Keine Terminalkenntnis erforderlich

Setting: `github.copilot.chat.backgroundAgent.enabled: true`

## Bewertung für Agentic Workspace (Stand 2026-04-15)

### Stärken
- Echte Parallelität bei natürlich partitionierbaren Tasks (z.B. 4 SHACL-Profile gleichzeitig validieren, KB-Snippets für 5 Domains parallel schreiben)
- Custom Agents pro Track möglich (`@technical-writer.md` für Docs, `@developer.md` für Code)
- Team- `.github/agents/`-Infrastruktur ist bereits kompatibel — kein Umbau nötig

### Grenzen
- `/fleet` ist CLI-only — kein Chat-Workflow
- Background Agents (VS Code) sind Preview/Beta — Account-Zugang erforderlich
- File-Locking fehlt: zwei Agenten, die dieselbe Datei schreiben → letzter gewinnt, kein Merge
- Prompts müssen vollständig self-contained sein (Sub-Agenten sehen keinen Chat-Verlauf)

### Wann sinnvoll
- ✅ Mehrere Dateien ohne Abhängigkeiten (z.B. parallele Confluence-Seiten)
- ✅ Feature-Implementierung über API + UI + Tests hinweg
- ❌ Lineare Abhängigkeitskette (Schema → Modell → Test)
- ❌ Einzeldatei-Tasks — normaler Chat ist schneller

## Entscheidung (Agentic Workspace, 2026-04-15)

**🟡 Zurückgestellt — nicht implementiert.**

**Begründung:**
- Background Agents für Authors GitHub-Account noch nicht in Preview verfügbar (geprüft 2026-04-15)
- `/fleet` CLI-only, passt nicht zum Chat-first Workflow des Agentic Workspace
- Infrastruktur (`.github/agents/`, Settings) ist bereits vorbereitet → Einstieg jederzeit möglich wenn Preview-Zugang kommt

**Wiedervorlage:** Sobald `github.copilot.chat.backgroundAgent.enabled` im Chat-Panel sichtbar wird (Tasks-Icon beim komplexen Task), erneut evaluieren.

## Prompt-Muster für effektives /fleet (zur späteren Nutzung)

```
/fleet <OBJECTIVE>

Track 1: [Deliverable] in [Verzeichnis/Datei] — keine Änderungen außerhalb
Track 2: [Deliverable] in [Verzeichnis/Datei] — keine Änderungen außerhalb
Track 3: [Deliverable] in [Verzeichnis/Datei] — hängt von Track 1 ab

Tracks 1 und 2 parallel. Track 3 nach Abschluss von Track 1.
Validierung: [Lint/Tests/Schema-Check] muss für jeden Track bestehen.
```

**Schlüsselprinzipien:**
- Explizite Dateigrenzen je Track (verhindert Überschreibkollisionen)
- Abhängigkeiten explizit deklarieren, nicht implizit lassen
- Validierungskriterien im Prompt angeben
- Prompts self-contained schreiben (kein Bezug auf Chat-Verlauf)


