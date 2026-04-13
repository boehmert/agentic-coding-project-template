---
description: "Plan a refactoring effort with minimal risk"
tools:
  - "codebase"
  - "search"
  - "editFiles"
---

# Refactoring Plan

This prompt helps create a safe, incremental refactoring plan.

---

## Refactoring Context

- **Target**: ${input:target:Code to refactor}
- **Goal**: ${input:goal:What improvement are we aiming for?}
- **Constraint**: ${input:constraint:Any constraints or requirements?}

---

## Refactoring Principles

### Core Rules
1. **Behavior preservation** - Tests must pass before and after
2. **Small steps** - Each step is independently reviewable
3. **Test first** - Add tests before refactoring untested code
4. **Continuous integration** - Merge frequently

### Risk Management
- Never refactor and add features simultaneously
- Have rollback strategy for each step
- Document decisions for future reference

---

## Analysis Phase

### Current State Assessment
1. What does this code do?
2. What tests exist?
3. What depends on this code?
4. What does this code depend on?

### Target State Vision
1. What should it look like after?
2. What problems will this solve?
3. What trade-offs are we accepting?

### Gap Analysis
1. What specific changes are needed?
2. What's the minimal path to get there?
3. What can be deferred?

---

## Output Format

```markdown
## Refactoring Plan: ${target}

**Date:** {date}
**Author:** planner
**Related WO:** WO{XX} (if applicable)

### 1. Current State

#### Code Structure
- Location: `path/to/code`
- Size: X lines / Y functions
- Dependencies: [list]
- Dependents: [list]

#### Issues
- Problem 1: Description
- Problem 2: Description

#### Test Coverage
- Unit tests: X%
- Integration tests: Exist/Missing

### 2. Target State

#### Vision
Description of the refactored state.

#### Benefits
- Benefit 1
- Benefit 2

#### Trade-offs
- Trade-off 1

### 3. Refactoring Steps

#### Phase 1: Preparation
**Goal:** Establish safety net

| Step | Action | Verification |
|------|--------|--------------|
| 1.1 | Add missing tests for current behavior | Tests pass |
| 1.2 | Document current behavior | README updated |
| 1.3 | Create feature branch | Branch created |

#### Phase 2: Structural Changes
**Goal:** Improve code structure

| Step | Action | Verification |
|------|--------|--------------|
| 2.1 | Extract function X | Tests pass |
| 2.2 | Rename Y to Z | Tests pass |
| 2.3 | Move module A to B | Tests pass |

#### Phase 3: Cleanup
**Goal:** Polish and document

| Step | Action | Verification |
|------|--------|--------------|
| 3.1 | Update documentation | Docs accurate |
| 3.2 | Remove deprecated code | No dead code |
| 3.3 | Final review | All tests pass |

### 4. Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Risk 1 | HIGH/MEDIUM/LOW | Mitigation strategy |

### 5. Rollback Strategy

For each phase:
- Phase 1: Revert commits X-Y
- Phase 2: Revert commits A-B
- Phase 3: Revert commits P-Q

### 6. Success Criteria

- [ ] All tests passing
- [ ] No new bugs introduced
- [ ] Code quality improved (measurable)
- [ ] Documentation updated
- [ ] Team reviewed and approved

### 7. Effort Estimate

| Phase | Effort | Risk |
|-------|--------|------|
| Phase 1 | X hours | Low |
| Phase 2 | Y hours | Medium |
| Phase 3 | Z hours | Low |
| **Total** | **W hours** | |
```

---

## Common Refactoring Patterns

### Extract Function
When code does too much.

### Rename
When names are unclear.

### Move
When code is in wrong module.

### Inline
When abstraction adds no value.

### Extract Class/Module
When function has too many responsibilities.

### Introduce Parameter Object
When function has too many parameters.

---

## Workflow

1. I will analyze the current code
2. I will identify issues and opportunities
3. I will create incremental steps
4. I will estimate effort and risk
5. I will present the plan for approval

---

## Let's Start

Please describe what you'd like to refactor and why.
