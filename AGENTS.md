# AGENTS.md — Multi-Agent Team Reference

This file documents all agents in this workspace, their domains, when to invoke them, and how they interact.

> **Quick start:** When in doubt, invoke `@Orchestrator – Workflow Manager`. The Orchestrator routes tasks to the right agents and manages Human-in-the-Loop gates.

---

## Two Functional Layers

This agent roster operates across two distinct functional layers:

| Layer | Tiers | Function |
|---|---|---|
| **Analysis Layer** | Tier 1–2 + Tier 4 | Deep domain analysis → Reports and recommendations for human review |
| **Execution Layer** | Tier 3 | Translate approved decisions into code, specs, tests, and commits |

**Flow:** Orchestrator → Lead Coordinator → Tier 4 Domain Personas → Lisa (Workorder Planner) → Execution Layer (Lena, Robin, Marco, Chris, Jana, Finn)

**Rule:** No Execution Layer agent implements work that has not been approved by a Workorder and cleared by Marco's pre-implementation gate. No Analysis Layer agent writes application code.

---

## Tier 1 — Orchestration

| Agent | File | When to Invoke |
|---|---|---|
| **Orchestrator** | `orchestrator.agent.md` | Entry point for new features, sprint start, phasenwechsel, cross-domain analysis |
| **Lead Coordinator** | `lead-coordinator.agent.md` | Strategic synthesis, conflict resolution between domain agents, architectural trade-off decisions |

---

## Tier 2 — Planning & Quality

Pure coordination and quality roles — no execution personas. For Workorder/code/doc work, use Tier 3.

| Agent | File | When to Invoke |
|---|---|---|
| **Project Planner** | `project-planner.agent.md` | Milestones, task sequencing, dependency mapping, sprint planning |
| **ADR Generator** | `adr-generator.agent.md` | Documenting architecture decisions formally (ADR format); utility for Robin |
| **Critical Thinker** | `critical-thinker.agent.md` | Red-teaming assumptions, challenging proposals before commitment |
| **Doublecheck** | `doublecheck.agent.md` | Second opinion on high-stakes decisions |

---

## Tier 3 — Execution Layer

These agents operate close to the code. They receive decisions from the Analysis Layer (Tier 4 personas) and execute against approved Workorders. Each has a persona that reflects their specific craft.

| Agent | Persona | File | When to Invoke |
|---|---|---|---|
| **Workorder Planner** | **Lisa** | `workorder-planner.agent.md` | Creating/refining Workorders, scope definition, WO_CATALOG |
| **Architect** | **Robin** | `architect.agent.md` | Translating architecture decisions into module structure, ADRs, import boundaries |
| **Developer** | **Lena** | `developer.agent.md` | Implementing approved Workorders in Python |
| **Reviewer** | **Marco** | `reviewer.agent.md` | Pre/post-implementation gate, GREEN/YELLOW/RED decisions |
| **Security Reviewer** | **Chris** | `security-reviewer.agent.md` | Code-level security review, OWASP findings, fix verification |
| **Integrator** | **Jana** | `integrator.agent.md` | Merging branches after GREEN gate, CI verification, PRs |
| **Documenter** | **Finn** | `documenter.agent.md` | README, docstrings, WO reports, wiki snippets |

---

## Tier 4 — Analysis Layer (Domain-Expert Personas)

These agents bring deep domain methodology. Invoke them directly for focused analysis in their domain or let the Lead Coordinator coordinate them.

### Product & Business

| Agent | File | Domain | When to Invoke |
|---|---|---|---|
| **Arne** | `arne-product-owner.agent.md` | Product strategy, roadmap, monetization | Backlog prioritization, pricing decisions, freemium design, OKR alignment, business case validation |
| **Tom** | `tom-growth.agent.md` | Growth, acquisition, retention | Channel strategy, A/B test design for growth, ASO/SEO, PLG mechanics, churn analysis |
| **David** | `david-customer-success.agent.md` | Onboarding, activation, health scoring | Activation design, TTV optimization, health score definition, churn intervention playbooks |

