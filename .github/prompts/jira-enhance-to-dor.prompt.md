---
description: "Unvollständiges Jira-Ticket auf DoR-Niveau bringen: Scope trennen, Annahmen markieren, testbare ACs."
---

# Jira Enhance-to-DoR Prompt

## Task
Enhance the Jira ticket provided above to meet your team's Definition of Ready. Rewrite and complete the ticket, maintaining scope but ensuring it is ready for development.

## Context
- Our Definition of Ready is in `docs/Definition_of_Ready.md`
- Our Jira template is in `docs/Jira_Template.md`
- Examples of compliant tickets are in `examples/sample-ticket-good.md`

## Key Principles

### 1. Keep Scope Tight
- Do NOT expand the ticket scope
- Do NOT combine multiple features
- Focus on ONE clear deliverable
- If scope creep is needed, recommend a separate ticket

### 2. Separate Requirement from Solution
- **Requirement:** What does the user need? Why?
- **Solution:** How might we solve it? (implementation ideas, not specs)
- Keep requirements in main ticket; suggestions in comments or subtasks

### 3. Mark Assumptions Explicitly
Every assumption should be visible:
```
// Assumption: [clear statement]
// Rationale: [why we're making this assumption]
// Risk: [what could go wrong]
// Mitigation: [how to validate or handle the risk]
```

## What to Enhance

### 1. Summary/Title
- Make it concise and user-focused
- Start with user role or action (e.g., "As a user, I can...")
- Remove jargon and internal implementation terms

### 2. Description
- Add or improve: **What** (clear problem/need)
- Add or improve: **Why** (business value, user benefit)
- Add or improve: **Context** (background, related work)
- Link to related tickets or docs where relevant

### 3. Acceptance Criteria (AC)
- Make each criterion **testable** and **measurable**
- Use Gherkin format if helpful: "Given... When... Then..."
- Cover **happy path** AND **edge cases**
- Ensure criteria are **independent** (one per line, one concept per criterion)

**Good AC:** "Search returns results within 2 seconds on Chrome 120+ with up to 10,000 items in the database"  
**Bad AC:** "Search should work"

### 4. Identify Dependencies
- What other work must be done first?
- What teams or services are affected?
- Are there data or integration dependencies?

### 5. Add Assumptions Section
For each assumption:
```
// Assumption: [statement]
// Rationale: [why]
// Risk: [impact if wrong]
// Mitigation: [how to validate/handle]
```

### 6. Improve Clarity
- Remove ambiguous pronouns
- Clarify acronyms
- Add concrete examples where relevant
- Remove implementation details (save for tech specs)

## Output Format

```
## Enhanced Ticket

### Title
[Improved, user-focused title]

### Type
[Issue type: Story, Task, Bug, etc.]

### Description

#### What
[Clear, user-centric problem or need statement]

#### Why
[Business value and user benefit]

#### Context
[Background, related work, references]

### Acceptance Criteria

- [ ] AC1: [Testable, measurable criterion]
- [ ] AC2: [Testable, measurable criterion]
- [ ] AC3: [Edge case or validation criterion]
- [ ] AC4: [Additional edge case or requirement]

### Dependencies
- [List of blocking or dependent work]

### Assumptions

// Assumption: [Statement]
// Rationale: [Why we're making this assumption]
// Risk: [What could go wrong if this is false]
// Mitigation: [How to validate or handle the risk]

[Repeat for each assumption]

### Notes for Implementation
[Optional: Brief pointers or suggestions, but NOT implementation spec]
```

## Guidelines

1. **Be explicit:** Every assumption, dependency, and edge case should be visible
2. **Be testable:** Every AC should be checkable by QA without interpretation
3. **Be concise:** Use short sentences and bullet points
4. **Be user-centric:** Frame requirements from user perspective, not implementation
5. **Preserve intent:** Don't change what the ticket is trying to achieve
6. **Scope lock:** If you discover missing scope, note it in "Notes" as a potential follow-up ticket, don't expand the current one

## Example Output

```
## Enhanced Ticket

### Title
Users can search open tickets by ID to find and track issues faster

### Type
Story

### Description

#### What
Currently, users cannot filter or search the ticket list by ticket ID. This forces them to scroll through potentially hundreds of tickets or use browser find, which is slow and error-prone.

#### Why
Searching by ticket ID is a core user workflow. Customers often have ticket IDs from emails or support conversations and need to locate those tickets quickly. This reduces support time and improves user satisfaction.

#### Context
The ticket system currently supports filtering by status and assignee, but not by ID. This is the most-requested feature from recent user interviews (3 of 5 users mentioned it).

### Acceptance Criteria

- [ ] User can enter a ticket ID in a search field on the ticket list view
- [ ] Search returns exact-match ticket or "no results found" message within 2 seconds
- [ ] Search works for all ticket ID formats (PROJ-1234, PROJ-12345)
- [ ] Search is case-insensitive and handles whitespace (e.g., "PROJ- 1234")
- [ ] Empty search field shows all tickets (no filtering)
- [ ] Special characters in search field are handled gracefully (no errors)
- [ ] Search field is accessible by keyboard (Tab, Enter)
- [ ] "Not found" message is clear and user-friendly

### Dependencies
- None identified; feature is independent

### Assumptions

// Assumption: Search is exact-match (ID "PROJ-1234" does not return "PROJ-12345")
// Rationale: Most users search for a specific ticket; fuzzy matching adds complexity
// Risk: Users may be confused if close matches appear
// Mitigation: Add help text: "Enter full ticket ID to search"

// Assumption: Search results update in real-time (no separate search button)
// Rationale: Modern UX patterns use live search; faster user experience
// Risk: Server load if many users search simultaneously
// Mitigation: Implement debouncing (300ms delay) and cache common searches

### Notes for Implementation
Consider implementing server-side search with database indexing on ticket ID for performance.
Frontend should debounce input to reduce server requests.
```

---

**Ready?** Paste your Jira ticket above this prompt and I'll enhance it to meet DoR.

