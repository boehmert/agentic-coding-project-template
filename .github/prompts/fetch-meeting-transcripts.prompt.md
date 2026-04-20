---
name: fetch-meeting-transcripts
description: "Retrieve and process meeting transcripts from Microsoft Graph or local files."
---

# Fetch Meeting Transcripts

Retrieve meeting transcripts and convert them into structured summaries.

## Input

The user provides:
- A date range or specific meeting name
- Optional: output format preference (summary, action items only, full transcript)

## Steps

1. **Source identification**
   - If Microsoft Graph MCP is configured: search for meeting transcripts via Graph API
   - If local files: check `inbox/` for transcript files (.vtt, .txt, .docx)

2. **Processing**
   - Extract raw transcript text
   - Identify speakers and timestamps
   - Use `/meeting-summary` prompt for structured output

3. **Output**
   - Save structured summary to `output/meetings/`
   - Optionally create wiki snippet via `/wiki-write`

## Output Format

```markdown
# Meeting: [Title]
**Date:** [Date]
**Participants:** [Names]

## Key Decisions
1. [Decision]

## Action Items
- [ ] [Owner]: [Action] (Due: [Date])

## Discussion Summary
[Structured summary of main topics]
```

## Prerequisites

- For Graph API transcripts: Microsoft Graph MCP server configured
- For local files: transcript files in `inbox/` or specified path

