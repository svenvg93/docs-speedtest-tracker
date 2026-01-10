---
title: Cloudflare Tunnel
description: Configure Cloudflare Tunnel (Zero Trust) as a reverse proxy without exposing your IP address.
icon: lucide/cloud
tags:
  - proxy
  - cloudflare
  - security
---

# Cloudflare Tunnel (Zero Trust)

A [Cloudflare tunnel](https://www.cloudflare.com/nl-nl/products/tunnel/) can be used as a reverse proxy in front of Speedtest Tracker when you want to expose the application publicly without exposing your IP address.

!!! warning "Community Configuration"
    This configuration is community-based and not officially supported by the Speedtest Tracker project. If you encounter any problems, please open a [discussion](https://github.com/alexjustesen/speedtest-tracker/discussions) to get community support. We welcome pull requests to improve this configuration.

## Step 1: Update Your Docker Compose

Add the following environment variables to your existing `speedtest-tracker` service in your `docker-compose.yml`:

```yaml hl_lines="3 4"
services:
    speedtest-tracker:
        environment:
            # Add these environment variables to your existing environment section
            - APP_URL=https://speedtest.yourdomain.com # Change to your domain
            - ASSET_URL=https://speedtest.yourdomain.com # Change to your domain
```

!!! warning "Important"
    Ensure Speedtest Tracker and your Cloudflare Tunnel are on the same Docker network if using container names.

## Step 2: Configure Cloudflare Tunnel

Set up the tunnel in the Cloudflare Zero Trust dashboard:

1. Go to **Zero Trust** → **Networks** → **Tunnels**
2. Select your tunnel or create a new one, then click **Edit**
3. Navigate to **Public Hostname**
4. Click **Add a public hostname**
5. Configure the following:
   - **Subdomain:** Your desired subdomain (e.g., `speedtest`)
   - **Domain:** Your domain name
   - **Type:** `http` or `https`
     - If using HTTPS, disable TLS verification under `Additional application settings → TLS → No TLS Verify`
   - **URL:** Connection to Speedtest Tracker
     - Use `speedtest-tracker:80` (container name) or `<IP-ADDRESS>:8080`

## Configuration Reference

| Added compose part | Description |
| ------------------ | ----------- |
| `APP_URL` | URL you want to access the WebGui on. |
| `ASSET_URL` | URL used for loading all the needed assets. Need to be the same as the `APP_URL`. |
