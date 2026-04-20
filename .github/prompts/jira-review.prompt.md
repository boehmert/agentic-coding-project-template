---
description: "Jira-Ticket gegen DoR-Checkliste und Team-Template prüfen, strukturierte Bewertung liefern."
---

# Jira Review Prompt

## Task
Review the Jira ticket provided above against our team's template and Definition of Ready (DoR) checklist. Provide a structured assessment of compliance.

## Context
- Our Jira template is in `docs/Jira_Template.md`
- Our Definition of Ready is in `docs/Definition_of_Ready.md`
- Examples of compliant tickets are in `examples/sample-ticket-good.md`

## What to Check

### 1. Template Compliance
For each mandatory field in our Jira template:
- ✅ Is it present?
- ✅ Is it complete?
- ✅ Is the content clear and professional?
- ❌ If missing or unclear, note it

### 2. Definition of Ready Checklist
For each criterion in our DoR:
- ✅ Does the ticket meet this criterion?
- ⚠️ Is it partially met?
- ❌ Is it missing?

Use this format:
```
// DoR Checklist
- [x] Criterion name: Clear statement of compliance
- [ ] Criterion name: Missing or incomplete (note why)
- [⚠️] Criterion name: Partially met (note what's missing)
```

### 3. Findings
Identify:
- **Critical gaps** (ticket cannot start without fixing)
- **Major issues** (should be addressed before development)
- **Minor issues** (nice-to-have improvements)
- **Strengths** (what's well done)

Use this format:
```
// Findings

#### Critical
- Issue: Description
  Recommendation: How to fix

#### Major
- Issue: Description
  Recommendation: How to fix

#### Minor
- Issue: Description
  Recommendation: How to fix

#### Strengths
- What's working well
```

## Output Format

```
## Jira Review: [Ticket ID]

### Template Compliance
[Summary of how well the ticket follows your template]

### Definition of Ready Checklist
// DoR Checklist
- [status] Item name: Comment

[Repeat for all DoR items]

### Findings

#### Critical
[Critical issues and fixes]

#### Major
[Major issues and fixes]

#### Minor
[Minor improvements]

#### Strengths
[What's well done]

### Recommendation
[One of:]
- ✅ Ready for development (all critical and major issues resolved)
- ⚠️ Needs revision before development (list key fixes required)
- ❌ Not ready (major work required before team review)
```

## Guidelines

1. **Be specific:** Reference field names from template; cite DoR criteria
2. **Be constructive:** Frame issues as opportunities, not failures
3. **Be objective:** Focus on compliance, not opinion
4. **Be actionable:** Suggest specific fixes for each issue
5. **Be concise:** Use bullet points and short statements

## Example Output

```
## Jira Review: PROJ-2451

### Template Compliance
Ticket includes all mandatory fields (Title, Description, Acceptance Criteria, Type). 
Acceptance Criteria are present but lack detail and testability.

### Definition of Ready Checklist
// DoR Checklist
- [x] Clear, one-line summary: "User can search by ticket ID"
- [x] Business value stated: "Reduces time to find open issues"
- [ ] Acceptance Criteria testable: Criteria exist but are not measurable
- [x] Dependencies identified: None listed (appears independent)

### Findings

#### Critical
- Issue: Acceptance Criteria are vague ("should work in Chrome")
  Recommendation: Replace with measurable criteria (e.g., "Search returns results within 2 seconds on Chrome 120+")

#### Major
- Issue: No mention of edge cases (empty search, special characters)
  Recommendation: Add acceptance criteria for at least 3 edge cases

#### Minor
- Issue: Type is "Task" but could be "Story" for user-facing feature
  Recommendation: Consider if this aligns with team's type definitions

#### Strengths
- Business value is clear and compelling
- Dependencies are well identified

### Recommendation
⚠️ Needs revision before development.
Fix critical acceptance criteria to be measurable, then resubmit.
```

---

**Ready?** Paste your Jira ticket above this prompt and I'll review it.

