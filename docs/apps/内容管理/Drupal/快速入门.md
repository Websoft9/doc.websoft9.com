---
sidebar_position: 1
slug: /drupal
tags:
  - Drupal
  - CMS
  - 建站系统
---

# 快速入门

[Drupal](https://www.drupal.org) 是全球三大开源内容管理系统之一，约3%的网站使用。Drupal也是一个开发框架，逻辑性强、一块块积木，搭起来以后使页面层层分明，它的内核中的有功能强大的PHP类库、函数库和API，能够通过二次化开发来构建复杂多用的企业级应用。Drupal有良好的商业生态，众多高端优质客户使用进一步推动了开源社区的发展。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-gui-websoft9.png)

## 演示

Drupal 官网提供了试用环境，您可以直接试用

* 演示地址：https://www.drupal.org/try-drupal

> 免责说明：此处仅提供 Drupal 官方的演示，不保证与 Websoft9 部署包功能完全一致，若演示过程中若需要填写个人资料、获取Cookie等，这些都是官方行为，由此产生的安全问题与我司无关。若您在演示中进行了付费，即表明您愿意接受官方提供的付费服务，由此可能存在的商业纠纷与我司无关。

在云服务器上部署 Drupal 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 Drupal，请先到 **域名控制台** 完成一个域名解析

## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

### Drupal

在初始化安装的时候由用户自行设置

### MySQL

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器指定文件中（ */credentials/password.txt* ）
   ![运行cat命令](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

  建议通过云控制台的命令终端，运行`cat /credentials/password.txt` 获取数据库密码（参上图）

  **注意**：旧版本 Drupal 上，不存在 password.txt 文件，其数据库密码是 `123456`。请在初始化安装之前务必将数据库密码修改成复杂密码，这样有助于提高数据库的安全性。

> 需要登录MySQL，请参考 [MySQL可视化管理](#MySQL-数据管理)

## Drupal 安装向导

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入引导页

2.  选择一门语言，进入下一步
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-install001-websoft9.png)

3.  选择一种安装方式，进入下一步
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-install002-websoft9.png)

4.  填写您的数据库参数（[查看数据库账号密码](/zh/stack-accounts.md#mysql)），保存并继续;
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-install003-websoft9.png)

5.  分别完成网站安装和翻译安装
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-install004-websoft9.png)

6.  设置网站信息。站点维护账号及后台账号，请务必设置好并牢记之。进入下一步
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-install005-websoft9.png)

7.  系统完成最后一步安装

8.  进入Drupal后台，体验完整功能
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-backend-websoft9.png)

