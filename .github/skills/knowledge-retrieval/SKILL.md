---
name: knowledge-retrieval
description: Retrieve knowledge from internal systems (Confluence, Jira, Azure DevOps, Salesforce, SharePoint, OneDrive) via Microsoft 365 Copilot connectors. Optionally maintains a knowledge/ folder with auto-refreshing markdown docs as a curated knowledge base. Use when the user needs to search organizational knowledge bases, find documentation, look up Confluence pages, query Jira issues, or access content indexed by Microsoft 365 Copilot connectors.
license: BSD-3-Clause
---

# Knowledge Retrieval Skill

Retrieve knowledge from internal systems (Confluence, Jira, Azure DevOps, Salesforce, SharePoint, OneDrive) using MCP tools backed by the Microsoft Graph Copilot Retrieval API. If a `knowledge/` folder exists in the repository, this skill also manages a curated knowledge base of auto-refreshing markdown documents.

## When to Use

- User asks about organizational knowledge, internal documentation, or company-specific information
- Need to search Confluence spaces, Jira issues, SharePoint sites, or OneDrive files
- Looking for specific documents, pages, or content indexed by Microsoft 365 Copilot connectors
- Building or refreshing curated knowledge files in the `knowledge/` folder

## Available Operations

Use the MCP tools from the **"Retrieve"** server:

- **`CopilotRetrieve`** — Main search tool. Always use `parallelSources: true` and `maximumNumberOfResults: 5-10`. Use `filterExpression` for KQL filtering (see below).
- **`CopilotGetItem`** — Get a specific item by its `secondaryId` (from retrieval results).
- **`GetExternalItem`** — Get an external item directly by `id` and `connectionId`.
- **Other tools** (`SearchFiles`, `SearchSites`, `DriveGetContent`, etc.) — Use as needed for specialized queries.
---

## KQL Filtering Reference

Use `filterExpression` in `CopilotRetrieve` to scope results with Keyword Query Language (KQL).

**Syntax:**
```
propertyName:"value"
propertyName:"value1" AND propertyName:"value2"
propertyName:"value1" OR propertyName:"value2"
NOT propertyName:"value"
```

### SharePoint / OneDrive Properties

| Property | Example |
|----------|---------|
| `Author` | `Author:"John Doe"` |
| `FileExtension` | `FileExtension:"docx"` |
| `Filename` | `Filename:"architecture"` |
| `FileType` | `FileType:"pdf"` |
| `LastModifiedTime` | `LastModifiedTime>="2025-01-01"` |
| `ModifiedBy` | `ModifiedBy:"Jane Smith"` |
| `Path` | `Path:"https://company.sharepoint.com/sites/engineering"` |
| `SiteID` | `SiteID:"guid-here"` |
| `Title` | `Title:"deployment guide"` |

### Confluence Properties (via Copilot Connectors)

| Property | Example |
|----------|---------|
| `secondaryId` | `secondaryId:"12345"` |
| `title` | `title:"API Documentation"` |
| `containerName` | `containerName:"Engineering"` |
| `authors` | `authors:"john.doe"` |
| `lastModifiedBy` | `lastModifiedBy:"jane.smith"` |
| `containerUrl` | `containerUrl:"https://confluence.example.com/display/ENG"` |
| `state` | `state:"published"` |
| `url` | `url:"https://confluence.example.com/x/abc123"` |
| `lastModifiedDateTime` | `lastModifiedDateTime>="2025-06-01"` |
| `createdDateTime` | `createdDateTime>="2025-01-01"` |
| `createdBy` | `createdBy:"admin"` |
| `itemPath` | `itemPath:"/spaces/ENG/pages"` |
| `itemType` | `itemType:"page"` |

### Filter Examples

```
containerName:"Engineering"                                    # Confluence space
lastModifiedDateTime>="2025-06-01"                             # Recent pages
containerName:"Engineering" AND authors:"john.doe"             # Combined
FileExtension:"pdf" AND Path:"https://company.sharepoint.com/sites/docs"  # SharePoint PDFs
```

---

## Knowledge Storage

