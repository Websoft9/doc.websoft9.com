---
title: YouTrack
slug: /youtrack
tags:
  - Agile Development
  - Project Management
  - YouTrack
---

import Meta from './_include/youtrack.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of YouTrack at **Websoft9 Console**, get the applicaiton's **Overview** from **My Apps**  

    - Obtain **URL** in the **Access** tab
    - Obtain **Main Container ID** in **Container** tab

2. The local browser accesses the **URL** in step1 and start the initialization.

3. Run the command to get the token, enter the token in the initialization page, and go to the next step.

    ```
    docker exec "**Main Container ID** in step1" cat /opt/youtrack/conf/internal/services/configurationWizard/wizard_token.txt
    ```

4. Click **Set Up** on the page and follow the wizard to complete the initialization and start using YouTrack.

### Change Base URL

Refer to: [Change Base URL](https://www.jetbrains.com/help/youtrack/server/change-base-url-listen-port.html)

## Configuration options{#configs}

- Multilingual (√)

## Administer{#administrator}

## Troubleshooting{#troubleshooting}
