"""Ingest workspace Markdown files into the Obsidian Vault with KB frontmatter."""

import re
import shutil
from datetime import datetime
from pathlib import Path

VAULT_ROOT = Path(
    r"C:\Users\user\OneDrive - your organization\Dokumente"
    r"\User\knowledge-base\Obsidian Vault\curated"
)
WORKSPACE = Path(
    r"C:\Users\user\OneDrive - your organization\Dokumente"
    r"\My-Team-Workspace"
)

TODAY = datetime.now().strftime("%Y-%m-%d")
TIMESTAMP_BASE = "202604150"  # KB-ID prefix for this batch


def slugify(text: str, max_len: int = 60) -> str:
    """Create a filesystem-safe slug from a title."""
    slug = re.sub(r"[^\w\s-]", "", text)
    slug = re.sub(r"[\s_]+", "-", slug).strip("-")
    return slug[:max_len]


def has_frontmatter(content: str) -> bool:
    """Check if content already starts with YAML frontmatter."""
    return content.strip().startswith("---")


def extract_title(content: str, filename: str) -> str:
    """Extract first heading or use filename as title."""
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line.lstrip("# ").strip()
    return Path(filename).stem.replace("-", " ").replace("_", " ")


def build_frontmatter(
    kb_id: str,
    title: str,
    tags: list[str],
    source_path: str,
    strategic_intent: str,
    language: str = "en",
) -> str:
    """Build Vault-compatible YAML frontmatter."""
    tags_str = ", ".join(f'"{t}"' for t in tags)
    return f"""---
id: {kb_id}
title: "{title}"
document_type: Knowledge Distillate
target_index: Team-Expert_curated

# --- Taxonomy & Connectivity ---
tags: [{tags_str}]
aliases: []
up: "[[MOC_Start]]"
predecessor: []
successor: []
related: []

# --- Provenance & Traceability ---
framework_version: 1.2.0
created_by: "User Name"
created_at: "{TODAY}"
source_origin: "{source_path}"
strategic_intent: "{strategic_intent}"
language: "{language}"

# --- Cognitive Layer ---
cognitive_intent: "KB-Dokument aus Workspace-Quelle destilliert für Vault-Retrieval."
transfer_score: 8

# --- Quality ---
quality_status: Draft
confidence: 7
---

"""


# ── File definitions ─────────────────────────────────────────────────────────

CODEGAMES_DIR = WORKSPACE / "inbox" / "CodeGames2026"
Team-META_DIR = WORKSPACE / "context" / "PROJECT-"

