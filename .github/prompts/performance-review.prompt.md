---
description: "Analyze code for performance issues and optimization opportunities"
tools:
  - "codebase"
  - "search"
  - "runCommands"
  - "problems"
---

# Performance Review

This prompt guides a performance analysis of code or a specific feature.

---

## Scope

- **Target**: ${input:target:Module, function, or feature to analyze}
- **Concern**: ${input:concern:Specific performance concern, if any}

---

## Analysis Areas

### 1. Algorithmic Complexity

| Area | Check |
|------|-------|
| Loop complexity | Nested loops, O(n²) or worse |
| Data structure choice | Appropriate for use case |
| Search/sort efficiency | Using optimal algorithms |
| Memory allocation | Unnecessary allocations |

### 2. I/O Operations

| Area | Check |
|------|-------|
| Database queries | N+1 problems, missing indexes |
| File operations | Buffering, streaming |
| Network calls | Batching, caching |
| Serialization | Efficient formats |

### 3. Caching Opportunities

| Area | Check |
|------|-------|
| Repeated calculations | Memoization candidates |
| Expensive queries | Result caching |
| Static data | Precomputation |

### 4. Resource Usage

| Area | Check |
|------|-------|
| Memory consumption | Large objects, leaks |
| Connection pooling | Database, HTTP |
| Thread/process usage | Concurrency patterns |

---

## Output Format

```markdown
## Performance Review: ${target}

**Date:** {date}
**Reviewer:** reviewer

### Summary
Brief overview of performance posture.

### Findings

#### 🔴 Critical (High Impact)
1. **Issue description**
   - Location: `file.py:45`
   - Current: O(n²) nested loop
   - Impact: 10x slowdown at scale
   - Recommendation: Use hash map lookup
   ```python
   # Current
   for item in items:
       for other in others:
           if item.id == other.id:
               ...
   
   # Recommended
   other_map = {o.id: o for o in others}
   for item in items:
       if item.id in other_map:
           ...
   ```

#### 🟡 Medium (Should Address)
1. **Issue description**
   - Location: ...
   - Impact: ...
   - Recommendation: ...

#### 💡 Optimization Opportunities
1. **Opportunity description**
   - Potential gain: ...
   - Implementation effort: ...

### Benchmarks (if applicable)
| Operation | Current | Target | Notes |
|-----------|---------|--------|-------|
| ... | ... | ... | ... |

### Recommendations
1. Priority action 1
2. Priority action 2
3. Priority action 3

### Follow-up
- [ ] Create Workorder for critical fixes
- [ ] Add performance tests
- [ ] Set up monitoring
```

---

## Common Patterns

### Python-Specific

```python
# ❌ Slow: String concatenation in loop
result = ""
for item in items:
    result += str(item)

# ✅ Fast: Join
result = "".join(str(item) for item in items)
```

```python
# ❌ Slow: List for membership test
if item in large_list:  # O(n)

# ✅ Fast: Set for membership
if item in large_set:  # O(1)
```

```python
# ❌ Slow: Multiple database queries
for user_id in user_ids:
    user = db.get_user(user_id)

# ✅ Fast: Batch query
users = db.get_users(user_ids)
```

---

## Workflow

1. I will read the target code
2. I will analyze for common performance issues
3. I will identify optimization opportunities
4. I will provide specific, actionable recommendations
5. I will suggest benchmarking approaches

---

## Let's Start

Please specify what you'd like me to analyze for performance.
