---
description: "Neue Workorder-Spezifikation erstellen — interaktiver Wizard mit Scope, ACs und Implementierungsplan."
tools:
  [vscode, execute, read, agent, edit, search, web, browser, todo]
---

# Create Workorder

This prompt guides you through creating a well-structured Workorder.

---

## Required Information

### Basic Details
- **Title**: ${input:title:Descriptive title for the work}
- **Priority**: ${input:priority:MEDIUM} (LOW | MEDIUM | HIGH | CRITICAL)
- **Estimated Effort**: ${input:effort:2-4 hours}

### Context
- **Why is this needed?**: ${input:context:Explain the background and motivation}
- **What triggered this?**: ${input:trigger:User request, bug report, improvement idea}

---

## Workflow

### Step 1: Gather Context

Before creating the Workorder, I will:
1. Search the codebase for affected areas
2. Check existing Workorders for dependencies
3. Review relevant architecture (ADRs)

### Step 2: Define Scope

I will ask you to confirm:
- What is **IN** scope (specific deliverables)
- What is **OUT** of scope (explicit exclusions)
- Any ambiguous areas that need clarification

### Step 3: Create Workorder

Using the schema from `schemas/workorder.schema.md`, I will create:
- Complete frontmatter
- All required sections
- Specific, testable acceptance criteria

### Step 4: Review and Approve

Before saving, I will present:
- Summary of the Workorder
- Key decisions and constraints
- Risks and dependencies
- Request your approval

---

## Output

The Workorder will be saved to:
```
workorders/WO{XX}_{title-slug}.md
```

WO_CATALOG.md will be updated with the new entry.

---

## Quality Checklist

Before finalizing, I will verify:

### Clarity
- [ ] Goal is specific and measurable
- [ ] Scope boundaries are explicit
- [ ] Deliverables are concrete
- [ ] Acceptance criteria are testable

### Completeness
- [ ] Context explains motivation
- [ ] Dependencies identified
- [ ] Risks documented
- [ ] Tests specified

### Feasibility
- [ ] Effort estimate realistic
- [ ] No unresolved blockers
- [ ] Dependencies are available

---

## Template Preview

```markdown
---
id: WO{XX}
title: "${title}"
version: 1.0.0
status: PLANNED
created: {date}
created_by: workorder-planner
priority: ${priority}
estimated_effort: "${effort}"
---

# WO{XX}: ${title}

## 1. Context

${context}

**Trigger:** ${trigger}

## 2. Goal

[Specific, measurable goal]

**Success looks like:**
- Measurable outcome 1
- Measurable outcome 2

## 3. Scope

### In Scope
- Deliverable 1
- Deliverable 2

### Out of Scope
- Excluded item 1
- Excluded item 2

## 4. Deliverables

| # | Deliverable | Description | Location |
|---|-------------|-------------|----------|
| 1 | ... | ... | ... |

## 5. Implementation Notes

[Technical guidance]

## 6. Tests

### Unit Tests
- Test 1
- Test 2

### Manual Tests
- [ ] Manual verification 1

## 7. Definition of Done

- [ ] All deliverables completed
- [ ] All tests passing
- [ ] Code compiles without errors
- [ ] Documentation updated
- [ ] WO_CATALOG.md updated
- [ ] WO Report created

## 8. Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| ... | ... | ... |

---

## Changelog

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | {date} | workorder-planner | Initial version |
```

---

## Let's Start

Please provide the basic details above, and I'll guide you through creating a complete Workorder.

