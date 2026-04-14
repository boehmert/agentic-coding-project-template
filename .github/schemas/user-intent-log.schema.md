# User Intent Log Schema

This schema defines the format for entries in `context/USER_INTENT_LOG.md`.
This is the **strategic meta-layer** – separate from session-level actions.
Each entry represents a significant strategic goal or initiative, not a single session.

---

## Entry Format

```markdown
---
## Intent: [Short strategic goal title] | YYYY-MM-DD

**Status:** ACTIVE | COMPLETED | PAUSED | SUPERSEDED
**Priority:** LOW | MEDIUM | HIGH | CRITICAL
**Related Workorders:** WOxx, WOxx
**Related ADRs:** ADR-xxx (if any)

### What the User Wants to Achieve
A 2-5 sentence description of the user's goal in their own words.
Focus on the outcome, not the implementation.

### Why This Matters
Business context, motivation, or strategic rationale.
What problem does this solve? What opportunity does it address?

### Success Criteria
- [ ] Concrete, measurable outcome 1
- [ ] Concrete, measurable outcome 2
- [ ] Concrete, measurable outcome 3

### Context & Constraints
- Important constraints or non-negotiables
- Known dependencies or blockers
- Relevant background knowledge

### Progress History
| Date | Update | Session Ref |
|------|--------|-------------|
| YYYY-MM-DD | What was done toward this goal | Session YYYY-MM-DD |

### Notes / Open Questions
- Open question or note 1
- Open question or note 2
---
```

---

## Field Descriptions

| Field | Required | Description |
|-------|----------|-------------|
| `Intent` header | Yes | Short title + date of recording |
| `Status` | Yes | Current state of this strategic goal |
| `Priority` | Yes | Relative importance |
| `Related Workorders` | Yes | WO IDs that implement parts of this intent |
| `Related ADRs` | Optional | Architectural decisions tied to this intent |
| `What the User Wants` | Yes | The goal, in non-technical human terms |
| `Why This Matters` | Yes | Rationale and business context |
| `Success Criteria` | Yes | Measurable DoD for the intent |
| `Context & Constraints` | Recommended | Non-negotiables, blockers, background |
| `Progress History` | Yes | Running log of progress toward this goal |
| `Notes / Open Questions` | Optional | Anything unresolved |

---

## Difference to SESSION_LOG

| SESSION_LOG | USER_INTENT_LOG |
|-------------|-----------------|
| What did the agent do? | What does the user want to achieve? |
| Per-session granularity | Per-initiative granularity |
| Operational (how) | Strategic (why) |
| Append after each session | Updated when intent changes or progresses |
| Consumed by: agent orientation | Consumed by: strategic alignment checks |

---

## Usage Rules

1. **One entry per strategic goal** – not per session or per workorder
2. **Update `Progress History`** rather than creating duplicate entries
3. **Change `Status`** when an intent is completed or shifts
4. **Link to sessions** via `Progress History.Session Ref`
5. **Keep entries focused** – split large initiatives into multiple intents
6. **Read at session start** – always load the most recent ACTIVE entry

---

## Example Entry

```markdown
---
## Intent: Build memory-safe agentic coding workflow | 2026-03-03

**Status:** ACTIVE  
**Priority:** HIGH  
**Related Workorders:** WO05, WO06  
**Related ADRs:** ADR-003  

### What the User Wants to Achieve
Copilot and other AI agents should maintain enough context across sessions
to work effectively without re-introduction at every session start.
The goal is a structured, low-overhead memory protocol built into the framework,
not a complex automation system.

### Why This Matters
Currently every new session loses context, causing repeated re-explanation,
re-reading of already-understood files, and inconsistent decisions.
This costs time and creates drift from the intended architecture.

### Success Criteria
- [ ] ARTIFACT_REGISTRY.md is the single source for artifact discoverability
- [ ] SESSION_LOG.md is consistently maintained after each session
- [ ] Agents can onboard to a session in < 5 min by reading 3 files
- [ ] Mandatory Context Protocol is part of every agent system prompt

### Context & Constraints
- Must remain low-overhead for the user (not a bureaucratic burden)
- Append-only logs preferred (no editing history)
- Framework changes must be backward-compatible with existing workspaces
- KMT workspace is the primary test case for these additions

### Progress History
| Date | Update | Session Ref |
|------|--------|-------------|
| 2026-03-03 | Schemas, templates, prompts, and instruction update created | Session 2026-03-03 |

### Notes / Open Questions
- Automate session-recap via tasks/ script in phase 2
- Evaluate whether ARTIFACT_REGISTRY should be per-agent-type or flat
---
```
