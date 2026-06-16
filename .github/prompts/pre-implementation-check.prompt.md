---
mode: agent
description: "Validate a Workorder before implementation against scope, policy, risks, and AC evidence."
tools:
  - "read"
  - "search"
  - "problems"
---

# Pre-Implementation Check

Validate that a Workorder is ready for implementation before Developer starts.

## Context to Load

1. `context/STARTUP_BRIEF.md`
2. `governance/project.profile.yaml`
3. `governance/policy.yaml`
4. `docs/agent-framework/workorder-quality-contract.md`
5. The Workorder under review: ${input:woPath:workorders/WOxx_short-title.md}
6. Relevant ADRs or referenced files

## Checklist

### Workorder Completeness

- [ ] Goal is clear
- [ ] Critical Path Fit is present for non-trivial work
- [ ] In scope and out of scope are explicit
- [ ] Deliverables are concrete
- [ ] Requirements use stable IDs where needed
- [ ] Every AC has evidence
- [ ] Definition of Done is complete
- [ ] Residual gaps are explicit or `none`

### Context and Dependencies

- [ ] Referenced files exist or are intentionally new
- [ ] Dependent Workorders are complete or explicitly not required
- [ ] ADR/schema references are available
- [ ] Test/validation commands are available

### Policy and Risk

- [ ] Security/privacy/legal/external-call impacts are addressed or `N/A`
- [ ] Policy gates are satisfied or marked as blocking
- [ ] Destructive actions are absent or explicitly approved
- [ ] No secrets or private paths are required

## Output

```markdown
## Pre-Implementation Check: [Workorder]

**Gate:** GREEN | YELLOW | RED

### Findings
| # | Severity | Location | Finding | Remediation |
|---|---|---|---|---|

### Evidence Checked
- [...]

### Blockers
- none | [...]

### Recommendation
Ready to implement | Revise before implementation
```
