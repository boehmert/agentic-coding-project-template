# Knowledge Retrieval Skill

Retrieve knowledge from internal systems (Confluence, Jira, SharePoint, OneDrive) via MCP servers or Microsoft 365 Copilot connectors.

## When to Use

- Search organizational knowledge bases
- Find documentation across Confluence spaces
- Query Jira issues and project data
- Access content indexed by Microsoft 365 Copilot connectors

## Prerequisites

- MCP servers configured in `.vscode/mcp.json` (see `docs/mcp.json.template`)
- Authentication tokens in `.env`

## Tools

The skill uses MCP server tools for:

| System | MCP Server | Tools |
|--------|------------|-------|
| Confluence | `wk-confluence` or similar | `SearchContent`, `PageGet`, `SpaceList` |
| Jira | `wk-jira` or similar | `jira_issue_search`, `jira_issue_get` |
| Microsoft Graph | `microsoft-graph` | `SearchFiles`, `DriveGetContent` |
| Vault (local) | `vault-mcp` | `vault_search`, `vault_context` |

## Search Strategy

1. **Vault first**  Local curated knowledge
2. **wiki/**  LLM-generated snippets with provenance
3. **Workspace files**  `context/` folder
4. **External systems**  Confluence, Jira, SharePoint via MCP

## Configuration

Copy `docs/mcp.json.template` to `.vscode/mcp.json` and fill in your organization-specific values.

## Customization

Replace the MCP server names and NPM packages with your organization's equivalents. The search strategy and tool patterns remain the same regardless of the specific MCP implementation.
