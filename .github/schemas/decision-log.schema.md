---
schema_id: decision-log
version: 1.0.0
status: ACTIVE
created: 2026-04-21
created_by: lead-coordinator
---

# Decision Log Schema (DL-NNN)

This schema defines the structure for finalized decisions in `context/DECISION_LOG.md`.

---

## Purpose

The Decision Log captures every decision that:
- Required human (HITL) approval
- Affects architecture, scope, or product direction
- Must be traceable for future agents and sessions

Decisions flow: `decisions-pending.md` → human approval → `DECISION_LOG.md`

---

## Frontmatter (file level)

```yaml
# context/DECISION_LOG.md has no YAML frontmatter — it's a running log.
# Individual entries use the format below.
```

---

## Entry Format

```markdown
### [DL-NNN] Short Title of Decision
**Date:** YYYY-MM-DD
**Approved by:** [name or "session YYYY-MM-DD"]
**Decision:** [The chosen option in one sentence — what was decided]
**Reasoning:** [Why this option? What alternatives were considered and rejected?]
**Impact:** [What changes as a result? Which workorders/tasks are now unblocked?]
**Source:** [DP-NNN (from decisions-pending.md) or "direct decision in session YYYY-MM-DD"]
```

---

## Numbering Rules

- Sequential, 3-digit: DL-001, DL-002, DL-003...
- Numbers are **never reused**, even if superseded
- If a decision is amended: create new DL-NNN with `**Supersedes:** DL-NNN`
- Pending decisions use `DP-NNN` (see `decisions-pending.md`)

---

## Status Values

Decisions in this log are final. They do NOT have a mutable status field.
If a decision becomes obsolete:
- Add `**Retired:** YYYY-MM-DD — [reason]` to the entry
- Create new DL-NNN if a replacement decision is made

---

## Relationship to Other Files

| File | Relationship |
|---|---|
| `context/decisions-pending.md` | Feed: pending decisions come from here |
| `context/sprint-state.md` | Reference: sprint-state links to DL-NNN for context |
| `docs/adr/ADR-NNN.md` | Architecture decisions may reference DL-NNN for business context |
| `workorders/WOxx_*.md` | Workorders may reference DL-NNN as decision basis |
