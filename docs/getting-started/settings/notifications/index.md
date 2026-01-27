---
title: Notifications
description: Configure notifications for speedtest results via database, mail, webhook, and Apprise.
icon: lucide/bell
tags:
  - settings
  - notifications
  - alerts
---

# Notifications

Speedtest Tracker supports multiple notification channels to keep you informed about your internet connection performance. Whether you want in-app alerts, email notifications, webhook integrations, or notifications to your favorite services, you can configure notifications to suit your needs.

## Available Channels

Speedtest Tracker offers several notification channels, each with its own strengths. You can enable multiple channels simultaneously to ensure you receive notifications through your preferred method.

<div class="grid cards" markdown>

- :lucide-inbox:{ .lg .middle } [__Database__]
  In-app notifications in the header.

- :lucide-mail:{ .lg .middle } [__Mail__]
  Email notifications via SMTP.

- :lucide-webhook:{ .lg .middle } [__Webhook__]
  JSON payloads for integration with other services.

- :lucide-bell-ring:{ .lg .middle } [__Apprise__]
  Unified notifications for 100+ services (Discord, Pushover, Ntfy, etc.).

</div>

## Triggers

Triggers determine when notifications are sent. All notification channels support the following triggers:

| Name | Description |
| ---- | ----------- |
| On every scheduled speedtest run | Sends a notification after each successful scheduled speedtest. |
| On threshold failures for scheduled speedtests | Sends a notification if any threshold is exceeded during a scheduled speedtest. |

??? tip "Configure thresholds"
    Set up your [thresholds] to define what counts as a failure.

  [__Database__]: database.md
  [__Mail__]: mail.md
  [__Webhook__]: webhook.md
  [__Apprise__]: apprise.md
  [thresholds]: ../thresholds.md