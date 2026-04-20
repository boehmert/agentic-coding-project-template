# Setup Guide

This guide covers two scenarios for using this template:

1. **New project** — Start a fresh repository with the full framework
2. **Existing project** — Integrate the framework into an already existing codebase

---

## Scenario A: New Project

Use this when you are starting a greenfield project and want the full framework from the start.

### Step 1: Clone and detach

```bash
git clone https://github.com/boehmert/agentic-coding-project-template.git my-project
cd my-project
rm -rf .git
git init
git add -A
git commit -m "chore: bootstrap from agentic-coding-project-template v2.x"
```

### Step 2: Configure environment

```bash
cp .env.example .env
# Open .env and fill in your values:
#   VAULT_PATH       → path to your Obsidian vault (optional)
#   CONFLUENCE_PAT   → Personal Access Token (optional)
#   CONFLUENCE_BASE_URL → https://your-confluence.example.com (optional)
#   JIRA_PAT         → Personal Access Token (optional)
#   JIRA_BASE_URL    → https://your-jira.example.com (optional)
```

### Step 3: Install Python dependencies

```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
# .venv\Scripts\Activate.ps1    # Windows PowerShell

pip install -r requirements.txt
```

### Step 4: Configure MCP servers (optional)

```bash
cp docs/mcp.json.template .vscode/mcp.json
# Edit .vscode/mcp.json:
#   - Set vault path for vault-mcp
#   - Add Jira/Confluence servers if needed (see template for examples)
```

### Step 5: Customize for your project

| File | What to customize |
|------|------------------|
| `governance/workday-goals.md` | Replace example goals with your annual goals |
| `governance/activity-log.md` | Clear example entries, start fresh |
| `_tools/validate/glossary.yaml` | Add your domain terminology |
| `.github/skills/domain-knowledge-example/` | Copy → rename → fill with your domain |
| `.github/instructions/workday-goals.instructions.md` | Update goal names |
| `context/ARTIFACT_REGISTRY.md` | Clear — will auto-populate during work |

### Step 6: Start working

In VS Code Copilot Chat:

```
/start Bootstrap my project — [describe your project here]
```

---

## Scenario B: Integrate into an Existing Project

Use this when you have an existing codebase and want to add the agentic framework on top.

### What to copy

The framework is fully contained in these directories — they are independent of your application code:

```
.github/           ← All Copilot configuration (agents, prompts, skills, instructions, schemas, hooks)
context/           ← Session and artifact tracking
governance/        ← Goals and activity log
workorders/        ← Spec-driven planning artifacts
wiki/              ← Knowledge management
docs/SETUP.md      ← This file
COPILOT.md         ← Copilot project context
```

These directories are **additive** — they do not interfere with existing source code, tests, or CI/CD.

### Step 1: Copy framework directories

```bash
# From inside your existing project:
git remote add template https://github.com/boehmert/agentic-coding-project-template.git
git fetch template

# Copy only the framework files (no application code)
git checkout template/main -- .github context governance workorders wiki COPILOT.md

# Optional Python tooling (only if you want validation/document pipeline)
git checkout template/main -- _tools tasks requirements.txt .env.example
```

Alternatively, download the ZIP from GitHub and manually copy the directories above.

### Step 2: Configure

Follow Steps 2–5 from Scenario A above.

### Step 3: Wire up ARCHITECTURE.md

If your project already has an `ARCHITECTURE.md`, append a section explaining the framework layer:

```markdown
## AI Framework Layer

This project uses the [Agentic Coding Project Template](https://github.com/boehmert/agentic-coding-project-template)
for AI-assisted development. See `COPILOT.md` for the framework overview and `docs/SETUP.md` for setup instructions.
```

### Step 4: Initialize context files

Clear the example content in the context files and initialize for your project:

- `context/ARTIFACT_REGISTRY.md` — set `last_updated` to today, clear placeholder rows
- `context/SESSION_LOG.md` — keep the header, delete the example comment block
- `workorders/WO_CATALOG.md` — clear example rows

### Step 5: Start working

```
/start I have integrated the agentic framework into my existing project. Help me orient.
```

---

## Required Customization Checklist

Regardless of scenario, complete these before productive use:

- [ ] `.env` filled with relevant credentials (Vault path minimum)
- [ ] `governance/workday-goals.md` updated with your actual goals
- [ ] `_tools/validate/glossary.yaml` — add your project's domain terms
- [ ] `.github/skills/domain-knowledge-example/` copied and renamed for your domain
- [ ] `context/ARTIFACT_REGISTRY.md` initialized
- [ ] MCP servers configured in `.vscode/mcp.json` (if using Jira/Confluence/Vault)

---

## Directory Reference

| Directory | Purpose | Required |
|-----------|---------|----------|
| `.github/` | All Copilot/AI configuration | Yes |
| `context/` | Session memory and artifact index | Yes |
| `governance/` | Goals and activity tracking | Yes |
| `workorders/` | Spec-driven work planning | Yes |
| `wiki/` | Knowledge snippets with provenance | Recommended |
| `_tools/` | Python validation and conversion tools | Optional |
| `tasks/` | CLI entrypoints for `_tools/` | Optional |
| `inbox/` | Drop input files here for processing | Optional |
| `output/` | Generated artifacts land here | Optional |
| `examples/` | Sample inputs for reference | Optional |
| `docs/adr/` | Architecture Decision Records | Recommended |

---

## Troubleshooting

**Agents don't appear in the `@` picker in VS Code**

VS Code Copilot (≥ 0.26) requires agents to be in the user-level agents folder for the picker:
```
macOS:   ~/Library/Application Support/Code/User/agents/
Windows: %APPDATA%\Code\User\agents\
Linux:   ~/.config/Code/User/agents/
```
Copy agent files there. `.github/agents/` files are loaded contextually by Copilot but not shown in the picker.

**`tasks/validate-output/run.py` fails with import errors**

Ensure the virtual environment is active and `requirements.txt` is installed:
```bash
source .venv/bin/activate
pip install -r requirements.txt
python tasks/validate-output/run.py
```

**MCP server not connecting**

1. Check `.vscode/mcp.json` exists (copy from `docs/mcp.json.template`)
2. Verify all paths/tokens in `.env` are set correctly
3. Reload VS Code window (`Cmd+Shift+P` → "Developer: Reload Window")
