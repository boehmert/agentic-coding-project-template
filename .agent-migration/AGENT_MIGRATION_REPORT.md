# Agent Framework Migration Report

**Repo:** agentic-coding-project-template  
**Date:** 2026-06-16  
**Requested by:** Carsten  
**Migration target:** Adopt the slim, policy-driven CIS agent workflow mechanics without turning this repository into CIS.

## Summary

This migration updates the template's agent framework from a broad always-on
multi-agent model to a smaller policy-driven model:

- Orchestrator Lite routes, classifies, enforces policy gates, and delegates.
- Core implementation flow is Workorder Planner -> Developer -> Reviewer ->
  Documenter when evidence/reporting is needed.
- Domain, risk, discovery, lead, and planning agents are on-demand only.
- Governance policy, routing policy, project profile, workflow modes, and
  Workorder evidence contract are now explicit repository artifacts.

Repo-specific adaptation: this repository uses `context/` and `workorders/`.
No `SDD/context/` or `SDD/workorders/` structure was introduced.

## Target Repo Inventory

| Area | Existing state before migration | Migration action |
|---|---|---|
| `AGENTS.md` | Large tiered team roster with Lead Coordinator and domain layers prominent | Replaced with concise routing entrypoint |
| `.github/agents/` | 25 active agents | Core agents replaced/adapted; optional roles kept on-demand; Mira added |
| `.github/prompts/` | 29 prompts | Workorder, ADR, and pre-implementation prompts adapted to policy/evidence model |
| `.github/instructions/` | 18 instructions including template-maintenance | Added common, context-management, spec-quality, and prompt-quality rules |
| Context | `context/` with registry, logs, decisions, sprint state | Added `context/STARTUP_BRIEF.md` |
| Workorders | `workorders/`, template, catalog, example | Workorder template adapted to evidence contract |
| Governance | Goals/activity log only | Added project profile, routing policy, and policy gates |
| Agent framework docs | none | Added workflow modes and Workorder quality contract |

## Replaced

- `AGENTS.md`
- `.github/copilot-instructions.md`
- `.github/agents/orchestrator.agent.md`
- `.github/agents/workorder-planner.agent.md`
- `.github/agents/developer.agent.md`
- `.github/agents/reviewer.agent.md`
- `.github/agents/documenter.agent.md`
- `.github/agents/architect.agent.md`
- `.github/agents/lead-coordinator.agent.md`
- `.github/agents/project-planner.agent.md`
- `.github/prompts/create-workorder.prompt.md`
- `.github/prompts/pre-implementation-check.prompt.md`
- `.github/prompts/create-adr.prompt.md`
- `workorders/_template/workorder-template.md`

## Added

- `context/STARTUP_BRIEF.md`
- `governance/project.profile.yaml`
- `governance/routing-policy.yaml`
- `governance/policy.yaml`
- `docs/agent-framework/workflow-modes.md`
- `docs/agent-framework/workorder-quality-contract.md`
- `.github/agents/mira-visionary-discovery.agent.md`
- `.github/instructions/agent-common.instructions.md`
- `.github/instructions/context-management.instructions.md`
- `.github/instructions/spec-quality.instructions.md`
- `.github/instructions/prompt-quality.instructions.md`

## Archived

Previous active routing/core files were copied to:

- `.agent-migration/archive-20260616/root/AGENTS.md`
- `.agent-migration/archive-20260616/agents/orchestrator.agent.md`
- `.agent-migration/archive-20260616/agents/workorder-planner.agent.md`
- `.agent-migration/archive-20260616/agents/developer.agent.md`
- `.agent-migration/archive-20260616/agents/reviewer.agent.md`
- `.agent-migration/archive-20260616/agents/documenter.agent.md`
- `.agent-migration/archive-20260616/agents/architect.agent.md`
- `.agent-migration/archive-20260616/agents/lead-coordinator.agent.md`
- `.agent-migration/archive-20260616/agents/project-planner.agent.md`

## Adapted, Not Blind-Copied

- CIS `SDD/context/STARTUP_BRIEF.md` was not copied. A new
  `context/STARTUP_BRIEF.md` was written for this template.
- CIS policies were adapted to this repository's paths and validation commands.
- Core agents were rewritten against `context/`, `workorders/`, `_tools/`, and
  `tasks/validate-output/run.py`.
- Mira was generalized for template/product discovery and stripped of CIS module
  references.

## Not Adopted from CIS

- CIS product state, sprint state, historical session logs, and workorders
- CIS wiki/knowledge artifacts
- Festival, Jobsearch, Receipt, Photo, Ghostwriter, Token Economy, My-Workspace
  artifacts
- CIS private paths, `.env`, credentials, tokens, or provider state
- CIS-specific prompt-time knowledge retrieval commands
- CIS metrics files and product test commands

## Validation Checklist

| Check | Result | Evidence |
|---|---|---|
| Orchestrator has no write/execute/install/terminal tools | PASS | `.github/agents/orchestrator.agent.md` tool list contains only read/search/delegate tools. |
| On-demand roles marked | PASS | `AGENTS.md`, `governance/routing-policy.yaml`, optional agent frontmatter, and manifest mark optional roles on-demand. |
| No CIS product artifacts copied | PASS | Search found only explicit no-copy/negative references in this report and startup brief. |
| No secrets or local private paths copied | PASS | Targeted search found no token/key/private-path values; remaining matches are false positives in existing prose. |
| Smoke validation runs | PASS | `python3 tasks/validate-output/run.py` passed. |
| Strict frontmatter validation | PASS | `python3 -m _tools.validate.frontmatter_check --path .github --strict` passed. |
| Python compile smoke | PASS | `python3 -m compileall _tools tasks` passed. |
| `git diff --check` clean | PASS | `git diff --check` passed. |

## Open Risks

- Legacy optional domain agent files still contain older long-form persona bodies.
  Runtime routing and frontmatter now mark them on-demand, but a future cleanup
  should align their full bodies with the slim policy-driven model.
- Strict frontmatter validation is now clean after updating prompt-field support
  and shortening long optional-agent descriptions.
- This template still has no CI, test suite, dependency lock, or secret-scan
  workflow. These remain recommended hardening items.
