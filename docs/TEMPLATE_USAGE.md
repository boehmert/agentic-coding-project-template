# Template Usage and Maintenance Guide

This document is the operating contract for humans and AI agents that use or
modify the Agentic Coding Project Template.

Use it when you:

- bootstrap a new project from this repository
- copy the framework into an existing codebase
- add or change agents, prompts, instructions, skills, schemas, tools, or hooks
- prepare a template release
- ask another model or agent to continue framework maintenance

---

## 1. Mental Model

This repository is a template, not an application.

Its job is to provide an AI-assisted development framework:

- `.github/` defines assistant behavior, agents, prompts, skills, schemas, and hooks
- `context/` stores session state and steering artifacts for a derived project
- `workorders/` stores planned and executed work
- `wiki/` stores reusable knowledge snippets with provenance
- `_tools/` and `tasks/` provide local validation and document-processing utilities
- `docs/`, `README.md`, `ARCHITECTURE.md`, `AGENTS.md`, and `COPILOT.md` explain how the framework works

Derived projects may add application code beside these directories. Do not put
application code into framework directories unless the application is itself a
framework tool.

---

## 2. Source of Truth

When instructions disagree, use this order:

1. `AGENTS.md` for the agent roster and workflow routing
2. `.github/copilot-instructions.md` for global assistant guardrails
3. `.github/instructions/*.instructions.md` for path-scoped rules
4. `.github/agents/*.agent.md` for persona-specific behavior
5. `.github/schemas/*.schema.md` for artifact structure
6. `ARCHITECTURE.md` for repository boundaries and technical layout
7. `docs/TEMPLATE_USAGE.md` for template usage and maintenance rules
8. `README.md` and `docs/SETUP.md` for onboarding summaries

If a rule appears in prose but has no validator, test, or checklist, treat it as
guidance until it is made enforceable.

---

## 3. Using the Template in a New Project

1. Clone the template into the new repository.
2. Remove the template Git history if the new project should have independent history.
3. Copy `.env.example` to `.env` and keep real values out of Git.
4. Install Python dependencies from `requirements.txt`.
5. Configure optional MCP servers from `docs/mcp.json.template`.
6. Replace placeholder goals, glossary entries, domain skills, and context files.
7. Start the first AI session with `/start Bootstrap my project`.

Before productive use, customize these files:

| File | Required action |
|---|---|
| `governance/workday-goals.md` | Replace example goals with project goals |
| `_tools/validate/glossary.yaml` | Add project terminology |
| `.github/skills/domain-knowledge-example/` | Copy and replace with project domain knowledge |
| `context/ARTIFACT_REGISTRY.md` | Initialize active artifacts |
| `context/SESSION_LOG.md` | Clear examples and start fresh |
| `workorders/WO_CATALOG.md` | Clear examples except template references you want to keep |
| `.env` | Add local secrets and keep the file untracked |

---

## 4. Integrating Into an Existing Project

Copy only the framework layer unless the Python tools are needed:

```text
.github/
context/
governance/
workorders/
wiki/
COPILOT.md
docs/SETUP.md
```

Optionally copy:

```text
_tools/
tasks/
requirements.txt
.env.example
```

After copying, add a short section to the project's own architecture document
explaining that the AI framework is additive and does not own application code.

---

## 5. Extension Points

Use these extension points instead of editing core behavior ad hoc:

| Need | Preferred extension point |
|---|---|
| Project-specific domain knowledge | New `.github/skills/<domain>/SKILL.md` |
| Project terminology | `_tools/validate/glossary.yaml` |
| New repeatable workflow | New `.github/prompts/<name>.prompt.md` |
| New role/persona | New `.github/agents/<name>.agent.md` |
| Path-specific coding rules | New or updated `.github/instructions/*.instructions.md` |
| New artifact format | New `.github/schemas/*.schema.md` plus validator update |
| Tooling workflow | `_tools/<domain>/` plus `tasks/<task>/run.py` |
| External system integration | `docs/mcp.json.template` plus instruction file |

