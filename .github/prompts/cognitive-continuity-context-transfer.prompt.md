---
description: "Strukturiertes Kontext-Transfer-Artefakt (CCCTP v1.3) für Session-Handover erstellen — Entscheidungslogik, Artefakte, Risiken."
---

# Cognitive Continuity & Context Transfer Prompt (CCCTP) v1.3

*Master Edition — Context · Consistency · Continuity · Governance*

---

## Role

You are creating a Cognitive Continuity & Context Transfer Artifact.

This is:

- **not** a transcript
- **not** a summary
- **not** a raw memory dump

This is a structured, validated, migration-grade knowledge document.

**Primary objective:** Preserve context, decision logic, working models, artifacts, collaboration patterns, risk areas, measurable quality indicators, and transfer stability so that a successor LLM can seamlessly continue the work.

Brevity is **not** a goal. Structural clarity, completeness, and transfer robustness are.

---

## Global operating principles

- Do not invent information.
- Clearly separate: explicit evidence vs. inferred implicit patterns (label the latter explicitly).
- Prefer hierarchical synthesis over flat listing.
- Preserve verbatim wording where strategically relevant.
- Use the EXACT scoring rubric provided.
- Do not omit phases.
- Perform internal validation before output.
- Do not assume scope — it must be selected explicitly.

---

## Scope selection (mandatory before execution)

| Option | Scope | Depth | Strategic value | Transferability |
|:---:|---|:---:|---|---|
| 1 | Single Topic | 🔹 | Low–Medium | Platform-specific only |
| 2 | Single Session | 🔹🔹 | Medium | Session-bound |
| 3 | Multi-Session / Thematic Cluster | 🔹🔹🔹 | High | Decision model transferable |
| 4 | Full Interaction History | 🔹🔹🔹🔹 | Very High | Generically transferable |

- Option 1 → Focused documentation
- Option 2 → Session-level continuity
- Option 3 → Structural decision logic extraction
- Option 4 → Cognitive system modeling

The user must explicitly choose 1–4. Do **not** assume scope.

### Score stability mapping

| Scope | Stability |
|:---:|---|
| 1 | Low |
| 2 | Medium |
| 3 | High |
| 4 | Very High |

Include in the output frontmatter:

```yaml
analysis_scope: "1|2|3|4"
score_stability: "low|medium|high|very_high"
```

> [!WARNING]
> For scope 1 or 2: scores may not represent stable cognitive patterns.

---

## Workflow (mandatory)

Follow all phases in order. Internal reasoning must **not** be output.

---

### Phase 0 — Structured planning (internal only)

Before extraction:

**Identify extraction domains:**
- Explicit memory
- Implicit patterns
- Project clusters
- Artifact inventory
- Collaboration dynamics
- Risk vectors

**Identify blind spots:**
- Long threads
- Repeated revisions
- Terminology drift
- Scope shifts

**Define synthesis logic:**
- Clustering criteria
- Definition of "decision heuristic"
- Definition of "iteration loop"

Do **not** output this plan.

---

### Phase 1 — Exhaustive context extraction

#### A. Explicit stored memory

- User instructions (tone, format, always/never)
- Personal/work context
- Tools and frameworks
- Goals and projects
- Corrections to assistant behavior

#### B. Implicit patterns (label as implicit)

Identify with examples:

- Recurring question archetypes
- Recurring critique patterns
- Frustration markers (language + trigger)
- Decision logic patterns
- Evaluation criteria
- Abstraction preferences
- Iteration behavior
- Trade-off patterns
- Meta-reasoning habits

#### C. Thematic & project evolution

- Topic clusters
- Active threads
- Closed threads
- Abandoned directions
- Strategic shifts
- Tested & rejected hypotheses

#### D. Artifact & output inventory

For **each** artifact include:

- Description
- Status (active / evolving / paused / abandoned)
- Strategic relevance
- Dependencies
- Quality threshold (if observable)
- Risk of context loss

---

### Phase 2 — Three-level synthesis

#### 1. Working model of the person

- Cognitive style
- Decision logic
- Evaluation framework
- Prompting maturity
- Frustration patterns
- Value system
- Strengths
- Recurrent gaps
- Evolution trajectory (if visible)

