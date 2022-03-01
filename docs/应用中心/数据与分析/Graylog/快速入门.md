---
sidebar_position: 1
slug: /graylog
tags:
  - Graylog
  - 日志管理
  - 数据分析
---

# 快速入门

[Graylog](https://graylog-server.apache.org/) 是一个基于 Java 开发的开源的日志聚合、分析、审计、展现和预警工具。

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/graylog/graylog-gui-websoft9.png)

在云服务器上部署 Graylog 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 Graylog，请先到 **域名控制台** 完成一个域名解析

## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

### Graylog

* 管理员账号: `admin`
* 管理员密码: 存储在您的服务器中的文件中 */credentials/password.txt*  

### MongoDB

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器中的文件中 */credentials/password.txt*  

## Graylog 安装向导

1. 使用本地 Chrome 等浏览器访问网址： *http://域名* or *http://服务器公网IP*，进入 Graylog 登录界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/graylog/graylog-login-websoft9.png)

2. 输入账号密码后，登入到 Graylog 控制台 ([不知道密码?](/zh/stack-accounts.md#graylog))  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/graylog/graylog-console-websoft9.png)

3. 如果需要，可以给 [Graylog 绑定域名](/zh/solution-more.md#域名绑定)

> 需要了解更多 Graylog 的使用，请参考官方文档：[Configuring Graylog](https://docs.graylog.org/en/latest/pages/installation/docker.html)

## Graylog 入门向导

正在编写

## 常用操作

### CLI


### 域名绑定

当服务器上只有一个网站时，不做域名绑定也可以访问网站。但从安全和维护考量，**域名绑定**不可省却。

以示例网站为例，域名绑定操作步骤如下：

1. 确保域名解析已经生效  

2. 使用 SFTP 工具登录云服务器

3. 修改 [Nginx虚拟机主机配置文件](/维护参考.md#nginx)，将其中的 **server_name** 项的值修改为你的域名
   ```text
   server
   {
   listen 80;
   server_name www.example.com;  # 此处修改为你的域名
   ...
   }
   ```
4. 修改 Graylog 目录下的 [.env 文件 ](/维护参考.md#graylog)，修改 `APP_SITE_URL` 为域名

5. 重启服务后生效
   ```
   sudo systemctl restart nginx
   cd /data/wwwroot/graylog && sudo docker-compose up -d
   ```

### SSL/HTTPS

网站完成域名绑定且可以通过HTTP访问之后，方可设置HTTPS。

Graylog 预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。

> 除了虚拟主机配置文件之外，HTTPS设置无需修改Nginx任何文件

#### 自动部署

如果没有申请证书，只需在服务器中运行一条命令`certbot`便可以启动免费证书**自动**申请和部署

```
sudo certbot
```

#### 手动部署

如果你已经申请了证书，只需三个步骤，即可完成 HTTPS 配置

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件：*/etc/nginx/conf.d/default.conf* ，插入**HTTPS 配置段** 到 *server{ }* 中
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
3. 重启 Nginx 服务
   ```
   sudo systemctl restart nginx
   ```
#### 专题指南

若参考上面的**简易步骤**仍无法成功设置HTTPS访问，请阅读由Websoft9提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

HTTPS专题指南方案包括：HTTPS前置条件、HTTPS 配置段模板、注意事项、详细步骤以及故障诊断等具体方案。

### SMTP

大量用户实践反馈，使用**第三方 SMTP 服务发送邮件**是一种最稳定可靠的方式。  

请勿在服务器上安装sendmail等邮件系统，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，非常不稳定，且不易维护、诊断故障很困难。

下面以**网易邮箱**为例，提供设置 Graylog 发邮件的步骤：

1. 在网易邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.163.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9@163.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过163邮箱后台设置去获取的授权码
   ```
2. 修改 Graylog 配置文件中的 Refer to [transport_email 参数](https://docs.graylog.org/en/3.3/pages/configuration/server.conf.html#email) 

3. 重启 Graylog 后生效
   ```
   sudo docker restart graylog
   ```

更多邮箱设置（QQ邮箱，阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)

### MongoDB 数据管理

Graylog 预装包中内置 MongoDB 及可视化数据库管理工具 `AdminMongo` ，使用请参考如下步骤：

1. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP:9091*，使用 adminMongo 管理数据库
   ![adminmongo](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mongodb/adminmongo-consolegui-websoft9.png)
   
2. 也可以使用 Mongo Shell 采用命令行方式管理数据库([不知道密码？](#账号密码))
   ```
   # log in Mongo Shell without authenticating
   mongo

   # log in Mongo Shell witt authenticating
   mongo admin --username root -p
   ```

> 阅读Websoft9提供的 [《MongoDB教程》](https://support.websoft9.com/docs/mongodb/zh) ，掌握更多的MongoDB实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等

### 集群

我们知道，Graylog 运行时，包括如下软件：  

* Graylog 日志采集、分析
* ElasticSearch 日志存储
* MongoDB 系统配置系统

Graylog 支持如下最简答的部署方式：  
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/graylog/graylog-minisetup-websoft9.png)

也支持复杂的[集群](https://docs.graylog.org/v1/docs/multinode-setup)部署：  
![Graylog 集群部署架构图](https://libs.websoft9.com/Websoft9/DocsPicture/zh/graylog/graylog-hasetup-websoft9.png)

其中，MongoDB 实际上可以不做集群。  

> 更多信息参考官方的[架构指南](https://www.slideshare.net/Graylog/graylog-engineering-design-your-architecture)

### 配置文件

针对于 Docker 安装，Graylog 每个配置选项都可以通过环境变量进行设置。  
只需在参数名称前加上前缀GRAYLOG_并将其全部大写。

```
version: '2'
  services:
    mongo:
      image: "mongo:4.2"
      # Other settings [...]
    elasticsearch:
      image: docker.elastic.co/elasticsearch/elasticsearch-oss:7.10.2
      # Other settings [...]
    graylog:
      image: graylog/graylog:4.2
      # Other settings [...]
      environment:
        GRAYLOG_TRANSPORT_EMAIL_ENABLED: "true"
        GRAYLOG_TRANSPORT_EMAIL_HOSTNAME: smtp
        GRAYLOG_TRANSPORT_EMAIL_PORT: 25
        GRAYLOG_TRANSPORT_EMAIL_USE_AUTH: "false"
        GRAYLOG_TRANSPORT_EMAIL_USE_TLS: "false"
        GRAYLOG_TRANSPORT_EMAIL_USE_SSL: "false"
```

同时，也支持直接修改配置文件 server.conf

### 重置密码

如果无法找回管理员密码，可以通过下面的步骤重置密码

1. 使用 SSH 工具登录服务器，运行下面的密码重置命令
   ```
   new_password=admin123@graylog
   sha_password=$(echo -n $new_password | sha256sum | awk '{ print $1 }')
   sudo sed -i "s/8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918/$sha_password/g" /data/wwwroot/graylog/.env
   ```

2. 重新运行容器编排命令，密码就被重置为 `admin123@graylog`
   ```
   cd /data/wwwroot/graylog && sudo docker-compose up -d
   ```

> 你可以将 new_password 设置为任何你想要的密码

## 异常处理

#### 浏览器打开IP地址，无法访问 Graylog（白屏没有结果）？

您的服务器对应的安全组 80 端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### Graylog 应用的端口是多少？

9001

#### 不配置域名可以使用 Graylog 吗？

可以

#### 本部署方案是如何部署 Graylog 的？

基于官方提供的 [Docker 部署方案](https://docs.graylog.org/en/latest/pages/installation/docker.html)

#### 如何修改域名配置？

1. 修改 */etc/nginx/sites-available/default* 的 server_name
2. 修改 */data/wwwroot/docker-graylog/.env* 中 APP_SITE_URL

