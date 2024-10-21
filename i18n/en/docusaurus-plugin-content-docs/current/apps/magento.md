---
title: Magento
slug: /magento
tags:
  - E-commerce
  - Payment
  - Cross-border e-commerce
---

import Meta from './_include/magento.md';

<Meta name="meta" />

## Getting started{#guide}

### Login verification{#verification}

Completed the installation of Magento at the Websoft9 console, and get the applicaiton's overview and access credentials from **My Apps**  

![](./assets/magento-backend-websoft9.png)

### Switch to Chinese {#setlanguage}

Websoft9 has pre-built Magento's Chinese package file `zh_Hans_CN`. To enable it:

#### Backend

1. Log in to Magento as an administrator.
2. Select **Account Settings** (at the upper right) > **Interface Locale**.
3. Set **Interface Locale** to Chinese.

#### frontend

1. Enter the command mode of the Magento container and run the following command:
   ```
   cd /bitnami/magento/
   php bin/magento config:set --scope=stores --scope-code=default general/locale/code zh_Hans_CN
   php bin/magento cache:clean
   php bin/magento cache:flush
   ```

2. Log in to Magento as an administrator, and navigate to: Stores > Configuration > General > Locale Options, then set **Locale** to Chinese.


### Install extensions {#installplugin}

Extensions are additional functionalities not part of Magento's core, including modules, language packs, etc.

They are installed by connecting to Magento's composer repository via PHP Composer. To install an extension, you need to enter the repository's [Access Key](#key).   

Refer to: [Install an extension](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/tutorials/extensions) 


### Setting up the Access Key{#key}

The Access Key is required for Magento to use Marketplace resources:

1. Register a [Magento account](https://account.magento.com/applications/customer/login), log in to Marketplace, and create your own Access Key from the Access Keys page of your Profile. 

2. Create a new file named `auth.json` based on `auth.json.example` in the root directory of your Magento application. 

3. Populate the auth.json file with the Access Key.


### Caching and Indexing

After configuring Magento, you may need to refresh the cache or rebuild the index:

- Via the Magento backend: Navigate to `System` > `Tools`.
- Command line: Use the following commands:
  ```
  php bin/magento cache:flush
  php magento indexer:reindex
  ```

## Configuration options{#configs}

- [Extension Management](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/tutorials/extensions)

- CLI: Use the command `magento list`

- [API](https://devdocs.magento.com/guides/v2.2/get-started/bk-get-started-api.html)

- Multilingual (✅ ): Download and import the language pack.

- Online Backup: Configure via **Stores > Configuration > ADVANCED > Backup Settings**.

- SMTP (✅ )
  1. Refer to [Email communications](https://experienceleague.adobe.com/zh-hans/docs/commerce-admin/systems/communications/email-) for SMTP parameters.

  2. Fill in the sender's email address (matching the SMTP email address) under **Backup > Store > Configuration > Store Email Address > General Contact**.

## Administer{#administrator}

- **Replacement of URL additional settings**: After changing the Magneto domain name in the Websoft9 console, update the Magento URL via CLI
   ```shell
   php bin/magento config:set web/unsecure/base_url http://www.mydomain.com/ # change to your actual domain name, must end with /
   php bin/magento config:set web/unsecure/base_url http://www.mydomain.com/ # change to your actual domain name, must end with /
   ```

- **Additional HTTPS settings**: After setting up Magento's HTTPS in the Websoft9 console, configure it via CLI commands:
  ```
  #1 set your url
  php bin/magento setup:store-config:set --use-secure=1 --use-secure-admin=1 --base-url-secure="https://www.yourdomain.com/”

  #2 flush cache
  php bin/magento cache:flush 
  ```

- **Upgrade**: Magento upgrades can be complex. Refer to the relevant documentation 
  - [Recommended reading for upgrade planning](https://experienceleague.adobe.com/en/docs/commerce-operations/upgrade-guide/resources/recommended-reading)
  - [Perform an upgrade](https://experienceleague.adobe.com/en/docs/commerce-operations/upgrade-guide/implementation/perform-upgrade)

## Troubleshooting{#troubleshooting}

#### Cron job warning?

Reason: One or more indexers are invalid. Ensure your Magento cron job is running     
Solution: Rebuild the indexes and refresh the backend page.
  ```
  php bin/magento indexer:reindex
  ```

#### Magento running slow?

Magento is a complex enterprise-level e-commerce system that requires significant computing resources.

#### Can't find the backend login?

Enter the Magento container and view or modify it using:  

```shell.
# Show Magento(URL)
magento info:adminuri

# Update Magento(URL)
magento setup:config:set --backend-frontname=[yourAdminUrl] -n
```

#### Redirection causing inaccessibility?

Description: Error message ERR_TOO_MANY_REDIRECTS in Magento admin     
Reason: If redirection issues in the `.htaccess` file are excluded, the most likely cause is the URL configuration  
Solution: Change the URL via the command line or **core_config_data** datasheet   

```shell
php bin/magento setup:store-config:set --use-secure=1 --use-secure-admin=1 --base-url-secure="https://www.yourdomain.com/”
php bin/magento cache:flush
```

#### After setting HTTPS, the page is messed up?

Description: The website is accessible, but the page layout is broken.    

Solution:

```shell
php bin/magento maintenance:enable
# Delete static and cached files
php rm -rf var/di/* && rm -rf var/generation/* && rm -rf var/cache/* && rm -rf var/page_cache/* && rm -rf var/view_preprocessed/* && rm -rf pub/static/* && rm -rf generated/* 

# Redeploy static files
php bin/magento setup:upgrade 
php bin/magento setup:di:compile
php bin/magento setup:static-content:deploy -f

# Rebuild index and cache
php bin/magento indexer:reindex
php bin/magento cache:clean && bin/magento cache:flush
php bin/magento maintenance:disable 
```

#### Product detail page not displaying properly?

Description: The frontend can't display product information properly, showing the error “We can't find products matching the selection”   
Reason: Investigation might reveal that the product attribute **eanl3** field is abnormal.   
Solution: Reset this field via **STORES > Attributes > Product**.

