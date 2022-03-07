---
sidebar_position: 1
slug: /prestashop
tags:
  - PrestaShop
  - 电子商务
---

# 快速入门

[PrestaShop](https://prestashop.com) 是一款全功能、跨平台的免费开源电子商务解决方案，采用PHP+MySQL开发。始于2008年，发展迅速，全球已超过四万家网店采用Prestashop进行部署。Prestashop基于Smarty引擎编程设计，模块化设计，扩展性强，能轻易实现多种语言，多种货币浏览交易，支持Paypal等几乎所有的支付手段，是外贸网站建站的不错选择。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/pretashopui-websoft9.png)


## 演示

Prestashop 官网提供了演示环境，您可以直接访问演示地址体验：http://demo.prestashop.com

> 免责说明：此处仅提供Prestashop官方的演示地址，不保证与Websoft9镜像功能完全一致，若演示过程中若需要填写个人资料、获取Cookie、显示广告等，这些都是官方行为，由此产生的安全问题与我司无关。若您在演示中进行了付费，即表明您愿意接受官方提供的付费服务，由此产生的可能存在的商业纠纷与我们司无关。


在云服务器上部署 PrestaShop 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 PrestaShop，请先到 **域名控制台** 完成一个域名解析

## 账号密码

使用PrestaShop，可能会用到的几组账号密码如下：

### PrestaShop

在初始化安装的时候由用户自行设置

### MySQL

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器指定文件中（ */credentials/password.txt* ）
   ![运行cat命令](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

  建议通过云控制台的命令终端，运行`cat /credentials/password.txt` 获取数据库密码（参上图）

  **注意**：旧版本 PrestaShop 上，不存在 password.txt 文件，其数据库密码是 `123456`。请在初始化安装之前务必将数据库密码修改成复杂密码，这样有助于提高数据库的安全性。

> 需要登录MySQL，请参考 [MySQL可视化管理](#MySQL-数据管理)

## PrestaShop 安装向导

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://Internet IP*, 就进入引导首页  

   可能会有小版本的升级提醒，建议点击【yes,please!】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-installupdate-websoft9.png)
   
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-language-websoft9.png)
   
2. 选择语言，接受许可协议，继续下一步

4. 安装进入管理员账号设置界面，牢记之，点击“下一步”
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-adminconf-websoft9.png)
   
4. 安装进入数据库配置界面（[不知道数据库密码？](#账号密码)）然后点击”保存”
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-dbconfig-websoft9.png)
   
5. 系统安装成功，分别进入后台和前台体验
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-installss-websoft9.png)
   
6. 登录后台，系统提示删除intall文件夹
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-delinstall-websoft9.png)
   
7. 使用WinSCP登录到服务器，进入 */data/wwwroot/prestashop*，删除 **install** 文件夹
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-delinstallftp-websoft9.png)
   
8. 删除完成后，点击第六步的后台链接，开始体验后台（请牢记后台地址）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-login-websoft9.png)
   
9. 登录成功，体验后台
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-backend-websoft9.png)

> 需要了解更多 PrestaShop 的使用，请参考官方文档：[PrestaShop Docs](https://www.prestashop.com/en/resources/documentations)

## 连接 PrestaShop Marketplace

安装 PrestaShop 后，建议把你安装的 PrestaShop 系统与 PrestaShop 官方的 Marketplace 资源进行在线连接，这样便可以在线使用 Marketplace 上的大量资源

1. 登录 PrestaShop 后台
2. 依次打开：【Modules】>【Module Manager】，点击【Connect to Addons marketplace】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-connectmk-websoft9.png)  
3. 开始注册账号
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-registeraccount-websoft9.png)  
4. 注册完成后，登录连接
5. 连接后，就可以很方便的使用 Marketplace 上的资源
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/prestashop/prestashop-marketplace-websoft9.png)

## 常用操作

### 域名绑定

绑定域名的前置条件是：已经完成域名解析（登录域名控制台，增加一个A记录指向服务器公网IP）  

完成域名解析后，从服务器安全和后续维护考量，需要完成**域名绑定**：

PrestaShop 域名绑定操作步骤：

