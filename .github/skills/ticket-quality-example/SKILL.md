---
name: ticket-quality-example
description: >
  Example skill: DoR checklist, Jira ticket template, and quality rules for ticket work.
  Use when creating, reviewing, or improving tickets.
---

# Ticket Quality (Example)

> **This is an example skill.** Replace the content below with your team's Definition of Ready
> and ticket conventions.

## 1. Definition of Ready (DoR) Checklist

A ticket is "ready" when all of the following are met:

- [ ] **Summary** is clear and action-oriented
- [ ] **Description** provides enough context for someone unfamiliar with the topic
- [ ] **Acceptance Criteria** are explicit, testable, and complete
- [ ] **Story Points** are estimated
- [ ] **Priority** is set
- [ ] **Labels** follow team conventions
- [ ] **Dependencies** are identified and linked
- [ ] **Risks** are noted (if any)
- [ ] **Assignee** is set (or explicitly "unassigned" for backlog)

## 2. Ticket Template

```markdown
## Context
[Why does this work need to be done? What problem does it solve?]

## Scope
### In Scope
- Item 1
- Item 2

### Out of Scope
- Item 1

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Technical Notes
[Implementation hints, relevant files, dependencies]

## Dependencies
- Blocked by: [PROJ-XXX]
- Blocks: [PROJ-YYY]

## Definition of Done
- [ ] Code reviewed
- [ ] Tests pass
- [ ] Documentation updated
```

## 3. Quality Rules

- **No vague summaries**: "Fix bug" → "Fix null pointer in user login when email is empty"
- **No missing AC**: Every ticket must have at least 2 testable acceptance criteria
- **No orphan tickets**: Every ticket links to an epic or initiative
- **Estimate before sprint**: Unestimated tickets cannot enter a sprint


