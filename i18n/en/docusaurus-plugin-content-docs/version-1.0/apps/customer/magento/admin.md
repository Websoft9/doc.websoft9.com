---
sidebar_position: 3
slug: /magento/admin
tags:
  - Magento
  - eCommerce
---

# Magento Maintenance

This chapter is special guide for Magento maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### Magento Backup and Restore

This section provides Magento online backup solution, please make a necessary snapshot backup in the cloud console in advance.

1. Log in Magento console, open 【System】>【System->Backup】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-backup-websoft9.png)
  
2. Set backup by yourself
    
3. Suggest you make the backup to your Schedule
   - Log in Magento console, open 【Stores】>【Configuration】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-bkscheduleset-websoft9.png)
   - go to【System】>【Backup Settings】, set your Schedule
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-bkschedulesets-websoft9.png)   

### Magento Upgrade

Magento provide two methond for Upgrade: Magento backend online upgrade and Composer command upgrade  

Below is the step for upgrade online:

1. Log in to your Magento, go to 【System】>【Web Setup Wizard】>【System Upgrade】 
   ![Magento upgrade](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-sysupgradestart-websoft9.png)
  
2. If your Magento not [Link Marketplace](../magento#link-magento-marketplace), you need to fill in your Access key to link Marketplace
   ![Magento connect Marketplace](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-sysupgradestartkey-websoft9.png)
  
3. Click the upgrade button to start upgrading online
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-sysupgradestarting-websoft9.png)
  
4. If upgrade is very slowly and have error, please refer to [Troubleshooting](#troubleshoot)

More upgrade detail please refer to [Magento Upgrade](https://devdocs.magento.com/guides/v2.3/comp-mgr/bk-compman-upgrade-guide.html)
  
## Troubleshoot{#troubleshoot}

In addition to the Magento issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  
  
**Magento upgrade or install module failed?**

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-upgrade-dependency.png)

If the upgrade have errors, the most likely cause is insufficient memory. On the one hand, you need to ensure that the server memory is not lower than 4G. On the other hand, you need to modify the `.htaccess` file in the Magento root directory.

Make sure `php_value memory_limit` not lower than 2048M

```
    php_value memory_limit 2048M
    php_value max_execution_time 18000
```
  
**When the Magento site is accessed through IP, the server IP is changed and cannot be accessed?**

SSH连接云服务器，重置 `base-url`的值：

```shell
/data/wwwroot/magento/bin/magento setup:store-config:set --base-url=http://URL 或 服务器IP
```  
**Magento 索引报异常？**

**现象描述**：错误信息 One or more indexers are invalid....   
**原因分析**：索引发生了变化
**解决方案**：重新编制索引

*方法1：控制台重置*

1.  在管理员页面的左边控制栏点击“SYSTEM”,在弹出的选项中选择Index Management；
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-cron001.png)

2.  点击图中所示的选项框，选择下拉菜单中的Update by Schedule，然后点击序号4所示的选项框选择Select All，最后单击5所示的Submit即可。

    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-cron002.png)

*方法2：命令行重置*

1. 使用命令行工具 (SSH or Terminal)进入magento安装根目录：cd /data/wwwroot/magento/bin

2. 重新编制索引：php magento indexer:reindex
  
**Cron job 告警？**

若出现 **One or more indexers are invalid. Make sure your Magento cron job is running** 的提示，请执行以下命令:

```
php htdocs\magento\bin\magento indexer:reindex
```

然后回到 Magento 界面，刷新页面即可解决。

#### Login error,need mail authentication？
  
Close Magento_TwoFactorAuth，login by password
  
```shell
# Close Magento_TwoFactorAuth
sudo php /data/wwwroot/magento/bin/magento module:disable Magento_TwoFactorAuth
```
  
**Magento 后台重定向太多，无法访问？**

**现象描述**：错误信息为 ERR_TOO_MANY_REDIRECTS magento admin     
**原因分析**：如果排除 '.htaccess' 文件中的重定向问题，那么最有可能是 URL 导致的
**解决方案**：通过命令行或  **core_config_data** 数据表修改 URL
```shell
cd /data/wwwroot/magento
php bin/magento setup:store-config:set --use-secure=1 --use-secure-admin=1 --base-url-secure="https://www.yourdomain.com/"
php bin/magento cache:flush  #将基础URL更改为https并刷新缓存
```

**无法加载CSS/JS，Magento 页面混乱？**

在网站配置域名或做了 https 配置后，网站可能出现，能访问但页面排版混乱，图片不显示（不能访问请先 **[域名五步设置](../administrator/domain_step)**）。

造成这样的原因，在确定不是配置文件的问题下，可以通过【重新发布】来处理。虽然不会删除数据，但请操作前做好数据备份。步骤如下:

1. 开启维护模式
2. 删除静态文件和一系列缓存文件
3. 更新数据库以及代码编译
4. deploy生成静态文件到pub/static里
5. 更新索引，关闭维护模式，以及清空刷新magento缓存


```shell
cd /data/wwwroot/magento
php bin/magento maintenance:enable
php rm -rf var/di/* && rm -rf var/generation/* && rm -rf var/cache/* && rm -rf var/page_cache/* && rm -rf var/view_preprocessed/* && rm -rf pub/static/* && rm -rf generated/* 
php bin/magento setup:upgrade 
php bin/magento setup:di:compile
php bin/magento setup:static-content:deploy -f
php bin/magento indexer:reindex
php bin/magento cache:clean && bin/magento cache:flush
php bin/magento maintenance:disable 
```

**后台添加商品类别不能正常显示？**

Magento 除了系统给出的商品属性，还允许用户通过后台“STORES”->"Attributes"->"Product"添加额外的商品属性。添加的额外属性的属性值设置不正确就会影响前台的商品展示，出现如图错误。通过以下步骤可以排查此问题：

![magento](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-products-matching-the-selection-websoft9.png)


1. 查看日志/data/wwwroot/magento/var/log/exception.log，看是否是添加的属性引发的异常，本例中查看到“eanl3”属性有异常

![magento](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-log-websoft9.png)

2. 进入后台“STORES”->"Attributes"->"Product"，查看相关属性设置.

![magento](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-product-attribute-websoft9.png)

3. 在属性列表中点击“ean13”，进入设置界面

![magento](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-product-attribute1-websoft9.png)

4. 属性设置

![magento](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-product-attribute2-websoft9.png)

5. 清空浏览器缓存，重新打开网站

## FAQ{#faq}

#### Magento support multi-language?

Yes, you should installed your language package first

#### Why is Magento running so slowly?

Magento is a complex enterprise Ecommerce system with high computing resource requirements

#### Forget backend URL of Magento?
  
```shell
# Show Magento(URL)
magento/bin/magento info:adminuri

# Update Magento(URL)
magento/bin/magento setup:config:set --backend-frontname=[yourAdminUrl] -n
```

#### Why should I link to the Magento Marketplace?

Just link Magento Marketplace, you can use the resources of Marketplace online.

#### Adobe Commerce vs Magento Open Source?

Magento Open Source is the formal name of Adobe Commerce