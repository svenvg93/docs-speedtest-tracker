---
title: What's new
description: Latest releases and updates for Speedtest Tracker
tags:
  - releases
  - changelog
  - updates
---

# Release Notes

<div id="releases-container">
  <p>Loading releases...</p>
</div>

<script>
async function fetchReleases() {
  const container = document.getElementById('releases-container');

  try {
    const response = await fetch('https://api.github.com/repos/alexjustesen/speedtest-tracker/releases?per_page=10', {
      headers: {
        'Accept': 'application/vnd.github.html+json'
      }
    });

    if (!response.ok) {
      throw new Error('Failed to fetch releases');
    }

    const releases = await response.json();

    if (releases.length === 0) {
      container.innerHTML = '<p>No releases found.</p>';
      return;
    }

    let html = '';

    releases.forEach(release => {
      const date = new Date(release.published_at).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      });

      // Use GitHub's rendered HTML (should be available with the Accept header)
      const body = release.body_html || parseMarkdown(release.body || 'No release notes provided.');

      // Create a URL-safe ID from the tag name
      const releaseId = (release.tag_name || '').replace(/[^a-zA-Z0-9-]/g, '-').toLowerCase();

      html += `
        <div class="release">
          <h2 id="${releaseId}">
            ${release.name || release.tag_name}
            ${release.prerelease ? '<span class="badge badge-prerelease">Pre-release</span>' : ''}
            ${release.draft ? '<span class="badge badge-draft">Draft</span>' : ''}
          </h2>

          <div class="release-meta">
            <span>${date}</span>
            ${release.author ? ` • by <a href="${release.author.html_url}" target="_blank" rel="noopener noreferrer">@${release.author.login}</a>` : ''}
            <span> • <a href="${release.html_url}" target="_blank" rel="noopener noreferrer">View on GitHub</a></span>
          </div>

          <div class="release-body">
            ${body}
          </div>
        </div>
      `;
    });

    html += `
      <div style="margin-top: 2rem; text-align: center;">
        <a href="https://github.com/alexjustesen/speedtest-tracker/releases" target="_blank" rel="noopener noreferrer" class="md-button md-button--primary">
          View All Releases on GitHub
        </a>
      </div>
    `;

    container.innerHTML = html;

  } catch (error) {
    console.error('Error fetching releases:', error);
    container.innerHTML = `
      <div class="admonition warning">
        <p class="admonition-title">Unable to load releases</p>
        <p>We couldn't fetch the latest releases. Please visit the
          <a href="https://github.com/alexjustesen/speedtest-tracker/releases" target="_blank" rel="noopener noreferrer">
            GitHub Releases page
          </a> directly.
        </p>
      </div>
    `;
  }
}

// Simple markdown parser for release notes
function parseMarkdown(markdown) {
  let html = markdown;

  // Code blocks (must be done before other replacements)
  html = html.replace(/```[\s\S]*?```/g, (match) => {
    return '<pre><code>' + match.slice(3, -3).trim() + '</code></pre>';
  });

  // Headers
  html = html.replace(/^### (.*$)/gim, '<h3>$1</h3>');
  html = html.replace(/^## (.*$)/gim, '<h2>$1</h2>');
  html = html.replace(/^# (.*$)/gim, '<h1>$1</h1>');

  // Bold (before italic to handle overlap)
  html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
  html = html.replace(/\_\_(.*?)\_\_/g, '<strong>$1</strong>');

  // Italic
  html = html.replace(/\*([^\*]+)\*/g, '<em>$1</em>');
  html = html.replace(/\_([^\_]+)\_/g, '<em>$1</em>');

  // Links - markdown format [text](url)
  html = html.replace(/\[([^\]]+)\]\(([^\)]+)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>');

  // Auto-link plain URLs (not already in href or inside tags)
  html = html.replace(/(?<!href="|">)(https?:\/\/[^\s<]+)/g, '<a href="$1" target="_blank" rel="noopener noreferrer">$1</a>');

  // Inline code (after links to avoid breaking URLs)
  html = html.replace(/`([^`]+)`/g, '<code>$1</code>');

  // Lists
  html = html.replace(/^\* (.*$)/gim, '<li>$1</li>');
  html = html.replace(/^- (.*$)/gim, '<li>$1</li>');
  html = html.replace(/(<li>.*<\/li>)/s, '<ul>$1</ul>');

  // Line breaks
  html = html.replace(/\n\n/g, '</p><p>');
  html = '<p>' + html + '</p>';

  // Clean up empty paragraphs
  html = html.replace(/<p><\/p>/g, '');
  html = html.replace(/<p>\s*<h/g, '<h');
  html = html.replace(/<\/h([1-6])>\s*<\/p>/g, '</h$1>');
  html = html.replace(/<p>\s*<ul>/g, '<ul>');
  html = html.replace(/<\/ul>\s*<\/p>/g, '</ul>');
  html = html.replace(/<p>\s*<pre>/g, '<pre>');
  html = html.replace(/<\/pre>\s*<\/p>/g, '</pre>');

  return html;
}

// Load releases when page loads
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', fetchReleases);
} else {
  fetchReleases();
}
</script>

<style>
.release {
  margin-bottom: 3rem;
  padding-bottom: 2rem;
  border-bottom: 1px solid var(--md-default-fg-color--lightest);
}

.release h2 {
  margin-bottom: 0.5rem;
}

.release h2 a {
  color: var(--md-default-fg-color);
}

.release h2 a:hover {
  color: var(--md-accent-fg-color);
}

.badge {
  padding: 0.2rem 0.5rem;
  border-radius: 0.2rem;
  font-size: 0.75rem;
  margin-left: 0.5rem;
  color: white;
}

.badge-prerelease {
  background: var(--md-accent-fg-color);
}

.badge-draft {
  background: var(--md-default-fg-color--lighter);
}

.release-meta {
  color: var(--md-default-fg-color--light);
  font-size: 0.9rem;
  margin-bottom: 1rem;
}

.release-body {
  line-height: 1.6;
}

.release-body ul {
  margin-left: 1.5rem;
}

.release-body li {
  margin-bottom: 0.5rem;
}

.release-body code {
  background: var(--md-code-bg-color);
  padding: 0.1rem 0.3rem;
  border-radius: 0.2rem;
  font-size: 0.85em;
  font-family: var(--md-code-font-family);
}

.release-body pre {
  background: var(--md-code-bg-color);
  padding: 1rem;
  border-radius: 0.3rem;
  overflow-x: auto;
  margin: 1rem 0;
}

.release-body pre code {
  background: transparent;
  padding: 0;
}

.release-body a {
  color: var(--md-accent-fg-color);
  text-decoration: none;
  border-bottom: 1px solid transparent;
  transition: border-bottom-color 0.2s;
}

.release-body a:hover {
  border-bottom-color: var(--md-accent-fg-color);
}

.release-body h1,
.release-body h2,
.release-body h3 {
  margin-top: 1.5rem;
  margin-bottom: 0.5rem;
}

.release-body p {
  margin-bottom: 1rem;
}
</style>
