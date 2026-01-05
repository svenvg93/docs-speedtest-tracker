---
title: Error Messages
description: Common error messages and their solutions in Speedtest Tracker.
icon: lucide/alert-circle
---

# Error Messages

This page contains common error messages you might encounter and how to resolve them.

## Quick Troubleshooting Steps

!!! tip "First Steps for Any Error"
    1. **Check container logs:** `docker logs speedtest-tracker`
    2. **Enable debug mode** (see below)
    3. **Look for the error** in the sections below
    4. **Check environment variables** are set correctly

### Viewing Logs

Check your container logs for detailed error information:

```bash
# View recent logs
docker logs speedtest-tracker

# Follow logs in real-time
docker logs -f speedtest-tracker

# View last 100 lines
docker logs --tail 100 speedtest-tracker
```

### Enable Debug Mode

??? tip "How to Enable Debugging"

    By default `APP_DEBUG` is set to `false` in production to prevent verbose error outputs.

    **To enable debugging:**

    1. Add `APP_DEBUG=true` to your environment variables
    2. Restart the container
    3. Reproduce the error
    4. Check the logs - look for lines starting with `[timestamp] production.ERROR:`
    5. Use the detailed error information to diagnose the issue
    6. **Remove `APP_DEBUG=true` when done** for security

    If you can't resolve the issue, [open a GitHub issue](https://github.com/alexjustesen/speedtest-tracker/issues) with the error details.

## Application

??? question "I'm getting a `500 | SERVER ERROR` error"

    The `500 | SERVER ERROR` is caused by either a bug or a misconfiguration. You must [enable debugging](#enable-debugging) to determine the exact cause of the error.

??? question "Unsupported cipher or incorrect key length"

    **Error:** Supported ciphers are: `aes-128-cbc`, `aes-256-cbc`, `aes-128-gcm`, `aes-256-gcm`.

    This error is shown when the `APP_KEY` is not set or not set correctly. Make sure you set the `APP_KEY` as described in the [installation steps](../getting-started/installation/docker-compose.md#generate-an-application-key).

## Speedtest Process

??? question "Failed to connected to hostname"

    When a speedtest is being processed, Speedtest Tracker will make a ICMP ping to [icanhazip.com](http://icanhazip.com) to check if there is an internet connection before starting the Speedtest

    **Possible reasons:**

    - There is a docker network problem or no internet connection.
    - Some DNS blocks lists will block this domain, if you're getting errors and your server has access to the internet you'll need to add this to your allow lists.
    - _Most_ Docker setups can send ICMP requests without needed elevated privileges on the host or in the container. That being said if your Docker user doesn't run with elevated permissions or doesn't belong to the Docker group you can get a failure on this step. To allow the user to send ICMP requests you need to add the permission to the container.

    **Configuration options:**

    - Use available [Environment Variables](../getting-started/configuration/environment-variables.md#speed-tests) to change the endpoint to your liking

??? question "Failed to fetch external IP address"

    When the `SPEEDTEST_SKIP_IPS` environment variable is set, Speedtest Tracker will make a call to [http://icanhazip.com](http://icanhazip.com/) to get your external IP address. This is done to check if your external IP address (WAN IP) should be skipped.

    **Possible reasons:**

    - There is a docker network problem or no internet connection.
    - Some DNS blocks lists will block this domain, if you're getting errors and your server has access to the internet you'll need to add this to your allow lists.

    **Configuration options:**

    - Use available [Environment Variables](../getting-started/configuration/environment-variables.md#speed-tests) to change the endpoint to your liking.

    !!! warning

        Whatever service you choose needs to only return an IP address in the body of the response for this to work.

## Ookla Related

??? question "Configuration - Could not retrieve or read configuration (ConfigurationError)"

    This is usually thrown when the CLI fails to reach the internet (internet down) or the specified server.

??? question "Configuration - No servers defined (NoServersException)"

    This usually means the defined server is no longer available. Remove it from your server list and try testing with a different server.

??? question "Server Selection - Failed to find a working test server (NoServers)"

    Not 100% sure what causes this exception yet but it's likely when the CLI can't locate a local server. You should specify a list of servers to see if that addresses the issue.

??? question "Unable to retrieve Ookla servers, check internet connection and see logs" 

    This errors is shown when we try to retrieve the Ookla server list when selecting a server when running a manual speedtest. We get the list from: [https://www.speedtest.net/api/js/servers](https://www.speedtest.net/api/js/servers).

    This error is usually caused by a docker network problem or no internet connection. You can check the [container logs](#troubleshooting) for more details.

## InfluxDB

??? question "Failed to bulk write to InfluxDB"

    When Speedtest Tracker fails to write data to InfluxDB this error is shown. The [container logs](#troubleshooting) will show more details on why it failed.

    **Possible reasons:**

    - Connectivity problem to InfluxDB
    - Problem with authentication
    - Specified bucket does not exist in InfluxDB

??? question "Failed to write test data to InfluxDB"

    When Speedtest Tracker fails to write data to InfluxDB this error is shown. The [container logs](#troubleshooting) will show more details on why it failed.

    **Possible reasons:**

    - Connectivity problem to InfluxDB
    - Problem with authentication
    - Specified bucket does not exist in InfluxDB

??? question "Failed to write to InfluxDB"

    When Speedtest Tracker fails to write data to InfluxDB this error is shown. The [container logs](#troubleshooting) will show more details on why it failed.

    **Possible reasons:**

    - Connectivity problem to InfluxDB
    - Problem with authentication
    - Specified bucket does not exist in InfluxDB
