---
sidebar_position: 1
slug: /zentao
tags:
  - ZenTao（禅道）
  - 项目管理
---

# 快速入门

[ZenTao（禅道）](https://www.zentao.net) 由青岛易软天创网络科技有限公司（用心做开源的杰出公司）开发，是一款优秀的开源项目管理软件。它集产品管理、项目管理、质量管理、文档管理、组织管理和事务管理于一体，是一款专业的研发项目管理软件，完整覆盖了研发项目管理的核心流程。禅道管理思想注重实效，功能完备丰富，操作简洁高效，界面美观大方，搜索功能强大，统计报表丰富多样，软件架构合理，扩展灵活，有完善的API可以调用。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-gui-websoft9.png)

## 演示

快速了解 ZenTao，请查看[官方演示](http://demo.zentao.net/)


在云服务器上部署 ZenTao 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 ZenTao，请先到 **域名控制台** 完成一个域名解析

## 账号密码

使用ZenTao，可能会用到的几组账号密码如下：

### ZenTao

在初始化安装的时候由用户自行设置

### MySQL

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器指定文件中（ */credentials/password.txt* ）
   ![运行cat命令](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

  建议通过云控制台的命令终端，运行`cat /credentials/password.txt` 获取数据库密码（参上图）

  **注意**：旧版本 ZenTao 上，不存在 password.txt 文件，其数据库密码是 `123456`。请在初始化安装之前务必将数据库密码修改成复杂密码，这样有助于提高数据库的安全性。

> 需要登录MySQL，请参考 [MySQL可视化管理](#mysql-数据管理)


## ZenTao 安装向导

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://Internet IP*, 就进入引导首页

2. 根据系统提示，选择语言，然后“开始安装”
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-install001-websoft9.png)

3. 安装进入环境检测页面，点击下一步
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-install002-websoft9.png)

4. 填写您的数据库参数（[查看数据库账号密码](#账号密码)）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-install003-websoft9.png)

5. 设置后台账号信息，请务必设置好并牢记之，然后“保存”（建议勾选导入demo数据，以便理解系统）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-install005-websoft9.png)

6. 系统完成最后一步安装，登录到禅道管理系统，体验并测试系统功能
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-install006-websoft9.png)

7. 登录后台
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-login-websoft9.png)

8. 体验后台
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-gui-websoft9.png)

