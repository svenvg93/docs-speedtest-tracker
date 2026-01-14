#!/usr/bin/env python3

import json
import urllib.request
from datetime import datetime
import os
import re

RELEASES_URL = 'https://api.github.com/repos/alexjustesen/speedtest-tracker/releases?per_page=10'
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), '../docs/release-notes.md')

def fetch_releases():
    """Fetch releases from GitHub API"""
    req = urllib.request.Request(RELEASES_URL)
    req.add_header('User-Agent', 'Python')
    req.add_header('Accept', 'application/vnd.github+json')

    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode())

def format_date(date_string):
    """Format ISO date string to readable format"""
    date = datetime.fromisoformat(date_string.replace('Z', '+00:00'))
    return date.strftime('%B %d, %Y')

def generate_markdown(releases):
    """Generate markdown content from releases"""
    markdown = """---
title: What's new
description: Latest releases and updates for Speedtest Tracker
tags:
  - releases
  - changelog
  - updates
---

# Release Notes

!!! info "Latest Releases"

    This page shows the 10 most recent releases. For the complete release history, visit the [GitHub releases page](https://github.com/alexjustesen/speedtest-tracker/releases).

"""

    for release in releases:
        title = release.get('name') or release.get('tag_name', 'Untitled Release')
        date = format_date(release['published_at'])
        author = release.get('author')
        github_link = release['html_url']
        body = release.get('body', 'No release notes provided.')

        # Convert ## What's Changed, ## What's New, ## What's Fixed to ### for proper hierarchy
        body = body.replace('## What\'s Changed', '### What\'s Changed')
        body = body.replace('## What\'s New', '### What\'s New')
        body = body.replace('## What\'s Fixed', '### What\'s Fixed')

        # Convert GitHub admonitions to Material for MkDocs format
        # > [!NOTE] -> !!! note
        # > [!TIP] -> !!! tip
        # > [!IMPORTANT] -> !!! warning
        # > [!WARNING] -> !!! warning
        # > [!CAUTION] -> !!! danger

        # Map GitHub admonition types to Material types
        admonition_map = {
            'NOTE': 'note',
            'TIP': 'tip',
            'IMPORTANT': 'warning',
            'WARNING': 'warning',
            'CAUTION': 'danger'
        }

        # Convert GitHub-style admonitions
        for gh_type, md_type in admonition_map.items():
            # Simple replacement for single-line or multi-line GitHub admonitions
            # Match: > [!TYPE]\r\n or \n> content
            # Handle both \r\n and \n line endings
            pattern = rf'> \[!{gh_type}\](?:\r?\n> .*)*'

            def replace_admonition(match):
                # Split by any line ending and process each line
                content_lines = re.split(r'\r?\n', match.group(0))
                # Skip the first line (> [!TYPE]) and remove '> ' prefix from the rest
                clean_lines = [line.lstrip('> ').strip() for line in content_lines[1:] if line.strip()]
                if clean_lines:
                    content_text = '\n    '.join(clean_lines)
                    return f'!!! {md_type}\n\n    {content_text}\n'
                else:
                    return f'!!! {md_type}\n'

            body = re.sub(pattern, replace_admonition, body)

        markdown += f"## {title}"

        if release.get('prerelease'):
            markdown += " :material-test-tube:{ title='Pre-release' }"
        if release.get('draft'):
            markdown += " :material-pencil:{ title='Draft' }"

        markdown += "\n\n"
        markdown += f"**Released:** {date}"

        if author:
            author_login = author['login']
            author_url = author['html_url']
            markdown += f" • **Author:** [@{author_login}]({author_url})"

        markdown += f" • [View on GitHub]({github_link})\n\n"
        markdown += f"{body}\n\n"
        markdown += "---\n\n"

    markdown += "\n[View All Releases on GitHub](https://github.com/alexjustesen/speedtest-tracker/releases){ .md-button .md-button--primary }\n"

    return markdown

def main():
    try:
        print('Fetching releases from GitHub...')
        releases = fetch_releases()

        print(f'Fetched {len(releases)} releases')

        markdown = generate_markdown(releases)

        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write(markdown)

        print(f'Release notes written to {OUTPUT_FILE}')
    except Exception as error:
        print(f'Error generating release notes: {error}')
        exit(1)

if __name__ == '__main__':
    main()
