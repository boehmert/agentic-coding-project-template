# Spec-Driven Development Framework

[![Framework Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/wk-dxg/spec-driven-development-framework)
[![Wolters Kluwer](https://img.shields.io/badge/Wolters%20Kluwer-Internal-orange.svg)](https://github.com/wk-dxg)
[![GitHub Issues](https://img.shields.io/github/issues/wk-dxg/spec-driven-development-framework)](https://github.com/wk-dxg/spec-driven-development-framework/issues)
[![GitHub Stars](https://img.shields.io/github/stars/wk-dxg/spec-driven-development-framework)](https://github.com/wk-dxg/spec-driven-development-framework/stargazers)

A structured framework for AI-assisted software development with specialized agents, workorder specifications, and quality gates. Works with GitHub Copilot, Cursor, and other AI coding assistants.

> **Internal Use Only** – This framework is proprietary to Wolters Kluwer.

**Topics:** `copilot` `github-copilot` `ai-assisted-development` `ai-coding` `development-framework` `software-architecture` `workorder` `architecture-decision-records` `adr` `code-quality` `code-review` `spec-driven-development` `ai-agents` `quality-gates` `developer-tools` `devops` `best-practices` `wolters-kluwer`

## The Problem This Solves

AI coding assistants are powerful but can produce code that is **"70% right"** – almost correct, but with subtle issues in edge cases, error handling, or architecture alignment. This framework addresses that by:

- ✅ **Requiring specs before code** – No implementation without clear scope
- ✅ **Enforcing quality checks** – Validation before and after implementation
- ✅ **Specializing agents** – Each agent has focused responsibilities
- ✅ **Tracking provenance** – Every artifact has version, author, and history

## Overview

This framework provides:
- **7 Specialized Agents** with clear roles and responsibilities
- **Structured Specifications** (Workorders, ADRs, Reports)
- **Quality Gates** (Pre-implementation check, Review)
- **Clear Handoffs** between agents with context preservation
- **Provenance Tracking** via FRAMEWORK_MANIFEST.md

## Quick Start

### Installation

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/wk-dxg/spec-driven-development-framework/main/install.ps1 | iex
```

**macOS / Linux:**
```bash
curl -fsSL https://raw.githubusercontent.com/wk-dxg/spec-driven-development-framework/main/install.sh | bash
```

**Manual:**
```bash
# Clone framework
git clone https://github.com/wk-dxg/spec-driven-development-framework.git temp
# Copy .github folder to your project
cp -r temp/.github /path/to/your/project/
rm -rf temp
```

See [INSTALL.md](INSTALL.md) for detailed installation instructions.

### Initialize your project

```
@workspace /prompt repo-bootstrap

Project: Your Project Name
Description: What your project does
Tech Stack: Python, FastAPI, PostgreSQL
```

### Create your first Workorder

```
@workspace /prompt create-workorder

Task: Implement user authentication
Context: Users need to log in to access protected resources
```

### Run pre-implementation check

```
@workspace /prompt pre-implementation-check WO01
```

### Implement with the Developer agent

```
@workspace Use the developer agent to implement WO01.
```

## Framework Structure

```
.github/
├── copilot-instructions.md     # Global guardrails & agent routing
├── instructions/               # Coding standards
│   ├── spec-driven.instructions.md
│   ├── python.instructions.md
│   ├── markdown.instructions.md
│   └── response-style.instructions.md
├── prompts/                    # Reusable workflows
│   ├── repo-bootstrap.prompt.md
│   ├── create-workorder.prompt.md
│   ├── create-adr.prompt.md
│   ├── pre-implementation-check.prompt.md
│   ├── performance-review.prompt.md
│   └── refactoring-plan.prompt.md
├── agents/                     # Specialized agents
│   ├── architect.agent.md
│   ├── workorder-planner.agent.md
│   ├── developer.agent.md
│   ├── reviewer.agent.md
│   ├── integrator.agent.md
│   ├── documenter.agent.md
│   └── security-reviewer.agent.md
└── schemas/                    # Specification templates
    ├── workorder.schema.md
    ├── adr.schema.md
    ├── report.schema.md
    └── handoff.schema.md
```

## Agents

| Agent | Role | When to Use |
|-------|------|-------------|
| **Architect** | System design, ADRs, tech decisions | Architecture questions, technology choices |
| **Workorder Planner** | Create specs, define scope | Planning new work |
| **Developer** | Write code, tests | Implementation |
| **Reviewer** | Validate plans and code | Before and after implementation |
| **Integrator** | Merge, resolve conflicts | Bringing work to main branch |
| **Documenter** | Documentation, reports | Knowledge artifacts |
| **Security Reviewer** | Security analysis | Security concerns, OWASP checks |

## The Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                    SPEC-DRIVEN WORKFLOW                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐ │
│   │  PLAN    │───▶│IMPLEMENT │───▶│ VALIDATE │───▶│INTEGRATE │ │
│   └──────────┘    └──────────┘    └──────────┘    └──────────┘ │
│        │               │               │               │        │
│   Workorder       Developer        Reviewer       Integrator    │
│   Planner         writes code      checks          merges       │
│   creates spec    and tests        quality         to main      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

1. **Plan**: Create Workorder with clear scope and acceptance criteria
2. **Check**: Run pre-implementation check (Reviewer)
3. **Implement**: Code within approved scope (Developer)
4. **Validate**: Review against criteria (Reviewer)
5. **Integrate**: Merge to main branch (Integrator)

## Key Concepts

### Workorders
Executable specifications that define:
- Goal and context
- Scope (in/out)
- Deliverables
- Acceptance criteria
- Tests

### Architecture Decision Records (ADRs)
Document significant decisions:
- Context and constraints
- Options considered
- Rationale for choice
- Consequences

### The 70% Problem
AI-generated code is often "almost right but not quite". This framework addresses this by:
- Explicit acceptance criteria
- Pre-implementation checks
- Review gates
- Small, reviewable increments

## Compatibility

This framework works with:

| Tool | Status |
|------|--------|
| GitHub Copilot (VS Code) | ✅ Fully supported |
| GitHub Copilot (JetBrains) | ✅ Fully supported |
| Cursor | ✅ Fully supported |
| Claude (API/Cursor) | ✅ Fully supported |
| Other AI assistants | ✅ With custom instructions |

## Communication Style

- **Agent definitions**: English
- **User responses**: Match user's language (German/English)
- **Decision points**: Present options, wait for user decision
- **Uncertainty**: Explicit markers, never guess silently

## Getting Started

### Initialize a New Project
```
Use prompt: repo-bootstrap
```

### Create Your First Workorder
```
Use prompt: create-workorder
```

### Check Before Implementation
```
Use prompt: pre-implementation-check
```

## Contributing

Contributions are welcome! Please:
1. Create a Workorder for your proposed change
2. Follow the framework's own workflow
3. Include tests and documentation

## License

**Wolters Kluwer Internal Use Only** – See [LICENSE](LICENSE) for details.

This software is proprietary to Wolters Kluwer and intended for internal use only.

---

**Framework Version:** 1.0.0  
**Owner:** Wolters Kluwer
