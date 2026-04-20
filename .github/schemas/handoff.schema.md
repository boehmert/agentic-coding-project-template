---
schema_id: handoff
version: 1.0.0
status: ACTIVE
created: 2026-02-06
created_by: developer
reviewed_by: pending
---

# Handoff Schema (Agent-to-Agent Context Transfer)

This schema defines the structure for context handoffs between agents.

---

## Purpose

A handoff document ensures seamless context transfer when:
- One agent's task is complete and another agent takes over
- A task is outside an agent's responsibility
- Work is paused and will be resumed later
- Multiple agents collaborate on the same Workorder

---

## Structure

### Inline Handoff (for quick transitions)

```markdown
## Handoff Summary

**From:** [Source Agent Name]
**To:** [Target Agent Name]
**Date:** 2026-02-06
**Workorder:** WO01 (if applicable)

### Task
Brief description of what needs to be done next.

### Current State
- What has been completed
- Current status of artifacts
- Any in-progress work

### Open Points
- Decisions that need to be made
- Questions that need answers
- Blockers to resolve

### Relevant Files
- `path/to/file1.md` – Description
- `path/to/file2.py` – Description

### Context
Any additional information the receiving agent needs to continue effectively.
```

---

## Detailed Handoff (for complex transitions)

### Frontmatter

```yaml
---
type: handoff
from_agent: developer
to_agent: reviewer
workorder_id: WO01
created: 2026-02-06T14:30:00Z
status: PENDING                   # PENDING | ACKNOWLEDGED | COMPLETED
---
```

### Body

```markdown
# Handoff: WO01 Implementation → Review

## 1. Source Agent Summary

**Agent:** Developer
**Task Completed:** Implementation of feature X
**Time Spent:** 3 hours
**Confidence Level:** High

### What Was Done
1. Created `src/module/feature.py` with main implementation
2. Added unit tests in `tests/unit/test_feature.py`
3. Updated configuration in `config/settings.py`
4. Ran all tests - 15/15 passing

### What Was NOT Done
- Performance optimization (out of scope for WO01)
- Integration tests (separate WO planned)

---

## 2. Artifacts for Review

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| Main implementation | `src/module/feature.py` | Ready for review | New file, 150 lines |
| Unit tests | `tests/unit/test_feature.py` | Ready for review | 15 test cases |
| Config changes | `config/settings.py` | Ready for review | 2 new settings |
| Documentation | `docs/feature.md` | Draft | Needs polish |

---

## 3. Review Focus Areas

Please pay special attention to:

1. **Error handling** in `feature.py:45-60` - Not sure if all edge cases covered
2. **Thread safety** in `feature.py:80-95` - Uses shared state
3. **Config validation** in `settings.py` - New pattern, needs consistency check

---

## 4. Known Issues

| Issue | Severity | Location | Notes |
|-------|----------|----------|-------|
| TODO marker | Low | `feature.py:120` | Placeholder for optimization |
| Missing docstring | Low | `feature.py:85` | Complex method needs docs |

---

## 5. Test Results

```
$ python -m pytest tests/unit/test_feature.py -v
========================= 15 passed in 0.45s =========================
```

**Coverage:** 92%
**Linting:** No warnings

---

## 6. Open Questions

- [ ] Should `process()` return None or raise exception on empty input?
- [ ] Is the current logging level (DEBUG) appropriate for production?

---

## 7. Recommended Next Steps

1. Review code changes
2. Answer open questions
3. If approved: Hand off to Integrator
4. If changes needed: Return to Developer with feedback
```

---

## Agent-Specific Handoff Patterns

### Developer → Reviewer
Focus on:
- Code changes and their purpose
- Test coverage and results
- Areas of uncertainty
- Compliance with Workorder scope

### Reviewer → Developer (Feedback)
Focus on:
- Specific issues found
- Required changes (must-fix)
- Suggestions (nice-to-have)
- Approval conditions

### Reviewer → Integrator
Focus on:
- Approval status
- Any conditions for merge
- Branch information
- PR preparation notes

### Planner → Developer
Focus on:
- Workorder details
- Implementation guidance
- Constraints and boundaries
- Success criteria

---

## Handoff Acknowledgment

When receiving a handoff, the target agent should acknowledge:

```markdown
## Handoff Acknowledged

**Received by:** [Agent Name]
**Date:** 2026-02-06T15:00:00Z
**Status:** ACKNOWLEDGED

### Understanding Confirmed
- [x] Task is clear
- [x] All artifacts accessible
- [x] Open questions understood
- [ ] Additional context needed: [specify]

### Planned Approach
Brief description of how the receiving agent will proceed.

### Estimated Completion
[Time estimate]
```

---

## File Storage

Handoffs are typically:
- **Inline in chat**: For quick, simple transitions
- **Temporary files**: `handoffs/WO01_dev-to-review_2026-02-06.md`
- **Embedded in reports**: As part of WO completion report

For audit trails, consider persisting handoffs in the `handoffs/` directory.

