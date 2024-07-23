---
title: Gogs
slug: /gogs
tags:
  - Git 
  - Code Repository
  - DevOps
---

import Meta from './_include/gogs.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

After installing Gogs on the **Websoft9 console**, view the application details through **My Applications** and get the login information in the **Access** tab.  

1. Use your local computer's browser to access the URL and enter the initialization page.   

2. Database settings: Please choose SQLite, if you choose any other database, you need to prepare available databases in advance.

3. Application basic settings: Refer to the instructions to avoid errors when filling.

   - Domain name: Use the URL of the current browser access (may include the port), remove the `http://` prefix, keep the latter part.
   - Application URL: Use the URL currently accessed by your browser.
   - SSH port: The port of the server that was set when Gogs was installed.
   - HTTP port: Do not modify.

4. Set the admin account and email address (admin is not allowed as a username).

5. After successful installation, enter the system backend

    ![](./assets/gogs-dashboard-websoft9.png)


## Configuration options{#configs}

- CLI: `./gogs -h`
- [Webhook](https://gogs.io/docs/features/webhook)
- Multilingual (✅): Automatically adapts to the browser language, which can also be selected in the bottom menu

## Administer{#administrator}


## Troubleshooting{#troubleshooting}

