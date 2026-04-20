# Workspace SessionStart Hook
# Injects workspace context at the beginning of each agent session.
# Docs: https://code.visualstudio.com/docs/copilot/customization/hooks

$additionalContext = @"
Workspace Context (auto-injected):
- Commands: /start {task}, /save-session, /remember, /wiki-write, /wiki-lint, /wiki-ingest
- Knowledge order: vault_search → wiki/ (grep_search) → context/ → Confluence → Jira
- MCP available: your-jira, your-confluence, vault-mcp (configure in .vscode/mcp.json)
- Active Context: /memories/repo/active-context.md (read via Memory tool)
- DO NOT run: /init (would overwrite copilot-instructions.md)
- Outputs: output/ | Inputs: inbox/ | Scripts: tasks/ | Libs: _tools/
"@

$output = [ordered]@{
    hookSpecificOutput = [ordered]@{
        hookEventName   = "SessionStart"
        additionalContext = $additionalContext.Trim()
    }
}

Write-Output ($output | ConvertTo-Json -Depth 5 -Compress)

