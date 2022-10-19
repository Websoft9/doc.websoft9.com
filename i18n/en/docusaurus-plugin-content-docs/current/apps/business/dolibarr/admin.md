---
sidebar_position: 3
slug: /dolibarr/admin
tags:
  - Dolibarr
  - CRM
  - 客户成功
---

# Dolibarr Maintenance

This chapter is special guide for Dolibarr maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide


### Dolibarr Backup

Dolibarr have provide the automatic backup tools

1. Login as superuser,admin tools->backup,you can enter the interface
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/dolibarr/dolibarr-backup-websoft9.png)
2. Click the “Generate backup” button,backup database, download all files in Dolibarr root directory
3. Login as superuser,admin tools->restore,you can enter the interface
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/dolibarr/dolibarr-restore-websoft9.png)
4. Restore the data, from a backup dump file, into the database of the new Dolibarr installation or into the database of this current installation (dolibarr). Warning, once restore is finished, you must use a login/password, that existed when backup was made, to connect again. To restore a backup database into this current installation, you can follow this assistant.

### Dolibarr Upgrade

## Troubleshoot{#troubleshoot}

In addition to the Dolibarr issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

## FAQ{#faq}

#### Which database does this Dolibarr package use?

Mariadb

#### Can I use Cloud database for Dolibarr?

Yes

