# Artifact Registry Schema

This schema defines the structure of `context/ARTIFACT_REGISTRY.md`.
The registry is the **single source of truth for artifact discoverability**.
It is the first file an agent reads at the start of a session.

---

## Purpose

| Without Registry | With Registry |
|-----------------|---------------|
| Agent scans repository blindly | Agent reads one file to locate all artifacts |
| Duplicates work done in previous sessions | Agent knows what exists and where |
| No disambiguation of active vs. archived artifacts | Status field makes current state visible |
| Artifacts discovered randomly | Structured discovery by type and status |

---

## File Structure

```markdown
---
last_updated: YYYY-MM-DD
updated_by: [human | agent-name]
---

# Artifact Registry

> Machine-readable index of all steering artifacts in this workspace.
> Read this file first at every session start.

---

## How to Use This Registry

1. Scan the tables below to understand what exists
2. Load only the artifacts relevant to your current task
3. Check `Status` – only ACTIVE/IN_PROGRESS artifacts need attention
4. After creating or completing artifacts, update this file

---

## Workorders

| ID | Title | Status | Path | Last Updated |
|----|-------|--------|------|-------------|
| WO01 | Title | DONE | `workorders/WO01_title.md` | 2026-02-06 |
| WO02 | Title | IN_PROGRESS | `workorders/WO02_title.md` | 2026-03-01 |

**Active Workorder:** WO02 – `workorders/WO02_title.md`

---

## Architecture Decision Records (ADRs)

| ID | Title | Status | Path | Last Updated |
|----|-------|--------|------|-------------|
| ADR-001 | Title | ACCEPTED | `docs/adr/ADR-001_title.md` | 2026-02-06 |

---

## Session Memory

| Artifact | Path | Last Updated | Notes |
|----------|------|-------------|-------|
| Session Log | `context/SESSION_LOG.md` | YYYY-MM-DD | Last session: [short description] |
| User Intent Log | `context/USER_INTENT_LOG.md` | YYYY-MM-DD | Active intent: [short description] |

---

## Reports

| ID | Title | Path | Date |
|----|-------|------|------|
| WO01-report | Report for WO01 | `workorders/reports/WO01_report_YYYY-MM-DD.md` | YYYY-MM-DD |

---

## Repository State

| Artifact | Path | Status |
|----------|------|--------|
| REPO_STATE | `REPO_STATE.md` | EXISTS / NOT YET CREATED |
| WO_CATALOG | `workorders/WO_CATALOG.md` | EXISTS / NOT YET CREATED |
| Framework Manifest | `.github/FRAMEWORK_MANIFEST.md` | EXISTS |
| This Registry | `context/ARTIFACT_REGISTRY.md` | EXISTS |

---

## Custom Artifacts
> Add project-specific artifacts here (Runbooks, Playbooks, Guardrails, etc.)

| Type | Title | Status | Path | Last Updated |
|------|-------|--------|------|-------------|
| Runbook | Title | ACTIVE | `docs/runbooks/title.md` | YYYY-MM-DD |
| Playbook | Title | ACTIVE | `docs/playbooks/title.md` | YYYY-MM-DD |

---

## Maintenance

See [Artifact Registry Maintenance Rules](#maintenance-rules) below.
```

---

## Status Values

| Status | Meaning | Agent Action |
|--------|---------|-------------|
| `PLANNED` | Not yet started | Load for planning |
| `IN_PROGRESS` | Actively being worked | **Always load** |
| `REVIEW` | Awaiting review | Load for review tasks |
| `DONE` | Completed | Load only for reference |
| `ACTIVE` | Ongoing artifact (ADRs, logs) | Load when relevant |
| `ACCEPTED` | ADR accepted | Load for architecture context |
| `DEPRECATED` | No longer in use | Skip |
| `CANCELLED` | Abandoned | Skip |

---

## Maintenance Rules

1. **Update on every session end** – add new artifacts, update statuses
2. **Never delete rows** – use `DONE`, `DEPRECATED`, or `CANCELLED`
3. **Keep path references exact** – repo-relative paths only
4. **One active workorder highlighted** – mark the current focus
5. **Custom artifacts section** – extend per project, do not modify the schema

---

## Relationship to Other Artifacts

```
ARTIFACT_REGISTRY.md ──points to──► All other artifacts
         │
         ├── WO_CATALOG.md (Workorder details)
         ├── SESSION_LOG.md (operational history)
         ├── USER_INTENT_LOG.md (strategic goals)
         └── REPO_STATE.md (current system state)
```

The registry is a **navigation index**, not a replacement for any of these files.

