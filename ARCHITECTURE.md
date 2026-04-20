# Architecture

This workspace is a Python-first collection of CLI workflows for document processing, knowledge management, content validation, and integration with external systems (Jira, Confluence, Obsidian Vault). Copilot should treat it as a set of small task entrypoints over reusable internal libraries, with Markdown and exported artifacts as the main inputs and outputs.

---

## Tech Stack

- **Language:** Python 3.11+ is the primary implementation language.
- **Workspace assets:** Markdown for prompts, specs, reports, examples, and knowledge/context files.
- **Runtime style:** Local CLI scripts, file-system workflows, and direct API clients. No web app or long-running service layer.
- **Key libraries:**
  - `python-dotenv` for environment-based configuration
  - `python-docx`, `pypdf`, `openpyxl`, `jinja2` for document and spreadsheet processing
  - `python-pptx`, `markdown2` for presentation generation
  - `rdflib`, `pyshacl` for RDF and SHACL processing (optional)
  - `pyyaml` for YAML configuration
- **Optional integrations:**
  - `atlassian-python-api`, `requests`, `msal` for Jira/Confluence access
  - `selenium`, `webdriver-manager` for browser-based auth flows
- **Secondary tooling:** `package.json` exists for workspace and extension-related assets; this is not a Node application.

---

## Folder Structure

### Framework Layer (`.github/`)
- `.github/copilot-instructions.md` — Master behavior rules for Copilot
- `.github/instructions/` — Path-scoped instruction files (~15 files)
- `.github/agents/` — Specialized agent definitions (5+ agents)
- `.github/prompts/` — Reusable workflow prompts (20+ prompts)
- `.github/skills/` — Domain knowledge bundles (8+ skills)
- `.github/schemas/` — Specification templates (workorder, ADR, report, handoff)
- `.github/hooks/` — Session start/stop automation

### Python Layer (`_tools/` + `tasks/`)
- `_tools/` — Reusable internal Python libraries. Domain code lives here and is imported by tasks.
  - `_tools/validate/` — Frontmatter, terminology, and AI-style validation
  - `_tools/ai_detect/` — AI content detection (stylometric analysis)
  - `_tools/documents/` — Format conversion (docx, pdf, xlsx → Markdown)
  - `_tools/vault/` — Obsidian Vault ingestion pipeline
- `tasks/` — Executable workflow entrypoints, one folder per task with a `run.py` CLI wrapper.

### Knowledge Layer (`wiki/` + `context/`)
- `wiki/` — LLM-generated knowledge snippets with provenance tracking
  - `wiki/_INDEX.md` — Auto-maintained knowledge base index
  - Subdirectories by domain (e.g. `wiki/agentic-coding/`)
- `context/` — Curated knowledge base for Copilot context (manually maintained)
  - `context/ARTIFACT_REGISTRY.md` — Central artifact index
  - `context/SESSION_LOG.md` — Append-only session history
  - `context/USER_INTENT_LOG.md` — Strategic intent tracking

### Governance Layer
- `governance/` — Workspace-level standards and goal tracking
  - `governance/workday-goals.md` — Annual goals definition
  - `governance/activity-log.md` — Goal-aligned activity tracking
- `workorders/` — Structured planning and execution artifacts
  - `workorders/_template/` — Workorder template

### I/O Layer
- `inbox/` — Default input landing zone for user-supplied source files
- `output/` — Default destination for generated Markdown, reports, presentations
- `docs/` — Human-facing setup guides, specs, and reference documentation
- `examples/` — Sample inputs and expected-quality examples

---

## Key Flows

### 1. Task Execution Flow
`tasks/<task>/run.py` parses CLI arguments, resolves `WORKSPACE_ROOT`, and delegates to `_tools/<domain>/` for actual logic.

### 2. File Processing Flow
Inputs from `inbox/` or explicit `--input` path → `_tools/` processors → output to `output/`.

### 3. Knowledge Management Flow
`/wiki-write` → creates snippet in `wiki/` with provenance frontmatter → `/wiki-lint` validates → `wiki/_INDEX.md` updated.

### 4. Validation Flow
`tasks/validate-output/run.py` runs checks: frontmatter validation, terminology consistency, AI-style detection.

### 5. Session Continuity Flow
`/save-session` → writes to `/memories/repo/active-context.md` → `/start` reads it at next session start.

---

## Key Boundaries

- `tasks/` owns CLI orchestration only: argument parsing, default paths, console output, process exit.
- `_tools/` owns reusable logic: API access, parsing, transformation, rendering, validation.
- Content directories (`docs/`, `context/`, `wiki/`) are inputs/reference, not shared Python modules.
- `inbox/` is for source material; `output/` is for generated artifacts. Do not treat `output/` as stable source of truth.
- New domain behavior goes into `_tools/` and is called from `tasks/`.
- Secrets belong in `.env` and environment variables only.

---

## Patterns

- **Naming:** Python `snake_case`, classes `PascalCase`, task folders `kebab-case` with `run.py`.
- **Paths:** Use `pathlib.Path`, not hard-coded absolute paths. Tasks derive `WORKSPACE_ROOT = Path(__file__).parent.parent.parent`.
- **Error handling:** `_tools/` raises exceptions; `tasks/` translates to user-facing messages.
- **Execution model:** Synchronous. No `asyncio` without strong reason.
- **Output style:** Markdown-first for inspection and downstream Copilot use.
- **Imports:** Task entrypoints prepend workspace root to `sys.path` to import `_tools` modules.
