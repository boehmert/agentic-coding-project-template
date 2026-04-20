"""Phase 3: Ingest reports, planning, cross-team, and prompts into Vault."""

import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[2]))

from _tools.vault.ingest_to_vault import process_file, WORKSPACE, VAULT_ROOT

PHASE3_FILES = [
    # (source_relative_path, kb_id, tags, strategic_intent, language)
    (
        "output/reports/Team-strategy-north-star-2026-03-10.md",
        "KB-202604150031",
        ["Team-/strategy", "Team-/PROJECT-", "Team-/mack", "Team-/libra", "Team-/evidence", "codegames2026", "status/draft"],
        "Team- Strategie-Nordstern: PROJECT- als Governor, 8 Deep Research Studien, Agentic SDLC Alignment.",
        "de",
    ),
    (
        "context/cross-team/GAMMA-Dossier.md",
        "KB-202604150032",
        ["Team-/gamma", "Team-/graphrag", "Team-/fab", "Team-/PROJECT-", "Team-/evaluation", "codegames2026", "status/draft"],
        "GAMMA GraphRAG Service: 3-Schichten-Modell, SAI-Metriken, LEX/Finance/Libra PoCs.",
        "de",
    ),
    (
        "context/cross-team/WK-Cross-Team-Knowledge_Graph-RAG-MCP.md",
        "KB-202604150033",
        ["Team-/mcp", "Team-/graphrag", "Team-/setup", "Team-/bitbucket", "status/draft"],
        "WK Cross-Team: MCP Server Setup, npm Registries (Artifactory/GitHub), MS Graph Scopes.",
        "en",
    ),
    (
        "context/cross-team/WK-Cross-Team-Knowledge_Integrations-Libra-Graph.md",
        "KB-202604150034",
        ["Team-/libra", "Team-/fab", "Team-/graph", "Team-/integrations", "Team-/allegro", "status/draft"],
        "WK Cross-Team: Libra Strategie, FAB RAGaaS, AllegroGraph, GRS OCL (11 Sections).",
        "en",
    ),
    (
        "output/prompts/PROJECT-ticket-analysis-setup-guide.md",
        "KB-202604150035",
        ["Team-/PROJECT-", "Team-/setup", "Team-/mcp", "Team-/jira", "Team-/team", "status/draft"],
        "PROJECT- Ticket Analysis Setup Guide: MCP, PATs, ODBC, Folder Structure fuer das Team.",
        "de",
    ),
    (
        "output/planning/runbook_PROJECT-pi_planning.md",
        "KB-202604150036",
        ["Team-/PROJECT-", "Team-/pi-planning", "Team-/runbook", "Team-/agile", "status/draft"],
        "PROJECT- PI Planning Runbook: 8 Milestone-Phasen, JQL-Templates, wiederverwendbar.",
        "de",
    ),
    (
        "output/planning/retro-fallstudien-2026.md",
        "KB-202604150037",
        ["Team-/retro", "Team-/ai-adoption", "Team-/team", "Team-/goal-1", "status/draft"],
        "Retro-Fallstudien 2026: Hands-On-Sessions, AI-Adoption-Evidenz fuer Goal 1.",
        "de",
    ),
    (
        "output/planning/runbook_pi17.md",
        "KB-202604150038",
        ["Team-/PROJECT-", "Team-/pi-planning", "Team-/pi17", "Team-/runbook", "status/draft"],
        "PI-17 spezifisches Runbook: Sprint-Filter, Miro-Board, konkrete Planungsdaten.",
        "de",
    ),
    (
        "output/planning/christian-gespr\u00e4ch-2026-03-13.md",
        "KB-202604150039",
        ["Team-/strategy", "Team-/PROJECT-", "Team-/positioning", "Team-/architecture", "status/draft"],
        "Strategisches Gespr\u00e4ch mit Architect: 5-Punkte-These zu strukturiertem Wissen + AI.",
        "de",
    ),
]


def main() -> None:
    before = len(list(VAULT_ROOT.glob("*.md")))
    print(f"Vault before: {before} files\n")

    for rel_path, kb_id, tags, intent, lang in PHASE3_FILES:
        src = WORKSPACE / rel_path
        if not src.exists():
            print(f"  MISSING: {rel_path}")
            continue
        process_file(src, kb_id, tags, intent, lang)

    after = len(list(VAULT_ROOT.glob("*.md")))
    print(f"\nVault after: {after} files (+{after - before} new)")


if __name__ == "__main__":
    main()


