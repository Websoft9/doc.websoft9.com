---
title: Zentao
slug: /zentao
tags:
  - Zentao
  - git
  - Requirements
  - Kanban
  - Project Management
---

import Meta from './\_include/zentao.md';

<Meta name="meta" />

## Getting Started {#guide}

1. After completing the installation of Zentao via the **Websoft9 Console**, retrieve the application’s **Overview** and **Access** information from **My Apps**.

2. Access the initialization interface and follow the prompts to complete the setup steps (it is recommended to keep the default database connection settings).

3. Once installed, explore the backend.
   ![](./assets/zentao-backend-websoft9.png)

## Configuration Options {#configs}

- **Multilingual (✅)**: Supports backend language switching.
- **Command Line**: Use the [Initialization Admin Script](https://www.zentao.net/book/zentaopmshelp/35.html).
- **Plugin Marketplace (✅)**: [Register](https://www.zentao.net/user-register.html) for an official account to install plugins online.
- **Client (✅)**: Available for Zentao Pro and Enterprise Edition users.
- **Zentao Directory**: Already mounted at `/data`.
- **Plugin Path**: Already mounted at `/data/module`.
- **Git Integration (✅)**: Supports integration with Git.
- **SMTP (✅)**: Set up SMTP via **Backend > Message > Mail**, select SMTP as the sending method.

## Administration {#administrator}

- **Install Plugins**: Supports online installation from the [Plugin Market](https://www.zentao.net/extension-browse.html). You can also download and unzip to the plugin directory for manual installation.
- **Reset Password**: Modify the password field in the **zt_user** table in the database to `e10adc3949ba59abbe56e057f20f883e`, which will reset the password to `123456`.
- **Online Backup**: Navigate to **Admin > System > Backup** to schedule backups.

## Troubleshooting {#troubleshooting}

#### Locked multiple times by wrong password entry?

1. The system will automatically unlock after 10 minutes.
2. Admin can log in, go to **System > Users**, and use the unlock button in the action bar.
