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

## Getting started{#guide}

### Initial setup{#wizard}

1. Log in to the Websoft9 Console, go to **Gateway** in the left menu, and follow the steps to configure HTTPS for Zulip (**Required**).

2. When completed installation of Zulip at **Websoft9 Console**, get the applicaiton's **Overview** from **My Apps**  

    - Obtain **URL** in the **Access** tab
    - Obtain **Main Container ID** in **Container** tab

3. Access the container and execute the command to generate a link to create the new organization

    ```
    docker exec -u zulip "Master container ID obtained in step2" /home/zulip/deployments/current/manage.py generate_realm_creation_link
    ```

4. Local browser accesses the URL returned in step3 and creates the organization and users to complete the initialization.

## Configuration options{#configs}

- Multilingual (√)

## Administer{#administrator}

## Troubleshooting{#troubleshooting}