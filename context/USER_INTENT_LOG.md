# User Intent Log

> Strategic meta-layer: records *why* the user is doing this work, not just what was done.
> Schema: `.github/schemas/user-intent-log.schema.md`

**Rule:** One entry per strategic goal. Update `Progress History` rather than creating duplicates.
Read the most recent **ACTIVE** entry at every session start.

---

## Difference to SESSION_LOG

| SESSION_LOG | USER_INTENT_LOG |
|-------------|-----------------|
| What did the agent do? | What does the user want to achieve? |
| Per-session granularity | Per-initiative granularity |
| Operational (how) | Strategic (why) |
| Append after each session | Updated when intent changes or progresses |

---

<!-- Intent entries below. Most recent ACTIVE entry should be easy to find. -->

<!-- EXAMPLE ENTRY (delete this when adding real entries)
---
## Intent: Build spec-driven development workflow | 2026-02-06

**Status:** ACTIVE
**Priority:** HIGH
**Related Workorders:** WO01, WO02
**Related ADRs:** ADR-001

### What the User Wants to Achieve
A reusable project template where AI coding agents follow consistent,
structured workflows with clear artifacts, versioning, and quality gates.
The goal is to reduce rework, improve traceability, and enable effective
human-AI collaboration on complex software projects.

### Why This Matters
Without a structured framework, AI agents hallucinate, drift from
architecture, and require constant re-explanation. This wastes time and
produces low-quality results.

### Success Criteria
- [ ] Template repository is complete and documented
- [ ] All agent types have defined roles and prompts
- [ ] Session memory persists across Copilot sessions
- [ ] New projects can be bootstrapped in < 30 min

### Context & Constraints
- Target: GitHub Copilot (VS Code) as primary agent runtime
- Must be usable without any additional tools or infrastructure
- Low-overhead: must not create bureaucratic burden for the user

### Progress History
| Date | Update | Session Ref |
|------|--------|-------------|
| 2026-02-06 | Initial framework scaffolding complete | Session 2026-02-06 |

### Notes / Open Questions
- Test with a real project (KMT workspace) to validate patterns
---
END EXAMPLE -->