# (filename, tags, strategic_intent, language)
CODEGAMES_FILES = [
    (
        "Agentic AI and Legal Ontologies.md",
        ["Team-/research", "Team-/agentic-ai", "Team-/ontology", "Team-/PROJECT-", "codegames2026", "status/draft"],
        "Deep Research: Transformation der Wissensmodellierung — vom semantischen Architekten zum agentischen Gouverneur.",
        "de",
    ),
    (
        "CodeGames2026-FAQ.txt",
        ["Team-/codegames", "codegames2026", "Team-/event", "status/draft"],
        "Offizielles FAQ und Regelwerk des WK CodeGames 2026 Hackathons (Agentic Edition).",
        "en",
    ),
    (
        "Competitor Analysis_ Legal AI & Ontologies.md",
        ["Team-/research", "Team-/competitive-analysis", "Team-/legal-ai", "Team-/ontology", "codegames2026", "status/draft"],
        "Strategische Wettbewerbsanalyse: Legal AI Marktpositionierung und Ontologie-basierte Differenzierung.",
        "en",
    ),
    (
        "Curated Knowledge Models and Semantic Content Infrastructure in Enterprise AI Transformation (Deep Research Results).md",
        ["Team-/research", "Team-/knowledge-models", "Team-/rag", "Team-/semantic-infrastructure", "codegames2026", "status/draft"],
        "Evidenzbasierte Analyse: Warum kuratierte Knowledge Models RAG-Qualität in Enterprises verbessern.",
        "en",
    ),
    (
        "deep-research-report_Chunking-Strategien für komplexe Rechtsdokumente.md",
        ["Team-/research", "Team-/rag", "Team-/chunking", "Team-/legal-content", "codegames2026", "status/draft"],
        "Chunking-Strategien für komplexe Rechtsdokumente: hierarchisch, semantisch, ontologiegesteuert.",
        "de",
    ),
    (
        "deep-research-report_Einsatz von Ontologien und Wissensgraphen zur Validierung von LLM-Ausgaben in Hochrisikodomänen.md",
        ["Team-/research", "Team-/ontology", "Team-/knowledge-graph", "Team-/llm-validation", "Team-/shacl", "codegames2026", "status/draft"],
        "Ontologie-basierte LLM-Validierung: OG-RAG und SHACL-Constraints reduzieren Halluzinationen um 40-58%.",
        "de",
    ),
    (
        "deep-research-report_Ontologie-Lernen aus Such- und Query-Logs.md",
        ["Team-/research", "Team-/ontology", "Team-/query-logs", "Team-/rag", "codegames2026", "status/draft"],
        "Automatische Ontologie-Erweiterung aus Query-Logs und RAG-Fehleranalyse.",
        "de",
    ),
    (
        "deep-research-report_Stand der Technik zeitabhängiger RAG-Ansätze im Rechtsbereich.md",
        ["Team-/research", "Team-/rag", "Team-/temporal", "Team-/legal-content", "Team-/graphrag", "codegames2026", "status/draft"],
        "Temporal RAG: Zeitabhängige Retrieval-Ansätze für Rechtsänderungen und Stichtagsabfragen.",
        "de",
    ),
    (
        "deep-research-report_Symbolische Verankerung von LLM-Antworten im juristischen Bereich.md",
        ["Team-/research", "Team-/neuro-symbolic", "Team-/shacl", "Team-/PROJECT-", "Team-/legal-content", "codegames2026", "status/draft"],
        "Neuro-symbolische Verankerung juristischer LLM-Antworten über PROJECT-Ontologie und SHACL.",
        "de",
    ),
    (
        "Do Structured Knowledge Layers Improve Deep Research Results.md",
        ["Team-/research", "Team-/knowledge-graph", "Team-/rag", "Team-/benchmarks", "codegames2026", "status/draft"],
        "Meta-Analyse: Strukturierte Wissensschichten verbessern Multi-Hop-Reasoning um 27-40%.",
        "en",
    ),
    (
        "Governance for AI-Augmented Knowledge Management deep-research-report.md",
        ["Team-/research", "Team-/governance", "Team-/knowledge-management", "Team-/shacl", "codegames2026", "status/draft"],
        "Governance-Framework für AI-unterstütztes Wissensmanagement: SHACL, PROV-O, Human-in-the-Loop.",
        "en",
    ),
    (
        "Governance-Modelle für KI-gestützte Wissensplattformen deep-research-report.md",
        ["Team-/research", "Team-/governance", "Team-/ai-platforms", "codegames2026", "status/draft"],
        "Governance-Modelle für KI-gestützte Wissensplattformen: Rollen, Fehlermuster, Entscheidungsrahmen.",
        "de",
    ),
    (
        "Intent-getriebene Inhaltsqualität für KI-Pipelines deep-research-report.md",
        ["Team-/research", "Team-/content-quality", "Team-/shacl", "Team-/ai-pipelines", "codegames2026", "status/draft"],
        "Intent-basierte Quality Gates mit SHACL, JSON Schema und Controlled Vocabularies für AI-Pipelines.",
        "de",
    ),
    (
        "Knowledge Engineers as Specification Authors in Agentic AI Workflows deep-research-report.md",
        ["Team-/research", "Team-/knowledge-engineering", "Team-/agentic-ai", "Team-/spec-driven", "codegames2026", "status/draft"],
        "Evolution der Knowledge-Engineer-Rolle: Spec-Driven Development für Agentic AI Workflows.",
        "en",
    ),
    (
        "Legal Tech Hackathon_ Agentic AI Research.md",
        ["Team-/research", "Team-/legal-tech", "Team-/agentic-ai", "Team-/hackathon", "codegames2026", "status/draft"],
        "Legal-Tech-Disruption 2024-2026: Agentic AI, PROJECT- als neuro-symbolische Architektur, Hackathon-Chancen.",
        "de",
    ),
    (
        "Neuro-Symbolic AI in Legal Content.md",
        ["Team-/research", "Team-/neuro-symbolic", "Team-/legal-content", "Team-/knowledge-graph", "codegames2026", "status/draft"],
        "Neuro-symbolische Synthese: LLMs + Ontologien + SHACL für vertrauenswürdige juristische Wissensarchitekturen.",
        "en",
    ),
    (
        "SHACL for Legal Rules Research.md",
        ["Team-/research", "Team-/shacl", "Team-/legal-rules", "Team-/rdf", "codegames2026", "status/draft"],
        "SHACL 1.2 Deep Dive: Constraint-Typen, SHACL Rules, temporale Modellierung, Integration mit Akoma Ntoso.",
        "en",
    ),
    (
        "The Evolving Knowledge Engineer - Deep Research Result.md",
        ["Team-/research", "Team-/knowledge-engineering", "Team-/career", "Team-/agentic-ai", "codegames2026", "status/draft"],
        "Evolution der KE/KM-Rollen in Agentic AI: Semantic Modeling + Prompt Engineering + Governance.",
        "en",
    ),
    (
        "The Long-Tail Quality Ceiling of Enterprise - Deep Research Result.md",
        ["Team-/research", "Team-/rag", "Team-/enterprise", "Team-/quality", "codegames2026", "status/draft"],
        "Enterprise RAG Quality Ceiling: Warum 95% der Piloten scheitern und Metadata-Enrichment hilft.",
        "en",
    ),
    (
        "Transforming Enterprise Knowledge Base - Deep Research Result.md",
        ["Team-/research", "Team-/data-transformation", "Team-/rag", "Team-/enterprise", "codegames2026", "status/draft"],
        "Praxisleitfaden: Enterprise Knowledge Bases (Confluence/SharePoint/Excel) für RAG-Pipelines transformieren.",
        "en",
    ),
    (
        "your organization AI Legal Research Analysis.md",
        ["Team-/research", "Team-/your-org", "Team-/legal-ai", "Team-/fab", "Team-/graphrag", "codegames2026", "status/draft"],
        "Technische Analyse: WK FAB-Plattform, Libra Legal AI, VitalLaw Expert AI — GraphRAG + Agentic Architecture.",
        "en",
    ),
]

