---
last_updated: YYYY-MM-DD
updated_by: human
---

# Artifact Registry

> Machine-readable index of all steering artifacts in this workspace.
> **Read this file first at every session start.**
> Schema: `.github/schemas/artifact-registry.schema.md`

---

## How to Use This Registry

1. Scan tables below for current artifact landscape
2. Load only files relevant to your current task
3. `DONE`, `DEPRECATED`, `CANCELLED` → skip unless historical reference needed
4. **Update this file at every session end** (new artifacts, status changes)

---

## Workorders

| ID | Title | Status | Path | Last Updated |
|----|-------|--------|------|--------------|
| – | – | – | – | – |

**Active Workorder:** *(none yet)*

---

## Architecture Decision Records (ADRs)

| ID | Title | Status | Path | Last Updated |
|----|-------|--------|------|--------------|
| – | – | – | – | – |

---

## Session Memory

| Artifact | Path | Last Updated | Notes |
|----------|------|--------------|-------|
| Session Log | `context/SESSION_LOG.md` | *(not yet started)* | – |
| User Intent Log | `context/USER_INTENT_LOG.md` | *(not yet started)* | – |

---

## Reports

| ID | Title | Path | Date |
|----|-------|------|------|
| – | – | – | – |

---

## Repository State

| Artifact | Path | Status |
|----------|------|--------|
| REPO_STATE | `REPO_STATE.md` | NOT YET CREATED |
| WO_CATALOG | `workorders/WO_CATALOG.md` | NOT YET CREATED |
| Framework Manifest | `.github/FRAMEWORK_MANIFEST.md` | EXISTS |
| This Registry | `context/ARTIFACT_REGISTRY.md` | EXISTS |

---

## Custom Artifacts

> Add project-specific artifacts here: Runbooks, Playbooks, Guardrails, Manifests, etc.

| Type | Title | Status | Path | Last Updated |
|------|-------|--------|------|--------------|
| – | – | – | – | – |

---

## Maintenance

- Update on every session end
- Never delete rows – change status to `DONE`, `DEPRECATED`, or `CANCELLED`
- Paths are repo-relative
- Keep **Active Workorder** line current
