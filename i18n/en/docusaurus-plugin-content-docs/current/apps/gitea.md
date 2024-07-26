---
title: Gitea
slug: /gitea
tags:
  - Gogs
  - Gitlab
  - DevOps
---

import Meta from './_include/gitea.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. After installing Gitea in the **Websoft9 console**, view the application details through **My Applications** and get the login information in the **Access** tab.

2. Follow the installation wizard to complete the initialization, and do not modify any parameters in the **General Settings**.

   - Base URL: The installation wizard program automatically gets the browser URL to fill in.
   - HTTP Service Port: This is the container port and cannot be changed.
   - SSH service port: This is the container port and the corresponding host port, which has been set by environment variables and cannot be changed.
   - Database Setting: Please choose SQLite, if you choose other database, you need to prepare the available database in advance.

3. Administrator account settings or Register the first account after login (both are administrator accounts)


## Configuration options{#configs}

- Multilingual (✅)
- Configuration file: *gitea/conf/app.ini*

## Administer{#administrator}


## Troubleshooting{#troubleshooting}

