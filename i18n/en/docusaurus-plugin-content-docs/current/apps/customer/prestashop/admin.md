---
sidebar_position: 3
slug: /prestashop/admin
tags:
  - PrestaShop
  - eCommerce
---

# PrestaShop Maintenance

This chapter is special guide for PrestaShop maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### PrestaShop Backup and Restore

This section provides PrestaShop online database backup solution

1. Log in PrestaShop console as administrator
2. Open【Advanced Parameters】>【DB backup】
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-dbbackup-websoft9.png)
3. Create a new backup and download it

### Automatic backup

Prestashop automatic backup is realized through a plug-in named [1-Click Upgrade]. The specific steps are as follows:

1. Log in to the PrestaShop background, open [Modules Catalog], search for [upgrade], and install the backup plugin
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/prestashop/prestashop-upgrade001-websoft9.png)

2. After the installation is complete, click [Configuration] to enter the module setting interface

3. Put the system into maintenance mode as suggested by the settings
   
4. Click the [Upgrade PrestaShop now] button to start the upgrade
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/prestashop/prestashop-upgrade002-websoft9.png)

5. During the upgrade process, the latest installation package will be downloaded first. Due to network factors, this process may be slow.
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/prestashop/prestashop-upgrade003-websoft9.png)

6. Exceptions to the upgrade process

   - If this step of downloading a new version cannot be completed, several attempts are required
   - If the error message "you don't have permission...ajax-upgradetab.php" appears, the upgrade fails, and there is no solution yet

> For more solutions related to the upgrade, please refer to the official document: [PrestaShop Backup](https://doc.prestashop.com/display/PS16/Manual+update)

### PrestaShop Upgrade

PrestaShop can upgrade the Module online

1. Log in PrestaShop as administrator, open【Modules Catalog】
2. Find the module you need to upgrade, click the 【Upgrade】 button
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-upgrademodules-websoft9.png)


## Troubleshoot{#troubleshoot}

In addition to the PrestaShop issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.

#### PrestaShop Redirects Error

When add new language for PrestaShop, it will add redirects rules in the `.htaccess` file of PrestaShop root directory.

Check your `.htaccess` file in your application root directory, make sure there not any cycle redirects settings  

## FAQ{#faq}

#### PrestaShop support multi-language?

Yes

#### Why should I link to the PrestaShop Marketplace?

Just link PrestaShop Marketplace, you can use the resources of Marketplace online. [Connect Marketplace](../prestashop#connect-prestashop-marketplace)
