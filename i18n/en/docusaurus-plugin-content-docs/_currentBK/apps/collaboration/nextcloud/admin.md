---
sidebar_position: 3
slug: /nextcloud/admin
tags:
  - Nextcloud
  - File sync and share
  - knowledge Management
---

# Nextcloud Maintenance

This chapter is special guide for Nextcloud maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### Nextcloud online backup

This section provides Nextcloud online backup solution.

1. Log in Nextcloud console as administrator, install **[OwnBackup](https://apps.nextcloud.com/apps/ownbackup)** 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-backupapps-websoft9.png)
2. Go to【Admin】>【OwnBackup】, start backup, and you can restore it.
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-backupapp002-websoft9.png)

### Nextcloud Upgrade

Nextcloud provides a user-friendly upgrade (update) portal. You can complete the update of the main version and APP plug-in according to the update prompt of the system.
> Before upgrade, take a necessary snapshot of the instance in case of the upgrade failed.

**Core Upgrade**

Upgrades between core and APP plug-in are different. For core upgrade, take the following steps:

1. Log in Nextcloud console, go to【Admin】>【Basic Settings】, click the【Open Updater】button when there is a new version.
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-openupdater-websoft9.png)

2. Go to Updater.
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-updater-websoft9.png)

3. Check the upgrade requirement, then click 【Start update】

4. The system enters the automatic upgrade process. As the download and upgrade process is relatively long, please be patient.

**Apps Upgrade**

Steps for APPs upgrade are as follows:

1. Log in Nextcloud console, go to 【Apps】, find the apps that need upgrade.
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-updatelist-websoft9.png)

2. Click 【Update】 button, wait for some minutes.

3. Complete all updates until all apps are up to date.

> During the upgrade process, If some problem occur, for example, unable to download upgrade package, or no read and write access, please check the network connection or ensure Nextcloud directory has read and write access.

## Troubleshoot{#troubleshoot}

In addition to the Nextcloud issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  


#### After the domain configuration, find page layout confusion or the picture cannot be displayed?

This problem occurs if you install through IP, and then bind the domain name. To solve it, please change the IP address to the domain name in Nextcloud [Confuguration file](../nextcloud#path).

#### Failed to install plugin due to network timeout?

Use [manual installation](../nextcloud#minstallplugin) method

## FAQ{#faq}

#### Nextcloud support multi-language?

Yes.

#### What is the relationship between Nextcloud and ownCloud?

Nextcloud is a branch project started by ownCloud inventor Frank Karlitschek and a dozen experienced open source entrepreneurs and engineers, similar to the relationship between MariaDB and MySQL.

#### Does Nextcloud provide a client?

Yes, includes: Nextcloud Desktop Client, Nextcloud Android App, Nextcloud iOS App

#### How can Nextcloud view & edit file online?

You should complete the [OnlyOffice setting](../nextcloud/solution#onlyoffice) on your Nextcloud.

#### Nextcloud can integrate external storage?

Yes，refer to [external storage](https://docs.nextcloud.com/server/latest/admin_manual/configuration_files/external_storage_configuration_gui.html#storage-configuration)
