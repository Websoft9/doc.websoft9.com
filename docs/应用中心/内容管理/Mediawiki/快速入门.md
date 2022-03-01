---
sidebar_position: 1
slug: /ghost
tags:
  - Ghost
  - CMS
  - 建站系统
  - 博客系统
---

# 快速入门

[MediaWiki](https://www.mediawiki.org) 是全球著名的开源wiki程序，采用 PHP+MySQL 开发。适合用于构建百科、知识库、在线文档、个人笔记等应用。超过数万个站点使用，大名鼎鼎的“维基百科”网站是基于这个软件而构建。MediaWiki的开发得到维基媒体基金会的支持。MediaWiki的最大作用在于对知识的归档，可用于构建企业/个人知识库，WIKI系统的思想是经过越多的人的编辑，结果就越趋于正确（完美）。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mediawiki/MediaWiki_UI.png)

## 演示

MediaWiki 官网提供了试用环境，您可以直接试用

* 演示地址：https://www.mediawiki.org/wiki/MediaWiki

> 免责说明：此处仅提供MediaWiki官方的演示，不保证与 Websoft9 部署包功能完全一致，若演示过程中若需要填写个人资料、获取Cookie等，这些都是官方行为，由此产生的安全问题与我司无关。若您在演示中进行了付费，即表明您愿意接受官方提供的付费服务，由此可能存在的商业纠纷与我司无关。

在云服务器上部署 MediaWiki 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 MediaWiki，请先到 **域名控制台** 完成一个域名解析


## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

### Ghost

在初始化安装的时候由用户自行设置

### MySQL

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器指定文件中（ */credentials/password.txt* ）
   ![运行cat命令](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

  建议通过云控制台的命令终端，运行`cat /credentials/password.txt` 获取数据库密码（参上图）

  **注意**：旧版本 Ghost 上，不存在 password.txt 文件，其数据库密码是 `123456`。请在初始化安装之前务必将数据库密码修改成复杂密码，这样有助于提高数据库的安全性。

> 需要登录MySQL，请参考 [MySQL可视化管理](#MySQL-数据管理)

## MediaWiki 安装向导

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://Internet IP*, 就进入引导首页
2. 根据系统提示，点击“…Installation”进入安装界面，选择语言 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mediawiki/mediawiki-install001-websoft9.png)
3. 填写你的数据库配置信息([不知道账号密码？](/zh/stack-accounts.html#mysql))，保存并继续; 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mediawiki/mediawiki-install002-websoft9.png)
4. 选择数据库引擎和字符集设置，字符集建议选用UFT-8 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mediawiki/mediawiki-install003-websoft9.png)
5. 设置后台账号信息，请务必设置好并牢记之。进入下一步 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mediawiki/mediawiki-install004-websoft9.png)
6. 跟随安装提示直到完成，过程中尽量选择默认设置，勾选安装所有模块
7. 配置完成后会生成 LocalSettings.php 文件，根据提示下载。 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mediawiki/mediawiki-install005-websoft9.png)
8. 将 `LocalSettings.php` 文件上传到服务器 MediaWiki 根目录
9. 系统完成最后一步安装，建议进入MediaWiki后台（以管理身份登录即进入后台），体验完整功能 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mediawiki/mediawiki-homepage-websoft9.png)

