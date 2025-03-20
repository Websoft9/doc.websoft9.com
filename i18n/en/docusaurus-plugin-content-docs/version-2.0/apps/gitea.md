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

1. After installing Gitea through the **Websoft9 console**, view the application details in the **My Applications** section and get the login information from the **Access** tab.

2. Follow the installation wizard to complete the initialization without modifying any parameters in the **General Settings**.

   - Base URL: The installation wizard will automatically detect and fill in the browser URL.
   - HTTP Service Port: This port is set for the container and cannot be changed.
   - SSH Service port: This port is set for both the container and the corresponding host port via environment variables and cannot be altered.
   - Database Setting: Choose SQLite. If you select a different database, ensure it is prepared and available in advance.

3. Set up the administrator account or register the first account after loggin in. (Both options will create administrator accounts)


## Configuration options{#configs}

- Multilingual (✅)
- Configuration file: *gitea/conf/app.ini*

## Administer{#administrator}


## Troubleshooting{#troubleshooting}

