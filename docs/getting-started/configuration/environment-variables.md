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
| `PUID` | :lucide-check:{ .required-yes } | Used to set the user the container should run as. | | `1000` |
| `PGID` | :lucide-check:{ .required-yes }| Used to set the group the container should run as. | | `1000` |
| `APP_KEY` | :lucide-check:{ .required-yes }| Key used to encrypt and decrypt data. See the [install](../installation/docker-compose.md#generate-an-application-key) docs to generate a key. | | |
| `APP_URL` | :lucide-check:{ .required-yes }| URL used for links in emails and notifications. | | `https://speedtest.example.com` |
| `APP_NAME` | :lucide-x:{ .required-no } | Used to define the application's name in the dashboard and in notifications. | | |
| `ADMIN_NAME` | :lucide-x:{ .required-no } | Name of the initial admin user. Note: Only effective during initial setup. | | `Admin` |
| `ADMIN_EMAIL` | :lucide-x:{ .required-no } | Email of the initial admin user. Note: Only effective during initial setup. | | `admin@example.com` |
| `ADMIN_PASSWORD` | :lucide-x:{ .required-no } | Password of the initial admin user. Note: Only effective during initial setup. | | `password` |
| `ASSET_URL` | :lucide-x:{ .required-no } | URL used for assets, needed when using a reverse proxy. | | `https://speedtest.example.com` |
| `APP_LOCALE` | :lucide-x:{ .required-no } | Change the default language. | | |
| `APP_TIMEZONE` | :lucide-x:{ .required-no } | Application timezone should be set if your database does not use UTC as its default timezone. | | `Europe/London` |
| `ALLOWED_IPS` | :lucide-x:{ .required-no } | Block requests to the application unless from the allowed addresses. | | `127.0.0.1,127.0.0.2` |

## Display

| Name | Required | Description | Default | Example |
| ---- | :------: | ----------- | ------- | ------- |
| `CHART_BEGIN_AT_ZERO` | :lucide-x:{ .required-no } | Begin the dashboard axis charts at zero. | `true` | `true` or `false` |
| `CHART_DATETIME_FORMAT` | :lucide-x:{ .required-no } | Set the formatting of timestamps in charts. Formatting: [PHP DateTime](https://www.php.net/manual/en/datetime.format.php) | | `j/m G:i` (18/10 20:06) |
| `DATETIME_FORMAT` | :lucide-x:{ .required-no } | Set the formatting of timestamps in tables and notifications. Formatting: [PHP DateTime](https://www.php.net/manual/en/datetime.format.php) | | `j M Y, G:i:s` (18 Oct 2024, 20:06:01) |
| `DISPLAY_TIMEZONE` | :lucide-x:{ .required-no } | Display timestamps in your local time. | | `America/New_York` |
| `CONTENT_WIDTH` | :lucide-x:{ .required-no } | Width of the content section of each page. Can be set to any value found in the Filament [docs](https://filamentphp.com/docs/4.x/panel-configuration#customizing-the-maximum-content-width). | `7xl` | |
| `PUBLIC_DASHBOARD` | :lucide-x:{ .required-no } | Enables the public dashboard for guest (unauthenticated) users. | `false` | |
| `DEFAULT_CHART_RANGE` | :lucide-x:{ .required-no } | Set the default time range for the dashboards. | `24h` | Options: `24h`, `week` or `month` |

## Speed tests

| Name | Required | Description | Default | Example |
| ---- | :------: | ----------- | ------- | ------- |
| `SPEEDTEST_SKIP_IPS` | :lucide-x:{ .required-no } | A comma separated list of public IP addresses where tests will be skipped when present. | | `127.0.0.1` or `127.0.0.0/16` |
| `SPEEDTEST_SCHEDULE` | :lucide-x:{ .required-no } | Cron expression used to run speedtests on a scheduled basis. [crontab.guru](https://crontab.guru/) is a helpful tool. | | `6 */2 * * *` (At minute 6 past every 2nd hour) |
| `SPEEDTEST_SERVERS` | :lucide-x:{ .required-no } | Comma separated list of server IDs to randomly use for speedtest. To find servers near you visit: [speedtest-servers-static.php](https://c.speedtest.net/speedtest-servers-static.php) | | `52365` or `36998,52365` |
| `SPEEDTEST_BLOCKED_SERVERS` | :lucide-x:{ .required-no } | Comma separated list of server IDs that should not be used when running an Ookla Speedtest. | | |
| `SPEEDTEST_INTERFACE` | :lucide-x:{ .required-no } | Set the network interface to use for the test. This need to be the network interface available inside the container | | `eth0` |
| `SPEEDTEST_EXTERNAL_IP_URL` | :lucide-x:{ .required-no } | URL of a service used to get the external WAN IP address. | | |
| `SPEEDTEST_INTERNET_CHECK_HOSTNAME` | :lucide-x:{ .required-no } | Hostname used to ping for an active internet connection. | | |
| `THRESHOLD_ENABLED` | :lucide-x:{ .required-no } | Enable the thresholds. Note: Only effective during initial setup. | | `true` |
| `THRESHOLD_DOWNLOAD` | :lucide-x:{ .required-no } | Set the Download Threshold. Note: Only effective during initial setup. | | `900` |
| `THRESHOLD_UPLOAD` | :lucide-x:{ .required-no } | Set the Upload Threshold. Note: Only effective during initial setup. | | `900` |
| `THRESHOLD_PING` | :lucide-x:{ .required-no } | Set the Ping Threshold. Note: Only effective during initial setup. | | `25` |
| `PRUNE_RESULTS_OLDER_THAN` | :lucide-x:{ .required-no } | Set the value to greater than zero to prune stored results. This value should be represented in days, e.g. `7` will purge all results over 7 days old. | | `7` |

## API

| Name | Required | Description | Default | Example |
| ---- | :------: | ----------- | ------- | ------- |
| `API_RATE_LIMIT` | :lucide-x:{ .required-no } | Number of requests per minute to the API. | `60` | `100` |
| `API_MAX_RESULTS` | :lucide-x:{ .required-no } | Sets the maximum number of results returned by API. | `500` | `500` |
