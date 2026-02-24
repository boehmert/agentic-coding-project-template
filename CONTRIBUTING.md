# Contributing to Spec-Driven Development Framework

Thank you for your interest in improving this framework! This document provides guidelines for contributing.

## 🎯 Ways to Contribute

- **Report bugs** – Found an issue? Open a GitHub Issue
- **Suggest features** – Ideas for improvements? Start a Discussion
- **Improve documentation** – Fix typos, clarify instructions, add examples
- **Share experiences** – Post your success stories or challenges in Discussions
- **Submit bug fixes** – PRs for clear bug fixes are welcome
- **Propose enhancements** – Larger changes should be discussed first

## 🔍 Before You Start

1. **Check existing issues** – Someone may already be working on it
2. **Review documentation** – Especially [documentation/](documentation/)
3. **Understand the framework** – Read [00_Framework_Overview.md](documentation/00_Framework_Overview.md)

## 📝 How to Contribute

### Reporting Bugs

**Use the Issue template and include:**
- Clear description of the problem
- Framework version (from [FRAMEWORK_MANIFEST.md](.github/FRAMEWORK_MANIFEST.md))
- Steps to reproduce
- Expected vs. actual behavior
- Your environment (OS, AI assistant used)
- Screenshots or error messages

**Example:**
```
**Bug:** Workorder schema validation fails on optional fields

**Version:** 1.0.0
**Environment:** Windows 11, GitHub Copilot
**Steps:**
1. Create workorder with empty `depends_on` field
2. Run pre-implementation check
3. Validation error appears

**Expected:** Empty array should be valid
**Actual:** "Field required" error
```

### Suggesting Features

**Start a GitHub Discussion first:**
- Describe the use case
- Explain why it's valuable
- Consider alternative solutions
- Discuss trade-offs

**Good feature suggestions:**
- Solve real problems you've encountered
- Align with framework principles (spec-driven, quality gates)
- Are well-scoped and implementable
- Don't break existing functionality

### Submitting Pull Requests

#### 1. Small Fixes (Typos, Docs)
- Fork the repo or create a branch
- Make your changes
- Submit PR with clear description
- Reference related issues

#### 2. Feature Implementations
**Follow the framework's own process:**

1. **Create a Workorder** (in your fork)
   ```
   @workspace /prompt create-workorder
   
   Task: Add support for custom agent templates
   Context: Users want to create organization-specific agent variants
   ```

2. **Get feedback** – Post your Workorder in Discussions

3. **Pre-implementation check** – Use the reviewer agent

4. **Implement** – Follow coding standards

5. **Test** – Validate against acceptance criteria

6. **Create report** – Document what was done

7. **Submit PR** – Include Workorder ID in PR description

## 📐 Coding Standards

### Markdown Files
Follow [.github/instructions/markdown.instructions.md](.github/instructions/markdown.instructions.md):
- Use ATX-style headings (`##` not `---`)
- Fenced code blocks with language tags
- Consistent formatting
- No trailing whitespace

### Python (if applicable)
Follow [.github/instructions/python.instructions.md](.github/instructions/python.instructions.md):
- PEP 8 compliance
- Type hints
- Docstrings for public functions
- Unit tests for new functionality

### Schema Files
- Maintain backward compatibility
- Version updates follow semantic versioning
- Update FRAMEWORK_MANIFEST.md

### Agent Definitions
- Clear role definitions
- Specific responsibilities
- Non-overlapping duties
- Practical examples

## 🔄 Pull Request Process

### PR Title Format
```
[Type] Brief description

Types:
- [Docs] – Documentation only
- [Fix] – Bug fix
- [Feature] – New feature
- [Schema] – Schema changes
- [Agent] – Agent definition changes
```

### PR Description Template
```markdown
## Summary
What does this PR do?

## Motivation
Why is this change needed?

## Changes
- Bullet list of changes

## Related
- Closes #123
- Related to WO05

## Testing
How was this tested?

## Checklist
- [ ] Follows coding standards
- [ ] Documentation updated
- [ ] FRAMEWORK_MANIFEST.md updated (if applicable)
- [ ] No breaking changes (or clearly documented)
```

### Review Process
1. Automated checks must pass
2. At least one maintainer review required
3. Address feedback professionally
4. Squash commits before merge (if requested)

## 🏗️ Architecture Decisions

**For significant architectural changes:**
- Create an ADR (Architecture Decision Record)
- Follow [schemas/adr.schema.md](.github/schemas/adr.schema.md)
- Discuss in PR before implementation
- Document trade-offs and alternatives

## 🧪 Testing Requirements

### For Framework Changes
- Test with multiple AI assistants (Copilot, Cursor, Claude)
- Validate on different OS (Windows, macOS, Linux)
- Check backward compatibility
- Test installation scripts

### For Documentation
- Links work correctly
- Examples are accurate
- Instructions are clear
- Markdown renders properly

## 📚 Documentation Guidelines

### When to Update Docs
- New features → Update relevant guides
- Bug fixes → Note in CHANGELOG.md
- Breaking changes → Update migration guides
- Schema changes → Update schema docs

### Documentation Structure
```
documentation/
├── 00_Framework_Overview.md    ← Start here for contributors
├── 01_Getting_Started.md       ← User onboarding
├── 02-08_*.md                  ← Detailed guides
└── INDEX.md                    ← Documentation index
```

## 🚫 What We Don't Accept

- **Untested changes** – All changes must be validated
- **Breaking changes without discussion** – Talk to maintainers first
- **Code without documentation** – Document new features
- **Proprietary/licensed code** – Must be original or compatible
- **Security vulnerabilities** – Report privately first
- **Scope creep** – Keep PRs focused on one thing

## 🛡️ Security

**Found a security issue?**
- **Do NOT open a public issue**
- Contact: [your-security-contact@wolterskluwer.com]
- Provide detailed description
- Allow time for fix before disclosure

## 📊 Project Governance

**Maintainers:**
- Carsten Böhmert (@Carsten-Boehmert_wkl)

**Decision Process:**
- Small changes: Maintainer approval
- Medium changes: Discussion + approval
- Large changes: ADR + community input + approval

## 💬 Communication

- **GitHub Issues** – Bug reports, feature requests
- **GitHub Discussions** – Questions, ideas, general discussion
- **Pull Requests** – Code contributions
- **Email** – Security issues only

## 🎓 Learning Resources

**To understand the framework:**
1. Read [documentation/00_Framework_Overview.md](documentation/00_Framework_Overview.md)
2. Review example Workorders (if available)
3. Check [documentation/07_Best_Practices.md](documentation/07_Best_Practices.md)
4. Try the framework in a test project

**To contribute effectively:**
1. Use the framework yourself first
2. Identify pain points or improvements
3. Propose solutions backed by experience
4. Share learnings with the community

## 🙏 Recognition

Contributors will be recognized in:
- GitHub Contributors page
- CHANGELOG.md for significant contributions
- Project documentation (with permission)

## 📄 License

By contributing, you agree that your contributions will be licensed under the same [Wolters Kluwer Internal Use License](LICENSE) as the project.

---

**Questions?** Start a Discussion or reach out to maintainers.

**Thank you for helping make this framework better!** 🚀
