# Session Log Schema

This schema defines the format for individual entries in `context/SESSION_LOG.md`.
Each session appends **one entry** at the bottom of the file (append-only).

---

## Entry Format

```markdown
---
## Session: YYYY-MM-DD HH:MM | [session-id or short description]

**Agent(s) used:** developer | reviewer | architect | ...
**Duration:** ~Xh
**Status:** COMPLETED | PARTIAL | BLOCKED

### User Intent
What the user wanted to achieve in this session (in their own words or paraphrased).
Use the "why", not just the "what".

### Consulted Artifacts
- `path/to/artifact.md` – reason (e.g. "active Workorder")
- `context/ARTIFACT_REGISTRY.md` – orientation
- `workorders/WO_CATALOG.md` – workorder status

### Decisions Made
- Decision 1 → see [ADR-xxx](docs/adr/ADR-xxx_title.md) (if applicable)
- Decision 2 (inline, no ADR needed)

### Created / Modified Artifacts
| Action | Artifact | Notes |
|--------|----------|-------|
| CREATED | `workorders/WO02_title.md` | New workorder |
| MODIFIED | `src/module/file.py` | Implemented feature X |
| CREATED | `context/ARTIFACT_REGISTRY.md` | Initial version |

### Open Points for Next Session
- [ ] Open question 1 – suggested owner or agent
- [ ] Open question 2 – decision still pending

### Recommendation for Next Session
Load: [list artifacts to load next time], start with: [suggested first action]
---
```

---

## Field Descriptions

| Field | Required | Description |
|-------|----------|-------------|
| `Session` header | Yes | ISO date + short description or session ID |
| `Agent(s) used` | Yes | Which agents were active in this session |
| `Duration` | Optional | Rough time spent |
| `Status` | Yes | Whether session goal was reached |
| `User Intent` | Yes | The _why_ – strategic goal of this session |
| `Consulted Artifacts` | Yes | Files read for context, with reason |
| `Decisions Made` | Yes | Key decisions, with ADR reference if applicable |
| `Created / Modified Artifacts` | Yes | All files touched (created, modified, deleted) |
| `Open Points` | Yes | Unresolved items for the next session |
| `Recommendation` | Recommended | What to load / where to start next session |

---

## Usage Rules

1. **Append-only** – never delete or overwrite existing entries
2. **One entry per session** – a session = one focused work block
3. **Write at session end** – use the `session-recap` prompt to generate
4. **Link artifacts by path** – use repo-relative paths
5. **Keep entries concise** – target max 30 lines per entry

---

## Example Entry

```markdown
---
## Session: 2026-03-03 14:00 | Bootstrap memory management artifacts

**Agent(s) used:** developer
**Duration:** ~2h
**Status:** COMPLETED

### User Intent
Solve the context/memory loss problem across Copilot sessions by adding
structured session logs, artifact registry, and intent tracking to the framework.

### Consulted Artifacts
- `.github/copilot-instructions.md` – framework entry point
- `.github/FRAMEWORK_MANIFEST.md` – existing artifact registry
- `Spec-Driven-Framework-Context.md` – framework context doc

### Decisions Made
- Use `context/` folder for all memory management artifacts
- SESSION_LOG.md is append-only, not per-session files (lower overhead)
- ARTIFACT_REGISTRY.md covers all artifact types (not a separate WO_CATALOG)

### Created / Modified Artifacts
| Action | Artifact | Notes |
|--------|----------|-------|
| CREATED | `context/ARTIFACT_REGISTRY.md` | Central artifact index |
| CREATED | `context/SESSION_LOG.md` | Append-only session memory |
| CREATED | `context/USER_INTENT_LOG.md` | Strategic intent tracking |
| MODIFIED | `.github/copilot-instructions.md` | Added Mandatory Context Protocol |

### Open Points for Next Session
- [ ] Adapt Team-workspace ARTIFACT_REGISTRY to actual project artifacts
- [ ] Decide whether to automate session-recap via tasks/ script

### Recommendation for Next Session
Load: `context/ARTIFACT_REGISTRY.md`, `context/SESSION_LOG.md` (last entry),
`context/USER_INTENT_LOG.md` (last entry). Start with: pending open points above.
---
```

