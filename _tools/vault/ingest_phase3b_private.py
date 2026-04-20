"""Phase 3b: Ingest sensitive/personal files into Vault private/ subfolders."""

import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[2]))

from pathlib import Path
from _tools.vault.ingest_to_vault import (
    build_frontmatter,
    extract_title,
    has_frontmatter,
    slugify,
    WORKSPACE,
    TODAY,
)

VAULT_PRIVATE = Path(
    r"C:\Users\user\OneDrive - your organization\Dokumente"
    r"\User\knowledge-base\Obsidian Vault\private"
)

# (source_relative_path, kb_id, subfolder, tags, strategic_intent, language)
PRIVATE_FILES = [
    (
        "governance/workday-goals-2026.md",
        "KB-202604150040",
        "goals",
        [
            "Team-/goals", "Team-/workday", "Team-/strategy", "Team-/2026",
            "sensitivity/career", "sensitivity/performance",
            "status/approved",
        ],
        "Workday Goals 2026 (genehmigte Version): 5 Jahresziele mit operativer Interpretation.",
        "en",
    ),
    (
        "output/planning/jahresziele-2026.md",
        "KB-202604150041",
        "goals",
        [
            "Team-/goals", "Team-/workday", "Team-/glsp", "Team-/2026",
            "sensitivity/career", "sensitivity/performance",
            "status/draft",
        ],
        "Jahresziele 2026 Entwurf v3: 4-Ziele-Struktur mit P4-Karrierekontext und GLSP-Mapping.",
        "de",
    ),
    (
        "output/planning/GLSP_Self-Assessment_IC_v2.md",
        "KB-202604150042",
        "goals",
        [
            "Team-/glsp", "Team-/self-assessment", "Team-/career-development",
            "sensitivity/career", "sensitivity/performance",
            "status/draft",
        ],
        "GLSP Self-Assessment v2: 4 Domaenen, Manager-Feedback, P3-to-P4 Entwicklungsplan.",
        "de",
    ),
    (
        "output/planning/jobsearch-strategy-2026.md",
        "KB-202604150043",
        "career",
        [
            "personal/jobsearch", "personal/career-strategy", "Team-/knowledge-engineer",
            "sensitivity/career", "sensitivity/jobsearch", "sensitivity/confidential",
            "status/draft",
        ],
        "Jobsuche-Strategie 2026: Positionierung, USP, Zielunternehmen, LinkedIn-Strategie.",
        "de",
    ),
]


def process_private_file(
    source_path: Path,
    kb_id: str,
    subfolder: str,
    tags: list[str],
    strategic_intent: str,
    language: str,
) -> Path:
    """Read source, prepend frontmatter with sensitivity tags, write to private vault."""
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
    vault_filename = f"PRIVATE_{kb_id}_{slug}.md"
    vault_path = VAULT_PRIVATE / subfolder / vault_filename

    if vault_path.exists():
        print(f"  SKIP (exists): {vault_filename}")
        return vault_path

    vault_path.write_text(frontmatter + content, encoding="utf-8")
    print(f"  OK: {subfolder}/{vault_filename}")
    return vault_path


def main() -> None:
    total_before = sum(
        len(list((VAULT_PRIVATE / d).glob("*.md")))
        for d in ["goals", "career", "health", "finance"]
        if (VAULT_PRIVATE / d).exists()
    )
    print(f"Private vault before: {total_before} files\n")

    for rel_path, kb_id, subfolder, tags, intent, lang in PRIVATE_FILES:
        src = WORKSPACE / rel_path
        if not src.exists():
            print(f"  MISSING: {rel_path}")
            continue
        process_private_file(src, kb_id, subfolder, tags, intent, lang)

    total_after = sum(
        len(list((VAULT_PRIVATE / d).glob("*.md")))
        for d in ["goals", "career", "health", "finance"]
        if (VAULT_PRIVATE / d).exists()
    )
    print(f"\nPrivate vault after: {total_after} files (+{total_after - total_before} new)")

    # Show structure
    print("\nStructure:")
    for d in ["goals", "career", "health", "finance"]:
        p = VAULT_PRIVATE / d
        if p.exists():
            files = list(p.glob("*.md"))
            print(f"  {d}/: {len(files)} files")
            for f in sorted(files):
                print(f"    - {f.name}")


if __name__ == "__main__":
    main()


