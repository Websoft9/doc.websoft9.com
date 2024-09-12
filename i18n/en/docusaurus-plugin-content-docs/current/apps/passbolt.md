---
title: Passbolt
slug: /passbolt
tags:
  - Passbolt
  - Password security
  - Password Management
---

import Meta from './_include/passbolt.md';

<Meta name="meta" />

## Getting Started {#guide}

### Initial setup{#wizard}

1. Once you have completed the installation of Passbolt in the **Websoft9 Console**, retrieve the application information from **My Apps**.

    - Get the access URL in the **Access** tab.
    - Get the **Main Container** in the **Container**.

2. Create an administrator account with the command, and generate a **path string** after the command is executed.

    ``
    docker exec "The **main container** from step1" su -m -c "bin/cake passbolt register_user -u "YOUR_EMAIL" -f "YOUR_NAME" -l "YOUR_LASTNAME" -r admin" -s /bin/sh www- data
    ```

3. Use your local browser to access the "URL in step1 + **path string** in step2".

4. Follow the prompts to install the Passbolt client plugin and set the master password.

5. After logging in, set the SMTP configuration in **Administration > Email Server**.

6. After the administrator adds a new user, the new user will receive the authentication code via email to register and log in.

## Configuration options{#configs}

- Multilingual (×): not support Chinese

## Administer{#administrator}

## Troubleshooting{#troubleshooting}