---
name: domain-knowledge-example
description: >
  Example skill: Domain-specific knowledge, terminology, architecture patterns
  and modeling principles. Replace with your own domain.
  Activated when domain-specific terms, architecture, or modeling questions arise.
---

# Domain Knowledge (Example)

> **This is an example skill.** Replace the content below with your project's domain knowledge.
> See `make-skill-skill` for how to create new skills from scratch.

## 1. Overview

This skill provides domain-specific context to the AI assistant. It covers:
- Component landscape and system boundaries
- Terminology and canonical naming
- Architecture patterns and integration points
- Modeling principles and data structures

## 2. Components (Example)

| Component | Purpose | Technology |
|---|---|---|
| Frontend App | User-facing UI | React / Angular |
| API Gateway | Request routing, auth | Node.js / Kong |
| Core Service | Business logic | Python / Java |
| Data Pipeline | ETL and transformation | Python / Spark |
| Knowledge Base | Semantic data store | RDF / Graph DB |

## 3. Terminology (Example)

| Term | Definition | Avoid |
|---|---|---|
| Entity | A uniquely identifiable domain object | "item", "thing", "record" |
| Pipeline | A multi-step data transformation flow | "process", "job" |
| Validation Rule | A constraint applied to incoming data | "check" |

## 4. Architecture Patterns

- **Event-driven**: Components communicate via events, not direct calls
- **Pipeline pattern**: Data flows through ordered transformation stages
- **Schema-first**: All data structures defined by schemas before implementation

## 5. When to Use This Skill

Activate when the user:
- Asks about domain-specific components or terminology
- Needs to understand system boundaries
- Is writing code that touches domain models
- Needs to validate data against domain rules


