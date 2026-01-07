---
title: Pull Requests
description: Guidelines for submitting pull requests to Speedtest Tracker.
icon: lucide/git-pull-request
---

# Submitting Pull Requests

Follow this workflow to submit changes to Speedtest Tracker.

## Quick Checklist

Before submitting:

- [ ] Code passes linting checks
- [ ] Changes tested in development environment
- [ ] Existing functionality still works
- [ ] Commit messages are clear
- [ ] PR description explains what, why, and how

## Workflow

### 1. Fork and Branch

Before starting, check [open](https://github.com/alexjustesen/speedtest-tracker/pulls) and [closed pull requests](https://github.com/alexjustesen/speedtest-tracker/pulls?q=is%3Apr+is%3Aclosed) to avoid duplicate work.

Then fork the repository and create a feature branch:

```bash
# Clone your fork
git clone git@github.com:YOUR-USERNAME/speedtest-tracker
cd speedtest-tracker

# Create a branch
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

**Branch naming:**
- `feature/` - New features
- `fix/` - Bug fixes
- `chore/` - Housekeeping changes
- `docs/` - Documentation changes

!!! info "Documentation Repository"
    For documentation changes, submit PRs to [speedtest-tracker-docs](https://github.com/alexjustesen/speedtest-tracker-docs) instead.

### 2. Make Changes

1. Set up your [development environment](development-environment.md)
2. Make your changes
3. Test thoroughly
4. Run linting:
   ```bash
   ./vendor/bin/pint
   ```

### 3. Commit

Write clear, descriptive commit messages:

```bash
git add .
git commit -m "Add support for custom Ookla servers"
```

**Good commit messages:**
- "Fix database connection timeout issue"
- "Add email notification retry logic"
- "Update installation docs for Docker Compose"

**Avoid:**
- "Fix stuff"
- "WIP"
- "Updates"

### 4. Push and Create PR

Push your branch:

```bash
git push origin feature/your-feature-name
```

Then on GitHub:

1. Go to [speedtest-tracker repository](https://github.com/alexjustesen/speedtest-tracker)
2. Click "New Pull Request"
3. Select your fork and branch
4. Fill out the PR template

## After Submission

- Respond to review feedback
- Make requested changes in new commits
- Be patient - reviews may take time

## Tips

- **Keep PRs focused**: One feature or fix per PR
- **Update your branch**: Sync with main if needed
- **Be responsive**: Address feedback promptly
- **Ask questions**: If feedback is unclear, ask for clarification
