---
title: Guidelines
description: Guidelines for contributing to and editing Speedtest Tracker documentation.
icon: lucide/file-text
tags:
  - contributing
  - documentation
  - writing
---

# Documentation Guidelines

Thank you for helping improve the Speedtest Tracker documentation! This guide will help you contribute effectively.

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

### Page Frontmatter

Every documentation page must include frontmatter with the following fields:

```markdown
---
title: Page Title
description: A brief description of the page content (1-2 sentences).
icon: lucide/icon-name
tags:
  - category-tag
  - feature-tag
---
```

### Tag Guidelines

Use a combination of category tags and contextual tags:

**Category Tags:**
- `installation` - Installation guides
- `configuration` - Configuration and setup
- `security` - Security-related topics
- `settings` - Application settings
- `help` - Troubleshooting
- `reference` - Reference materials
- `contributing` - Contributing guides
- `api` - API documentation

**Contextual Tags:**
- Technology tags: `docker`, `kubernetes`, `nginx`, `traefik`
- Platform tags: `unraid`, `synology`, `qnap`, `nas`
- Feature tags: `notifications`, `monitoring`, `database`, `proxy`

## Markdown Features

The documentation uses Zensical, which provides powerful markdown extensions for creating rich, interactive documentation. For complete documentation on all available markdown features and syntax, see the official Zensical documentation:

**[Zensical Markdown Reference](https://zensical.org/docs/authoring/markdown/)**

## Making Changes

### Local Testing

Before submitting changes, test your documentation locally to ensure everything renders correctly.

??? tip "Install Zensical"
    You can follow Zensical [installation guide](https://zensical.org/docs/get-started/#installation) to install everything needed 

??? tip "Using Dev Container"

    **Prerequisites**

    - [Docker](https://www.docker.com/get-started) installed and running  
    - [Visual Studio Code](https://code.visualstudio.com)  
    - [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) installed in VS Code

    **Launch Dev Container**

    1. Open your repository in VS Code
    2. Then follow the instructions for your OS:\
    •	macOS: Press Command + Shift + P → type Dev Containers: Reopen in Container → press Enter\
    •	Windows: Press Ctrl + Shift + P → type Dev Containers: Reopen in Container → press Enter
    4. VS Code will build the container and install all dependencies automatically

    Once inside the container, you can serve the site locally:

    ```bash
    zensical serve -a 0.0.0.0:8000
    ```

    Then open `http://localhost:8000` in your browser to preview.

## Common Mistakes to Avoid

- Don't use absolute URLs for internal links
- Don't forget to include frontmatter tags
- Don't use first person ("I", "we") in documentation
- Don't include outdated version-specific information without noting versions
- Don't create documentation without testing locally first

## Questions or Help

If you have questions about contributing to the documentation:

- Open a [GitHub Discussion](https://github.com/alexjustesen/speedtest-tracker/discussions)
- Reference existing documentation pages as examples

Thank you for helping make Speedtest Tracker's documentation better!
