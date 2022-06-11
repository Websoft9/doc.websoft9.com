---
sidebar_position: 3
slug: /zentao/admin
tags:
  - ZenTao（禅道）
  - 项目管理
---

# ZenTao Maintenance

This chapter is special guide for ZenTao maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### ZenTao Online backup&restore

This section provides ZenTao online backup&restore solution

1. Log in as adminitrator,go to Admin->Data->backup, Eit the Cron for autmatic backup
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-backupstr-websoft9.png)

2. Click Backup
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/zentao/zentao-backup-websoft9.png)

3. You can **restore** your backup online also

4. ZenTao's **Recycle** can restore the data your have deleted manually
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/zentao/zentao-recycle-websoft9.png)

### ZenTao Upgrade

ZenTao is upgraded by manually uploading code.

1. [Download](https://www.zentao.net/download.html) the latest source code of ZenTao, unzip it

2. Upload and cover your old ZenTao source code on your Server

3. Visit *https://Internet IP/upgrade.php* to start upgrade

4. If error like **" Uncaught Error: Call to a member function query() on null in li..."**, please set **777* permission recursively for the folder `zentao/www` and `zentao/tmp`, then try it again

> More details about upgrade, please refer to [ZenTao Upgrade](https://www.zentao.pm/book/zentaomanual/free-open-source-project-management-software-upgradezentao-18.html)

## Troubleshoot{#troubleshoot}

In addition to the ZenTao issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  


#### 密码输入错误多次被锁，怎么解决？

1. 10 分钟后会自动解锁。
2. 管理员登录，组织 → 用户 操作栏里有解锁按钮。

## FAQ{#faq}

#### ZenTao support multi-language?

Chinese and English

#### ZenTao Opensource is free?

Yes, it's License is ZPL. You can buy [ZenTao Enterpise](https://www.zentao.net/page/professional.html) also if you want to more functions

#### Why should you need to register account of ZenTao?

[Register](https://www.zentao.net/user-register.html)account of ZenTao, you can connect your ZenTao to ZenTao's Marketplace

#### Does ZenTao provide a client?

Yes, includes: Android App and iOS App. But not for opensource users