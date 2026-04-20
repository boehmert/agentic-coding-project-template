# Team- Stop Hook
# Zeigt Reminder für /save-session am Ende einer Agent-Session.
# stop_hook_active-Check verhindert Endlosschleife.
# Docs: https://code.visualstudio.com/docs/copilot/customization/hooks

$hookInput = $null
try {
    $raw = [Console]::In.ReadToEnd()
    if ($raw.Trim()) {
        $hookInput = $raw | ConvertFrom-Json
    }
} catch {}

# Kein Blocking wenn bereits in Stop-Hook-Loop
if ($hookInput -and $hookInput.stop_hook_active -eq $true) {
    Write-Output "{}"
    exit 0
}

$output = @{
    systemMessage = "Session beendet. Entstand domain-relevantes Wissen (Entscheidungen, Patterns, neue Erkenntnisse)? → /save-session aufrufen um active-context.md zu aktualisieren."
}

Write-Output ($output | ConvertTo-Json -Compress)

