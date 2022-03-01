---
sidebar_position: 1
slug: /discuz
tags:
  - Discuz
  - CMS
  - 建站系统
  - 博客系统
---

# 快速入门

[Discuz](https://www.discuz.net)是开源的论坛社区系统，诞生于2001年6月，目前已经演进为 [DiscuzQ](https://discuz.com/)，它拥有完全开源、提供丰富接口、前后端分离、轻量化、数据独立可控、敏捷上云、快速变现七大能力。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuzq-guiweb-websoft9.png)


## 演示

通过官网 [Discuz](https://www.discuz.net)和[DiscuzQ](https://discuz.com/) 查看其界面。官方看起来“平淡无奇”，但是实际上户可以通过“应用中心”进行丰富的外观的定制、功能的扩展。

> 免责说明：此处仅提供 discuz 官方的演示，不保证与 Websoft9 部署包功能完全一致，若演示过程中若需要填写个人资料、获取Cookie等，这些都是官方行为，由此产生的安全问题与我司无关。若您在演示中进行了付费，即表明您愿意接受官方提供的付费服务，由此可能存在的商业纠纷与我司无关。

在云服务器上部署 Discuz 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 Discuz，请先到 **域名控制台** 完成一个域名解析

## 账号密码

使用Discuz，可能会用到的几组账号密码如下：

### Discuz

在初始化安装的时候由用户自行设置

### MySQL

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器指定文件中   

  - Linux 系统  

     **密码存储路径**：*/credentials/password.txt*    
     **获取方式**： 建议通过云控制台的命令终端，运行下图**红框**所示命令，获取数据库密码   
     ![运行cat命令](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

  - Windows 系统  

     **密码存储路径**：*C:/credentials/password.txt*     
     **获取方式**： 远程桌面到服务器，打开此文件即可   

  **注意**：若服务器上不存在 password.txt 文件，那么数据库密码是 `123456`。此时务必修改为强密码，类似于：f@N7eUUm25xAjP!$ ，这样有助于提高数据库的安全性，减少数据库密码被破解的风险。

> 需要登录MySQL，请参考 [MySQL可视化管理](#MySQL-数据管理)

## Discuz!Q 安装向导

1. 本地电脑浏览器访问网址：*http://域名/install* 或 *http://服务器公网IP/install*, 进入安装向导界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuzq-wizard-websoft9.png)

2. 设置站点名称、数据库连接和管理员账号，其中**数据库连接无需修改**，然后点击【下一步】
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuzq-setting-websoft9.png)

3. 安装完成，手机扫描右侧二维码可以进入移动端页面。  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuzq-installok-websoft9.png)

4. 本地电脑浏览器访问网址：输入*http://域名/admin* 或 *http://Internet IP/admin*, 进入登录页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuzq-admin-websoft9.png)

5. 输入账号密码（[不知道账号密码？](/zh/stack-accounts.md#superset)），成功登录到 Discuz!Q 后台 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuzq-index-websoft9.png)
    
6. 其他设置：微信公众号，小程序，微信支付等
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuzq-waychat-websoft9.png)

## Discuz 安装向导

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://Internet IP*, 就进入引导首页

2.  首先点击【我同意】，确认用户许可协议
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/ds01.png)

3.  通过环境检测后，点击【下一步】。  
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/ds02.png)

4.  选择需要安装的程序组，建议选择【全新安装】，然后点击【下一步】。  
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/ds03.png)

5.  配置数据库连接信息：默认项已经可用，即直接点击【下一步】而不做任何修改便可以完成连接。   
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/ds04.png)

    > 预装的 MySQL 数据库信息（[查看数据库密码](/zh/stack-accounts.md#mysql)）

6.  安装完成后的界面如下
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/ds05.png)

7.  进入论坛后，可以通过右上角登录对论坛进行管理。
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/ds06.png)


## 常用操作

### 配置

