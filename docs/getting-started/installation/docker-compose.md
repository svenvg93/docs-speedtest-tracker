---
title: Docker Compose
description: These instructions will run you through setting up Speedtest Tracker on a Docker server using Docker Compose.
icon: lucide/package
---

# Docker Compose

Setting up your environment with Docker Compose is the recommended way as it'll setup the application and a database for you. These steps will run you through setting up the application using Docker and Docker Compose.

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

!!! warning "Required: User ID Configuration"

    You will need to get your user's `PUID` and `PGID`, you can do this by running `id $user` on the host.

    [Learn more about PUID and PGID](https://docs.linuxserver.io/general/understanding-puid-and-pgid/)


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
            volumes:
                - /path/to/data:/config
                - /path/to-custom-ssl-keys:/config/keys
    ```

    1. Your user ID - run `id -u` to find it
    2. Your group ID - run `id -g` to find it
    3. Generate with: `echo -n 'base64:'; openssl rand -base64 32`
    4. The URL where you'll access the app (e.g., `http://localhost:8080`)

=== "MariaDB"

    ```yaml hl_lines="10 11 12 13 19"
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
                - DB_PASSWORD=password # (5)!
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
    5. Change this to a secure password of your choice

=== "MySQL"

    ```yaml hl_lines="10 11 12 13 19"
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
                - DB_PASSWORD=password # (5)!
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
    5. Change this to a secure password of your choice

=== "Postgres"

    ```yaml hl_lines="10 11 12 13 19"
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
                - DB_PASSWORD=password # (5)!
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
    5. Change this to a secure password of your choice

!!! info

    If you would like to provide your own SSL keys, they must be named `cert.crt` (full chain) and `cert.key` (private key), and mounted in the container folder `/config/keys`.

## Environment Variables

In order for the application to run smoothly, some environment variables need to be set. Check out the [Environment Variables](../configuration/environment-variables.md) section. Make sure all **required** variables are configured.

## Configuration Variables (Optional)

You can set configuration variables to have automatic speedtest on an schedule. Check out the [Environment Variables](../configuration/environment-variables.md#speedtest) section on how to set the variables. Also see the [FAQ](../../help/faqs.md#speedtest) for tips effectively scheduling tests.

## Start the Container

You can now start the container accordingly the platform you are on.

## First Login

During the start the container there is a default username and password created. Use the [default login](../security/authentication.md#default-user-account) credentials to login to the application. You can [change the default user](../security/authentication.md#change-account-details) after logging in.
