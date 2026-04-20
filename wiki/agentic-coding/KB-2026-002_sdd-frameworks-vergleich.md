---
id: KB-2026-002
title: "SDD-Frameworks Vergleich: OpenSpec vs. Spec Kit vs. This Framework"
domain: agentic-coding
source_type: llm-generated
confidence: high
created: 2026-04-13
created_by: copilot
session_context: "Session 2026-04-13: Comparison of public SDD frameworks with this agentic workspace framework"
related_to: [KB-2026-001]
sources:
  - "https://github.com/Fission-AI/OpenSpec"
  - "https://github.com/github/spec-kit"
  - "https://github.com/cameronsjo/spec-compare"
reviewed_by: null
status: draft
---

# SDD-Frameworks Vergleich: OpenSpec vs. Spec Kit vs. This Framework

## Kernaussage

Es gibt drei relevante SDD-Frameworks für AI-assisted Development. Dieses Framework ist technisch ausgereifter in Session-Management und Agent-Governance, hat aber geringere externe Sichtbarkeit.

## Details

### Kurzvergleich

| Feature | OpenSpec | Spec Kit | This Framework |
|---|---|---|---|
| Backing | Fission-AI (~31k Stars) | GitHub offiziell (~77k Stars) | This project (public template) |
| Installation | `npm install -g @fission-ai/openspec` | `uv tool install specify-cli` | No install needed |
| Workflow | Fluid, customizable | constitution → specify → plan → tasks → implement | PLAN → IMPLEMENT → VALIDATE → INTEGRATE |
| Agents | Generische Slash-Commands | Generische Slash-Commands | 7 spezialisierte Agents mit Nicht-Verantwortlichkeiten |
| Session-Kontinuität | ❌ | ❌ | ✅ SESSION_LOG + USER_INTENT_LOG + ARTIFACT_REGISTRY |
| Handoff-Schema | ❌ | ❌ | ✅ explizites handoff.schema.md |
| Anti-Halluzination | ❌ | ❌ | ✅ 70%-Problem explizit adressiert |
| Knowledge-Integration | Nur Codebase | Nur Codebase | context/ + Vault-MCP (workspace-spezifisch) |
| Sichtbarkeit | Community | Community | Public template, not yet listed in spec-compare |

### Wann welches Framework wählen?

- **OpenSpec:** Brownfield-Projekte, bestehende Node.js-Toolchain, will kein neues Tool lernen
- **Spec Kit:** Greenfield, GitHub-native Team, will phasierte Struktur (constitution-Phase)
- **This Framework:** Copilot + Jira + Confluence-Stack, braucht Session-Kontinuität und Agent-Governance

## Relevanz für diesen Workspace

Dieser Agentic Workspace implementiert das Framework bereits vollständig (Workorders, Agents, Schemas, Prompts). Die wichtigsten Erweiterungen gegenüber externen Frameworks sind die Knowledge-Integration über MCP und die Handoff-Protokolle.

**Gap to close:** Das Framework ist nicht im [spec-compare](https://github.com/cameronsjo/spec-compare)-Repo gelistet.

## Quellen

- [spec-compare Repo](https://github.com/cameronsjo/spec-compare)
- [OpenSpec](https://github.com/Fission-AI/OpenSpec)
- [Spec Kit](https://github.com/github/spec-kit)


