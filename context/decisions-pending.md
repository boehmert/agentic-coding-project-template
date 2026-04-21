# Decisions Pending – Human-in-the-Loop Stop Signal

This file is the **stop signal** for the Orchestrator workflow.
It contains **only** entries with status `[BLOCKED]` or `[DEFERRED]`.

| Status | Meaning |
|---|---|
| `[BLOCKED]` | Workflow paused — waiting for human decision |
| `[DEFERRED]` | Not an active blocker — waiting for external input or later session |

> ⚠️ **`[APPROVED]` entries do not belong here.** Approved decisions go to `DECISION_LOG.md`.
> Leave only a brief archive note below.

---

## Format

```
### [DP-NNN] Short Title of Decision
**Status:** [BLOCKED] | [DEFERRED]
**Entered by:** [Agent name]
**Date:** YYYY-MM-DD
**Context:** [Why must this be decided?]
**Options:**
- Option A: ...
- Option B: ...
**Team recommendation:** [if available]
**Approved by:** [leave blank — filled by human]
```

**Lifecycle:**
1. Lead Coordinator enters decision as `[BLOCKED]` or `[DEFERRED]`
2. Human decides → Lead Coordinator documents fully in `DECISION_LOG.md`
3. Entry is deleted from this file → brief archive note remains below

---

## Open Decisions

*(empty — add entries here when decisions are pending)*

---

## Archive

*(Approved decisions are documented in `DECISION_LOG.md`. Brief notes go here.)*
