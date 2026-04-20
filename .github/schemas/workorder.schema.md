---
schema_id: workorder
version: 1.0.0
status: ACTIVE
created: 2026-02-06
created_by: developer
reviewed_by: pending
---

# Workorder Schema

This schema defines the structure for Workorder specification files.

---

## Frontmatter (Required)

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
tags: [setup, infrastructure]     # Optional categorization
---
```

---

## Body Structure

### 1. Context (Required)
Brief background explaining why this work is needed.

```markdown
## 1. Context

We need to implement X because Y. This is part of the larger effort to Z.

**Background:**
- Relevant fact 1
- Relevant fact 2

**Trigger:** What initiated this work (user request, bug report, dependency)
```

### 2. Goal (Required)
Clear, measurable objective.

```markdown
## 2. Goal

Implement [specific outcome] so that [benefit/purpose].

**Success looks like:**
- Measurable outcome 1
- Measurable outcome 2
```

### 3. Scope (Required)
Explicit boundaries of what is and is not included.

```markdown
## 3. Scope

### In Scope
- Specific deliverable 1
- Specific deliverable 2
- Specific deliverable 3

### Out of Scope
- Explicitly excluded item 1
- Explicitly excluded item 2
- Future enhancement (separate WO)
```

### 4. Deliverables (Required)
Concrete outputs of this Workorder.

```markdown
## 4. Deliverables

| # | Deliverable | Description | Location |
|---|-------------|-------------|----------|
| 1 | New module | Implements X | `src/module/new.py` |
| 2 | Unit tests | Tests for module | `tests/unit/test_new.py` |
| 3 | Documentation | Usage docs | `docs/new-feature.md` |
```

### 5. Implementation Notes (Optional)
Technical guidance for the implementer.

```markdown
## 5. Implementation Notes

### Approach
Recommended implementation strategy.

### Constraints
- Must use existing pattern from `src/utils/`
- Must not introduce new dependencies
- Must maintain backward compatibility

### References
- Related code: `src/existing/module.py`
- External docs: [Link to documentation]
```

### 6. Tests (Required)
Specific tests that validate the deliverables.

```markdown
## 6. Tests

### Unit Tests
- `tests/unit/test_new.py::test_happy_path` - Normal operation
- `tests/unit/test_new.py::test_edge_case` - Edge case handling
- `tests/unit/test_new.py::test_error_handling` - Error paths

### Integration Tests
- `tests/integration/test_workflow.py` - End-to-end workflow

### Manual Tests
- [ ] Verify UI renders correctly
- [ ] Verify error messages are clear
```

### 7. Definition of Done (Required)
Checklist that must be complete before closing.

```markdown
## 7. Definition of Done

- [ ] All deliverables completed
- [ ] All tests passing
- [ ] Code compiles without errors (`python -m compileall src`)
- [ ] No new linter warnings
- [ ] Documentation updated
- [ ] WO_CATALOG.md updated
- [ ] WO Report created
```

### 8. Risks and Open Questions (Optional)
Known risks and unresolved questions.

```markdown
## 8. Risks and Open Questions

### Risks
| Risk | Impact | Mitigation |
|------|--------|------------|
| API may change | HIGH | Pin version, add adapter layer |
| Performance unknown | MEDIUM | Add benchmarks in tests |

### Open Questions
- [ ] Question 1? (Assigned to: @person)
- [ ] Question 2? (Blocked by: WO05)
```

---

## Extended Sections (Optional)

### 9. Delta Specs (for Brownfield changes)

```markdown
## 9. Delta Specs

### ADDED
- `src/module/new_file.py` – New component for X
- `tests/unit/test_new_file.py` – Tests for new component

### MODIFIED
- `src/module/existing.py` – Added method `foo()` (lines 45-67)
- `config/settings.py` – New config key `FEATURE_FLAG`

### REMOVED
- `src/module/deprecated.py` – Replaced by new_file.py
```

### 10. Requirements Traceability (for large WOs)

```markdown
## 10. Requirements Traceability

### Functional Requirements
| ID | Requirement | Acceptance Criteria | Test |
|----|-------------|---------------------|------|
| FR-001 | User can upload file | File appears in list | `test_upload.py` |
| FR-002 | System validates format | Error on invalid | `test_validation.py` |

### Non-Functional Requirements
| ID | Category | Requirement | Metric |
|----|----------|-------------|--------|
| NFR-001 | Performance | Response < 2s | Load test |
| NFR-002 | Security | No hardcoded secrets | Static analysis |
```

---

## Footer (Required)

```markdown
---

## Changelog

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-02-06 | @author | Initial version |
```

---

## File Naming

```
workorders/WO01_descriptive-title.md
workorders/WO02_another-workorder.md
```

---

## Status Transitions

```
PLANNED → IN_PROGRESS → REVIEW → DONE
    ↓         ↓           ↓
 BLOCKED   BLOCKED     BLOCKED
    ↓         ↓           ↓
CANCELLED CANCELLED   CANCELLED
```

---

## Example

See `workorders/WO00_repo-bootstrap.md` for a complete example.

