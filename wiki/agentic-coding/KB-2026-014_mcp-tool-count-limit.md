---
id: KB-2026-014
title: "MCP Tool-Count-Limit: Degradation ab ~40–60 Tools"
domain: agentic-coding
source_type: llm-generated
confidence: high
created: 2026-04-14
created_by: copilot
session_context: "Session 2026-04-14: DXDP MCP-Seite analysiert (Thomas Caudal Webinar Kontext)"
related_to: [KB-2026-001]
sources:
  - "https://your-confluence-instance.example.com
  - "https://your-confluence-instance.example.com
reviewed_by: null
status: draft
---

# MCP Tool-Count-Limit: Degradation ab ~40–60 Tools

## Kernaussage

Jedes MCP-Tool-Schema verbraucht Tokens im Modell-Kontext. Frontier-Modelle degradieren messbar ab ~40–60 aktiven Tools; viele haben Hard Limits um 128 Tools. Im Agentic Workspace mit 5 MCP-Servern ist das eine aktive Risikogröße.

## Details

### Das Problem

Wenn ein MCP-Host (VS Code Copilot) sich mit mehreren MCP-Servern verbindet, werden **alle** Tool-Schemas aller Server in den Modell-Kontext injiziert — unabhängig davon, ob das Tool in dieser Session benötigt wird.

Konsequenzen:
- Token-Budget schrumpft für nutzbare Kontext-Inhalte
- Modell-Performance sinkt bei Tool-Selection und Reasoning
- Hard Limit bei ~128 Tools (modellabhängig)

### Faustregel

| Tool-Anzahl | Erwartetes Verhalten |
|---|---|
| < 20 | Kein messbarer Effekt |
| 20–40 | Leichte Token-Budget-Kosten, noch stabil |
| 40–60 | Messbare Degradation bei Tool-Selection |
| > 60 | Signifikante Qualitätsverluste |
| > 128 | Hard Limit — viele Modelle verwerfen Tools |

### Agentic Workspace Bestandsaufnahme

Der Workspace hat 5 MCP-Server:

| Server | Geschätzte Tool-Anzahl |
|---|---|
| your-jira | ~15–20 |
| your-confluence | ~15–20 |
| microsoft-graph (gateway mode) | ~30–40 |
| retrieve | ~5–8 |
| vault-mcp | ~5 |

**Gesamtschätzung: ~70–93 Tools** — potenziell im Degradationsbereich.

### Gegenmaßnahmen

1. **Deferred Tools** (wie im Agentic Workspace implementiert): Tools werden erst bei Bedarf geladen — Copilot lädt sie mit `tool_search_tool_regex` on demand
2. **Tool-Exposure-Mode**: `microsoft-graph` läuft bereits im `gateway`-Mode (reduzierter Tool-Count)
3. **Selektives Aktivieren**: Nur benötigte MCP-Server für eine Session aktivieren
4. **Tool-Batching in Prompts**: Mehrere Tool-Calls in einer Anweisung statt einzeln

## Relevanz für diesen Workspace

Wenn Copilot in komplexen Sessions träge wirkt oder falsche Tools auswählt, ist Tool-Count-Degradation ein möglicher Faktor. Diagnose: In VS Code → Chat → `...` → "Show Agent Debug Logs" prüfen wie viele Tools aktiv sind.

## Quellen

- VS Code Copilot Documentation: MCP Servers
- MCP Protocol Spec (modelcontextprotocol.io)


