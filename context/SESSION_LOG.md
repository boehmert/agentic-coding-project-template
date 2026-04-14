# Session Log

> Append-only log of AI coding sessions.
> Schema: `.github/schemas/session-log.schema.md`
> Prompt: `.github/prompts/session-recap.prompt.md`

**Rule:** Never edit or delete existing entries. Always append at the bottom.

---

## How to Generate a New Entry

Use the session-recap prompt at the end of each work session:
1. Open `.github/prompts/session-recap.prompt.md`
2. Or say: "session recap" / "log the session" / "wrap up"

---

<!-- Session entries start below. Most recent entry is at the bottom. -->

<!-- EXAMPLE ENTRY (delete this when adding real entries)
---
## Session: 2026-02-06 10:00 | Example session

**Agent(s) used:** developer
**Duration:** ~1h
**Status:** COMPLETED

### User Intent
Bootstrap the repository with the spec-driven framework to create
a reusable template for future projects.

### Consulted Artifacts
- `.github/copilot-instructions.md` – main framework instructions
- `.github/FRAMEWORK_MANIFEST.md` – artifact versions

### Decisions Made
- Use semantic versioning for all framework artifacts
- agents/ and schemas/ live under .github/

### Created / Modified Artifacts
| Action | Artifact | Notes |
|--------|----------|-------|
| CREATED | `context/SESSION_LOG.md` | This file |
| CREATED | `context/ARTIFACT_REGISTRY.md` | Central index |

### Open Points for Next Session
- [ ] Add first real workorder

### Recommendation for Next Session
Load: `context/ARTIFACT_REGISTRY.md`. Start with: creating first workorder.
---
END EXAMPLE -->
