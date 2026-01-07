---
title: Notifications
description: Configure notifications for speedtest results via database, mail, webhook, and Apprise.
icon: lucide/bell
---

# Notifications

Speedtest Tracker supports multiple notification channels to keep you informed about your internet connection performance. Whether you want in-app alerts, email notifications, webhook integrations, or notifications to your favorite services, you can configure notifications to suit your needs.

## Available Channels

Speedtest Tracker offers several notification channels, each with its own strengths. You can enable multiple channels simultaneously to ensure you receive notifications through your preferred method.

<div class="grid cards" markdown>

-   :lucide-inbox:{ .lg .middle } __Database__

    ---

    In-app notifications that appear in the application header

    [:octicons-arrow-right-24: Configure Database Notifications](database.md)

-   :lucide-mail:{ .lg .middle } __Mail__

    ---

    Email notifications via SMTP to one or more recipients

    [:octicons-arrow-right-24: Configure Mail Notifications](mail.md)

-   :lucide-webhook:{ .lg .middle } __Webhook__

    ---

    JSON payloads sent to custom endpoints for integration with other services

    [:octicons-arrow-right-24: Configure Webhook Notifications](webhook.md)

-   :lucide-bell-ring:{ .lg .middle } __Apprise__

    ---

    Unified notification system supporting 100+ services including Discord, Pushover, Ntfy, and more

    [:octicons-arrow-right-24: Configure Apprise Notifications](apprise.md)

</div>

## Triggers

Triggers determine when notifications are sent. All notification channels support the following triggers:

| Name | Description |
| ---- | ----------- |
| on every scheduled speedtest run | On each successful scheduled speedtest a notification will be sent to the application. |
| on threshold failures for scheduled speedtests | On any absolute threshold failure for scheduled speedtest a notification will be sent to the application. |

!!! tip

    Configure your [thresholds](../thresholds.md) to define what constitutes a threshold failure.

