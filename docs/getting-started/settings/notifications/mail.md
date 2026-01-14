---
title: Mail
description: Configure email notifications via SMTP for speedtest results.
icon: lucide/mail
tags:
  - settings
  - notifications
  - email
  - smtp
---

# Mail

Notifications sent to the mail channel will be emailed to the list of recipients.

## Setting Up SMTP

Speedtest Tracker uses SMTP mail protocol to send email messages, you can use any service that allows you to send emails via SMTP.

To configure the mail server settings you'll need to update the following variables in your `.env` file or add them to the environment variables passed into the container. When choosing mail scheme both `ssl` and `tls` protocols are supported and you'll want to check with your mail provider for which to use and which port.

!!! warning

    Make sure these are not set in both your `.env` file or your `docker-compose.yml` file as that can cause issues.

```
MAIL_MAILER=smtp
MAIL_HOST=
MAIL_PORT=
MAIL_USERNAME=
MAIL_PASSWORD=
MAIL_FROM_ADDRESS=
MAIL_FROM_NAME=
```

!!! info

    `MAIL_SCHEME` is optional, only use it if you need to define `smtp` or `smtps` otherwise Laravel will determine the scheme based on the port provided.

## Providers
Most SMTP providers work with Speedtest Tracker. Check your mail provider's documentation for SMTP settings. Below are some common examples:

??? example "Gmail"

    To generate an app-specific password:

    1. Go to https://myaccount.google.com/
    2. Go to **Security and sign-in**, click on "2-Step Verification"
    3. Click on **App passwords** at the bottom of the page
    4. Give it a name (e.g., "Speedtest Tracker") and copy the generated password

    Use this password for the `MAIL_PASSWORD` environment variable in the configuration below.

    ```bash title="environment variables" hl_lines="4 5 6"
    MAIL_MAILER=smtp
    MAIL_HOST=smtp.gmail.com
    MAIL_PORT=465
    MAIL_USERNAME=username@gmail.com
    MAIL_PASSWORD=your-app-specific-password
    MAIL_FROM_ADDRESS=username@gmail.com
    MAIL_FROM_NAME="Speedtest Tracker"
    ```

??? example "iCloud"

    To generate an app-specific password:

    1. Go to https://appleid.apple.com
    2. Sign in and go to Security section
    3. Under "App-Specific Passwords", click "Generate password"
    4. Give it a name (e.g., "Speedtest Tracker") and copy the generated password

    Use this password for the `MAIL_PASSWORD` environment variable in the configuration below.

    ```bash title="environment variables" hl_lines="4 5 6"
    MAIL_MAILER=smtp
    MAIL_HOST=smtp.mail.me.com
    MAIL_PORT=587
    MAIL_USERNAME=username@icloud.com
    MAIL_PASSWORD=your-app-specific-password
    MAIL_FROM_ADDRESS=username@icloud.com
    MAIL_FROM_NAME="Speedtest Tracker"
    ```

    ??? info "Using Email Aliases"
        If you use an email alias for sending the notifications, `MAIL_USERNAME` needs to be your main iCloud email address, and `MAIL_FROM_ADDRESS` needs to be your alias email address.


## Recipients

A recipient is any valid email address, you can add one or many recipients that will receive notifications based on the triggers selected.
