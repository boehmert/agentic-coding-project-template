# Spec-Driven Development Framework – Context for External AI

This document provides context for AI assistants to generate framework-compliant artifacts.

---

## 1. Core Workflow

```
PLAN → IMPLEMENT → VALIDATE → INTEGRATE
  │         │           │           │
Planner  Developer   Reviewer   Integrator
```

**Rule: No code without a Workorder.**

---

## 2. Agent Roles

| Agent | Responsibility | NOT Responsible For |
|-------|----------------|---------------------|
| **Architect** | System design, ADRs, technology decisions | Writing code |
| **Workorder Planner** | Create Workorders, define scope, identify risks | Implementation |
| **Developer** | Implement Workorders, write code and tests | Creating Workorders, reviewing own work |
| **Reviewer** | Pre-implementation check, post-implementation review | Writing code |
| **Integrator** | Merge branches, resolve conflicts, prepare PRs | Code review |
| **Documenter** | Documentation, guides, reports | Implementation |
| **Security Reviewer** | Security analysis, OWASP checks | General code review |

**Key principle:** Each agent has focused responsibilities. Handoffs between agents must be explicit.

---

## 3. Workorder Schema

### 3.1 Frontmatter (Required)

```yaml
---
id: WO01                          # Unique identifier (WOxx format)
title: "Descriptive Title"        # Human-readable title
version: 1.0.0                    # Semantic version
status: PLANNED                   # PLANNED | IN_PROGRESS | REVIEW | DONE | BLOCKED | CANCELLED
created: 2026-02-06               # ISO date
created_by: human                 # human | agent-name
reviewed_by: pending              # reviewer-name | pending | N/A
parent_spec: null                 # null | WOxx (if derived from another WO)
depends_on: []                    # List of WO IDs that must be completed first
priority: MEDIUM                  # LOW | MEDIUM | HIGH | CRITICAL
estimated_effort: "2-4 hours"     # Time estimate
---
```

### 3.2 Body Structure

```markdown
## 1. Context
Brief background explaining why this work is needed.
- What triggered this work?
- Relevant facts

## 2. Goal
Clear, measurable objective.
- What success looks like
- Measurable outcomes

## 3. Scope

### In Scope
- Specific deliverable 1
- Specific deliverable 2

### Out of Scope
- Explicitly excluded item 1
- Future enhancement (separate WO)

## 4. Deliverables

| # | Deliverable | Description | Location |
|---|-------------|-------------|----------|
| 1 | New module | Implements X | `src/module/new.py` |
| 2 | Unit tests | Tests for module | `tests/unit/test_new.py` |
| 3 | Documentation | Usage docs | `docs/feature.md` |

## 5. Implementation Notes (Optional)
Technical guidance, constraints, references.

## 6. Tests

### Unit Tests
- `test_happy_path` – Normal operation
- `test_edge_case` – Edge case handling
- `test_error_handling` – Error paths

### Integration Tests (if applicable)
- End-to-end workflow tests

## 7. Definition of Done
- [ ] All deliverables completed
- [ ] All tests passing
- [ ] Code compiles without errors
- [ ] No new linter warnings
- [ ] Documentation updated
- [ ] WO_CATALOG.md updated

## 8. Risks and Open Questions (Optional)

### Risks
| Risk | Impact | Mitigation |
|------|--------|------------|
| Risk description | HIGH/MEDIUM/LOW | How to mitigate |

### Open Questions
- [ ] Question 1?
- [ ] Question 2?
```

### 3.3 Changelog (Required at end)

```markdown
---

## Changelog

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-02-06 | @author | Initial version |
```

---

## 4. Workorder Sizing Guide

| Effort | Scope | Example |
|--------|-------|---------|
| 1-2 hours | Single file change | Bug fix, config update |
| 2-4 hours | Few files, isolated | New utility function |
| 1-2 days | New component | New API endpoint |
| 3-5 days | Feature with tests | User-facing feature |
| 1 week+ | Multiple components | **Split into smaller WOs** |

