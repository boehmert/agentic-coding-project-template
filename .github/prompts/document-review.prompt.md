---
description: "Dokument, Spezifikation oder Anforderung als Review-Partner prüfen und konkrete Verbesserungen vorschlagen."
---

# Document Review Prompt

## Task
Review the document, specification, or requirement provided above in **review partner mode**. Identify issues, provide concrete improvements, and offer objective feedback.

## Context
- This review focuses on clarity, completeness, and compliance with professional standards
- No generic praise; feedback is specific and actionable
- You decide what to accept or revise

## What to Review

### 1. Clarity
- Are terms defined or easily understood?
- Are sentences concise and active voice?
- Are acronyms explained on first use?
- Could a new reader understand the intent?

### 2. Completeness
- Are there gaps or missing information?
- Are assumptions stated explicitly?
- Are edge cases or exceptions covered?
- Is scope clearly bounded?

### 3. Correctness
- Are statements factually accurate?
- Are technical details correct?
- Are references current and valid?
- Are there internal contradictions?

### 4. Consistency
- Is terminology used consistently?
- Are formatting and structure uniform?
- Do examples match descriptions?
- Are related sections aligned?

### 5. Actionability
- Can a reader act on this document?
- Are steps or requirements testable?
- Are success criteria clear?
- Are dependencies identified?

## Output Format

```
## Document Review: [Document Title]

### Summary
[One-sentence overview of document quality and readiness]

### Issues by Severity

#### Critical
- **Issue:** [Specific problem, with location/example]
  - **Impact:** Why this matters
  - **Fix:** Specific, concrete improvement or rewrite

#### Major
- **Issue:** [Specific problem, with location/example]
  - **Impact:** Why this matters
  - **Fix:** Specific, concrete improvement

#### Minor
- **Issue:** [Specific problem, with location/example]
  - **Impact:** Why this matters
  - **Fix:** Specific, concrete improvement or suggestion

### Strengths
- [What's well written or clear]
- [What works well]

### Recommendation
[One of:]
- ✅ Ready to use / publish
- ⚠️ Address critical and major issues before use
- ❌ Significant rework recommended before use
```

## Guidelines

1. **Be specific:** Reference exact sections, lines, or phrases
2. **Provide concrete examples:** Show what's unclear or missing
3. **Suggest fixes:** Rewrite or improve, don't just complain
4. **Focus on impact:** Explain why each issue matters
5. **No generic praise:** Skip "this is well written"; focus on substantive feedback
6. **Be professional:** Assume good intent; frame as improvement, not criticism
7. **Offer alternatives:** When there's a choice, note trade-offs

## Issue Categories

**Critical Issues:**
- Missing essential information
- Contradictions or errors that could cause wrong action
- Ambiguity that could lead to misunderstanding
- Compliance or legal risks

**Major Issues:**
- Important information unclear or hard to find
- Scope not well defined
- Dependencies or assumptions unstated
- Steps not testable or measurable

**Minor Issues:**
- Typos or formatting inconsistencies
- Terminology could be clearer
- Examples could be added
- Structure could flow better

## Example Output

```
## Document Review: Q2 Release Plan

### Summary
Plan covers all major milestones and feature areas, but lacks testable success criteria and assumes reader familiarity with internal project structure. Address critical issues before sharing with external partners.

### Issues by Severity

#### Critical
- **Issue:** Success criteria for "improve performance" (Phase 2) are not measurable. Currently states "system should feel faster."
  - **Impact:** Team cannot validate completion; stakeholders cannot assess progress
  - **Fix:** Replace with specific metrics: "Reduce page load time from 3.2s to <1.5s (P95, 10K concurrent users on prod)"

- **Issue:** Section 3.2 references "SMART goals framework" but framework is not defined anywhere in document.
  - **Impact:** Readers outside the organization won't understand what "SMART" means or how it applies
  - **Fix:** Add one-sentence definition: "SMART goals are Specific, Measurable, Achievable, Relevant, Time-bound. See [link] for details."

#### Major
- **Issue:** Phase 2 timeline says "Q2" but lists specific dates (April 3 - May 15) that overlap into June. Inconsistency about whether this is Q2 only.
  - **Impact:** Stakeholders unsure of actual end date; may impact budgeting and resource planning
  - **Fix:** Choose one: either "Q2 (through June 15)" or specific dates, and be consistent throughout

- **Issue:** Dependencies section lists "requires design approval" but doesn't identify who approves or expected timeline.
  - **Impact:** Team can't plan when this dependency will be resolved
  - **Fix:** Add: "Design approval required (owned by [person], typically 2-week review cycle)"

- **Issue:** Document mentions "V1" and "V2" releases but never defines the difference or which features are in scope for each.
  - **Impact:** Readers confused about what's included in each release
  - **Fix:** Add brief table or definition (e.g., "V1 = core search feature; V2 = advanced filters and saved searches")

#### Minor
- **Issue:** Heading "Risk Mitigation" on page 4, but next section "Risks and Mitigations" on page 7. Use consistent terminology.
  - **Impact:** Minor readability issue
  - **Fix:** Choose one heading style and apply consistently

- **Issue:** Example in Phase 1 uses fictional stakeholder name "Bob" but should reference the actual stakeholder role instead.
  - **Impact:** Confusing for real team; Bob may not be involved
  - **Fix:** Replace "Bob approves" with "Product Manager approves"

### Strengths
- Timeline with specific dates is clear and easy to scan
- Feature breakdown by phase is logical and well-organized
- Risk section shows thoughtful planning

### Recommendation
⚠️ Address critical and major issues before sharing with stakeholders.
- Add measurable success criteria (Critical)
- Define internal terms and acronyms (Critical)
- Clarify timeline inconsistency (Major)
- Identify dependency owners and timelines (Major)

After fixes, this will be a solid communication document.
```

---

## How to Use This Review

1. **Read through all issues** in order of severity
2. **Decide what to fix** — not all feedback requires action (it's suggestions, not requirements)
3. **Rewrite sections** as needed
4. **Share revised version** for follow-up review if desired
5. **Integrate changes** into your document

---

**Ready?** Paste your document above this prompt and I'll review it.

