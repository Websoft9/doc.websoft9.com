---
sidebar_position: 1
slug: /metabase
tags:
  - Metabase
  - 大数据分析
  - BI
---

# 快速入门

[Metabase](https://www.metabase.com/) 是一个简单、开源的数据呈现方式，通过给公司成员、分析师新建Question，从而得到数据进行分析、学习。

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-product-screenshot.png)

在云服务器上部署 Metabase 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 Metabase，请先到 **域名控制台** 完成一个域名解析

## 账号密码

使用Metabase，可能会用到的几组账号密码如下：

### Metabase

在初始化安装的时候由用户自行设置

### MySQL

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器指定文件中（ */credentials/password.txt* ）
   ![运行cat命令](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

  建议通过云控制台的命令终端，运行`cat /credentials/password.txt` 获取数据库密码（参上图）

  **注意**：旧版本 Metabase 上，不存在 password.txt 文件，其数据库密码是 `123456`

> 需要登录MySQL，请参考 [MySQL可视化管理](#mysql-数据管理)

## Metabase 安装向导

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://Internet IP*，进入登陆页面（如果页面不是登陆页面，请按照步骤3-7操作）
![Metabase登陆界面](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-login-websoft9.png)

2. 输入邮件地址和密码[（不知道密码？）](/zh/stack-accounts.md)，登录到 Metabase 后台管理界面
![Metabase后台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-dashborad-websoft9.png)

3. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://Internet IP*, 就进入了软件的引导首页
![Metabase初始化页面](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-start-websoft9.png)

4. 软件的加载速度比较慢，耐心等待1-3分钟，直至出现如下的界面。
![开始安装Metabase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-starty-websoft9.png)

5. 点击“让我们开始吧”，接下来首先设置登录账号，完成后进入下一步
6. 添加你的数据：可以选择使用的数据类型来连接一个需要分析的外部数据库，如果没有也可以点击“我之后再添加”，这样系统会默认给 Metabase 增加一个H2演示数据
![配置Metabase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-installdb-websoft9.png)

7. 安装成功后的界面，点击“带我去Metabase”登录后台
![Metabase安装成功](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-installss-websoft9.png)

8. 以H2演示数据为例，开始数据分析工作
![Metabase H2演示](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-dashborad-websoft9.png)

9. Metabase有强大的系统管理能力：后台->设置，进入系统管理界面
![Metabase Admin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-admin-websoft9.png)

10. 通过“添加一个数据库”来增加一个数据分析源
![Metabase 增加数据库](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-adddb-websoft9.png)

11. 通过点击“人员管理”标签，管理使用Metabase用户，包括增加用户、修改密码等
![Metabase 人员管理](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-users-websoft9.png)

> 需要了解更多Metabase的使用，请参考官方文档：[Metabase Documentation](https://metabase.com/docs/latest/)


## 常用操作

### 域名绑定

绑定域名的前置条件是：Metabase已经可以通过解析后的域名访问。  

虽然如此，从服务器安全和后续维护考量，**域名绑定**步骤不可省却  

Metabase 域名绑定操作步骤：

1. 登录云服务器
2. 修改 [Nginx虚拟机主机配置文件](/维护参考.md#nginx)，将其中的 **server_name** 项的值 *metabase.example.com* 修改为你的域名
   ```text
   server {
      listen 80;
      server_name    metabase.example.com; # 改为自定义域名
   ...
   ```
3. 保存配置文件，重启[Nginx服务](/维护参考.md#nginx-1)

### SSL/HTTPS

网站完成域名绑定且可以通过HTTP访问之后，方可设置HTTPS。

Metabase预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。

> 除了虚拟主机配置文件之外，HTTPS设置无需修改Nginx任何文件

### 快速参考

如果你想使用免费证书，只需在服务器中运行一条命令`certbot`就可以启动证书部署

如果你已经申请了商业证书，只需三个步骤，即可完成HTTPS配置

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件：*/etc/nginx/conf.d/default.conf* ，插入**HTTPS 配置段** 到 *server{ }* 中
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

下面以**网易邮箱**为例，提供设置 Metabase 发邮件的步骤：

1. 在网易邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.163.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9@163.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过163邮箱后台设置去获取的授权码
   ```
2. 登录 Metabase控制台
3. 填写 SMTP 参数
![Metabase SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-smtp-websoft9.png)
4. 点击【Test Connection】

更多邮箱设置（QQ邮箱，阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)


### MySQL 数据管理

Metabase 预装包中内置 MySQL 及可视化数据库管理工具 `phpMyadmin` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组9090端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP:9090*，进入phpMyAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)
3. 输入数据库用户名和密码([不知道密码？](#账号密码))
4. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

> 阅读Websoft9提供的 [《MySQL教程》](https://support.websoft9.com/docs/mysql/zh/admin-phpmyadmin.html) ，掌握更多的MySQL实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等+

### 迁移

暂无


## 异常处理

#### 浏览器打开IP地址，无法访问 Metabase（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 Metabase 数据？

是MySQL



