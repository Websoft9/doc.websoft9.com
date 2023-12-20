---
sidebar_position: 2
slug: /wamp/admin
tags:
  - WAMP
  - PHP
  - Apache
  - Windows
---


# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup) 相关章节。

## 场景

### 设置 SSL/HTTPS

网站完成域名绑定且可以通过 HTTP 访问之后，方可设置HTTPS。WampServer 默认安装 OpenSSL 模块，并完成预配置。

1. 将申请的证书、秘钥文件上传到 *C:\wwwroot\cert * 目录

3. 打开 [bitnami-apps-vhosts.conf（虚拟主机配置配置文件）](../wamp#apache)

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/wamp-addmorevhostconfig-websoft9.png)

3. 将下面的 HTTPS 配置文件模板，增加到 httpd-vhosts.conf 文件中(不能删除原有内容)

    ```
    <VirtualHost *:443>
    ServerName  www.mydomain.com
    DocumentRoot "C:\wwwroot\mysite2"
    <Directory "C:\wwwroot\mysite2">
    Options Indexes FollowSymlinks
    AllowOverride All
    Require all granted
    </Directory>
    SSLEngine on
    SSLCertificateFile  "C:\wwwroot\cert\cert.pem"
    SSLCertificateKeyFile  "C:\wwwroot\cert\key.pem"
    SSLCertificateChainFile  "C:\wwwroot\cert\chain.pem"
    </VirtualHost>
    ```

4. 修改其中的 ServerName, DocumentRoot, ErrorLog, CusomLog, Directory等 [VirtualHost](../apache#virtualhost)的值，修改完成后保存

5. 重启 Apache 服务 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/wamp-bitnami001-websoft9.png)

### 重置 MySQL 密码

重置 MySQL 密码的分为三个步骤：

##### 将 MySQL 更改为临时免密模式

1. 远程连接到服务器，打开 [MySQL 配置文件](../wamp#mysql)，在 [mysqld] 配置项中增加一行 `skip-grant-tables`，保存
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/wamp-addconfigtomysqld-websoft9.png)

2. 重启 MySQL 服务
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/wamp-managerservice-websoft9.png)

##### 修改密码 

- 进入到 MySQL 下的 bin 目录，按住键盘 `Shift`键的同时点击鼠标右键，
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/wamp-opencmdinbin-websoft9.png)

- 进入命令窗口，依次运行下列命令：
   ```
    mysql -uroot
    use mysql;
    update user set authentication_string=password("12345678") where user="root";
    flush privileges;
    exit
   ```

##### 将 MySQL 恢复为正常模式

1. 打开 [MySQL 配置文件](../wamp#mysql)，在 [mysqld] 配置项中删除 `skip-grant-tables` 这一行
2. 再次重启 MySQL 服务，此时密码已被重置为 `12345678`

### 更新 PHP 版本

以从 PHP7.0.29 升级到 PHP7.0.31 为例：

1. 左击右下角任务栏的 WAMP 图标，停止所有服务

2. 到 [PHP 官网](https://windows.php.net/download/)下载所需的版本 
   > 注意：下载的文件为压缩包文件，且必须选择 **Thread Safe** 版本。
   	![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/wampserver-phpupdate-1-websoft9.png)

3. 备份原来的 C:\websoft9\wampstack\php 文件夹，再将该文件夹下所有文件删除，将新版 PHP 文件解压到这个文件夹里

4. 将新版 php 文件夹下的 php.ini-production 文件重命名为 php.ini

5. 重启服务


### 迁移网站

迁移网站就是将**网站数据**移动到新的位置，然后通过配置，保证移动后可正常访问。

迁移是需要谨慎对待的操作，迁移之前需要清楚的明白如下要点：

- 被移动的网站数据对象：网站源码文件和数据库数据文件  
- 目的地位置：服务器目录之间转移（本地）和转移到外部服务器（外部）

被迁移对象和目的地位置的组合，形成了多种多样的迁移场景。下面详细说明最常见的迁移场景：

#### 迁移网站源码（本地）

以将原目录 *c:\wwwroot* 下的 **mysite1** 迁移到 *d:\www* 目录下为例，具体步骤如下：

1. 使用 **远程桌面** 连接服务器，停止 [Apache 服务](#apache)
2. 将 ***mysite1*** 文件夹整体拷贝到目标位置 *d:\www*
3. 修改 [虚拟主机配置文件](../wamp#apache) 中 mysite1 这个网站对应的 VirtualHost 配置段 DocumentRoot, Directory 项的值，并保存它

   原地址：c:\wwwroot\mysite1  
   目标地址：d:\www\mysite1

4. 重启 [Apache 服务](#apache)
5. 测试迁移后的结果，成功后可以删除原来的 *mysite1* 文件夹

#### 迁移数据库文件（本地）

没有特殊情况，我们不建议迁移数据库文件到服务器上另外一个目录，毕竟主流的云厂商磁盘均可扩容。

1. 停止 MySQL 服务

2. 将 *C:/websoft9/wampstack/mysql/data* 下所有文件拷贝到新目录，例如：D:\data

3. 修改 [数据库配置文件](../mysql#path) 文件中数据存放的路径，范例参考：
	~~~
    datadir="C:/websoft9/wampstack/mysql/data"
    log-error="C:/websoft9/wampstack/mysql/data/mysqld.log"
        
    修改为：
    
    datadir="D:\data"
    log-error="D:\data\mysqld.log"
    ~~~

 4. 重启 MySQL 服务

#### 迁移到外部服务器

网站从一台服务器（原服务器）迁移到另外一台服务器（目的服务器）是一个系统工程，基本步骤如下：

1. 通过云控制台，在目的服务器上部署参数一致的 WAMP 镜像。

2. 将原服务器上的网站源文件**转移到**目的服务器。

3. 通过 phpMyAdmin **导出**原服务器上的数据库，然后在目的服务器上**导入**数据库。

4. 把原服务器上的 [虚拟主机配置文件](#apache) 配置文件内容，完整拷贝到目的服务器的 [虚拟主机配置文件](#apache) 中，保存之。

5. 重启 Apache 服务。

5. 解析域名到目的服务器，等待域名解析生效。

5. 通过域名访问网站，测试可用性。

6. 正式发布。

如果一台服务器上有多个网站需要迁移，建议逐个迁移

## 故障排除

除以下列出的 WAMP 故障问题之外， [通用故障处理](../troubleshoot) 、 [Apache 故障排除](../apache#troubleshoot) 专题章节提供了更多的故障方案。 

#### 修改[虚拟主机](../wamp#path)后，Apache 无法启动？

一般是 VirtualHost 中虚拟主机的目录位置不正确导致

## 常见问题

#### 默认字符集是什么？

UTF-8

#### Apache 工作模式是哪个？

prefork

#### Apache 虚拟主机配置文件是什么？

虚拟主机配置文件是 Apache 用于管理多个网站的**配置段集合**，有多少个网站就有多少个配置段。

#### WAMP 是否支持部署多个网站？

支持。每增加一个网站，只需在 [Apache 虚拟主机配置文件](../wamp#apache)中增加对应的 VirtualHost 即可。

#### 如何将 phpMyAdmin 限制为本地访问？

参考：[Apache Require](../apache#require)

#### 上传的文件是否需修改拥有者权限？

不需要，WAMP 会自动修正

#### WAMP 默认安装了哪些模块？ 

Apache, PHP 模块都可以通过 WAMP 可视化界面查看


