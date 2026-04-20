# Changelog

All notable changes to this project are documented here.

Format: [Semantic Versioning](https://semver.org/) — `MAJOR.MINOR.PATCH`

---

## [2.1.0] — 2026-04-20

### Added
- `COPILOT.md` — workspace context guide for Copilot
- `workorders/WO_CATALOG.md` — central workorder registry
- `workorders/examples/WO00_bootstrap.md` — complete example workorder
- `docs/adr/` — directory for Architecture Decision Records
- `docs/SETUP.md` — onboarding guide (new project and integration scenarios)
- `inbox/`, `output/`, `examples/` — standard I/O directories
- `CHANGELOG.md` — this file
- `LICENSE` — MIT license
- `glossary.yaml` — added 9 generic framework terms (Workorder, ADR, Spec-Driven Development, Knowledge Snippet, Vibecoding, DoD, Session Continuity, Active Context, Pre-Implementation Check)
- `.github/hooks/hooks.json` — Stop hook with session-end reminder

### Changed
- `workday-goal-awareness.md` → `workday-goal-awareness.prompt.md` (correct VS Code prompt extension)
- `workday-goal-awareness.prompt.md` — added required `description:` frontmatter
- `start.prompt.md` — `{{task}}` variable replaced with `${input:task:...}` (consistent VS Code schema)
- `package.json` — updated name, version (2.0.0), description, removed `main: index.js`, added `private: true` and `_note`

### Removed
- `.apm/` directory — legacy Agent Prompt Manager copies (superseded by `.github/agents/` and `.github/prompts/`)

### Fixed
- WK/Wolters Kluwer specific references removed throughout framework (see commit `a966923`)

---

## [2.0.0] — 2026-04-15

### Added
- Layer 2: Knowledge Management
  - `wiki/` system with provenance frontmatter schema
  - Vault integration via `vault-mcp` MCP server
  - Wiki prompts: `/wiki-write`, `/wiki-ingest`, `/wiki-lint`
  - `_tools/validate/` — frontmatter, terminology, AI-style validation pipeline
  - `_tools/ai_detect/` — stylometric AI content detection (Claude, ChatGPT, Copilot, Gemini)
  - `_tools/documents/` — document conversion (docx, pdf, xlsx, pptx → Markdown)
  - `tasks/validate-output/` — combined CLI quality check
- Layer 3: Session Continuity
  - Memory system (user, session, repo scopes)
  - `.github/hooks/` — `hooks.json` with SessionStart/Stop automation
  - `/cognitive-continuity-context-transfer` prompt (CCCTP v1.3)
  - `/save-session` and `/session-recap` prompts
- Layer 4: Governance
  - `governance/workday-goals.md` and `governance/activity-log.md`
  - `workday-goals.instructions.md`
- New agents: `adr-generator`, `critical-thinker`, `doublecheck`
- New skills: `ai-content-check`, `document-pipeline`, `knowledge-retrieval`, `make-skill-skill`, `schreibstil`
- `FRAMEWORK_MANIFEST.md` — version tracking for all artifacts
- `context/USER_INTENT_LOG.md` — strategic intent tracking

### Changed
- Complete refactor from v1 vibecoding-project-template
- `copilot-instructions.md` expanded to full multi-layer system

---

## [1.0.0] — 2026-02-06

### Added
- Layer 1: Spec-Driven Development foundation
- Agent definitions: architect, workorder-planner, developer, reviewer, integrator, documenter, security-reviewer
- Schemas: workorder, ADR, report, handoff
- Prompts: create-workorder, create-adr, pre-implementation-check, repo-bootstrap, session-start, session-recap
- Instructions: vibecoding-core, vibecoding-extended, spec-driven, python, markdown, response-style
- `context/ARTIFACT_REGISTRY.md` and `context/SESSION_LOG.md`
- `requirements.txt` with core Python dependencies
- `.env.example`
