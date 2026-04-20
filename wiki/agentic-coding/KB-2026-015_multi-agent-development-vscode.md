---
id: KB-2026-015
title: "Multi-Agent Development in VS Code: Agent-Typen, Subagents, Orchestrierung"
domain: agentic-coding
source_type: llm-generated
confidence: high
created: 2026-04-14
created_by: copilot
session_context: "Session 2026-04-14: DXDP 'Multi-Agent Development in VS Code'-Seite analysiert"
related_to: [KB-2026-001, KB-2026-010]
sources:
  - "https://your-confluence-instance.example.com
  - "https://code.visualstudio.com/blogs/2026/02/05/multi-agent-development"
  - "https://code.visualstudio.com/docs/copilot/agents/subagents"
reviewed_by: null
status: draft
---

# Multi-Agent Development in VS Code: Agent-Typen, Subagents, Orchestrierung

## Kernaussage

VS Code 1.109+ (Januar 2026) unterstützt drei Agent-Typen (Local, Background, Cloud) und parallele Subagents mit Context-Isolation. Das ermöglicht spezialisierte Workflows mit sauberem Context-Management — der Agentic Workspace nutzt das bereits über `.agent.md`-Definitionen und `runSubagent`.

## Details

### Die drei Agent-Typen

| Typ | Ausführungsort | Interaktion | Team-Sichtbarkeit | Isolation |
|---|---|---|---|---|
| **Local Agent** | Eigene Maschine | Interaktiv | Nein | Nein (direkter Workspace-Zugriff) |
| **Background Agent** | Eigene Maschine (CLI) | Unattended (async) | Nein | Ja (Worktrees) |
| **Cloud Agent** | Remote Infra | Unattended (async) | Ja (PRs/Issues) | Ja (remote) |

**Verfügbarkeit:**
- Local + Background: VS Code 1.109+ (alle Copilot-Pläne)
- Cloud (Claude/Codex): Copilot Pro+ und Enterprise

**Im Agentic Workspace relevant:** Primär Local Agent. Cloud-Agenten erst wenn Copilot Pro+ vorliegt.

### Subagent-Orchestrierung (ab VS Code 1.109)

Subagents sind context-isolierte Agents, die vom Haupt-Agent gestartet werden und nur ihr Ergebnis zurückliefern — nicht den gesamten Erkundungskontext.

**Key benefits:**
- Parallele Ausführung unabhängiger Tasks
- Sauberer Haupt-Kontext (nur Ergebnisse, kein Exploration-Noise)
- Spezialisierung: Research-Agent (read-only), Implementation-Agent, Security-Agent

**Beispiel-Workflow:**
```
Haupt-Agent erhält Task "Feature X implementieren"
  ├─ Subagent A: Auth-Patterns recherchieren (parallel)
  ├─ Subagent B: Ähnliche Features im Codebase analysieren (parallel)
  └─ Subagent C: Docs scannen (parallel)
        ↓
Haupt-Agent synthetisiert und implementiert
```

### Custom Agent Specialization

Custom Agents via `.agent.md`-Dateien kombiniert mit Subagents:

```
Research Agent   → readonly, web search
Implementation   → full editing
Security         → vulnerability scan only
Documenter       → write to output/ only
```

Handoffs zwischen Agents via `handoff.schema.md` (im WK SDD Framework vorhanden).

### MCP Apps (Generally Available)

MCP-Tool-Aufrufe können interaktive UI-Komponenten zurückgeben (Dashboards, Formulare, Multi-Step-Workflows) — direkt im Chat sichtbar. Nicht nur Text-Responses.

## Relevanz für Team-

Der Agentic Workspace implementiert das Pattern bereits:
- `runSubagent` im `copilot-instructions.md` konfiguriert
- Agents: `architect`, `developer`, `doublecheck`, `critical-thinker`, `Explore`
- Background-Agents: noch nicht genutzt — könnte für lang laufende Analyse-Tasks relevant sein (z.B. Confluence-Audit)

**Nächster Schritt:** Background-Agent-Pattern für den Confluence-Audit-Task evaluieren (`tasks/confluence-audit/`).

## Quellen

- [Multi-Agent Development in VS Code (DXDP)](https://your-confluence-instance.example.com)
- [VS Code Blog: Your Home for Multi-Agent Development](https://code.visualstudio.com/blogs/2026/02/05/multi-agent-development)
- [Subagents Documentation](https://code.visualstudio.com/docs/copilot/agents/subagents)


