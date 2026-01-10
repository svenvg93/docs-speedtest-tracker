---
title: Dev Environment
description: Set up a local development environment for Speedtest Tracker using Laravel Sail.
icon: lucide/code
tags:
  - contributing
  - development
---

# Development Environment

Speedtest Tracker uses [Laravel Sail](https://laravel.com/docs/10.x/sail) for local development. Sail provides a containerized environment where the only requirements are Git and Docker.

!!! info

    This guide assumes basic knowledge of Laravel. See the [Laravel Docs](https://laravel.com/docs/10.x) and [Laracasts](https://laracasts.com/series/laravel-8-from-scratch) for more information.

## Setup

### 1. Clone and Configure

Clone the repository and set up environment variables:

```bash
# Clone repository
git clone git@github.com:YOUR-USERNAME/speedtest-tracker.git
cd speedtest-tracker

# Copy environment file
cp .env.example .env

# Generate application key
echo -n 'base64:'; openssl rand -base64 32
```

Update `.env` with your generated `APP_KEY`.

### 2. Install Dependencies

Install Composer dependencies using a temporary container:

```bash
docker run --rm \
    -u "$(id -u):$(id -g)" \
    -v "$(pwd):/var/www/html" \
    -w /var/www/html \
    laravelsail/php83-composer:latest \
    composer install --ignore-platform-reqs
```

### 3. Build and Start

Build the Sail container and start the environment:

```bash
# Build container
./vendor/bin/sail build --no-cache

# Start in background
./vendor/bin/sail up -d
```

!!! tip "Sail Alias"
    Create an alias for convenience: `alias sail='./vendor/bin/sail'`

### 4. Database and Assets

Set up the database and build frontend assets:

```bash
# Create SQLite database
touch database/database.sqlite

# Run migrations
./vendor/bin/sail artisan migrate:fresh --force

# Install and build frontend
./vendor/bin/sail npm install && ./vendor/bin/sail npm run build
```

## Development Workflows

### Reset Database

Reset your database to a clean state:

```bash
./vendor/bin/sail artisan migrate:fresh --force
```

### Process Queue Jobs

Speedtests and notifications run in the queue. Start a worker:

```bash
./vendor/bin/sail artisan queue:work
```

### Lint Code

All code must pass linting before submission:

```bash
./vendor/bin/pint
```

### Stop Environment

Stop the containers when done:

```bash
./vendor/bin/sail down
```

## Next Steps

Environment ready? See the [Contributing Guide](index.md) to learn how to submit your changes.
