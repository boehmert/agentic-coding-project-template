---
description: "Shared evidence, assumption, context-pruning, and critical-path rules for all agents."
applyTo: "**"
priority: recommended
---

# Agent Common Protocol

## Evidence Grade

Use evidence grades instead of unsupported confidence.

| Grade | Meaning | Action |
|---|---|---|
| A | Code, tests, primary source, deterministic check, or binding artifact supports the claim. | Proceed. |
| B | Strong evidence exists but coverage is incomplete. | Proceed with caveat. |
| C | Plausible assumption but weak evidence. | Proceed only if reversible and low-risk; record assumption. |
| D | Insufficient evidence or high-risk uncertainty. | Abstain or escalate. |

## Assumption Handling

If evidence is incomplete:

- Create `ASM-001`, `ASM-002`, etc.
- Mark the assumption as blocking or non-blocking.
- Proceed only if the action is reversible, local, and policy-covered.
- Ask or escalate when the decision is irreversible, public,
  security/privacy/legal-sensitive, expensive, or changes a public contract.

## Context Pruning

Load only context relevant to the current task. Prefer:

1. `context/STARTUP_BRIEF.md`
2. active Workorder
3. relevant ADRs
4. relevant policy files
5. targeted code or docs

Do not load full session logs unless explicitly needed.

## Critical Path Discipline

For non-trivial work, use `docs/agent-framework/workorder-quality-contract.md`.
Before expanding scope, classify optional suggestions:

| Classification | Meaning | Action |
|---|---|---|
| `critical_path` | Required to reach the current outcome. | May enter active scope. |
| `quality_bar` | Needed to make the current outcome credible, reviewable, or maintainable. | May enter current scope if small and evidence-backed. |
| `risk_reduction` | Reduces immediate policy, security, privacy, legal, data, or delivery risk. | May enter scope only with the relevant gate. |
| `roadmap_candidate` | Valuable, but belongs in roadmap/backlog shaping. | Route to planning. |
| `parking_lot` | Plausibly useful but not needed now and not ready for commitment. | Record outside implementation scope. |
| `do_not_do_now` | Distracting, speculative, duplicate, or contrary to current intent/policy. | Do not implement. |

Parking Lot items do not authorize implementation.

## Output Discipline

For non-trivial outputs include:

- decision or finding
- rationale
- evidence
- risks
- next step
