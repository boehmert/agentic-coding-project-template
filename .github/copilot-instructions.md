---
name: Agentic Coding Project Template
description: Global guardrails for AI coding agents in this workspace.
applyTo: "**"
---

# Copilot Instructions - Agentic Coding Workspace

This repository is an AI-assisted development template. It uses a slim,
policy-driven workflow with Orchestrator Lite as router and on-demand specialist
agents.

For structure and boundaries see:

- `AGENTS.md`
- `ARCHITECTURE.md`
- `docs/TEMPLATE_USAGE.md`
- `context/STARTUP_BRIEF.md`
- `governance/project.profile.yaml`
- `governance/routing-policy.yaml`
- `governance/policy.yaml`

## Core Rules

1. Workspace files are the source of truth.
2. Policy beats persona.
3. Use the smallest safe workflow mode.
4. Do not activate domain experts by default.
5. Do not expose, persist, log, or report secrets.
6. External writes and external calls require explicit approval when policy says so.
7. Destructive or irreversible changes require explicit approval.
8. AI concurrence is not independent assurance.
9. Non-trivial work needs scope, acceptance criteria, and evidence.
10. If evidence is insufficient, mark assumptions or escalate.

## Startup Context

Use hot context first:

1. `context/STARTUP_BRIEF.md`
2. `governance/project.profile.yaml`
3. `governance/routing-policy.yaml`
4. `governance/policy.yaml`
5. active Workorder, if any
6. active `[BLOCKED]` decisions in `context/decisions-pending.md`

Do not load full `context/SESSION_LOG.md` by default.

## Workflow Modes

See `docs/agent-framework/workflow-modes.md`.

- `lightweight`: small local reversible work
- `standard`: normal feature/template work
- `high_risk`: security, privacy, legal, API/schema, infra, LLM/RAG, external effects, dependencies, irreversible changes
- `discovery`: ideas, vision, roadmap, opportunity discovery

## Workorder Quality

See `docs/agent-framework/workorder-quality-contract.md`.

Every non-trivial Workorder needs:

- Critical Path Fit
- explicit in/out scope
- stable requirement and AC IDs
- evidence for every AC
- risk and assumption tracking
- policy impact review or explicit `N/A`
- validation commands or manual review evidence

## Agent Routing

- Orchestrator Lite routes and enforces gates. It does not edit, execute, or make domain decisions.
- Workorder Planner creates/refines specs.
- Developer implements approved scope.
- Reviewer issues GREEN/YELLOW/RED gate decisions.
- Documenter writes final docs/reports after evidence exists.
- Architect, Lead Coordinator, Project Planner, Mira, and domain/risk agents are on-demand only.

## External Systems

MCP servers are configured in `.vscode/mcp.json` from `docs/mcp.json.template`.
Do not put credentials into tracked files. Keep secrets in `.env` or approved
secret storage only.
