---
title: Rundeck
slug: /rundeck
tags:
  - Automation Systems
  - DevOps
  - Runbook
---

import Meta from './\_include/rundeck.md';

<Meta name="meta" />

## Getting Started {#guide}

### Initial Setup {#wizard}

1. After completing the installation of Rundeck in the **Websoft9 Console**, retrieve the application's **Overview** and **Access** information from **My Apps**.

2. Change the password immediately after logging in.

## Configuration Options {#configs}

- Multilingual (✅)

## Administration {#administrator}

## Troubleshooting {#troubleshooting}

#### Can't access Rundeck through IP?

You need to change the environment variable **RUNDECK_GRAILS_URL** to `http://$W9_URL:$W9_HTTP_PORT_SET`, and rebuild the application for the changes to take effect.
