---
name: Markdown Standards
description: Standards for Markdown documentation files.
applyTo: "**/*.md"
priority: optional
---

# Markdown Standards

These standards apply to all Markdown files in this workspace.

---

## 1. File Structure

### Frontmatter (Required for Specs)
All specification files (Workorders, ADRs, Reports) must have YAML frontmatter:

```markdown
---
id: WO01
title: "Descriptive Title"
status: PLANNED
created: 2026-02-06
---
```

### Document Structure
```markdown
# Main Title (H1 - only one per document)

Brief introduction paragraph.

---

## Section 1 (H2)

Content...

### Subsection 1.1 (H3)

Content...

---

## Section 2 (H2)

Content...
```

---

## 2. Headings

### Hierarchy Rules
- **H1 (`#`)**: Document title only, exactly once
- **H2 (`##`)**: Major sections
- **H3 (`###`)**: Subsections
- **H4 (`####`)**: Avoid if possible; restructure content instead
- **H5+**: Never use

### Formatting
- Use sentence case: `## Getting started` (not `## Getting Started`)
- No punctuation at end of headings
- Blank line before and after headings

---

## 3. Lists

### Bullet Lists
Use for unordered items:
```markdown
- First item
- Second item
  - Nested item (2 spaces indent)
  - Another nested item
- Third item
```

### Numbered Lists
Use for sequential steps or ordered items:
```markdown
1. First step
2. Second step
   1. Sub-step (3 spaces indent)
   2. Another sub-step
3. Third step
```

### Task Lists
Use for checklists:
```markdown
- [ ] Incomplete task
- [x] Completed task
- [ ] Another task
```

---

## 4. Code

### Inline Code
Use backticks for:
- File names: `config.yaml`
- Function names: `process_data()`
- Variable names: `user_id`
- Commands: `pip install`

### Code Blocks
Always specify the language:

~~~markdown
```python
def example():
    return "Hello"
```
~~~

~~~markdown
```yaml
key: value
list:
  - item1
  - item2
```
~~~

~~~markdown
```bash
pip install -r requirements.txt
python -m pytest
```
~~~

---

## 5. Tables

### Standard Format
```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Value 1  | Value 2  | Value 3  |
| Value 4  | Value 5  | Value 6  |
```

### Alignment
```markdown
| Left     | Center   | Right    |
|:---------|:--------:|---------:|
| Text     | Text     | Text     |
```

### Best Practices
- Keep tables simple (max 5-6 columns)
- Use consistent column widths
- Align separator dashes with content

---

## 6. Links and References

### Internal Links
```markdown
See [Workorder Schema](schemas/workorder.schema.md) for details.
Refer to [Section 2](#section-2) above.
```

### External Links
```markdown
Based on [PEP 8](https://pep8.org/) guidelines.
```

### Reference-Style Links
For documents with many links:
```markdown
See the [official documentation][docs] for more details.

[docs]: https://example.com/docs
```

---

## 7. Emphasis

### Bold and Italic
```markdown
**Bold** for strong emphasis or key terms.
*Italic* for introducing terms or light emphasis.
***Bold italic*** sparingly, for critical warnings.
```

### Strikethrough
```markdown
~~Deprecated~~ - use for obsolete content
```

---

## 8. Blockquotes

### Standard Usage
```markdown
> This is a blockquote.
> It can span multiple lines.
```

### Callouts (GitHub-style)
```markdown
> [!NOTE]
> Useful information that users should know.

> [!TIP]
> Helpful advice for doing things better.

> [!IMPORTANT]
> Key information users need to know.

> [!WARNING]
> Urgent info that needs immediate attention.

> [!CAUTION]
> Advises about risks or negative outcomes.
```

---

## 9. Horizontal Rules

Use `---` to separate major sections:
```markdown
## Section 1

Content...

---

## Section 2

Content...
```

---

## 10. Line Length and Wrapping

### Rules
- **Prose**: Wrap at ~80-100 characters for readability
- **Code blocks**: Can exceed line length if necessary
- **Tables**: Can exceed line length if necessary
- **URLs**: Never break URLs across lines

### Paragraph Spacing
- One blank line between paragraphs
- One blank line before and after code blocks
- One blank line before and after lists

---

## 11. File Naming

### Conventions
- Use kebab-case: `my-document.md`
- Workorders: `WO01_descriptive-title.md`
- ADRs: `ADR-001_decision-title.md`
- Reports: `WO01_report_2026-02-06.md`
- Schemas: `workorder.schema.md`

### Avoid
- Spaces in filenames
- Special characters except `-` and `_`
- Very long filenames (>50 chars)

---

## 12. Accessibility

### Images
Always include alt text:
```markdown
![Diagram showing data flow](images/data-flow.png)
```

### Semantic Structure
- Use proper heading hierarchy (don't skip levels)
- Use lists for list content (not just line breaks)
- Use tables for tabular data (not code blocks)

---

## 13. Changelog Section

For versioned documents, include at the end:

```markdown
---

## Changelog

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-02-06 | @author | Initial version |
| 1.1.0 | 2026-02-07 | @author | Added section X |
```

