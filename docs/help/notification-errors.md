---
title: Notifications
description: Troubleshoot notification delivery and configuration issues.
icon: lucide/bell
---

# Notification Errors

This page covers errors related to email notifications, webhooks, and third-party notification services.

??? question "Links in notificatons don't point to the correct URL"

    **Problem:** Notification links show incorrect URLs or localhost addresses.

    **Solution:**

    1. Set the correct URL as the `APP_URL` environment variable: `APP_URL=https://speedtest.yourdomain.com`
    2. Restart the container
    3. Test by triggering a new notification

??? question "I'm getting duplicate messages via Apprise"

    By default when sending notifications via Apprise we wait up to 30 seconds for Apprise to respond back with any message. If these 30 seconds are exceeded, we will retry 3 times. Very slow Apprise processing can cause duplicate notifications.

    **Solution:**

    1. Check the [logs](index.md#check-container-logs) to see if the timeout happened
    2. Look for messages indicating Apprise timeout or retry attempts
    3. Consider optimizing your Apprise configuration or notification services
    4. If a specific service is slow, consider removing it or increasing timeout tolerance

## Email Notifications

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

## Webhook Notifications

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

## Need More Help?

If you can't resolve the problem:

1. Check the [container logs](index.md#check-container-logs) for detailed error messages
2. Enable [debug mode](index.md#enable-debug-mode) for more information
3. Review the [configuration documentation](../../getting-started/configuration/environment-variables.md)
4. Check [GitHub Issues](https://github.com/alexjustesen/speedtest-tracker/issues) for similar problems
5. Open a new issue with logs and configuration details (remove sensitive data)