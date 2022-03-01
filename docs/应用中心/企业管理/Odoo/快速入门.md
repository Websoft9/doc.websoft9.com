---
sidebar_position: 1
slug: /odoo
tags:
  - Odoo
  - 企业管理
  - ERP
---

# 快速入门

[Odoo](https://www.odoo.com/) 是全球成功的开源ERP/CRM软件，有超过730个合作伙伴和200万用户。采用Python+Postgresql开发，产品远超过ERP范畴，对CRM、门户网站、电子商务、互联网方面的支持也非常完善。Odoo有强大而灵活的系统架构，可在不修改核心代码的情况下修改功能、升级模块、新增模块。 Odoo活跃的社区在不断修正各类错误，贡献各种用途的模块，产品迭代速度非常快。常用模块包括：采购管理，销售管理，库存管理，财务管理，货品管理，营销管理，客户关系管理，生产管理，人事管理，服务支持、电子商务、建站等。用户可以直接从模块库中选择安装适用模块，或进行模块卸载，升级的管理操作。

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odooui-websoft9.png)


在云服务器上部署 Odoo 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 Odoo，请先到 **域名控制台** 完成一个域名解析

## 账号密码

使用Odoo，可能会用到的几组账号密码如下：

### Odoo

在初始化安装的时候由用户自行设置

### PostgreSQL

Odoo 采用 [Peer Authentication](https://www.postgresql.org/docs/10/auth-methods.html#AUTH-PEER) 方式连接 PostgreSQL，即以操作系统用户登录数据库，无需密码。Odoo 本身集成了管理和备份 PostgreSQL的功能，请参考 [Odoo 数据库管理](#odoo-中管理数据库)

另外，**Windows版**安装了 PostgreSQL 桌面工具 pgAdmin，使用参考：

1. 远程桌面登录到Windows服务器
2. 打开pgAdmin，输入账号（默认用户名 : `openpg`，默认密码 : `openpgpwd`）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/odoo/odoo-pgadmin2-websoft9.png)

## Odoo 安装向导

下面分别介绍社区版和企业版安装向导：

### 社区版

1. 使用本地 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://Internet IP*, 进入初始化页面
   ![Odoo 社区版初始化页面](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-startcreatedb-websoft9.png)

2. 填写好所有参数，点击【create database】按钮，开始初始化安装。
   > 其中 Email 和 Password 是登录账号密码，务必牢记之

3. 初始化安装完成后，登录后台，安装所需的 APP
  ![Odoo APPS](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-consoleui-websoft9.png)

### 企业版

部署 Odoo 企业版后，根据镜像引导页获取试用授权，便可以免费试用一个月。

1. 使用本地 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://Internet IP*, 进入欢迎页面
  ![Odoo 欢迎页面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/odoo/odoo-eewelcome-websoft9.png)

2. 获取授权后，登录云服务器，运行如下命令解锁企业版
```
bash /etc/odoo/ee_init.sh
```

3. 刷新欢迎页面后，显示初始化安装步骤
  ![Odoo 初始化页面](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-startcreatedb-websoft9.png)

4. 完成初始化后，提示一旦安装第一个应用之后，系统就会提示要求注册订阅号（You will be able to register your database once you have installed your first app.）
  ![Odoo 注册提示](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-registersb000-websoft9.png)

5. 系统提示 **Register your subscription or buy a subscription**，请输入试用码
  ![Odoo 注册提示](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-registersb001-websoft9.png)

6. 开始试用。请注意试用期后正式向 Odoo 官方订阅企业版，否则数据库被清空
  ![Odoo 注册提示](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-registersb002-websoft9.png)

7. 更多应用的安装和系统管理类似社区版

