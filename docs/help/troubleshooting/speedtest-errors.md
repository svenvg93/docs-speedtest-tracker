---
title: Speedtest Errors
description: Troubleshoot speedtest execution, server selection, and connectivity issues.
icon: lucide/zap
---

# Speedtest Errors

This page covers errors related to running speedtests, server selection, and the Ookla CLI.

## Connectivity Errors

??? question "Failed to connected to hostname"

    When a speedtest is being processed, Speedtest Tracker will make a ICMP ping to [icanhazip.com](http://icanhazip.com) to check if there is an internet connection before starting the Speedtest.

    **Possible reasons:**

    - There is a docker network problem or no internet connection
    - Some DNS block lists will block this domain, if you're getting errors and your server has access to the internet you'll need to add this to your allow lists
    - _Most_ Docker setups can send ICMP requests without needed elevated privileges on the host or in the container. That being said if your Docker user doesn't run with elevated permissions or doesn't belong to the Docker group you can get a failure on this step. To allow the user to send ICMP requests you need to add the permission to the container.

    **Configuration options:**

    - Use available [Environment Variables](../../getting-started/configuration/environment-variables.md#speed-tests) to change the endpoint to your liking

??? question "Failed to fetch external IP address"

    When the `SPEEDTEST_SKIP_IPS` environment variable is set, Speedtest Tracker will make a call to [http://icanhazip.com](http://icanhazip.com/) to get your external IP address. This is done to check if your external IP address (WAN IP) should be skipped.

    **Possible reasons:**

    - There is a docker network problem or no internet connection
    - Some DNS block lists will block this domain, if you're getting errors and your server has access to the internet you'll need to add this to your allow lists

    **Configuration options:**

    - Use available [Environment Variables](../../getting-started/configuration/environment-variables.md#speed-tests) to change the endpoint to your liking

    !!! warning

        Whatever service you choose needs to only return an IP address in the body of the response for this to work.

## Ookla CLI Errors

??? question "Configuration - Could not retrieve or read configuration (ConfigurationError)"

    This is usually thrown when the CLI fails to reach the internet (internet down) or the specified server.

    **Troubleshooting:**

    1. Check your internet connection
    2. Verify Docker network configuration
    3. Test connectivity: `docker exec speedtest-tracker ping -c 4 speedtest.net`
    4. Check container logs for more details

??? question "Configuration - No servers defined (NoServersException)"

    This usually means the defined server is no longer available. Remove it from your server list and try testing with a different server.

    **Solution:**

    1. Go to Settings → Speedtest in the web interface
    2. Remove the unavailable server from your server list
    3. Add a different server or let it auto-select
    4. Run a new test

??? question "Server Selection - Failed to find a working test server (NoServers)"

    Not 100% sure what causes this exception yet but it's likely when the CLI can't locate a local server. You should specify a list of servers to see if that addresses the issue.

    **Solution:**

    1. Go to Settings → Speedtest in the web interface
    2. Manually specify a list of preferred servers
    3. Choose servers close to your location
    4. Save and run a new test

??? question "Unable to retrieve Ookla servers, check internet connection and see logs"

    This error is shown when we try to retrieve the Ookla server list when selecting a server when running a manual speedtest. We get the list from: [https://www.speedtest.net/api/js/servers](https://www.speedtest.net/api/js/servers).

    This error is usually caused by a docker network problem or no internet connection.

    **Troubleshooting:**

    ```bash
    # Check container can reach the internet
    docker exec speedtest-tracker ping -c 4 speedtest.net

    # Check DNS resolution
    docker exec speedtest-tracker nslookup speedtest.net

    # View detailed logs
    docker logs speedtest-tracker
    ```

    **Common fixes:**

    - Verify Docker network configuration
    - Check firewall rules aren't blocking outbound connections
    - Ensure DNS is properly configured in the container

## Test Quality Issues

??? question "Scheduled tests give lower results than manual tests"

    Starting your cron schedule at an off-peak minute can help reduce network congestion or avoid overloading a speed test server.

    **Solution:**

    Instead of scheduling at exactly `:00` or `:30`, try scheduling at random minutes like `:07` or `:37`:

    ```
    # Instead of: 0 * * * * (every hour at :00)
    # Use: 7 * * * * (every hour at :07)
    ```

    This [comment on GitHub](https://github.com/alexjustesen/speedtest-tracker/issues/552#issuecomment-2028532010) can help you get the formatting right.

## Network Configuration

??? question "Tests are failing behind a proxy or VPN"

    If you're running Speedtest Tracker behind a proxy or VPN, the speedtests may fail or return unexpected results.

    **Things to check:**

    1. **Proxy configuration** - Ensure the container can bypass the proxy for speedtest traffic if needed
    2. **VPN routing** - Verify the VPN isn't interfering with speedtest traffic
    3. **Firewall rules** - Check that required ports aren't blocked
    4. **Docker network mode** - Consider using `host` network mode if appropriate

    **Test connectivity:**

    ```bash
    # Test from inside the container
    docker exec speedtest-tracker ping -c 4 google.com
    docker exec speedtest-tracker curl -I https://speedtest.net
    ```

## Still Having Issues?

If you can't resolve the problem:

1. Check the [container logs](index.md#check-container-status) for detailed error messages
2. Enable [debug mode](index.md#enable-debug-mode) for more information
3. Review [environment variables](../../getting-started/configuration/environment-variables.md#speed-tests) for speedtest configuration
4. Check [GitHub Issues](https://github.com/alexjustesen/speedtest-tracker/issues) for similar problems
5. Open a new issue with logs and configuration details (remove sensitive data)
