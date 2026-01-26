---
title: Docker Run
description: These instructions will run you through setting up Speedtest Tracker on a Docker server using Docker run.
icon: lucide/container
tags:
  - installation
  - docker
---

# Docker

Setting up your environment with Docker Compose is the recommended way as it will set up the application and a database for you. These steps will guide you through setting up the application using Docker run commands.

!!! info

    Docker run commands assume you already have a database installed and configured.

## Generate an Application Key

Run the command below to generate a key, the key is required for [encryption](../security/encryption.md). Copy this key including the `base64:` prefix and paste it as your `APP_KEY` value.

```bash
echo -n 'base64:'; openssl rand -base64 32;
```
For Example:
```
base64:j+cdcxP3SV7Ja85jrW8f7uwdkp99mRdxtKu2wF8cwcs=
```

## Setting Up Docker

SQLite is fine for most installs but you can also use more traditional relational databases like MariaDB, MySQL and Postgres.

!!! tip
    Please make sure the highlighted values are filled in — each one is required for the application to work properly.

=== "SQLite"

    ```bash hl_lines="4 5 6 7 11 12"
    docker run -d --name speedtest-tracker --restart unless-stopped \
        -p 8080:80 \
        -p 8443:443 \
        -e PUID= \ # (1)!
        -e PGID= \ # (2)!
        -e APP_KEY= \ # (3)!
        -e APP_URL= \ # (4)!
        -e DB_CONNECTION=sqlite \
        -e SPEEDTEST_SCHEDULE= \ # (5)!
        -e SPEEDTEST_SERVERS= \ # (6)!
        -v /path/to/data:/config \ # (7)!
        -v /path/to-custom-ssl-keys:/config/keys \ # (8)!
        lscr.io/linuxserver/speedtest-tracker:latest
    ```

    1. Your user ID - run `id -u` to find it
    2. Your group ID - run `id -g` to find it
    3. Generate with: `echo -n 'base64:'; openssl rand -base64 32`
    4. The URL where you'll access the app (e.g., `http://localhost:8080`)
    5. (Optional) Cron expression for when to run tests (e.g., `"0 */2 * * *"` for every 2 hours)
    6. (Optional) Comma separated server IDs to use (e.g., `"52365"` or `"36998,52365"`)
    7. Change to an actual path on your system (e.g., `./data:/config`)
    8. (Optional) Change to your SSL keys path, or remove if not using HTTPS

=== "MariaDB"

    ```bash hl_lines="4 5 6 7 9 12 13 16 17"
    docker run -d --name speedtest-tracker --restart unless-stopped \
        -p 8080:80 \
        -p 8443:443 \
        -e PUID= \ # (1)!
        -e PGID= \ # (2)!
        -e APP_KEY= \ # (3)!
        -e APP_URL= \ # (4)!
        -e DB_CONNECTION=mariadb \
        -e DB_HOST= \ # (5)!
        -e DB_PORT=3306 \
        -e DB_DATABASE=speedtest_tracker \
        -e DB_USERNAME= \ # (6)!
        -e DB_PASSWORD= \ # (7)!
        -e SPEEDTEST_SCHEDULE= \ # (8)!
        -e SPEEDTEST_SERVERS= \ # (9)!
        -v /path/to/data:/config \ # (10)!
        -v /path/to-custom-ssl-keys:/config/keys \ # (11)!
        lscr.io/linuxserver/speedtest-tracker:latest
    ```

    1. Your user ID - run `id -u` to find it
    2. Your group ID - run `id -g` to find it
    3. Generate with: `echo -n 'base64:'; openssl rand -base64 32`
    4. The URL where you'll access the app (e.g., `http://localhost:8080`)
    5. Your MariaDB server hostname or IP address
    6. Your database username
    7. Your database password
    8. (Optional) Cron expression for when to run tests (e.g., `"0 */2 * * *"` for every 2 hours)
    9. (Optional) Comma separated server IDs to use (e.g., `"52365"` or `"36998,52365"`)
    10. Change to an actual path on your system (e.g., `./data:/config`)
    11. (Optional) Change to your SSL keys path, or remove if not using HTTPS

