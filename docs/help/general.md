---
title: General
description: Find solutions to common issues and get help with Speedtest Tracker.
icon: lucide/life-buoy
tags:
  - help
  - troubleshooting
  - overview
---

# Help & Troubleshooting

Need help with Speedtest Tracker? Start here to diagnose and resolve issues.

## Quick Diagnostics

### Check Container Logs

Most issues can be diagnosed by checking the container logs:

??? tip "How to check the logs"

      ```bash
      # View recent logs
      docker logs speedtest-tracker

      # Follow logs in real-time
      docker logs -f speedtest-tracker

      # View last 100 lines
      docker logs --tail 100 speedtest-tracker
      ```

### Enable Debug Mode

By default `APP_DEBUG` is set to false in production to prevent verbose error outputs.


??? tip "How to Enable Debugging"

    **To enable debugging:**

    1. Add `APP_DEBUG=true` to your environment variables
    2. Restart the container
    3. Reproduce the error
    4. Check the logs - look for lines starting with `[timestamp] production.ERROR:`
    5. Use the detailed error information to diagnose the issue
    6. **Remove `APP_DEBUG=true` when done** for security

    If you can't resolve the issue, [open a GitHub issue](https://github.com/alexjustesen/speedtest-tracker/issues) with the error details.

??? info "Need More Help?"

    If you can't resolve the problem:

    1. Check the [container logs](general.md#check-container-logs) for detailed error messages
    2. Enable [debug mode](general.md#enable-debug-mode) for more information
    3. Review the [configuration documentation](../getting-started/configuration/environment-variables.md)
    4. Search [GitHub Issues](https://github.com/alexjustesen/speedtest-tracker/issues) for similar problems
    5. [Open a new issue](https://github.com/alexjustesen/speedtest-tracker/issues/new) with logs and configuration details (remove sensitive data)
