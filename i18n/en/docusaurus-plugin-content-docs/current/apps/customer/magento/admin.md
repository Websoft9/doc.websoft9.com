---
sidebar_position: 3
slug: /magento/admin
tags:
  - Magento
  - 电子商务
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup/) 相关章节。

## 场景

### 备份

本节提供 Magento 在线备份方案，请提前在云控制台做好必备的快照备份。

1. 登录到 Magento 后台，依次打开：【System】>【System->Backup】，进入Magento的备份设置页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-backup-websoft9.png)

2. 设置备份
   
3. 建议将备份加入到计划任务中

   - 登录 Magento 后台，依次打开：【Stores】>【Configuration】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-bkscheduleset-websoft9.png)

   - 找到：【System】>【Backup Settings】，设置计划任务
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-bkschedulesets-websoft9.png)

### 升级

Magento 可以通过两种方式升级：后台升级界面和 Composer 升级命令。  

下面介绍后台升级界面升级步骤：

1. 以管理身份登录 Magento，依次打开：【System】>【Web Setup Wizard】>【System Upgrade】 
   ![Magento upgrade](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-sysupgradestart-websoft9.png)

2. 如果没有连接 Marketplace，系统会要求你输入 Access key
   ![Magento connect Marketplace](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-sysupgradestartkey-websoft9.png)

3. 点击升级按钮，开始在线升级
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-sysupgradestarting-websoft9.png)

4. 升级过程时间较长且报错，请查看[故障原因](#updateplugin)

更多更新操作请参考官方文档：[Magento Upgrade](https://devdocs.magento.com/guides/v2.3/comp-mgr/bk-compman-upgrade-guide.html)


## 故障排除

除以下列出的 Magento 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。 

#### Magento 在线升级或在线安装插件报错？{#updateerror}

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-upgrade-dependency.png)

如果升级过程若报错，最可能的原因是内存不足，一方面需要保证服务器内存不低于 4G，另一方面需要修改 Magento 根目录下的 `.htaccess` 文件。

其中的 `php_value memory_limit` 不低于 2048M

```
    php_value memory_limit 2048M
    php_value max_execution_time 18000
```

#### IP/域名 变更导致 Magento 无法访问？

SSH连接云服务器，重置 `base-url`的值：

```shell
/data/wwwroot/magento/bin/magento setup:store-config:set --base-url=http://URL 或 服务器IP
```

#### Magento 索引报异常？

**现象描述**：错误信息 One or more indexers are invalid....   
**原因分析**：索引发生了变化
**解决方案**：重新编制索引

##### 方法1：控制台重置

1.  在管理员页面的左边控制栏点击“SYSTEM”,在弹出的选项中选择Index Management；
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-cron001.png)

2.  点击图中所示的选项框，选择下拉菜单中的Update by Schedule，然后点击序号4所示的选项框选择Select All，最后单击5所示的Submit即可。

    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-cron002.png)

##### 方法2：命令行重置

1. 使用命令行工具 (SSH or Terminal)进入magento安装根目录：cd /data/wwwroot/magento/bin

2. 重新编制索引：php magento indexer:reindex

#### Cron job 告警？

若出现 **One or more indexers are invalid. Make sure your Magento cron job is running** 的提示，请执行以下命令:

```
php htdocs\magento\bin\magento indexer:reindex
```

然后回到 Magento 界面，刷新页面即可解决。

#### 邮件未设置，跳过登陆时的邮件验证？

关闭密码邮件**双重认证**，通过密码即可登陆：

```shell
# Close Magento_TwoFactorAuth
sudo php /data/wwwroot/magento/bin/magento module:disable Magento_TwoFactorAuth
```
#### Magento 后台重定向太多，无法访问？

**现象描述**：错误信息为 ERR_TOO_MANY_REDIRECTS magento admin     
**原因分析**：如果排除 '.htaccess' 文件中的重定向问题，那么最有可能是 URL 导致的
**解决方案**：通过命令行或  **core_config_data** 数据表修改 URL
```shell
cd /data/wwwroot/magento
php bin/magento setup:store-config:set --use-secure=1 --use-secure-admin=1 --base-url-secure="https://www.yourdomain.com/"
php bin/magento cache:flush  #将基础URL更改为https并刷新缓存
```

#### 无法加载CSS/JS，Magento 页面混乱？

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

#### 后台添加商品类别不能正常显示？

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

## 问题解答

#### Magento 支持多语言吗？

支持多语言（包含中文），需要上传语言包才能设置语言

#### Magento 为什么运行这么慢？

Magento 是一个复杂的企业级电商系统，对计算资源要求较高

#### 找不到 Magento 后台登陆地址？

进入linux系统，通过命令一下命令查看

```shell
# Show Magento(URL)
/data/wwwroot/magento/bin/magento info:adminuri

# Update Magento(URL)
sudo /data/wwwroot/magento/bin/magento setup:config:set --backend-frontname=[yourAdminUrl] -n
```

#### 为什么要连接 Magento Marketplace？

只有连接 [Magento Marketplace](../magento#marketplace)，才可以使用其资源。

#### 使用外部 RDS 作为 Magento 的数据库？

可以，修改 Magento [配置文件](../magento#path) 中对应的参数

#### Magento 能在 Windows 上部署吗？

可以，但是我们推荐在运行 Magento 效率更高的 Linux 服务器上运行

#### Adobe Commerce 与 Magento 关系？

Magento Open Source 被 Adobe 收购后，Adobe 将其商业版本更名为 Adobe Commerce。