官方提供了很多配置方案，参考：[Tutorials](https://ghost.org/tutorials/) 和 [FAQ](https://ghost.org/faq/)

### 域名绑定

绑定域名的前置条件是：已经完成域名解析（登录域名控制台，增加一个A记录指向服务器公网IP）  

完成域名解析后，从服务器安全和后续维护考量，需要完成**域名绑定**：

Discuz 域名绑定操作步骤：

1. 使用 SFTP 工具登录云服务器
2. 修改 [虚拟机主机配置文件](/维护参考.md#apache)，将其中的域名相关的值
   ```text
     <VirtualHost *:80>
     ServerName  www.mydomain.com # 修改成您的实际域名
     DocumentRoot "/data/wwwroot/discuz"
     ...
   ```
3. 保存配置文件，[重启服务](/维护参考.md#apache-1)

### Discuz 更换域名

Discuz 更换域名非常繁琐，参考论坛上的热心帖子：[discuz! X3 更改域名全程记录](https://www.discuz.net/thread-3528253-1-1.html)

### SSL/HTTPS

网站完成域名绑定且可以通过HTTP访问之后，方可设置HTTPS。

Discuz 预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。

> 除了虚拟主机配置文件之外，HTTPS设置无需修改Nginx任何文件

#### 快速参考

如果你想使用免费证书，只需在服务器中运行一条命令`certbot`就可以启动证书部署

如果你已经申请了商业证书，只需三个步骤，即可完成HTTPS配置

#### Discuz(LAMP)

Discuz(LAMP) 即运行环境采用 **Apache** 作为 Web Server  

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件： */etc/httpd/conf.d/vhost.conf* 
3. 将如下的 **HTTPS 配置段模板**  `<VirtualHost *:443>--</VirtualHost>` 插入到`vhost.conf` 文件中
   ``` text
   #-----HTTPS template start------------
   <VirtualHost *:443>
    ServerName  discuz.yourdomain.com
    DocumentRoot "/data/wwwroot/discuz"
    #ErrorLog "logs/discuz.yourdomain.com-error_log"
    #CustomLog "logs/discuz.yourdomain.com-access_log" common
    <Directory "/data/wwwroot/discuz">
    Options Indexes FollowSymlinks
    AllowOverride All
    Require all granted
    </Directory>
    SSLEngine on
    SSLCertificateFile  /data/cert/discuz.yourdomain.com.crt
    SSLCertificateKeyFile  /data/cert/discuz.yourdomain.com.key
    </VirtualHost>
   #-----HTTPS template end------------
   ```
4. 修改 ServerName, SSLCertificateFile, SSLCertificateKeyFile等参数的值
5. 保存， [重启 Apache 服务](/维护参考.md#apache-1)

#### Discuz(LEMP)

Discuz(LEMP) 即运行环境采用 **Nginx** 作为 Web Server  

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件：*/etc/nginx/conf.d/default.conf* ，插入**HTTPS 配置段** 到 Discuz 的 *server{ }* 中
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

下面以**网易邮箱**为例，提供设置 Discuz 发邮件的步骤：

1. 在网易邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.163.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9@163.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过163邮箱后台设置去获取的授权码
   ```
2. 进入 Discuz 后台，打开：【站长】>【邮件设置】，仔细填写 SMTP 参数项   
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-smtp-1-websoft9.png)

	- 选择第二项
	- 根据你的 SMTP 邮箱选择 SMTP服务器域名，前面的”ssl://“一定不能省略
	- 端口栏输入 SMTP 服务器提供的端口号，一般为 465 ，具体的可根据自己的邮箱地址到官网查看
	- 发件人邮件地址输入你自己的邮箱（**需要与SMTP身份验证用户名所填的邮箱地址一致**）
	- 输入提供 SMTP 服务的邮箱地址
	- 输入 SMTP 服务验证码（和邮箱登陆密码不一样）
 
3. 在 Discuz 后台，打开【全局】>【站点信息】，设置全局管理员邮箱，尽量和 SMTP 发件人邮箱保持一致
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-smtp-2-websoft9.png)
    
4. 测试，如出现如图所示的对话框则证明 SMTP 设置正确，另外，如果出现该对话框却在收件箱内没有邮件，请到垃圾邮件列表查看
	![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-smtp-3-websoft9.png)
 
> 更多邮箱设置（QQ邮箱，阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)

### Discuz 模板/主题/应用中心使用

Discuz 有非常强大生态，大量在线安装模板、插件，您通过登录到 Discuz 后台，并连接您的【应用中心】账号，你就可以通过后台在线购买（免费或收费）插件模板，并在线安装就可以使用了。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-appcenter-websoft9.png)

> 声明：Websoft9 不擅长 Discuz 具体功能的使用，更无法提供此类问题指出。请自行参阅 [Discuz 官方论坛](http://www.discuz.net/forum.php) 完成你要做的吧

### DiscuzQ 修改数据库配置

DiscuzQ 安装目录下的 *config/config.php* 存储数据库连接信息，可以通过此文件来应对数据库账号信息发送变化。

### Discuz 修改数据库配置

在你的 Discuz 安装目录下，有三个与数据库相关的配置文件：

- config/config_global.php
- config/config_ucenter.php
- uc_server/data/config.inc.php

一旦你修改了初始化安装所用的的数据库信息，你需要配套修改以上三个文件以适用新的数据库配置

### Discuz 重置管理员密码

Discuz 密码忘记了，怎么找回？ 如下方案经过实践可用：

1. 适用 SFTP 工具连接服务器，编辑 Discuz 根目录下的 *uc_server/data/config.inc.php* 文件
2. 用下面两行代码替换 `config.inc.php` 中已有的同名段
   ```
   define('UC_FOUNDERPW','047099adb883dc19616dae0ef2adc5b6');
   define('UC_FOUNDERSALT','311254');
   ```
3. [重启服务](/zh/admin-services.md)
4. 此时 Ucenter 创始人的密码就变为: `123456789`
5. 访问 *http://服务器公网IP/uc_server*，以`123456789`作为密码登录 Ucenter
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-ucpwlogin-websoft9.png)
6. 通过【用户管理】中修改管理员密码
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-ucentermodifyadmin-websoft9.png)

### Discuz 集成 WordPress

参考[此处](https://support.websoft9.com/docs/wordpress/zh/solution-more.html##wordpress-与-discuz-集成)

### Discuz 更换默认 Logo

参考论坛上的热心帖子：[如何替换程序默认Logo](http://www.discuz.net/thread-3185527-1-1.html) 

### Discuz 设置伪静态

Discuz论坛安装完成后，想使连接里面显示文章名，应怎么开启它的伪静态功能？

1. 网站安装完成后，登录进入后台，在全局>SEO优化设置>将要设置的页面勾选上，然后提交； 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-rewrite001-websoft9.png)

2. 重新回到上图页面，点击【查看当前的 Rewrite 规则】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-rewrite002-websoft9.png)

3. 页面会列出多种规则，请选择【Apache Web Server(虚拟主机用户)】模板（内容如下）
   ```
   # 将 RewriteEngine 模式打开
   RewriteEngine On

   # 修改以下语句中的 /discuz 为您的论坛目录地址，如果程序放在根目录中，请将 /discuz 修改为 /  对于websoft9提供的镜像，如果服务器内只有一个dicuz网站，则改成如下即可
   RewriteBase / 

   # Rewrite 系统规则请勿修改
   RewriteCond %{QUERY_STRING} ^(.*)$
   RewriteRule ^topic-(.+)\.html$ portal.php?mod=topic&topic=$1&%1
   RewriteCond %{QUERY_STRING} ^(.*)$
   RewriteRule ^article-([0-9]+)-([0-9]+)\.html$ portal.php?mod=view&aid=$1&page=$2&%1
   RewriteCond %{QUERY_STRING} ^(.*)$
   RewriteRule ^forum-(\w+)-([0-9]+)\.html$ forum.php?mod=forumdisplay&fid=$1&page=$2&%1
   RewriteCond %{QUERY_STRING} ^(.*)$
   RewriteRule ^thread-([0-9]+)-([0-9]+)-([0-9]+)\.html$ forum.php?mod=viewthread&tid=$1&extra=page\%3D$3&page=$2&%1
   RewriteCond %{QUERY_STRING} ^(.*)$
   RewriteRule ^group-([0-9]+)-([0-9]+)\.html$ forum.php?mod=group&fid=$1&page=$2&%1
   RewriteCond %{QUERY_STRING} ^(.*)$
   RewriteRule ^space-(username|uid)-(.+)\.html$ home.php?mod=space&$1=$2&%1
   RewriteCond %{QUERY_STRING} ^(.*)$
   RewriteRule ^blog-([0-9]+)-([0-9]+)\.html$ home.php?mod=space&uid=$1&do=blog&id=$2&%1
   RewriteCond %{QUERY_STRING} ^(.*)$
   RewriteRule ^(fid|tid)-([0-9]+)\.html$ archiver/index.php?action=$1&value=$2&%1
   RewriteCond %{QUERY_STRING} ^(.*)$
   RewriteRule ^([a-z]+[a-z0-9_]*)-([a-z0-9_\-]+)\.html$ plugin.php?id=$1:$2&%1
   ```

4. 在 Discuz 的根目录下，新建一个`.htaccess` 文件，将上面的模板内容拷贝进去，保存
   如果是Windows服务器，请选择【另存为】，文件类型选择【所有文件】，否则无法命名
  
5. [重启服务](/zh/admin-services.md) 后生效
  
### Discuz 修改上传附件大小

如果 [PHP](http://support.websoft9.com/docs/lamp) 上传参数已经足够大，但 Discuz 用户上传大小无法满足需求，请通过如下的方式进行修改：

1.进入后台，选择【用户】选项，在【管理者】中选择相应用户组，进入基本设置

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-modifyfilesize001-websoft9.png)

2.选择【论坛相关】，选中【附件相关】

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-modifyfilesize002-websoft9.png)

3.进入附件相关，在【论坛最大附件尺寸】中设置附加最大尺寸

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-modifyfilesize003-websoft9.png)


### MySQL 数据管理

Discuz 预装包中内置 MySQL 及可视化数据库管理工具 `phpMyadmin` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组80端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP/phpmyadmin*，进入phpMyAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)
3. 输入数据库用户名和密码([不知道密码？](#账号密码))
4. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

> 阅读Websoft9提供的 [《MySQL教程》](https://support.websoft9.com/docs/mysql/zh/admin-phpmyadmin.html) ，掌握更多的MySQL实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等

## 异常处理

#### 本地浏览器访问： *http://服务器公网IP* 显示 "该站点未安装"？

问题原因： 没有完成 DiscuzQ 初始化  
解决方案： 本地浏览器访问： *http://服务器公网IP/dl.php* 开始安装

#### 安装的时候显示Discuz! Database Error

如果数据库名称、数据库账号与数据库密码填写与实际不符合，安装就会失败，显示“Discuz! Database Error”错误，具体解决办法：

1. 使用 [phpMyAdmin](/zh/admin-mysql.md) 验证你填写的数据库账号是否与实际匹配
2. 请到服务器上删除./data/install.lock文件
3. 通过网址 *http://服务器公网IP/discuz/install* 或 *http://域名/install* 重装

#### WordPress&Discuz 组合类安装

如何你使用的是 Wordpress+Discuz等组合类部署包，请阅读[《Wordpress&Discuz 安装向导》](https://support.websoft9.com/docs/wordpress/zh/stack-installation.html#wordpress-discuz-安装向导)

#### 浏览器打开IP地址，无法访问 Discuz（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 Discuz 数据？

MySQL

#### 是否可以采用云厂商提供的 RDS 来存储 Discuz 数据？

可以

#### Discuz 默认界面为什么这么普通？

是的，Discuz 默认的界面非常简单，但你可以通过后台的【应用中心】去购买模板，安装插件，对 Discuz 进行十足的个性化设置。
