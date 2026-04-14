---
name: Spec-Driven Development Framework
description: Global guardrails for all AI coding agents in this workspace.
applyTo: "**"
---

# Spec-Driven Development Framework

These instructions apply to **all AI coding agents** working in this workspace. You are part of a structured, spec-driven development workflow.

---

## 1. Core Principles

### 1.1 Specs Before Code
- **Never write code without a spec.** Every change requires a Workorder, ADR, or explicit user approval.
- Treat Workorders as executable contracts, not task descriptions.
- When in doubt, create a spec first and get confirmation.

### 1.2 The 70% Problem
Assume your first draft is "almost right, but not quite" and therefore risky.
- Never treat the first draft as final.
- Compare your work explicitly against acceptance criteria.
- Call out uncertainties and open questions.
- Suggest concrete checks and tests to verify behaviour.

### 1.3 Provenance & Traceability
Every artifact must have clear provenance:
- **Frontmatter** with version, created_by, reviewed_by, parent_spec
- **References** to source documents (Workorders, ADRs, Schemas)
- **Changelog** for significant updates

---

## 2. Context Management

### 2.1 Mandatory Context Protocol – Session Start

Use the `session-start` prompt (`prompts/session-start.prompt.md`) or follow these steps manually:

| Step | File | What to extract |
|------|------|-----------------|
| 1 | `context/ARTIFACT_REGISTRY.md` | Active WO, REVIEW/BLOCKED items, last session date |
| 2 | `context/SESSION_LOG.md` (last entry only) | Open points, recommendation for this session |
| 3 | `context/USER_INTENT_LOG.md` (last ACTIVE entry) | Strategic goal, open success criteria |
| 4 | Active Workorder `workorders/WOxx_*.md` | Remaining deliverables, open DoD items |
| 5 | `REPO_STATE.md` (if exists) | Current system/branch state |

**Target:** Full orientation in < 5 minutes. Skip steps 1–3 only if the `context/` folder does not yet exist.

### 2.2 Context Refresh Protocol
When context becomes stale or confusing:
1. Stop and summarize current understanding
2. Re-read `context/ARTIFACT_REGISTRY.md` and last `SESSION_LOG.md` entry
3. Ask user to confirm or correct your understanding
4. Continue with refreshed context

### 2.3 Minimal Context Loading
- Use `codebase` and `search` surgically – load only what you need
- Prefer summarizing long files over pasting them verbatim
- Avoid loading large, unrelated parts of the codebase "just in case"

### 2.4 Mandatory Context Protocol – Session End

#### Auto-Trigger: When to proactively write a session recap

You must **proactively** trigger a session recap (without being asked) when any of these conditions are met:

| Trigger | Example |
|---------|---------|
| A Workorder deliverable is completed | "Done, all tests pass" |
| A significant decision was made | ADR, architecture choice, scope change |
| Files were created or modified | Any non-trivial file change |
| Approx. every 15–20 turns in a long session | Natural checkpoint |
| Before switching to a clearly different task domain | "Now let's work on X instead" |
| User says "session recap", "wrap up", or "log this" | Explicit trigger |

When auto-triggering, say briefly: *"Zwischenspeichern – ich schreibe einen kurzen Session-Eintrag."*
Then write the entry and continue without interrupting the workflow.

#### What to write

1. **Append** a new entry to `context/SESSION_LOG.md`
   - Use the `session-recap` prompt (`prompts/session-recap.prompt.md`)
   - Include: User Intent, Consulted Artifacts, Decisions, Modified Files, Open Points, Recommendation
2. **Update** `context/ARTIFACT_REGISTRY.md`
   - Add any newly created artifacts
   - Change status of completed Workorders to `DONE`
   - Update `Last Updated` dates
3. **Offer** to update `context/USER_INTENT_LOG.md` if a strategic goal shifted or was completed

> Rule: Session memory is only as good as what you write down. An unlogged session is a lost session.

---

## 3. Agent Routing & Handoff

### 3.1 Agent Selection Guide

| Task Type | Primary Agent | When to Use |
|-----------|--------------|-------------|
| Architecture decisions, NFRs, Tech-Stack | `architect` | System design, ADRs, technology choices |
| Workorder creation, scope definition | `workorder-planner` | Planning new work, risk identification |
| Code implementation | `developer` | Writing code, tests, implementation |
| Plan & code review, validation | `reviewer` | Pre-implementation check, post-implementation review |
| Branch merging, PR preparation | `integrator` | Bringing validated work into shared branches |
| Documentation, specs, reports | `documenter` | Knowledge artifacts, specs, reports |
| Security-focused review | `security-reviewer` | OWASP, secrets, auth, security concerns |

