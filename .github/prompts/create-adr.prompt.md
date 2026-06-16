---
mode: agent
description: "Format an approved or proposed architecture decision as an ADR with trade-offs, consequences, and reversal condition."
tools:
  - "read"
  - "search"
  - "edit"
  - "fetch"
---

# Create ADR

Create an Architecture Decision Record. Architect owns decision content;
this prompt owns ADR formatting, numbering, filename, and quality checklist.

## Context to Load

1. `context/STARTUP_BRIEF.md`
2. `governance/project.profile.yaml`
3. existing ADRs in `docs/adr/`
4. active Workorder or decision brief, if any
5. targeted files affected by the decision

## ADR Triggers

Create or propose an ADR when:

- a top-level module or boundary changes
- an API/schema/data contract changes
- persistence, dependency, or integration strategy changes
- a policy-relevant irreversible decision is made
- multiple Workorders depend on the decision

Do not create ADRs for local helper refactors, renames, or routine cleanup.

## Required Fields

- Context
- Decision
- Options considered
- Rationale
- Trade-offs accepted
- Consequences
- Reversal condition
- Implementation constraints
- Evidence grade

## Output

Save to:

```text
docs/adr/ADR-xxx_short-title.md
```

Use repo-relative paths only. If the decision is not approved, set
`status: PROPOSED`.
