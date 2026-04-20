#!/usr/bin/env python3
"""
Universal Document → Markdown Converter
========================================
Converts a wide range of document formats to LLM-readable Markdown.

Supported formats (detected by content signature, not solely by extension):

  .docx         – Word Open XML (via python-docx, delegates to doc_processor.py)
  .doc          – Legacy Word binary OR Word-HTML (detected automatically)
                  • Word-HTML (common Jira/Confluence export): parsed via BeautifulSoup
                  • OLE2 binary (.doc): requires pandoc or Win32 Word (see notes below)
  .pdf          – PDF (via pypdf, delegates to doc_processor.py)
  .pptx         – PowerPoint (via python-pptx)
  .xlsx / .xls  – Excel (via openpyxl)
  .html / .htm  – HTML (via BeautifulSoup)
  .txt / .md    – Plain text / Markdown (pass-through copy)

Format Detection
----------------
Files are identified by their first bytes (magic bytes), not their extension.
This correctly handles .doc files that are actually HTML or ZIP/OOXML.

  50 4B ...       → ZIP / OOXML  → treat as .docx
  D0 CF 11 E0 ... → OLE2 binary  → true .doc (needs pandoc)
  3C 21 44 4F ... → <!DO...      → Word-HTML (common in Jira exports)
  3C 68 74 6D ... → <htm...      → HTML
  25 50 44 46 ... → %PDF         → PDF

Usage
-----
    from _tools.documents.converter import to_markdown, convert_directory
    from pathlib import Path

    out = to_markdown(Path("inbox/jira/TICKET-1280.doc"), Path("output/context"))
    print(f"Written: {out}")

    convert_directory(Path("inbox/jira"), Path("output/context"))
"""

import re
import html as html_module
from pathlib import Path
from typing import Callable


# ── Constants ─────────────────────────────────────────────────────────────────

_EXT_PPTX = ".pptx"
_EXT_XLSX = ".xlsx"

# ── Magic bytes → format detection ───────────────────────────────────────────

_MAGIC = {
    b"\x50\x4B":             "zip_ooxml",   # ZIP → DOCX/PPTX/XLSX
    b"\xD0\xCF\x11\xE0":    "ole2",         # OLE2 compound document
    b"\x25\x50\x44\x46":    "pdf",          # %PDF
}

# HTML variants (<!D, <htm, <?xm, <HTM, <!-)
_HTML_STARTS = [b"<!D", b"<HT", b"<ht", b"<?x", b"<!-", b"\xEF\xBB\xBF<"]  # last = UTF-8 BOM + <


def _detect_format(path: Path) -> str:
    """
    Detect the actual file format by reading the first bytes.

    Returns one of: 'docx', 'ole2_doc', 'word_html', 'html', 'pdf',
                    'pptx', 'xlsx', 'txt'
    """
    raw = path.read_bytes()[:16]

    # ZIP-based formats: look at the content-type inside the ZIP
    if raw[:2] == b"PK":
        suffix = path.suffix.lower()
        if suffix in (_EXT_PPTX,):
            return "pptx"
        if suffix in (_EXT_XLSX, ".xls"):
            return "xlsx"
        return "docx"  # assume Word if unknown zip

    # OLE2 compound document
    if raw[:4] == b"\xD0\xCF\x11\xE0":
        return "ole2_doc"

    # PDF
    if raw[:4] == b"%PDF":
        return "pdf"

    # HTML variants (including Word-HTML .doc files)
    for start in _HTML_STARTS:
        if raw[:len(start)] == start:
            # Distinguish Word-HTML from plain HTML by MIME hint in first KB
            chunk = path.read_bytes()[:1024]
            if b"vnd.ms-word" in chunk or b"mso-" in chunk or b"mso_" in chunk:
                return "word_html"
            return "html"

    # Fallback: trust the extension
    ext = path.suffix.lower()
    ext_map = {".docx": "docx", ".pdf": "pdf", _EXT_PPTX: "pptx",
               _EXT_XLSX: "xlsx", ".xls": "xlsx", ".htm": "html", ".html": "html",
               ".md": "txt", ".txt": "txt"}
    return ext_map.get(ext, "txt")


# ── HTML / Word-HTML → Markdown ───────────────────────────────────────────────

def _html_cell_text(cell) -> str:
    """Extract clean text from an HTML table cell."""
    return cell.get_text(separator=" ", strip=True).replace("\n", " ")


def _html_fmt_row(cells: list[str]) -> str:
    """Format a list of cell texts as a Markdown table row."""
    return "| " + " | ".join(cells) + " |"


def _html_dedup_row(row: list[str]) -> list[str]:
    """Remove duplicate adjacent cell texts caused by merged cells in HTML tables."""
    clean: list[str] = []
    prev = object()
    for cell in row:
        clean.append(cell if cell != prev else "")
        prev = cell
    return clean


