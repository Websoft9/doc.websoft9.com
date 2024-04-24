---
sidebar_position: 3
slug: /suitecrm/admin
tags:
  - SuiteCRM
  - 企业管理
  - CRM
---

# SuiteCRM Maintenance

This chapter is special guide for SuiteCRM maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### SuiteCRM Backup and Restore

**Set Automatic Backup**

SuiteCRM have the Backups interface

1. Log into your existing SuiteCRM application as the administrator and click admin on the right-hand corner of the page.
2. System->Backups
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/suitecrm/suitecrm-backupfunction-websoft9.png)

3. Input the backup directory adn Filename,then click the “Confirm Settings”
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/suitecrm/suitecrm-backup-websoft9.png)

4. Settings confirmed. Press "run backup" to perform the backup.
5. Now,your backup file has been generated
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/suitecrm/suitecrm-backupfiles-websoft9.png)

> Refers to the[SuiteCRM Backup](https://docs.suitecrm.com/developer/best-practices/#_backup)

### SuiteCRM Upgrade

The Upgrade Wizard provides a quick way to upgrade to the latest version of the SuiteCRM application. It includes critical upgrade logic as well as the SQL commands needed to upgrade the application. Ensure that the config.php file for your installation, located in the SuiteCRM root directory, is writable, before using the Upgrade Wizard. Note: Manual upgrades by file replacements and running the upgrade SQL are not supported.

1. Download the appropriate SuiteCRM Upgrade zip file from the SuiteCRM website or GitHub Repository to your local machine.

2. Log into your existing SuiteCRM application as the administrator and click admin on the right-hand corner of the page.
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/suitecrm/suitecrm-upgradewz-websoft9.png)

3. Click Upgrade Wizard in the Systems panel of the Administration Home page.


> Refers to the [SuiteCRM Documentation](https://docs.suitecrm.com/) to get start your SuiteCRM tutorial


## Troubleshoot{#troubleshoot}

In addition to the SuiteCRM issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### SuiteCRM installation wizard steps to connect to the database, click [Next] nothing happens?

**Cause of the problem**: After investigation, it is found that there is a file 404 in the [Next] action (it is estimated to be triggered by Ajax), that is, there is a file that cannot be downloaded and the program does not respond.
![](https://libs.websoft9.com/Websoft9/DocsPicture/en/suitecrm/suitecrm-noresponse-websoft9.png)

**Solution**: Temporarily purchase a Windows server in Hong Kong, open a browser on this server and install SuiteCRM


## FAQ{#faq}