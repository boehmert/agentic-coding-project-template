---
schema_id: adr
version: 1.0.0
status: ACTIVE
created: 2026-02-06
created_by: developer
reviewed_by: pending
---

# ADR Schema (Architecture Decision Record)

This schema defines the structure for Architecture Decision Records.

---

## Frontmatter (Required)

```yaml
---
id: ADR-001                       # Unique identifier (ADR-xxx format)
title: "Decision Title"           # Human-readable title
version: 1.0.0                    # Semantic version
status: PROPOSED                  # PROPOSED | ACCEPTED | DEPRECATED | SUPERSEDED
created: 2026-02-06               # ISO date
created_by: architect             # human | agent-name
reviewed_by: pending              # reviewer-name | pending
decision_date: null               # Date when decision was made (if ACCEPTED)
supersedes: null                  # ADR-xxx (if this replaces another ADR)
superseded_by: null               # ADR-xxx (if this was replaced)
related_workorders: [WO01, WO02]  # Related Workorders
tags: [architecture, database]    # Optional categorization
---
```

---

## Body Structure

### 1. Context (Required)
The situation and forces at play.

```markdown
## 1. Context

### Situation
Describe the current situation that requires a decision.

### Forces
- Force 1: Technical constraint or requirement
- Force 2: Business constraint or requirement
- Force 3: Team capability or preference

### Trigger
What initiated the need for this decision?
```

### 2. Decision (Required)
The decision that was made.

```markdown
## 2. Decision

We will [decision statement].

### Key Points
- Specific aspect 1 of the decision
- Specific aspect 2 of the decision
- Specific aspect 3 of the decision
```

### 3. Options Considered (Required)
Alternatives that were evaluated.

```markdown
## 3. Options Considered

### Option A: [Name]
**Description:** Brief description of this option.

**Pros:**
- Advantage 1
- Advantage 2

**Cons:**
- Disadvantage 1
- Disadvantage 2

**Effort:** Low/Medium/High
**Risk:** Low/Medium/High

---

### Option B: [Name]
**Description:** Brief description of this option.

**Pros:**
- Advantage 1

**Cons:**
- Disadvantage 1
- Disadvantage 2

**Effort:** Low/Medium/High
**Risk:** Low/Medium/High

---

### Option C: Do Nothing
**Description:** Maintain current state.

**Pros:**
- No immediate effort

**Cons:**
- Problem persists
- Technical debt accumulates

**Effort:** None
**Risk:** High (long-term)
```

### 4. Rationale (Required)
Why this option was chosen.

```markdown
## 4. Rationale

We chose **Option A** because:

1. Primary reason with explanation
2. Secondary reason with explanation
3. Alignment with [principle/constraint]

### Trade-offs Accepted
- We accept [trade-off 1] because [reason]
- We accept [trade-off 2] because [reason]
```

### 5. Consequences (Required)
Expected outcomes of the decision.

```markdown
## 5. Consequences

### Positive
- Expected benefit 1
- Expected benefit 2

### Negative
- Known drawback 1 (mitigated by X)
- Known drawback 2 (accepted because Y)

### Neutral
- Change in workflow/process
- Team needs to learn X
```

### 6. Implementation (Optional)
Guidance for implementing the decision.

```markdown
## 6. Implementation

### Affected Components
- `src/module/` - Needs refactoring
- `config/` - New configuration required
- `docs/` - Documentation updates

### Migration Path
1. Step 1 of migration
2. Step 2 of migration
3. Step 3 of migration

### Timeline
- Phase 1: [Date] - Initial implementation
- Phase 2: [Date] - Migration complete
- Phase 3: [Date] - Old approach deprecated
```

### 7. Related Decisions (Optional)

```markdown
## 7. Related Decisions

- **ADR-000**: Previous decision that this builds upon
- **ADR-002**: Follow-up decision for specific aspect
- **WO05**: Workorder implementing this decision
```

---

## Footer (Required)

```markdown
---

## Changelog

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-02-06 | @architect | Initial proposal |
| 1.0.1 | 2026-02-07 | @team | Updated after review |
| 1.1.0 | 2026-02-10 | @architect | Decision accepted |
```

---

## File Naming

```
docs/adr/ADR-001_use-postgresql-database.md
docs/adr/ADR-002_adopt-hexagonal-architecture.md
```

---

## Status Transitions

```
PROPOSED → ACCEPTED → DEPRECATED
              ↓
         SUPERSEDED (by new ADR)
```

---

## When to Create an ADR

Create an ADR when:
- Choosing between technologies (database, framework, library)
- Defining architectural patterns (layering, modules, APIs)
- Making security-relevant decisions
- Establishing coding conventions with trade-offs
- Any decision that affects multiple Workorders

Do NOT create an ADR for:
- Implementation details within a single Workorder
- Obvious choices with no real alternatives
- Temporary workarounds (document in Workorder instead)