1. 使用 SFTP 工具登录云服务器
2. 修改 [虚拟机主机配置文件](/zh/stack-components.html#apache)，将其中的域名相关的值
   ```text
   #### PrestaShop(LAMP) bind domain #### 

     <VirtualHost *:80>
     ServerName  www.mydomain.com # 修改成您的实际域名
     DocumentRoot "/data/wwwroot/prestashop"
     ...
     
   #### PrestaShop(LNMP) bind domain #### 

     server {
      listen 80;
      server_name prestashop.example.com; # 修改成您的实际域名
     ...

   ```
3. 保存配置文件，[重启服务](/维护参考.md#apache-1)

### SSL/HTTPS

网站完成域名绑定且可以通过HTTP访问之后，方可设置HTTPS。

PrestaShop 预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。

> 除了虚拟主机配置文件之外，HTTPS设置无需修改Nginx任何文件

#### 快速参考

如果你想使用免费证书，只需在服务器中运行一条命令`certbot`就可以启动证书部署

如果你已经申请了商业证书，只需三个步骤，即可完成HTTPS配置

#### PrestaShop(LAMP)

PrestaShop(LAMP) 即运行环境采用 **Apache** 作为 Web Server  

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件： */etc/httpd/conf.d/vhost.conf* 
3. 将如下的 **HTTPS 配置段模板**  `<VirtualHost *:443>--</VirtualHost>` 插入到`vhost.conf` 文件中
   ``` text
   #-----HTTPS template start------------
   <VirtualHost *:443>
    ServerName  prestashop.yourdomain.com
    DocumentRoot "/data/wwwroot/prestashop"
    #ErrorLog "logs/prestashop.yourdomain.com-error_log"
    #CustomLog "logs/prestashop.yourdomain.com-access_log" common
    <Directory "/data/wwwroot/prestashop">
    Options Indexes FollowSymlinks
    AllowOverride All
    Require all granted
    </Directory>
    SSLEngine on
    SSLCertificateFile  /data/cert/prestashop.yourdomain.com.crt
    SSLCertificateKeyFile  /data/cert/prestashop.yourdomain.com.key
    </VirtualHost>
   #-----HTTPS template end------------
   ```
4. 修改 ServerName, SSLCertificateFile, SSLCertificateKeyFile等参数的值
5. 保存， [重启 Apache 服务](/维护参考.md#apache-1)

#### PrestaShop(LEMP)

PrestaShop(LEMP) 即运行环境采用 **Nginx** 作为 Web Server  

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件：*/etc/nginx/conf.d/default.conf* ，插入**HTTPS 配置段** 到 PrestaShop 的 *server{ }* 中
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

---

完成环境的 HTTPS 设置之后，【登录 PrestaShop 后台】>【Shop Parameters】>【General】，对所有页面启用 HTTPS 设置
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-allhttps-websoft9.png)


#### 详细指南

若参考上面的**简易步骤**仍无法成功设置 HTTPS 访问，请阅读由 Websoft9 提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

HTTPS专题指南方案包括：HTTPS 前置条件、HTTPS 配置段模板、注意事项、详细步骤以及故障诊断等具体方案。

### SMTP

大量用户实践反馈，使用**第三方 SMTP 服务发送邮件**是一种最稳定可靠的方式。  

请勿在服务器上安装sendmail等邮件系统，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，非常不稳定，且不易维护、诊断故障很困难。

下面以**网易邮箱**为例，提供设置 PrestaShop 发邮件的步骤：

1. 在网易邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.163.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9@163.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过163邮箱后台设置去获取的授权码
   ```
4. 登录到 PrestaShop 后台，完成 SMTP 参数设置  
  
   - 依次打开：【配置】>【高级参数】>【邮箱】，选择第二项【设置我的SMTP参数】
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-smtp-1-websoft9.png)
   - 准确的填写你的 SMTP 参数
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-smtp-2-websoft9.png) 

5. 发送测试邮件
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-smtp-3-websoft9.png)
     
> 更多邮箱设置（QQ邮箱，阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)

### PrestaShop 维护模式

登录 PrestaShop 后台，打开：【Shop Parameters】>【General】>【Maintenance】，设置维护模式
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-mantmode-websoft9.png)


### Prestashop 更换域名

如果 PrestaShop 需要更换域名，具体操作如下：

1. 完成域名解析和域名绑定
2. 将 PrestaShop 设置为维护模式
3. 打开 PrestaShop 的配置文件（[路径参考](/zh/stack-components.html#prestashop)），修改其中与域名有关的内容
4. 登录 PrestaShop 后台，打开：【Shop Parameters】>【Traffic&SEO】，修改它
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-seturl-websoft9.png)

### PrestaShop 导入数据

登录 PrestaShop 后台，打开：【Advanced Parameters】>【Import】，导入所需的数据
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-importdb-websoft9.png)


### PrestaShop Modules

Modules 是 PrestaShop 功能扩展，Modules 可以即插即用

1. 登录 PrestaShop 后台，
2. 依次打开：【Modules】>【Module Catalog】，找到所需的插件，点击【Install】开始安装
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-installmd-websoft9.png)
3. 依次打开：【Modules】>【Module Manager】，找到所需的插件，点击【Upgrade】即可在线升级
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-upgrademodules-websoft9.png)

### Prestashop 连接 Marketplace

除了系统提供 Modules 之外，更多的 Modules 都是通过 Marketplace 发布，因此需要将你的 PrestaShop 连接到 Marketplace，便可以在线使用上面的资源。

具体操作步骤参考：[连接 Marketplace](#连接-PrestaShop-Marketplace)


### PrestaShop 语言包

Prestashop的多语言支持非常的成熟，系统在后台内置一套多语言体系，只需要选择对应的语言，在线导入到您的 PrestaShop 系统即可。

#### 导入语言

1. 登录Prestashop后台，依次打开：【国际】>【本地化】，进入设置界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-setlanguage-websoft9.png)
2. 选择一个语言包，点击本项之右下角【上传】图标，完成在线导入
3. 选择【语言】选项卡，我们就可以看到成功导入的语言包
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-alllanguage-websoft9.png) 

> 每次导入一个新的语言包，系统会自动为此语言生成一个伪静态规则。如果您的某个语言的伪静态设置出现问题导致了 Redirect（重定向），可以删除这个语言，然后重新导入一次即可。

#### 删除语言

1. 登录Prestashop后台，依次打开：【国际】>【本地化】>【语言】，编辑您需要的语言
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-dellanguage001-websoft9.png)
2. 将语言的状态修改为“否”，然后保存
3. 回到【语言】选项开，找到已经打叉的语言，删除之即可
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-dellanguage002-websoft9.png)

### MySQL 数据管理

PrestaShop 预装包中内置 MySQL 及可视化数据库管理工具 `phpMyadmin` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组80端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP/phpmyadmin*，进入phpMyAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)
3. 输入数据库用户名和密码([不知道密码？](/zh/stack-accounts.md))
4. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

> 阅读Websoft9提供的 [《MySQL教程》](https://support.websoft9.com/docs/mysql/zh/admin-phpmyadmin.html) ，掌握更多的MySQL实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等

## 异常处理

#### 浏览器打开IP地址，无法访问 PrestaShop（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 PrestaShop 数据？

是MySQL

#### 是否可以采用云厂商提供的 RDS 来存储 PrestaShop 数据？

可以
