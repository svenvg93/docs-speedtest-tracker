---
title: Help & Troubleshooting
description: Find solutions to common issues and get help with Speedtest Tracker.
icon: lucide/life-buoy
---

# Help & Troubleshooting

Need help with Speedtest Tracker? This section contains answers to common questions and solutions to known issues.

## Quick Links

### [Frequently Asked Questions](faqs.md)
Common questions about Docker setup, notifications, timezones, and speedtest scheduling.

**Popular topics:**
- Setting up APP_KEY
- Configuring notifications
- Timezone configuration
- Speedtest scheduling tips

### [Error Messages](error-messages.md)
Detailed explanations of error messages and how to resolve them.

**Common errors:**
- 500 Server Error
- APP_KEY issues
- Speedtest process failures
- InfluxDB connection problems

## Getting Help

### Check the Logs
Most issues can be diagnosed by checking the container logs:

```bash
docker logs speedtest-tracker
```

### Enable Debug Mode
For detailed error information:

1. Set `APP_DEBUG=true` in your environment variables
2. Restart the container
3. Reproduce the issue
4. Check logs for detailed error messages
5. Remove `APP_DEBUG` once resolved

### Still Need Help?

If you can't find a solution here:

1. **Search existing issues:** Check if someone else has reported the same problem
2. **Open a new issue:** [GitHub Issues](https://github.com/alexjustesen/speedtest-tracker/issues)
3. **Provide details:** Include logs, error messages, and your configuration (remove sensitive data)

!!! tip "Before Opening an Issue"
    - Check that you're using a [supported installation method](../getting-started/index.md)
    - Verify all required environment variables are set
    - Review the [configuration documentation](../getting-started/configuration/environment-variables.md)
