---
framework_name: Spec-Driven Development Framework
version: 1.0.0
status: ACTIVE
created: 2026-02-06
created_by: developer
reviewed_by: pending
model_used: "Claude Opus 4.5"
---

# Framework Manifest

This file tracks provenance and version information for all framework artifacts.

---

## Framework Version

| Field | Value |
|-------|-------|
| **Version** | 1.0.0 |
| **Status** | ACTIVE |
| **Created** | 2026-02-06 |
| **Created By** | developer |
| **Model Used** | Claude Opus 4.5 |

---

## Artifact Registry

### Agents

| ID | File | Version | Status | Description |
|----|------|---------|--------|-------------|
| architect | `agents/architect.agent.md` | 1.0.0 | ACTIVE | System design, ADRs, tech decisions |
| workorder-planner | `agents/workorder-planner.agent.md` | 1.0.0 | ACTIVE | Create workorders, define scope |
| developer | `agents/developer.agent.md` | 1.0.0 | ACTIVE | Implement workorders, write code |
| reviewer | `agents/reviewer.agent.md` | 1.0.0 | ACTIVE | Validate plans and implementations |
| integrator | `agents/integrator.agent.md` | 1.0.0 | ACTIVE | Merge branches, prepare PRs |
| documenter | `agents/documenter.agent.md` | 1.0.0 | ACTIVE | Documentation and knowledge |
| security-reviewer | `agents/security-reviewer.agent.md` | 1.0.0 | ACTIVE | Security analysis |

### Instructions

| ID | File | Version | Status | Description |
|----|------|---------|--------|-------------|
| spec-driven | `instructions/spec-driven.instructions.md` | 1.0.0 | ACTIVE | Spec-driven development rules |
| python | `instructions/python.instructions.md` | 1.0.0 | ACTIVE | Python coding standards |
| markdown | `instructions/markdown.instructions.md` | 1.0.0 | ACTIVE | Markdown formatting standards |
| response-style | `instructions/response-style.instructions.md` | 1.0.0 | ACTIVE | Communication style rules |

### Schemas

| ID | File | Version | Status | Description |
|----|------|---------|--------|-------------|
| workorder | `schemas/workorder.schema.md` | 1.0.0 | ACTIVE | Workorder specification format |
| adr | `schemas/adr.schema.md` | 1.0.0 | ACTIVE | Architecture decision record format |
| report | `schemas/report.schema.md` | 1.0.0 | ACTIVE | Workorder completion report format |
| handoff | `schemas/handoff.schema.md` | 1.0.0 | ACTIVE | Agent-to-agent handoff format |

### Prompts

| ID | File | Version | Status | Description |
|----|------|---------|--------|-------------|
| repo-bootstrap | `prompts/repo-bootstrap.prompt.md` | 1.0.0 | ACTIVE | Initialize new repository |
| create-workorder | `prompts/create-workorder.prompt.md` | 1.0.0 | ACTIVE | Create new workorder |
| create-adr | `prompts/create-adr.prompt.md` | 1.0.0 | ACTIVE | Create architecture decision |
| pre-implementation-check | `prompts/pre-implementation-check.prompt.md` | 1.0.0 | ACTIVE | Validate before implementation |
| performance-review | `prompts/performance-review.prompt.md` | 1.0.0 | ACTIVE | Analyze performance |
| refactoring-plan | `prompts/refactoring-plan.prompt.md` | 1.0.0 | ACTIVE | Plan refactoring work |

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-02-06 | developer | Initial framework creation |

---

## Update Protocol

When updating framework artifacts:

1. **Increment version** in this manifest
2. **Update the artifact** file
3. **Add changelog entry** below
4. **Update Artifact Registry** table above

### Version Semantics

- **MAJOR** (1.0.0 → 2.0.0): Breaking changes to artifact structure
- **MINOR** (1.0.0 → 1.1.0): New artifacts or additive changes
- **PATCH** (1.0.0 → 1.0.1): Bug fixes, clarifications
