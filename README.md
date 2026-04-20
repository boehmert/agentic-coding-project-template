# Agentic Coding Project Template

A comprehensive framework for AI-assisted software development with specialized agents, structured workflows, knowledge management, and quality gates. Works with GitHub Copilot, Cursor, and other AI coding assistants.

## When to Use This Template

This template serves two scenarios:

**Scenario A — New project:** Clone and use as the foundation for a greenfield project. You get the full framework structure from day one.

**Scenario B — Existing project:** Copy the framework directories (`.github/`, `context/`, `workorders/`, `wiki/`) into an existing codebase. The framework is additive and does not interfere with application code.

→ See **[docs/SETUP.md](docs/SETUP.md)** for full setup instructions for both scenarios.

---

## The Problem This Solves

AI coding assistants are powerful but can produce code that is **"70% right"** — almost correct, but with subtle issues in edge cases, error handling, or architecture alignment. This framework addresses that by:

- **Requiring specs before code** — No implementation without clear scope
- **Enforcing quality checks** — Validation before and after implementation
- **Specializing agents** — Each agent has focused responsibilities
- **Managing knowledge** — wiki/ system with provenance tracking
- **Preserving context** — Session continuity across conversations
- **Tracking provenance** — Every artifact has version, author, and history

## What's Included