def _html_kv_to_md(rows: list[list[str]]) -> str:
    """Render a 2-column HTML table as a key/value definition list."""
    lines = []
    for row in rows:
        padded_row = (row + ["", ""])[:2]
        key, val = padded_row[0], padded_row[1]
        if key and val:
            lines.append(f"**{key}:** {val}")
        elif key:
            lines.append(f"**{key}**")
        elif val:
            lines.append(val)
    return "\n\n".join(lines)


def _html_table_to_md(table) -> str:
    """Convert an HTML table to Markdown (definition list or full table)."""
    rows = []
    for tr in table.find_all("tr"):
        cells = [_html_cell_text(td) for td in tr.find_all(["td", "th"])]
        rows.append(cells)
    if not rows:
        return ""

    deduped = [_html_dedup_row(row) for row in rows]
    num_cols = max(len(r) for r in deduped)

    if num_cols == 2:
        return _html_kv_to_md(deduped)

    # General → Markdown table
    padded = [(r + [""] * num_cols)[:num_cols] for r in deduped]
    header    = padded[0]
    separator = [":---"] * num_cols
    body      = padded[1:]

    return "\n".join(
        [_html_fmt_row(header), _html_fmt_row(separator)]
        + [_html_fmt_row(r) for r in body]
    )


def _html_list_to_md(tag, ordered: bool = False, depth: int = 0) -> str:
    """Convert an HTML ul/ol to Markdown with nested list support."""
    lines = []
    indent = "  " * depth
    idx = 1
    for child in tag.children:
        if hasattr(child, "name") and child.name == "li":
            nested = ""
            for sub in child.children:
                if hasattr(sub, "name") and sub.name in ("ul", "ol"):
                    nested = "\n" + _html_list_to_md(
                        sub, ordered=(sub.name == "ol"), depth=depth + 1
                    )
                    sub.decompose()
            text = child.get_text(separator=" ", strip=True)
            bullet = f"{idx}." if ordered else "-"
            lines.append(f"{indent}{bullet} {text}{nested}")
            idx += 1
    return "\n".join(lines)


_BLOCK_TAGS = frozenset({
    "div", "section", "article", "main", "body", "html",
    "blockquote", "td", "th", "li",
})


def _html_inline_tag(node, wrapper: str) -> str:
    """Wrap a node's text content in Markdown inline formatting."""
    text = node.get_text(separator=" ", strip=True)
    return f"{wrapper}{text}{wrapper}" if text else ""


def _html_link_to_md(node) -> str:
    """Convert an HTML anchor to a Markdown link."""
    text = node.get_text(separator=" ", strip=True)
    href = node.get("href", "")
    return f"[{text}]({href})" if href else text


def _html_heading_to_md(node) -> str:
    """Convert an HTML heading to Markdown."""
    level = int(node.name[1])
    text = node.get_text(separator=" ", strip=True)
    return "#" * level + " " + text + "\n\n"


_HEADING_TAGS = frozenset({"h1", "h2", "h3", "h4", "h5", "h6"})


def _html_node_to_md(node, depth: int = 0) -> str:
    """Recursively convert a BeautifulSoup node to Markdown."""
    from bs4 import NavigableString

    if isinstance(node, NavigableString):
        return ""

    tag = node.name
    if not tag:
        return ""

    # Compound tags with special rendering
    if tag == "table":
        return _html_table_to_md(node) + "\n\n"
    if tag == "ul":
        return _html_list_to_md(node, ordered=False) + "\n\n"
    if tag == "ol":
        return _html_list_to_md(node, ordered=True) + "\n\n"
    if tag in _HEADING_TAGS:
        return _html_heading_to_md(node)

    # Paragraph
    if tag == "p":
        text = node.get_text(separator=" ", strip=True)
        return (text + "\n\n") if text else ""

    # Block-level structural tags — recurse into children
    if tag in _BLOCK_TAGS:
        return "".join(_html_node_to_md(child, depth) for child in node.children)

    # Simple tag → Markdown mappings
    simple: dict[str, str] = {
        "code": f"`{node.get_text()}`",
        "pre":  f"\n```\n{node.get_text()}\n```\n\n",
        "hr":   "\n---\n\n",
        "br":   "\n",
    }
    if tag in simple:
        return simple[tag]

    # Inline formatting
    if tag in ("b", "strong"):
        return _html_inline_tag(node, "**")
    if tag in ("i", "em"):
        return _html_inline_tag(node, "_")
    if tag == "a":
        return _html_link_to_md(node)

    # Default: recurse
    return "".join(_html_node_to_md(child, depth) for child in node.children)


