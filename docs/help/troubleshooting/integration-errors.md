---
title: Integration Errors
description: Troubleshoot data exports, notifications, and third-party integrations.
icon: lucide/plug
---

# Integration Errors

This page covers errors related to data exports (InfluxDB, Prometheus), notifications, and third-party integrations.

## InfluxDB Integration

??? question "Failed to bulk write to InfluxDB"

    When Speedtest Tracker fails to write data to InfluxDB this error is shown. The [container logs](index.md#check-container-status) will show more details on why it failed.

    **Possible reasons:**

    - Connectivity problem to InfluxDB
    - Problem with authentication
    - Specified bucket does not exist in InfluxDB
    - Wrong InfluxDB version (v2 required)

    **Troubleshooting steps:**

    1. **Verify connectivity:**
    ```bash
    # From the speedtest-tracker container, test connection to InfluxDB
    docker exec speedtest-tracker curl -I http://<INFLUXDB_HOST>:8086/health
    ```

    2. **Check authentication:**
       - Verify `INFLUXDB_TOKEN` is correct
       - Ensure token has write permissions to the bucket
       - Check token hasn't expired

    3. **Verify bucket exists:**
       - Log into InfluxDB UI
       - Navigate to Data → Buckets
       - Ensure the bucket specified in `INFLUXDB_BUCKET` exists

    4. **Check Docker network:**
       - If using Docker Compose, ensure both containers are on the same network
       - Verify `INFLUXDB_HOST` uses the correct container name or IP

??? question "Failed to write test data to InfluxDB"

    When Speedtest Tracker fails to write data to InfluxDB this error is shown. The [container logs](index.md#check-container-status) will show more details on why it failed.

    **Possible reasons:**

    - Connectivity problem to InfluxDB
    - Problem with authentication
    - Specified bucket does not exist in InfluxDB

    **Solution:**

    See the troubleshooting steps in "Failed to bulk write to InfluxDB" above.

??? question "Failed to write to InfluxDB"

    When Speedtest Tracker fails to write data to InfluxDB this error is shown. The [container logs](index.md#check-container-status) will show more details on why it failed.

    **Possible reasons:**

    - Connectivity problem to InfluxDB
    - Problem with authentication
    - Specified bucket does not exist in InfluxDB

    **Solution:**

    See the troubleshooting steps in "Failed to bulk write to InfluxDB" above.

## Notification Errors

??? question "Email notifications aren't being sent"

    **Common causes:**

    1. **SMTP configuration incorrect**
       - Verify `MAIL_HOST`, `MAIL_PORT`, `MAIL_USERNAME`, `MAIL_PASSWORD`
       - Check `MAIL_ENCRYPTION` is set correctly (`tls` or `ssl`)
       - Ensure `MAIL_FROM_ADDRESS` is valid

    2. **Firewall blocking SMTP**
       - Check port 587 (TLS) or 465 (SSL) is allowed
       - Test from container: `docker exec speedtest-tracker telnet <MAIL_HOST> <MAIL_PORT>`

    3. **Authentication failure**
       - Verify username/password are correct
       - Some providers require app-specific passwords (Gmail, Outlook)

    **Troubleshooting:**

    ```bash
    # Enable debug mode to see detailed SMTP errors
    # Add to environment variables:
    APP_DEBUG=true

    # View logs for SMTP errors
    docker logs speedtest-tracker
    ```

??? question "I'm getting duplicate messages via Apprise"

    By default when sending notifications via Apprise we wait up to 30 seconds for Apprise to respond back with any message. In case this 30 seconds is exceeded, we will retry 3 times. In case of any very slow Apprise processing this might cause duplicated notifications.

    **Solution:**

    1. Check the [logs](index.md#check-container-status) to see if the timeout happened
    2. Look for messages indicating Apprise timeout or retry attempts
    3. Consider optimizing your Apprise configuration or notification services
    4. If a specific service is slow, consider removing it or increasing timeout tolerance

??? question "Webhook notifications are failing"

    **Troubleshooting steps:**

    1. **Verify webhook URL:**
       - Ensure the URL is correct and accessible
       - Test the endpoint manually with curl

    2. **Check response codes:**
       - View container logs to see HTTP response codes
       - Most webhook services expect a 200 response

    3. **Test connectivity:**
    ```bash
    # Test from inside the container
    docker exec speedtest-tracker curl -X POST <WEBHOOK_URL> \
      -H "Content-Type: application/json" \
      -d '{"test": "message"}'
    ```

    4. **Review webhook service logs:**
       - Check the receiving service's logs for errors
       - Verify the payload format is correct

??? question "Notification links point to the wrong URL"

    **Problem:** Notification links show incorrect URLs or localhost addresses.

    **Solution:**

    1. Set the correct URL as the `APP_URL` environment variable: `APP_URL=https://speedtest.yourdomain.com`
    2. Also set `ASSET_URL` to the same value
    3. Restart the container
    4. Test by triggering a new notification

## Prometheus Integration

??? question "Prometheus can't scrape metrics"

    **Troubleshooting steps:**

    1. **Verify metrics endpoint is accessible:**
    ```bash
    # From Prometheus host, test the endpoint
    curl http://<SPEEDTEST_TRACKER_HOST>:8080/metrics
    ```

    2. **Check Prometheus configuration:**
       - Ensure the job is configured correctly in `prometheus.yml`
       - Verify the target address and port
       - Check scrape interval isn't too aggressive

    3. **Review Prometheus logs:**
    ```bash
    # Check Prometheus logs for scrape errors
    docker logs prometheus
    ```

    4. **Verify Docker network:**
       - If using Docker Compose, ensure containers are on the same network
       - Check firewall rules aren't blocking the connection

## General Integration Issues

??? question "Integration works intermittently"

    **Common causes:**

    1. **Network instability:**
       - Check Docker network health
       - Verify DNS resolution is stable
       - Test connectivity over time

    2. **Resource constraints:**
       - Check container resource usage: `docker stats speedtest-tracker`
       - Ensure sufficient memory and CPU available
       - Review host system resources

    3. **Rate limiting:**
       - Some services rate-limit API requests
       - Check service documentation for limits
       - Consider reducing notification frequency

??? question "Data isn't syncing to external service"

    **Troubleshooting checklist:**

    - [ ] Verify environment variables are set correctly
    - [ ] Check both containers are running: `docker ps`
    - [ ] Test network connectivity between containers
    - [ ] Review authentication credentials
    - [ ] Check container logs for both services
    - [ ] Verify the external service is accepting data
    - [ ] Ensure data format is correct

## Still Having Issues?

If you can't resolve the problem:

1. Check the [container logs](index.md#check-container-status) for both Speedtest Tracker and the integration service
2. Enable [debug mode](index.md#enable-debug-mode) for detailed error messages
3. Review the [configuration documentation](../../getting-started/configuration/environment-variables.md)
4. Check [GitHub Issues](https://github.com/alexjustesen/speedtest-tracker/issues) for similar problems
5. Open a new issue with logs and configuration details from **both services** (remove sensitive data)
