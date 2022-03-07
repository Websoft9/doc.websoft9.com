---
sidebar_position: 1
slug: /opencart
tags:
  - OpenCart
  - 电子商务
---

# 快速入门

[OpenCart](https://opencart.com) 是近年来国内外非常流行的 PHP 开源电子商务网站系统。该电商网站系统安装方便，功能强大，操作简单。支持多语言、多货币和多店铺。OpenCart 外围开发生态圈发达，更有上万款免费和收费的模块插件和模板主题可供选择。代码完全开源，功能持续更新，代码结构清晰易懂，二次开发容易上手，入门门槛低。基于这些特点使得 OpenCart 快速成为了世界上广泛应用的电子商务建站系统。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/opencart/opencart-gui-websoft9.png)

## 演示

OpenCart 官网提供了演示环境，您可以直接访问演示地址体验：[https://demo.opencart.com](https://demo.opencart.com)


在云服务器上部署 OpenCart 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 OpenCart，请先到 **域名控制台** 完成一个域名解析

## 账号密码

使用OpenCart，可能会用到的几组账号密码如下：

### OpenCart

在初始化安装的时候由用户自行设置

### MySQL

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器指定文件中（ */credentials/password.txt* ）
   ![运行cat命令](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

  建议通过云控制台的命令终端，运行`cat /credentials/password.txt` 获取数据库密码（参上图）

  **注意**：旧版本 OpenCart 上，不存在 password.txt 文件，其数据库密码是 `123456`。请在初始化安装之前务必将数据库密码修改成复杂密码，这样有助于提高数据库的安全性。

> 需要登录MySQL，请参考 [MySQL可视化管理](#MySQL-数据管理)

## OpenCart 安装向导

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://Internet IP*, 就进入引导首页
2. 进入安装界面，同意安装协议
   ![oc1](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/oc1.png)  
3. 通过环境检测后，进入下一步  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/oc2.png)
3. 填写数据库信息（[不知道账号密码？](#账号密码)）并设置后台管理账号
   ![oc1](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/oc3.png)
4. 安装成功后，系统提示“删除安装目录”
   ![oc1](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/oc4.png)
5. 请记得通过SFTP工具删除安装目录（*/data/wwwroot/opencart/upload/install*）
6. 安装成功，可以分别体验商城前台和后台

> 需要了解更多 OpenCart 的使用，请参考官方文档：[OpenCart Docs](http://docs.opencart.com)

## 常用操作

### 域名绑定

绑定域名的前置条件是：已经完成域名解析（登录域名控制台，增加一个A记录指向服务器公网IP）  

完成域名解析后，从服务器安全和后续维护考量，需要完成**域名绑定**：

OpenCart 域名绑定操作步骤：

1. 使用 SFTP 工具登录云服务器
2. 修改 [虚拟机主机配置文件](/维护参考.md#apache)，将其中的域名相关的值
   ```text
   #### OpenCart(LAMP) bind domain #### 

     <VirtualHost *:80>
     ServerName  www.mydomain.com # 修改成您的实际域名
     DocumentRoot "/data/wwwroot/opencart"
     ...
     
   #### OpenCart(LNMP) bind domain #### 

     server {
      listen 80;
      server_name opencart.example.com; # 修改成您的实际域名
     ...

   ```
3. 保存配置文件，[重启服务](/维护参考.md#apache-1)

### OpenCart 更换域名

如果 OpenCart 需要更换域名，具体操作如下：

1. 完成新的 **域名解析和域名绑定**
2. 修改 OpenCart 根目录下的配置文件 `config.php`
   ```
   // HTTP
   define('HTTP_SERVER', 'http://example.com/');
   // HTTPS
   define('HTTPS_SERVER', 'https://example.com/');
   ```
3. 修改 OpenCart 后台目录下的配置文件 `admin/config.php`
   ```
   // HTTP
   define('HTTP_SERVER', 'http://www.example.com/admin/');
   define('HTTP_CATALOG', 'http://www.example.com/');
   // HTTPS
   define('HTTPS_SERVER', 'http://www.example.com/admin/');
   define('HTTPS_CATALOG', 'http://www.example.com/');
   ```
4. [重启 PHP-FPM 服务](/维护参考.md#php-fpm)后生效

### OpenCart vQmod

Opencart 2.0 使用vQmod机制安装扩展，需提前安装并启用vQmod，具体如下：

1. [下载vQmod](https://github.com/vqmod/vqmod)
2. Go to Extensions > Installer，上传下载的 vqmod.zip 文件
3. Go to Extensions > Extensions > Modules > Integrated VQmod to install and then edit to enable this module

### OpenCart 重置密码

如果忘记了管理员密码，又没有配置好 SMTP 导致无法通过邮箱找回密码，怎么办？

1. 首先使用 [phpMyAdmin 登录 MySQL](#mysql-数据管理)
2. 找到您的 Opencart 数据库，打开SQL命令操作窗口
3. 运行如下命令
   ```
   //下面是将用户名 admin 的后台管理员密码重置为 123456，请根据实际情况调整命令
   UPDATE oc\_user SET password = md5('123456'), salt = '' WHERE username = 'admin';
   ```

### OpenCart Extension

OpenCart 提供了大量的扩展发布在 Marketplace 上，下面是具体的安装扩展步骤：

1. 在 Marketplace 上下载扩展
2. 登录 OpenCart 后台，依次打开：【Extensions】>【Installer】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/opencart-installex-websoft9.png)
3. 上传扩展文件
4. 等待安装完成

### OpenCart 语言包

在Opencart中增加一个新的语言（以中文包为例），主要有三个步骤：

1. 到 [OpenCart Marketplace](https://www.opencart.com/index.php?route=marketplace/extension/info&extension_id=19126&filter_category_id=2&page=8)下载中文语言包（请注意版本）；
2. 将下载好的语言包解压出来，会得到一个名为 upload 的文件夹，内有 admin 和 catalog 两个文件夹分别为后台和前台的文件夹；
3. 使用 SFTP 软件将前后台中文包分别上传到服务器：
   ```
   admin->language->zh_cn 文件夹 上传到  ```/data/wwwroot/opencart/admin/language``` 目录下
   catalog->language->zh-cn 文件夹 上传到 ```/data/wwwroot/opencart/catalog/language``` 目录下
   ```
4. 登录 OpenCart，打开【System】>【localization】>【languages】，增加一个语言并填写配置信息
	![websoft9](https://libs.websoft9.com/Websoft9/DocsPicture/zh/opencart/opencart-language-1-websoft9.png)

5. 店铺前后台分别选择所需的语言：【System】>【Settings】，其中Language 为前台默认语言，Administration Language 为后台默认语言
	   ![websoft9](https://libs.websoft9.com/Websoft9/DocsPicture/zh/opencart/opencart-language-2-websoft9.png)

6. 刷新前后台页面，系统显示新的语言


### SSL/HTTPS

网站完成域名绑定且可以通过HTTP访问之后，方可设置HTTPS。

OpenCart 预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。

> 除了虚拟主机配置文件之外，HTTPS设置无需修改Nginx任何文件

#### 快速参考

如果你想使用免费证书，只需在服务器中运行一条命令`certbot`就可以启动证书部署

如果你已经申请了商业证书，只需三个步骤，即可完成HTTPS配置

#### OpenCart(LAMP)

OpenCart(LAMP) 即运行环境采用 **Apache** 作为 Web Server  

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件： */etc/httpd/conf.d/vhost.conf* 
3. 将如下的 **HTTPS 配置段模板**  `<VirtualHost *:443>--</VirtualHost>` 插入到`vhost.conf` 文件中
   ``` text
   #-----HTTPS template start------------
   <VirtualHost *:443>
    ServerName  opencart.yourdomain.com
    DocumentRoot "/data/wwwroot/opencart"
    #ErrorLog "logs/opencart.yourdomain.com-error_log"
    #CustomLog "logs/opencart.yourdomain.com-access_log" common
    <Directory "/data/wwwroot/opencart">
    Options Indexes FollowSymlinks
    AllowOverride All
    Require all granted
    </Directory>
    SSLEngine on
    SSLCertificateFile  /data/cert/opencart.yourdomain.com.crt
    SSLCertificateKeyFile  /data/cert/opencart.yourdomain.com.key
    </VirtualHost>
   #-----HTTPS template end------------
   ```
4. 修改 ServerName, SSLCertificateFile, SSLCertificateKeyFile等参数的值
5. 保存， [重启 Apache 服务](/维护参考.md#apache-1)

#### OpenCart(LEMP)

OpenCart(LEMP) 即运行环境采用 **Nginx** 作为 Web Server  

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件：*/etc/nginx/conf.d/default.conf* ，插入**HTTPS 配置段** 到 OpenCart 的 *server{ }* 中
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

#### 详细指南

若参考上面的**简易步骤**仍无法成功设置 HTTPS 访问，请阅读由 Websoft9 提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

HTTPS专题指南方案包括：HTTPS 前置条件、HTTPS 配置段模板、注意事项、详细步骤以及故障诊断等具体方案。

### SMTP

大量用户实践反馈，使用**第三方 SMTP 服务发送邮件**是一种最稳定可靠的方式。  

请勿在服务器上安装sendmail等邮件系统，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，非常不稳定，且不易维护、诊断故障很困难。

下面以**网易邮箱**为例，提供设置 OpenCart 发邮件的步骤：

1. 在网易邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.163.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9@163.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过163邮箱后台设置去获取的授权码
   ```
2. 登录到 OpenCart 后台，完成 SMTP 参数设置  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/opencart/opencart-smtp-websoft9.png)
  
   - 输入提供SMTP服务的服务器地址，其中的 ssl://  一定不能省略
   - 务必准确的填写你的 SMTP 参数

3. 发送测试邮件
     
> 更多邮箱设置（QQ邮箱，阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)

### MySQL 数据管理

OpenCart 预装包中内置 MySQL 及可视化数据库管理工具 `phpMyadmin` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组80端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP/phpmyadmin*，进入phpMyAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)
3. 输入数据库用户名和密码([不知道密码？](#账号密码))
4. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

> 阅读Websoft9提供的 [《MySQL教程》](https://support.websoft9.com/docs/mysql/zh/admin-phpmyadmin.html) ，掌握更多的MySQL实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等

## 异常处理

#### 浏览器打开IP地址，无法访问 OpenCart（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 OpenCart 数据？

是MySQL

#### 是否可以采用云厂商提供的 RDS 来存储 OpenCart 数据？

可以
