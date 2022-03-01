---
sidebar_position: 1
slug: /joomla
tags:
  - Joomla
  - CMS
  - 建站系统
---

# 快速入门

[Joomla](https://joomla.org) 是全球三大开源内容管理系统之一（CMS），占据全球5%的建站市场。其拥有高度的可定制性和电子商务方面的优势，一旦突破最初的学习瓶颈之后，你可以用它进行广泛的Web应用开发，简直是无所不能。目前是由Open Source Matters（见扩展阅读）这个开放源码组织进行开发与支持，Joomla实际有两个开源的部分：一个是Joomla CMS（Joomla内容管理系统），它是网站的一个基础管理平台；另一个是Joomla Platform（Joomla框架）。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-gui-websoft9.jpg)

## 演示

Joomla 官网提供了试用环境，您可以直接试用

* 演示地址：https://launch.joomla.org

> 免责说明：此处仅提供 Joomla 官方的演示，不保证与 Websoft9 部署包功能完全一致，若演示过程中若需要填写个人资料、获取Cookie等，这些都是官方行为，由此产生的安全问题与我司无关。若您在演示中进行了付费，即表明您愿意接受官方提供的付费服务，由此可能存在的商业纠纷与我司无关。

在云服务器上部署 Joomla 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 Joomla，请先到 **域名控制台** 完成一个域名解析

## 账号密码

使用Joomla，可能会用到的几组账号密码如下：

### Joomla

在初始化安装的时候由用户自行设置

### MySQL

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器指定文件中（ */credentials/password.txt* ）
   ![运行cat命令](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

  建议通过云控制台的命令终端，运行`cat /credentials/password.txt` 获取数据库密码（参上图）

  **注意**：旧版本 Joomla 上，不存在 password.txt 文件，其数据库密码是 `123456`。请在初始化安装之前务必将数据库密码修改成复杂密码，这样有助于提高数据库的安全性。

> 需要登录MySQL，请参考 [MySQL可视化管理](#MySQL-数据管理)

## Joomla 安装向导

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://Internet IP*, 就进入引导首页

2. 选择一门语言，并设置站点名称
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-wizard1-websoft9.png)

3. 填写用户，账号，邮件等信息，然后进入下一步
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-wizard2-websoft9.png)

4. 填写您的数据库参数（[不知道账号密码？](#账号密码)），然后进入下一步
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-wizard3-websoft9.png)

5. 安装成功，建议此时点击【特别推荐：安装语言】以安装更多语言以支持未来的多语言网
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-wizard4-websoft9.png)

6. 开始安装更多语言（可选），其中【Chinese Simplified (zh-CN)】是必选语言
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-wizard5-websoft9.png)

7. 根据提示，设置是否开启网站的多语言功能，并设置默认前后台语言
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-wizard6-websoft9.png)

8. Joomla后台地址：http://域名/administrator，成功登陆后您可以开始使用Joomla
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-wizard7-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-wizard8-websoft9.png)

