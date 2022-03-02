---
sidebar_position: 1
slug: /sakai
tags:
  - Sakai
  - LMS
  - 在线学习系统
---

# 快速入门

[Sakai](赛课)是一个自由、开源的在线协作和学习环境，是一个类似于 Moodle 的课程管理、学习管理系统，以及虚拟学习环境。

![](https://photogallery.oss.aliyuncs.com/photo/1904996544835414/undefined/ab4c28cc-5f11-49ec-aa09-ec512039b4f5.png)

## 演示

Sakai 官网提供了试用环境，您可以直接试用

* 演示地址：https://trysakai.longsight.com/

> 免责说明：此处仅提供 Sakai 官方的演示，不保证与 Websoft9 部署包功能完全一致，若演示过程中若需要填写个人资料、获取Cookie等，这些都是官方行为，由此产生的安全问题与我司无关。若您在演示中进行了付费，即表明您愿意接受官方提供的付费服务，由此可能存在的商业纠纷与我司无关。


在云服务器上部署 Sakai 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 Moodle，请先到 **域名控制台** 完成一个域名解析

## 账号密码

使用Sakai，可能会用到的几组账号密码如下：

### Sakai 

管理员用户名：admin  
管理员密码：admin

### MySQL账号和密码：

MySQL 的 root 账户默认密码已优化为强随机密码，查看方式：

1. 使用 [SFTP远程管理工具](http://support.websoft9.com/docs/linux-sftp/) 连接到服务器；
2. 找到 **password.txt** 文件 ( **/root/password.txt** )，打开即可查看 MySQL 数据库用户名和密码；
3. 若无 **password.txt** 文件，则为旧版镜像，其 MySQL 默认用户名和密码为 ：`root/123456`；
4. 查看密码后，可自行访问 http://公网IP/phpmyadmin 管理数据库相关信息。
   
  >[danger] 默认的 “123456” 请务必修改为强密码，类似于：f@N7eUUm25xAjP!$ ，这样有助于提高数据库的安全性，减少数据库密码被破解的风险。


## Sakai 安装向导

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://公网ip/portal/*  

2. 输入账号和密码（[查看](#账号密码)），登录


## 常用操作

### 域名绑定

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

EspoCRM 预装包中内置 MySQL 及可视化数据库管理工具 `phpMyadmin` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组80端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP/phpmyadmin*，进入phpMyAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)
3. 输入数据库用户名和密码([不知道密码？](#账号密码))
4. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

> 阅读Websoft9提供的 [《MySQL教程》](https://support.websoft9.com/docs/mysql/zh/admin-phpmyadmin.html) ，掌握更多的MySQL实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等

## 异常处理
