---
framework_name: Agentic Coding Project Template
version: 2.1.0
status: ACTIVE
created: 2026-02-06
updated: 2026-06-16
---

# Framework Manifest

Provenance and version tracking for all framework artifacts.

---

## Framework Version

| Field | Value |
|---|---|
| **Version** | 2.1.0 |
| **Status** | ACTIVE |
| **Created** | 2026-02-06 |
| **Updated** | 2026-06-16 |

---

## Artifact Registry

### Agents (Layer 1 — Spec-Driven)

| ID | File | Status | Description |
|---|---|---|---|
| orchestrator | `agents/orchestrator.agent.md` | ACTIVE | Orchestrator Lite: routing, policy gates, delegation only |
| architect | `agents/architect.agent.md` | ON_DEMAND | Architecture impact, ADR content, API/schema/module-boundary decisions |
| workorder-planner | `agents/workorder-planner.agent.md` | ACTIVE | Create workorders, define scope |
| developer | `agents/developer.agent.md` | ACTIVE | Implement workorders, write code |
| reviewer | `agents/reviewer.agent.md` | ACTIVE | Validate plans and implementations |
| integrator | `agents/integrator.agent.md` | ACTIVE | Merge branches, prepare PRs |
| documenter | `agents/documenter.agent.md` | ACTIVE | Documentation and knowledge |
| security-reviewer | `agents/security-reviewer.agent.md` | ON_DEMAND | Security analysis |

### Agents (Layer 2 — Knowledge & Review)

| ID | File | Status | Description |
|---|---|---|---|
| adr-generator | `agents/adr-generator.agent.md` | ACTIVE | Create ADRs with structured formatting |
| critical-thinker | `agents/critical-thinker.agent.md` | ACTIVE | Challenge assumptions, find blind spots |
| doublecheck | `agents/doublecheck.agent.md` | ACTIVE | Fact-check AI outputs, flag risks |
| lead-coordinator | `agents/lead-coordinator.agent.md` | ON_DEMAND | Cross-domain synthesis and conflict resolution |
| project-planner | `agents/project-planner.agent.md` | ON_DEMAND | Roadmap, milestone, dependency, and plan-state ownership |
| mira-visionary-discovery | `agents/mira-visionary-discovery.agent.md` | ON_DEMAND | Discovery, opportunity, vision, and roadmap hypotheses |

### Instructions

| ID | File | Status | Description |
|---|---|---|---|
| vibecoding-core | `instructions/vibecoding-core.instructions.md` | ACTIVE | Vibecoding loop, 70% risk, context management |
| vibecoding-extended | `instructions/vibecoding-extended.instructions.md` | ACTIVE | Project guardrails (security, architecture, style) |
| spec-driven | `instructions/spec-driven.instructions.md` | ACTIVE | Spec-driven development rules |
| spec-quality | `instructions/spec-quality.instructions.md` | ACTIVE | Workorder evidence, stable IDs, risks, and assumptions |
| agent-common | `instructions/agent-common.instructions.md` | ACTIVE | Shared evidence, assumption, and context-pruning protocol |
| context-management | `instructions/context-management.instructions.md` | ACTIVE | Hot/warm/cold context loading rules |
| prompt-quality | `instructions/prompt-quality.instructions.md` | ACTIVE | Prompt quality and acceptance-criteria rules |
| python | `instructions/python.instructions.md` | ACTIVE | Python coding standards |
| markdown | `instructions/markdown.instructions.md` | ACTIVE | Markdown formatting standards |
| response-style | `instructions/response-style.instructions.md` | ACTIVE | Communication style rules |
| memory-system | `instructions/memory-system.instructions.md` | ACTIVE | Memory scopes, active context |
| context-engineering | `instructions/context-engineering.instructions.md` | ACTIVE | Context optimization |
| copilot-customization | `instructions/copilot-customization.instructions.md` | ACTIVE | Standards for prompt/agent/instruction files |
| vault-knowledge | `instructions/vault-knowledge.instructions.md` | ACTIVE | Research order, Vault integration |
| wiki-provenance | `instructions/wiki-provenance.instructions.md` | ACTIVE | wiki/ provenance schema |
| prompt-catalog | `instructions/prompt-catalog.instructions.md` | ACTIVE | Catalog of all prompts/agents/skills |
| jira-integration | `instructions/jira-integration.instructions.md` | ACTIVE | Jira MCP server usage |
| confluence-integration | `instructions/confluence-integration.instructions.md` | ACTIVE | Confluence MCP server usage |
| workday-goals | `instructions/workday-goals.instructions.md` | ACTIVE | Goal tracking and alignment |
| template-maintenance | `instructions/template-maintenance.instructions.md` | ACTIVE | Template modification rules for agents |

