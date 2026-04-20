---
name: ticket-analysis
description: "Analyze a Jira ticket for completeness, clarity, and readiness."
---

# Ticket Analysis

Analyze a Jira ticket and produce a structured quality assessment.

## Input

The user provides:
- A Jira ticket ID (e.g. PROJ-123) or ticket content
- Optional: specific focus (DoR check, scope clarity, acceptance criteria)

## Analysis Steps

1. **Fetch** — Load the ticket via Jira MCP (or use provided content)
2. **DoR Check** — Validate against Definition of Ready criteria (see `ticket-quality-example` skill)
3. **Clarity** — Assess whether description, scope, and acceptance criteria are unambiguous
4. **Completeness** — Check for missing fields (priority, estimate, labels, dependencies)
5. **Testability** — Verify acceptance criteria are concrete and testable
6. **Risks** — Identify implicit assumptions, missing context, or hidden dependencies

## Output Format

```markdown
# Ticket Analysis: [PROJ-XXX]

## DoR Status: READY / NOT READY

## Score: X/10

## Findings

### Missing
- [What's missing]

### Unclear
- [What's ambiguous]

### Risks
- [Hidden assumptions or dependencies]

## Suggested Improvements
1. [Specific improvement]
2. [Specific improvement]
```

## Prerequisites

Requires a configured Jira MCP server. See `.github/instructions/jira-integration.instructions.md`.

