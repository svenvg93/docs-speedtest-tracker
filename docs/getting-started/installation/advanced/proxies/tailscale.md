---
title: Tailscale
description: Access Speedtest Tracker securely within your Tailnet using Tailscale Mesh VPN.
icon: lucide/shield
tags:
  - vpn
  - tailscale
  - security
---

# Tailscale

[Tailscale](https://tailscale.com) Mesh VPN service can be used as a sidecar container to access Speedtest Tracker within your Tailnet using its own MagicDNS name.

!!! warning "Community Configuration"
    This configuration is community-based and not officially supported by the Speedtest Tracker project. If you encounter any problems, please open a [discussion](https://github.com/alexjustesen/speedtest-tracker/discussions) to get community support. We welcome pull requests to improve this configuration.

## Step 1: Generate Tailscale Auth Key

Create an authentication key for the Docker container:

1. Open the [**Keys**](https://login.tailscale.com/admin/settings/keys) page in the Tailscale admin console
2. Click **Generate auth key**
3. Configure key settings:
   - Set description (e.g., "Speedtest Tracker")
   - Choose if reusable
   - Set expiration
   - Configure device settings
4. Click **Generate key**
5. **Save this key** - you'll need it in the next step

## Step 2: Add Tailscale Sidecar to Your Docker Compose

Add the Tailscale sidecar service and update your existing Speedtest Tracker configuration:

```yaml hl_lines="2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 20 21 22"
services:
  # Add this new Tailscale sidecar service
  tailscale-speedtest:
    image: tailscale/tailscale
    container_name: tailscale_speedtest-tracker
    hostname: speedtest # This will be your MagicDNS hostname
    environment:
      - TS_AUTHKEY=<YOUR_AUTH_KEY> # Paste your auth key here
      - TS_STATE_DIR=/var/lib/tailscale
      - TS_USERSPACE=false
    volumes:
      - ./tailscale-speedtest/state:/var/lib/tailscale
      - /dev/net/tun:/dev/net/tun
    cap_add:
      - net_admin
      - sys_module
    restart: unless-stopped

  # Update your existing speedtest-tracker service
  speedtest-tracker:
    depends_on:
      - tailscale-speedtest
    network_mode: service:tailscale-speedtest # Share network with Tailscale
    environment:
      # Add these to your existing environment section
      - APP_URL=https://speedtest.yourtailnet.ts.net # Change to your MagicDNS name
      - ASSET_URL=https://speedtest.yourtailnet.ts.net # Change to your MagicDNS name
```

!!! warning "Important Configuration Changes"
    - Replace `<YOUR_AUTH_KEY>` with the key from Step 1
    - Update the MagicDNS URLs to match your Tailnet name
    - The `network_mode` setting makes Speedtest Tracker share the Tailscale container's network
    - Remove any `ports:` mapping from your speedtest-tracker service (not needed with Tailscale)

## Configuration Reference

| Added compose part | Description |
| ------------------ | ----------- |
| `APP_URL` | URL you want to access the WebGui on. This will need to be the Tailscale Magic DNS name |
| `ASSET_URL` | URL used for loading all the needed assets. Need to be the same as the `APP_URL`. |
| `TS_AUTHKEY` | Auth key for Tailscale |
