# Workflow Modes

This repository uses four workflow modes. Orchestrator Lite selects the smallest
safe mode using `governance/routing-policy.yaml` and `governance/policy.yaml`.

## Lightweight

Use for:

- small docs updates
- small local reversible config changes
- local validation/tooling smoke checks
- low-risk typo or formatting fixes

Default agents:

- Orchestrator Lite
- Developer or Documenter
- optional Reviewer

Artifacts:

- inline contract or mini Workorder
- validation evidence
- short completion note

Do not invoke:

- Lead Coordinator
- Project Planner
- Mira
- domain experts

## Standard

Use for:

- normal template/framework work
- multi-file implementation
- prompt/agent/instruction updates with explicit scope
- changes requiring acceptance criteria and validation evidence

Default agents:

- Orchestrator Lite
- Workorder Planner
- Developer
- Reviewer
- Documenter when docs/report updates are needed

Optional:

- Architect if architecture, schema, or boundary impact exists
- Domain expert only if routing policy triggers one

## High Risk

Use for:

- secrets
- PII or sensitive raw content
- legal/privacy/security impact
- API, schema, or data model changes
- dependency changes
- CI/CD, deployment, or external automation
- LLM/RAG/agentic behavior
- destructive or irreversible actions
- external factual claims or external side effects

Default:

- Orchestrator Lite
- Workorder Planner
- relevant risk/domain triage
- Developer
- Reviewer

Optional:

- Lead Coordinator for cross-domain conflict
- DoubleCheck for factual verification
- Architect for architecture impact
- Human approval when policy requires it

## Discovery

Use for:

- opportunity discovery
- roadmap shaping
- strategic provocations
- capability hypotheses
- major product direction questions

Default:

- Mira

Next filters:

- Product Owner prioritizes
- Data Analyst measures
- Workorder Planner specifies
- Developer implements only after approved scope exists
