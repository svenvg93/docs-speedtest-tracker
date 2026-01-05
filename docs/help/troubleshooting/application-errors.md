---
title: Application Errors
description: Troubleshoot web interface, authentication, and core application issues.
icon: lucide/alert-triangle
---

# Application Errors

This page covers errors related to the web interface, authentication, and core application functionality.

## Server Errors

??? question "I'm getting a `500 | SERVER ERROR` error"

    The `500 | SERVER ERROR` is caused by either a bug or a misconfiguration. You must enable debugging to determine the exact cause of the error.

    **To enable debugging:**

    1. Add `APP_DEBUG=true` to your environment variables
    2. Restart the container: `docker restart speedtest-tracker`
    3. Reproduce the error
    4. Check the logs - look for lines starting with `[timestamp] production.ERROR:`
    5. Use the detailed error information to diagnose the issue
    6. **Remove `APP_DEBUG=true` when done** for security

    If you can't resolve the issue, [open a GitHub issue](https://github.com/alexjustesen/speedtest-tracker/issues) with the error details.

## Encryption & Security

??? question "Unsupported cipher or incorrect key length"

    **Error:** Supported ciphers are: `aes-128-cbc`, `aes-256-cbc`, `aes-128-gcm`, `aes-256-gcm`.

    This error is shown when the `APP_KEY` is not set or not set correctly.

    **Solution:**

    1. Generate a key: `echo -n 'base64:'; openssl rand -base64 32`
    2. Add it to your environment variables: `APP_KEY=base64:your-generated-key`
    3. Restart the container

    See the [installation steps](../../getting-started/installation/docker-compose.md#generate-an-application-key) for detailed instructions.

??? question "I get a warning on container start up that the APP_KEY is missing"

    The `APP_KEY` is required for encryption and security.

    **Solution:**

    1. Generate a key using: `echo -n 'base64:'; openssl rand -base64 32`
    2. Add it to your `docker-compose.yml` or docker run command: `APP_KEY=base64:your-generated-key`
    3. Restart the container

    See the [installation docs](../../getting-started/installation/docker-compose.md#generate-an-application-key) for detailed instructions.

## Authentication Issues

??? question "Login problems or can't access the web interface"

    **Common causes:**

    1. **Using wrong credentials** - Check the [default login credentials](../../getting-started/security/authentication.md#default-user-account)
    2. **APP_KEY not set** - See the cipher error above
    3. **Wrong APP_URL** - Verify `APP_URL` matches how you access the app
    4. **Container not running** - Check with `docker ps | grep speedtest-tracker`

    **Troubleshooting steps:**

    ```bash
    # Check if container is running
    docker ps | grep speedtest-tracker

    # View logs for errors
    docker logs speedtest-tracker

    # Verify environment variables
    docker inspect speedtest-tracker | grep -A 20 Env
    ```

## Configuration Issues

??? question "Links in emails don't point to the correct URL"

    **Problem:** Notification links show incorrect URLs or localhost addresses.

    **Solution:**

    1. Set the correct URL as the `APP_URL` environment variable: `APP_URL=https://speedtest.yourdomain.com`
    2. Restart the container
    3. Test by triggering a new notification

??? question "My display timestamps or scheduled tests aren't correct"

    Speedtest Tracker assumes your application and database containers are set to `UTC` by default. If your database instance has your local time zone set it needs to **match** that set in `APP_TIMEZONE` and `DISPLAY_TIMEZONE` environment variables.

    **Solution:**

    1. Set `DISPLAY_TIMEZONE` environment variable to your local timezone
    2. Ensure `APP_TIMEZONE` matches your database timezone
    3. Restart the container

## Database Issues

??? question "Database connection errors"

    **For external databases (MySQL/MariaDB/Postgres):**

    ```bash
    # Test database connection
    docker exec speedtest-tracker php artisan db:monitor

    # Or check manually
    mysql -h <DB_HOST> -u <DB_USERNAME> -p<DB_PASSWORD> <DB_DATABASE>
    ```

    **Common causes:**

    - Incorrect `DB_HOST`, `DB_USERNAME`, `DB_PASSWORD`, or `DB_DATABASE`
    - Database container not running or not on the same network
    - Database user doesn't have proper permissions
    - Wrong `DB_CONNECTION` type specified

    **Solution:**

    1. Verify all database environment variables are correct
    2. Check database container is running: `docker ps`
    3. Verify containers are on the same Docker network
    4. Check database user has proper permissions

## Still Having Issues?

If you can't resolve the problem:

1. Enable [debug mode](#server-errors) and check the logs
2. Review the [general troubleshooting steps](index.md#general-troubleshooting-steps)
3. Check [GitHub Issues](https://github.com/alexjustesen/speedtest-tracker/issues) for similar problems
4. Open a new issue with logs and configuration details (remove sensitive data)
