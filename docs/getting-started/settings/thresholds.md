---
title: Thresholds
description: Set minimum download, upload, and ping values to automatically mark tests as unhealthy when they fall below these thresholds.
icon: lucide/gauge
tags:
  - settings
  - benchmarking
  - thresholds
---

# Thresholds

Thresholds allow you to define minimum acceptable values for your speedtest results. When a test result falls below any of the configured thresholds, it will automatically be marked as unhealthy. This helps you quickly identify network performance issues and trigger notifications when your connection doesn't meet expectations.

## Settings

Configure thresholds in the application settings to define minimum acceptable values for each metric.

| Name | Default | Description |
| ---- | ------- | ----------- |
| Minimum Download | `blank` | Minimum download speed in Mbps. Tests below this value are marked as unhealthy. |
| Minimum Upload | `blank` | Minimum upload speed in Mbps. Tests below this value are marked as unhealthy. |
| Maximum Ping | `blank` | Maximum acceptable ping latency in ms. Tests above this value are marked as unhealthy. |

!!! note

    Set a threshold to `0` to disable that specific check. At least one threshold must be set for the health monitoring to be active.

## How It Works

When a speedtest completes, the results are automatically compared against your configured thresholds:

- **Download Speed**: If the measured download speed is less than the minimum download threshold, the test is marked as unhealthy.
- **Upload Speed**: If the measured upload speed is less than the minimum upload threshold, the test is marked as unhealthy.
- **Ping Latency**: If the measured ping is greater than the minimum ping threshold (lower is better for ping), the test is marked as unhealthy.

If any single threshold is exceeded, the entire test result will be flagged as unhealthy.

## Use Cases

Thresholds are useful for:

- **SLA Monitoring**: Ensure your ISP is meeting service level agreements
- **Quality Alerts**: Get notified when network performance degrades
- **Data Analysis**: Filter and analyze periods of poor connectivity
- **Troubleshooting**: Identify patterns in network performance issues

## Integration with Notifications

Unhealthy test results can trigger notifications through your configured notification channels. This allows you to be alerted immediately when your internet connection fails to meet your minimum requirements.

See [Notifications] for more information on setting up alerts.

## Example Configuration

For a typical home internet connection with a 500 Mbps download, 100 Mbps upload plan:

- **Minimum Download**: `400` (80% of rated speed)
- **Minimum Upload**: `80` (80% of rated speed)
- **Minimum Ping**: `50` (acceptable latency for most activities)

Adjust these values based on your specific internet plan and requirements.

  [Notifications]: ../settings/notifications/index.md