---
schema_id: report
version: 1.0.0
status: ACTIVE
created: 2026-02-06
created_by: developer
reviewed_by: pending
---

# Report Schema (Workorder Completion Report)

This schema defines the structure for Workorder completion reports.

---

## Frontmatter (Required)

```yaml
---
workorder_id: WO01                # Reference to completed Workorder
title: "WO01 Completion Report"   # Report title
version: 1.0.0                    # Report version
status: FINAL                     # DRAFT | FINAL
created: 2026-02-06               # ISO date
created_by: developer             # Agent or human who completed the work
reviewed_by: pending              # Reviewer name or pending
completion_date: 2026-02-06       # When work was completed
model: "Claude Opus 4.5"          # AI model used for implementation
token_usage:                      # Token consumption (optional but recommended)
  input: 45000                    # Approximate input tokens
  output: 12000                   # Approximate output tokens
  total: 57000                    # Total tokens consumed
---
```

### Model Tracking Fields

| Field | Required | Description |
|-------|----------|-------------|
| `model` | Recommended | AI model used (e.g., "Claude Opus 4.5", "GPT-4o", "Claude Sonnet 4") |
| `token_usage.input` | Optional | Approximate input tokens consumed |
| `token_usage.output` | Optional | Approximate output tokens generated |
| `token_usage.total` | Optional | Total tokens (for cost analysis) |

**Note:** Token counts are estimates. Use for trend analysis, not precise billing.

---

## Body Structure

### 1. Summary (Required)
Brief overview of what was accomplished.

```markdown
## 1. Summary

Completed implementation of [feature/fix] as specified in WO01.

**Key Outcomes:**
- Outcome 1
- Outcome 2
- Outcome 3

**Duration:** [Actual time spent]
**Estimated vs Actual:** [2-4 hours] vs [3 hours]
```

### 2. Deliverables (Required)
Status of each deliverable from the Workorder.

```markdown
## 2. Deliverables

| # | Deliverable | Status | Location | Notes |
|---|-------------|--------|----------|-------|
| 1 | New module | ✅ Done | `src/module/new.py` | – |
| 2 | Unit tests | ✅ Done | `tests/unit/test_new.py` | 95% coverage |
| 3 | Documentation | ✅ Done | `docs/new-feature.md` | – |
| 4 | Config update | ⚠️ Partial | `config/settings.py` | Needs review |
```

**Legend:**
- ✅ Done: Fully completed
- ⚠️ Partial: Partially completed (explain in Notes)
- ❌ Blocked: Could not complete (explain in Notes)
- ⏭️ Deferred: Moved to different Workorder

### 3. Changes Made (Required)
Detailed list of all changes.

```markdown
## 3. Changes Made

### Added
- `src/module/new_file.py` – New component implementing X
- `tests/unit/test_new_file.py` – Unit tests (12 test cases)
- `docs/new-feature.md` – User documentation

### Modified
- `src/module/existing.py`
  - Added `new_method()` (lines 45-67)
  - Updated `existing_method()` to handle new case
- `config/settings.py`
  - Added `NEW_FEATURE_ENABLED` flag

### Removed
- `src/module/deprecated.py` – Replaced by new_file.py

### Configuration
- Added `.env` variable: `NEW_FEATURE_ENABLED=true`
```

### 4. Tests (Required)
Test execution results.

```markdown
## 4. Tests

### Test Execution
```bash
$ python -m pytest tests/unit/test_new.py -v
========================= test session starts =========================
collected 12 items

tests/unit/test_new.py::test_happy_path PASSED
tests/unit/test_new.py::test_edge_case_empty PASSED
tests/unit/test_new.py::test_edge_case_large PASSED
tests/unit/test_new.py::test_error_invalid_input PASSED
...

========================= 12 passed in 0.45s =========================
```

### Coverage
- Module coverage: 95%
- Branch coverage: 88%

### Manual Tests
- [x] Verified UI renders correctly
- [x] Verified error messages are clear
- [ ] Performance test (deferred to WO05)
```

### 5. Definition of Done (Required)
Checklist from Workorder with completion status.

```markdown
## 5. Definition of Done

- [x] All deliverables completed
- [x] All tests passing
- [x] Code compiles without errors
- [x] No new linter warnings
- [x] Documentation updated
- [x] WO_CATALOG.md updated
- [x] WO Report created (this document)
```

### 6. Issues and Deviations (Optional)
Any problems encountered or deviations from plan.

```markdown
## 6. Issues and Deviations

### Issues Encountered
| Issue | Impact | Resolution |
|-------|--------|------------|
| API rate limiting | Medium | Added retry logic with backoff |
| Missing test fixture | Low | Created fixture, added to repo |

### Deviations from Plan
| Planned | Actual | Reason |
|---------|--------|--------|
| Use library X | Used library Y | X deprecated, Y is successor |
| 2-4 hours | 5 hours | Unexpected API complexity |

### Technical Debt Introduced
- `TODO(WO07)` in `new_file.py:45` – Caching not implemented
```

### 7. Follow-Up (Optional)
Recommendations for future work.

```markdown
## 7. Follow-Up

### Recommended Next Steps
1. Create WO for performance optimization
2. Review error handling in edge cases
3. Consider adding integration tests

### New Workorders Created
- WO07: Implement caching for new feature
- WO08: Performance optimization

### Observations
- Pattern in `existing.py` could be extracted to utility
- Consider ADR for error handling strategy
```

---

## Footer (Required)

```markdown
---

## Changelog

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-02-06 | @developer | Initial report |
| 1.0.1 | 2026-02-06 | @reviewer | Added review notes |
```

---

## File Naming

```
workorders/reports/WO01_report_2026-02-06.md
workorders/reports/WO02_report_2026-02-07.md
```

---

## When to Create a Report

Create a completion report when:
- Workorder status changes to DONE
- Workorder is being closed (even if CANCELLED or BLOCKED)
- Significant milestone reached within a large Workorder

Report is **mandatory** before:
- Updating WO_CATALOG.md to DONE
- Merging implementation branch
- Handing off to integration

