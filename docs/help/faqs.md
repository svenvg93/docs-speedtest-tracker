---
title: Frequently Asked Questions
description: A running list of frequently asked questions and their answers.
icon: lucide/help-circle
---

# Frequently Asked Questions

Common questions and answers about Speedtest Tracker setup and usage.

## Installation & Setup

??? question "I get a warning on container start up that the APP_KEY is missing"

    The `APP_KEY` is required for encryption and security.

    **Solution:**

    1. Generate a key using: `echo -n 'base64:'; openssl rand -base64 32`
    2. Add it to your `docker-compose.yml` or docker run command: `APP_KEY=base64:your-generated-key`
    3. Restart the container

    See the [installation docs](../getting-started/installation/docker-compose.md#generate-an-application-key) for detailed instructions.

??? question "How do I access Speedtest Tracker after installation?"

    By default, Speedtest Tracker is accessible at:

    - **HTTP:** `http://your-server-ip:8080`
    - **HTTPS:** `https://your-server-ip:8443`

    Use the [default login credentials](../getting-started/security/authentication.md#default-user-account) on first access.

??? question "Can I change the default ports?"

    Yes! In your `docker-compose.yml`, modify the port mapping:

    ```yaml
    ports:
      - 9090:80  # Change 9090 to your desired port
      - 9443:443 # Change 9443 to your desired HTTPS port
    ```

    Restart the container after making changes.

## Database & Data

??? question "Which database should I use?"

    **For most users:** SQLite (default) is perfectly fine and requires no additional setup.

    **Use MariaDB/MySQL/Postgres if:**

    - You expect high traffic or many concurrent users
    - You want to run multiple instances
    - You need advanced database features

    See [Database Drivers](../getting-started/configuration/database-drivers.md) for more information.

??? question "Can I migrate from SQLite to MySQL/Postgres?"

    Yes, but it requires manual migration. The recommended approach:

    1. Export your existing data
    2. Set up a new instance with your preferred database
    3. Import the data

    **Note:** There's no automated migration tool currently available.

??? question "Where is my data stored?"

    Your data is stored in the volume you mounted to `/config`:

    - **SQLite database:** `/config/database/speedtest.db`
    - **Configuration files:** `/config`
    - **Logs:** Check with `docker logs speedtest-tracker`

## Notifications

??? question "Links in emails don't point to the correct URL"

    **Problem:** Notification links show incorrect URLs or localhost addresses.

    **Solution:**

    1. Set the correct URL as the `APP_URL` environment variable: `APP_URL=https://speedtest.yourdomain.com`
    2. Restart the container
    3. Test by triggering a new notification

??? question "I'm getting duplicate message via Apprise"

    By default when sending an notifications via Apprise we wait up to 30 seconds for Apprise to respond back with any message. Incase this 30 seconds is exceeded, we will retry 3 times. In case of any very slow Apprise processing this might cause duplicated notifications. Please check the [logs](error-messages.md#troubleshooting) to see the the timeout happend

## Time Zones

??? question "How do I set the display and schedule time zone?"

    1. Set `DISPLAY_TIMEZONE` environment variables to your local timezone.
    2. Restart the container

??? question "My display timestamps or scheduled tests aren't correct"

    Speedtest Tracker assumes your application and database containers are set to `UTC` by default. If your database instance has your local time zone set it needs to **match** that set in `APP_TIMEZONE` and `DISPLAY_TIMEZONE` environment variables.

    Once set restart the container.

## Speedtest

??? question "Scheduled tests give lower results then manual tests"

    Starting your cron schedule at an off-peak minute can help reduce network congestion or avoid overloading a speed test server. This [comment](https://github.com/alexjustesen/speedtest-tracker/issues/552#issuecomment-2028532010) on this issue can help you get the formatting right.
