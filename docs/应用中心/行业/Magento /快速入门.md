---
sidebar_position: 1
slug: /magento
tags:
  - Magento
  - 电子商务
---

# 快速入门

[Magento](https://magento.com) 是全球知名的开源电子商务系统之一，采用php开发，使用Zend Framwork框架，支持B2C、B2B等应用场景。设计得非常灵活、健壮，具有模块化架构体系和丰富的功能组件，是企业级商城建设子首选系统。Magento易于与第三方应用系统无缝集成，可处理海量并发请求，方便通过配置和二次化开发建设一个多种用途、多渠道的电子商务门户。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magentogui-websoft9.png)


在云服务器上部署 Magento 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 Magento，请先到 **域名控制台** 完成一个域名解析

## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

### Magento

* 管理员账号: `admin`
* 管理员密码: 存储在您的服务器中的文件中 */credentials/password.txt*  

### MySQL

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器中的文件中 */credentials/password.txt*  

## Magento 安装向导

Magento 最新版本已经采用命令行完成了安装向导，即可直接使用：

1. 使用本地电脑浏览器访问网址：http://域名 或 http://服务器公网IP, 可以直接进入商城首页  
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-mall-websoft9.png)

2. 访问网址：*http://域名/admin* 或 *http://服务器公网IP/admin*，进入后台登陆页面  
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-login-websoft9.png)

3. 输入用户名和密码[（不知道密码？）](#账号密码)，登录到 Magento 后台管理界面  
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-backend-websoft9.png)