> 需要了解更多 Drupal 的使用，请参考官方文档：[Drupal Community Guides](https://www.drupal.org/documentation)

## Drupal 入门向导

Coming soon...

## 常用操作

### 域名绑定

绑定域名的前置条件是：已经完成域名解析（登录域名控制台，增加一个A记录指向服务器公网IP）  

完成域名解析后，从服务器安全和后续维护考量，需要完成**域名绑定**：

Drupal 域名绑定操作步骤：

1. 使用 SFTP 工具登录云服务器
2. 修改 [虚拟机主机配置文件](/维护参考.md#apache)，将其中的域名相关的值
   ```text
   #### Drupal(LAMP) bind domain #### 

     <VirtualHost *:80>
     ServerName  www.mydomain.com # 修改成您的实际域名
     DocumentRoot "/data/wwwroot/Drupal"
     ...
     
   #### Drupal(LNMP) bind domain #### 

     server {
      listen 80;
      server_name Drupal.example.com; # 修改成您的实际域名
     ...

   ```
3. 保存配置文件，[重启服务](/维护参考.md#apache-1)

### Drupal 更换域名

如果 Drupal 需要更换域名，具体操作如下：

1. 完成新的域名解析和域名绑定
2. 检查 [Drupal 配置文件](/zh/stack-components.html#drupal)中的域名值
3. 检查 Drupal 根目录下 `.htaccess` 文件中域名值
4. [重启 PHP-FPM 服务](/zh/admin-services.html#php-fpm)后生效

### SSL/HTTPS

网站完成域名绑定且可以通过HTTP访问之后，方可设置HTTPS。

Drupal 预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。

> 除了虚拟主机配置文件之外，HTTPS设置无需修改Nginx任何文件

#### 快速参考

如果你想使用免费证书，只需在服务器中运行一条命令`certbot`就可以启动证书部署

如果你已经申请了商业证书，只需三个步骤，即可完成HTTPS配置

#### Drupal(LAMP)

Drupal(LAMP) 即运行环境采用 **Apache** 作为 Web Server  

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件： */etc/httpd/conf.d/vhost.conf* 
3. 将如下的 **HTTPS 配置段模板**  `<VirtualHost *:443>--</VirtualHost>` 插入到`vhost.conf` 文件中
   ``` text
   #-----HTTPS template start------------
   <VirtualHost *:443>
    ServerName  Drupal.yourdomain.com
    DocumentRoot "/data/wwwroot/Drupal"
    #ErrorLog "logs/Drupal.yourdomain.com-error_log"
    #CustomLog "logs/Drupal.yourdomain.com-access_log" common
    <Directory "/data/wwwroot/Drupal">
    Options Indexes FollowSymlinks
    AllowOverride All
    Require all granted
    </Directory>
    SSLEngine on
    SSLCertificateFile  /data/cert/Drupal.yourdomain.com.crt
    SSLCertificateKeyFile  /data/cert/Drupal.yourdomain.com.key
    </VirtualHost>
   #-----HTTPS template end------------
   ```
4. 修改 ServerName, SSLCertificateFile, SSLCertificateKeyFile等参数的值
5. 保存， [重启 Apache 服务](/维护参考.md#apache-1)

#### Drupal(LEMP)

Drupal(LEMP) 即运行环境采用 **Nginx** 作为 Web Server  

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件：*/etc/nginx/conf.d/default.conf* ，插入**HTTPS 配置段** 到 Drupal 的 *server{ }* 中
 ``` text
   #-----HTTPS template start------------
   listen 443 ssl; 
   ssl_certificate /data/cert/xxx.crt;
   ssl_certificate_key /data/cert/xxx.key;
   ssl_session_timeout 5m;
   ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
   ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE;
   ssl_prefer_server_ciphers on;
   #-----HTTPS template end------------
   ```
3. 修改 ssl_certificate, ssl_certificate_key 的值
4. 保存，[重启 Nginx 服务](/维护参考.md#nginx-1)

#### 专题指南

若参考上面的**简易步骤**仍无法成功设置HTTPS访问，请阅读由Websoft9提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

HTTPS专题指南方案包括：HTTPS前置条件、HTTPS 配置段模板、注意事项、详细步骤以及故障诊断等具体方案。

### SMTP

大量用户实践反馈，使用**第三方 SMTP 服务发送邮件**是一种最稳定可靠的方式。  

请勿在服务器上安装sendmail等邮件系统，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，非常不稳定，且不易维护、诊断故障很困难。

下面以**网易邮箱**为例，提供设置 Drupal 发邮件的步骤：

1. 在网易邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.163.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9@163.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过163邮箱后台设置去获取的授权码
   ```
2. 获取 [SMTP Authentication Support](https://www.drupal.org/project/smtp) 下载链接（Drupal 默认没有安装 SMTP 模块），在线安装
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-installsmtp-websoft9.png)

3. 打开：【管理】>【扩展】，找到【SMTP Authentication Support】，点击【Install】完成最终安装步骤
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-installsmtp002-websoft9.png)

3. 打开：【管理】>【配置】，找到【SMTP Authentication Support】，配置它
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-setsmtp-websoft9.png)

5. 填写准确的 SMTP 设置项信息
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-smtp-4-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-smtp-5-websoft9.png)

    * 发送模式选择“SMTP”，加密方式选择“SSL/TLS”;
    * 输入发送方邮箱地址；
    * 认证方式选择“登录”，并勾选“需要认证”选项；
    * 输入SMTP服务器地址和SMTP服务器的端口号；
    * 输入和发件人邮箱一致的邮箱地址；
    * 输入该邮箱地址的SMTP服务的授权码或密码；
    * 存储凭据；

3. 设置完成后，勾选【启用调试】，将发出测试邮件
     
> 更多邮箱设置（QQ邮箱，阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)

### Drupal 多语言

Drupal 支持多语言，下面是安装并设置多语言的主要步骤：

1. 登录 Drupal，在后台 【管理】>【配置】>【地区和语言】中安装语言
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-addlanguage-websoft9.png)

2. 安装新语言后，根据实际需要，设置默认语言

### Drupal 安装扩展

Drupal 提供的 [Drupal Modules](https://www.drupal.org/project/project_module)包含大量的扩展，下面介绍如何安装它们

1. 打开 [Drupal Modules](https://www.drupal.org/project/project_module)网站，搜寻所需的扩展
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-searchformodule-websoft9.png)

2. 获取扩展的下载地址
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-dlmodule-websoft9.png)

3. 登录 Drupal 后台，打开安装扩展的界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-extend-websoft9.png)

4. 通过输入下载地址，在线安装扩展
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-installsmtp-websoft9.png)

5. 安装完成
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-moduleinstalled-websoft9.png)

6. 最后，需要到模块管理中启用刚安装的插件
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-enablemodule-websoft9.png)

### Drupal 安装主题

Drupal 提供的 [Drupal Themes](https://www.drupal.org/project/project_theme) 包含大量的主题，下面介绍如何安装它们

1. 打开 [Drupal Themes](https://www.drupal.org/project/project_theme) 网站，搜寻所需的主题
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-searchthemes-websoft9.png)

2. 获取主题的下载地址
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-themesurl-websoft9.png)

3. 打开 【扩展管理】>【安装扩展】，输入下载地址，开始安装
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-installsmtp-websoft9.png)

4. 安装后，打开【外观】，找到已经在线安装的主题，启用它
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-themeenable-websoft9.png)

> 有些模板提供商，提供的模板压缩包中包含 Drupal 内核文件，这种情况下 **安装模板=安装Drupal**

### Drupal 重置管理员密码

如果忘记了管理员密码，可以参考 [此处](https://www.drupal.org/node/44164) 重置密码

### MySQL 数据管理

Drupal 预装包中内置 MySQL 及可视化数据库管理工具 `phpMyadmin` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组80端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP/phpmyadmin*，进入phpMyAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)
3. 输入数据库用户名和密码([不知道密码？](#账号密码))
4. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

> 阅读Websoft9提供的 [《MySQL教程》](https://support.websoft9.com/docs/mysql/zh/admin-phpmyadmin.html) ，掌握更多的MySQL实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等

## 异常处理

#### 安装后有错误提示？

参考本文档之 [故障处理](/zh/else-troubleshooting.md) 章节

#### 浏览器打开IP地址，无法访问 Drupal（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 Drupal 数据？

是MySQL

#### 是否可以采用云厂商提供的 RDS 来存储 Drupal 数据？

可以

