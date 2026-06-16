# AGENTS.md

This repository is an AI-assisted development template. It uses a slim,
policy-driven agent workflow. Start with the smallest safe workflow mode and
activate domain experts only when routing or policy requires them.

Start with:

- `context/STARTUP_BRIEF.md`
- `governance/project.profile.yaml`
- `governance/routing-policy.yaml`
- `governance/policy.yaml`
- `docs/agent-framework/workflow-modes.md`
- `docs/agent-framework/workorder-quality-contract.md`

Do not load full session logs by default. Use hot context first, then targeted
files only.

---

## Workflow Modes

Use the smallest safe mode:

| Mode | Use for | Default agents |
|---|---|---|
| `lightweight` | Small local reversible docs, config, validation, or tooling tasks | Orchestrator Lite -> Developer or Documenter |
| `standard` | Normal feature or template work with explicit scope and evidence | Orchestrator Lite -> Workorder Planner -> Developer -> Reviewer |
| `high_risk` | Security, privacy, legal, API/schema, infra, dependency, LLM/RAG, irreversible, or external-effect work | Orchestrator Lite -> Workorder Planner -> relevant risk/domain triage -> Developer -> Reviewer |
| `discovery` | Ideas, vision, roadmap shaping, opportunity discovery | Mira only, then optional product/data review |

Policy beats persona. If `governance/policy.yaml` says ask or deny, no agent may
route around it.

---

## Core Agents

| Agent | File | Activation |
|---|---|---|
| Orchestrator Lite | `.github/agents/orchestrator.agent.md` | Always first for non-trivial routing; read/classify/delegate only |
| Workorder Planner | `.github/agents/workorder-planner.agent.md` | Standard/high-risk work that needs a Workorder or spec |
| Developer | `.github/agents/developer.agent.md` | Implementation of approved scope |
| Reviewer | `.github/agents/reviewer.agent.md` | Pre-implementation and post-implementation quality gates |
| Documenter | `.github/agents/documenter.agent.md` | README/docs/reports/closeouts after evidence exists |

---

## On-Demand Optional Agents

These agents are not part of the default workflow.

| Agent | File | Call only when |
|---|---|---|
| Architect | `.github/agents/architect.agent.md` | Architecture, API/schema, data model, import boundaries, ADR impact |
| Lead Coordinator | `.github/agents/lead-coordinator.agent.md` | 3+ domains, conflicting findings, multi-option HITL synthesis |
| Project Planner | `.github/agents/project-planner.agent.md` | Roadmap, milestones, dependency sequencing, plan-health |
| Mira | `.github/agents/mira-visionary-discovery.agent.md` | Discovery, strategic provocation, major roadmap shaping |
| Security Reviewer | `.github/agents/security-reviewer.agent.md` | Secrets, auth, vulnerabilities, dependency/security review |
| Privacy/CISO | `.github/agents/nadia-privacy-ciso.agent.md` | PII, threat modeling, privacy-by-design, TEE/OAuth risks |
| Legal Advisor | `.github/agents/jochen-legal-advisor.agent.md` | Legal/regulatory claims, GDPR/EU AI Act/DSA/product liability |
| AI Engineer | `.github/agents/elena-ai-engineer.agent.md` | PromptOps, RAG, tool calls, model evals, LLM/agentic risks |
| DevOps | `.github/agents/felix-devops.agent.md` | CI/CD, infrastructure, observability, hosting/data residency |
| Product/Business/UX/Data domain agents | relevant `.github/agents/*.agent.md` | Product strategy, UX, content, growth, analytics, customer success |

Domain experts provide analysis and recommendations. They are not independent
assurance, legal sign-off, security sign-off, or implementation approval.

---

## Routing Rules

1. Orchestrator Lite reads startup brief, routing policy, governance policy, and
   active blocked decisions.
2. Orchestrator Lite classifies the request as `lightweight`, `standard`,
   `high_risk`, or `discovery`.
3. If policy requires explicit approval, pause before routing.
4. If work is non-trivial, Workorder Planner creates or refines the Workorder.
5. Developer implements only approved scope.
6. Reviewer checks spec-code gap and issues GREEN/YELLOW/RED.
7. Documenter writes final closeout only after implementation evidence and review
   evidence exist.

AI concurrence is not independent assurance. Multiple AI reviews from the same
model/context count as one correlated AI signal unless evidence packages or
deterministic tools differ.

---

## Workorder Rule

Non-trivial Workorders must include:

- explicit user/template value
- in-scope and out-of-scope items
- Critical Path Fit
- stable IDs for requirements and acceptance criteria
- evidence mapping for every acceptance criterion
- risk/security/privacy/architecture impact or explicit `N/A`
- validation commands or manual review checklist
- residual gaps or explicit `none`

Use `docs/agent-framework/workorder-quality-contract.md` as the contract.

---

## No-Copy Rule for Cross-Repo Migration

When adopting patterns from another repository, copy workflow mechanics only.
Do not copy product-specific wiki, knowledge, historical session logs, private
paths, `.env`, secrets, local credentials, provider tokens, domain workorders, or
irrelevant domain agents.
