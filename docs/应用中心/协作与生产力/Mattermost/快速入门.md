---
sidebar_position: 1
slug: /mattermost
tags:
  - Mattermost
  - 团队协作
  - 团队通讯
---

# 快速入门

[Mattermost](https://mattermost.com/) 是一个 Slack 的开源替代品。Mattermost 采用 Go 语言开发，这是一个开源的团队通讯服务。为团队带来跨 PC 和移动设备的消息、文件分享，提供归档和搜索功能。

![](https://ucarecdn.com/8cd90d9d-8902-4845-a15b-f4664e5fcfb3/-/format/auto/-/quality/lighter/-/max_icc_size/10/-/resize/1288x/)


在云服务器上部署 Mattermost 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 Mattermost，请先到 **域名控制台** 完成一个域名解析

## 账号密码

使用Mattermost，可能会用到的几组账号密码如下：

### Mattermost

在初始化安装的时候由用户自行设置

### MySQL

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器指定文件中：*/credentials/password.txt*。建议通过云控制台直接连接服务器，进入命令终端，运行`cat /credentials/password.txt` 命令获取数据库密码：
   ![运行cat命令](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

> 需要登录MySQL，请参考 [MySQL可视化管理](#mysql-数据管理)

## Mattermost 安装向导

1. 本地电脑的 Chrome 或 Firefox 浏览器访问网址：`http://域名` 或 `http://服务器公网IP`, 进入引导页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mattermost/mattermost-install-websoft9.png)
2. 设置后台管理员账号和密码，开始创建账号
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mattermost/mattermost-createdaccount-websoft9.png)
3. 开始创建团队 或 登录到系统控制台
4. 打开：【Settings】>【Display】设置你所需的语言
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mattermost/mattermost-display-websoft9.png)
5. 退出并重新登录，所选语言生效

> 需要了解更多 Mattermost 的使用，请参考官方文档：[Matterbase Administrator’s Guide](https://docs.mattermost.com/guides/administrator.html)

## 常用操作

### 域名绑定

绑定域名的前置条件是：Mattermost已经可以通过解析后的域名访问。  

虽然如此，从服务器安全和后续维护考量，**域名绑定**步骤不可省却  

Mattermost 域名绑定操作步骤：

1. 登录云服务器
2. 修改 [Nginx虚拟机主机配置文件](/维护参考.md#nginx)，将其中的域名项的值 *mattermost.example.com* 修改为你的域名
   ```text
   server {
      listen 80;
      server_name    mattermost.example.com; # 改为自定义域名
   ...
   ```
3. 保存配置文件，重启[Nginx服务](/维护参考.md#nginx-1)
4. 登录Mattermost控制台，打开：【ENVIRONMENT】>【Web Server】，修改 【Site URL】值
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mattermost/mattermost-urlset-websoft9.png)

### SSL/HTTPS

网站完成域名绑定且可以通过HTTP访问之后，方可设置HTTPS。

Mattermost预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。

> 除了虚拟主机配置文件之外，HTTPS设置无需修改Nginx任何文件

#### 简易步骤

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

请勿尝试在服务器上安装sendmail等发邮件方案，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，导致不稳定、不易维护、诊断故障困难。

下面以**网易邮箱**为例，提供设置 Mattermost 发邮件的步骤：

1. 在网易邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.163.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9@163.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过163邮箱后台设置去获取的授权码
   ```
2. 登录 Mattermost控制台，打开【ENVIROMENT】>【SMTP】
   ![设置smtp](https://libs.websoft9.com/Websoft9/DocsPicture/en/mattermost/mattermost-smtp-websoft9.png)
3. 填写 SMTP 参数
4. 点击【Test Connection】

更多邮箱设置（QQ邮箱，阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)


### MySQL 数据管理

Mattermost 预装包中内置 MySQL 及可视化数据库管理工具 `phpMyadmin` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组80端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP:9090*，进入phpMyAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)
3. 输入数据库用户名和密码([不知道密码？](/zh/stack-accounts.md))
4. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

> 阅读Websoft9提供的 [《MySQL教程》](https://support.websoft9.com/docs/mysql/zh/admin-phpmyadmin.html) ，掌握更多的MySQL实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等

### 插件

例如，jitmi被用户大量使用

### 迁移

暂无

## 异常处理

#### 浏览器打开IP地址，无法访问 Mattermost（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 Mattermost 数据？

是MySQL

#### 团队用户数受限？

通过 System Console 控制台 【SITE CONFIGURATION】-【Users and Teams】 选项设置 【Max Users Per Team】值来设置团队人数
![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mattermost/mattermost-maxusers-websoft9.png)

