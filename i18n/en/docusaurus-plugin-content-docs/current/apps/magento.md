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

Completed installation Magento at Websoft9 console, get the applicaiton's overview and access credentials from **My Apps**  

![](./assets/magento-backend-websoft9.png)

### Switch to Chinese {#setlanguage}

Websoft9 has pre-built Magento's Chinese package file zh_Hans_CN, just enable it:

#### Backend

Login to Magento as administrator, select **Account Setting(on upper right) > Interface Local**, select Interface Local as Chinese.

#### frontend

1. Enter the command mode of the Magento container and run the following command
   ```
   cd /bitnami/magento/
   php bin/magento config:set --scope=stores --scope-code=default general/locale/code zh_Hans_CN
   php bin/magento cache:clean
   php bin/magento cache:flush
   ```

2. Log in to Magento as administrator, open: Stores > Configuration > General > Locale Options, set Locale to Chinese.


### Install extensions {#installplugin}

Extensions are anything that is not part of Magento's core functionality, including modules, bodies, language packs, etc.

Extensions are installed by connecting to Magento's composer repository via php composer. To install an extension, you need to enter the repository's [Access Key](#key).   

Refer to: [Install an extension](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/tutorials/extensions) 


### Setting up the Access Key{#key}

The Access Key is the credentials for Magento to use Marketplace resources:

1. Register a [Magento account](https://account.magento.com/applications/customer/login), log in to Marketplace, and create your own Access Key from the Access Keys page of your My Profile. 

2. Create a new file auth.json based on auth.json.example in the root directory of your Magento application. 

3. Fill in the auth.json file with the Access Key.


### Caching and Indexing

After configuring Magento, you may need to refresh the cache or rebuild the index:

- Via the Magento backend: `System` > `Tools`.
- Command line settings: `php bin/magento cache:flush`, `php magento indexer:reindex`

## Configuration options{#configs}

- [Extension Management](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/tutorials/extensions)

- CLI: `magento list`

- [API](https://devdocs.magento.com/guides/v2.2/get-started/bk-get-started-api.html)

- Multilingual (✅ ): you need to download the language pack and import it.

- Online Backup: **Stores > Configuration > ADVANCED > Backup Settings**.

- SMTP (✅ )
  1. Refer to [Email communications](https://experienceleague.adobe.com/zh-hans/docs/commerce-admin/systems/communications/email-) for SMTP parameters. communications) Fill in the SMTP parameters 

  2. Fill in the sender's email address (same name as the SMTP email address) in **Backup > Store > Configuration > Store Email Address > General Contact**.

## Administer{#administrator}

- **Replacement of URL additional settings**: After changing the Magneto domain name in the Websoft9 console, you also need to update the Magento URL via the CLI
   ```shell
   php bin/magento config:set web/unsecure/base_url http://www.mydomain.com/ # change to your actual domain name, must end with /
   php bin/magento config:set web/unsecure/base_url http://www.mydomain.com/ # change to your actual domain name, must end with /
   ```

- **Additional HTTPS settings**: After setting up Magento's HTTPS in the Websoft9 console, you also need to configure it via CLI commands:
  ```
  #1 set your url
  php bin/magento setup:store-config:set --use-secure=1 --use-secure-admin=1 --base-url-secure="https://www.yourdomain.com/”

  #2 flush cache
  php bin/magento cache:flush 
  ```

- **Upgrade**: Magento upgrades are very complex, refer to the relevant documentation 
  - [Recommended reading for upgrade planning](https://experienceleague.adobe.com/en/docs/commerce-operations/upgrade-guide/resources/recommended-reading)
  - [Perform an upgrade](https://experienceleague.adobe.com/en/docs/commerce-operations/upgrade-guide/implementation/perform-upgrade)

## Troubleshooting{#troubleshooting}

#### Cron job warning?

Reason: One or more indexers are invalid. Make sure your Magento cron job is running     
Solution: Need to rebuild the indexes and refresh the page in the backend.
  ```
  php bin/magento indexer:reindex
  ```

#### Magento running slow?

Magento is a complex enterprise-level e-commerce system that requires high computing resources.

#### Can't find the backend login?

Enter the Magento container and view or modify it with the command ``shell:  

```shell.
# Show Magento(URL)
magento info:adminuri

# Update Magento(URL)
magento setup:config:set --backend-frontname=[yourAdminUrl] -n
```

#### Redirection causing inaccessibility?

Description: Error message ERR_TOO_MANY_REDIRECTS magento admin     
Reason: If we exclude redirection problems in the `.htaccess` file, the most likely cause is the URL   
Solution: Change the URL via command line or **core_config_data** datasheet   

```shell
php bin/magento setup:store-config:set --use-secure=1 --use-secure-admin=1 --base-url-secure="https://www.yourdomain.com/”
php bin/magento cache:flush
```

#### After setting HTTPS, the page is messed up?

Description: After setting HTTPS, the website can be accessed, but the page is messed up.    

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

Description: The frontend can't display product information properly, error “We can't find products matching the selection”   
Reason: After log investigation, it is found that the product attribute **eanl3** field is abnormal.   
Solution: **STORES > Attributes > Product** reset this field.

