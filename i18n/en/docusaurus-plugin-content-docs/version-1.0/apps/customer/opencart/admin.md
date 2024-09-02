---
sidebar_position: 3
slug: /opencart/admin
tags:
  - OpenCart
  - eCommerce
---

# OpenCart Maintenance

This chapter is special guide for OpenCart maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### OpenCart Backup and Restore

This section provides OpenCart online database backup solution

1. Log in OpenCart console as administrator
2. Open:【Advanced Parameters】>【DB backup】,create a new backup and download it
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/opencart-backupdb-websoft9.png)

### OpenCart Upgrade

The following upgrade steps are a simplification of the official upgrade documentation:

1. Backup OpenCart source code and database, and download them to local computer
  
2. [Download](https://www.opencart.com/index.php?route=cms/download) the latest version of OpenCart and unzip it
  
3. Use SFTP to log in Server, upload latest OpenCart source code and cover the old
  
4. Upload the `config.php` and `admin/config.php` in the OpenCart root directory of backup to Server
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/Opencart-update001-websoft9.png)  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/Opencart-update002-websoft9.png) 
  
5. Visit *http://域名/install* to start upgrade
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/Opencart-update003-websoft9.png)  
  
6. Upgrading successfully
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/Opencart-update004-websoft9.png)  

> More upgrade details please refer to: [OpenCart Upgrading](https://docs.opencart.com/en-gb/upgrading/)


## Troubleshoot{#troubleshoot}

In addition to the OpenCart issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more. 

####  域名配置后，页面布局混乱？

**原因分析**：先通过 IP 安装，再绑定域名，导致默认 URL 发生变化   

**解决方案**：[修改 URL](../opencart)

#### 安装插件，显示403权限不足？

**现象描述**：错误信息 "you dont have permession to access /admin/index.php"   
**解决方案**：修改文件：/etc/httpd/conf.d/mod\_evasive.conf 中  DOSPageCount 2 改为 DOSPageCount 12 

## FAQ{#faq}

#### OpenCart support multi-language?
  
Yes

#### 安装 Extension 需要[设置 FTP 账号](http://docs.opencart.com/en-gb/extension/installer/)吗？

自 OpenCart3.0 开始已经不需要了
