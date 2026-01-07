---
title: Mail
description: Configure email notifications via SMTP for speedtest results.
icon: lucide/mail
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
Most SMTP providers work with Speedtest Tracker. Check your mail provider's documentation for SMTP settings. Common ports: `25`, `465` (SSL), `587` (TLS)

## Recipients

A recipient is any valid email address, you can add one or many recipients that will receive notifications based on the triggers selected.