> 免费试用期结束之后，到 [Odoo 官方](https://www.odoo.com/zh_CN/pricing)进行企业版订阅，需折扣可以联系我们。


### 数据库管理

为了保障 Odoo 系统的数据库安全，下面的数据库管理工作非常重要：

1. 注销 Odoo 登录，在登录界面点击【Manage Database】链接  
  ![Odoo manage database](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-loginpage-websoft9.png)

2. 点击【set a master password】给数据库设置一个主密码保护数据库（非常重要）
  ![Odoo set a pssword](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-setmasterpw-websoft9.png)

3. Odoo 支持多租户（多企业组织），点击【create database】，可以再增加一个企业组织
  ![Odoo 新增数据库](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-multidb-websoft9.png)

4. 回到登录界面，发现会多一个 database 选项
  ![Odoo 重新登录](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-multidblogin-websoft9.png)

> 需要了解更多Odoo的使用，请参考官方文档：[Odoo Documentation](https://www.odoo.com/documentation/master/index.html)


## 常用操作

### 管理Odoo

本章列出使用 Odoo 过程中最常见的一些配置

#### 普通设置

Odoo 后台提供了设置界面，参考：

1. 登录 Odoo 后，打开点击左上角的设置图标，打开【Settings】项
   ![Odoo设置界面](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-settingspanel-websoft9.png)
2. 接下来可以进行：安装apps，设置语言，增加用户，企业初始化等操作

#### 设置企业 Logo
![Odoo 设置logo](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-settingslogo-websoft9.png)

#### 增加语言
1. 通过【Settings】控制台增加一个语言
  ![Odoo 增加语言](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-settingslangs-websoft9.png)
2. 转到【Administrator】>【Prefrences】  
  ![Odoo 用户管理](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-pref-websoft9.png)
3. 给用户设置语言
  ![Odoo 设置语言](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-language002-websoft9.png)

#### 开发者模式

Odoo 默认是管理者模式，如果需要深度设置，请先开启开发者模式

1. 登录 Odoo 后，打开点击左上角的设置图标，打开【Settings】项
2. 在 Settings 界面的右下点击【Active the developer mode】
   ![Odoo 开发者模式](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-enabledev-websoft9.png)
3. 在开发者模式下，Settings 控制台的功能更多了

#### 安装wkhtmltopdf

Odoo 镜像默认已经安装 wkhtmltopdf，如何你想重新安装它，具体操作步骤如下：

1.  卸载已经安装的 wkhtmltopdf 旧版本:

    ~~~
    ~# sudo apt-get remove wkhtmltopdf 
    ~# sudo apt-get autoremove
    ~~~

2.  去官网下载最新版本的 wkhtmltopdf 压缩包:

    ~~~
    ~# wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
    ~~~

3.  解压下载好的压缩包，得到一个名为：wkhtmltox 的文件夹：

    ~~~
    ~# tar –xf [filename]
    ~~~

4.  将 wkhtmltox/bin/wkhtmltomage 和 wkhtmmltox/bin/wkhtmltoodf 这两个文件复制到 /usr/bin 目录下去：

    ~~~
    ~# cp wkhtmltox/bin/wkhtmltoimage /usr/bin/
    ~# cp wkhtmmltox/bin/wkhtmltoodf /usr/bin/
    ~~~

5.  重启Odoo服务

    ~~~
    ~# systemctl restart odoo
    ~~~

#### Apps市场

Odoo除了基础模块之外，通过[Odoo Apps市场](https://www.odoo.com/apps/modules)提供了大量优质的第三方模块。通过使用第三方模块，用户可以快速找到所需的功能，以免费或极小的代价满足需求，快速上线业务，这是Odoo开源生态的带给用户的巨大价值，商业ERP在这方面是无法取代的。

### 域名绑定

绑定域名的前置条件是：已经完成域名解析（一般是通过增加一个A记录指向服务器IP来实现解析操作） 

虽然如此，从服务器安全和后续维护考量，**域名绑定**步骤不可省却  

Odoo 域名绑定操作步骤：

1. 使用 WinSCP 登录云服务器
2. 修改 [Nginx虚拟机主机配置文件](/维护参考.md#nginx)，将其中的 **server_name** 项的值 *_* 修改为你的域名
   ```text
   server {
      listen 80;
      server_name    _; # 改为自定义域名
   ...
   ```
3. 保存配置文件，[重启Nginx服务](/维护参考.md#nginx)

### Odoo 中管理数据库

Odoo 预装包中内置 PostgreSQL 及可视化数据库管理功能 ，使用请参考如下步骤：

1. 在 Odoo 登录界面点击【Manage Database】链接  
![Odoo manage database](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-loginpage-websoft9.png)

2. 点击【set a master password】给数据库设置一个主密码保护数据库（非常重要）
![Odoo set a password](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-setmasterpw-websoft9.png)

3. 设置密码
![Odoo set a password](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-setapw-websoft9.png)

3. 选择操作项，管理数据库
![Odoo set a password](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-manages-websoft9.png)

#### 新增

Odoo 支持多租户（多企业组织），增加一个数据库就等于增加一个企业。多个企业共同使用一套 Odoo，采用不同的账号登录，相互不干扰。

1. 点击【create database】，输入密码，设置名称
   ![Odoo 新增数据库](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-multidb-websoft9.png)
2. 新增完成后，你会看到数据库管理界面列出新增的数据库

#### 备份

1. 输入密码，选择备份格式，点击【Backup】
   ![Odoo 备份](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-managesbk-websoft9.png)

2. 备份完成后，系统会自动下载备份数据（zip文件）

#### 复制

可以完整复制一个企业组织，作为新企业组织的数据

1. 输入密码，设置名称，点击【Continue】
![Odoo set a pssword](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-managesdp-websoft9.png)

2. 复制成功后，数据库管理栏目会列出新复制的数据库

#### 删除

请谨慎操作

#### 恢复

数据库被删除后，可以通过备份进行恢复

1. 输入密码，选择备份文件，命名恢复后的数据库名称，点击【Continue】
![Odoo set a pssword](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-managesrs-websoft9.png)

2. 数据库恢复过程中可能会出现"413 Request Entity Too Large"，[解决办法](/zh/else-troubleshooting.md#odoo类)

#### 修改主密码

只可以修改主密码，如果忘记了主密码，重置密码方案待研究

#### Web GUI 工具管理数据库

Odoo 预装包中内置 PostgreSQL 及可视化数据库管理工具 `phpPgAdmin` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组9090端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP:9090*，进入phpPgAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin.png)
3. 输入数据库用户名和密码([不知道密码？](/zh/stack-accounts.md))
4. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/phppgadmin-gui-websoft9.png)

#### 更多

阅读Websoft9提供的 [《PostgreSQL教程》](https://support.websoft9.com/docs/postgresql/zh/) ，掌握更多的 PostgreSQL 实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等


### SSL/HTTPS

网站完成[域名绑定](/zh/solution-more.md#域名绑定)且可以通过HTTP访问之后，方可设置HTTPS。

Odoo预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。

> 除了虚拟主机配置文件之外，HTTPS设置无需修改Nginx任何文件

#### 简易步骤

如果你想使用免费证书，只需在服务器中运行一条命令`certbot`就可以启动证书部署

如果你已经申请了商业证书，只需三个步骤，即可完成HTTPS配置

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件：*/etc/nginx/sites-available/default* ，插入**HTTPS 配置段** 到 *server{ }* 中
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
3. 重启Nginx服务

#### 专题指南

若参考上面的**简易步骤**仍无法成功设置HTTPS访问，请阅读由Websoft9提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

HTTPS专题指南方案包括：HTTPS前置条件、HTTPS 配置段模板、注意事项、详细步骤以及故障诊断等具体方案。

### SMTP

大量用户实践反馈，使用**第三方 SMTP 服务发送邮件**是一种最稳定可靠的方式。  

请勿在服务器上安装sendmail等邮件系统，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，非常不稳定，且不易维护、诊断故障很困难。

下面以**网易邮箱**为例，提供设置 Odoo 发邮件的步骤：

1. 在网易邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.163.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9@163.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过163邮箱后台设置去获取的授权码
   ```
2. 登录 Odoo 控制台，安装 SMTP 所需的 **Discuss** 模块
   ![Odoo SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-discussmodule-websoft9.png)

3. 通过：【Settings】>【General Settings】>【Discuss】开始配置邮箱
   ![Odoo SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-gsetmail-websoft9.png)

3. 填写 SMTP 参数
   ![Odoo SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-smtps-websoft9.png)
4. 点击【Test Connection】

更多邮箱设置（QQ邮箱，阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)

### 开启PostgreSQL远程连接

Odoo默认安装的PostgreSQL并不会启用数据库账号，也不会开启远程连接。如果需要通过本地的Navicat等客户端连接数据库，主要操作如下：

官方解决方案：https://www.odoo.com/documentation/13.0/setup/deploy.html#postgresql


### 企业版

部署 Odoo 企业版后，需要根据镜像的引导页面向 Odoo 官方人员获取试用授权，便可以免费试用一个月。

获取授权后，试用 SSH 登录云服务器，运行如下脚本解锁企业版

```
bash /etc/odoo/ee_init.sh
```

## 异常处理

#### 浏览器打开IP地址，无法访问 Odoo（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 Odoo 数据？

PostgreSQL

#### 勾选 Demo data了，以后还能删除这些数据吗？

官方并没有提供 Demo data 的删除工具，建议直接删除数据库，然后再新增（此时不再勾选 Demo data）
