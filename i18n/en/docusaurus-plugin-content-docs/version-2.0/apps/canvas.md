---
title: Canvas
slug: /canvas
tags:
  - Canvas
  - LMS
  - Online Learning
---

import Meta from './_include/canvas.md';

<Meta name="meta" />

## Getting Started {#guide}

### Initialize {#wizard}

After installing Canvas in the Websoft9 console, open **My Apps** > **Canvas** and get the URL and account information from the **Access** tab. Sign in to the Canvas admin console with the provided account. The administrator email, password, and account name are initialized on first startup using `CANVAS_LMS_ADMIN_EMAIL`, `CANVAS_LMS_ADMIN_PASSWORD`, and `CANVAS_LMS_ACCOUNT_NAME`.

### Manage courses {#courses}

After signing in, use the admin console to access account and course features and configure the account and courses for your organization. Canvas data and configuration are stored in persistent volumes and configuration files. For details about teaching workflows, see the [Canvas production documentation](https://github.com/instructure/canvas-lms/wiki/Production-Start).

### Configure email {#email}

Canvas mail server settings are in `outgoing_mail.yml`. To enable email notifications, configure SMTP for your mail provider and make sure the domain and links in email messages are reachable by users.

## Best Practices

### Configure the initial administrator {#first-admin}

After first startup, sign in with the initialized administrator account and review account settings. The administrator environment variables above take effect only on first startup; changing them does not automatically replace an initialized account.

### Persist application data {#data}

Canvas uses PostgreSQL and Redis and stores database, cache, bundle, temporary, and uploaded asset data in persistent volumes. Back up the relevant data volumes and custom configuration files before upgrading.

## Configuration {#configs}

| Setting | Description | Default / location |
|---------|-------------|--------------------|
| Administrator email | Initial administrator account email | `CANVAS_LMS_ADMIN_EMAIL` |
| Administrator password | Initial administrator password | `CANVAS_LMS_ADMIN_PASSWORD` |
| Account name | Initial Canvas account name | `CANVAS_LMS_ACCOUNT_NAME` |
| SMTP | Outgoing email settings | `./src/outgoing_mail.yml` |
| Persistent data | PostgreSQL, Redis, bundle, temporary files, and assets | App volumes |

Administrator initialization variables are read only on first startup. Recreate the app as required after changing environment variables or configuration.

## Administration {#administrator}

### Upgrade

Canvas upgrades may involve application and data migrations. Before upgrading, back up the app data volumes and configuration from the Websoft9 console, then follow the [Canvas upgrade instructions](https://github.com/instructure/canvas-lms/wiki/Upgrading).

### Backup and restore

Use the Websoft9 console to back up and restore Canvas persistent data volumes, including PostgreSQL, Redis, uploaded assets, and application files. To restore configuration, restore the corresponding files such as `database.yml`, `domain.yml`, `redis.yml`, and `outgoing_mail.yml`.

## Troubleshooting {#troubleshooting}

#### The app does not start

Check the Canvas Compose logs and app health status. Initial setup or an upgrade may take time to complete.

#### The administrator password is forgotten or initial settings did not change

`CANVAS_LMS_ADMIN_EMAIL`, `CANVAS_LMS_ADMIN_PASSWORD`, and `CANVAS_LMS_ACCOUNT_NAME` apply only on first startup. Changing them later does not automatically reset existing data or accounts.

#### Email notifications do not work

Check the SMTP settings in `outgoing_mail.yml`, network connectivity, and domain configuration. Make sure links in notifications open through the URL users access.

## References {#references}

- [Canvas production documentation](https://github.com/instructure/canvas-lms/wiki/Production-Start)
- [Canvas upgrade instructions](https://github.com/instructure/canvas-lms/wiki/Upgrading)
- [Canvas project](https://github.com/instructure/canvas-lms)
