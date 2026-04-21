---
description: "Framework-Integration: Einmalig nach dem Import von agentic-coding-project-template in ein bestehendes Repo ausführen — Agenten inventarisieren, Konflikte auflösen, konfigurieren."
tools:
  [vscode, execute, read, agent, edit, search, todo]
---

# Integrate Framework

This prompt runs **once** after the framework directories have been copied from
`agentic-coding-project-template` into this repository. It guides you through
the complete integration without overwriting anything important.

---

## Context for the Agent

You have just received a set of new directories from the
[agentic-coding-project-template](https://github.com/boehmert/agentic-coding-project-template).
The imported content is additive — it does not touch application source code,
tests, or CI/CD configuration.

**What was imported (typical):**

```
.github/agents/        ← 22 specialised AI agents (personas)
.github/prompts/       ← Workflow prompts (/start, /save-session, etc.)
.github/instructions/  ← Auto-applied instruction files
.github/skills/        ← Domain skill bundles
.github/schemas/       ← Workorder, ADR, Report, Handoff schemas
context/               ← Artifact registry, session log, user intent log
workorders/            ← Spec-driven work specifications
wiki/                  ← LLM-generated knowledge snippets
COPILOT.md             ← Copilot project context (framework overview)
```

Your task as the agent in this repository: **complete the integration in the
steps below and make the framework operational for this project.**

---

## Step 0 — Inventory

Before touching anything, run a full inventory.

### 0a: Existing agents

```
find .github/agents -name "*.agent.md" | sort
```

List every agent file that existed **before** the import. Mark each one:

| File | Source | Status |
|------|--------|--------|
| … | pre-existing / framework | to assess |

### 0b: Conflicting files

Look for files that exist in **both** the pre-import repo and the framework:

- `.github/copilot-instructions.md`
- `.github/agents/developer.agent.md` (or equivalent)
- `README.md` sections about Copilot
- Any `.github/instructions/*.instructions.md` files that already exist

Document every conflict before resolving it.

---

## Step 1 — Resolve Agent Conflicts

Apply the following decision rules for **every** agent file that existed
before the import.

### Rule A — Framework agent replaces a generic placeholder

**Condition:** The pre-existing agent has little customisation — no project-specific
rules, no domain knowledge, generic role description only.

**Action:** Replace — the framework agent (with persona) supersedes it.

```bash
# Back up first:
git mv .github/agents/developer.agent.md .github/agents/_archive/developer-legacy.agent.md
# The framework's lena-python-developer.agent.md is now the canonical agent.
```

### Rule B — Framework agent conflicts with a custom project agent

**Condition:** The pre-existing agent contains project-specific rules, custom
quality gates, domain knowledge, or deliberately different behaviour.

**Action:** Keep both — rename the pre-existing file, note the divergence.

```bash
git mv .github/agents/developer.agent.md .github/agents/project-developer.agent.md
```

Then add a header comment to `project-developer.agent.md`:

```markdown
> **Note:** This file contains project-specific overrides.
> The framework default is `lena-python-developer.agent.md`.
> Reconcile these two files before the next major sprint.
```

### Rule C — Pre-existing agent covers a role the framework does not have

**Condition:** The pre-existing agent fills a domain not present in the 22
framework agents (e.g. a specialist for this project's tech stack or domain).

**Action:** Keep — rename it to `project-<role>.agent.md` to distinguish it
from framework agents. No further action needed.

---

## Step 2 — Configure COPILOT.md

COPILOT.md is the single most important file for the framework to work.
Open it and fill in the **Product Context** block:

```yaml
## Product Context
# — Fill in once; all persona agents (Arne, Max, Elena, Nadia, …) read this first —
product_name:         "[Your product name]"
problem_statement:    "[The problem you solve in 1–2 sentences]"
target_audience:      "[Who uses it and why]"
business_model:       "[SaaS / open source / internal tool / etc.]"
tech_stack:
  backend:            "[Language, framework, DB]"
  frontend:           "[Language, framework]"
  infra:              "[Cloud, CI/CD]"
regulatory_context:   "[GDPR / EU AI Act / none / specify]"
current_phase:        "[Idea / MVP / Growth / Mature]"
open_strategic_questions:
  - "[First open question]"
  - "[Second open question]"
```

**Rule:** Do not leave placeholder values. If a field is genuinely unknown,
write `"unknown — ask product owner"` so the gap is visible.

---

## Step 3 — Configure Individual Agents

Every framework agent ends with a `## ⚙️ Project Configuration` section.
These are currently filled with placeholder values or intentionally empty.

**Open each of the following agents** and fill in their configuration block
with project-specific context:

| Agent | File | What to fill in |
|-------|------|-----------------|
| Lisa – Workorder Planner | `lisa-workorder-planner.agent.md` | Domain context, known constraints |
| Robin – Execution Architect | `robin-execution-architect.agent.md` | Module structure, dependency rules |
| Lena – Python Developer | `lena-python-developer.agent.md` | Test framework, code conventions |
| Marco – Code Reviewer | `marco-code-reviewer.agent.md` | Project quality bars, forbidden patterns |
| Chris – Security Reviewer | `chris-security-reviewer.agent.md` | Threat surface, compliance requirements |
| Jana – Integrator | `jana-integrator.agent.md` | Branch strategy, merge rules |
| Finn – Technical Writer | `finn-documenter.agent.md` | Doc targets, style guide |

For Tier-4 domain personas (Arne, Max, Elena, Nadia, Felix, Sam, Tom, David,
Sophie, Mia, Jochen, Kai): their configuration block is secondary as long as
COPILOT.md is filled correctly — they read that first.

---

## Step 4 — VS Code Agent Picker

Agents in `.github/agents/` are **not** auto-listed in the VS Code Copilot
agent picker. You must copy them to the User-level agents folder:

```bash
# macOS
DEST="$HOME/Library/Application Support/Code/User/agents"
mkdir -p "$DEST"

# Copy all framework agents:
cp .github/agents/*.agent.md "$DEST/"

# Verify:
ls "$DEST"/*.agent.md | wc -l   # should show 22+ files
```

**Note for the user:** After copying, reload VS Code (`Cmd+Shift+P` →
`Developer: Reload Window`) for the agents to appear in the picker.

**Important:** Memory/state files (context/, workorders/, wiki/) stay in the
workspace — they are resolved via relative paths from the workspace root.
The agents in `User/agents/` reference them correctly.

---

## Step 5 — Initialize Context Files

The context files that came with the framework contain **example content**.
Clear them and initialize for this project.

### context/ARTIFACT_REGISTRY.md

Replace the example entries with a single bootstrapping row:

```markdown
| ID | Type | Title | Status | Created | Notes |
|----|------|-------|--------|---------|-------|
| WO00 | Workorder | Framework Integration | DONE | [today] | Initial framework setup |
```

### context/SESSION_LOG.md

Keep the schema header. Delete example entries. Add one bootstrapping entry:

```markdown
### Session: [today's date] — Framework Integration
**Focus:** Initial integration of agentic-coding-project-template
**Completed:** Steps 0–6 of integrate-framework prompt
**Open points:** Fill in agent ⚙️ Project Configuration blocks
**Recommendation:** Run /start next session to verify orientation
```

### context/USER_INTENT_LOG.md

Add one ACTIVE entry reflecting why this framework is being adopted:

```markdown
### [today] — Framework Adoption
**Status:** ACTIVE
**Strategic goal:** [Why is the team adopting AI-assisted development?]
**Success criteria:** [How will you know it worked?]
```

---

## Step 6 — Wire Up ARCHITECTURE.md (if it exists)

If this project has an `ARCHITECTURE.md`, append this section:

```markdown
## AI Framework Layer

This project uses [agentic-coding-project-template](https://github.com/boehmert/agentic-coding-project-template)
for AI-assisted development (spec-driven workflow, multi-agent system,
knowledge management).

- Framework overview: `COPILOT.md`
- Agent roster: `AGENTS.md`
- Setup and integration: `docs/SETUP.md`
- Workorder specs: `workorders/`
```

---

## Step 7 — Smoke Test

Run the following checks to verify the integration is operational:

```
1. Open VS Code Copilot Chat
2. Type: /start
   → Should load context/ARTIFACT_REGISTRY.md and orient correctly
3. Type: @Lisa Erstelle ein Test-Workorder für eine kleinere Verbesserung
   → Lisa should respond with a structured Workorder draft
4. Type: @Marco Prüfe diesen Entwurf
   → Marco should respond with a GREEN/YELLOW/RED gate assessment
```

If any step fails, check:
- Did agents get copied to `User/agents/`?
- Is COPILOT.md filled in (no placeholder values)?
- Is `.github/copilot-instructions.md` present (framework) or was it overwritten?

---

## Step 8 — Commit

```bash
git add .github/ context/ workorders/ wiki/ COPILOT.md AGENTS.md
git commit -m "chore: integrate agentic-coding-project-template framework

- Added 22 specialised AI agents (Tier 1–4)
- Initialized context tracking (ARTIFACT_REGISTRY, SESSION_LOG, USER_INTENT_LOG)
- Configured COPILOT.md for this project
- Filled agent Project Configuration blocks
- Archived superseded legacy agents (if any)"
```

---

## Summary

| Step | What | Owner |
|------|------|-------|
| 0 | Inventory existing agents | Agent |
| 1 | Resolve agent conflicts (A/B/C rules) | Agent + human review |
| 2 | Fill COPILOT.md Product Context | **Human** |
| 3 | Fill agent ⚙️ Project Configuration | Human (agent assists) |
| 4 | Copy agents to User/agents/ | Human (terminal) |
| 5 | Initialize context files | Agent |
| 6 | Wire up ARCHITECTURE.md | Agent |
| 7 | Smoke test | Human + Agent |
| 8 | Commit | Human |

Steps 2 and 3 **require human input** — the agent cannot invent project context.
All other steps can be executed autonomously by the agent.
