---
description: "Bootstrap a new repository with complete project structure"
tools:
  - "editFiles"
  - "runCommands"
  - "codebase"
---

# Repository Bootstrap

This prompt guides you through setting up a new repository with the complete spec-driven development structure.

## Overview

This will create:
- Project structure (src, tests, docs, etc.)
- Configuration files
- Initial documentation
- Workorder catalog
- First Workorder (WO00 - Bootstrap)

---

## Required Information

Please provide the following:

### Project Basics
- **Project Name**: ${input:projectName:my-project}
- **Project Description**: ${input:projectDescription:A brief description of the project}
- **Primary Language**: ${input:language:python}
- **Author/Team**: ${input:author:Team Name}

### Repository Type
- [ ] New greenfield project
- [ ] Existing project (adding structure)

---

## Directory Structure

The following structure will be created:

```
${projectName}/
├── .github/
│   ├── copilot-instructions.md
│   ├── instructions/
│   │   ├── spec-driven.instructions.md
│   │   ├── ${language}.instructions.md
│   │   ├── markdown.instructions.md
│   │   └── response-style.instructions.md
│   ├── prompts/
│   ├── agents/
│   └── schemas/
│       ├── workorder.schema.md
│       ├── adr.schema.md
│       ├── report.schema.md
│       └── handoff.schema.md
├── src/
│   └── ${projectName}/
│       └── __init__.py
├── tests/
│   ├── unit/
│   └── integration/
├── docs/
│   ├── adr/
│   └── guides/
├── workorders/
│   ├── WO_CATALOG.md
│   ├── WO00_repo-bootstrap.md
│   └── reports/
├── schemas/
├── data/
│   ├── input/
│   └── output/
├── .env.example
├── .gitignore
├── README.md
├── REPO_STATE.md
├── requirements.txt (or pyproject.toml)
└── LICENSE
```

---

## Files to Create

### README.md
```markdown
# ${projectName}

${projectDescription}

## Quick Start

1. Clone the repository
2. Create virtual environment: `python -m venv .venv`
3. Activate: `.venv\Scripts\activate` (Windows) or `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

## Documentation

- [Repository State](REPO_STATE.md)
- [Workorder Catalog](workorders/WO_CATALOG.md)
- [Architecture Decisions](docs/adr/)

## Development

This project follows a spec-driven development workflow:
1. **Plan**: Create Workorder before coding
2. **Implement**: Code within approved scope
3. **Validate**: Review against acceptance criteria
4. **Integrate**: Merge approved changes

## License

[License Type]
```

### REPO_STATE.md
```markdown
# Repository State

**Last Updated:** ${date}
**Updated By:** ${author}

## Current Status

Project initialized. Ready for first feature development.

## Active Workorders

| ID | Title | Status | Assignee |
|----|-------|--------|----------|
| WO00 | Repo Bootstrap | DONE | ${author} |

## Completed Workorders

(None yet)

## Known Issues

(None)

## Next Steps

1. Define first feature Workorder
2. Review architecture needs
3. Set up CI/CD
```

### workorders/WO_CATALOG.md
```markdown
# Workorder Catalog

Central registry of all Workorders in this project.

## Active

| ID | Title | Status | Priority | Created | Assignee |
|----|-------|--------|----------|---------|----------|
| WO00 | Repo Bootstrap | DONE | HIGH | ${date} | ${author} |

## Completed

| ID | Title | Completed | Report |
|----|-------|-----------|--------|
| WO00 | Repo Bootstrap | ${date} | [Report](reports/WO00_report_${date}.md) |

## Cancelled

(None)
```

### workorders/WO00_repo-bootstrap.md
```markdown
---
id: WO00
title: "Repository Bootstrap"
version: 1.0.0
status: DONE
created: ${date}
created_by: ${author}
priority: HIGH
estimated_effort: "1-2 hours"
---

# WO00: Repository Bootstrap

## 1. Context

Initialize the repository with the complete spec-driven development structure.

## 2. Goal

Create a fully configured repository ready for feature development.

## 3. Scope

### In Scope
- Directory structure
- Configuration files
- Initial documentation
- Workorder catalog
- Development environment setup

### Out of Scope
- Feature implementation
- CI/CD pipeline (future WO)
- Deployment configuration (future WO)

## 4. Deliverables

| # | Deliverable | Location | Status |
|---|-------------|----------|--------|
| 1 | Directory structure | / | ✅ |
| 2 | README | /README.md | ✅ |
| 3 | Repo state | /REPO_STATE.md | ✅ |
| 4 | WO Catalog | /workorders/WO_CATALOG.md | ✅ |
| 5 | This Workorder | /workorders/WO00_repo-bootstrap.md | ✅ |

## 5. Definition of Done

- [x] All directories created
- [x] All template files in place
- [x] README complete
- [x] WO_CATALOG.md initialized
- [x] WO00 complete and documented

---

## Changelog

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | ${date} | ${author} | Initial bootstrap |
```

### .env.example
```
# Environment Configuration
# Copy to .env and fill in values

# Project
PROJECT_NAME=${projectName}
ENVIRONMENT=development

# Add project-specific variables below
```

### .gitignore
```
# Python
__pycache__/
*.py[cod]
*$py.class
.venv/
venv/
*.egg-info/
dist/
build/

# Environment
.env
.env.local

# IDE
.vscode/
.idea/
*.swp

# Data
data/output/
*.log

# OS
.DS_Store
Thumbs.db
```

---

## Execution Steps

1. Create directory structure
2. Copy framework files from `.github/` template
3. Create project-specific files
4. Initialize git (if not exists)
5. Create WO00 completion report
6. Verify structure

---

## After Completion

- [ ] Verify all directories exist
- [ ] Verify README is complete
- [ ] Verify WO_CATALOG.md is initialized
- [ ] Run initial tests (if any)
- [ ] Make initial commit