> 需要了解更多 Joomla 的使用，请参考官方文档：[Joomla Docs](https://docs.joomla.org/Main_Page/zh-cn)

## 常用操作

### 域名绑定

绑定域名的前置条件是：已经完成域名解析（登录域名控制台，增加一个A记录指向服务器公网IP）  

完成域名解析后，从服务器安全和后续维护考量，需要完成**域名绑定**：

Joomla 域名绑定操作步骤：

1. 使用 SFTP 工具登录云服务器
2. 修改 [虚拟机主机配置文件](/维护参考.md#apache)，将其中的域名相关的值
   ```text
   #### Joomla(LAMP) bind domain #### 

     <VirtualHost *:80>
     ServerName  www.mydomain.com # 修改成您的实际域名
     DocumentRoot "/data/wwwroot/joomla"
     ...
     
   #### Joomla(LNMP) bind domain #### 

     server {
      listen 80;
      server_name joomla.example.com; # 修改成您的实际域名
     ...

   ```
3. 保存配置文件，[重启服务](/维护参考.md#apache-1)


### SSL/HTTPS

网站完成域名绑定且可以通过HTTP访问之后，方可设置HTTPS。

Joomla 预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。

> 除了虚拟主机配置文件之外，HTTPS设置无需修改Nginx任何文件

#### 快速参考

如果你想使用免费证书，只需在服务器中运行一条命令`certbot`就可以启动证书部署

如果你已经申请了商业证书，只需三个步骤，即可完成HTTPS配置

#### Joomla(LAMP)

Joomla(LAMP) 即运行环境采用 **Apache** 作为 Web Server  

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件： */etc/httpd/conf.d/vhost.conf* 
3. 将如下的 **HTTPS 配置段模板**  `<VirtualHost *:443>--</VirtualHost>` 插入到`vhost.conf` 文件中
   ``` text
   #-----HTTPS template start------------
   <VirtualHost *:443>
    ServerName  joomla.yourdomain.com
    DocumentRoot "/data/wwwroot/joomla"
    #ErrorLog "logs/joomla.yourdomain.com-error_log"
    #CustomLog "logs/joomla.yourdomain.com-access_log" common
    <Directory "/data/wwwroot/joomla">
    Options Indexes FollowSymlinks
    AllowOverride All
    Require all granted
    </Directory>
    SSLEngine on
    SSLCertificateFile  /data/cert/joomla.yourdomain.com.crt
    SSLCertificateKeyFile  /data/cert/joomla.yourdomain.com.key
    </VirtualHost>
   #-----HTTPS template end------------
   ```
4. 修改 ServerName, SSLCertificateFile, SSLCertificateKeyFile等参数的值
5. 保存， [重启 Apache 服务](/维护参考.md#apache-1)

#### Joomla(LEMP)

Joomla(LEMP) 即运行环境采用 **Nginx** 作为 Web Server  

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件：*/etc/nginx/conf.d/default.conf* ，插入**HTTPS 配置段** 到 Joomla 的 *server{ }* 中
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

下面以**网易邮箱**为例，提供设置 Joomla 发邮件的步骤：

1. 在网易邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.163.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9@163.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过163邮箱后台设置去获取的授权码
   ```
2. 登录 Joomla 后，打开：【系统管理】>【全局设置】>【服务器设置】，服务器邮件类型选择：SMTP
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-opensmtp-websoft9.png)

3. 填写准确的 SMTP 设置项信息
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-smtpsettings-websoft9.png)

    * 发送模式选择“SMTP”，加密方式选择“SSL/TLS”;
    * 输入发送方邮箱地址；
    * 认证方式选择“登录”，并勾选“需要认证”选项；
    * 输入SMTP服务器地址和SMTP服务器的端口号；
    * 输入和发件人邮箱一致的邮箱地址；
    * 输入该邮箱地址的SMTP服务的授权码或密码；
    * 存储凭据；

3. 设置完成后，点击【发送测试邮件】，测试可用性
     
> 更多邮箱设置（QQ邮箱，阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)

### Joomla 多语言

Joomla 支持多语言，下面是安装并设置多语言的主要步骤：

1. 登录 Joomla，在后台 【扩展管理】>【语言管理】中安装语言
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-bkinstalllan-websoft9.png)

2. 然后设置前后台的默认语言
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-bkenablelang-websoft9.png)

### Joomla 扩展

Joomla 后台集成了 [Joomla! Extensions Directory™](https://extensions.joomla.org/) 大量的扩展，下面介绍如何安装它们

1. 登录 Joomla
2. 打开【扩展管理】>【安装扩展】，建议选择【从扩展目录安装】的方式在线寻找扩展
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-bkinstallext-websoft9.png)
3. 安装你所需的扩展

### Joomla 安装模板

Joomla 的模板安装，主要通过上传模板安装包的方式实现：

1. 准备好你的模板安装包（一般是 .zip 文件）

2. 登录 Joomla 后台

3. 打开 【扩展管理】>【安装扩展】，选择【上传安装包文件】的方式上传你的模板，开始安装
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-bkuploadext-websoft9.png)

4. 安装后，打开【扩展管理】>【模板管理】>【风格管理】，找到已经安装的模板，启用它
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-bkenabletemplate-websoft9.png)

> 有些模板提供商，提供的模板压缩包中包含 Joomla 内核文件，这种情况下 **安装模板=安装Joomla**

### Joomla Cache

Joomla 后台提供了缓存管理功能，参考下图：

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-cache-websoft9.png)

### Joomla 重置管理员密码

如果忘记了管理员密码，可以参考 [此处](https://docs.joomla.org/How_do_you_recover_or_reset_your_admin_password%3F/zh-cn) 重置密码

### MySQL 数据管理

Joomla 预装包中内置 MySQL 及可视化数据库管理工具 `phpMyadmin` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组80端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP/phpmyadmin*，进入phpMyAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)
3. 输入数据库用户名和密码([不知道密码？](#账号密码))
4. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

> 阅读Websoft9提供的 [《MySQL教程》](https://support.websoft9.com/docs/mysql/zh/admin-phpmyadmin.html) ，掌握更多的MySQL实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等

## 异常处理

#### 浏览器打开IP地址，无法访问 Joomla（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 Joomla 数据？

是MySQL

#### 是否可以采用云厂商提供的 RDS 来存储 Joomla 数据？

可以

#### 当前 Joomla 不是最新版本怎么办？

完成 Joomla 初始化安装后，登录后台可以一键在线更新至最新版本