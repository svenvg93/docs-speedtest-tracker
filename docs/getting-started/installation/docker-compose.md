---
title: Docker Compose
description: These instructions will run you through setting up Speedtest Tracker on a Docker server using Docker Compose.
icon: lucide/package
tags:
  - installation
  - docker
  - docker-compose
---

# Docker Compose

Setting up your environment with Docker Compose is the recommended way as it will set up the application and a database for you. These steps will guide you through setting up the application using Docker Compose.

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
    Please make sure the highlighted environment variables are filled in — each one is required for the application to work properly.

=== "SQLite"

    ```yaml hl_lines="10 11 12 13"
    services:
        speedtest-tracker:
            image: lscr.io/linuxserver/speedtest-tracker:latest
            restart: unless-stopped
            container_name: speedtest-tracker
            ports:
                - 8080:80
                - 8443:443
            environment:
                - PUID= # (1)!
                - PGID= # (2)!
                - APP_KEY= # (3)!
                - APP_URL= # (4)!
                - DB_CONNECTION=sqlite
                - SPEEDTEST_SCHEDULE= # (5)!
                - SPEEDTEST_SERVERS= # (6)!
            volumes:
                - /path/to/data:/config
                - /path/to-custom-ssl-keys:/config/keys
    ```

    1. Your user ID - run `id -u` to find it
    2. Your group ID - run `id -g` to find it
    3. Generate with: `echo -n 'base64:'; openssl rand -base64 32`
    4. The URL where you'll access the app (e.g., `http://localhost:8080`)
    5. (Optional) Cron expression for when to run tests (e.g., `0 */2 * * *` for every 2 hours)
    6. (Optional) Comma separated server IDs to use (e.g., `52365` or `36998,52365`)

=== "MariaDB"

    ```yaml hl_lines="10 11 12 13"
    services:
        speedtest-tracker:
            image: lscr.io/linuxserver/speedtest-tracker:latest
            restart: unless-stopped
            container_name: speedtest-tracker
            ports:
                - 8080:80
                - 8443:443
            environment:
                - PUID= # (1)!
                - PGID= # (2)!
                - APP_KEY= # (3)!
                - APP_URL= # (4)!
                - DB_CONNECTION=mariadb
                - DB_HOST=db
                - DB_PORT=3306
                - DB_DATABASE=speedtest_tracker
                - DB_USERNAME=speedtest_tracker
                - DB_PASSWORD=password
                - SPEEDTEST_SCHEDULE= # (5)!
                - SPEEDTEST_SERVERS= # (6)!
            volumes:
                - /path/to/data:/config
                - /path/to-custom-ssl-keys:/config/keys
            depends_on:
                - db
        db:
            image: mariadb:11
            restart: always
            environment:
                - MYSQL_DATABASE=speedtest_tracker
                - MYSQL_USER=speedtest_tracker
                - MYSQL_PASSWORD=password
                - MYSQL_RANDOM_ROOT_PASSWORD=true
            volumes:
                - speedtest-db:/var/lib/mysql
            healthcheck:
                test: ["CMD", "healthcheck.sh", "--connect", "--innodb_initialized"]
                interval: 5s
                retries: 3
                timeout: 5s
    volumes:
    speedtest-db:
    ```

    1. Your user ID - run `id -u` to find it
    2. Your group ID - run `id -g` to find it
    3. Generate with: `echo -n 'base64:'; openssl rand -base64 32`
    4. The URL where you'll access the app (e.g., `http://localhost:8080`)
    5. (Optional) Cron expression for when to run tests (e.g., `0 */2 * * *` for every 2 hours)
    6. (Optional) Comma separated server IDs to use (e.g., `52365` or `36998,52365`)