### Design & Communication

| Agent | File | Domain | When to Invoke |
|---|---|---|---|
| **Sophie** | `sophie-ux-designer.agent.md` | UX/UI, interaction design, permission flows | User flows, wireframe review, onboarding design, dark pattern audit, A/B test UX |
| **Mia** | `mia-content-strategist.agent.md` | UX writing, content strategy, plain language | Microcopy, consent copy, legal translation, voice/tone, incident communication |

### Engineering & Data

| Agent | File | Domain | When to Invoke |
|---|---|---|---|
| **Elena** | `elena-ai-engineer.agent.md` | LLM architecture, RAG, AI evaluation, AI security | Model selection, RAG design, evaluation strategy, prompt injection defense, cost optimization |
| **Max** | `max-software-architect.agent.md` | Software architecture, ADRs, API design | Microservices vs. monolith, API contract design, persistence strategy, C4 documentation |
| **Felix** | `felix-devops.agent.md` | Infrastructure, CI/CD, SRE, EU data residency | Deployment architecture, observability, SLO definition, queue design, EU hosting compliance |
| **Sam** | `sam-ios-developer.agent.md` | iOS/Swift/SwiftUI, App Store, StoreKit | SwiftUI architecture, subscription flows, privacy manifests, App Review compliance |
| **Kai** | `kai-data-analyst.agent.md` | Analytics, metrics, A/B testing, event tracking | Metrics design, funnel analysis, cohort analysis, experiment validity, analytics stack |

### Legal & Privacy

| Agent | File | Domain | When to Invoke |
|---|---|---|---|
| **Jochen** | `jochen-legal-advisor.agent.md` | EU AI Act, GDPR, DSA, product liability | Regulatory compliance assessment, DPIA triggers, legal basis for processing, license risks |
| **Nadia** | `nadia-privacy-ciso.agent.md` | Privacy by design, CISO, TEE, threat modeling | STRIDE/LINDDUN analysis, TEE design, OAuth security, prompt injection defense, privacy engineering |

---

## Collaboration Patterns

### Feature Planning Workflow

```
1. @Orchestrator           → assess scope and risks, create brief
2. @Lead Coordinator       → coordinate domain analysis (max 4 agents/batch)
3. Domain Agents (Tier 4)  → parallel analysis in their domain
4. @Lead Coordinator       → synthesize, identify conflicts
5. [HITL]                  → human review of critical decisions
6. @Lisa                   → create implementation Workorder
7. @Lena                   → implement against approved spec
8. @Marco                  → code review (GREEN/YELLOW/RED gate)
9. @Jana                   → merge after GREEN gate
10. @Finn                  → update technical docs
```

### Cross-Domain Escalation Patterns

| Situation | Escalate To |
|---|---|
| Privacy vs. UX tension (consent flow) | Nadia + Sophie → Lead Coordinator |
| Legal vs. Product (feature risk) | Jochen + Arne → Lead Coordinator |
| AI vs. DevOps (model hosting decision) | Elena + Felix → Lead Coordinator |
| Architecture vs. Delivery speed | Max + Arne → Lead Coordinator |

---

## Agent Configuration

All persona agents end with a `## ⚙️ Project Configuration` section in YAML. This section **must be filled in** with project-specific context before the agent can provide accurate domain analysis.

See each individual `.agent.md` file for the project configuration template relevant to that agent's domain.

---

## Adding New Agents

1. Create `your-agent-name.agent.md` in `.github/agents/`
2. Use the structure established in this directory (frontmatter → Session Start → Domain Expertise → Tasks → Boundaries → Output Format → Agent Skills → ⚙️ Project Configuration)
3. Add the agent to the Layer 4 table above with domain and invocation criteria
4. Copy to `~/Library/Application Support/Code/User/agents/` to make it visible in the VS Code agent picker