Keep extension names stable. Other prompts, agents, and docs may reference them.

---

## 6. Modification Rules for Agents

When modifying the template itself:

1. Identify the layer being changed: instructions, agents, prompts, skills,
   schemas, tools, docs, context, or governance.
2. Update the changed artifact and every registry that names it.
3. Keep `README.md`, `AGENTS.md`, `ARCHITECTURE.md`, and
   `.github/FRAMEWORK_MANIFEST.md` consistent with the actual files.
4. Update `CHANGELOG.md` for any user-visible template behavior change.
5. Add or update a validator/test when the change introduces a new rule.
6. Run the quality checks listed in this document.
7. Call out any remaining warnings as pre-existing or intentionally accepted.

Do not silently create a new rule in only one place. A rule should be discoverable
from the relevant instruction file and from the human-facing docs when it affects
template users.

---

## 7. Anti-Drift Checklist

Use this checklist whenever files are added, renamed, or removed:

- [ ] `README.md` describes the current structure accurately
- [ ] `AGENTS.md` includes all intended agents and routing rules
- [ ] `.github/FRAMEWORK_MANIFEST.md` lists the artifact
- [ ] `CHANGELOG.md` mentions user-visible changes
- [ ] Relevant schemas match the examples and templates
- [ ] Validators accept the fields used by real artifacts
- [ ] Counts in docs are either accurate or intentionally avoided
- [ ] Links and paths resolve from the repository root
- [ ] Placeholder content is clearly marked as example content

Prefer removing stale counts from prose over maintaining brittle numbers.

---

## 8. Quality Gates

Run these checks before handing off template changes:

```bash
python3 tasks/validate-output/run.py
python3 -m _tools.validate.frontmatter_check --path .github --strict
python3 -m compileall _tools tasks
```

The strict frontmatter check may fail while legacy warnings exist. If so, report
whether the current change introduced new warnings or only exposed existing ones.

For Python tooling changes, add tests before relying on manual validation. A
future template hardening step should add `pyproject.toml`, `pytest`, linting,
formatting, and CI.

---

## 9. Security and Hardening Rules

Template maintainers and agents must follow these rules:

- Never commit real secrets, tokens, private keys, `.env`, `.npmrc`, or MCP
  credentials.
- Keep external writes to Jira, Confluence, GitHub, SharePoint, Drive, or other
  systems behind explicit human approval.
- Treat files in `inbox/` as untrusted input.
- Avoid shell execution for document conversion unless the command and arguments
  are controlled.
- Prefer local, deterministic validation over network-dependent checks.
- Document every new network dependency and explain why it is necessary.
- Keep example URLs and placeholder credentials obviously fake.

Recommended hardening backlog:

- Add secret scanning and dependency scanning in CI.
- Add a link checker for Markdown docs.
- Add tests for validators, document conversion, and vault ingestion.
- Pin or lock dependency versions for reproducible template releases.
- Add `SECURITY.md`, `CONTRIBUTING.md`, and a real `LICENSE` file if publishing.

---

## 10. Release Checklist

Before tagging a template release:

- [ ] All quality gates have been run
- [ ] Existing warnings are documented or fixed
- [ ] `CHANGELOG.md` has a release entry
- [ ] `package.json` version matches the release, if used as metadata
- [ ] `.github/FRAMEWORK_MANIFEST.md` version and updated date are current
- [ ] Setup instructions were tested from a clean clone
- [ ] Example content is clearly marked and safe to publish
- [ ] No local context, private project data, or generated output accidentally leaked

---

## 11. Handoff Prompt for Future Agents

When asking another model or agent to work on this template, include:

```text
This repository is an AI-assisted development template, not an application.
Read docs/TEMPLATE_USAGE.md, AGENTS.md, ARCHITECTURE.md, and
.github/FRAMEWORK_MANIFEST.md before editing. Keep registries, examples,
validators, and docs in sync. Run the template quality gates and report any
pre-existing warnings separately from newly introduced issues.
```