> 需要了解更多MediaWiki的使用，请参考官方文档：[MediaWiki FAQ](https://www.mediawiki.org/wiki/Sysadmin_hub/zh)


## 常用操作

### 配置

官方提供了很多配置方案，参考：[Tutorials](https://ghost.org/tutorials/) 和 [FAQ](https://ghost.org/faq/)

### 域名绑定

绑定域名的前置条件是：已经完成域名解析（登录域名控制台，增加一个A记录指向服务器公网IP）  

完成域名解析后，从服务器安全和后续维护考量，需要完成**域名绑定**：

MediaWiki 域名绑定操作步骤：

1. 使用 SFTP 工具登录云服务器
2. 修改 [虚拟机主机配置文件](/维护参考.md#apache)，将其中的域名相关的值
   ```text
   #### MediaWiki(LAMP) bind domain #### 

     <VirtualHost *:80>
     ServerName  www.mydomain.com # 修改成您的实际域名
     DocumentRoot "/data/wwwroot/mediawiki"
     ...
     
   #### MediaWiki(LNMP) bind domain #### 

     server {
      listen 80;
      server_name mediawiki.example.com; # 修改成您的实际域名
     ...

   ```
3. 保存配置文件，[重启服务](/维护参考.md#apache-1)

### SSL/HTTPS

网站完成域名绑定且可以通过HTTP访问之后，方可设置HTTPS。

MediaWiki预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。

> 除了虚拟主机配置文件之外，HTTPS设置无需修改Nginx任何文件

#### 快速参考

如果你想使用免费证书，只需在服务器中运行一条命令`certbot`就可以启动证书部署

如果你已经申请了商业证书，只需三个步骤，即可完成HTTPS配置

#### MediaWiki(LAMP)

MediaWiki(LAMP) 即运行环境采用 **Apache** 作为 Web Server  

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件： */etc/httpd/conf.d/vhost.conf* 
3. 将如下的 **HTTPS 配置段模板**  `<VirtualHost *:443>--</VirtualHost>` 插入到`vhost.conf` 文件中
   ``` text
   #-----HTTPS template start------------
   <VirtualHost *:443>
    ServerName  mediawiki.yourdomain.com
    DocumentRoot "/data/wwwroot/mediawiki"
    #ErrorLog "logs/mediawiki.yourdomain.com-error_log"
    #CustomLog "logs/mediawiki.yourdomain.com-access_log" common
    <Directory "/data/wwwroot/mediawiki">
    Options Indexes FollowSymlinks
    AllowOverride All
    Require all granted
    </Directory>
    SSLEngine on
    SSLCertificateFile  /data/cert/mediawiki.yourdomain.com.crt
    SSLCertificateKeyFile  /data/cert/mediawiki.yourdomain.com.key
    </VirtualHost>
   #-----HTTPS template end------------
   ```
4. 修改 ServerName, SSLCertificateFile, SSLCertificateKeyFile等参数的值
5. 保存， [重启 Apache 服务](/维护参考.md#apache-1)

#### MediaWiki(LEMP)

MediaWiki(LEMP) 即运行环境采用 **Nginx** 作为 Web Server  

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件：*/etc/nginx/conf.d/default.conf* ，插入**HTTPS 配置段** 到 MediaWiki 的 *server{ }* 中
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
4. 修改 ssl_certificate, ssl_certificate_key 的值
5. 保存，[重启 Nginx 服务](/维护参考.md#nginx-1)

#### 专题指南

若参考上面的**简易步骤**仍无法成功设置HTTPS访问，请阅读由Websoft9提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

HTTPS专题指南方案包括：HTTPS前置条件、HTTPS 配置段模板、注意事项、详细步骤以及故障诊断等具体方案。

### SMTP

大量用户实践反馈，使用**第三方 SMTP 服务发送邮件**是一种最稳定可靠的方式。  

请勿在服务器上安装sendmail等邮件系统，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，非常不稳定，且不易维护、诊断故障很困难。

下面以**网易邮箱**为例，提供设置 MediaWiki 发邮件的步骤：

1. 在网易邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.163.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9@163.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过163邮箱后台设置去获取的授权码
   ```
2. 编辑网站根目录下的 `LocalSettings.php` 配置文件
3. 找到变量 $wgSMTP，并设置它
   ```
    $wgSMTP = array(
    'host'     => "smtp.163.com", 
    'IDHost'   => "example.com",      // 邮箱域名，可选.如果不设置的话会设置成 $wgServer 的值.
    'port'     => 465,                 
    'auth'     => true,               
    'username' => "websoft9@163.com",     
    'password' => "#wwBJ8"       
    );
   ```
4. 找到变量 $ wgEnableEmail，设置其值为 true
   ```
   $ wgEnableEmail = true
   ```
5. 查找以下变量，将其值设置为发件邮箱
   ```
   $wgEmergencyContact = "websoft9@163.com";
   $wgPasswordSender = "websoft9@163.com";
   ```
4. 保存设置
5. 重启 [PHP-FPM 服务](/zh/admin-services.html#php-fpm)后生效
6. 测试是否可以发邮件

更多邮箱设置（QQ邮箱，阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)

### MediaWiki 配置设置

主要通过修改 LocalSettings.php 文件来对 MediaWiki 进行设置，而 LocalSettings.php 文件

参考官方文档: [Configuration settings](https://www.mediawiki.org/wiki/Manual:Configuration_settings/zh)

### MediaWiki 安装扩展

参考官方文档：[Manual:Extensions](https://www.mediawiki.org/wiki/Manual:Extensions/zh)

### MediaWiki 创建或编辑页面

参考官方文档：[Help:Starting_a_new_page](https://www.mediawiki.org/wiki/Help:Starting_a_new_page/zh)

### MediaWiki 可视化编辑器

参考官方文档：[Help:Starting_a_new_page](https://www.mediawiki.org/wiki/Help:VisualEditor/User_guide/zh)

### MediaWiki 定制界面

定制界面包括：修改 Logo, 设置导航栏，修改 CSS 等  

参考官方文档：[Help:FAQ:定制界面](https://www.mediawiki.org/wiki/Manual:FAQ/zh#定制界面)

### MediaWiki 允许文件上传

Mediawiki 默认并不可以上传文件，需要启动文件上传功能  

参考官方文档：[Help:FAQ:启用文件上传](https://www.mediawiki.org/wiki/Manual:FAQ/zh#如何启用文件上传?)

### MediaWiki 语言设置

参考官方文档：[Help:FAQ:语言设置](https://www.mediawiki.org/wiki/Manual:FAQ/zh#我如何更改界面语言？)

### MediaWiki 设置主页

参考官方文档：[Help:FAQ:设置主页](https://www.mediawiki.org/wiki/Manual:FAQ/zh#如何指定首页?)

### MediaWiki 使用 Composer

本预装包默认已经安装 Composer，详细使用  

参考官方文档：[Help:Composer](https://www.mediawiki.org/wiki/Composer/zh)

### MySQL 数据管理

MediaWiki 预装包中内置 MySQL 及可视化数据库管理工具 `phpMyadmin` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组80端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP/phpmyadmin*，进入phpMyAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)
3. 输入数据库用户名和密码([不知道密码？](#账号密码))
4. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

> 阅读Websoft9提供的 [《MySQL教程》](https://support.websoft9.com/docs/mysql/zh/admin-phpmyadmin.html) ，掌握更多的MySQL实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等

## 异常处理

#### 浏览器打开IP地址，无法访问 MediaWiki（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 MediaWiki 数据？

是MySQL

#### 是否可以采用云厂商提供的 RDS 来存储 MediaWiki 数据？

可以

#### 是否可以重装 MediaWiki

本地浏览器访问： *http://服务公网IP/mw-config/index.php?page=Restart&lastPage=Install* ，开始重装

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mediawiki/Mediawiki-reinstall-websoft9.png)