### 3.2 Self-Detection & Handoff Protocol
When you detect a task outside your responsibility:

1. **Recognize the mismatch** – Compare task against your role definition
2. **Communicate transparently** – Tell the user which agent would be better suited
3. **Prepare handoff context** – Summarize what you understood so the next agent can continue seamlessly

**Handoff Format:**
```markdown
## Handoff Summary
**From:** [Your Agent Name]
**To:** [Target Agent]
**Task:** [Brief description]
**Current State:** [What has been done/understood]
**Open Points:** [What needs to be resolved]
**Relevant Files:** [List of files]
```

### 3.3 Explicit Outputs
Every agent must write outputs as **files**, not just chat messages:
- Workorders → `workorders/WOxx_*.md`
- Reports → `workorders/reports/WOxx_report_*.md`
- ADRs → `docs/adr/ADR-xxx_*.md`
- Update `WO_CATALOG.md` after completing any workorder

---

## 4. Communication Style

### 4.1 Language
- **Agent definitions and specs:** English
- **Responses to user:** Match user's language (German or English)
- Once a language is established in a session, maintain it consistently

### 4.2 Decision Points
When multiple valid options exist:
1. Present options clearly with pros/cons
2. Make a recommendation with reasoning
3. **Wait for user decision** before proceeding

Only ask for confirmation on:
- Scope changes (outside current Workorder)
- Architecture decisions
- Security-relevant changes
- Breaking changes to APIs or schemas

Do NOT ask for confirmation on:
- Standard implementation steps within scope
- Minor refactorings within scope
- Test creation

### 4.3 Response Structure
Use structured, skimmable output:
- **Summary:** 2-4 sentences
- **Details:** Bullet points or tables
- **Next Steps:** Numbered list
- **Open Questions:** If any

---

## 5. Quality Gates

### 5.1 Pre-Implementation Check
Before implementing any Workorder:
1. Verify Workorder is complete (Goal, Scope, DoD, Tests)
2. Check all referenced files exist
3. Confirm dependent Workorders are complete
4. Assess architecture alignment

### 5.2 Post-Implementation Validation
After implementing:
1. Run `python -m compileall src` (for Python)
2. Run specified tests
3. Check for diagnostics/errors
4. Update WO_CATALOG.md
5. Create WO Report

---

## 6. File References

### Framework Manifest
- [FRAMEWORK_MANIFEST.md](FRAMEWORK_MANIFEST.md) – Version registry for all framework artifacts

### Context / Session Memory (read first at session start)
- [context/ARTIFACT_REGISTRY.md](../context/ARTIFACT_REGISTRY.md) – Central artifact index (read first)
- [context/SESSION_LOG.md](../context/SESSION_LOG.md) – Append-only session history
- [context/USER_INTENT_LOG.md](../context/USER_INTENT_LOG.md) – Strategic user intent layer

### Instruction Files
- [Spec-Driven Rules](instructions/spec-driven.instructions.md)
- [Python Standards](instructions/python.instructions.md)
- [Markdown Standards](instructions/markdown.instructions.md)
- [Response Style](instructions/response-style.instructions.md)

### Schema Files
- [Workorder Schema](schemas/workorder.schema.md)
- [ADR Schema](schemas/adr.schema.md)
- [Report Schema](schemas/report.schema.md)
- [Handoff Schema](schemas/handoff.schema.md)
- [Session Log Schema](schemas/session-log.schema.md)
- [User Intent Log Schema](schemas/user-intent-log.schema.md)
- [Artifact Registry Schema](schemas/artifact-registry.schema.md)

### Prompt Files
- [Session Start](prompts/session-start.prompt.md) – Load context at session start
- [Session Recap](prompts/session-recap.prompt.md) – Write session log entry at session end
- [Create Workorder](prompts/create-workorder.prompt.md)
- [Pre-Implementation Check](prompts/pre-implementation-check.prompt.md)
- [Create ADR](prompts/create-adr.prompt.md)
- [Performance Review](prompts/performance-review.prompt.md)
- [Refactoring Plan](prompts/refactoring-plan.prompt.md)

### Agent Files
- [Architect](agents/architect.agent.md)
- [Workorder Planner](agents/workorder-planner.agent.md)
- [Developer](agents/developer.agent.md)
- [Reviewer](agents/reviewer.agent.md)
- [Integrator](agents/integrator.agent.md)
- [Documenter](agents/documenter.agent.md)
- [Security Reviewer](agents/security-reviewer.agent.md)
