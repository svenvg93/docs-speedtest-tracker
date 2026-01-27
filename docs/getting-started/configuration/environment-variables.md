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

!!! info "Restart Required"
    Changes to environment variables require a container restart to take effect.

## Application

| Name | Required | Description | Default | Example |
| ---- | :------: | ----------- | ------- | ------- |
| `PUID` | :lucide-check:{ .env-required-yes } | User ID the container runs as. | | `1000` |
| `PGID` | :lucide-check:{ .env-required-yes } | Group ID the container runs as. | | `1000` |
| `APP_KEY` | :lucide-check:{ .env-required-yes } | Application encryption key. :lucide-info:{ title="See Installation Guide" .env-tooltip } | | |
| `APP_URL` | :lucide-check:{ .env-required-yes } | Base URL used in emails and notifications. | | `https://speedtest.example.com` |
| `APP_NAME` | :lucide-x:{ .env-required-no } | Application name shown in the UI and notifications. | Speedtest Tracker | |
| `ASSET_URL` | :lucide-x:{ .env-required-no } | Base URL for serving assets (reverse proxy setups). | | `https://speedtest.example.com` |
| `APP_LOCALE` | :lucide-x:{ .env-required-no } | Default application language. | `en` | |
| `APP_TIMEZONE` | :lucide-x:{ .env-required-no } | Application timezone (if DB is not UTC). | `UTC` | `Europe/London` |
| `ALLOWED_IPS` | :lucide-x:{ .env-required-no } | Only allow access from these IP addresses. | | `127.0.0.1,127.0.0.2` |
| `PRUNE_RESULTS_OLDER_THAN` | :lucide-x:{ .env-required-no } | Delete results older than this many days. | `0` :lucide-info:{ title="0 = Disable" .env-tooltip } | `7` |

## Database

For database configuration options including SQLite, MySQL, MariaDB, and PostgreSQL, see the [Database Drivers] documentation.

## Authentication

| Name | Required | Description | Default | Example |
| ---- | :------: | ----------- | ------- | ------- |
| `ADMIN_NAME` | :lucide-x:{ .env-required-no } | Initial admin username. :lucide-info:{ title="Initial setup only" .env-tooltip } | [See Authentication] | `Speedy` |
| `ADMIN_EMAIL` | :lucide-x:{ .env-required-no } | Initial admin email. :lucide-info:{ title="Initial setup only" .env-tooltip } | [See Authentication] | `speedy@tracker.com` |
| `ADMIN_PASSWORD` | :lucide-x:{ .env-required-no } | Initial admin password. :lucide-info:{ title="Initial setup only" .env-tooltip } |[See Authentication] | `superinternet` |

## Display

| Name | Required | Description | Default | Example |
| ---- | :------: | ----------- | ------- | ------- |
| `PUBLIC_DASHBOARD` | :lucide-x:{ .env-required-no } | Enable public (unauthenticated) dashboard. | `false` | `true` |
| `DEFAULT_CHART_RANGE` | :lucide-x:{ .env-required-no } | Default dashboard time range. | `24h` | `week` |
| `CONTENT_WIDTH` | :lucide-x:{ .env-required-no } | Maximum content width of pages. [Filament Docs] | `7xl` | |
| `DISPLAY_TIMEZONE` | :lucide-x:{ .env-required-no } | Timezone used for displayed timestamps. | `UTC` | `America/New_York` |
| `DATETIME_FORMAT` | :lucide-x:{ .env-required-no } | Date/time format for tables and notifications.  [PHP Format] | `M. j, Y g:ia` | `j M Y, G:i:s` |
| `CHART_DATETIME_FORMAT` | :lucide-x:{ .env-required-no } | Date/time format for charts.  [PHP Format] | `'M. j - G:i'` | `j/m G:i` |
| `CHART_BEGIN_AT_ZERO` | :lucide-x:{ .env-required-no } | Start chart axes at zero. | `true` | `true` |

## Speed Tests

| Name | Required | Description | Default | Example |
| ---- | :------: | ----------- | ------- | ------- |
| `SPEEDTEST_SCHEDULE` | :lucide-x:{ .env-required-no } | Cron schedule for automated speedtests. [crontab.guru] | | `6 */2 * * *` |
| `SPEEDTEST_SERVERS` | :lucide-x:{ .env-required-no } | Server IDs randomly used for testing. [Server List] | | `36998,52365` |
| `SPEEDTEST_BLOCKED_SERVERS` | :lucide-x:{ .env-required-no } | Server IDs excluded from testing. | | `36998,52365` |
| `SPEEDTEST_INTERFACE` | :lucide-x:{ .env-required-no } | Network interface used inside the container. | | `eth0` |
| `SPEEDTEST_INTERNET_CHECK_HOSTNAME` | :lucide-x:{ .env-required-no } | Hostname used to verify internet connectivity. | `icanhazip.com` | |
| `SPEEDTEST_EXTERNAL_IP_URL` | :lucide-x:{ .env-required-no } | Service used to detect external IP address. :lucide-info:{ title="Service must return only an IP address in the response body" .env-tooltip } | `https://icanhazip.com` | |
| `SPEEDTEST_SKIP_IPS` | :lucide-x:{ .env-required-no } | Skip tests when these public IPs are detected. :lucide-info:{ title="Comma separated list. Either IPs or CIDR notations" .env-tooltip } | | `1.1.1.1` |

