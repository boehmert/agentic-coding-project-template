---
description: "Create an Architecture Decision Record (ADR)"
tools:
  - "codebase"
  - "search"
  - "editFiles"
  - "fetch"
---

# Create ADR

This prompt guides you through creating an Architecture Decision Record.

---

## When to Create an ADR

Create an ADR when:
- Choosing between technologies (database, framework, library)
- Defining architectural patterns
- Making security-relevant decisions
- Establishing conventions with trade-offs
- Any decision affecting multiple Workorders

---

## Required Information

### Decision Context
- **Title**: ${input:title:Decision title}
- **Problem Statement**: ${input:problem:What problem are we solving?}
- **Constraints**: ${input:constraints:What constraints exist?}

---

## Workflow

### Step 1: Understand the Context

I will:
1. Review existing ADRs for related decisions
2. Search codebase for affected areas
3. Research options (fetch external docs if needed)

### Step 2: Identify Options

I will present at least 2-3 viable options with:
- Description
- Pros and cons
- Effort and risk assessment
- Long-term implications

### Step 3: Evaluate Trade-offs

For each option, I will analyze:
- Technical fit
- Team capability
- Cost/effort
- Scalability
- Maintainability

### Step 4: Present Recommendation

I will:
- Recommend an option with reasoning
- Explain trade-offs accepted
- Wait for your decision

### Step 5: Document the Decision

Using schema from `schemas/adr.schema.md`, I will:
- Create the ADR document
- Save to `docs/adr/ADR-{XXX}_{title}.md`

---

## Output

The ADR will be saved to:
```
docs/adr/ADR-{XXX}_{title-slug}.md
```

---

## Template Preview

```markdown
---
id: ADR-{XXX}
title: "${title}"
version: 1.0.0
status: PROPOSED
created: {date}
created_by: architect
decision_date: null
---

# ADR-{XXX}: ${title}

## 1. Context

### Situation
${problem}

### Constraints
${constraints}

### Forces
- Force 1
- Force 2

## 2. Decision

We will [decision statement].

### Key Points
- Point 1
- Point 2

## 3. Options Considered

### Option A: [Name]
**Description:** ...

**Pros:**
- ...

**Cons:**
- ...

**Effort:** Low/Medium/High
**Risk:** Low/Medium/High

---

### Option B: [Name]
...

---

### Option C: Do Nothing
...

## 4. Rationale

We chose **Option X** because:
1. Reason 1
2. Reason 2

### Trade-offs Accepted
- We accept [trade-off] because [reason]

## 5. Consequences

### Positive
- Benefit 1
- Benefit 2

### Negative
- Drawback 1 (mitigated by X)

### Neutral
- Change in workflow

## 6. Implementation

### Affected Components
- Component 1
- Component 2

### Migration Path
1. Step 1
2. Step 2

---

## Changelog

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | {date} | architect | Initial proposal |
```

---

## Quality Checklist

Before finalizing:

- [ ] Context clearly explains the situation
- [ ] At least 2-3 options considered
- [ ] Each option has pros/cons/effort/risk
- [ ] Rationale explains why this option
- [ ] Consequences are documented
- [ ] Trade-offs are explicit

---

## Let's Start

Please provide the decision context above, and I'll guide you through the ADR creation process.
