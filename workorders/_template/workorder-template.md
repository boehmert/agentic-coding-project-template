---
id: WO-YYYY-NNN
title: "<Workorder title>"
version: 1.0.0
status: PLANNED
created: YYYY-MM-DD
created_by: workorder-planner
reviewed_by: pending
parent_spec: null
priority: MEDIUM
estimated_effort: "2-4 hours"
workflow_mode: standard
---

# WO-YYYY-NNN: <Title>

## 1. Context

Why does this work exist? What triggered it? Reference user request, decision,
roadmap item, bug report, or template maintenance need.

## 2. Goal

State the smallest valuable outcome.

## 3. Critical Path Fit

**Source:** explicit user request | manifest item | roadmap item | decision ID
**User/Template Value:** Who benefits and how?
**Contribution:** Blocker removed | value delivered | risk reduced | delivery integrity preserved
**If Not Done Now:** Cost of delay or why delay is acceptable
**Not On Critical Path:** Explicit non-goals

## 4. Scope

### In Scope

- [ ] OUT-001:

### Out of Scope

- [ ] OOS-001:

### Optional Suggestion Classification

| Item | Classification | Decision |
|---|---|---|
|  | critical_path | include |

Allowed classifications: `critical_path`, `quality_bar`, `risk_reduction`,
`roadmap_candidate`, `parking_lot`, `do_not_do_now`.

## 5. Requirements

| ID | Requirement | Notes |
|---|---|---|
| REQ-001 |  |  |

## 6. Acceptance Criteria and Evidence

| AC | Acceptance Criterion | Evidence | Owner |
|---|---|---|---|
| AC-001 |  | TEST-001 | developer |

## 7. Evidence Plan

| ID | Evidence Type | Command / Checklist / Artifact |
|---|---|---|
| TEST-001 | smoke | `python3 tasks/validate-output/run.py` |

## 8. Impact Review

| Area | Impact | Notes |
|---|---|---|
| Architecture | N/A |  |
| Security | N/A |  |
| Privacy / Personal Data | N/A |  |
| Legal / Regulatory | N/A |  |
| External Calls | N/A |  |
| API / Schema | N/A |  |
| Dependencies | N/A |  |

## 9. Assumptions

| ID | Assumption | Blocking? | Validation |
|---|---|---|---|
| ASM-001 |  | no |  |

## 10. Risks

| ID | Risk | Probability | Impact | Mitigation |
|---|---|---|---|---|
| RSK-001 |  | Medium | Medium |  |

## 11. Dependencies

| Dependency | Status | Notes |
|---|---|---|
|  |  |  |

## 12. Definition of Done

- [ ] All deliverables completed
- [ ] All AC evidence collected
- [ ] Relevant validation commands run
- [ ] Reviewer gate completed
- [ ] Docs/catalog/state updated if needed
- [ ] Completion handoff or report created

## 13. Residual Gaps

Write `none` if no known gaps remain.

## Changelog

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0.0 | YYYY-MM-DD | workorder-planner | Initial version |
