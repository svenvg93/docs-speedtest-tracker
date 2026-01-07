---
title: Data Export
description: Troubleshoot data exports
icon: lucide/plug
---

# Data Export Errors

This page covers errors related to data exports.

## InfluxDB Integration

??? question "Failed to bulk write to InfluxDB"

    When Speedtest Tracker fails to write data to InfluxDB this error is shown. The [container logs](index.md#check-container-logs) will show more details on why it failed.

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

    When Speedtest Tracker fails to write data to InfluxDB this error is shown. The [container logs](index.md#check-container-logs) will show more details on why it failed.

    **Possible reasons:**

    - Connectivity problem to InfluxDB
    - Problem with authentication
    - Specified bucket does not exist in InfluxDB

    **Solution:**

    See the troubleshooting steps in "Failed to bulk write to InfluxDB" above.

??? question "Failed to write to InfluxDB"

    When Speedtest Tracker fails to write data to InfluxDB this error is shown. The [container logs](index.md#check-container-logs) will show more details on why it failed.

    **Possible reasons:**

    - Connectivity problem to InfluxDB
    - Problem with authentication
    - Specified bucket does not exist in InfluxDB

    **Solution:**

    See the troubleshooting steps in "Failed to bulk write to InfluxDB" above.

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

## Need More Help?

If you can't resolve the problem:

1. Check the [container logs](index.md#check-container-logs) for both Speedtest Tracker and the integration service
2. Enable [debug mode](index.md#enable-debug-mode) for detailed error messages
3. Review the [configuration documentation](../../getting-started/configuration/environment-variables.md)
4. Check [GitHub Issues](https://github.com/alexjustesen/speedtest-tracker/issues) for similar problems
5. Open a new issue with logs and configuration details from **both services** (remove sensitive data)
