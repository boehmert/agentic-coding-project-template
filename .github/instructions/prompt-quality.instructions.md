---
description: "Practical prompt quality rules: goals, constraints, structured outputs, examples, acceptance criteria, and staged workflows."
applyTo: "**/*.prompt.md, **/*.md"
priority: recommended
---

# Prompt Quality Guidelines

## Core Rules

1. Define goal, audience, and constraints before execution.
2. Request structured outputs when they make the result easier to verify.
3. Include acceptance criteria for non-trivial prompts.
4. Use concrete repo examples instead of abstract instructions.
5. Split large tasks into staged prompts with checkpoints.
6. Require assumptions to be explicit before implementation.

## Standard Prompt Template

Use this structure for new `.prompt.md` files and complex chat requests:

```markdown
**Goal:** [Artifact, decision, code, analysis?]
**Context:** [Relevant repo facts and constraints]
**Constraints:** [Technology, policy, style, what not to do]
**Deliverable:** [Expected artifact and format]
**Validation:** [Test, review, checklist, or evidence]
```

## Frontmatter for Prompt Files

```yaml
---
mode: agent
description: "One-line description of what the prompt does."
---
```

Allowed modes: `agent`, `ask`, `edit`.

## Warning Signals

| Anti-pattern | Problem | Fix |
|---|---|---|
| Vague explanatory request | Output is not verifiable | Define the intended use |
| No format | Output is hard to consume | Request table, checklist, or specific artifact |
| Everything at once | Context overflow | Split into stages |
| No constraints | Unneeded generalization | State boundaries |
| No example | Misinterpretation risk | Reference an existing repo file |
