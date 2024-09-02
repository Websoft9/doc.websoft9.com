---
title: Vtiger CRM
slug: /vtiger
tags:
  - CRM
  - 客户关系管理
  - 销售管理
---

import Meta from './\_include/vtiger.md';

<Meta name="meta" />

## Getting Started {#guide}

### Initializing {#wizard}

1. After installing Vtiger CRM on Websoft9 console, view the application details through “My Applications”.

   - Get access information in the **Access** tab
   - Get the **database account** in the **Database** tab

2. Enter the Vtiger CRM installation wizard, when the environment testing step passed, start to fill in the database parameters

   - Host Name: Get from application management
   - User Name: `vtiger
   - Password: Get in the application management
   - Database Name: `vtiger`

3. Then set up the first administrator account

4. Complete the subsequent settings and enter the console.

## Configuration options {#configs}

- Multi-language (√): You need to download [Language Pack](https://marketplace.vtiger.com/app/listings) first, and then import it as Modules in the backend.
- 模块导入（√）：**Setting > CRM Setting > Module Management**

- Online Marketplace: Set **Extension Store** in the background to enter the marketplace, register and login to install it online.

- SMTP（√）： **Settings > CRM Settings > CONFIGURATION > Outgoing Server**

## Administrative maintenance {#administrator}

## Troubleshooting.

#### Can't access Vtiger CRM after changing domain name?

Error message: _Invalid compiled template for 'modules/Install/Header.tpl'_  
Problem Cause: Vtiger CRM will generate a cache file to record the access address after startup.  
Solution: Enter the Vtiger CRM container and delete the cache file with the following command

```
- rm -rf path/test/templates_c/v7
- rm -rf path/vtigercrm/cache/*
```
