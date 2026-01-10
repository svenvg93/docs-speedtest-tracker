---
title: Authorization
description: User roles and permissions in Speedtest Tracker.
icon: lucide/shield-check
tags:
  - security
  - authorization
  - permissions
---

# Authorization

## Results

| Permission | User | Admin |
| ---------- | ---- | ----- |
| View any (list) | Yes | Yes |
| View (show) | Yes | Yes |
| Create | No | No |
| Update | Yes | Yes |
| Delete any (bulk) | No | Yes |
| Delete | No | Yes |

### Notes

1. Creating results are done through a scheduled Speedtest or triggered manually.
2. Updating a result only applies to editing the record's comments.

## Users

| Permission | User | Admin |
| ---------- | ---- | ----- |
| View any (list) | No | Yes |
| View (show) | No | Yes |
| Create | No | Yes |
| Update | No | Yes |
| Delete any (bulk) | No | Yes |
| Delete | No | Yes |

### Notes

If you need to change the role an existing user you can now use the available [commands](../../other/commands.md).

## Other Permissions

| Permission | User | Admin |
| ---------- | ---- | ----- |
| Manage API tokens | No | Yes |
| Trigger a manual Speedtest | Yes | Yes |

## Settings

| Permission | User | Admin |
| ---------- | ---- | ----- |
| Data integrations | No | Yes |
| Notifications | No | Yes |
| Thresholds | No | Yes |