### Prompts (Layer 1 — Spec-Driven)

| ID | File | Status | Description |
|---|---|---|---|
| repo-bootstrap | `prompts/repo-bootstrap.prompt.md` | ACTIVE | Initialize new repository |
| create-workorder | `prompts/create-workorder.prompt.md` | ACTIVE | Create new workorder |
| create-adr | `prompts/create-adr.prompt.md` | ACTIVE | Create architecture decision |
| pre-implementation-check | `prompts/pre-implementation-check.prompt.md` | ACTIVE | Validate before implementation |
| performance-review | `prompts/performance-review.prompt.md` | ACTIVE | Analyze performance |
| refactoring-plan | `prompts/refactoring-plan.prompt.md` | ACTIVE | Plan refactoring work |
| session-start | `prompts/session-start.prompt.md` | ACTIVE | Load context at session start |
| session-recap | `prompts/session-recap.prompt.md` | ACTIVE | Write session log entry |

### Prompts (Layer 2 — Knowledge & Session)

| ID | File | Status | Description |
|---|---|---|---|
| start | `prompts/start.prompt.md` | ACTIVE | Catalog and onboarding |
| save-session | `prompts/save-session.prompt.md` | ACTIVE | Save session to active-context |
| remember | `prompts/remember.prompt.md` | ACTIVE | Persist learning to memory |
| cognitive-continuity | `prompts/cognitive-continuity-context-transfer.prompt.md` | ACTIVE | Structured session handover |
| wiki-write | `prompts/wiki-write.prompt.md` | ACTIVE | Write wiki snippet |
| wiki-ingest | `prompts/wiki-ingest.prompt.md` | ACTIVE | Ingest source → wiki snippets |
| wiki-lint | `prompts/wiki-lint.prompt.md` | ACTIVE | Wiki health check |
| refresh-docs | `prompts/refresh-docs.prompt.md` | ACTIVE | Validate ARCHITECTURE.md |
| document-review | `prompts/document-review.prompt.md` | ACTIVE | Review document quality |
| document-comparison | `prompts/document-comparison.prompt.md` | ACTIVE | Compare documents, gap analysis |
| requirements-analysis | `prompts/requirements-analysis.prompt.md` | ACTIVE | Analyze requirements |
| meeting-summary | `prompts/meeting-summary.prompt.md` | ACTIVE | Structured meeting summary |
| prompt-to-skill | `prompts/prompt-to-skill.prompt.md` | ACTIVE | Convert prompt to skill |
| jira-review | `prompts/jira-review.prompt.md` | ACTIVE | Review Jira ticket against DoR |
| jira-enhance-to-dor | `prompts/jira-enhance-to-dor.prompt.md` | ACTIVE | Upgrade ticket to DoR |
| ticket-analysis | `prompts/ticket-analysis.prompt.md` | ACTIVE | Analyze ticket completeness |
| strategy-context | `prompts/strategy-context.prompt.md` | ACTIVE | Load strategic context |
| confluence-space-audit | `prompts/confluence-space-audit.prompt.md` | ACTIVE | Audit Confluence space |
| fetch-meeting-transcripts | `prompts/fetch-meeting-transcripts.prompt.md` | ACTIVE | Retrieve meeting transcripts |
| workday-goal-awareness | `prompts/workday-goal-awareness.md` | ACTIVE | Goal alignment awareness |

