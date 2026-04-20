---
id: KB-2026-001
title: "Vibe Coding vs. Vibe Engineering – Begriffs-Abgrenzung"
domain: agentic-coding
source_type: llm-generated
confidence: high
created: 2026-04-13
created_by: copilot
session_context: "Session 2026-04-13: Thomas Caudal DXG Architect CoP Webinar, Analyse DXDP Confluence"
related_to: [KB-2026-002, KB-2026-003]
sources:
  - "https://your-confluence-instance.example.com
  - "DXG Architect Community of Practice Webinar 2026-03-16 (Thomas Caudal)"
reviewed_by: null
status: draft
---

# Vibe Coding vs. Vibe Engineering – Begriffs-Abgrenzung

## Kernaussage

Vibe Coding und Vibe Engineering sind keine Synonyme. Sie beschreiben zwei unterschiedliche Reifegrade im Umgang mit AI-Coding-Assistenten.

## Details

**Vibe Coding**
Explorativ, prompt-driven. Ein Mensch reagiert iterativ auf LLM-Outputs und optimiert für Speed und Intuition statt für Struktur. Kein explizites Governance-System. Erzeugt technische Schulden, wenn ausschließlich eingesetzt.

**Vibe Engineering**
Deliberate Design, Governance und Orchestration von AI-Agenten. Humans kodieren Intent, Constraints und Control-Mechanismen damit Systeme zuverlässig at scale ausführen können.

**Die 5 Zutaten von Vibe Engineering (Caudal 2026):**

| Zutat | Funktion |
|---|---|
| Control plane | Governs *who* can give context |
| Knowledge systems | Supply *what* context exists |
| Orchestration | Decides *when* context is injected |
| SDD | Defines *how* intent is encoded into context |
| Evaluation | Checks *whether context was sufficient* |

## Relevanz für Team-

Der Agentic Workspace ist bereits Vibe Engineering: Custom Instructions, Agents, MCP-Server, Vault, Workorders = vollständiges Control-Plane + Knowledge-System. Bewusstes Framing nach außen (Team, DXDP) als "Vibe Engineering" stärkt Positionierung.

Vibe Coding ist erlaubt für schnelle Exploration (z.B. Skript ausprobieren, Meeting-Zusammenfassung). Nicht für produktive Artefakte (Confluence-Seiten, Jira-Tickets, Code für _tools/).

## Quellen

- [Journey to GenAI for SDLC (Confluence DXDP)](https://your-confluence-instance.example.com)
- [DEV.to Artikel: "Vibe Coding is Technical Debt. Vibe Engineering is the Fix"](https://dev.to)
- VSCode Blog: [Making agents practical for real-world development](https://code.visualstudio.com/blogs/2026/03/05/making-agents-practical-for-real-world-development)


