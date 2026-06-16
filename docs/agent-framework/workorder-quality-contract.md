# Workorder Quality Contract

**Date:** 2026-06-16  
**Status:** active  
**Scope:** New non-trivial Workorders in this template repository

## Purpose

Workorders must be traceable from intent to evidence. A Workorder is ready for
implementation only when a Developer can execute it without inventing scope,
acceptance criteria, or validation strategy.

## Required Workorder Elements

| Area | Requirement |
|---|---|
| Goal | One clear outcome and why it matters for this template or derived users |
| Scope | Explicit in-scope and out-of-scope items |
| Critical Path Fit | Manifest/user request, user value, contribution, delay cost, and non-goals |
| Requirements | Stable IDs such as `REQ-001` |
| Acceptance Criteria | Stable IDs such as `AC-001` |
| Evidence | Every AC maps to executable or reviewable evidence |
| Impact | Architecture, Security, Privacy, Legal, External Call impact or explicit `N/A` |
| Assumptions | Stable IDs such as `ASM-001`, marked blocking or non-blocking |
| Risks | Stable IDs such as `RSK-001` with mitigation |
| Dependencies | Prior Workorders, ADRs, files, tools, or external approvals |
| Definition of Done | Validation commands, reports, docs updates, catalog/state updates |
| Residual Gaps | Deferred items and known gaps; write `none` only if no known gap exists |

## Acceptance Criteria Evidence

No Acceptance Criterion without planned evidence.

Evidence may be:

- automated test
- smoke command
- compile/lint/static validation
- schema/frontmatter validation
- manual review checklist
- deterministic diff or artifact check
- documented human approval where policy requires it

Use this table shape:

| AC | Evidence | Owner |
|---|---|---|
| AC-001 | `python3 tasks/validate-output/run.py` | Developer |
| AC-002 | Reviewer checklist | Reviewer |

## Optional Suggestion Classification

Adjacent work must be classified before it changes scope:

| Classification | Meaning | Action |
|---|---|---|
| `critical_path` | Required for the current outcome | May enter active scope |
| `quality_bar` | Needed for credible maintainability/reviewability | May enter scope if small and evidenced |
| `risk_reduction` | Reduces immediate policy/security/privacy/legal/delivery risk | Requires relevant gate |
| `roadmap_candidate` | Valuable later | Route to Project Planner or backlog |
| `parking_lot` | Plausibly useful but not ready | Record outside implementation scope |
| `do_not_do_now` | Distracting, duplicate, or contrary to policy | Keep out of scope |

## Completion Report Requirements

Completion reports must include:

- deliverable status
- Acceptance Criteria Evidence
- Critical Path Fit and scope-drift notes
- validation commands and outcomes
- residual gaps and follow-up
- changed control artifacts when status changes

## Reviewer Gate

Reviewer decisions:

- `GREEN`: scope met, evidence acceptable, no blocking gaps
- `YELLOW`: non-blocking quality gaps or documented residual risk
- `RED`: missing/deviant deliverable, untestable AC, policy violation, or blocking risk
