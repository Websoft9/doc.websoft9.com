---
sidebar_position: 1
slug: /ghost
tags:
  - Ghost
  - CMS
  - 建站系统
  - 博客系统
---

# 快速入门

[Ghost](https://ghost.org) 是一个开源的博客系统，界面简洁、现代、美观，代码优雅。其核心理念是帮助知识创业者以订阅的方式向读者出售知识。系统采用 Node.js 开发，前端和后端完全分离，运行速度非常快。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/ghost/ghostui.jpg)


在云服务器上部署 Ghost 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 Ghost，请先到 **域名控制台** 完成一个域名解析


## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

### Ghost

在初始化安装的时候由用户自行设置

### MySQL

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器指定文件中（ */credentials/password.txt* ）
   ![运行cat命令](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

  建议通过云控制台的命令终端，运行`cat /credentials/password.txt` 获取数据库密码（参上图）

  **注意**：旧版本 Ghost 上，不存在 password.txt 文件，其数据库密码是 `123456`。请在初始化安装之前务必将数据库密码修改成复杂密码，这样有助于提高数据库的安全性。

> 需要登录MySQL，请参考 [MySQL可视化管理](#MySQL-数据管理)

## Ghost 安装向导

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://Internet IP*, 进入前台界面
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/ghost/ghost-bootpage-websoft9.png)

2. 访问网址：*http://域名/ghost* 或 *http://Internet IP/ghost*, 进入后台
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/ghost/ghost-register001-websoft9.png)

3. 开始创建管理员账号，以邮箱地址为用户名，密码不要设置过于简单  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/ghost/ghost-register002-websoft9.png)