### Layer 1: Spec-Driven Development (Foundation)
From the original [vibecoding-project-template](https://github.com/boehmert/vibecoding-project-template):
- 12 specialized agents (architect, developer, reviewer, etc.)
- Workorder and ADR schemas with versioning
- Pre-implementation checks and quality gates
- Structured handoff protocols between agents

### Layer 2: Knowledge Management (Advanced)
- **wiki/ system** — LLM-generated knowledge snippets with provenance frontmatter
- **Vault integration** — Obsidian Vault via MCP server for persistent knowledge
- **Validation pipeline** — Frontmatter, terminology, and AI-style checks
- **AI content detection** — Stylometric analysis to identify AI-generated text

### Layer 3: Session Continuity
- **Memory system** — Three scopes: user, session, repository
- **Active context** — Automatic session state preservation (`/save-session`)
- **Session hooks** — Auto-reminders for session start/stop workflows
- **Context transfer** — Structured handover between sessions

### Layer 4: Governance & Goals
- **Activity logging** — Track work against defined goals
- **Goal alignment** — Copilot outputs aligned with annual objectives
- **Writing style** — Configurable style guide for consistent output

---

## Quick Start

### New Project

```bash
git clone https://github.com/boehmert/agentic-coding-project-template.git my-project
cd my-project && rm -rf .git && git init
cp .env.example .env
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Then in VS Code Copilot Chat: `/start Bootstrap my project`

### Existing Project

Copy `.github/`, `context/`, `governance/`, `workorders/`, `wiki/`, `COPILOT.md` into your repo.

→ **Full instructions for both scenarios: [docs/SETUP.md](docs/SETUP.md)**

---

## Framework Structure

```
.github/
├── copilot-instructions.md          # Global guardrails & routing
├── instructions/                    # Path-scoped rules (~15 files)
│   ├── vibecoding-core.instructions.md
│   ├── vibecoding-extended.instructions.md
│   ├── spec-driven.instructions.md
│   ├── memory-system.instructions.md
│   ├── wiki-provenance.instructions.md
│   ├── vault-knowledge.instructions.md
│   └── ...
├── agents/                          # Specialized agents (12)
│   ├── architect.agent.md
│   ├── developer.agent.md
│   ├── critical-thinker.agent.md
│   ├── doublecheck.agent.md
│   └── ...
├── prompts/                         # Reusable workflows (20+)
│   ├── save-session.prompt.md
│   ├── start.prompt.md
│   ├── wiki-write.prompt.md
│   ├── create-workorder.prompt.md
│   └── ...
├── skills/                          # Domain knowledge bundles (10)
│   ├── ai-content-check/
│   ├── document-pipeline/
│   ├── schreibstil/
│   ├── domain-knowledge-example/    # ← Replace with your domain
│   └── ...
├── schemas/                         # Specification templates
│   ├── workorder.schema.md
│   ├── adr.schema.md
│   └── ...
└── hooks/                           # Session automation
    └── scripts/

_tools/                              # Python libraries
├── validate/                        # Frontmatter, terminology, AI-style
├── ai_detect/                       # AI content detection
├── documents/                       # Format conversion
└── vault/                           # Vault ingestion

tasks/                               # CLI entrypoints
└── validate-output/                 # Run validation checks

wiki/                                # Knowledge base
├── _INDEX.md                        # Auto-maintained index
└── agentic-coding/                  # Example articles

governance/                          # Goals & tracking
├── workday-goals.md
└── activity-log.md

workorders/                          # Planning artifacts
└── _template/

context/                             # Session & artifact tracking
├── ARTIFACT_REGISTRY.md
├── SESSION_LOG.md
└── USER_INTENT_LOG.md
```

---

## Agents

### From Layer 1 (Spec-Driven)

| Agent | Role | When to Use |
|-------|------|-------------|
| **Architect** | System design, ADRs, tech decisions | Architecture questions |
| **Workorder Planner** | Create specs, define scope | Planning new work |
| **Developer** | Write code, tests | Implementation |
| **Reviewer** | Validate plans and code | Quality gates |
| **Integrator** | Merge, resolve conflicts | PR preparation |
| **Documenter** | Documentation, reports | Knowledge artifacts |
| **Security Reviewer** | Security analysis | OWASP concerns |

### From Layer 2 (Knowledge & Review)

| Agent | Role | When to Use |
|-------|------|-------------|
| **ADR Generator** | Create ADRs with structured formatting | Architecture decisions |
| **Critical Thinker** | Challenge assumptions, find blind spots | Before major decisions |
| **Doublecheck** | Fact-check AI outputs, flag risks | Verification |

---

## Key Workflows

### The Vibecoding Loop
```
Context → Goals → Plan → Execute → Review
```
Every non-trivial task follows this loop. See `vibecoding-core.instructions.md`.

### Spec-Driven Development
```
Plan → Check → Implement → Validate → Integrate
```
Workorders define scope; quality gates enforce standards.

### Knowledge Management
```
/wiki-write → wiki/ snippet → /wiki-lint → wiki/_INDEX.md
```
Knowledge snippets have provenance frontmatter (source, confidence, review status).

### Session Continuity
```
/start → work → /save-session → (next session) → /start
```
Context persists across conversations via memory system.

---

## Customization

### Add Your Domain Knowledge
1. Copy `.github/skills/domain-knowledge-example/` → `.github/skills/your-domain/`
2. Replace example content with your terminology, architecture, patterns
3. Update `_tools/validate/glossary.yaml` with your canonical terms

### Add External Integrations
1. Edit `docs/mcp.json.template` to add MCP server definitions
2. Copy template to `.vscode/mcp.json`
3. Add corresponding instruction file in `.github/instructions/`

### Customize Goals
1. Edit `governance/workday-goals.md` with your annual goals
2. The activity log at `governance/activity-log.md` tracks progress automatically

---

## Compatibility

| Tool | Status |
|------|--------|
| GitHub Copilot (VS Code) | Fully supported |
| GitHub Copilot (JetBrains) | Agents + Instructions supported |
| Cursor | Fully supported |
| Claude (API/Cursor) | Fully supported |
| Other AI assistants | With custom instructions |

---

## Version History

- **v2.0** (April 2026) — Added Knowledge Management, Session Continuity, Validation Pipeline, AI Detection, Vault integration, Governance layer
- **v1.0** (February 2026) — Spec-Driven Development Foundation (agents, schemas, prompts, quality gates)

---

## Related

- [vibecoding-project-template](https://github.com/boehmert/vibecoding-project-template) — The simpler v1 foundation (public template)