## Benchmarking

| Name | Required | Description | Default | Example |
| ---- | :------: | ----------- | ------- | ------- |
| `THRESHOLD_ENABLED` | :lucide-x:{ .env-required-no } | Enable speed and ping thresholds. :lucide-info:{ title="Initial setup only" .env-tooltip } | `false` | `true` |
| `THRESHOLD_DOWNLOAD` | :lucide-x:{ .env-required-no } | Minimum download speed threshold (Mbps). :lucide-info:{ title="Initial setup only" .env-tooltip } | `0` :lucide-info:{ title="0 = Disable" .env-tooltip } | `900` |
| `THRESHOLD_UPLOAD` | :lucide-x:{ .env-required-no } | Minimum upload speed threshold (Mbps). :lucide-info:{ title="Initial setup only" .env-tooltip } | `0` :lucide-info:{ title="0 = Disable" .env-tooltip } | `900` |
| `THRESHOLD_PING` | :lucide-x:{ .env-required-no } | Maximum ping threshold (ms). :lucide-info:{ title="Initial setup only" .env-tooltip } | `0` :lucide-info:{ title="0 = Disable" .env-tooltip } | `25` |

## API

| Name | Required | Description | Default | Example |
| ---- | :------: | ----------- | ------- | ------- |
| `API_RATE_LIMIT` | :lucide-x:{ .env-required-no } | Maximum API requests per minute. | `60` | `100` |
| `API_MAX_RESULTS` | :lucide-x:{ .env-required-no } | Maximum results returned per API request. | `500` | `500` |

## Data Integrations

### InfluxDB v2

| Name | Required | Description | Default | Example |
| ---- | :------: | ----------- | ------- | ------- |
| `INFLUXDB_V2_ENABLED` | :lucide-x:{ .env-required-no } | Enable InfluxDB v2 integration. :lucide-info:{ title="Initial setup only" .env-tooltip } | `false` | `true` |
| `INFLUXDB_V2_URL` | :lucide-x:{ .env-required-no } | InfluxDB v2 server URL. :lucide-info:{ title="Initial setup only" .env-tooltip } | | `http://influxdb:8086` |
| `INFLUXDB_V2_ORG` | :lucide-x:{ .env-required-no } | InfluxDB v2 organization name. :lucide-info:{ title="Initial setup only" .env-tooltip } | | `my-org` |
| `INFLUXDB_V2_BUCKET` | :lucide-x:{ .env-required-no } | InfluxDB v2 bucket name. :lucide-info:{ title="Initial setup only" .env-tooltip } | | `speedtest-tracker` |
| `INFLUXDB_V2_TOKEN` | :lucide-x:{ .env-required-no } | InfluxDB v2 API token. :lucide-info:{ title="Initial setup only" .env-tooltip } | | |
| `INFLUXDB_V2_VERIFY_SSL` | :lucide-x:{ .env-required-no } | Verify SSL certificates for InfluxDB connections. :lucide-info:{ title="Initial setup only" .env-tooltip } | `true` | `false` |

### Prometheus

| Name | Required | Description | Default | Example |
| ---- | :------: | ----------- | ------- | ------- |
| `PROMETHEUS_ENABLED` | :lucide-x:{ .env-required-no } | Enable Prometheus metrics endpoint. :lucide-info:{ title="Initial setup only" .env-tooltip } | `false` | `true` |
| `PROMETHEUS_ALLOWED_IPS` | :lucide-x:{ .env-required-no } | IP addresses allowed to scrape metrics. :lucide-info:{ title="Initial setup only" .env-tooltip } | | `127.0.0.1,192.168.1.0/24` |

  [Database Drivers]: database-drivers.md
  [See Authentication]: ../security/authentication.md#default-user-account
  [Filament Docs]: https://filamentphp.com/docs/4.x/panel-configuration#customizing-the-maximum-content-width
  [PHP Format]: https://www.php.net/manual/en/datetime.format.php
  [crontab.guru]: https://crontab.guru/
  [Server List]: https://c.speedtest.net/speedtest-servers-static.php
