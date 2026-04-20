---
name: Session Recap
description: "Generate a structured session recap entry for SESSION_LOG.md after completing a work session."
mode: ask
---

# Session Recap Prompt

Generate a structured session recap entry and append it to `context/SESSION_LOG.md`.

---

## Your Task

1. Review what was accomplished in this session
2. Generate a new SESSION_LOG entry following the schema in `.github/schemas/session-log.schema.md`
3. Append the entry to `context/SESSION_LOG.md` (never overwrite existing entries)
4. Update `context/ARTIFACT_REGISTRY.md` if any artifacts were created or changed status

---

## Questions to Answer Before Writing

Before generating the entry, answer (from session history or by asking the user):

- **User Intent:** What did the user want to achieve? What was the goal, not just the tasks?
- **Consulted Artifacts:** Which files were read for context?
- **Decisions Made:** What was decided, and are any ADRs needed?
- **Created / Modified:** What files were created, changed, or deleted?
- **Open Points:** What was NOT completed? What needs attention next session?
- **Recommendation:** What should the next agent/session load and do first?

---

## Output Format

Use this exact format for the new entry:

```markdown
---
## Session: {{YYYY-MM-DD HH:MM}} | {{short session description}}

**Agent(s) used:** {{agent names used}}
**Duration:** ~{{X}}h
**Status:** {{COMPLETED | PARTIAL | BLOCKED}}

### User Intent
{{What the user wanted to achieve – the "why", not just the "what"}}

### Consulted Artifacts
- `{{path}}` – {{reason}}
- `{{path}}` – {{reason}}

### Decisions Made
- {{Decision 1}} → see [ADR-xxx](docs/adr/ADR-xxx.md) *(if applicable)*
- {{Decision 2 – inline if no ADR needed}}

### Created / Modified Artifacts
| Action | Artifact | Notes |
|--------|----------|-------|
| {{CREATED|MODIFIED|DELETED}} | `{{path}}` | {{brief note}} |

### Open Points for Next Session
- [ ] {{Open point 1}}
- [ ] {{Open point 2}}

### Recommendation for Next Session
Load: {{list of files to load}}.
Start with: {{suggested first action}}.
---
```

---

## After Generating the Entry

1. Append it to `context/SESSION_LOG.md`
2. Update `context/ARTIFACT_REGISTRY.md`:
   - Change status of any completed Workorders to `DONE`
   - Add any newly created artifacts
   - Update `Last Updated` dates
3. If a significant strategic goal was reached or started, offer to update `context/USER_INTENT_LOG.md`

---

## Triggering This Prompt

### Automatic triggers (agent-initiated, no user action needed)
- A Workorder deliverable or task was completed
- A significant decision was made (ADR-worthy or scope change)
- Files were created or modified in a meaningful way
- Approx. every 15–20 turns in a long session
- Before switching to a clearly different task domain

When auto-triggering: announce briefly (*"Zwischenspeichern..."*), write the entry, then continue.

### Manual triggers (user-initiated)
- User says "session recap", "log the session", "wrap up", or "save progress"
- Before the context window gets full
- When switching agent types

