---
title: Strapi
slug: /strapi
tags:
  - Backend as a Service
  - Headless CMS
  - strapi
---

import Meta from './\_include/strapi.md';

<Meta name="meta" />

## Getting Started {#guide}

### Initial Setup {#wizard}

1. After completing the installation of Strapi in the **Websoft9 Console**, retrieve the application's overview and access information from **My Apps**.

2. Wait for the Strapi container to start: The first time Strapi starts, it will pull external software packages online, so you may need to wait a few minutes before accessing the initial page.

### Create Your Data Model

1. Log in to Strapi, then go to **Plugins > Content-type Builder** and add a dataset. For example, name it `websoft9`.

2. Add a user under **Users** and set the role to `public`.

3. Navigate to **Settings > USERS & PERMISSIONS PLUGIN > Roles**, edit the public role to grant access to the `websoft9` dataset.

4. Access the following URLs to obtain data:
   ```bash
   # Get all data
   http://URL/websoft9

   # Get the first piece of data
   http://URL/websoft9/1
   ```

## Configuration Options {#configs}

- Multilingual (√)

## Administration {#administrator}

## Troubleshooting {#troubleshooting}

#### Strapi First Startup Error?

**Reason**: When Strapi is first launched, it installs some **Node.js** packages from GitHub, which may fail due to network issues.  
**Solution**: Ensure that the server has smooth access to the npm repository and GitHub.
