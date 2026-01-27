---
title: Pull Requests
icon: lucide/git-pull-request-create
---
# Pull Requests

The process and requirements we describe below serve as important guardrails
that are essential to running an Open Source project and help us prevent wasted
effort and ensure the integrity of the codebase. This is more important than
ever as the number of attacks on Open Source projects by malicious actors and
the amount of AI slop both increase.

## Before you start

Before you start work on a pull request (PR), we need you to open an issue and
discuss it with us so we know what you are working on and so we can agree on the
approach to take. This prevents you from spending time on a feature that may not
align with the project's goals. You then reference the issue number in your PR
to link back to our discussion.

## Styles and linting

It is important that your edits produce clean commits that can be reviewed
quickly and without distractions caused by spurious diffs caused by format
changes that conflict with the style we use.

## Use of Generative AI

AI-assisted coding can be useful but the unreflected inclusion of AI-generated
code can also do great harm. 

Code contributions that contain obviously AI-generated code that you cannot
fully explain to us will be rejected. We must ensure, after all, that the
contribution does not contain bugs or malicious code, and that we can commit to
maintaining it in the future.

## Commit message standards

We follow the [Conventional Commits] specification, with automatically computed
scopes for changes derived from the structure of the project or from
configuration. This helps us automate our release notes and versioning. Each
commit message must follow this structure:

  [Conventional Commits]: https://www.conventionalcommits.org/

```
<type>: <summary description>
```