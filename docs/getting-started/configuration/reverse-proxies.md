---
title: Reverse Proxies
description: Example reverse proxy configurations for Nginx and Traefik
icon: lucide/waypoints
tags:
  - configuration
  - proxy
  - nginx
  - traefik
---

# Reverse Proxies

Speedtest Tracker can be served behind a reverse proxy to add features like SSL/TLS encryption, custom domains, and centralized routing for multiple services.

!!! warning "Community Configuration"
    This configuration is community-based and not officially supported by the Speedtest Tracker project. If you encounter any problems, please open a [discussion] to get community support. We welcome pull requests to improve this configuration.

## Common Configuration

All reverse proxy setups require these environment variables in your `speedtest-tracker` service:

```yaml hl_lines="2 3"
environment:
    - APP_URL=https://speedtest.yourdomain.com # (1)!
    - ASSET_URL=https://speedtest.yourdomain.com # (2)!
```

1. Replace with your actual domain where you'll access Speedtest Tracker
2. Replace with your actual domain (same as APP_URL)


## Nginx

```nginx hl_lines="4 12 15 16 30"
# Redirect HTTP to HTTPS
server {
    listen 80;
    server_name speedtest.yourdomain.com; # (1)!

    return 301 https://$host$request_uri;
}

# HTTPS server
server {
    listen 443 ssl http2;
    server_name speedtest.yourdomain.com; # (2)!

    # SSL certificate (Let's Encrypt)
    ssl_certificate /etc/letsencrypt/live/speedtest.yourdomain.com/fullchain.pem; # (3)!
    ssl_certificate_key /etc/letsencrypt/live/speedtest.yourdomain.com/privkey.pem; # (4)!

    # SSL security
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers 'ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384';
    ssl_prefer_server_ciphers on;
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 10m;
    ssl_stapling on;
    ssl_stapling_verify on;

    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;

    location / {
        proxy_pass http://speedtest-tracker:80; # (5)!

        # Forward headers
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_redirect off;
    }
}
```

1. Replace with your actual domain
2. Replace with your actual domain (same as line 4)
3. Path to your SSL certificate full chain
4. Path to your SSL certificate private key
5. Replace `speedtest-tracker:80` with your container name or IP:port (e.g., `192.168.1.100:8080` if different)

## Traefik

Add these labels to your `speedtest-tracker` docker compose.

```yaml hl_lines="2 3 4 6 7"
labels:
    - "traefik.enable=true"
    - "traefik.http.routers.speedtest-tracker.rule=Host(`speedtest.yourdomain.com`)" # (1)!
    - "traefik.http.routers.speedtest-tracker.entrypoints=websecure" # (2)!
    - "traefik.http.routers.speedtest-tracker.tls=true"
    - "traefik.http.routers.speedtest-tracker.tls.certresolver=yourresolver" # (3)!
    - "traefik.http.services.speedtest-tracker.loadbalancer.server.port=80" # (4)!
```

1. Replace with your actual domain - this is the domain Traefik will respond to
2. Use the `websecure` entrypoint (HTTPS) defined in your Traefik configuration
3. Replace `yourresolver` with your Traefik certificate resolver name (e.g., `letsencrypt`)
4. Tell Traefik to connect to container port 80

  [discussion]: https://github.com/alexjustesen/speedtest-tracker/discussions