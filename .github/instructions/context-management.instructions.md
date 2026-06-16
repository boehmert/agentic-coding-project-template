---
description: "Hot/warm/cold context loading rules for token-aware agent sessions."
applyTo: "**"
priority: recommended
---

# Context Management Instructions

## Hot / Warm / Cold Context

Hot context:

- `context/STARTUP_BRIEF.md`
- active Workorder
- active blocked decisions
- relevant ADRs
- `governance/project.profile.yaml`
- `governance/routing-policy.yaml`
- `governance/policy.yaml`

Warm context:

- related completed Workorders
- relevant session outputs
- referenced reports
- project profile sections
- targeted docs

Cold context:

- full session logs
- archived reports
- old branches
- completed Workorders not referenced by the current task
- generated output

## Startup Rule

Do not replay full history. Rehydrate from `context/STARTUP_BRIEF.md` and
targeted artifacts.

## Memory Metadata

When adding persistent memory or context entries, include when possible:

- scope
- workorder_id
- agent_id
- source_artifact
- created_at
- last_validated_at
- importance
- evidence_grade
- supersedes
- expires_at
- visibility
