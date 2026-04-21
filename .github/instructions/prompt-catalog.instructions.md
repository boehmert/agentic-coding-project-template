---
description: "Katalog aller verfügbaren Prompts, Agents und Skills im Workspace."
applyTo: "**"
priority: optional
---

# Prompt, Agent & Skill Katalog

Übersicht aller Copilot-Erweiterungen in diesem Workspace. Für Qualitätsstandards der Dateien selbst siehe `copilot-customization.instructions.md`.

---

## 1. Prompts (`.github/prompts/`)

Aufruf via `/name` im Chat.

| Prompt | Zweck |
|---|---|
| `/jira-review` | Jira-Ticket gegen DoR-Checkliste und Team-Template prüfen |
| `/jira-enhance-to-dor` | Unvollständiges Jira-Ticket auf DoR-Niveau bringen |
| `/document-review` | Dokument/Spezifikation als Review-Partner prüfen |
| `/document-comparison` | Zwei Dokumente/Versionen vergleichen, Gap-Analyse erstellen |
| `/requirements-analysis` | Anforderungen auf Vollständigkeit, Testbarkeit, Klarheit prüfen |
| `/meeting-summary` | Strukturierte Meeting-Zusammenfassung erstellen |
| `/create-workorder` | Neue Workorder-Spezifikation erstellen (interaktiver Wizard) |
| `/wiki-write` | Wissens-Snippet aus Session in wiki/ zurückschreiben |
| `/wiki-ingest` | Quelldatei aus inbox/ destillieren → wiki/-Snippets |
| `/wiki-lint` | Health-Check für wiki/ |
| `/save-session` | Session-Ergebnisse + Denkprozess für nächste Session speichern |
| `/start` | Alle verfügbaren Prompts, Skills und Instructions als Katalog anzeigen |
| `/remember` | Einzelnes Learning persistent als Memory speichern |
| `/cognitive-continuity-context-transfer` | Strukturiertes Kontext-Transfer-Artefakt (CCCTP) für Session-Handover |
| `/refresh-docs` | ARCHITECTURE.md und copilot-instructions.md gegen Workspace prüfen, Updates vorschlagen |
| `/integrate-framework` | Einmalig nach Framework-Import: Agenten-Konflikte auflösen, COPILOT.md konfigurieren, VS Code einrichten |

---

## 2. Agents (`.github/agents/`)

Aufruf via `@name` im Chat. Vollständiger Katalog: siehe `AGENTS.md`.

### Tier 1 — Orchestration

| Agent | Rolle |
|---|---|
| `@Orchestrator` | Einstiegspunkt für neue Features, Sprint-Start, Cross-Domain-Analyse |
| `@Lead Coordinator` | Cross-domain-Synthese, Konfliktauflösung, Confidence Scoring |

### Tier 2 — Planning & Quality

| Agent | Rolle |
|---|---|
| `@Project Planner` | Roadmap, Meilensteine, Sprint-Planung |
| `@critical-thinker` | Hinterfragt Annahmen, deckt blinde Flecken auf — schreibt keinen Code |
| `@doublecheck` | Prüft AI-Outputs auf Faktengenauigkeit, flaggt Risiken |

### Tier 3 — Execution Layer (Personas)

| Agent | Persona | Rolle |
|---|---|---|
| `@Lisa – Workorder Planner` | **Lisa** | Workorders erstellen/verfeinern, Scope definieren, WO_CATALOG |
| `@Robin – Execution Architect` | **Robin** | Architektur-Entscheidungen in Modul-Struktur übersetzen, ADRs |
| `@Lena – Python Developer` | **Lena** | Approved Workorders implementieren, Tests schreiben |
| `@Marco – Code Reviewer` | **Marco** | Pre/Post-Implementation Gate, GREEN/YELLOW/RED |
| `@Chris – Security Reviewer` | **Chris** | Code-Level Security Review, OWASP, Fix-Verifikation |
| `@Jana – Integrator` | **Jana** | Branches mergen, CI verifizieren, PRs |
| `@Finn – Technical Writer` | **Finn** | README, Docstrings, WO-Reports, Wiki-Snippets |

### Tier 4 — Analysis Layer (Domain-Expert Personas)

| Agent | Domäne |
|---|---|
| `@Arne – Product Owner` | Produkt-Strategie, Roadmap, Monetarisierung |
| `@Tom – Growth & Marketing` | Wachstum, Akquise, Retention |
| `@David – Customer Success` | Onboarding, Activation, Churn |
| `@Sophie – UX/UI Designer` | UX/UI, Onboarding-Flows, Permission-UX |
| `@Mia – Content Strategist` | UX Writing, Content-Strategie, Plain Language |
| `@Elena – AI/ML Engineer` | LLM-Architektur, RAG, AI-Evaluation |
| `@Max – Software Architect` | Architektur-Entscheidungen, ADRs, API-Design |
| `@Felix – DevOps & Platform` | Infrastruktur, CI/CD, SRE, EU Data Residency |
| `@Sam – iOS Developer` | Swift/SwiftUI, App Store, StoreKit |
| `@Kai – Data Analyst` | Analytics, Metriken, A/B-Testing |
| `@Jochen – Legal Advisor` | EU AI Act, DSGVO, Produkthaftung |
| `@Nadia – Privacy Architect & CISO` | Privacy-by-Design, Threat Modeling, OAuth |

---

## 3. Skills (`.github/skills/`)

Werden automatisch oder per Agent aktiviert.

| Skill | Zweck |
|---|---|
| `knowledge-retrieval` | Wissen aus Confluence, Jira, SharePoint, Vault abrufen |
| `schreibstil` | Schreibstil-Guide — eliminiert KI-Muster, erzeugt direkte Sprache |
| `rdf-shacl` | RDF/SHACL-Arbeits-Skill: Formate, Shape-Syntax, Workspace-Tools |
| `document-pipeline` | Dokumenten-Konvertierung: Word/PDF/Excel/PPTX/HTML → Markdown |
| `ai-content-check` | KI-Text-Erkennung: Stylometrische Analyse, Modell-Attribution |

---

## 4. Instructions (`.github/instructions/`)

Werden automatisch per `applyTo`-Pattern aktiviert.

| Instruction | Zweck | Scope |
|---|---|---|
| `vibecoding-core` | Vibecoding-Loop, 70%-Risiko, Context-Management | `**` |
| `vibecoding-extended` | Projekt-Guardrails: Security, Architektur, Code-Qualität, Tests | `**` |
| `context-engineering` | Context-Optimierung für Copilot | `**` |
| `copilot-customization` | Standards für .prompt.md, .agent.md, .instructions.md | Copilot-Dateien |
| `markdown` | Markdown-Standards | `**/*.md` |
| `memory-system` | Memory-Scopes, Active Context, Session-Workflow | `**` |
| `prompt-catalog` | Dieser Katalog | `**` |
| `python` | Python-Konventionen | `**/*.py` |
| `response-style` | Kommunikation, Sprache, Severity Levels | `**` |
| `spec-driven` | Workorder/ADR-Lifecycle | `**` |
| `vault-knowledge` | Recherche-Reihenfolge, Vault, wiki/ | `**` |
| `wiki-provenance` | wiki/-Provenance-Schema | `wiki/**` |

