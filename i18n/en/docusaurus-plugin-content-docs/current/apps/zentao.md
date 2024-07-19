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

import Meta from './_include/zentao.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of Zentao at **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

2. Access the initialization interface, following the prompts to complete the steps (it is recommended to maintain the default database connection settings)

3. After installation, experience the backend 
   ![](./assets/zentao-backend-websoft9.png)

## Configuration options{#configs}

- Multilingual (✅): Support for backend switching
- Command Line: [Initialization Admin Script](https://www.zentao.net/book/zentaopmshelp/35.html)
- Plugin Marketplace (✅): [Register](https://www.zentao.net/user-register.html) official website account to install plugins online
- Client (✅): only for Zendo Pro and Enterprise Edition users
- Zendo directory (already mounted): */data*
- Plug-in path (mounted): */data/module*
- Integrating Git (✅)
- SMTP (✅): **Backend > Message > Mail**, select STMP as sending method

## Administer{#administrator}

- Install plugins: Support [Plugin Market](https://www.zentao.net/extension-browse.html) online installation, also supports downloading and unzipping to the plugin directory to install
- Reset password: Modify the database **zt_user** table, change the password field value to `e10adc3949ba59abbe56e057f20f883e`, and the password will be reset to `123456`
- Online backup: **Admin > System > Backup**

## Troubleshooting{#troubleshooting}

#### Locked multiple times by wrong password entry?

1. It will be unlocked automatically after 10 minutes
2. Administrator login, selecting **System→ Users**, there is an unlock button in the action bar