---

## 5. ADR Schema (Architecture Decision Records)

### Frontmatter

```yaml
---
id: ADR-001
title: "Decision Title"
version: 1.0.0
status: PROPOSED                  # PROPOSED | ACCEPTED | DEPRECATED | SUPERSEDED
created: 2026-02-06
created_by: architect
reviewed_by: pending
supersedes: null                  # ADR-xxx if replacing another
---
```

### Body Structure

```markdown
## 1. Context
Situation and forces at play.

## 2. Decision
What we decided and key points.

## 3. Options Considered

### Option A: [Name]
**Pros:** ...
**Cons:** ...
**Effort:** Low/Medium/High

### Option B: [Name]
**Pros:** ...
**Cons:** ...
**Effort:** Low/Medium/High

## 4. Rationale
Why this option was chosen.

## 5. Consequences
### Positive
### Negative
### Neutral
```

---

## 6. Markdown Standards

### Headings
- H1 (`#`): Document title only, once
- H2 (`##`): Major sections
- H3 (`###`): Subsections
- Never skip levels

### Code
- Inline: `backticks` for file names, functions, variables
- Blocks: Always specify language (```python, ```yaml, etc.)

### Tables
```markdown
| Column 1 | Column 2 |
|----------|----------|
| Value 1  | Value 2  |
```

### File Naming
- Workorders: `WO01_descriptive-title.md`
- ADRs: `ADR-001_decision-title.md`
- Reports: `WO01_report_2026-02-06.md`

---

## 7. Quality Gates

### Pre-Implementation Check (Before coding)

Must verify:
- [ ] Workorder is complete (Goal, Scope, DoD, Tests)
- [ ] All referenced files exist
- [ ] Dependencies are met (prior WOs complete)
- [ ] Architecture is aligned

**Status:** 🟢 GREEN (proceed) | 🟡 YELLOW (caveats) | 🔴 RED (blocked)

### Post-Implementation Review (After coding)

Must verify:
- [ ] All deliverables present
- [ ] All acceptance criteria met
- [ ] Tests passing
- [ ] Code standards followed

---

## 8. Key Principles

1. **Specs Before Code** – Every change needs a Workorder
2. **The 70% Problem** – AI output is "almost right"; always verify
3. **Explicit Scope** – In/Out boundaries prevent scope creep
4. **Testable Criteria** – Acceptance criteria must be verifiable
5. **Small Increments** – Keep Workorders focused and reviewable
6. **Provenance** – Every artifact has version, author, date

---

## 9. Example: Minimal Workorder

```markdown
---
id: WO01
title: "Add health check endpoint"
version: 1.0.0
status: PLANNED
created: 2026-02-06
created_by: human
priority: MEDIUM
estimated_effort: "2 hours"
---

## 1. Context
The API needs a health check endpoint for load balancer monitoring.

## 2. Goal
Provide a `/health` endpoint that returns service status.

## 3. Scope

### In Scope
- GET /health endpoint
- Return 200 with status JSON
- Unit test

### Out of Scope
- Detailed dependency checks
- Authentication

## 4. Deliverables

| # | Deliverable | Location |
|---|-------------|----------|
| 1 | Health endpoint | `src/api/health.py` |
| 2 | Unit test | `tests/unit/test_health.py` |

## 5. Tests
- Returns 200 with `{"status": "ok"}`
- Response time < 100ms

## 6. Definition of Done
- [ ] Endpoint implemented
- [ ] Test passing
- [ ] Documentation updated

---

## Changelog

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-02-06 | @human | Initial version |
```

---

## 10. Instructions for AI

When creating Workorders:
1. Always include complete frontmatter
2. Define explicit In Scope / Out of Scope
3. List concrete deliverables with file locations
4. Specify testable acceptance criteria
5. Include Definition of Done checklist
6. Add Changelog section

When unclear, ask:
- What is the goal?
- What is explicitly out of scope?
- What are the acceptance criteria?
- What priority and effort estimate?

---

*Framework Version: 1.0.0*
