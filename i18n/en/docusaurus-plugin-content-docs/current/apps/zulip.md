---
title: Zulip
slug: /zulip
tags:
  - Zulip
  - Team Collaboration
  - Team Communications
---


import Meta from './_include/zulip.md';

<Meta name="meta" />

## Getting Started {#guide}

### Initial Setup {#wizard}

1. Log in to the Websoft9 Console, go to **Gateway** in the left menu, and follow the steps to configure HTTPS for Zulip (**Required**).

2. After completing the installation of Zulip in the **Websoft9 Console**, retrieve the application's **Overview** from **My Apps**:

   - Obtain the **URL** in the **Access** tab.
   - Obtain the **Main Container ID** in the **Container** tab.

3. Access the container and execute the command to generate a link for creating a new organization:

   ```
   docker exec -u zulip "Master container ID obtained in step 2" /home/zulip/deployments/current/manage.py generate_realm_creation_link
   ```

4. Use a local browser to access the URL returned in step 3, create the organization and users, and complete the initialization.

## Configuration Options {#configs}

- Multilingual (✅)

## Administration {#administrator}

## Troubleshooting {#troubleshooting}
