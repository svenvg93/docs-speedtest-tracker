---
title: Getting Started
description: Learn how to contribute to Speedtest Tracker through bug reports, feature requests, and code contributions.
icon: lucide/play
tags:
  - contributing
  - community
  - overview
---

# Contributing to Speedtest Tracker

Thank you for your interest in contributing to Speedtest Tracker! We welcome contributions from the community.

## Ways to Contribute

- Fix [existing issues](https://github.com/alexjustesen/speedtest-tracker/issues?q=is%3Aissue%20state%3Aopen%20label%3Abug)
- Implement [new features](https://github.com/alexjustesen/speedtest-tracker/issues?q=state%3Aopen%20label%3Afeature)
- Improve the [documentation](documentation.md)

## Before You Start

### Pick the Right Repository

- **Application code** → [speedtest-tracker](https://github.com/alexjustesen/speedtest-tracker)
- **Documentation** → [speedtest-tracker-docs](https://github.com/alexjustesen/speedtest-tracker-docs)

### Check for Existing Work

Before starting, search to avoid duplicate effort:

- [Open Issues](https://github.com/alexjustesen/speedtest-tracker/issues) - Current bugs and feature requests
- [Open Pull Requests](https://github.com/alexjustesen/speedtest-tracker/pulls) - Work in progress
- [Closed Pull Requests](https://github.com/alexjustesen/speedtest-tracker/pulls?q=is%3Apr+is%3Aclosed) - Recently completed work
- [GitHub Discussions](https://github.com/alexjustesen/speedtest-tracker/discussions) - Community conversations

### Major Changes

For significant features or architectural changes, open an issue first to discuss the approach.

## Quick Start

### 1. Fork and Clone

Fork the appropriate repository on GitHub, then clone your fork:

```bash
git clone git@github.com:YOUR-USERNAME/speedtest-tracker.git
cd speedtest-tracker
```

### 2. Create a Branch

Create a branch using these naming conventions:

- `feature/` - New features (e.g., `feature/discord-notifications`)
- `fix/` - Bug fixes (e.g., `fix/database-timeout`)
- `docs/` - Documentation changes (e.g., `docs/installation-guide`)

```bash
git checkout -b feature/your-feature-name
```

### 3. Make Your Changes

- For code: See [Development Environment](development-environment.md) to set up your local environment
- For docs: See [Documentation Guidelines](documentation.md) for style and structure

### 4. Submit a Pull Request

Before submitting, ensure:

- [ ] All automated checks pass (linting, tests, documentation builds)
- [ ] Changes tested in local development environment
- [ ] Existing functionality still works
- [ ] Commit messages are clear and descriptive

Then on GitHub:

1. Push your branch: `git push origin feature/your-feature-name`
2. Click "Compare & pull request" on your fork
3. Fill out the PR template with:
   - Clear title describing the change
   - Explanation of what, why, and how
   - Reference to related issue numbers

### 5. Respond to Feedback

Maintainers will review your PR and may request changes. To update your PR:

```bash
# Make requested changes
git add .
git commit -m "Address review feedback"
git push origin feature/your-feature-name
```

The PR updates automatically. Be patient and respectful - reviews take time.

## Tips

- **Keep PRs focused**: One feature or fix per PR
- **Update your branch**: Sync with main if the base branch changes
- **Ask questions**: If feedback is unclear, ask for clarification
- **Be respectful**: We're all here to improve the project together

## Need Help?

- Check [GitHub Discussions](https://github.com/alexjustesen/speedtest-tracker/discussions)
- Ask in an [existing issue](https://github.com/alexjustesen/speedtest-tracker/issues)
- Review the [documentation](../index.md)
