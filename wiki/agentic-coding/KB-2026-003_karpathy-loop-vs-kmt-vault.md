---
id: KB-2026-003
title: "Karpathy LLM-Wiki Ansatz vs. Team- Vault – Architekturvergleich"
domain: agentic-coding
source_type: llm-generated
confidence: medium
created: 2026-04-13
created_by: copilot
session_context: "Session 2026-04-13: Karpathy X-Post (Anfang April 2026) analysiert und mit Team- Vault verglichen"
related_to: [KB-2026-001]
sources:
  - "Andrej Karpathy, X-Post April 2026 (LLM Knowledge Bases)"
  - "Team- Workspace Vault-MCP (vault-mcp Server)"
reviewed_by: null
status: draft
---

# Karpathy LLM-Wiki Ansatz vs. Team- Vault – Architekturvergleich

## Kernaussage

Karpathys LLM-Wiki und der Team- Obsidian Vault lösen dasselbe Problem (strukturiertes Wissenssystem für LLM-Nutzung), aber mit entgegengesetzten Prinzipien: LLM schreibt vs. Human schreibt. Der Knowledge Vault fehlt der kompoundierende Feedback-Loop.

## Details

### Karpathys Ansatz

```
raw/ (Papers, Artikel, Repos)
  ↓ LLM kompiliert
wiki/ (.md-Dateien, LLM-geschrieben)
  ↓ Q&A gegen Wiki
output (Slides, Grafiken, Markdown)
  ↓ zurück in Wiki ("file back")
wiki/ wächst durch Nutzung
```

**LLM ist Autor.** Human stellt Fragen und moderiert. Wiki akkumuliert automatisch.

### Team- Vault Ansatz

```
Author schreibt/kuratiert → Obsidian Vault
  ↓ vault-mcp MCP-Server (read-only)
Copilot Sessions lesen Vault
  ↓
output/ (isoliert, kein Rückfluss in Vault)
```

**Human ist Autor.** LLM ist Leser. Vault wächst nur durch manuelle Curation.

### Stärken/Schwächen im Vergleich

| Dimension | Karpathy | Team- Vault |
|---|---|---|
| Compounding Loop | ✅ Wiki wächst durch Nutzung | ❌ kein Rückschreibeweg |
| Skalierbarkeit | ✅ 100+ Dokumente auto-kompiliert | ❌ manuell, kapazitätsbegrenzt |
| Provenance | ❌ LLM-Authorship unklar | ✅ Author kuratiert, klare Verantwortung |
| Governance | ❌ keine | ✅ MCP-standardisiertes Interface |
| Tool-Qualität | ❌ "hackige Sammlung von Skripten" | ✅ standardisiertes MCP-Protokoll |
| Organisationales Wissen | ❌ Forschungs-Fokus | ✅ Prozesse, Konventionen, PROJECT/MACK |

### Der Karpathy-Loop für Team- (implementierter Ansatz)

Mit der wiki/-Erweiterung in diesem Workspace:

```
Session-Erkenntnisse
  ↓ /wiki-write
wiki/{domain}/KB-YYYY-NNN.md (LLM-geschrieben, mit Provenance)
  ↓ /wiki-lint (monatlich)
Wiki-Qualität steigt
  ↓ Zukunft: vault-sync?
Obsidian Vault (optional)
```

## Relevanz für Team-

Die `wiki/`-Schicht ist die fehlende Brücke: LLM-generiertes Wissen mit Provenance-Header, durchsuchbar, akkumulierend — aber nicht im Vault (der manuell bleibt). Trennung: Vault = stabile kuratierte Basis, wiki/ = wachsende LLM-Schicht.

**Schlüsselentscheidung (2026-04-13):** Provenance via YAML-Frontmatter (`source_type`, `confidence`, `reviewed_by`) sichert Qualität: `status: draft` bis Author prüft und `reviewed_by: Author` setzt.

## Quellen

- Andrej Karpathy, X-Post April 2026
- Team- Workspace: `.github/prompts/wiki-write.prompt.md`
- Team- Workspace: `wiki/_INDEX.md`


