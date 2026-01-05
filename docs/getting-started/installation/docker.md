---
title: Docker Run
description: These instructions will run you through setting up Speedtest Tracker on a Docker server using Docker run.
icon: lucide/container
---

# Docker

Setting up your environment with Docker Compose is the recommended way as it'll setup the application and a database for you. These steps will run you through setting up the application using Docker and Docker Compose.

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

!!! warning "Required: User ID Configuration"

    You will need to get your user's `PUID` and `PGID`, you can do this by running `id $user` on the host.

    [Learn more about PUID and PGID](https://docs.linuxserver.io/general/understanding-puid-and-pgid/)

=== "SQLite"

    ```bash hl_lines="4 5 6 7"
    docker run -d --name speedtest-tracker --restart unless-stopped \
        -p 8080:80 \
        -p 8443:443 \
        -e PUID= \ # (1)!
        -e PGID= \ # (2)!
        -e APP_KEY= \ # (3)!
        -e APP_URL= \ # (4)!
        -e DB_CONNECTION=sqlite \
        -v /path/to/data:/config \
        -v /path/to-custom-ssl-keys:/config/keys \
        lscr.io/linuxserver/speedtest-tracker:latest
    ```

    1. Your user ID - run `id -u` to find it
    2. Your group ID - run `id -g` to find it
    3. Generate with: `echo -n 'base64:'; openssl rand -base64 32`
    4. The URL where you'll access the app (e.g., `http://localhost:8080`)

=== "MariaDB"

    ```bash hl_lines="4 5 6 7 9 12 13"
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
        -v /path/to/data:/config \
        -v /path/to-custom-ssl-keys:/config/keys \
        lscr.io/linuxserver/speedtest-tracker:latest
    ```

    1. Your user ID - run `id -u` to find it
    2. Your group ID - run `id -g` to find it
    3. Generate with: `echo -n 'base64:'; openssl rand -base64 32`
    4. The URL where you'll access the app (e.g., `http://localhost:8080`)
    5. Your MariaDB server hostname or IP address
    6. Your database username
    7. Your database password

=== "MySQL"

    ```bash hl_lines="4 5 6 7 9 12 13"
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
        -v /path/to/data:/config \
        -v /path/to-custom-ssl-keys:/config/keys \
        lscr.io/linuxserver/speedtest-tracker:latest
    ```

    1. Your user ID - run `id -u` to find it
    2. Your group ID - run `id -g` to find it
    3. Generate with: `echo -n 'base64:'; openssl rand -base64 32`
    4. The URL where you'll access the app (e.g., `http://localhost:8080`)
    5. Your MySQL server hostname or IP address
    6. Your database username
    7. Your database password

=== "Postgres"

    ```bash hl_lines="4 5 6 7 9 12 13"
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
        -v /path/to/data:/config \
        -v /path/to-custom-ssl-keys:/config/keys \
        lscr.io/linuxserver/speedtest-tracker:latest
    ```

    1. Your user ID - run `id -u` to find it
    2. Your group ID - run `id -g` to find it
    3. Generate with: `echo -n 'base64:'; openssl rand -base64 32`
    4. The URL where you'll access the app (e.g., `http://localhost:8080`)
    5. Your Postgres server hostname or IP address
    6. Your database username
    7. Your database password

!!! info

    If you would like to provide your own SSL keys, they must be named `cert.crt` (full chain) and `cert.key` (private key), and mounted in the container folder `/config/keys`.

## Environment Variables

In order for the application to run smoothly, some environment variables need to be set. Check out the [Environment Variables](../configuration/environment-variables.md) section. Make sure all **required** variables are configured.

## Configuration Variables (Optional)

You can set configuration variables to have automatic speedtest on an schedule. Check out the [Environment Variables](../configuration/environment-variables.md#speedtest) section on how to set the variables. Also see the [FAQ](../../help/faqs.md#speedtest) for tips effectively scheduling tests.

!!! info

    Complete overview of the Environment Variables for custom configuration can be found [here](../configuration/environment-variables.md).

## Start the Container

You can now start the container accordingly the platform you are on.

## First Login

During the start the container there is a default username and password created. Use the [default login](../security/authentication.md#default-user-account) credentials to login to the application. You can [change the default user](../security/authentication.md#change-account-details) after logging in.
