---
sidebar_position: 1
slug: /nextcloud
tags:
  - Nextcloud
  - 网盘
  - 知识管理
  - 团队协作
---

# 快速入门

[Nextcloud](https://nextcloud.com) 是 ownCloud 创始人发起的分支项目，是一款用于自建私有网盘的云存储开源软件，采用PHP+MySQL开发，提供了PC、IOS和Android三个同步客户端支持多种设备访问，用户可以很方便地与服务器上存储的文件、日程安排、通讯录、书签等重要数据保持同步，还支持其他同步来源：Amazon S3、Dropbox、FTP、Google Drive、OpenStack Object Storage、SMB、WebDAV、SFTP。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-gui-websoft9.png)


## 演示

Nextcloud 官网提供了演示环境，您可以直接[访问演示地址](https://try.nextcloud.com/)

> 免责说明：此处仅提供 Nextcloud 官方的演示地址，不保证与 Websoft9 镜像功能完全一致，若演示过程中若需要填写个人资料、获取Cookie、显示广告等，这些都是官方行为，由此产生的安全问题与我司无关。若您在演示中进行了付费，即表明您愿意接受官方提供的付费服务，由此产生的可能存在的商业纠纷与我们司无关。


在云服务器上部署 Nextcloud 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 和 **TCP:9002** 端口是否开启
3. 若想用域名访问 Nextcloud，请先到 **域名控制台** 完成一个域名解析

## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码。  

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

### Nextcloud

在初始化安装的时候由用户自行设置

### MySQL

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器指定文件中（ */credentials/password.txt* ）


> 需要登录MySQL，请参考 [MySQL可视化管理](#mysql-数据管理)


## Nextcloud 安装向导

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入引导首页

2. 系统首先要求设置一个管理员账号，选择 Nextcloud 的数据库存储方式，建议选择【MySQL】    

3. 填写 MySQL 数据库连接信息（[不知道账号密码？](/zh/stack-accounts.html#mysql)）  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-intall-websoft9.png)

4. 点击“Flish Setup”，完成安装，获得安装成功的提示
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-intallss-websoft9.png)

5. 关闭弹窗，开始体验后台
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-backend-websoft9.png)

6. 进入Marketplace，扩展更多的功能
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-app-websoft9.png)
   
7. 浏览器访问网址：*https://Internet IP:9002* 查看是否安装 **OnlyOffice Document Server**
   ![](http://libs-websoft9-com.oss-cn-qingdao.aliyuncs.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-documentserver-websoft9.png)

8. [设置文档预览与编辑](/zh/solution-more.md#nextcloud-文件预览与编辑)功能（非必要）

> 需要了解更多 Nextcloud 的使用，请参考官方文档：[Nextcloud admin_manual](https://docs.nextcloud.com/server/latest/admin_manual/)

## 常用操作

### 域名绑定

绑定域名的前置条件是：已经完成域名解析（登录域名控制台，增加一个A记录指向服务器公网IP）  

完成域名解析后，从服务器安全和后续维护考量，需要完成**域名绑定**：

Nextcloud 域名绑定操作步骤：

1. 使用 SFTP 工具登录云服务器
2. 修改 [虚拟机主机配置文件](/维护参考.md#apache)，将其中的域名相关的值
   ```text
   #### Nextcloud(LAMP) bind domain #### 

     <VirtualHost *:80>
     ServerName  www.mydomain.com # 修改成您的实际域名
     DocumentRoot "/data/wwwroot/nextcloud"
     ...
     
   #### Nextcloud(LNMP) bind domain #### 

     server {
      listen 80;
      server_name nextcloud.example.com; # 修改成您的实际域名
     ...

   ```
3. 保存配置文件，[重启服务](/维护参考.md#apache-1)

### SSL/HTTPS

网站完成域名绑定且可以通过HTTP访问之后，方可设置HTTPS。

Nextcloud 预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。

> 除了虚拟主机配置文件之外，HTTPS设置无需修改Nginx任何文件

#### 快速参考

如果你想使用免费证书，只需在服务器中运行一条命令`certbot`就可以启动证书部署

如果你已经申请了商业证书，只需三个步骤，即可完成HTTPS配置

#### Nextcloud(LAMP)

Nextcloud(LAMP) 即运行环境采用 **Apache** 作为 Web Server  

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件： */etc/httpd/conf.d/vhost.conf* 
3. 将如下的 **HTTPS 配置段模板**  `<VirtualHost *:443>--</VirtualHost>` 插入到`vhost.conf` 文件中
   ``` text
   #-----HTTPS template start------------
   <VirtualHost *:443>
    ServerName  nextcloud.yourdomain.com
    DocumentRoot "/data/wwwroot/nextcloud"
    #ErrorLog "logs/nextcloud.yourdomain.com-error_log"
    #CustomLog "logs/nextcloud.yourdomain.com-access_log" common
    <Directory "/data/wwwroot/nextcloud">
    Options Indexes FollowSymlinks
    AllowOverride All
    Require all granted
    </Directory>
    SSLEngine on
    SSLCertificateFile  /data/cert/nextcloud.yourdomain.com.crt
    SSLCertificateKeyFile  /data/cert/nextcloud.yourdomain.com.key
    </VirtualHost>
   #-----HTTPS template end------------
   ```
4. 修改 ServerName, SSLCertificateFile, SSLCertificateKeyFile等参数的值
5. 保存， [重启 Apache 服务](/维护参考.md#apache-1)

#### Nextcloud(LEMP)

Nextcloud(LEMP) 即运行环境采用 **Nginx** 作为 Web Server  

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件：*/etc/nginx/conf.d/default.conf* ，插入**HTTPS 配置段** 到 Nextcloud 的 *server{ }* 中
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

下面以**网易邮箱**为例，提供设置 Nextcloud 发邮件的步骤：

1. 在网易邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.163.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9@163.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过163邮箱后台设置去获取的授权码
   ```
2. 登录 Nextcloud 后，点击齿轮图标，打开【个人】设置页面，填写发件邮箱地址
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-smtp-2-websoft9.png)

3. 点击【其他设置】>【电子邮件服务器】，依次填写 SMTP 信息
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-smtp-1-websoft9.png)

    * 发送模式选择“SMTP”，加密方式选择“SSL/TLS”;
    * 输入发送方邮箱地址；
    * 认证方式选择“登录”，并勾选“需要认证”选项；
    * 输入SMTP服务器地址和SMTP服务器的端口号；
    * 输入和发件人邮箱一致的邮箱地址；
    * 输入该邮箱地址的SMTP服务的授权码或密码；
    * 存储凭据；

3. 点击“发送邮件”即可测试SMTP是否设置正确。
     
> 更多邮箱设置（QQ邮箱，阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)

### Nextcloud 更换域名

如果 Nextcloud 需要更换域名，具体操作如下：

1. 完成新的域名解析和域名绑定
2. 修改 [Nextcloud 配置文件](/zh/stack-components.html#nextcloud)中的域名值
   ```
   'overwrite.cli.url' => 'nextcloud.yourdomain.com', # 修改为新域名
   ```
2. [重启 PHP-FPM 服务](/zh/admin-services.html#php-fpm)后生效

### Nextcloud 设置语言

登录 Nextcloud，在后台 【个人】>【个人信息】中设置语言

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-mylanguage-websoft9.png)

### Nextcloud 安装扩展

Nextcloud 后台集成了 [Marketplace](https://apps.nextcloud.com) 大量的扩展（也叫apps），下面介绍如何安装它们

1. 登录 Nextcloud，在后台 【应用】>【应用软件包】中寻找所需的应用
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-backendmk-websoft9.png)
2. 在线安装它

### Nextcloud 集成 LDAP

当企业网盘与多个人使用的时候，用户需要与内部域控集成，以保证用户可以通过Windows账号集成。

Nextcloud提供了 LDAP 集成工具，具体参考官方方案：*[User Authentication with LDAP](https://docs.nextcloud.com/server/latest/admin_manual/configuration_user/user_auth_ldap.html)*

### Nextcloud 命令行工具-OCC

OCC命令是 Nextcloud 的命令行界面。您可以使用OCC执行许多常见的服务器操作，例如安装和升级 Nextcloud，管理用户，加密，密码，LDAP设置等。

### Nextcloud 连接外部存储

Nextcloud 支持多种流行的企业存储服务，具体使用步骤如下：

1. 登录 Nextcloud 后台，安装 **External storage support** 扩展
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-enablestorage-websoft9.png)

2. 打开：【Admin】>【Add storage】>【External Storage】，选择一个外部存储服务
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-enablestorage002-websoft9.png)

3. 根据实际情况进行设置
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-auth_mechanism-websoft9.png)

更多详情参考官方文档：[External Storage](https://docs.nextcloud.com/server/latest/admin_manual/configuration_files/external_storage_configuration_gui.html)

### Nextcloud 数据转移

Nextcloud 的程序和数据文件默认均存在系统盘，你要转移到数据盘（或对象存储），步骤如下：

#### 转移到数据盘

1. 在服务器所在的云平台上购买数据盘，并**挂载**到 Nextcloud 服务器
2. 使用 SFTP 工具连接服务器，停止服务
   ```
   systemctl stop httpd
   ```
3. 新建一个 */data/wwwroot/nextcloud2* 文件夹
4. 初始化数据盘，并将数据盘 **mount** 到新建的 *nextcloud2* 文件夹
5. 将 */data/wwwroot/nextcloud* 下的数据全部拷贝到 */data/wwwroot/nextcloud2*  
6. 修改 Nextcloud [虚拟主机配置文件](/维护参考.md#apache) 的路径
7. 启动服务后生效
   ```
   systemctl start httpd
   ```

#### 转移到对象存储

1. 在服务器所在的云平台上购买对象存储，新建一个 **bucket**
2. 使用 SFTP 工具连接服务器，停止服务
   ```
   systemctl stop httpd
   ```
3. 新建一个 */data/wwwroot/nextcloud2* 文件夹
4. 将对象存储的 bucket **mount** 到新建的 *nextcloud2* 文件夹
5. 将 */data/wwwroot/nextcloud* 下的数据全部拷贝到 */data/wwwroot/nextcloud2*  
6. 修改 Nextcloud [虚拟主机配置文件](/维护参考.md#apache) 的路径
7. 启动服务后生效
   ```
   systemctl start httpd
   ```
8. 设置对象存储开机自动挂载（不同云平台操作不同）

> 以上两种数据转移方案中，**mount** 操作对新手来说是几乎是不可能独立完成的任务。另外，如果转移的数据超过10G，会存在拷贝失败的风险

### Nextcloud 文件预览与编辑

Nextcloud 自身是不能对 Office 文件进行预览或编辑的，需要集成外部的 Office 文档编辑和预览服务才可以具备这样的功能。  

Websoft9 提供的 Nextcloud 部署包内置了 OnlyOffice Document Server(Docker版) ，此软件为 Nextcloud 提供文档预览与编辑服务，具体设置步骤如下：

1. 在云控制台安全组中，检查 **TCP:9002** 端口是否开启

2. 使用本地电脑浏览器测试文档服务是否可用：打开网址：*http://服务器公网IP:9002*，会看到 OnlyOffice Document Server 正在运行的提示 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-dkisrunning-websoft9.png)
   
   > 如果计划使用 HTTPS 访问 OnlyOffice Document Server，需给它绑定域名并设置 HTTPS

3. 登录到 Nextcloud ，单击右上角上角齿轮图标，点击【应用】
	![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-olpreview-1-websoft9.png)

4. 找到【ONLYOFFICE】插件，安装它

  > 可能因为服务器位于中国大陆地区，网络原因在上述第 3 步不能显示应用列表，需手动安装 ONLYOffice 插件：
  > - 可以到 Nextcloud [官方应用商店](https://apps.nextcloud.com/apps/onlyoffice/releases?platform=22#22)下载
  > - 下载到本地后，解压，通过FTP上传到服务器 Nextcloud 应用目录：/data/wwwroot/nextcloud/apps
  > - 登录Nextcloud后台，进入应用中心，启用 ONLYOffice 即可进入下一步操作，开启文档在线预览和编辑
  > ![onlyoffice](https://libs.websoft9.com/Websoft9/blog/tmp/nextcloud/zh/nextcloud-onlyoffice-enable-websoft9.png)

5. 安装完成后，找到**设置**页面，对 ONLYOFFICE 进行如图所示的设置（[参考官方文档](https://api.onlyoffice.com/editors/nextcloud)）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-setonlyoffice-websoft9.png)

   > 图中涂抹处应修改为**服务器公网IP**

6. 返回到首页，刷新或重新登录，然后单击 Office 文件即可在线预览和编辑。

如果连接 ONLYOFFICE 时，Nextcloud 强制要求 ONLYOFFICE 需配置 HTTPS，请参考：[OnlyOffice Document Server 域名绑定和 HTTPS](http://support.websoft9.com/docs/onlyoffice/zh/solution-documentserver.html#域名绑定) 相关章节。

### 使用移动端

Nextcloud 支持移动端，使用步骤如下：
1. [下载](https://nextcloud.com/install)移动端
2. [设置](https://docs.nextcloud.com/android/)移动端到服务器的连接


### MySQL 数据管理

Nextcloud 预装包中内置 MySQL 及可视化数据库管理工具 `phpMyadmin` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组80端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP:9090*，进入phpMyAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)
3. 输入数据库用户名和密码([不知道密码？](/zh/stack-accounts.md))
4. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

> 阅读Websoft9提供的 [《MySQL教程》](https://support.websoft9.com/docs/mysql/zh/admin-phpmyadmin.html) ，掌握更多的MySQL实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等


## 异常处理

#### 浏览器打开IP地址，无法访问 Nextcloud（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 Nextcloud 数据？

是MySQL

#### 是否可以采用云厂商提供的 RDS 来存储 Nextcloud 数据？

可以

#### Nextcloud 是否支持采用对象存储作为网盘使用？

支持，但需要额外配置

#### Nextcloud 是否支持在线文档编辑与预览？

部分镜像预装了 OnlyOffice Document Server，可以通过配置实现在线文档编辑与预览

