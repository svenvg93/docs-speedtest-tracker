---
title: Authentication
description: Manage user accounts and authentication in Speedtest Tracker.
icon: lucide/user
---

# Authentication

Speedtest Tracker uses Filament for the admin panel. During the install process an admin account is created for you.

## Default User Account

During the first start of the application a default admin account is created for you:

| Username            | Password   |
| ------------------- | ---------- |
| `admin@example.com` | `password` |

## Change Account Details

### Login Details

You can update the login details of your account through the profile page. Every user can update these details for their own account.

1. In the top right corner click on the user logo next to the bell icon.
2. Click on Profile
3. Change the `Name`, `E-Mail Address` and `Password` to your liking.

### Update Other User Accounts

As an Admin you can change the account details of other accounts.

1. On the right side menu click on `Users`
2. Click on user account you want to change
3. Change the `Name`, `E-Mail Address` ,`Password` and `Role` to your liking.

## Create User Account

You can create additional user accounts.

1. On the right side menu click on `Users`
2. Click on `New User`
3. Fill in the `Name`, `E-Mail Address, Password` and `Password confirmation` to your liking.
4. Choose the needed role for the user under `Role`.

!!! info

    The difference between the Roles can be found in the [Authorization](authorization.md) section.
