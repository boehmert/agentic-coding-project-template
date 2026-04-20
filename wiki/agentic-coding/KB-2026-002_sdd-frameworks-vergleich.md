---
id: KB-2026-002
title: "SDD-Frameworks Vergleich: OpenSpec vs. Spec Kit vs. WK SDD Framework"
domain: agentic-coding
source_type: llm-generated
confidence: high
created: 2026-04-13
created_by: copilot
session_context: "Session 2026-04-13: DXDP SDD-Seite analysiert, your-org/your-repo lokal gelesen"
related_to: [KB-2026-001]
sources:
  - "https://your-confluence-instance.example.com
  - "C:\\Author\\agentic-coding-project-template"
  - "https://github.com/Fission-AI/OpenSpec"
  - "https://github.com/github/spec-kit"
  - "https://github.com/cameronsjo/spec-compare"
reviewed_by: null
status: draft
---

# SDD-Frameworks Vergleich: OpenSpec vs. Spec Kit vs. WK SDD Framework

## Kernaussage

Es gibt drei relevante SDD-Frameworks für AI-assisted Development. Authors WK-internes Framework ist technisch ausgereifter in Session-Management und Agent-Governance, hat aber geringere externe Sichtbarkeit.

## Details

### Kurzvergleich

| Feature | OpenSpec | Spec Kit | WK SDD Framework |
|---|---|---|---|
| Backing | Fission-AI (~31k Stars) | GitHub offiziell (~77k Stars) | WK-intern (Author Böhmert) |
| Installation | `npm install -g @fission-ai/openspec` | `uv tool install specify-cli` | PowerShell/Bash-Installer, kein Tool nötig |
| Workflow | Fluid, customizable | constitution → specify → plan → tasks → implement | PLAN → IMPLEMENT → VALIDATE → INTEGRATE |
| Agents | Generische Slash-Commands | Generische Slash-Commands | 7 spezialisierte Agents mit Nicht-Verantwortlichkeiten |
| Session-Kontinuität | ❌ | ❌ | ✅ SESSION_LOG + USER_INTENT_LOG + ARTIFACT_REGISTRY |
| Handoff-Schema | ❌ | ❌ | ✅ explizites handoff.schema.md |
| Anti-Halluzination | ❌ | ❌ | ✅ 70%-Problem explizit adressiert |
| Knowledge-Integration | Nur Codebase | Nur Codebase | context/ + Vault-MCP (workspace-spezifisch) |
| Sichtbarkeit | Community | Community | WK-intern, nicht in spec-compare gelistet |

### Wann welches Framework wählen?

- **OpenSpec:** Brownfield-Projekte, bestehende Node.js-Toolchain, will kein neues Tool lernen
- **Spec Kit:** Greenfield, GitHub-native Team, will phasierte Struktur (constitution-Phase)
- **WK SDD Framework:** WK-intern, Copilot + Jira + Confluence-Stack, braucht Session-Kontinuität und Agent-Governance

## Relevanz für Team-

Der Agentic Workspace implementiert das WK SDD Framework bereits vollständig (Workorders, Agents, Schemas, Prompts). Die wichtigsten Erweiterungen gegenüber externen Frameworks sind die Knowledge-Integration über MCP und die Handoff-Protokolle.

**Gap to close:** Das Framework ist nicht im [spec-compare](https://github.com/cameronsjo/spec-compare)-Repo gelistet und fehlt auf der DXDP SDD-Confluence-Seite.

## Quellen

- [SDD-Seite DXDP Confluence](https://your-confluence-instance.example.com)
- [WK SDD Framework lokal](C:\Author\agentic-coding-project-template)
- [spec-compare Repo](https://github.com/cameronsjo/spec-compare)
- [your-org/your-repo](https://github.com/your-org/your-repo)


