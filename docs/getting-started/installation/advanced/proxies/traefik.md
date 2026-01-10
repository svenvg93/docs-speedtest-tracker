---
title: Traefik
description: Configure Traefik as a reverse proxy for Speedtest Tracker with automatic SSL.
icon: lucide/network
tags:
  - proxy
  - traefik
  - ssl
---

# Traefik

[Traefik](https://traefik.io) can be used as a Reverse Proxy in front of Speedtest Tracker when you want to expose the Dashboard publicly with a trusted certificate.

!!! warning "Community Configuration"
    This configuration is community-based and not officially supported by the Speedtest Tracker project. If you encounter any problems, please open a [discussion](https://github.com/alexjustesen/speedtest-tracker/discussions) to get community support. We welcome pull requests to improve this configuration.

## Update Your Docker Compose

Add the following to your existing `speedtest-tracker` service in your `docker-compose.yml`:

```yaml hl_lines="4 5 7 8 9 10 11 12"
services:
    speedtest-tracker:
        environment:
            # Add these environment variables to your existing environment section
            - APP_URL=https://speedtest.yourdomain.com # Change to your domain
            - ASSET_URL=https://speedtest.yourdomain.com # Change to your domain
        # Add these labels to enable Traefik routing
        labels:
            - "traefik.enable=true"
            - "traefik.http.routers.speedtest-tracker.rule=Host(`speedtest.yourdomain.com`)"
            - "traefik.http.routers.speedtest-tracker.entrypoints=websecure"
            - "traefik.http.routers.speedtest-tracker.tls=true"
            - "traefik.http.routers.speedtest-tracker.tls.certresolver=yourresolver"
            - "traefik.http.services.speedtest-tracker.loadbalancer.server.port=80"
```

!!! warning "Important"
    - Replace `speedtest.yourdomain.com` with your actual domain
    - Update `yourresolver` to match your Traefik certificate resolver name
    - Ensure Speedtest Tracker and Traefik are on the same Docker network

## Configuration Reference

| Added compose part | Description |
| ------------------ | ----------- |
| `APP_URL` | URL you want to access the WebGui on. |
| `ASSET_URL` | URL used for loading all the needed assets. Need to be the same as the `APP_URL`. |
| `traefik.enable=true` | Explicitly tell Traefik to expose this container |
| `traefik.http.routers.speedtest-tracker.rule=Host(\`speedtest.yourdomain.com\`)` | The domain the service will respond to |
| `traefik.http.routers.speedtest-tracker.entrypoints=websecure` | Allow request only from the predefined entry point |
| `traefik.http.routers.speedtest-tracker.tls=true` | When a TLS section is specified, it instructs Traefik that the current router is dedicated to HTTPS requests only |
| `traefik.http.routers.speedtest-tracker.tls.certresolver=yourresolver` | Explicitly tell Traefik which Certificate provider to use matching your Traefik configuration |
| `traefik.http.services.speedtest-tracker.loadbalancer.server.port=80` | Explicitly tell Traefik port to use to connect to the container |
