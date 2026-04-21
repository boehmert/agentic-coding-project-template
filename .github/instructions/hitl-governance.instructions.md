---
description: "HITL-Governance-Muster: BLOCKED/DEFERRED/APPROVED-Workflow, decisions-pending.md als Stopp-Signal, Decision Log mit DL-xxx-Nummern."
applyTo: "**"
---

# HITL Governance – Human-in-the-Loop Pattern

This instruction defines the governance pattern for decisions that require human approval before an agent may continue. All agents in the multi-agent orchestration layer must follow these rules.

---

## 1. The Two-File System

| File | Purpose | Who writes |
|---|---|---|
| `context/decisions-pending.md` | Stop-signal. Active BLOCKED/DEFERRED items | Lead Coordinator / Orchestrator |
| `context/DECISION_LOG.md` | Permanent record of all finalized decisions (DL-NNN) | Lead Coordinator (after human approval) |

**Rule:** Decisions do not live in chat history. Every decision that affects future work must be captured in one of these files.

---

## 2. Decision States

| Status | Meaning | Effect on workflow |
|---|---|---|
| `[BLOCKED]` | Cannot continue without human decision | Orchestrator pauses workflow |
| `[DEFERRED]` | Non-critical, waiting for external input or later session | Workflow continues |
| `[APPROVED]` | Human has decided | Move to DECISION_LOG.md, remove from decisions-pending.md |

**APPROVED items do not stay in `decisions-pending.md`.** They get a brief archive note + full entry in `DECISION_LOG.md`.

---

## 3. Entry Format in `decisions-pending.md`

```markdown
### [DP-NNN] Short Title of Decision
**Status:** [BLOCKED] | [DEFERRED]
**Entered by:** [Agent name]
**Date:** YYYY-MM-DD
**Context:** [Why must this be decided? What is at stake?]
**Options:**
- Option A: [description + trade-offs]
- Option B: [description + trade-offs]
**Team recommendation:** [if available — with reasoning]
**Approved by:** [leave blank — filled by human]
```

---

## 4. Entry Format in `DECISION_LOG.md`

```markdown
### [DL-NNN] Short Title of Decision
**Date:** YYYY-MM-DD
**Approved by:** [human / session reference]
**Decision:** [The chosen option in one sentence]
**Reasoning:** [Why this option? What alternatives were rejected?]
**Impact:** [What changes as a result? Which tasks/specs are now unblocked?]
**Source:** [DP-NNN or free context]
```

---

## 5. Numbering Convention

- `DP-NNN` — Decision Pending (3-digit, sequential per project)
- `DL-NNN` — Decision Log (3-digit, sequential per project)
- Numbers are never reused, even if entries are archived.

---

## 6. Orchestrator Behavior

When Orchestrator detects `[BLOCKED]` in `decisions-pending.md`:

1. Show user the blocked decision(s) clearly:
   ```
   ⚠️ APPROVAL REQUIRED
   [DP-NNN] [Title]: [options]
   → Workflow paused until this is resolved.
   ```
2. Do NOT start any new analysis or implementation.
3. After human decides: Lead Coordinator documents in DECISION_LOG.md + cleans decisions-pending.md.

---

## 7. When to Create a DP vs. Proceeding

| Situation | Action |
|---|---|
| Critical: affects architecture, scope, legal positioning, data model | Create `[BLOCKED]` DP |
| Medium: affects roadmap prioritization, deferred feature | Create `[DEFERRED]` DP |
| Routine: standard implementation within approved Workorder | No DP needed — proceed |
| Ambiguous requirements within Workorder scope | Developer asks user directly, no DP needed |
