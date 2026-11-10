---
title: QwenPaw
slug: /qwenpaw
tags:
  - QwenPaw
  - AI Agent
  - LLM
---

import Meta from './_include/qwenpaw.md';

<Meta name="meta" />

## Getting Started {#guide}

### Initialize {#wizard}

After installing QwenPaw in the Websoft9 console, open the Hub URL from the **Access** tab and sign in with the administrator credentials set during deployment. The first startup installs components required by the Hub; wait for the service health check to pass before using it.

### Manage users and runtimes {#users}

1. Open **User Management** in the Hub to create users, or allow self-registration according to the registration mode.
2. Each user gets an isolated QwenPaw runtime, workspace, credentials, and conversations after signing in.
3. In a user's personal Console, open **Settings → Models** to add a model provider and API key, or select a local model.

### Set the registration mode {#registration}

Set `QWENPAW_HUB_REGISTRATION_MODE` to control registration: `open` allows self-registration, `invite` uses invitations, and `closed` disables self-registration. For a trusted team deployment, consider setting it to `closed` and creating users as an administrator.

## Best Practices

### Restrict access to trusted users {#trusted-users}

QwenPaw Hub is an early release intended for trusted teams, not mutually untrusted users. The local runtime backend requires the container to run in privileged mode. First startup also requires network access to install dependencies. Restrict access to the Hub and choose an appropriate registration mode.

## Configuration {#configs}

| Setting | Description | Default / location |
|---------|-------------|--------------------|
| Hub Console | Hub web console port | 8000 |
| `W9_URL` | Source of the public Hub URL used to derive `QWENPAW_HUB_PUBLIC_BASE_URL` | Websoft9 app URL |
| `QWENPAW_HUB_REGISTRATION_MODE` | Self-registration mode | `open` |
| `W9_LOGIN_USER` / `W9_LOGIN_PASSWORD` | Seeds the Hub administrator on first startup | First startup only |
| `/app/working` | QwenPaw data directory | `qwenpaw_data` persistent volume |

Rebuild the app after changing `.env`. The initial administrator credentials are seeded only on first startup.

## Administration {#administrator}

### Upgrade

Upgrade the app from the Websoft9 console. Back up the `qwenpaw_data` persistent volume first. After upgrading, confirm that both the Hub and user runtimes are operating normally.

### Backup and restore

Back up the persistent data mounted at `/app/working`. To restore, put the data back in the corresponding volume, start the app, and check runtime status in the Hub's **Runtimes** page.

## Troubleshooting {#troubleshooting}

#### First startup takes a long time

On first startup, the container installs the Hub Docker SDK and `bubblewrap`. This requires network access and may take several minutes. Check the Compose logs for progress.

#### A user runtime cannot be created or started

Confirm that the container runs in privileged mode as configured, then check the error in the Hub's **Runtimes** page.

#### The Hub cannot be opened

Confirm that `W9_URL` matches the URL users open. Also check the port and firewall or cloud security group rules.

## References {#references}

- [QwenPaw quick start](https://qwenpaw.agentscope.io/docs/quickstart)
- [QwenPaw Hub documentation](https://qwenpaw.agentscope.io/docs/hub)
- [QwenPaw project documentation](https://github.com/agentscope-ai/QwenPaw)
