---
name: strategy-context
description: "Load strategic context and goals for planning sessions."
---

# Load Strategy Context

Load and present the current strategic context for planning and decision-making sessions.

## Steps

1. Read `governance/workday-goals.md` for current goals and contribution criteria
2. Read `governance/activity-log.md` for recent progress and open follow-ups
3. Check `context/` folder for any domain-specific strategy documents
4. If Vault is configured: search for strategy-related notes via `vault_search`

## Output

Present a structured summary:

```markdown
## Current Strategic Context

### Active Goals
- Goal 1: [Title] — [Status summary]
- Goal 2: [Title] — [Status summary]

### Recent Progress (last 2 weeks)
- [Activity 1]
- [Activity 2]

### Open Follow-ups
- [Follow-up 1]
- [Follow-up 2]

### Key Decisions Pending
- [Decision 1]
```

## When to Use

- Before PI planning sessions
- When prioritizing backlog items
- When evaluating whether new work aligns with goals
- In quarterly review preparation

