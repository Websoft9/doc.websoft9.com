---
title: LobeHub
slug: /lobehub
tags:
  - LobeHub
  - AI
  - LLM
---

import Meta from './_include/lobehub.md';

<Meta name="meta" />

## Getting Started {#guide}

### Initialize {#wizard}

After installing LobeHub in the Websoft9 console, open **My Apps** > **LobeHub** and get the app URL and credentials from the **Access** tab. Sign in to the LobeHub admin console.

### Use LobeHub {#usage}

After signing in, use the available features in the LobeHub console. For details about model setup, conversations, and other features, see the [LobeHub self-hosting documentation](https://lobehub.com/docs/self-hosting/platform/docker-compose).

### Change the password {#password}

Open the app's **Compose** tab in the Websoft9 console, update the password in `.env`, save, and rebuild the app.

## Best Practices

### Configure a domain and HTTPS {#https}

The online community feature requires access through a configured domain over HTTPS. Configure the app domain and enable HTTPS, then reload the page.

### Back up application data {#data}

LobeHub uses PostgreSQL, Redis, and RustFS to store data in their respective persistent volumes. Back up these volumes before upgrading or recreating the app. Mount `bucket.config.json` as a single file when overriding it.

## Configuration {#configs}

| Setting | Description | Default / location |
|---------|-------------|--------------------|
| Web Console | LobeHub web access port | 3210 |
| PostgreSQL | Relational data persistence directory | `/var/lib/postgresql/data` |
| Redis | Cache persistence directory | `/data` |
| RustFS | Object storage persistence directory | `/data` |
| Bucket configuration | Object storage configuration file | `./src/bucket.config.json` |

See the app's `.env` on the **Compose** tab for supported environment variables. Rebuild the app after changing configuration.

## Administration {#administrator}

### Upgrade

Upgrade LobeHub from the Websoft9 console. Pin a specific app version for production. Back up the PostgreSQL, Redis, and RustFS data volumes before upgrading.

### Backup and restore

Back up and restore the PostgreSQL, Redis, and RustFS persistent data volumes separately. If you use a custom bucket configuration, also back up `bucket.config.json`.

## Troubleshooting {#troubleshooting}

#### The app does not start

Check the app's Compose logs and confirm that LobeHub and its dependent services started successfully.

#### The online community does not load

This feature requires a configured domain with HTTPS. Check the app's domain and HTTPS settings, then reload.

#### The app page is not reachable

Check the access URL and confirm that port 3210 is allowed by the server firewall or cloud security group.

## References {#references}

- [LobeHub self-hosting documentation](https://lobehub.com/docs/self-hosting/platform/docker-compose)
- [LobeHub project](https://github.com/lobehub/lobehub)
- [LobeHub releases](https://github.com/lobehub/lobehub/releases)
