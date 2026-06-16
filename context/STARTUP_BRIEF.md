# STARTUP_BRIEF

**Last updated:** 2026-06-16  
**Updated by:** orchestrator  
**Status:** active

## Active Goal

Operate this repository as a reusable agentic coding project template. The
current framework direction is a slim, policy-driven agent team: Orchestrator
Lite routes and enforces policy gates; execution and domain agents are activated
only when needed.

## Active Workflow Mode

standard

## Active Workorder

No active Workorder is registered in `workorders/WO_CATALOG.md`.

## Current State

This repository uses root-level template paths:

- `context/` for hot context and steering state
- `workorders/` for Workorders and Workorder catalog
- `docs/adr/` for ADRs
- `.github/agents/`, `.github/prompts/`, `.github/instructions/` for agent setup
- `_tools/` and `tasks/` for local Python utilities

It does not use CIS `SDD/context/` or `SDD/workorders/` paths.

## Open Decisions

Use `context/decisions-pending.md` as the source of truth for active
`[BLOCKED]` or `[DEFERRED]` decisions.

## Binding Constraints

- Follow `governance/project.profile.yaml`.
- Follow `governance/routing-policy.yaml`.
- Follow `governance/policy.yaml`.
- Use the smallest safe workflow mode.
- Do not activate domain experts by default.
- Do not treat AI concurrence as independent assurance.
- Do not copy source-repo product artifacts into this template.
- Do not persist secrets, local private paths, raw private logs, or external
  credentials.

## Relevant Artifacts

| Artifact | Why relevant | Status |
|---|---|---|
| `governance/project.profile.yaml` | Repo-specific paths, commands, and assumptions | active |
| `governance/routing-policy.yaml` | Workflow mode and agent activation source of truth | active |
| `governance/policy.yaml` | Policy gates for risky actions | active |
| `docs/agent-framework/workflow-modes.md` | Human-readable workflow mode reference | active |
| `docs/agent-framework/workorder-quality-contract.md` | Workorder quality and evidence rules | active |
| `docs/TEMPLATE_USAGE.md` | Template usage and maintenance contract | active |
| `.agent-migration/AGENT_MIGRATION_REPORT.md` | Migration inventory and validation state | active |
| `context/ARTIFACT_REGISTRY.md` | Artifact registry | active |
| `workorders/WO_CATALOG.md` | Workorder registry | active |

## Files Likely Relevant for Agent Framework Work

- `AGENTS.md`
- `.github/agents/`
- `.github/prompts/`
- `.github/instructions/`
- `.github/schemas/`
- `.github/FRAMEWORK_MANIFEST.md`
- `README.md`
- `ARCHITECTURE.md`
- `COPILOT.md`
- `docs/TEMPLATE_USAGE.md`
- `workorders/`
- `context/`
- `governance/`

## Do Not Load Unless Needed

- Full `context/SESSION_LOG.md`
- Archived Workorders or migration archives
- Generated output under `output/`
- User-supplied files under `inbox/`
- Historical wiki entries unrelated to the current task

## Recovery Hint for Fresh Sessions

Start here, then read the routing policy, governance policy, project profile,
active Workorder if any, pending decisions, and only the targeted files required
for the current request.
