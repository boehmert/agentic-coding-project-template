---
name: Session Start
description: "Load context at the beginning of a new agent session to quickly orient the agent."
mode: ask
---

# Session Start Prompt

Use this prompt at the beginning of a new session to load context and orient the agent efficiently.

---

## Mandatory Context Protocol

Execute these steps in order. Read each file and summarize what you learn.

### Step 1 – Artifact Registry (orientation)

Read `context/ARTIFACT_REGISTRY.md`.

Extract:
- Active Workorder (if any)
- Last session date
- Any REVIEW or BLOCKED items

### Step 2 – Recent Session History (last entry only)

Read `context/SESSION_LOG.md` and find the **last entry** (most recent `---` separator block).

Extract:
- User Intent of the last session
- Open Points for this session
- Recommendation (what to load, where to start)

### Step 3 – Strategic Intent (last ACTIVE entry)

Read `context/USER_INTENT_LOG.md` and find the most recent **ACTIVE** intent.

Extract:
- What the user wants to achieve long-term
- Success Criteria that are still open

### Step 4 – Active Workorder (if exists)

If Step 1 revealed an active Workorder, read it now.

Extract:
- Current status
- Remaining deliverables
- Definition of Done items that are open

### Step 5 – Confirm and Surface Context

Provide a brief session-start summary:

```markdown
## Session Start Summary

**Date:** YYYY-MM-DD
**Active Workorder:** WOxx – Title (or: none)
**Last Session:** YYYY-MM-DD – [what was done]
**Strategic Goal:** [active user intent]

### Open Points from Last Session
- [ ] Item 1
- [ ] Item 2

### My Recommendation
[What to tackle first based on loaded context]

**Shall I proceed?** ✓ / Please correct me if something has changed.
```

---

## Conditional Loads

Only load these if relevant to the current task:

| Condition | Additional file to load |
|-----------|------------------------|
| Architecture question | Relevant `docs/adr/ADR-xxx.md` |
| Code implementation | `REPO_STATE.md`, relevant source files |
| Security concern | `.github/agents/security-reviewer.agent.md` |
| New Workorder needed | `.github/schemas/workorder.schema.md` |

---

## When to Use This Prompt

- At the start of every new chat session
- When switching tasks after a long break
- When context feels stale or agent seems confused
- When onboarding a different agent type

---

## Time Budget

| Step | Target Time | Skip if |
|------|-------------|---------|
| Step 1 – Registry | 30 sec | File does not exist → note it missing |
| Step 2 – Session Log | 30 sec | File empty or missing → note it |
| Step 3 – Intent Log | 20 sec | File empty → continue without |
| Step 4 – Active WO | 1–2 min | No active WO in registry |
| Step 5 – Summary | 1 min | Always required |

**Target:** Full orientation in < 5 minutes.

