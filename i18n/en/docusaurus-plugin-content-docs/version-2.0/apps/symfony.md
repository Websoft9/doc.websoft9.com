---
title: Symfony
slug: /symfony
tags:
  - Symfony
  - PHP
  - Developer Tools
---

import Meta from './_include/symfony.md';

<Meta name="meta" />

## Getting Started {#guide}

### Initialize {#wizard}

After installing Symfony in the Websoft9 console, open **My Apps** > **Symfony** and use the app's access URL to confirm that the Symfony starter page loads.

### Deploy your project {#project}

The app starts with a Symfony starter project. When your own application code is ready, deploy it to `/var/www/html`, the app's data directory, replacing the starter project. Recreate the app as needed after changing code or container configuration.

### Connect a database {#database}

The default deployment does not bundle a database, and the Symfony skeleton does not require one by default. If your application needs a database, install Doctrine ORM or DBAL in the project and set `DATABASE_URL` in the app's `.env` to connect to an available external database.

## Best Practices

### Manage the database separately {#external-database}

Deploy the database as a separate service and configure a dedicated database and user for the app. After updating `DATABASE_URL`, recreate the app and check its logs to confirm the connection. Back up the Symfony project data and database separately.

## Configuration {#configs}

| Setting | Description | Default / location |
|---------|-------------|--------------------|
| Web Console | Symfony web access port | 8080 |
| `/var/www/html` | Symfony application code directory | `symfony_app` persistent volume |
| `DATABASE_URL` | Doctrine ORM/DBAL database connection string | Set in the app's `.env` when needed |
| PHP runtime | Server Side Up PHP FrankenPHP image | PHP 8.5 |
| Symfony version | Currently supported version | 8.1.11; `latest` is also available |

For production, pin a specific Symfony version instead of relying on the potentially changing `latest` tag.

## Administration {#administrator}

### Upgrade

Upgrade the app from the Websoft9 console. Back up the project data in `/var/www/html` and the external database first. Choose a Symfony version compatible with your project dependencies.

### Backup and restore

Back up the `symfony_app` persistent volume and the separate database. To restore, put the application data back in `/var/www/html`, restore the database, and verify `DATABASE_URL` in `.env`.

## Troubleshooting {#troubleshooting}

#### The starter page does not load or the app fails to start

Check the app's Compose logs to confirm the service started successfully. Also verify that the firewall or cloud security group allows the access port.

#### The app cannot connect to the database

Confirm that the project includes Doctrine ORM/DBAL, the host, port, database name, and credentials in `DATABASE_URL` are correct, and the database is reachable from the app container.

## References {#references}

- [Symfony setup documentation](https://symfony.com/doc/current/setup.html)
- [Symfony Docker documentation](https://symfony.com/doc/current/setup/docker.html)
- [FrankenPHP image documentation](https://serversideup.net/open-source/docker-php/docs/image-variations/frankenphp)