> This section applies **only** when a `knowledge/` folder exists at the repository root (even if empty). Use `list_dir` to verify. If the folder does not exist, operate in **retrieval-only mode**: return results directly to the user without creating files.

When enabled, the `knowledge/` folder is the primary source of truth for curated documentation. Always save retrieved information as knowledge files, and check for existing files before creating new ones.

### Folder Structure

```
knowledge/
├── features/       # Feature-specific docs (copilot-retrieval.md, refrag-engine.md)
├── common/         # Cross-cutting concerns (authentication-flow.md, error-handling.md)
├── guidelines/     # Standards (conventional-commits.md, code-style.md)
└── architecture/   # System design (tool-architecture.md, mcp-server-design.md)
```

**File naming:** `kebab-case` (e.g., `microsoft-graph-authentication.md`)

**Request translation:**
- "How does auth work?" → `knowledge/common/authentication-flow.md`
- "What's REFRAG?" → `knowledge/features/refrag-engine.md`
- "Coding standards?" → `knowledge/guidelines/code-style.md`

### File Format

```yaml
---
title: "Human-Readable Title"
summary: "2-3 sentence description"
last-update: "2025-12-19T14:00:00Z"  # ISO 8601
sources: ["copilot-retrieval", "code-analysis", "repo-docs"]
staleness-threshold: "7d"  # Optional (default: 7d). Format: Xd, Xh, Xm
related-files: ["src/tools/validate.ts"]
tags: ["retrieval", "copilot", "rag"]
confidence: "high"  # high | medium | low
---
```

**Content sections:** Overview (2-4 sentences) → Details (subsections, code snippets) → Warnings & Insights (`[!WARNING]`, `[!IMPORTANT]`, `[!TIP]`) → Related Files (markdown links)

### Lifecycle

#### 1. Check Freshness

1. Search `knowledge/` by keywords
2. Read header (lines 1-30) for metadata
3. Compare `last-update` against `staleness-threshold` (default: 7d)

#### 2. Serve or Refresh

- **Fresh** (within threshold): Return content immediately. **Do NOT** call retrieval tools.
- **Stale** (exceeds threshold): Return content with warning `⚠️ This knowledge may be outdated (last updated: <date>). Refresh?` — wait for user confirmation before re-retrieving.
- **Missing**: Proceed to Create New Knowledge.

> **CRITICAL**: Only use CopilotRetrieve when no fresh knowledge exists OR user explicitly requests a refresh.

#### 3. Create / Refresh Knowledge

1. **Retrieve**: Use `CopilotRetrieve` with `parallelSources: true` and `maximumNumberOfResults: 5`
2. **Analyze repo**: Search/read `.md`, `.ts` files if relevant
3. **Analyze code**: Read `related-files` source if applicable
4. **Synthesize**: Apply source hierarchy, flag conflicts
5. **Save**: Write to `knowledge/<category>/<topic>.md` with frontmatter
6. **Respond**: Tell user about the file with link and brief summary

On refresh, do a complete regeneration (not merge). Update `last-update` and `confidence`.

#### 4. Delete Obsolete

Remove file when no longer relevant. Git history preserves old versions.

### Source Hierarchy

**Priority:** Code (truth) > Repository Docs > External Docs

On conflict: trust the hierarchy, flag in warnings ("External docs suggest X, code uses Y. Following code."), lower confidence to `medium`/`low`.

---

## Error Handling

| Error | Action |
|-------|--------|
| Tool not available | MCP server may not be running — notify user |
| 400 Bad request | Check query length (<1500 chars) and KQL syntax |
| 401/403 Permissions | Some sources may be unavailable due to missing scopes — skip and mark confidence `medium`/`low` |
| 429 Rate limited | Wait and retry |
| 500 Server error | Retry after brief delay |

## Skill Boundaries

**Will:** Retrieve from Microsoft 365 sources, synthesize multi-source information, manage knowledge lifecycle (when `knowledge/` folder exists), handle missing permissions gracefully.

**Won't:** Modify source code, make business decisions, execute unrelated commands, store secrets.

---

*Skill Version: 3.0 | Last Updated: 2026-02-10 | Uses MCP tools from "Retrieve" server*


