---
mode: agent
description: "Create or refine a Workorder with Critical Path Fit, scope, risks, AC evidence, and validation plan."
tools:
  - "read"
  - "search"
  - "edit"
---

# Create Workorder

Create or refine a Workorder for this template repository.

## Context to Load

Read only what is needed:

1. `context/STARTUP_BRIEF.md`
2. `governance/project.profile.yaml`
3. `governance/routing-policy.yaml`
4. `governance/policy.yaml`
5. `docs/agent-framework/workorder-quality-contract.md`
6. `workorders/WO_CATALOG.md`
7. `workorders/_template/workorder-template.md`

## Inputs

- **Title:** ${input:title:Descriptive title}
- **Priority:** ${input:priority:MEDIUM}
- **Effort:** ${input:effort:2-4 hours}
- **Context:** ${input:context:Why is this needed?}
- **Trigger:** ${input:trigger:What triggered this work?}

## Task

Produce a Workorder that is implementation-ready or state why it is not ready.

Required:

- explicit goal and value
- Critical Path Fit
- in-scope and out-of-scope items
- `REQ-*`, `AC-*`, `TEST-*`, `ASM-*`, and `RSK-*` IDs where relevant
- evidence for every AC
- architecture/security/privacy/legal/external-call impact or `N/A`
- validation commands
- residual gaps or `none`
- optional-suggestion classification

Do not include scope just because it is adjacent. Classify it first.

## Output

1. Present a short Workorder summary for approval.
2. If approved, save to `workorders/WOxx_short-title.md`.
3. Update `workorders/WO_CATALOG.md`.

Use repo-relative paths only.
