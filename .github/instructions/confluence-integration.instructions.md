---
description: "Manage Confluence content with a Confluence MCP server. USE THIS SKILL for finding pages/spaces, searching docs, creating and updating pages, and adding metadata."
applyTo: "**"
priority: core
---

# Confluence Integration Skill

Guidance for working with Confluence via an MCP server (e.g. `wk-confluence` or similar Atlassian MCP assistant).

## When to Use This Skill

Activate when the user needs to:
- Find or search documentation in Confluence
- Create or update pages
- Add metadata or properties to pages
- Organize page hierarchies

## Workflow

1. **Search/discover** — Use SearchContent for keyword searches or SearchCQL for precise filters
2. **Inspect** — Fetch target space or page details to understand context
3. **Create/update** — PageCreate for new content, PageUpdate for edits
4. **Enhance** — Use PropertyCreate to attach structured metadata

## Best Practices

- **Search strategy**: Start with SearchContent for exploratory searches; use SearchCQL when you need precise filtering (e.g., by space, status, label)
- **Page bodies**: Always use Confluence storage format (XHTML). Invalid markup causes rendering failures
- **Version handling**: PageUpdate requires the current version number. Fetch fresh before updating to avoid conflicts
- **Metadata**: Use properties for structured data (owner, domain, tags, status) rather than embedding in page body
- **Spaces**: Reuse existing spaces when possible; create new spaces only when governance requires it

## Common Patterns

- **Search by space and topic**: Use CQL with `space = "KEY"` and `text ~ "keyword"` for precise results
- **Bulk page listing**: SpaceList with pagination (`limit`, `start`) to traverse many pages
- **Update workflow**: Get current page → extract body/version → modify → PageUpdate with matching version
- **Hierarchies**: PageCreate accepts `parentId` to establish child relationships

## Setup

Configure the Confluence MCP server in `.vscode/mcp.json`:
- Set `CONFLUENCE_PAT` in `.env` with a valid Personal Access Token
- Set `CONFLUENCE_BASE_URL` in `.env` (e.g. `https://your-confluence-instance.example.com`)
- See `docs/mcp.json.template` for the server configuration template

When a PAT expires: update the value in `.env` and reload the VS Code window. No changes to `mcp.json` needed.

