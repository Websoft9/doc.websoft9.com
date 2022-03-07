---
sidebar_position: 1
slug: /gogs
tags:
  - Gogs
  - DevOps
---

# 快速入门

[Gogs](gogs.io)是一款极易搭建的自助 Git 服务，相对于GitHub而言Gogs更加轻量级。任何 Go 语言 支持的平台都可以运行 Gogs，包括 Windows、Mac、Linux 以及 ARM。


## 演示

Gogs 官网提供了试用环境，您可以直接试用

* 演示地址：https://try.gogs.io/

> 免责说明：此处仅提供 XWiki 官方的演示，不保证与 Websoft9 部署包功能完全一致，若演示过程中若需要填写个人资料、获取Cookie等，这些都是官方行为，由此产生的安全问题与我司无关。若您在演示中进行了付费，即表明您愿意接受官方提供的付费服务，由此可能存在的商业纠纷与我司无关。


在云服务器上部署 Gogs 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 Moodle，请先到 **域名控制台** 完成一个域名解析

## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

使用 Gogs，可能会用到的几组账号密码如下：

### Gogs 

在初始化安装的时候由用户自行设置

### MySQL账号和密码：

MySQL 的 root 账户默认密码已优化为强随机密码，查看方式：

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器中的文件中 */credentials/password.txt*  
>[danger] 默认的 “123456” 请务必修改为强密码，类似于：f@N7eUUm25xAjP!$ ，这样有助于提高数据库的安全性，减少数据库密码被破解的风险。
> 需要登录MySQL，请参考 [MySQL可视化管理](#MySQL-数据管理)


## Gogs 安装向导

1. 通过Chrome或FireFox访问：http://服务器公网ip/ ，首先进行数据库设置 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-installdb-websoft9.png)
2. 然后完成应用设置 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-installset-websoft9.png)
3. 点击安装后，系统进入登录界面 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-installreg-websoft9.png)
4. 由于还没有账户，请先点击“还没账户？马上注册”链接，开始注册 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-installreg2-websoft9.png)
5. 注册后再次登录，进入Gogs后台 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-backend-websoft9.png)


## 常用操作

### 域名绑定

当服务器上只有一个网站时，不做域名绑定也可以访问网站。但从安全和维护考量，**域名绑定**不可省却。

以示例网站为例，域名绑定操作步骤如下：

1. 确保域名解析已经生效  
2. 使用 WinSCP 等工具登录云服务器
3. 修改 [Apache虚拟机主机配置文件](/维护参考.md#apache)，将其中的 **ServerName** 项的值修改为你的域名
   ```text
   <VirtualHost *:80>
   ServerName www.mydomain.com # 此处修改为你的域名
   DocumentRoot "/data/wwwroot/mysite2"
   ...
   ```
4. 保存配置文件，重启 [Apache 服务](/维护参考.md#apache-1)

### SSL/HTTPS

### SMTP

大量用户实践反馈，使用**第三方 SMTP 服务发送邮件**是一种最稳定可靠的方式。  

请勿尝试在服务器上安装sendmail等发邮件方案，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，导致不稳定、不易维护、诊断故障困难。

下面以**网易邮箱**为例，提供设置 Parse Server  发邮件的步骤：

1. 在网易邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.163.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9@163.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过163邮箱后台设置去获取的授权码
   ```
2. Parse Server 暂无 SMTP 功能

更多邮箱设置（QQ邮箱，阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)

### MySQL 数据管理

XWiki 预装包中内置 MySQL 及可视化数据库管理工具 `phpMyadmin` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组80端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP/phpmyadmin*，进入phpMyAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)
3. 输入数据库用户名和密码([不知道密码？](#账号密码))
4. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

> 阅读Websoft9提供的 [《MySQL教程》](https://support.websoft9.com/docs/mysql/zh/admin-phpmyadmin.html) ，掌握更多的MySQL实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等

## 异常处理

#### 浏览器打开IP地址，无法访问 Gogs（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 Gogs 数据？

部署包内置 MySQL

#### 是否可以采用云厂商提供的 RDS 来存储 Gogs 数据？

可以
