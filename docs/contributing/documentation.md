---
title: Documentation
description: Guidelines for contributing to and editing Speedtest Tracker documentation.
icon: lucide/file-pen-line
tags:
  - contributing
  - documentation
  - writing
---

# Documentation

Our documentation includes information on features, configurations  and much more. 
If you have found an inconsistency or see room
for improvement, please follow this guide to submit an issue on our [issue
tracker] for the documentation repository.

  [issue tracker]: https://github.com/alexjustesen/speedtest-tracker-docs/issues

## Documentation Structure

The documentation is organized into the following sections:

- **Getting Started** - Installation, configuration, and initial setup
- **Security** - Authentication, authorization, and encryption
- **Settings** - Application settings, notifications, and integrations
- **Help** - Troubleshooting and error resolution
- **API** - API reference and usage
- **Other** - Additional reference materials
- **Contributing** - How to contribute to the project

## Writing Style

### Voice and Tone

- Use **clear, concise language**
- Write in **second person** ("you") when addressing the reader
- Use **active voice** instead of passive voice
- Be **friendly and helpful** without being overly casual

## Making Changes

### Using GitBook

The documentation is hosted and managed on **GitBook**. Since GitBook uses a proprietary markdown format, the easiest way to edit the documentation is through the GitBook web app, which provides the best editing experience with live preview and a visual editor.

**To edit documentation via GitBook:**

1. Fork the [speedtest-tracker/docs-speedtest-tracker](https://github.com/alexjustesen/speedtest-tracker) repository on GitHub
2. Create a new branch called: docs/your-nice-branch-name
2. Go to [GitBook](https://www.gitbook.com) and sign in with your GitHub account
3. Link your GitHub fork to GitBook:
   - Create a new space or import your fork
   - Enable Git Sync to connect your fork
4. Edit documentation in GitBook's visual editor with live preview
5. Changes are automatically synced to your GitHub fork
6. Submit a pull request from your fork to the main repository

This approach gives you the best editing experience with real-time preview, spell checking, and GitBook's markdown enhancements.

## Common Mistakes to Avoid

- Don't use absolute URLs for internal links
- Don't use first person ("I", "we") in documentation
- Don't include outdated version-specific information without noting versions

## Questions or Help

If you have questions about contributing to the documentation:

- Open a [GitHub Discussion]
- Reference existing documentation pages as examples

  [GitHub Discussion]: https://github.com/alexjustesen/speedtest-tracker/discussions

Thank you for helping make Speedtest Tracker's documentation better!
