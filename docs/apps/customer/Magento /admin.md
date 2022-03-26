---
sidebar_position: 3
slug: /magento/admin
tags:
  - Magento
  - 电子商务
---

# 维护指南

## 场景

### 备份与恢复

本节提供Magento在线备份方案，请提前在云控制台做好必备的快照备份。

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

2. 如果没有[连接 Marketplace](/zh/stack-installation.html#连接-magento-marketplace)，系统会要求你输入 Access key
   ![Magento connect Marketplace](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-sysupgradestartkey-websoft9.png)

3. 点击升级按钮，开始在线升级
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-sysupgradestarting-websoft9.png)

4. 升级过程时间较长且报错，请查看[故障原因](#updateplugin)

更多更新操作请参考官方文档：[Magento Upgrade](https://devdocs.magento.com/guides/v2.3/comp-mgr/bk-compman-upgrade-guide.html)


## 故障速查

除以下列出的 Magento 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。 

#### Magento 在线升级或在线安装插件报错？{#updateplugin}

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-upgrade-dependency.png)

如果升级过程若报错，最可能的原因是内存不足，一方面需要保证服务器内存不低于 4G，另一方面需要修改 Magento 根目录下的 `.htaccess` 文件。

其中的 `php_value memory_limit` 不低于 2048M

```
    php_value memory_limit 2048M
    php_value max_execution_time 18000
```

#### Magento 站点通过IP访问的情况下， 服务器IP发生变更导致无法访问？

通过SSH连接云服务器，运行下面的CLI命令即可恢复
```shell
    /data/wwwroot/magento/bin/magento setup:store-config:set --base-url=http://服务器公网IP # 修改成您的当前服务器IP
```
 > 通过域名访问的情况，请参照 **[域名五步设置](../dns#domain)**

#### 修改了数据库密码 Magento 不能访问？

若已完成 Magento 安装向导，再通过 phpMyAdmin 修改数据库密码，此候 Magento 就会连不上数据库

需要修改配置文件（/data/wwwroot/magento/app/etc/env.php）对应的数据库 password 参数即可。

#### Magento 出现“One or more indexers are invalid....”如何解决？

##### 方法1
1.  在管理员页面的左边控制栏点击“SYSTEM”,在弹出的选项中选择Index Management；
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-cron001.png)
2.  点击图中所示的选项框，选择下拉菜单中的Update by Schedule，然后点击序号4所示的选项框选择Select All，最后单击5所示的Submit即可。
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-cron002.png)

##### 方法2
1. 使用命令行工具 (SSH or Terminal)进入magento安装根目录：cd /data/wwwroot/magento/bin
2. 重新编制索引：php magento indexer:reindex

#### Apache httpd 服务无法启动？

请通过分析日志文件定位原因： */var/log/httpd*

#### 登陆时需要邮件验证，无法收到邮件怎么办？

关闭密码邮件双重认证，通过密码即可登陆
```shell
# Close Magento_TwoFactorAuth
sudo php /data/wwwroot/magento/bin/magento module:disable Magento_TwoFactorAuth
```

#### 网站重定向错误？

分析网站根目录下的 `.htaccess` 文件，看看有没有死循环规则

#### Magento 后台重定向太多，无法访问（ERR_TOO_MANY_REDIRECTS magento admin）

在网站配置域名或做了 https 配置后，网站可能出现后台重定向太多无法访问，在确定不是 '.htaccess' 配置文件的问题下，请检查如下几个 url ，将其改成你的域名，同时修改2个选项为 true。
这些信息保存在 Magento 的配置数据表 core_config_data 中，可以通过修改数据表来修改，也可以通过下列 cli 方式处理。

```shell
cd /data/wwwroot/magento
php bin/magento setup:store-config:set --use-secure=1 --use-secure-admin=1 --base-url-secure="https://www.yourdomain.com/"
php bin/magento cache:flush  #将基础URL更改为https并刷新缓存
```

#### Magento 无法加载CSS/js资源，页面排版混乱

在网站配置域名或做了 https 配置后，网站可能出现，能访问但页面排版混乱，图片不显示（不能访问请先 **[域名五步设置](../dns#domain)**）。

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


#### We can't find products matching the selection，添加类别和商品但不能正常显示

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


#### 数据库服务无法启动

数据库服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh
```


## 问题解答

#### Magento 支持多语言吗？

支持多语言（包含中文），需要上传语言包才能设置语言

#### Magento 为什么运行这么慢？

Magento 是一个复杂的企业级电商系统，对计算资源要求较高

#### 忘记了Magento后台登陆地址怎么办？

进入linux系统，通过命令一下命令查看

```shell
# Show Magento(URL)
/data/wwwroot/magento/bin/magento info:adminuri

# Update Magento(URL)
sudo /data/wwwroot/magento/bin/magento setup:config:set --backend-frontname=[yourAdminUrl] -n
```

#### 为什么要连接 Magento Marketplace？

只有连接 Magento Marketplace，才可以使用其资源。连接教程[参考](../magento#marketplace)

#### Magento(LAMP)，Magento(LNMP)等商品括号中的 LAMP,LNMP 是什么意思？

LAMP 和 LNMP 代表支持 Magento 运行所对应的基础环境中的 Web 服务器是 Apache 或 Nginx，具体参考[Apache](../apache) 和 [Nginx](../nginx) 

#### 是否可以使用云平台的 RDS 作为 Magento 的数据库？

可以，修改 Magento 根目录下的配置文件 `config.php` 即可

#### Magento能在Windows服务器上运行吗？

可以，但是我们推荐在运行 Magento 效率更高的 Linux 服务器上运行

#### Magento数据库连接配置信息在哪里？

数据库配置信息在Magento安装目录下的 *LocalSettings.php* 中，[查阅安装目录路径](../magento#path)

#### 如果没有域名是否可以部署 Magento？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin，访问地址：http://服务器公网IP/phpmyadmin

#### 如何禁止phpMyAdmin访问？

连接服务器，编辑 phpMyAdmin 配置文件，将其中的 Require all granted 更改为 Require ip 192.160.1.0，然后重启 Apache 服务

#### 是否可以修改 Magento 的源码路径？

可以，通过修改 [虚拟主机配置文件](../apache#virtualHost)中相关参数
