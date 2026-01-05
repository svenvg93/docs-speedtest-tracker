---
title: Troubleshooting
description: Diagnose and resolve issues with Speedtest Tracker.
icon: lucide/wrench
---

# Troubleshooting

Having issues with Speedtest Tracker? This section will help you diagnose and fix common problems.

## Quick Diagnostics

### Check Container Status

```bash
# Check if container is running
docker ps | grep speedtest-tracker

# View container logs
docker logs speedtest-tracker

# Follow logs in real-time
docker logs -f speedtest-tracker
```

### Enable Debug Mode

For detailed error information:

1. Add `APP_DEBUG=true` to your environment variables
2. Restart the container: `docker restart speedtest-tracker`
3. Reproduce the issue
4. Check logs for detailed error messages
5. **Remove `APP_DEBUG=true` when done** for security

## Common Issues by Category

### [Application Errors](application-errors.md)
Issues with the web interface, authentication, and core application functionality.

**Common problems:**
- 500 Server Error
- APP_KEY issues
- Cipher errors
- Login problems

### [Speedtest Errors](speedtest-errors.md)
Issues running speedtests, server selection, and test failures.

**Common problems:**
- Failed to connect errors
- Server selection issues
- Ookla CLI errors
- Network connectivity problems

### [Integration Errors](integration-errors.md)
Issues with data exports, notifications, and third-party integrations.

**Common problems:**
- InfluxDB connection failures
- Notification delivery issues
- Apprise problems
- Webhook failures

## General Troubleshooting Steps

### 1. Verify Environment Variables

Check that all required variables are set correctly:

```bash
docker inspect speedtest-tracker | grep -A 20 Env
```

Required variables:
- `APP_KEY` - Must be properly formatted with `base64:` prefix
- `APP_URL` - Should match how you access the application
- `PUID` / `PGID` - Should match your host user
- `DB_CONNECTION` - Must be valid (sqlite, mysql, pgsql, mariadb)

### 2. Check Docker Network

Ensure containers can communicate:

```bash
# List networks
docker network ls

# Inspect network
docker network inspect <network-name>
```

### 3. Verify Permissions

Check file permissions on your data volume:

```bash
ls -la /path/to/data
```

The directory should be owned by the user specified in `PUID:PGID`.

### 4. Test Database Connection

For external databases:

```bash
# MySQL/MariaDB
docker exec speedtest-tracker php artisan db:monitor

# Or check manually
mysql -h <DB_HOST> -u <DB_USERNAME> -p<DB_PASSWORD> <DB_DATABASE>
```

## Still Need Help?

If you can't resolve the issue:

1. **Gather information:**
   - Container logs (with `APP_DEBUG=true`)
   - Docker compose file (remove sensitive data)
   - Environment variables (remove sensitive data)
   - Steps to reproduce the issue

2. **Search existing issues:**
   [GitHub Issues](https://github.com/alexjustesen/speedtest-tracker/issues)

3. **Open a new issue:**
   Provide all gathered information and clearly describe the problem

!!! tip "Before Opening an Issue"
    - Verify you're using a [supported installation method](../../getting-started/index.md)
    - Check you're on the latest version
    - Review [configuration documentation](../../getting-started/configuration/environment-variables.md)
