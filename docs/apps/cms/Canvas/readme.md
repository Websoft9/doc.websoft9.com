---
sidebar_position: 1
slug: /canvas
tags:
  - Canvas
  - 在线学习管理
---

# 快速入门

[Canvas](https://www.instructure.com/canvas/) 是一个基于云端的开源在线学习系统（LMS），使学校能够构建数字学习环境，以应对远程教学趋势。Canvas简化了教学，提高了学习效率，并消除了支持和发展传统学习技术的麻烦。它具有开放，直观的特点，通过所有数字工具和内容，简化老师的教学，让学生获得更简单的互联网学习体验。

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/canvas/canvas-gui-websoft9.png)


在云服务器上部署 Canvas 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 Canvas，请先到 **域名控制台** 完成一个域名解析

## 账号密码

通过**SSH**连接云服务器，运行 `cat /credentials/password.txt` 命令，可以查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

### Canvas

* 管理员账号: `help@websoft9.com`
* 管理员密码: 存储在您的服务器中的文件中 */credentials/password.txt*  

> 请登录 Canvas 后台后修改账号和密码

### PostgreSQL

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器指定文件中（ */credentials/password.txt* ）

## Canvas 安装向导

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入登录页面
   ![canvas 登录](https://libs.websoft9.com/Websoft9/DocsPicture/zh/canvas/canvas-login-websoft9.png)

2. 输入账号密码（[不知道账号密码？](/zh/stack-accounts.md#canvas)），成功登录到 Canvas 后台  
   ![canvas 后台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/canvas/canvas-console001-websoft9.png)

3. 依次打开：【管理员】>【设置】>【账户设置】设置语言  
   ![canvas 设置语言](https://libs.websoft9.com/Websoft9/DocsPicture/zh/canvas/canvas-setlanguage-websoft9.png)

4. 依次打开：【账户】>【设置】>【编辑设置】修改默认邮件账户和密码
   ![canvas 修改账号](https://libs.websoft9.com/Websoft9/DocsPicture/zh/canvas/canvas-setaccount001-websoft9.png)
   ![canvas 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/canvas/canvas-setaccount002-websoft9.png)

5. 开放注册：【管理员】>【身份验证设置】>【提供者】开放教师和学生注册 
   ![canvas 开放注册](https://libs.websoft9.com/Websoft9/DocsPicture/zh/canvas/canvas-register-websoft9.png)

## Canvas 入门向导

编写中... (欢迎您投稿)

> 需要了解更多 Canvas 的使用，请参考官方文档：[Canvas Guides](https://community.canvaslms.com/community/answers/guides)

## 常用操作

### 初始化 Canvas

如果你忘记了管理员密码，又无法通过邮件找回密码，就只能初始化 Canvas。

使用 SSH 连接服务器，运行下面的命令后就可以使用：help@websoft9.com/websoft9 登录。

```
export RAILS_ENV=production
export CANVAS_LMS_ADMIN_EMAIL=help@websoft9.com
export CANVAS_LMS_ADMIN_PASSWORD=websoft9
export CANVAS_LMS_ACCOUNT_NAME=admin
export CANVAS_LMS_STATS_COLLECTION=opt_in
cd /data/wwwroot/canvas; bundle exec rake db:initial_setup
```

> 初始化可能会删除历史数据

### 域名绑定

当服务器上只有一个网站时，不做域名绑定也可以访问网站。但从安全和维护考量，**域名绑定**不可省却。

以示例网站为例，域名绑定操作步骤如下：

1. 确保域名解析已经生效  
2. 使用 SFTP 工具登录云服务器
3. 修改 [Apache虚拟机主机配置文件](/维护参考.md#apache)，将其中的 **server_name** 项的值修改为你的域名
   ```text
   <VirtualHost *:80>
   ServerName canvas.example.com
   ...
   </VirtualHost>
   ```
4. 修改域名配置文件：将/data/wwwroot/canvas/config/domain.yml 文件 production 配置节点的 **domain** 项的值修改为你的域名
5. 保存配置文件，重启 [Apache 服务](/维护参考.md#apache)

### SSL/HTTPS

网站完成域名绑定且可以通过HTTP访问之后，方可设置 HTTPS。

Canvas 预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。

> 除了虚拟主机配置文件之外，HTTPS设置无需修改Nginx任何文件

#### 自动部署

如果没有申请证书，只需在服务器中运行一条命令`certbot`便可以启动免费证书**自动**申请和部署

```
sudo certbot
```

#### 手动部署

如果你已经申请了商业证书，只需三个步骤，即可完成HTTPS配置

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件：*/etc/httpd/conf.d/vhost.conf* ，插入**HTTPS 配置段** 到 *server{ }* 中
 ``` text
   #-----HTTPS template start------------
    <VirtualHost *:443>
      ServerName canvas.example.com
      #ServerAlias canvasfiles.example.com
      #ServerAdmin youremail@example.com
      DocumentRoot /data/wwwroot/canvas/public
      ErrorLog /var/log/apache2/canvas_errors.log
      LogLevel warn
      CustomLog /var/log/apache2/canvas_ssl_access.log combined
      SSLEngine on
      BrowserMatch "MSIE [17-9]" ssl-unclean-shutdown
      # the following ssl certificate files are generated for you from the ssl-cert package.
      SSLCertificateFile /data/cert/ssl-cert-snakeoil.pem
      SSLCertificateKeyFile /data/cert/ssl-cert-snakeoil.key
      SetEnv RAILS_ENV production
      <Directory /data/wwwroot/canvas/public>
        Allow from all
        Options -MultiViews
      </Directory>
    </VirtualHost>
   #-----HTTPS template end------------
   ```
3. 如果打算设置 HTTP 自动跳转到 HTTPS，请找到 `<VirtualHost *:80>..</VirtualHost>`中下面的内容，并删除#
    ```
    #RewriteEngine On
    #RewriteCond %{HTTP:X-Forwarded-Proto} !=https
    #RewriteCond %{REQUEST_URI} !^/health_check
    #RewriteRule (.*) https://%{HTTP_HOST}%{REQUEST_URI} [L]
    ```
4. 重启 Apache 服务后生效
   ```
   systemctl restart apache
   ```

#### 专题指南

若参考上面的**快速指南**仍无法成功设置HTTPS访问，请阅读由Websoft9提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

HTTPS专题指南方案包括：HTTPS前置条件、HTTPS 配置段模板、注意事项、详细步骤以及故障诊断等具体方案。

### SMTP

大量用户实践反馈，使用**第三方 SMTP 服务发送邮件**是一种最稳定可靠的方式。  

请勿在服务器上安装sendmail等邮件系统，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，非常不稳定，且不易维护、诊断故障很困难。

下面提供设置 Canvas 发邮件的步骤：

1. 在网易邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.163.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9@163.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过163邮箱后台设置去获取的授权码
   ```
2. 使用 SSH 登录服务器，修改 */data/wwwroot/canvas/config/outgoing_mail.yml* 文件后保存
   ```
   production:
   address: smtp.163.com
   port: 465
   user_name: websoft9@163.com
   password: #wwBJ8
   authentication: plain        # plain, login, or cram_md5
   domain: smtp.163.com
   outgoing_address: websoft9@163.com
   default_name: Instructure Canvas
   ```
   > 以上配置如果不能收到邮件，请尝试将 authentication 改为 login**

3. 给 Canvas [配置域名](#域名绑定)，并确保可以访问

   > 配置域名很重要，否则即使收到邮件，里面的链接也无法打开。如果没有配置 SSL 证书，打开链接时会有安全提示，忽略即可。

4. 重启 Apache 服务
   ```
   systemctl restart apache
   ```

> 很多用户反馈，Canvas部署在中国大陆之外（比如香港）区域，方可成功发出邮件。原因未知。

更多邮箱设置（QQ邮箱，阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)

### PostgreSQL 数据管理

Canvas 预装包中内置 PostgreSQL 及可视化数据库管理工具 `phpPgAdmin` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组9090端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP:9090*，进入phpPgAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin.png)
3. 输入数据库用户名和密码([不知道密码？](#账号密码))
4. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/phppgadmin-gui-websoft9.png)

> 阅读 Websoft9 提供的 [《PostgreSQL教程》](http://support.websoft9.com/docs/postgresql/zh/solution-phppgadmin.html) ，掌握更多的 PostgreSQL 实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等

## 异常处理

#### 浏览器打开IP地址，无法访问 Canvas（白屏没有结果）？

您的服务器对应的安全组 80 端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### Canvas 访问速度很慢？

Canvas 对服务器的配置要求极高，最低配置为2核8G