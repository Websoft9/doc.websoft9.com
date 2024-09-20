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

    - Get the **access URL** in the **Access** tab.
    - Get the **App Id** in the **Overview**.

2. Run the following command to create an admin account and get the initial **installation URL suffix**:

    ```
    docker exec <App Id> su -m -c "bin/cake passbolt register_user -u "YOUR_EMAIL" -f "YOUR_NAME" -l "YOUR_LASTNAME" -r admin" -s /bin/sh www-data
    ```

3. Use your local browser to visit `http://URL/installation URL suffix` and go to the initialization wizard to complete it in order:

   - Install the Passbolt browser plugin
   - Set the administrator password

4. After completing the initialization, log in to the Passbolt console and set up SMTP before inviting other users to enroll via email.

## Configuration options{#configs}

- Multilingual (×): not support Chinese
- SMTP: Console **administration > Email server**

## Administer{#administrator}

## Troubleshooting{#troubleshooting}