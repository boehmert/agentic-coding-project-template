---
id: WO00
title: "Framework Bootstrap — Agentic Coding Project Template"
version: 1.0.0
status: DONE
created: 2026-02-06
created_by: human
reviewed_by: developer
parent_spec: null
depends_on: []
priority: HIGH
estimated_effort: "1-2 days"
tags: [bootstrap, setup, framework]
---

# WO00 — Framework Bootstrap

## 1. Context

We are creating a new project repository and need to set up the complete
spec-driven development framework including agents, prompts, schemas,
knowledge management, and validation tooling.

**Trigger:** New project initiated. No existing structure present.

---

## 2. Goal

Establish a fully functional agentic coding workspace so that AI assistants
can operate with structured workflows, quality gates, and persistent context.

**Success looks like:**
- All framework layers (Spec-Driven, Knowledge, Session, Governance) are in place
- A developer can call `/start`, `/create-workorder`, and `/save-session` immediately
- `tasks/validate-output/run.py` executes without errors
- At least one example Workorder documents the bootstrap itself

---

## 3. Scope

### In Scope
- `.github/` framework setup (agents, prompts, skills, schemas, instructions)
- Python tooling (`_tools/`, `tasks/`)
- Context and governance structure
- `docs/SETUP.md` with onboarding instructions
- Initial `WO_CATALOG.md`, `ARTIFACT_REGISTRY.md`, `SESSION_LOG.md`

### Out of Scope
- Domain-specific customization (glossary terms, skill content)
- MCP server configuration (Jira, Confluence — project-specific)
- CI/CD pipeline setup

---

## 4. Deliverables

| # | Deliverable | Path | Status |
|---|-------------|------|--------|
| 1 | Framework directory structure | `.github/` | ✅ Done |
| 2 | Agent definitions (10) | `.github/agents/` | ✅ Done |
| 3 | Prompt library (27+) | `.github/prompts/` | ✅ Done |
| 4 | Skill bundles (8) | `.github/skills/` | ✅ Done |
| 5 | Schema files (7) | `.github/schemas/` | ✅ Done |
| 6 | Instruction files (15) | `.github/instructions/` | ✅ Done |
| 7 | Python validation pipeline | `_tools/validate/` | ✅ Done |
| 8 | AI detection module | `_tools/ai_detect/` | ✅ Done |
| 9 | Document conversion tools | `_tools/documents/` | ✅ Done |
| 10 | Hook system (SessionStart/Stop) | `.github/hooks/` | ✅ Done |
| 11 | Workorder catalog | `workorders/WO_CATALOG.md` | ✅ Done |
| 12 | Setup guide | `docs/SETUP.md` | ✅ Done |
| 13 | COPILOT.md | `COPILOT.md` | ✅ Done |

---

## 5. Acceptance Criteria

- [x] `/start {task}` works and shows the catalog
- [x] `/create-workorder` guides through spec creation
- [x] `/save-session` persists context to memory
- [x] `python tasks/validate-output/run.py` runs without import errors
- [x] `COPILOT.md` loaded by Copilot as project context
- [x] All framework directories exist and are tracked in git

---

## 6. Technical Notes

### Layer Architecture
The framework is organized in four layers, each building on the previous:

```
Layer 1: Spec-Driven   → Workorders, ADRs, quality gates
Layer 2: Knowledge     → wiki/, Vault, validation pipeline
Layer 3: Session       → Memory, hooks, context transfer
Layer 4: Governance    → Goals, activity log, workday alignment
```

### Key Conventions
- `_tools/` = reusable library code (no CLI logic)
- `tasks/` = CLI entrypoints with `run.py` (no business logic)
- `wiki/` = LLM-generated snippets with provenance frontmatter
- `context/` = manually curated steering artifacts

---

## 7. Definition of Done

- [x] All deliverables marked Done
- [x] Framework manifest updated to v2.0.0
- [x] README describes all layers and quick start
- [x] ARCHITECTURE.md reflects actual structure

---

## Changelog

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-02-06 | human | Initial bootstrap |
| 1.0.1 | 2026-04-20 | developer | Added WO_CATALOG.md, SETUP.md, COPILOT.md, directory structure |