### Skills

| ID | File | Status | Description |
|---|---|---|---|
| ai-content-check | `skills/ai-content-check/SKILL.md` | ACTIVE | AI text detection, stylometric analysis |
| document-pipeline | `skills/document-pipeline/SKILL.md` | ACTIVE | Document conversion |
| knowledge-retrieval | `skills/knowledge-retrieval/SKILL.md` | ACTIVE | Knowledge from internal systems |
| make-skill-skill | `skills/make-skill-skill/SKILL.md` | ACTIVE | Scaffold new skills |
| schreibstil | `skills/schreibstil/SKILL.md` | ACTIVE | Writing style guide |
| rdf-shacl | `skills/rdf-shacl/SKILL.md` | ACTIVE | RDF/SHACL working skill (example) |
| domain-knowledge-example | `skills/domain-knowledge-example/SKILL.md` | EXAMPLE | Replace with your domain |
| ticket-quality-example | `skills/ticket-quality-example/SKILL.md` | EXAMPLE | Replace with your DoR |

### Schemas

| ID | File | Status | Description |
|---|---|---|---|
| workorder | `schemas/workorder.schema.md` | ACTIVE | Workorder specification format |
| adr | `schemas/adr.schema.md` | ACTIVE | Architecture decision record format |
| report | `schemas/report.schema.md` | ACTIVE | Workorder completion report |
| handoff | `schemas/handoff.schema.md` | ACTIVE | Agent-to-agent handoff format |
| session-log | `schemas/session-log.schema.md` | ACTIVE | Session log entry format |
| user-intent-log | `schemas/user-intent-log.schema.md` | ACTIVE | User intent log format |
| artifact-registry | `schemas/artifact-registry.schema.md` | ACTIVE | Artifact registry structure |

### Python Tools

| ID | Path | Status | Description |
|---|---|---|---|
| validate | `_tools/validate/` | ACTIVE | Frontmatter, terminology, AI-style checks |
| ai_detect | `_tools/ai_detect/` | ACTIVE | AI content detection engine |
| documents | `_tools/documents/` | ACTIVE | Format conversion |
| vault | `_tools/vault/` | ACTIVE | Vault ingestion pipeline |

### Documentation

| ID | Path | Status | Description |
|---|---|---|---|
| setup | `docs/SETUP.md` | ACTIVE | Onboarding guide for new and existing projects |
| template-usage | `docs/TEMPLATE_USAGE.md` | ACTIVE | Usage and maintenance contract for humans and agents |
| workflow-modes | `docs/agent-framework/workflow-modes.md` | ACTIVE | Workflow mode reference |
| workorder-quality-contract | `docs/agent-framework/workorder-quality-contract.md` | ACTIVE | Workorder quality and evidence contract |

### Governance

| ID | Path | Status | Description |
|---|---|---|---|
| project-profile | `governance/project.profile.yaml` | ACTIVE | Repo-specific paths, commands, assumptions, and policy defaults |
| routing-policy | `governance/routing-policy.yaml` | ACTIVE | Workflow mode and agent activation policy |
| policy | `governance/policy.yaml` | ACTIVE | Policy gates for risky actions |

---

## Changelog

| Version | Date | Changes |
|---|---|---|
| Unreleased | 2026-06-16 | Migrated agent framework to slim policy-driven Core Pack with Orchestrator Lite, governance policies, hot context, workflow modes, and Workorder evidence contract |
| Unreleased | 2026-05-24 | Added template usage guide and maintenance instruction for future agents |
| 2.0.0 | 2026-04-20 | Added Knowledge Management, Session Continuity, Validation, AI Detection, Vault, Governance, 5 new agents, 20+ prompts, 8 skills, Python tooling |
| 1.1.0 | 2026-03-03 | Session management protocols, context refresh |
| 1.0.0 | 2026-02-06 | Initial framework (7 agents, 4 instructions, 7 schemas, 8 prompts) |
