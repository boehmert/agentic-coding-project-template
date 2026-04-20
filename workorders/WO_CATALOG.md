---
last_updated: 2026-04-20
---

# Workorder Catalog

Central registry of all Workorders in this workspace.

> **Rule:** Never delete rows. Use status `CANCELLED` or `DONE` to close items.
> Add new entries at the bottom. Keep `Last Updated` current.

---

## Active

| ID | Title | Status | Priority | Created | Assignee | Last Updated |
|----|-------|--------|----------|---------|----------|-------------|
| – | – | – | – | – | – | – |

---

## Completed

| ID | Title | Status | Priority | Created | Completed | Report |
|----|-------|--------|----------|---------|-----------|--------|
| WO00 | Framework Bootstrap | DONE | HIGH | 2026-02-06 | 2026-04-20 | – |

---

## Cancelled / Blocked

| ID | Title | Status | Reason | Created |
|----|-------|--------|--------|---------|
| – | – | – | – | – |

---

## How to Add a New Workorder

1. Copy `workorders/_template/workorder-template.md` → `workorders/WOxx_your-title.md`
2. Fill in all required frontmatter fields
3. Add entry to the **Active** table above
4. Move to **Completed** when status = `DONE` (add completion date and report link)
