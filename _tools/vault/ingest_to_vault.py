"""Ingest workspace Markdown files into the Obsidian Vault with KB frontmatter."""

import re
import shutil
from datetime import datetime
from pathlib import Path

# Configure these paths for your environment:
# VAULT_ROOT: Where to write the processed KB files (your Obsidian vault)
# WORKSPACE:  Root of this repository on your machine
VAULT_ROOT = Path.home() / "vault" / "curated"  # adapt to your vault path
WORKSPACE = Path(__file__).resolve().parents[2]

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
target_index: curated

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
# Replace these with your own file lists.
# Format: (filename, tags, strategic_intent, language)

EXAMPLE_SOURCE_DIR = WORKSPACE / "inbox" / "example"

EXAMPLE_FILES = [
    # Add your own files here. Each entry is a tuple:
    # (filename, tags, strategic_intent, language)
    # Example:
    # (
    #     "my-research-notes.md",
    #     ["domain/research", "topic/ai", "status/draft"],
    #     "Summary of research on AI agents and retrieval patterns.",
    #     "en",
    # ),
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

    print("=== Example Files ===")
    for filename, tags, intent, lang in EXAMPLE_FILES:
        source = EXAMPLE_SOURCE_DIR / filename
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
