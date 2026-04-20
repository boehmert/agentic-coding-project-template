# Team- SessionStart Hook
# Injiziert Team-Workspace-Kontext am Beginn jeder Agent-Session.
# Docs: https://code.visualstudio.com/docs/copilot/customization/hooks

$additionalContext = @"
Team-Workspace Kontext (auto-injiziert):
- Befehle: /start {task}, /save-session, /remember, /wiki-write, /wiki-lint, /wiki-ingest
- Wissensbasis-Reihenfolge: vault_search → wiki/ (grep_search) → context/ → Confluence → Jira
- MCP sofort nutzbar: wk-jira, wk-confluence, vault-mcp, microsoft-graph
- Active Context: /memories/repo/active-context.md (via Memory-Tool lesen)
- NICHT ausführen: /init (würde copilot-instructions.md überschreiben)
- Ausgaben: output/ | Eingaben: inbox/ | Scripts: tasks/ | Libs: _tools/
"@

$output = [ordered]@{
    hookSpecificOutput = [ordered]@{
        hookEventName   = "SessionStart"
        additionalContext = $additionalContext.Trim()
    }
}

Write-Output ($output | ConvertTo-Json -Depth 5 -Compress)