=== "MySQL"

    ```yaml hl_lines="10 11 12 13"
    services:
        speedtest-tracker:
            image: lscr.io/linuxserver/speedtest-tracker:latest
            restart: unless-stopped
            container_name: speedtest-tracker
            ports:
                - 8080:80
                - 8443:443
            environment:
                - PUID= # (1)!
                - PGID= # (2)!
                - APP_KEY= # (3)!
                - APP_URL= # (4)!
                - DB_CONNECTION=mysql
                - DB_HOST=db
                - DB_PORT=3306
                - DB_DATABASE=speedtest_tracker
                - DB_USERNAME=speedtest_tracker
                - DB_PASSWORD=password
                - SPEEDTEST_SCHEDULE= # (5)!
                - SPEEDTEST_SERVERS= # (6)!
            volumes:
                - /path/to/data:/config
                - /path/to-custom-ssl-keys:/config/keys
            depends_on:
                - db
        db:
            image: mysql:8
            restart: always
            environment:
                - MYSQL_DATABASE=speedtest_tracker
                - MYSQL_USER=speedtest_tracker
                - MYSQL_PASSWORD=password
                - MYSQL_RANDOM_ROOT_PASSWORD=true
            volumes:
                - speedtest-db:/var/lib/mysql
            healthcheck:
                test: ["CMD", "mysqladmin", "ping", "-p${MYSQL_PASSWORD}"]
                interval: 5s
                retries: 5
                timeout: 5s
    volumes:
    speedtest-db:
    ```

    1. Your user ID - run `id -u` to find it
    2. Your group ID - run `id -g` to find it
    3. Generate with: `echo -n 'base64:'; openssl rand -base64 32`
    4. The URL where you'll access the app (e.g., `http://localhost:8080`)
    5. (Optional) Cron expression for when to run tests (e.g., `0 */2 * * *` for every 2 hours)
    6. (Optional) Comma separated server IDs to use (e.g., `52365` or `36998,52365`)

=== "Postgres"

    ```yaml hl_lines="10 11 12 13"
    services:
        speedtest-tracker:
            image: lscr.io/linuxserver/speedtest-tracker:latest
            restart: unless-stopped
            container_name: speedtest-tracker
            ports:
                - 8080:80
                - 8443:443
            environment:
                - PUID= # (1)!
                - PGID= # (2)!
                - APP_KEY= # (3)!
                - APP_URL= # (4)!
                - DB_CONNECTION=pgsql
                - DB_HOST=db
                - DB_PORT=5432
                - DB_DATABASE=speedtest_tracker
                - DB_USERNAME=speedtest_tracker
                - DB_PASSWORD=password
                - SPEEDTEST_SCHEDULE= # (5)!
                - SPEEDTEST_SERVERS= # (6)!
            volumes:
                - /path/to/data:/config
                - /path/to-custom-ssl-keys:/config/keys
            depends_on:
                - db
        db:
            image: postgres:18
            restart: always
            environment:
                - POSTGRES_DB=speedtest_tracker
                - POSTGRES_USER=speedtest_tracker
                - POSTGRES_PASSWORD=password
                - PGDATA=/var/lib/postgresql/data/
            volumes:
                - speedtest-db:/var/lib/postgresql/data
            healthcheck:
                test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER:-postgres}"]
                interval: 10s
                retries: 5
                timeout: 5s
    volumes:
    speedtest-db:
    ```

    1. Your user ID - run `id -u` to find it
    2. Your group ID - run `id -g` to find it
    3. Generate with: `echo -n 'base64:'; openssl rand -base64 32`
    4. The URL where you'll access the app (e.g., `http://localhost:8080`)
    5. (Optional) Cron expression for when to run tests (e.g., `0 */2 * * *` for every 2 hours)
    6. (Optional) Comma separated server IDs to use (e.g., `52365` or `36998,52365`)

??? tip "Want to use HTTPS?"

    Provide your own SSL keys, they must be named `cert.crt` (full chain) and `cert.key` (private key), and mounted in the container folder `/config/keys`.

??? tip "Scheduling automatic speedtests"
    Use [crontab.guru](https://crontab.guru/) to help create cron expressions for `SPEEDTEST_SCHEDULE`. See the [FAQ](../../help/speedtest-errors/#test-quality-issues) for tips on effectively scheduling tests.

??? tip "Running with unprivileged containers?"

    Most Docker setups can send ICMP requests (used for connectivity checks) without needing elevated privileges. However, if your Docker user doesn't run with elevated permissions or doesn't belong to the Docker group, the ping check during speedtests may fail.

    **Solution:**

    Add the `NET_RAW` capability to allow ICMP requests:

    ```yaml
    services:
      speedtest-tracker:
        # ... other configuration
        cap_add:
          - NET_RAW
    ```

    **Security Options:**

    If you have security options like `no-new-privileges:true` configured, these may also block ICMP requests. Remove any conflicting security options:

    ```yaml
    # Remove or comment out:
    # security_opt:
    #   - no-new-privileges:true
    ```

## Environment Variables

The examples above include the required environment variables. For additional configuration options like [Display](../configuration/environment-variables.md#display) and other settings, see the complete [Environment Variables](../configuration/environment-variables.md) reference.

## Start the Container

Save your Docker Compose configuration to a file named `docker-compose.yml`, then start the container:

```bash
docker compose up -d
```

The `-d` flag runs the containers in detached mode (in the background).

## First Login

When the container starts for the first time, a default username and password are created. Use the [default login](../security/authentication.md#default-user-account) credentials to login to the application. You can [change the default user](../security/authentication.md#change-account-details) after logging in.
