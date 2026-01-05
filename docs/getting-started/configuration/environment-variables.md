---
title: Environment Variables
description: A complete inventory of all environment variables for configuring Speedtest Tracker.
---

# Environment Variables

## Application

| Name | Required | Description | Example |
| ---- | -------- | ----------- | ------- |
| `PUID` | :lucide-check: | Used to set the user the container should run as. | `1000` |
| `PGID` | Yes | Used to set the group the container should run as. | `1000` |
| `APP_KEY` | Yes | Key used to encrypt and decrypt data. See the [install](../installation/docker-compose.md#generate-an-application-key) docs to generate a key. | |
| `APP_URL` | Yes | URL used for links in emails and notifications. | `https://speedtest.example.com` |
| `APP_NAME` | No | Used to define the application's name in the dashboard and in notifications. | |
| `ADMIN_NAME` | No | Name of the initial admin user. Note: Only effective during initial setup. | `Admin` |
| `ADMIN_EMAIL` | No | Email of the initial admin user. Note: Only effective during initial setup. | `admin@example.com` |
| `ADMIN_PASSWORD` | No | Password of the initial admin user. Note: Only effective during initial setup. | `password` |
| `ASSET_URL` | No | URL used for assets, needed when using a reverse proxy. | `https://speedtest.example.com` |
| `APP_LOCALE` | No | Change the default language. | |
| `APP_TIMEZONE` | No | Application timezone should be set if your database does not use UTC as its default timezone. | `Europe/London` |
| `ALLOWED_IPS` | No | Block requests to the application unless from the allowed addresses. | `127.0.0.1,127.0.0.2` |

## Display

| Name | Required | Description | Example |
| ---- | -------- | ----------- | ------- |
| `CHART_BEGIN_AT_ZERO` | No | Begin the dashboard axis charts at zero. Default: `true` | `true` or `false` |
| `CHART_DATETIME_FORMAT` | No | Set the formatting of timestamps in charts. Formatting: [PHP DateTime](https://www.php.net/manual/en/datetime.format.php) | `j/m G:i` (18/10 20:06) |
| `DATETIME_FORMAT` | No | Set the formatting of timestamps in tables and notifications. Formatting: [PHP DateTime](https://www.php.net/manual/en/datetime.format.php) | `j M Y, G:i:s` (18 Oct 2024, 20:06:01) |
| `DISPLAY_TIMEZONE` | No | Display timestamps in your local time. | `America/New_York` |
| `CONTENT_WIDTH` | No | Width of the content section of each page. Can be set to any value found in the Filament [docs](https://filamentphp.com/docs/4.x/panel-configuration#customizing-the-maximum-content-width). Default: `7xl` | |
| `PUBLIC_DASHBOARD` | No | Enables the public dashboard for guest (unauthenticated) users. Default: `false` | |
| `DEFAULT_CHART_RANGE` | No | Set the default time range for the dashboards. Default: `24h` | Options: `24h`, `week` or `month` |

## Speed tests

| Name | Required | Description | Example |
| ---- | -------- | ----------- | ------- |
| `SPEEDTEST_SKIP_IPS` | No | A comma separated list of public IP addresses where tests will be skipped when present. | `127.0.0.1` or `127.0.0.0/16` |
| `SPEEDTEST_SCHEDULE` | No | Cron expression used to run speedtests on a scheduled basis. [crontab.guru](https://crontab.guru/) is a helpful tool. | `6 */2 * * *` (At minute 6 past every 2nd hour) |
| `SPEEDTEST_SERVERS` | No | Comma separated list of server IDs to randomly use for speedtest. To find servers near you visit: [speedtest-servers-static.php](https://c.speedtest.net/speedtest-servers-static.php) | `52365` or `36998,52365` |
| `SPEEDTEST_BLOCKED_SERVERS` | No | Comma separated list of server IDs that should not be used when running an Ookla Speedtest. | |
| `SPEEDTEST_INTERFACE` | No | Set the network interface to use for the test. This need to be the network interface available inside the container | `eth0` |
| `SPEEDTEST_EXTERNAL_IP_URL` | No | URL of a service used to get the external WAN IP address. | |
| `SPEEDTEST_INTERNET_CHECK_HOSTNAME` | No | Hostname used to ping for an active internet connection. | |
| `THRESHOLD_ENABLED` | No | Enable the thresholds. Note: Only effective during initial setup. | `true` |
| `THRESHOLD_DOWNLOAD` | No | Set the Download Threshold. Note: Only effective during initial setup. | `900` |
| `THRESHOLD_UPLOAD` | No | Set the Upload Threshold. Note: Only effective during initial setup. | `900` |
| `THRESHOLD_PING` | No | Set the Ping Threshold. Note: Only effective during initial setup. | `25` |
| `PRUNE_RESULTS_OLDER_THAN` | No | Set the value to greater than zero to prune stored results. This value should be represented in days, e.g. `7` will purge all results over 7 days old. | `7` |

## API

| Name | Required | Description | Example |
| ---- | -------- | ----------- | ------- |
| `API_RATE_LIMIT` | No | Number of requests per minute to the API. Default: `60` | `100` |
| `API_MAX_RESULTS` | No | Sets the maximum number of results returned by API. Default: `500` | `500` |