> 需要了解更多Magento的使用，请参考官方文档：[Magento Docs](https://magento.com/resources/technical)

## Magento 入门向导

> 需要了解更多 Canvas 的使用，请参考官方文档：[Canvas Guides](https://community.canvaslms.com/community/answers/guides)

## 常用操作

### 域名绑定

绑定域名的前置条件是：已经完成域名解析（登录域名控制台，增加一个A记录指向服务器公网IP）  

完成域名解析后，从服务器安全和后续维护考量，需要完成**域名绑定**：

Magento 域名绑定操作步骤：

1. 使用 SFTP 工具登录云服务器
2. 修改 [虚拟机主机配置文件](/维护参考.md#apache)，将其中的域名相关的值
   ```text
   #### Magento(LAMP) bind domain #### 

     <VirtualHost *:80>
     ServerName  www.mydomain.com # 修改成您的实际域名
     DocumentRoot "/data/wwwroot/magento"
     ...
     
   #### Magento(LNMP) bind domain #### 

     server {
      listen 80;
      server_name magento.example.com; # 修改成您的实际域名
     ...

   ```
3. 保存配置文件，[重启服务](/维护参考.md#apache-1)
4. 通过SSH连接云服务器，运行下面的CLI命令
   ```shell
   cd /data/wwwroot/magento
   php bin/magento config:set web/unsecure/base_url http://www.mydomain.com/ # 修改成您的实际域名，必须以 / 结束
   php bin/magento config:set web/secure/base_url http://www.mydomain.com/ # 修改成您的实际域名，必须以 / 结束
   ```

### SSL/HTTPS

必须完成[域名绑定](/zh/solution-more.md)且可通过 HTTP 访问 Magento ，才可以设置 HTTPS。

Magento 预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。因此，除了虚拟主机配置文件之外，HTTPS 设置则不需要修改 Nginx 其他文件。

#### 快速指南

不管使用下面2种的哪种部署，在设置完服务器配置后，必须要完成Magento自身的配置，通过执行下面的命令：

```
cd /data/wwwroot/magento
php bin/magento setup:store-config:set --use-secure=1 --use-secure-admin=1 --base-url-secure="https://www.yourdomain.com/"
php bin/magento cache:flush  #将基础URL更改为https并刷新缓存
```

#### 自动部署

如果没有申请证书，只需在服务器中运行一条命令`sudo certbot`便可以启动免费证书**自动**申请和部署

```
sudo certbot
```

#### 手动部署

如果你已经申请了证书，只需下面几个步骤，即可完成 HTTPS 配置

#### Magento(LAMP)

Magento(LAMP) 即运行环境采用 **Apache** 作为 Web Server  

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件： */etc/httpd/conf.d/vhost.conf* 
3. 将如下的 **HTTPS 配置段模板**  `<VirtualHost *:443>--</VirtualHost>` 插入到`vhost.conf` 文件中
   ``` text
   #-----HTTPS template start------------
   <VirtualHost *:443>
    ServerName  magento.yourdomain.com
    DocumentRoot "/data/wwwroot/magento"
    #ErrorLog "logs/magento.yourdomain.com-error_log"
    #CustomLog "logs/magento.yourdomain.com-access_log" common
    <Directory "/data/wwwroot/magento">
    Options Indexes FollowSymlinks
    AllowOverride All
    Require all granted
    </Directory>
    SSLEngine on
    SSLCertificateFile  /data/cert/magento.yourdomain.com.crt
    SSLCertificateKeyFile  /data/cert/magento.yourdomain.com.key
    SSLCertificateChainFile  /data/cert/magento.yourdomain.com_chain.crt
    </VirtualHost>
   #-----HTTPS template end------------
   ```
4. 修改 ServerName, SSLCertificateFile, SSLCertificateKeyFile等参数的值
5. 保存， [重启 Apache 服务](/维护参考.md#apache-1)

#### Magento(LNMP)

Magento(LMP) 即运行环境采用 **Nginx** 作为 Web Server  

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件：*/etc/nginx/conf.d/default.conf* ，插入**HTTPS 配置段** 到 Magento 的 *server{ }* 中
 ``` text
   #-----HTTPS template start------------
   listen 443 ssl; 
   ssl_certificate /data/cert/xxx.crt;
   ssl_certificate_key /data/cert/xxx.key;
   ssl_trusted_certificate /data/cert/chain.pem;
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

下面以**网易邮箱**为例，提供设置 Magento 发邮件的步骤：

1. 在网易邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.163.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9@163.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过163邮箱后台设置去获取的授权码
   ```
2. 确保你的 Magento 已经[连接到官方 Marketplace](/zh/stack-installation.html#连接-magento-marketplace)
3. 使用 SSH 工具登录到服务器，使用命令方式安装 Magento SMTP 扩展
   ```
    cd /data/wwwroot/magento` 
	composer require mageplaza/module-smtp
	php bin/magento setup:upgrade 
	php bin/magento setup:di:compile
   ```
   如果不会使用命令，请直接在 Marketplace 上购买 SMTP 插件
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-smtpplugin-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-buysmtpplugin-websoft9.png)

4. 登录到 Magento 后台，完成 SMTP 参数设置  
   - 点击**MAGEPLAZA**，在右边菜单选择**应用配置管理**;  
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-smtp-2-websoft9.png)

   - 按照下图输入相应的信息
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-smtp-3-websoft9.png)

5. 登录到 Magento 后台，设置发件箱
   - 首先进入应用配置管理页面:  
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-smtp-4-websoft9.png)
   - 按照下图设置邮箱：  
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-smtp-5-websoft9.png)
     
> 更多邮箱设置（QQ邮箱，阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)


### Magento 安装扩展

建议通过 Magento 后台在线安装扩展：

1. 确保你的 Magento 已经[连接到官方的 Marketplace](/zh/stack-installation.html#连接-magento-marketplace)
3. 在 Marketplace 找到您需要的扩展或主题，购买完成，点击【Install】
4. 登录 Magento 后台，打开：【SYSTEM】>【Web Setup Wizard】>【System Configration】 
5. 在左侧菜单栏选择【EXTENSION MANAGER】，单击【Refresh】 将购买信息同步到网站，然后通过【Review and Install】查看
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-theme-1-websoft9.png)
   > Refresh 可能会出现同步失败，请多次刷新

6. 在列表内选择插件或主题，即可进行安装；
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-theme-2-websoft9.png)
7. 安装时会进行系统环境检查，条件全面满足才可以开始安装
8. 安装过程时间较长且报错，请查看[故障原因](/zh/else-troubleshooting.html#magento-在线升级或在线安装插件报错？)

### 连接 Magento Marketplace

安装 Magento 后，建议把你安装的 Magento 系统与 Magento 官方的 Marketplace 资源进行在线连接，这样便可以使用 Marketplace 上的大量资源

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-setuptools-websoft9.png)  

1. 到官方 [注册 Magento 账号](https://account.magento.com/applications/customer/login)
2. 登录 Marketplace，打到My Profile 的 Access Keys 页面新建一个自己的 Access Key; 
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-smtp-1-websoft9.png)  
3. 保存 Access Key
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-savemykey-websoft9.png)  
4. 登录自己的 Magento 后台，依次打开：【SYSTEM】> 【Web Setup Wizard】
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-websetupwz-websoft9.png) 
5. 在【System config】设置项中输入你在 Marketplace 上获取的 Access Key
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-setmkkey-websoft9.png) 
6. 成功保存，连接成功
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-setmkkeyss-websoft9.png) 
7. 连接后，就可以很方便的使用 Marketplace 上的资源

### Magento 安装中文包

中文包 zh_Hans_CN 已经存在 */data/wwwroot/Magento/vendor/magento/language-zh_hans_cn* 目录下  

需要启用中文请完成如下两个步骤：

1.  如果你希望你的前台是中文，进入到Magento管理员界面，后台 Stores > Configuration > General > Local 中设置Local为Chinese(China)
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-setlan-websoft9.png)
2.  如果你希望你的账户后台是中文，那么请在管理员页面右上角点击你的账户 Account Setting > Interface Local 中设置 Interface Local 为Chinese（China）

### Magento Cache

Cache（缓存）是 Magento 的一项重要设置：

1. 登录 Magento 后台，依次打开：【System】>【Tools】> 【Cache Management】
2. 选择需要刷新的缓存
3. 点击【Flush Magento Cache】和【Flush Cache Storage】开始刷新
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-flushcache-websoft9.png)
4. 也可以取消一些页面的缓存设置
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-dscache-websoft9.png)


### MySQL 数据管理

Magento 预装包中内置 MySQL 及可视化数据库管理工具 `phpMyadmin` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组9090端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP:9090*，进入phpMyAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)
3. 输入数据库用户名和密码([不知道密码？](/zh/stack-accounts.md))
4. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

> 阅读Websoft9提供的 [《MySQL教程》](https://support.websoft9.com/docs/mysql/zh/) ，掌握更多的MySQL实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等

## 异常处理

#### 浏览器打开IP地址，无法访问 Magento（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 Magento 数据？

安装在服务器上的 MySQL 数据库

#### 是否可以采用云厂商提供的 RDS 来存储 Magento 数据？

可以，执行下面命令可以更换 Magento 所使用的数据库

```
magento setup:config:set --db-host=DB-HOST --db-name=DB-NAME --db-user=DB-USER --db-engine=DB-ENGINE --db-password=DB-PASSWORD
```

#### Cron job问题处理（Windows）

Windows下安装 Magento 后，若出现 **One or more indexers are invalid. Make sure your Magento cron job is running** 的提示,请执行以下步骤:

1. 双击右下角xampp界面,点击shell按钮打开命令行窗口;
2. 输入 `php htdocs\magento\bin\magento indexer:reindex` 即可；
3. 回到magento界面，刷新页面，该问题即可解决。