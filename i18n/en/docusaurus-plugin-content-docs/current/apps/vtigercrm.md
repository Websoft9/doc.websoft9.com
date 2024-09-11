---
title: Vtiger CRM
slug: /vtiger
tags:
  - CRM
  - Customer Relationship Management
  - Sales Management
---

import Meta from './\_include/vtiger.md';

<Meta name="meta" />

## Getting Started {#guide}

1. After completing the installation of Vtiger CRM through the **Websoft9 Console**, retrieve the application’s **Overview** and **Access** information from **My Apps**.

   - **Access Information**: Found in the **Access** section.
   - **Database Account**: Found in the **Database** section.

2. Access the Vtiger CRM installation wizard. Once the environment testing step passes, proceed to fill in the database parameters.

   - **Host Name**: Retrieve from the application management section.
   - **User Name**: `vtiger`
   - **Password**: Retrieve from the application management section.
   - **Database Name**: `vtiger`

3. Set the first administrator account.

4. Complete the remaining setup steps and enter the Vtiger CRM console.

## Configuration Options {#configs}

- **Multilingual (✅)**: First download the [Language Pack](https://marketplace.vtiger.com/app/listings), then import it as a module in the backend.

- **Module Import (✅)**: Navigate to **Settings > CRM Settings > Module Management** to import modules.

- **Online Marketplace (✅)**: Set up the **Extension Store** in the backend, register, and log in to install modules from the marketplace.

- **SMTP Configuration (✅)**: Navigate to **Settings > CRM Settings > CONFIGURATION > Outgoing Server** to set up SMTP.

## Administration {#administrator}

## Troubleshooting {#troubleshooting}

#### Can't access Vtiger CRM after changing the domain name?

- **Issue**: "Invalid compiled template for 'modules/Install/Header.tpl'"
- **Reason**: Vtiger CRM generates a cache file that records the access address after startup.
- **Solution**: Access the Vtiger CRM container and delete the cache file using the following commands:

```bash
rm -rf path/test/templates_c/v7
rm -rf path/vtigercrm/cache/*
```