9. [注册 ZenTao 官网账号](https://www.zentao.net/user-register.html)，便于后续在线安装插件

> 需要了解更多 ZenTao 的使用，请参考官方文档：[ZenTao 开源版手册](https://www.zentao.net/book/zentaopmshelp/40.html) 和 [FAQ](https://www.zentao.net/faq.html)

## 常用操作

### 域名绑定

绑定域名的前置条件是：已经完成域名解析（登录域名控制台，增加一个A记录指向服务器公网IP）  

完成域名解析后，从服务器安全和后续维护考量，需要完成**域名绑定**：

ZenTao 域名绑定操作步骤：

1. 使用 SFTP 工具登录云服务器
2. 修改 [虚拟机主机配置文件](/维护参考.md#apache)，将其中的域名相关的值
   ```text
   #### ZenTao(LAMP) bind domain #### 

     <VirtualHost *:80>
     ServerName  www.mydomain.com # 修改成您的实际域名
     DocumentRoot "/data/wwwroot/zentao"
     ...
     
   #### ZenTao(LNMP) bind domain #### 

     server {
      listen 80;
      server_name zentao.example.com; # 修改成您的实际域名
     ...

   ```
3. 保存配置文件，[重启服务](/维护参考.md#apache-1)

### SSL/HTTPS

网站完成域名绑定且可以通过HTTP访问之后，方可设置HTTPS。

ZenTao 预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。

> 除了虚拟主机配置文件之外，HTTPS设置无需修改Nginx任何文件

#### 快速参考

如果你想使用免费证书，只需在服务器中运行一条命令`certbot`就可以启动证书部署

如果你已经申请了商业证书，只需三个步骤，即可完成HTTPS配置

#### ZenTao(LAMP)

ZenTao(LAMP) 即运行环境采用 **Apache** 作为 Web Server  

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件： */etc/httpd/conf.d/vhost.conf* 
3. 将如下的 **HTTPS 配置段模板**  `<VirtualHost *:443>--</VirtualHost>` 插入到`vhost.conf` 文件中
   ``` text
   #-----HTTPS template start------------
   <VirtualHost *:443>
    ServerName  zentao.yourdomain.com
    DocumentRoot "/data/wwwroot/zentao"
    #ErrorLog "logs/zentao.yourdomain.com-error_log"
    #CustomLog "logs/zentao.yourdomain.com-access_log" common
    <Directory "/data/wwwroot/zentao">
    Options Indexes FollowSymlinks
    AllowOverride All
    Require all granted
    </Directory>
    SSLEngine on
    SSLCertificateFile  /data/cert/zentao.yourdomain.com.crt
    SSLCertificateKeyFile  /data/cert/zentao.yourdomain.com.key
    </VirtualHost>
   #-----HTTPS template end------------
   ```
4. 修改 ServerName, SSLCertificateFile, SSLCertificateKeyFile等参数的值
5. 保存， [重启 Apache 服务](/维护参考.md#apache-1)

#### ZenTao(LEMP)

ZenTao(LEMP) 即运行环境采用 **Nginx** 作为 Web Server  

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件：*/etc/nginx/conf.d/default.conf* ，插入**HTTPS 配置段** 到 ZenTao 的 *server{ }* 中
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

若参考上面的**快速指南**仍无法成功设置HTTPS访问，请阅读由Websoft9提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

HTTPS专题指南方案包括：HTTPS前置条件、HTTPS 配置段模板、注意事项、详细步骤以及故障诊断等具体方案。

### SMTP

大量用户实践反馈，使用**第三方 SMTP 服务发送邮件**是一种最稳定可靠的方式。  

请勿在服务器上安装sendmail等邮件系统，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，非常不稳定，且不易维护、诊断故障很困难。

下面以**网易邮箱**为例，提供设置 ZenTao 发邮件的步骤：

1. 在网易邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.163.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9@163.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过163邮箱后台设置去获取的授权码
   ```
2. 登录禅道，打开：【后台】>【通知】>【邮件】，选择 STMP 作为发信方式

5. 填写准确的 SMTP 设置项信息
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-smtp-websoft9.png)

    * 发送模式选择“SMTP”，加密方式选择“SSL/TLS”;
    * 输入发送方邮箱地址；
    * 认证方式选择“登录”，并勾选“需要认证”选项；
    * 输入SMTP服务器地址和SMTP服务器的端口号；
    * 输入和发件人邮箱一致的邮箱地址；
    * 输入该邮箱地址的SMTP服务的授权码或密码；
    * 存储凭据；

3. 设置完成后，触发消息通知，检验 SMTP 是否正确
     
> 更多邮箱设置（QQ邮箱，阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)

### ZenTao 多语言

ZenTao 支持多语言，直接到后台切换即可  
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-changelanguage-websoft9.png)

### ZenTao 安装插件

ZenTao 提供了 [插件市场](https://www.zentao.net/extension-browse.html) 以方便用户扩展功能

1. 登录后台，打开**插件市场**，搜寻所需的扩展
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-dlplugins-websoft9.png)

2. 点击【下载】，开始安装（安装过程中需要登录 ZenTao 官网）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-installplugin-websoft9.png)

3. 如果是收费插件，需要输入本地电脑的 MAC 地址以验证版权

也可以通过手工安装插件：下载插件，并压缩，然后将目录拷贝到禅道对应的目录，比如 */zentao/module*

### ZenTao 重置管理员密码

禅道管理员密码忘记了，怎么找回？ 使用 phpMyAdmin 登录禅道数据库 **zt_user** 表，找到用户的记录，把 password 的值改成 `e10adc3949ba59abbe56e057f20f883e` ，登录密码重置为：`123456`。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-recoverpw-websoft9.png)

### ZenTao 命令操作

ZenTao 提供了一套命令操作，详情参考官方文档：[初始化管理脚本](https://www.zentao.net/book/zentaopmshelp/35.html)

### ZenTao 集成 Git

参考官方文档：[集成禅道和Git](https://www.zentao.net/book/zentaopmshelp/207.html)

### MySQL 数据管理

ZenTao 预装包中内置 MySQL 及可视化数据库管理工具 `phpMyadmin` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组80端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP:9090*，进入phpMyAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)
3. 输入数据库用户名和密码([不知道密码？](/zh/stack-accounts.md))
4. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

> 阅读Websoft9提供的 [《MySQL教程》](https://support.websoft9.com/docs/mysql/zh/admin-phpmyadmin.html) ，掌握更多的MySQL实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等


## 异常处理

#### 浏览器打开IP地址，无法访问 ZenTao（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 ZenTao 数据？

MySQL

#### 是否可以采用云厂商提供的 RDS 来存储 ZenTao 数据？

可以

