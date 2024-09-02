---
title: ERPNext
slug: /erpnext
tags:
  - ERP
  - Enterprise Management
  - Manufacturing
  - Supply Chain
  - Purchasing
---

import Meta from './_include/erpnext.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. After completing the installation of ERPNext in the **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

2. Complete the installation of wizard step by step

## Configuration options{#configs}

- Multilingual (✅)
- SMTP (✅): Select **Console > Settings > Email Domain**, and fill in the SMTP parameters
- [ERPNext Documentation](https://docs.erpnext.com)
- [CLI to manage Multi-tenant deployments for Frappe apps](https://github.com/frappe/bench)
- [API](https://frappeframework.com/docs/user/en/api)

## Administer{#administrator}

- Reset the administrator password: Access the ERPNext container and run the command
  ```export GIT_PYTHON_REFRESH=quiet && /usr/local/bin/bench set-admin-password newpassword```

- Automatic backup (recommended): Log in to ERPNext, Select **Settings > System Settings** 

- [Command line backup](https://frappeframework.com/docs/user/en/bench/reference/backup):
  ```bench --site URL backup```

## Troubleshooting{#troubleshooting}

#### Failed to download Backups?

Reason unknown.

#### Frappe, Bench, ERPNext?

- ERPNext is a free ERP system based on the [Frappe](https://github.com/frappe/frappe) framework.
- Frappe is a framework for the rapid development of integrated JS and Python applications.
- [Bench](https://github.com/frappe/bench) is a CLI tool within the Frappe framework architecture for creating and managing Frappe-based applications.

The Frappe framework consists of two main parts: the app, which is the back-end Python code, and the site, which is the front-end component that handles HTTP requests.

#### ERPNext service startup failed?
  Ensure the hostname contains a dot **.** , e.g. `erpnext12.14.0` is a non-compliant hostname.

You can use the following command to change the hostname:

    ```shell
    hostnamectl set-hostname erpnext
    ```

#### Error reported after changing password in Chrome?

This is not a server-side issue; simply update your browser.

#### Error when running Bench command ?

Description: You should not run this command as root.  
Solution: Bench can only be run from the `frapper` user, you must switch to this user first:

    ```shell
    su - frapper
    ```

#### ConnectionError: Error 111 for erpnext?

  The ERP initialization process may report `ConnectionError: Error 111 for erpnext`. [The official reply](https://github.com/frappe/frappe_docker/issues/1314) indicates this is normal because only the configuration job container has completed, and the Redis connection is correct.
