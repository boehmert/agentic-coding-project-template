---
name: Spec-Driven Development Rules
description: Rules for creating and managing specification artifacts.
applyTo: "**"
---

# Spec-Driven Development Rules

This file defines the rules for creating, managing, and versioning specification artifacts.

---

## 1. Artifact Types

| Type | Purpose | Location | Schema |
|------|---------|----------|--------|
| Workorder | Executable work specification | `workorders/WOxx_*.md` | `workorder.schema.md` |
| ADR | Architecture decision record | `docs/adr/ADR-xxx_*.md` | `adr.schema.md` |
| Report | Workorder completion report | `workorders/reports/WOxx_report_*.md` | `report.schema.md` |
| Schema | Data contract definition | `schemas/*.schema.md` | – |
| Handoff | Agent-to-agent context transfer | (inline or temp) | `handoff.schema.md` |

---

## 2. Mandatory Frontmatter

Every specification artifact **must** include YAML frontmatter with these fields:

### Workorders
```yaml
---
id: WO01
title: "Descriptive Title"
version: 1.0.0
status: PLANNED | IN_PROGRESS | REVIEW | DONE | BLOCKED
created: 2026-02-06
created_by: [human | agent-name]
reviewed_by: [reviewer-name | pending]
parent_spec: null | WO00
priority: LOW | MEDIUM | HIGH | CRITICAL
estimated_effort: "2-4 hours" | "1-2 days" | "1 week"
---
```

### ADRs
```yaml
---
id: ADR-001
title: "Decision Title"
version: 1.0.0
status: PROPOSED | ACCEPTED | DEPRECATED | SUPERSEDED
created: 2026-02-06
created_by: [human | agent-name]
reviewed_by: [reviewer-name | pending]
supersedes: null | ADR-000
superseded_by: null | ADR-002
---
```

### Reports
```yaml
---
workorder_id: WO01
version: 1.0.0
status: DRAFT | FINAL
created: 2026-02-06
created_by: [agent-name]
reviewed_by: [human | pending]
---
```

---

## 3. Versioning Rules

### Semantic Versioning for Specs
- **MAJOR** (1.0.0 → 2.0.0): Breaking changes to scope or acceptance criteria
- **MINOR** (1.0.0 → 1.1.0): Additive changes (new deliverables, refined details)
- **PATCH** (1.0.0 → 1.0.1): Clarifications, typo fixes, no semantic change

### Version Update Protocol
1. Never overwrite previous versions silently
2. Update frontmatter `version` field
3. Add changelog entry at bottom of document
4. For major changes, consider creating a new spec instead

---

## 4. Provenance Tracking

### Required References
Every spec must reference its sources:
- `parent_spec`: The spec this was derived from (if any)
- `depends_on`: List of specs that must be completed first
- `related_to`: Other relevant specs (informational)

### Changelog Section
Every spec should end with a changelog:
```markdown
---

## Changelog

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-02-06 | @human | Initial version |
| 1.0.1 | 2026-02-07 | @reviewer | Clarified acceptance criteria |
```

---

## 5. Workflow: Plan → Implement → Validate → Integrate

### Phase 1: Plan
1. Create Workorder using schema template
2. Define scope (in/out), deliverables, acceptance criteria
3. Run pre-implementation check
4. Get user approval before proceeding

### Phase 2: Implement
1. Work strictly within approved scope
2. Write code in small, reviewable chunks
3. Create/update tests for each change
4. Document decisions in code comments

### Phase 3: Validate
1. Run all specified tests
2. Check against acceptance criteria
3. Review for security, performance, architecture
4. Create validation report

### Phase 4: Integrate
1. Prepare PR with clear description
2. Update WO_CATALOG.md
3. Create WO Report
4. Archive or close Workorder

---

## 6. Delta-Specs (for Brownfield Changes)

When modifying existing code, include a Delta-Spec section:

```markdown
## Delta Specs

### ADDED
- `src/module/new_file.py` – New component for X
- `tests/test_new_file.py` – Tests for new component

### MODIFIED
- `src/module/existing.py` – Added method `foo()` (lines 45-67)
- `config/settings.py` – New config key `FEATURE_FLAG`

### REMOVED
- `src/module/deprecated.py` – Replaced by new_file.py
```

---

## 7. FR/NFR Traceability (for Large Workorders)

For Workorders with >5 deliverables or >1 week effort, add requirements tables:

### Functional Requirements
```markdown
| ID | Requirement | Acceptance Criteria | Test |
|----|-------------|---------------------|------|
| FR-001 | User can upload file | File appears in list | `test_upload.py` |
| FR-002 | System validates format | Error on invalid | `test_validation.py` |
```

### Non-Functional Requirements
```markdown
| ID | Category | Requirement | Metric |
|----|----------|-------------|--------|
| NFR-001 | Performance | Response < 2s | Load test |
| NFR-002 | Security | No hardcoded secrets | Static analysis |
```

Use IDs (FR-001, NFR-001) in code comments and test docstrings for traceability.

---

## 8. Catalog Management

### WO_CATALOG.md Structure
```markdown
# Workorder Catalog

| ID | Title | Status | Priority | Created | Completed |
|----|-------|--------|----------|---------|-----------|
| WO01 | Repo Bootstrap | DONE | HIGH | 2026-02-01 | 2026-02-02 |
| WO02 | Feature X | IN_PROGRESS | MEDIUM | 2026-02-03 | – |
```

### Update Rules
- Update status immediately when Workorder state changes
- Add completion date when status becomes DONE
- Never delete rows – mark as DONE or CANCELLED
