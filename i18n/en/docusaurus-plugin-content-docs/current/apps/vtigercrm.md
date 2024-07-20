---
title: Vtiger CRM
slug: /vtiger
tags:
  - CRM
  - Customer Relationship Management
  - Sales Management
---

import Meta from './_include/vtiger.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of Vtiger CRM at **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  
  
   - Get access information in the **Access**
   - Get **database account** in the **Database** 

2. Access the Vtiger CRM installation wizard, when the environment testing step passed, start to fill in the database parameters.

   - Host Name: get from application management 
   - User Name: `vtiger`
   - Password: get in the application management
   - Database Name: `vtiger`

3. Then set the first administrator account.

4. After completing the subsequent settings, enter the console.


## Configuration options{#configs}

- Multilingual(✅): You need to download [Language Pack](https://marketplace.vtiger.com/app/listings) first, and then import it as Modules in the backend.

- Module Import(✅): Select **Setting > CRM Setting > Module Management**

- Online Marketplace: Set **Extension Store** in the background to enter the marketplace, and you can install online after registering and logging in.

- SMTP(✅): Select **Settings > CRM Settings > CONFIGURATION > Outgoing Server**

## Administer{#administrator}


## Troubleshooting{#troubleshooting}

#### Can't access Vtiger CRM after changing domain name?

Description: *Invalid compiled template for 'modules/Install/Header.tpl'*  
Reason: Vtiger CRM will generate a cache file to record the access address after startup.    
Solution: Access the Vtiger CRM container and delete the cache file with the following command  

```
- rm -rf path/test/templates_c/v7
- rm -rf path/vtigercrm/cache/*
```

