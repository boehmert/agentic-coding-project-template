# Agentic Coding Project Template — Copilot Guide

This file gives GitHub Copilot the essential architecture and convention context for this workspace.

---

## What This Workspace Is

A **framework for AI-assisted software development** — not an application. It provides:
- Structured workflows (Spec-Driven Development with Workorders and ADRs)
- Specialized agents (architect, developer, reviewer, critical-thinker, etc.)
- Knowledge management (wiki/ with provenance, Vault integration)
- Session continuity (memory system, hooks)
- Validation tooling (frontmatter, terminology, AI-style checks)

**Primary language:** Python 3.11+ for tooling. Markdown for all specs, prompts, knowledge.

---

## Layer Architecture

```
Layer 1: Spec-Driven   .github/agents/, prompts/, schemas/   Workorders → Quality Gates → Code
Layer 2: Knowledge     wiki/, context/, _tools/vault/         Snippets with provenance
Layer 3: Session       /memories/, .github/hooks/             Context persistence
Layer 4: Governance    governance/, workorders/               Goals, activity tracking
```

---

## Key Conventions

### Canonical Directories

| Purpose | Path |
|---------|------|
| Agent definitions | `.github/agents/*.agent.md` |
| Reusable prompts | `.github/prompts/*.prompt.md` |
| Skill bundles | `.github/skills/<name>/SKILL.md` |
| Path-scoped rules | `.github/instructions/*.instructions.md` |
| Spec schemas | `.github/schemas/*.schema.md` |
| Library code | `_tools/<domain>/` |
| CLI entrypoints | `tasks/<task>/run.py` |
| Knowledge snippets | `wiki/<domain>/KB-YYYY-NNN_*.md` |
| Steering artifacts | `context/` |
| Workorders | `workorders/WOxx_*.md` |
| ADRs | `docs/adr/ADR-xxx_*.md` |
| Input files | `inbox/` |
| Generated output | `output/` |

### Code Style
- Python: `snake_case` functions, `PascalCase` classes, `kebab-case` task folders
- `_tools/` = pure library logic (no argparse, no `print()`, no `sys.exit()`)
- `tasks/` = CLI wrappers only (argparse + delegation to `_tools/`)
- Never hardcode paths — use `Path(__file__).resolve().parents[N]` for workspace root

### Workorder Lifecycle
```
PLANNED → IN_PROGRESS → REVIEW → DONE
                      → BLOCKED
```
Every Workorder needs: goal, scope (in/out), deliverables, acceptance criteria, tests.
Pre-Implementation Check is mandatory before coding.

### Memory System
- `/memories/` — User-level, persists across all workspaces
- `/memories/repo/` — Repo-level, persists across sessions in this workspace
- `/memories/session/` — Session-level, cleared after conversation

### Research Order
1. Vault (`vault_search`) — first
2. `wiki/` — second
3. `context/` — third
4. External (only if internal sources exhausted)

---

## Key Prompts

| Command | When |
|---------|------|
| `/start` | Begin any session — loads context + catalog |
| `/create-workorder` | Before any non-trivial implementation |
| `/save-session` | At session end — persists context |
| `/pre-implementation-check` | Before coding begins |
| `/wiki-write` | Capture reusable knowledge |
| `/remember` | Save a persistent learning |

---

## What NOT to Do

- Never implement without a Workorder or explicit user approval
- Never change public APIs in `_tools/` without updating callers in `tasks/`
- Never write secrets — use `.env` and `python-dotenv`
- Never hardcode WK/company-specific paths or names (this is a public template)
- Never bypass quality gates (`/pre-implementation-check`) for shortcuts

---

## Layer 5: Multi-Agent Orchestration

### Agent Routing

| Situation | Agent |
|---|---|
| New spec, phase change, blocked decision | `@Orchestrator` — always first |
| Architecture question, multi-domain analysis | `@Lead Coordinator` (via Orchestrator) |
| Project plan / roadmap update | `@Project Planner` |
| Implementation (Workorder approved) | `@Developer` |
| Challenge assumptions before a decision | `@Critical Thinker` |
| Fact-check an AI-generated output | `@Doublecheck` |

### HITL Decision Workflow

```
Lead Coordinator cannot resolve → context/decisions-pending.md [BLOCKED]
Orchestrator surfaces to user → human decides
Lead Coordinator documents → context/DECISION_LOG.md (DL-NNN)
Entry removed from decisions-pending.md
```

### New Context Files

| File | Written by | Purpose |
|---|---|---|
| `context/sprint-state.md` | Lead Coordinator | Current phase + open decisions |
| `context/decisions-pending.md` | Lead Coordinator | HITL stop-signal |
| `context/DECISION_LOG.md` | Lead Coordinator | Finalized decisions (DL-NNN) |
| `context/lessons-learned.md` | All agents via `/remember` | Compound team learning |

### New Prompt

| Command | When |
|---|---|
| `/save-session` | Session end — persist thinking process and open questions |
| `/remember` | Save a new team learning to `context/lessons-learned.md` |
