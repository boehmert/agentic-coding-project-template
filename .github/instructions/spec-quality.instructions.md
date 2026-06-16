---
description: "SPEC and Workorder quality rules: evidence mapping, stable IDs, risks, assumptions, and completion evidence."
applyTo: "workorders/**/*.md, .github/prompts/create-workorder.prompt.md, .github/schemas/workorder.schema.md, .github/schemas/report.schema.md"
priority: recommended
---

# SPEC and Workorder Quality Instructions

## Rule

No Acceptance Criterion without planned evidence.

Every AC must map to at least one of:

- automated test
- smoke command
- contract test
- schema validation
- property or invariant check
- manual review checklist
- metric check

## Required IDs

Use stable IDs:

- `OUT-001` outcome
- `PRB-001` problem
- `REQ-001` requirement
- `AC-001` acceptance criterion
- `NFR-001` non-functional requirement
- `ASM-001` assumption
- `RSK-001` risk
- `DEC-001` decision
- `TEST-001` evidence

## Required Fields for Non-Trivial Workorders

- Goal
- Context
- Critical Path Fit
- In Scope
- Out of Scope
- Requirements
- Acceptance Criteria
- Executable Evidence
- Edge Cases
- Non-Functional Requirements
- Assumptions
- Risks
- Dependencies
- Definition of Done
- Traceability

## Completion Report Requirements

Every completion report must include:

- deliverable status
- Acceptance Criteria Evidence
- validation commands and outcomes
- residual gaps and follow-up
- updated control artifacts when status changes

If there are no residual gaps, write `none` explicitly.