def _html_to_markdown(html_content: str) -> str:
    """
    Convert an HTML string to Markdown using BeautifulSoup.

    Handles: headings, paragraphs, bold/italic, links, unordered/ordered
    lists, tables (2-col definition list or full MD table), code blocks.
    """
    try:
        from bs4 import BeautifulSoup
    except ImportError:
        raise ImportError("beautifulsoup4 is not installed. Run: pip install beautifulsoup4")

    soup = BeautifulSoup(html_content, "lxml")

    for tag in soup.find_all(["script", "style", "meta", "link", "head"]):
        tag.decompose()

    title = ""
    if soup.title and soup.title.string:
        title = soup.title.string.strip()
        title = re.sub(r"^\[#[A-Z]+-\d+\]\s*", "", title)

    body = soup.find("body") or soup
    md = _html_node_to_md(body)
    md = re.sub(r"\n{3,}", "\n\n", md).strip()

    return (f"# {title}\n\n" + md) if title else md


def _word_html_to_markdown(path: Path) -> str:
    """Read a Word-HTML .doc file and convert to Markdown."""
    # Detect encoding from BOM or charset meta
    raw = path.read_bytes()
    encoding = "utf-8"
    if raw[:3] == b"\xEF\xBB\xBF":
        encoding = "utf-8-sig"
        raw = raw[3:]
    elif raw[:2] in (b"\xFF\xFE", b"\xFE\xFF"):
        encoding = "utf-16"

    try:
        content = raw.decode(encoding)
    except UnicodeDecodeError:
        # Fallback to latin-1 (always succeeds)
        content = raw.decode("latin-1")

    return _html_to_markdown(content)


# ── PPTX → Markdown ──────────────────────────────────────────────────────────

_PPTX_TITLE_SHAPE_TYPE = 13


def _extract_slide_content(slide) -> tuple[str, list[str]]:
    """Extract title and body texts from a single PPTX slide."""
    title_text = ""
    body_texts: list[str] = []

    for shape in slide.shapes:
        if not shape.has_text_frame:
            continue
        full = "\n".join(
            para.text for para in shape.text_frame.paragraphs
            if para.text.strip()
        )
        if not full.strip():
            continue
        if shape.shape_type == _PPTX_TITLE_SHAPE_TYPE:
            title_text = full.strip()
        elif title_text == "" and not body_texts:
            title_text = full.strip()
        else:
            body_texts.append(full)

    return title_text, body_texts


def _pptx_to_markdown(path: Path) -> str:
    """Extract text from a PowerPoint file, slide by slide."""
    try:
        from pptx import Presentation
    except ImportError:
        raise ImportError("python-pptx is not installed. Run: pip install python-pptx")

    prs = Presentation(path)
    blocks = [f"# {path.stem}\n"]

    for i, slide in enumerate(prs.slides, 1):
        title_text, body_texts = _extract_slide_content(slide)

        slide_header = f"## Slide {i}: {title_text}" if title_text else f"## Slide {i}"
        blocks.append(slide_header)
        if body_texts:
            blocks.append("\n".join(body_texts))

    return "\n\n".join(blocks)


# ── XLSX → Markdown ───────────────────────────────────────────────────────────

def _xlsx_to_markdown(path: Path) -> str:
    """Convert the first N rows of each sheet to a Markdown table."""
    try:
        import openpyxl
    except ImportError:
        raise ImportError("openpyxl is not installed. Run: pip install openpyxl")

    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    blocks = [f"# {path.stem}\n"]
    MAX_ROWS = 200

    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        rows = []
        for row in ws.iter_rows(max_row=MAX_ROWS, values_only=True):
            cells = [str(c) if c is not None else "" for c in row]
            if any(cells):
                rows.append(cells)
        if not rows:
            continue

        blocks.append(f"## Sheet: {sheet_name}")
        num_cols = max(len(r) for r in rows)
        padded = [(r + [""] * num_cols)[:num_cols] for r in rows]
        header = padded[0]
        sep    = [":---"] * num_cols
        body   = padded[1:]

        lines = ["| " + " | ".join(header) + " |",
                 "| " + " | ".join(sep)    + " |"]
        for row in body:
            lines.append("| " + " | ".join(row) + " |")
        blocks.append("\n".join(lines))

    return "\n\n".join(blocks)


# ── Format-specific converters for to_markdown dispatch ───────────────────────

def _convert_word_html(file_path: Path, out_file: Path, **_) -> Path:
    md = _word_html_to_markdown(file_path)
    out_file.write_text(md, encoding="utf-8")
    return out_file


def _convert_html(file_path: Path, out_file: Path, **_) -> Path:
    raw = file_path.read_bytes()
    content = raw.decode("latin-1")  # fallback that always succeeds
    for enc in ("utf-8-sig", "utf-8"):
        try:
            content = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    md = _html_to_markdown(content)
    out_file.write_text(md, encoding="utf-8")
    return out_file


