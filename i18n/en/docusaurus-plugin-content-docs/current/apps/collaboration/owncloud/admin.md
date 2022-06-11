---
sidebar_position: 3
slug: /owncloud/admin
tags:
  - ownCloud
  - 网盘
  - 知识管理
  - 团队协作
---

# ownClouds Maintenance

This chapter is special guide for ownCloud maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  


## Maintenance guide

### Nextcloud online backup

This section provides ownCloud online backup solution

1. Log in ownCloud console as administrator, install **[OwnBackup](https://en.websoft9.com/xdocs/owncloud-image-guide/#using-apps)** 
2. Go to【Admin】>【OwnBackup】, start backup
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-ownbackup-websoft9.png)
3. You can restore it also
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-restore-websoft9.png)

### ownCloud Upgrade

ownCloud provides a very user-friendly upgrade (update) portal, which can complete the update of the main version and APP plug-in according to the update prompt of the system.

**Plugin Upgrade**

1. After logging in to OwnCloud, see if there is an update notification in the upper right corner. if so, please click on the update entry in it.
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-updatenotify-websoft9.png)
2. After clicking on the update entry, enter the update interface.
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-updatelist-websoft9.png)
3. Click the "update" button and the system goes to "update" and wait patiently for the update
4. When all updates are completed, the update list shows "all apps are up to date"

> If there is a problem with the upgrade process, such as: unable to download the upgrade package/no read and write permissions, make sure that the network is connected/OwnCloud Directory has read and write permissions

**Master Program Upgrade**

1. Once have upgrade message "OwnCloud is available". Get more information on how to update.", you should upgrade it now
2. Go to 【Admin】>【Setting】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-openupdater-websoft9.png)
3. Go to Updater
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-updater-websoft9.png)
4. Click the button "Create a checkpoint" first
5. Click the button "Start"

## Troubleshoot{#troubleshoot}

In addition to the ownCloud issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### After the domain configuration, find page layout confusion or the picture cannot be displayed?

This problem occurs if you install through IP, and then bind the domain name. To solve it, please change the IP address to the domain name in Nextcloud [Confuguration file](../owncloud#path).

## FAQ{#faq}

#### ownCloud support multi-language?

Yes.

#### Does ownCloud provide a client?

Yes, includes: Nextcloud Desktop Client, Nextcloud Android App, Nextcloud iOS App

#### How can ownCloud view & edit file online?

You should complete the [OnlyOffice setting](../ownCloud/solution#onlyoffice) on your Nextcloud.

#### ownCloud can integrate external storage?

Yes.