#### 2. Working model of the projects

- Strategic objectives
- Systems & architectures
- Models & frameworks
- Evolution narrative
- Artifact map
- Dependencies
- Constraints

#### 3. Working model of the collaboration

- Iteration patterns
- Feedback mechanics
- Correction typology
- Quality threshold model
- Escalation triggers
- "How to work with this user" playbook

---

### Phase 3 — Structural synthesis

- Cluster thematically
- Remove redundancy
- Surface implicit assumptions
- Extract decision heuristics
- Identify strategic tensions
- Label inference confidence (high / medium / low)

---

### Phase 4 — Cognitive risk map (mandatory)

#### A. Frequent context loss areas

- Where context drops
- Why
- Symptoms
- Mitigation strategies

#### B. Recurring misunderstandings

- Categories
- Root causes
- Prevention mechanisms

#### C. Iteration loops

- Topics repeatedly revised
- Structural cause
- Loop-breaking strategies

---

### Phase 5 — Standardized scoring (cross-chat comparable)

Use the EXACT rubric.

#### Prompting Quality Index (PQI)

Dimensions (0–5):

- Goal clarity
- Context completeness
- Structural guidance
- Iteration guidance
- Operationalizability
- Meta-layer explicitness
- Transfer awareness

#### Cognitive Structure Score (CSS)

- Hierarchical thinking
- Model-building tendency
- Cross-iteration consistency
- Abstraction control
- Synthesis capability

#### Iteration Efficiency Score (IES)

- Precision of corrections
- Ambiguity reduction
- Improvement-per-iteration
- Loop-breaking behavior

#### Frustration Signal Index (FSI)

- Frequency
- Intensity
- Recurrence around same triggers
- Escalation trend

**Scoring formula:**

```
(sum of dimension scores / (5 × number_of_dimensions)) × 100
```

Round to nearest integer.

For each index include: score, subscores, evidence-based justification, confidence level.

---

### Phase 6 — Red-team & gap analysis (internal)

Internally test:

- What might a successor LLM misinterpret?
- Which assumptions remain implicit?
- Which artifacts lack clarity?
- Where is ambiguity?

Integrate fixes.

---

### Phase 7 — Self-validation (internal)

Confirm:

- [ ] All explicit memory included
- [ ] Major implicit patterns surfaced
- [ ] Cognitive risk map actionable
- [ ] Scores follow rubric exactly
- [ ] Structure complete
- [ ] No critical omissions

Only then finalize.

---

## Output requirements

Produce ONE standalone Markdown document containing:

1. YAML frontmatter
2. Full structured document
3. Filename recommendation

No commentary outside the file.

---

## File naming & generation (mandatory)

### Pattern

```
YYYY-MM-DD__chat-slug__origin-model__cognitive-continuity__v1.3.md
```

**Rules:**

- ISO date format
- Lowercase only
- Hyphen-separated slug
- No special characters
- No double hyphens
- Include version number

**Slug normalization:**

- Spaces → hyphens
- Remove accents/umlauts
- Remove special characters
- Lowercase only

Validate filename before saving.

### Generation requirements

After validation:

1. Generate UTF-8 encoded `.md` file
2. Save under validated filename
3. File must contain: YAML frontmatter + full document body

Output only: exact filename and download link.

On failure: retry once. If still failing, state the technical reason.

If file-writing is unavailable: return Markdown inside a single code block.

---

## Output frontmatter template

```yaml
---
title: ""
date: ""
origin_model: ""
analysis_scope: ""
score_stability: ""
session_summary: ""
---
```

## Output document structure

1. Executive Context
2. Working Model of the Person
3. Working Model of the Projects
4. Working Model of the Collaboration
5. Thematic Synthesis
6. Cognitive Risk Map
7. Standardized Scores
8. Open Threads & Next Steps
9. Transfer Risk Assessment
10. Transfer Readiness Score
Executive Context\
Working Model of the Person\
Working Model of the Projects\
Working Model of the Collaboration\
Thematic Synthesis\
Cognitive Risk Map\
Standardized Scores\
Open Threads & Next Steps\
Transfer Risk Assessment\
Transfer Readiness Score
END OF CCCTP v1.3
