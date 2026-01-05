---
title: Nginx
description: Configure Nginx as a reverse proxy for Speedtest Tracker with SSL support.
icon: lucide/network
---

# Nginx

[Nginx](https://nginx.org) can be used as a Reverse Proxy in front of Speedtest Tracker to expose the Dashboard publicly with a trusted certificate.

## Step 1: Update Your Docker Compose

Add the following environment variables to your existing `speedtest-tracker` service in your `docker-compose.yml`:

```yaml hl_lines="3 4"
services:
    speedtest-tracker:
        environment:
            # Add these two lines to your existing environment section
            - APP_URL=https://speedtest.yourdomain.com # Change to your domain
            - ASSET_URL=https://speedtest.yourdomain.com # Change to your domain
```

!!! tip "Complete Example"
    Your complete environment section should include all your existing variables plus the two new ones above.

## Step 2: Configure Nginx

Create an Nginx configuration file to proxy requests to Speedtest Tracker:

!!! info "Before You Start"
    - Replace `speedtest.yourdomain.com` with your actual domain
    - Update SSL certificate paths to match your setup
    - Adjust `proxy_pass` to match your Docker network configuration (hostname or IP:port)

```nginx
server {
        listen 80;
        server_name speedtest.yourdomain.com;
        return 301 https://$host$request_uri;
}

server {
        listen 443 ssl;
        server_name speedtest.yourdomain.com;

        ssl_certificate /etc/letsencrypt/live/speedtest.yourdomain.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/speedtest.yourdomain.com/privkey.pem;

        ssl_protocols TLSv1.2;
        ssl_ciphers
'ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:AES:CAMELLIA:DES-CBC3-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!aECDH:!EDH-DSS-DES-CBC3-SHA:!EDH-RSA-DES-CBC3-SHA:!KRB5-DES-CBC3-SHA';
        ssl_prefer_server_ciphers on;
        ssl_session_cache shared:SSL:10m;
        ssl_session_timeout 10m;
        ssl_dhparam /etc/ssl/certs/dhparam.pem;

        add_header Strict-Transport-Security "max-age=31536000;includeSubdomains";

        location / {
                proxy_set_header X-Forwarded-Host $host;
                proxy_set_header X-Forwarded-Server $host;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;

                proxy_pass http://speedtest-container-host:80;
        }
}
```