def _convert_pptx(file_path: Path, out_file: Path, **_) -> Path:
    md = _pptx_to_markdown(file_path)
    out_file.write_text(md, encoding="utf-8")
    return out_file


def _convert_xlsx(file_path: Path, out_file: Path, **_) -> Path:
    md = _xlsx_to_markdown(file_path)
    out_file.write_text(md, encoding="utf-8")
    return out_file


def _convert_txt(file_path: Path, out_file: Path, output_dir: Path, **_) -> Path:
    import shutil
    shutil.copy2(file_path, output_dir / file_path.name)
    return output_dir / file_path.name


# ── Unified entry point ───────────────────────────────────────────────────────

def to_markdown(
    file_path: Path,
    output_dir: Path | None = None,
    *,
    overwrite: bool = True,
) -> Path:
    """
    Convert any supported document to a Markdown file.

    Args:
        file_path:  Path to the source document.
        output_dir: Directory for the output .md file.
                    Defaults to output/context/ relative to the workspace root.
        overwrite:  If False, skip files that already have a .md counterpart.

    Returns:
        Path to the written Markdown file.

    Raises:
        ValueError: If the format is not supported or conversion fails.
    """
    from _tools.documents.doc_processor import docx_to_markdown, pdf_to_markdown

    file_path  = Path(file_path)
    output_dir = Path(output_dir) if output_dir else Path("output/context")
    output_dir.mkdir(parents=True, exist_ok=True)

    stem = file_path.stem
    if stem.lower().endswith(".doc"):
        stem = stem[:-4]
    out_file = output_dir / (stem + ".md")

    if not overwrite and out_file.exists():
        return out_file

    fmt = _detect_format(file_path)

    # Dispatch table: format → handler
    dispatch: dict[str, Callable] = {
        "word_html": _convert_word_html,
        "html":      _convert_html,
        "docx":      lambda fp, of, **_: docx_to_markdown(fp, output_dir),
        "pdf":       lambda fp, of, **_: pdf_to_markdown(fp, output_dir),
        "pptx":      _convert_pptx,
        "xlsx":      _convert_xlsx,
        "txt":       _convert_txt,
    }

    handler = dispatch.get(fmt)
    if handler:
        out_file = handler(file_path, out_file, output_dir=output_dir)
    elif fmt == "ole2_doc":
        raise ValueError(
            f"'{file_path.name}' is a true binary OLE2 .doc file. "
            "Conversion requires either:\n"
            "  1. Install pandoc (https://pandoc.org) → pip install pypandoc\n"
            "  2. Install pywin32 and use Microsoft Word via COM automation\n"
            "  3. Manually save as .docx in Word, then re-run."
        )
    else:
        raise ValueError(f"Unsupported format '{fmt}' for file: {file_path.name}")

    return out_file


# ── Batch conversion ──────────────────────────────────────────────────────────

SUPPORTED_EXTENSIONS = {".doc", ".docx", ".pdf", _EXT_PPTX, _EXT_XLSX, ".xls",
                        ".html", ".htm", ".txt", ".md"}


def _is_convertible(file_path: Path) -> bool:
    """Check if a file should be processed by convert_directory."""
    return (
        file_path.is_file()
        and not file_path.name.startswith(".")
        and file_path.suffix.lower() in SUPPORTED_EXTENSIONS
    )


def convert_directory(
    input_dir: Path,
    output_dir: Path,
    *,
    recursive: bool = False,
    overwrite: bool = True,
    on_error: str = "warn",        # "warn" | "raise" | "skip"
) -> list[Path]:
    """
    Convert all supported documents in a directory to Markdown.

    Args:
        input_dir:  Source directory.
        output_dir: Destination directory for .md files.
        recursive:  If True, recurse into subdirectories.
        overwrite:  Overwrite existing .md files.
        on_error:   How to handle individual file errors:
                    'warn' – print warning and continue
                    'raise' – re-raise the exception
                    'skip'  – silently skip

    Returns:
        List of Paths to successfully written .md files.
    """
    input_dir = Path(input_dir)
    if not input_dir.exists():
        print(f"  Directory not found: {input_dir}")
        return []

    glob = "**/*" if recursive else "*"
    all_files = sorted(input_dir.glob(glob))
    convertible = [f for f in all_files if _is_convertible(f)]
    skipped = len(all_files) - len(convertible)
    results: list[Path] = []

    for file_path in convertible:
        try:
            out = to_markdown(file_path, output_dir, overwrite=overwrite)
            print(f"  OK  {file_path.name}  ->  {out.name}")
            results.append(out)
        except Exception as exc:
            if on_error == "raise":
                raise
            if on_error == "warn":
                print(f"  ERR {file_path.name}: {exc}")

    if skipped:
        print(f"  (skipped {skipped} unsupported file(s))")

    return results

