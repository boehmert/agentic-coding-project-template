---
description: "Manage Jira work items with a Jira MCP server. USE THIS SKILL for searching issues, triaging backlogs, creating or updating tickets, and progressing delivery workflows."
applyTo: "**"
priority: core
---

# Jira Integration Skill

Guidance for working with Jira via an MCP server (e.g. `wk-jira` or similar Atlassian MCP assistant).

## When to Use This Skill

Activate when the user needs to:
- Find or search Jira issues
- Triage, prioritize, or refine backlog items
- Create or update tickets
- Move work through workflow states
- Manage ownership, labels, and tracking metadata

## Workflow

1. **Search/discover** — Find relevant issues using text and project filters
2. **Inspect** — Review issue details, status, owner, priority, and linked context
3. **Act** — Create, update, assign, comment, or transition issues as requested
4. **Verify** — Confirm resulting status, ownership, and traceability fields

## Best Practices

- Search first to avoid duplicate tickets before creating a new issue
- Keep issue summaries concise and action-oriented; put implementation detail in descriptions
- Preserve project conventions for issue types, priorities, labels, and sprint/release fields
- For workflow transitions, verify required fields before moving status
- Record rationale in comments when changing priority, scope, or ownership
- Keep acceptance criteria explicit so downstream implementation is testable

## Common Patterns

- **Search by project and keyword**: start broad, then narrow by status/assignee/label
- **Triage flow**: identify duplicates, set priority, assign owner, and capture next action
- **Delivery updates**: move issue state, add progress notes, and link related issues/epics
- **Handoff-ready tickets**: clear context, acceptance criteria, dependencies, and definition of done

## Setup

Configure the Jira MCP server in `.vscode/mcp.json`:
- Set `JIRA_PAT` in `.env` with a valid Personal Access Token
- Set `JIRA_BASE_URL` in `.env` (e.g. `https://your-jira-instance.example.com`)
- See `docs/mcp.json.template` for the server configuration template

When a PAT expires: update the value in `.env` and reload the VS Code window. No changes to `mcp.json` needed.

