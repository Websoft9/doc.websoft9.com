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

### 自动备份

Prestashop 自动备份是通过一个名称为【1-Click Upgrade】的插件实现的，具体步骤如下：

1. 登录 PrestaShop 后台，打开【Modules Catalog】，搜索【upgrade】，安装备份插件
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-upgrade001-websoft9.png)

2. 安装完成后，点击【配置】，进入模块设置界面

3. 根据设置建议，将系统置为维护模式（maintenance mode）
   
4. 点击【Upgrade PrestaShop now】按钮，开始升级
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-upgrade002-websoft9.png)

5. 升级过程中首先会下载最新的安装包，受制于网络因素，这个过程可能会比较慢。
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-upgrade003-websoft9.png)

6. 升级过程的例外情况

   - 如果下载新版本这个步骤无法完成，需要多次尝试
   - 若出现 “you don't have permission...ajax-upgradetab.php” 的错误提示，升级失败，暂无解决办法

> 与升级有关的更多方案，请参考官方文档：[PrestaShop Backup](https://doc.prestashop.com/display/PS16/Manual+update)   

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