---
description: "Validate that a Workorder is ready for implementation"
tools:
  - "codebase"
  - "search"
  - "problems"
---

# Pre-Implementation Check

This prompt validates that a Workorder is ready for implementation before coding begins.

---

## Purpose

Prevent the "70% problem" by ensuring:
- Workorder is complete and clear
- All prerequisites are met
- Architecture is aligned
- Risks are identified

---

## Input

- **Workorder ID**: ${input:woId:WO01}

---

## Checklist

### 1. Workorder Completeness

| Check | Status | Notes |
|-------|--------|-------|
| Goal is clear and measurable | ⬜ | |
| Scope (in/out) is defined | ⬜ | |
| Deliverables are concrete | ⬜ | |
| Acceptance criteria are testable | ⬜ | |
| Tests are specified | ⬜ | |
| Definition of Done is complete | ⬜ | |
| Effort estimate is provided | ⬜ | |

### 2. Context Availability

| Check | Status | Notes |
|-------|--------|-------|
| All referenced files exist | ⬜ | |
| Dependent Workorders complete | ⬜ | |
| Required schemas available | ⬜ | |
| Test fixtures/data available | ⬜ | |

### 3. Architecture Alignment

| Check | Status | Notes |
|-------|--------|-------|
| Respects existing module structure | ⬜ | |
| No circular dependencies | ⬜ | |
| Follows naming conventions | ⬜ | |
| Consistent with relevant ADRs | ⬜ | |
| Security considerations addressed | ⬜ | |

### 4. Risk Assessment

| Check | Status | Notes |
|-------|--------|-------|
| Breaking changes identified | ⬜ | |
| Performance implications considered | ⬜ | |
| Security implications reviewed | ⬜ | |
| Rollback strategy known | ⬜ | |

---

## Output Format

```markdown
## Pre-Implementation Check: ${woId}

**Date:** {date}
**Checked By:** reviewer

### Status: 🟢 GREEN | 🟡 YELLOW | 🔴 RED

### Summary
Brief assessment of readiness.

### Checklist Results

#### Workorder Completeness: ✅ Pass / ⚠️ Issues / ❌ Fail
- [x] Goal clear
- [x] Scope defined
- [ ] Tests specified (MISSING: integration tests)

#### Context Availability: ✅ Pass / ⚠️ Issues / ❌ Fail
- [x] Files exist
- [x] Dependencies met

#### Architecture Alignment: ✅ Pass / ⚠️ Issues / ❌ Fail
- [x] Structure respected
- [x] ADRs followed

#### Risk Assessment: ✅ Pass / ⚠️ Issues / ❌ Fail
- [x] Risks identified
- [x] Mitigations documented

### Blockers (if RED)
1. [Specific blocker]
2. [Specific blocker]

### Caveats (if YELLOW)
1. [Caveat with suggested mitigation]

### Recommendations
1. [Action before proceeding]
2. [Thing to watch out for]

### Verdict
- 🟢 Ready to proceed
- 🟡 Proceed with awareness of [caveats]
- 🔴 Do not proceed until [blockers resolved]
```

---

## Status Definitions

### 🟢 GREEN - Ready
- All checks pass
- No blockers
- Clear path forward

### 🟡 YELLOW - Ready with Caveats
- Minor issues that don't block
- Proceed with awareness
- Document caveats

### 🔴 RED - Not Ready
- Critical issues exist
- Must resolve before implementation
- List specific blockers

---

## Workflow

1. I will read the specified Workorder
2. I will check each item in the checklist
3. I will search codebase to verify context
4. I will compile findings into the output format
5. I will present the verdict and recommendations

---

## Let's Start

Please provide the Workorder ID to check.
