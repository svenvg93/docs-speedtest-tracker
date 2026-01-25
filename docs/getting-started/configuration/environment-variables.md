---
title: Environment Variables
description: A complete inventory of all environment variables for configuring Speedtest Tracker.
icon: lucide/settings
tags:
  - configuration
  - reference
  - environment
hide:
    - toc
---

# Environment Variables

A complete inventory of all environment variables for configuring Speedtest Tracker.

## Application

| Name | Required | Description | Default | Example |
| ---- | :------: | ----------- | ------- | ------- |
| `PUID` | :lucide-check:{ .env-required-yes } | User ID the container runs as. | | `1000` |
| `PGID` | :lucide-check:{ .env-required-yes } | Group ID the container runs as. | | `1000` |
| `APP_KEY` | :lucide-check:{ .env-required-yes } | Application encryption key. :material-information-outline:{ title="See Installation Guide" .env-tooltip } | | |
| `APP_URL` | :lucide-check:{ .env-required-yes } | Base URL used in emails and notifications. | | `https://speedtest.example.com` |
| `APP_NAME` | :lucide-x:{ .env-required-no } | Application name shown in the UI and notifications. | Speedtest Tracker | |
| `ASSET_URL` | :lucide-x:{ .env-required-no } | Base URL for serving assets (reverse proxy setups). | | `https://speedtest.example.com` |
| `APP_LOCALE` | :lucide-x:{ .env-required-no } | Default application language. | `en` | |
| `APP_TIMEZONE` | :lucide-x:{ .env-required-no } | Application timezone (if DB is not UTC). | | `Europe/London` |
| `ALLOWED_IPS` | :lucide-x:{ .env-required-no } | Only allow access from these IP addresses. | | `127.0.0.1,127.0.0.2` |

## Authentication

| Name | Required | Description | Default | Example |
| ---- | :------: | ----------- | ------- | ------- |
| `ADMIN_NAME` | :lucide-x:{ .env-required-no } | Initial admin username. :material-information-outline:{ title="Initial setup only" .env-tooltip } | [See Authentication](../security/authentication.md#default-user-account) | `Speedy` |
| `ADMIN_EMAIL` | :lucide-x:{ .env-required-no } | Initial admin email. :material-information-outline:{ title="Initial setup only" .env-tooltip } | [See Authentication](../security/authentication.md#default-user-account) | `speedy@tracker.com` |
| `ADMIN_PASSWORD` | :lucide-x:{ .env-required-no } | Initial admin password. :material-information-outline:{ title="Initial setup only" .env-tooltip } |[See Authentication](../security/authentication.md#default-user-account) | `superinternet` |

## Display 

| Name | Required | Description | Default | Example |
| ---- | :------: | ----------- | ------- | ------- |
| `CHART_BEGIN_AT_ZERO` | :lucide-x:{ .env-required-no } | Start chart axes at zero. | `true` | `true` |
| `CHART_DATETIME_FORMAT` | :lucide-x:{ .env-required-no } | Date/time format for charts.  [PHP Format](https://www.php.net/manual/en/datetime.format.php) | `'M. j - G:i'` | `j/m G:i` |
| `DATETIME_FORMAT` | :lucide-x:{ .env-required-no } | Date/time format for tables and notifications.  [PHP Format](https://www.php.net/manual/en/datetime.format.php) | `M. j, Y g:ia` | `j M Y, G:i:s` |
| `DISPLAY_TIMEZONE` | :lucide-x:{ .env-required-no } | Timezone used for displayed timestamps. | `UTC` | `America/New_York` |
| `CONTENT_WIDTH` | :lucide-x:{ .env-required-no } | Maximum content width of pages. | `7xl` | See Filament docs |
| `PUBLIC_DASHBOARD` | :lucide-x:{ .env-required-no } | Enable public (unauthenticated) dashboard. | `false` | `true` |
| `DEFAULT_CHART_RANGE` | :lucide-x:{ .env-required-no } | Default dashboard time range. | `24h` | `week` |

## Speed Tests

| Name | Required | Description | Default | Example |
| ---- | :------: | ----------- | ------- | ------- |
| `SPEEDTEST_SKIP_IPS` | :lucide-x:{ .env-required-no } | Skip tests when these public IPs are detected.:material-information-outline:{ title="Comma sperated list. Either IPs or CIDR notations" .env-tooltip } | | `1.1.1.1` |
| `SPEEDTEST_SCHEDULE` | :lucide-x:{ .env-required-no } | Cron schedule for automated speedtests. | | `6 */2 * * *` |
| `SPEEDTEST_SERVERS` | :lucide-x:{ .env-required-no } | Server IDs randomly used for testing. | | `36998,52365` |
| `SPEEDTEST_BLOCKED_SERVERS` | :lucide-x:{ .env-required-no } | Server IDs excluded from testing. | | |
| `SPEEDTEST_INTERFACE` | :lucide-x:{ .env-required-no } | Network interface used inside the container. | | `eth0` |
| `SPEEDTEST_EXTERNAL_IP_URL` | :lucide-x:{ .env-required-no } | Service used to detect external IP address. | `https://icanhazip.com` | |
| `SPEEDTEST_INTERNET_CHECK_HOSTNAME` | :lucide-x:{ .env-required-no } | Hostname used to verify internet connectivity. | `icanhazip.com` | |
| `THRESHOLD_ENABLED` | :lucide-x:{ .env-required-no } | Enable speed and ping thresholds :material-information-outline:{ title="Initial setup only" .env-tooltip }. | `false` | `true` |
| `THRESHOLD_DOWNLOAD` | :lucide-x:{ .env-required-no } | Minimum download speed threshold (Mbps). :material-information-outline:{ title="Initial setup only" .env-tooltip } | `0` :material-information-outline:{ title="0 = Disable" .env-tooltip } | `900` |
| `THRESHOLD_UPLOAD` | :lucide-x:{ .env-required-no } | Minimum upload speed threshold (Mbps). :material-information-outline:{ title="Initial setup only" .env-tooltip } | `0` :material-information-outline:{ title="0 = Disable" .env-tooltip } | `900` |
| `THRESHOLD_PING` | :lucide-x:{ .env-required-no } | Maximum ping threshold (ms). :material-information-outline:{ title="Initial setup only" .env-tooltip } | `0` :material-information-outline:{ title="0 = Disable" .env-tooltip }| `25` |
| `PRUNE_RESULTS_OLDER_THAN` | :lucide-x:{ .env-required-no } | Delete results older than this many days. | `0` :material-information-outline:{ title=" 0 = Disable" .env-tooltip } | `7` |

## API

| Name | Required | Description | Default | Example |
| ---- | :------: | ----------- | ------- | ------- |
| `API_RATE_LIMIT` | :lucide-x:{ .env-required-no } | Maximum API requests per minute. | `60` | `100` |
| `API_MAX_RESULTS` | :lucide-x:{ .env-required-no } | Maximum results returned per API request. | `500` | `500` |