4. 使用 SFTP工具连接服务器，修改 [Nginx 虚拟主机](/zh/stack-components.md#nginx)配置文件，绑定域名（如果想采用域名，此步骤必做）
   ```
    listen 80;
    server_name ghost.yourdomain.com;
   ```

5. 使用 SFTP工具连接服务器，修改 [Ghost 配置文件](/zh/stack-components.md#ghost)中的 URL 域名地址（同上）
   ```
   {
   "url": "http://ghost.yourdomain.com",
   "server": {
      "port": 2368,
      "host": "0.0.0.0"
   },
   ```
6. 运行相关命令，重启以下服务后以上设置才生效
   ```
   sudo systemctl restart nginx
   cd /data/wwwroot/ghost && sudo docker-compose up -d && sudo docker restart ghost
   ```

> 需要了解更多 Ghost 的使用，请参考官方文档：[Ghost Documentation](https://docs.ghost.org/docs)

## Ghost 入门向导

Coming soon...

## 常用操作

### 配置

官方提供了很多配置方案，参考：[Tutorials](https://ghost.org/tutorials/) 和 [FAQ](https://ghost.org/faq/)

### 域名绑定

当服务器上只有一个网站时，不做域名绑定也可以访问网站。但从安全和维护考量，**域名绑定**不可省却。

以示例网站为例，域名绑定操作步骤如下：

1. 确保域名解析已经生效  
2. 使用 SFTP工具连接服务器，修改 [Nginx 虚拟主机](/维护参考.md#nginx)配置文件，绑定域名（如果想采用域名，此步骤必做）
   ```
    listen 80;
    server_name ghost.yourdomain.com;
   ```

3. 使用 SFTP工具连接服务器，修改 [Ghost 配置文件](/维护参考.md#ghost)中的 URL 域名地址（同上）
   ```
   {
   "url": "http://ghost.yourdomain.com",
   "server": {
      "port": 2368,
      "host": "0.0.0.0"
   },
   ```
4. 运行相关命令，重启以下服务后以上设置才生效
   ```
   sudo systemctl restart nginx
   cd /data/wwwroot/ghost && sudo docker-compose up -d && sudo docker restart ghost
   ```

### SSL/HTTPS

必须完成[域名绑定](/zh/solution-more.md)且可通过 HTTP 访问 Ghost ，才可以设置 HTTPS。

Ghost 预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。因此，除了虚拟主机配置文件之外，HTTPS 设置则不需要修改 Nginx 其他文件。

#### 自动部署

如果没有申请证书，只需在服务器中运行一条命令`sudo certbot`便可以启动免费证书**自动**申请和部署

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
3. 重启Nginx服务

#### 专题指南

若参考上面的**简易步骤**仍无法成功设置HTTPS访问，请阅读由Websoft9提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

HTTPS专题指南方案包括：HTTPS前置条件、HTTPS 配置段模板、注意事项、详细步骤以及故障诊断等具体方案。

### SMTP

大量用户实践反馈，使用**第三方 SMTP 服务发送邮件**是一种最稳定可靠的方式。  

请勿在服务器上安装sendmail等邮件系统，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，非常不稳定，且不易维护、诊断故障很困难。  

Ghost 以[Nodemailer](https://github.com/nodemailer) 作为邮件发送的模块，并预设 Gmail, QQ, SendGrid 等[二十多种](https://github.com/nodemailer/nodemailer/tree/0.7/#well-known-services-for-smtp)邮箱服务配置。

下面以**QQ邮箱**为例，提供设置 Ghost 发邮件的步骤：

1. 在 QQ 邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.qq.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: 45745412@qq.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过 QQ 邮箱后台设置去获取的授权码
   ```
2. 修改 Ghost 配置文件 mail 相关配置段。特别注意的是 "from" 与 "user" 必须一致，否则邮件无法发送。
   ```
      "mail": {
         "transport": "SMTP",
         "from": "45745412@qq.com",
         "options": {
            "service": "QQ",
            "auth": {
               "user": "45745412@qq.com",
               "pass": "#wwBJ8"
            }
         }
   },
   ```

   也支持详细的 SMTP 设置方案（此时不要 "service": "QQ" 这个配置段）

   ```
      "mail": {
         "transport": "SMTP",
         "from": "norelpy@smtp.websoft9.com",
         "options": {
            "host": "smtp.websoft9.com",
            "port": 465,
            "secureConnection": true,
            "auth": {
               "user": "norelpy@smtp.websoft9.com",
               "pass": "yourpassword****"
            }
         }
   },
   ```

3. 重启 Ghost 容器
   ```
   cd /data/wwwroot/ghost && docker-compose up -d && docker restart ghost
   ```
4. 登录 Ghost 后台，打开：【Manage】>【Staff】，通过【Invite People】 测试邮箱可用性

### 个性化

#### 菜单

Ghost 可以很方便的定义菜单栏：

1. 登录 Ghost，点击左侧菜单栏的【SETTING】>【Design】
  ![Ghost 代码插入](https://libs.websoft9.com/Websoft9/DocsPicture/en/ghost/ghost-setmenus-websoft9.png)

2. 设置所需的网址，点击【Save】保存后即可生效。

#### 主题

Ghost 的主题是网站页面的主要个性化入口。系统默认提供了一个主题，同时也支持用户自己上传主题，实现界面个性化

1. 登录 Ghost，点击左侧菜单栏的【SETTING】>【Design】，下拉到主题设置区域

2. 先点击【Theme Marketplace】找到一款自己喜欢的主题，并下载主题的压缩文件（一般以.zip结尾）
  ![Ghost 设置主题](https://libs.websoft9.com/Websoft9/DocsPicture/en/ghost/ghost-setthemes-websoft9.png)

3. 再点击【Upload a theme】上传主题文件，并【Active】它后生效

上传的主题会保存到服务器：*/data/wwwroot/ghost/content/themes* 目录下，用户可以修改其中的文件，实现主题在代码层面的个性化定制与开发。

#### 多语言

Ghost 的后台不支持中文，但是前台支持中文（需主题中有中文）。

1. 使用 SSH 或 SFTP 工具登录服务，进入到你的主题下 locales 目录

2. 正常情况下，你会看到很多 json 文件，这些就是主题的翻译文件

3. 查看 zh-hans.json 文件，你会看到中文简体的翻译，即此文件代表简体中文

4. 登录到 Ghost 后台，点击左侧菜单栏的【General】，展开【Publication Language】，设置其值为：zh-hans
  ![Ghost 设置语言](https://libs.websoft9.com/Websoft9/DocsPicture/en/ghost/ghost-setzhhans-websoft9.png)

5. 保存后即刻生效

#### 代码嵌入

代码嵌入可以帮助你的 Ghost 网站插入第三方 JavaScript 代码，例如：百度统计、Google Analysis 等。这些代码一旦插入之后，就会针对每一个页面生效。

1. 登录 Ghost，点击左侧菜单栏的【SETTING】>【Code Injection】
  ![Ghost 代码插入](https://libs.websoft9.com/Websoft9/DocsPicture/en/ghost/ghost-codeinjection-websoft9.png)

2. 将所需的代码拷贝到此处后，点击【Save】保存后即可生效。

#### 订阅

Ghost 支持网站向客户以订阅的方式售卖文章，是知识付费创业者的生产力工具。

1. 登录 Ghost，点击左侧菜单栏的【SETTING】>【Labs 】

2. 分别对 Enable members, Connect to Stripe, Subscription pricing 等项进行设置
  ![Ghost 代码插入](https://libs.websoft9.com/Websoft9/DocsPicture/en/ghost/ghost-setsubs-websoft9.png)

### MySQL 数据管理

Ghost 预装包中内置 MySQL 及可视化数据库管理工具 `phpMyadmin` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组80端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP/phpmyadmin*，进入phpMyAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)
3. 输入数据库用户名和密码([不知道密码？](#账号密码))
4. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

> 阅读Websoft9提供的 [《MySQL教程》](https://support.websoft9.com/docs/mysql/zh/admin-phpmyadmin.html) ，掌握更多的MySQL实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等

## 异常处理

#### 浏览器打开IP地址，无法访问 Ghost（白屏没有结果）？

您的服务器对应的安全组 80 端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署方案是采用什么方式部署 Ghost？

采用 Docker 安装 Ghost，数据库存放在服务器的 MySQL 中