Team-META_FILES = [
    (
        "Team-Meta-01_PROJECT-Platform.md",
        ["Team-/PROJECT-", "Team-/platform", "Team-/metadata", "Team-/shacl", "Team-/governance", "status/draft"],
        "PROJECT-Plattform: Governance, Validierungsinfrastruktur (334 SHACL Shapes), Datenmodell-Referenz.",
        "de",
    ),
    (
        "Team-Meta-02_Data-Pipeline-Pipeline.md",
        ["Team-/mack", "Team-/Data-Pipeline", "Team-/transformation", "Team-/ai-pipeline", "status/draft"],
        "Data-Pipeline Transformations-Pipeline: AI-gestützte Konversion heterogener XML-Quellen zu MACK.",
        "en",
    ),
    (
        "Team-Meta-03_AI-Agent-Systems.md",
        ["Team-/ai-agents", "Team-/agentic-ai", "Team-/fab", "Team-/strategy", "status/draft"],
        "WK AI & Agent-Systeme: Strategische Vision, FAB-Plattform, agentic engineering approach.",
        "en",
    ),
    (
        "Team-Meta-04_QA-Testing.md",
        ["Team-/qa", "Team-/testing", "Team-/shacl", "Team-/goldset", "status/draft"],
        "QA & Testing Framework: Multi-Layer-Validierung, Goldset-basierte Ground Truth, Pipeline-Qualität.",
        "de",
    ),
    (
        "Team-Meta-05_Team-Processes.md",
        ["Team-/team", "Team-/processes", "Team-/agile", "Team-/jira", "status/draft"],
        "Team- Team-Prozesse: Agile Workflows, Jira-Administration, Templates, Projektmanagement-Infrastruktur.",
        "de",
    ),
    (
        "Team-Meta-06_Architecture-Decisions.md",
        ["Team-/architecture", "Team-/decisions", "Team-/PROJECT-", "Team-/mack", "status/draft"],
        "Architektur-Entscheidungen: Synthese aus 40+ Architecture-Call-Protokollen (Jan 2025 – Feb 2026).",
        "de",
    ),
]


def process_file(
    source_path: Path,
    kb_id: str,
    tags: list[str],
    strategic_intent: str,
    language: str,
) -> Path:
    """Read source, prepend frontmatter, write to vault."""
    content = source_path.read_text(encoding="utf-8")
    title = extract_title(content, source_path.name)

    # Strip existing frontmatter if present
    if has_frontmatter(content):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            content = parts[2].lstrip("\n")

    frontmatter = build_frontmatter(
        kb_id=kb_id,
        title=title,
        tags=tags,
        source_path=str(source_path.relative_to(WORKSPACE)),
        strategic_intent=strategic_intent,
        language=language,
    )

    slug = slugify(title)
    vault_filename = f"{kb_id}_{slug}.md"
    vault_path = VAULT_ROOT / vault_filename

    if vault_path.exists():
        print(f"  SKIP (exists): {vault_filename}")
        return vault_path

    vault_path.write_text(frontmatter + content, encoding="utf-8")
    print(f"  OK: {vault_filename}")
    return vault_path


def main() -> None:
    """Ingest all configured files into the Vault."""
    print(f"Vault root: {VAULT_ROOT}")
    print(f"Workspace:  {WORKSPACE}\n")

    counter = 1

    print("=== CodeGames2026 Deep Research ===")
    for filename, tags, intent, lang in CODEGAMES_FILES:
        source = CODEGAMES_DIR / filename
        # Handle .txt extension
        if not source.exists() and source.with_suffix(".txt").exists():
            source = source.with_suffix(".txt")
        if not source.exists():
            print(f"  MISSING: {filename}")
            continue
        kb_id = f"KB-{TIMESTAMP_BASE}{counter:03d}"
        process_file(source, kb_id, tags, intent, lang)
        counter += 1

    print("\n=== Team-Meta Documents ===")
    for filename, tags, intent, lang in Team-META_FILES:
        source = Team-META_DIR / filename
        if not source.exists():
            print(f"  MISSING: {filename}")
            continue
        kb_id = f"KB-{TIMESTAMP_BASE}{counter:03d}"
        process_file(source, kb_id, tags, intent, lang)
        counter += 1

    after = len(list(VAULT_ROOT.glob("*.md")))
    print(f"\nDone. Vault now has {after} files.")


if __name__ == "__main__":
    main()



