---
title: Commands
description: Commands offer additional functionality like providing debug information and performing maintenance tasks.
icon: lucide/terminal
tags:
  - reference
  - commands
  - cli
---

# Commands

Commands are intended to be run from within the CLI of the container and from the application's root directory. The application directory is located at: `/app/www`. When using the commands below they should be prefixed with `php artisan`.

??? example
    From within the container:    
    ```
    /app/www php artisan about
    ```

    From the host system running the container:
    ```
    docker exec speedtest-tracker /app/www php artisan about
    ```

## Core commands

Core commands exist at the framework level and might be extended to provide additional functionality.

| Command | Description |
| ------- | ----------- |
| `about` | Provides information on the current version of Speedtest Tracker, Laravel and Filament. |

## Application commands

Application commands are built to extend Speedtest Tracker's functionality from the CLI.

| Command | Description |
| ------- | ----------- |
| `app:ookla-list-servers` | Get a list of local Ookla speedtest servers. |
| `app:user-change-role` | Change the role for a user. |
| `app:user-reset-password` | Change the password for a user. |

## Maintenance commands

Maintenance commands help fix issues that might crop up over time.

| Command | Description |
| ------- | ----------- |
| `app:result-fix-statuses` | Reviews the data payload of each result and corrects the status attribute. |
