---
name: confluence-space-audit
description: "Audit a Confluence space for content quality, structure, and completeness."
---

# Confluence Space Audit

Audit a Confluence space and produce a structured quality report.

## Input

The user provides:
- A Confluence space key or URL
- Optional: specific focus areas (e.g. outdated pages, missing labels, orphan pages)

## Audit Steps

1. **Inventory** — List all pages in the space with their last-modified dates
2. **Structure** — Analyze the page hierarchy for depth, orphans, and navigation clarity
3. **Freshness** — Flag pages not updated in >6 months
4. **Labels** — Check for consistent labeling; identify unlabeled pages
5. **Quality** — Spot pages with very short content (<100 words) or placeholder text
6. **Duplicates** — Identify pages with very similar titles or content

## Output Format

```markdown
# Confluence Space Audit: [SPACE-KEY]

## Summary
- Total pages: X
- Outdated (>6 months): Y
- Unlabeled: Z
- Potential duplicates: N

## Findings

### Critical
- [Finding 1]

### Recommended
- [Finding 2]

### Nice to Have
- [Finding 3]

## Action Items
1. [Action 1]
2. [Action 2]
```

## Prerequisites

Requires a configured Confluence MCP server. See `.github/instructions/confluence-integration.instructions.md`.

