---
title: Apprise
description: Use Apprise to send notifications to multiple services like Discord, Pushover, and Ntfy.
icon: lucide/bell-ring
tags:
  - settings
  - notifications
  - apprise
  - integrations
---

# Apprise

Apprise provides a unified notification channel that lets you send alerts to numerous services—like Discord, Pushover, and Ntfy as well as many additional platforms.

!!! question "Why Apprise?"

    Apprise allows the application to send notifications to a wide variety of services. It lets us focus on features instead of maintaining X number of notification channels. Essentially, this helps us cut down on maintenance and feature requests.

## Apprise Sidecar Container

To use Apprise, you'll need to set up your own Apprise instance. This instance isn't created automatically, so make sure to include it in your deployment. See the Apprise [Github Repo](https://github.com/caronc/apprise-api) for the setup instructions. 

!!! info "Support"

    We don't offer support on setting up Apprise. In case of any problems with the Apprise container, please reach out to the Apprise team.

## Settings

### Apprise Server URL 

On the notifications page under the Apprise tab, you'll need to configure the connection to your Apprise instance:

- **Apprise Server URL**: This is the URL where the Apprise server can be reached. The URL must end with `/notify` (e.g., `http://apprise:8000/notify`)

### Notification Channels

Notification channels are the specially formatted URLs (`discord://WebhookID/Token`, `slack://TokenA/TokenB/TokenC`) used by Apprise to send notifications to various services. These URLs tell Apprise which service and which format needs to be used.

Refer to the [Apprise documentation](https://appriseit.com/services/) for a full list of supported channels and their required formats. You can add as many different channels as you wish. The notifications will be sent to all of them.

## Tips and Tricks

### Format

By default, the format used for messages is `markdown`. This allows us to do some formatting on the message like bold text.

### Preview Images

By default, Apprise does not allow preview images for URLs. This is a default setting on the Apprise instance. Depending on the service used, you can override this setting in the notification channel URL. Check the Apprise documentation to see if your service supports this and how to configure it.