=== "MySQL"

    ```bash hl_lines="4 5 6 7 9 12 13 16 17"
    docker run -d --name speedtest-tracker --restart unless-stopped \
        -p 8080:80 \
        -p 8443:443 \
        -e PUID= \ # (1)!
        -e PGID= \ # (2)!
        -e APP_KEY= \ # (3)!
        -e APP_URL= \ # (4)!
        -e DB_CONNECTION=mysql \
        -e DB_HOST= \ # (5)!
        -e DB_PORT=3306 \
        -e DB_DATABASE=speedtest_tracker \
        -e DB_USERNAME= \ # (6)!
        -e DB_PASSWORD= \ # (7)!
        -e SPEEDTEST_SCHEDULE= \ # (8)!
        -e SPEEDTEST_SERVERS= \ # (9)!
        -v /path/to/data:/config \ # (10)!
        -v /path/to-custom-ssl-keys:/config/keys \ # (11)!
        lscr.io/linuxserver/speedtest-tracker:latest
    ```

    1. Your user ID - run `id -u` to find it
    2. Your group ID - run `id -g` to find it
    3. Generate with: `echo -n 'base64:'; openssl rand -base64 32`
    4. The URL where you'll access the app (e.g., `http://localhost:8080`)
    5. Your MySQL server hostname or IP address
    6. Your database username
    7. Your database password
    8. (Optional) Cron expression for when to run tests (e.g., `"0 */2 * * *"` for every 2 hours)
    9. (Optional) Comma separated server IDs to use (e.g., `"52365"` or `"36998,52365"`)
    10. Change to an actual path on your system (e.g., `./data:/config`)
    11. (Optional) Change to your SSL keys path, or remove if not using HTTPS

=== "Postgres"

    ```bash hl_lines="4 5 6 7 9 12 13 16 17"
    docker run -d --name speedtest-tracker --restart unless-stopped \
        -p 8080:80 \
        -p 8443:443 \
        -e PUID= \ # (1)!
        -e PGID= \ # (2)!
        -e APP_KEY= \ # (3)!
        -e APP_URL= \ # (4)!
        -e DB_CONNECTION=pgsql \
        -e DB_HOST= \ # (5)!
        -e DB_PORT=5432 \
        -e DB_DATABASE=speedtest_tracker \
        -e DB_USERNAME= \ # (6)!
        -e DB_PASSWORD= \ # (7)!
        -e SPEEDTEST_SCHEDULE= \ # (8)!
        -e SPEEDTEST_SERVERS= \ # (9)!
        -v /path/to/data:/config \ # (10)!
        -v /path/to-custom-ssl-keys:/config/keys \ # (11)!
        lscr.io/linuxserver/speedtest-tracker:latest
    ```

    1. Your user ID - run `id -u` to find it
    2. Your group ID - run `id -g` to find it
    3. Generate with: `echo -n 'base64:'; openssl rand -base64 32`
    4. The URL where you'll access the app (e.g., `http://localhost:8080`)
    5. Your Postgres server hostname or IP address
    6. Your database username
    7. Your database password
    8. (Optional) Cron expression for when to run tests (e.g., `"0 */2 * * *"` for every 2 hours)
    9. (Optional) Comma separated server IDs to use (e.g., `"52365"` or `"36998,52365"`)
    10. Change to an actual path on your system (e.g., `./data:/config`)
    11. (Optional) Change to your SSL keys path, or remove if not using HTTPS

??? tip "Want to use HTTPS?"
    Provide your own SSL keys, they must be named `cert.crt` (full chain) and `cert.key` (private key), and mounted in the container folder `/config/keys`.

??? tip "Monitor container health"

    The application provides a healthcheck endpoint at `/api/healthcheck` that returns a 200 status code when running properly. You can use this endpoint to monitor your container's status with external monitoring tools or orchestration platforms.

    ```bash
    curl http://localhost:8080/api/healthcheck
    ```

## Environment Variables

The examples above include the required environment variables. For additional configuration options like [Display](../configuration/environment-variables.md#display) and other settings, see the complete [Environment Variables](../configuration/environment-variables.md) reference.

## Start the Container

Run the Docker command from the appropriate tab above to start your container. The container will start automatically and begin running in the background.

## First Login

When the container starts for the first time, a default username and password are created. Use the [default login](../security/authentication.md#default-user-account) credentials to login to the application. You can [change the default user](../security/authentication.md#change-account-details) after logging in.
