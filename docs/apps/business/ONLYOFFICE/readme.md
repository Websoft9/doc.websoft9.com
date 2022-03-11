---
sidebar_position: 1
slug: /onlyoffice
tags:
  - ONLYOFFICE Workspace
  - 企业管理
  - CRM
---

# 快速入门

[ONLYOFFICE](https://onlyoffice.com) 是一款集成了文档、电子邮件、事件、任务和客户关系管理工具的开源在线办公套件。其文档管理功能实现了文档的在线编辑、在线预览和协同管理，可用于替代Office365或Google docs。另外，它还提供了CRM、项目管理等功能，非常合适作为企业内部的全员协作Office系统。  

ONLYOFFICE 包括三大套件：Community Server, Document Server and Mail Server，各司其职。

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-websoft9-001.png)


在云服务器上部署 ONLYOFFICE 预装包之后，请参考下面的步骤快速入门。
> 关于 ONLYOFFICE Document Server 的安装和使用，请参考 [Document Server](#document-server) 章节。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 ONLYOFFICE，请先到 **域名控制台** 完成一个域名解析


## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

### ONLYOFFICE

初始化安装之时自行设置

### MySQL

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器中的文件中 */credentials/password.txt*  

## ONLYOFFICE 安装向导

1. 使用本地 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入初始化页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-installwait-websoft9.png)

2. 耐心等待 ONLYOFFICE 初始化过程（可能会持续2-5分钟），直至出现如下界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-install-websoft9.png)

3. 设置自己的密码和邮箱（作为登录的用户名），勾选条款后点击【Continue】开始安装
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-bk-websoft9.png)

4. 登录到 ONLYOFFICE 后台，开始使用。  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-websoft9-001.png)

   * **文档管理**
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-websoft9-002.png)

   * **项目管理**
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-websoft9-003.png)

   * **客户关系管理（CRM）**
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-websoft9-004.png)

   * **文档在线编辑（默认可用，无需任何设置）**
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-websoft9-005.png)

   * **社区博客**
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-function-club-websoft9.png)

   * **邮件管理门户**
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-function-email-websoft9.png)

   * **第三方APP集成**
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-function-apps-websoft9.png)

> 需要了解更多 ONLYOFFICE 的使用，请参考官方文档：[ONLYOFFICE Documentation](https://helpcenter.onlyoffice.com/server/docker/opensource/index.aspx)

## 常用操作

### Document Server

本章适合使用了 Websoft9 提供的 ONLYOFFICE Document Server 部署方案（区别于 ONLYOFFICE）。

#### 组件

包含：Nginx, ONLYOFFICE Document Server on Docker, Docker等三个组件。  

Nginx 用于接受用户访问请求，然后转发给 ONLYOFFICE Document Server on Docker。  

组件的详细信息参考 [*参数*](/维护参考.md#系统参数) 章节。

#### 访问

本地浏览器访问：*http://服务器公网IP:9002* 可看到 OnlyOffice Document Server 正在运行的提示。  
![ONLYOFFICE Document Server is running](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-dkisrunning-websoft9.png)

> 如果画面的提示不是*OnlyOffice Document Server is running*，则说明服务运行异常。

#### 域名绑定

完成域名解析后，请针对不同的 Web 服务器下，完成对应的域名绑定操作：

##### Nginx

1. 编辑 **Nginx 虚拟主机配置文件**，增加如下域名绑定代码，保存
    ```
    server {
        listen 80;
        server_name onlyoffice.yourdomain.com;
        location / {
            proxy_pass  http://127.0.0.1:9002;
            proxy_redirect     off;
            proxy_set_header   Host             $host;
            proxy_set_header   X-Real-IP        $remote_addr;
            proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
            #proxy_set_header   X-Forwarded-Proto $scheme;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection upgrade;
            proxy_next_upstream error timeout invalid_header http_500 http_502 http_503 http_504;
            proxy_max_temp_file_size 0;
            proxy_connect_timeout      90;
            proxy_send_timeout         90;
            proxy_read_timeout         90;
            proxy_buffer_size          4k;
            proxy_buffers              4 32k;
            proxy_busy_buffers_size    64k;
            proxy_temp_file_write_size 64k;
    }
    error_log /var/log/nginx/onlyoffice.yourdomain.com-error.log error;
    access_log  /var/log/nginx/onlyoffice.yourdomain.com-access.log;
    }
    ```
2. 重启 Nginx 服务后生效
   ```
   sudo systemctl restart nginx
   ```

##### Apache

当用户使用 nextCloud 等网盘解决方案时，ONLYOFFICE Document Server 已经被包含到部署方案中。  

如果想更安全、更方便的使用 ONLYOFFICE Document Server，需要参考下面的方案配置域名

1. 编辑 **Apache 虚拟主机配置文件**，增加如下域名绑定代码，保存
    ```
    <VirtualHost *:80>
    ProxyPreserveHost On
    ProxyAddHeaders Off
    ServerName onlyoffice.yourdomain.com
    ProxyPass / http://127.0.0.1:9002/
    ProxyPassReverse / http://127.0.0.1:9002/
    </VirtualHost>
    ```
2. 重启 Apache 服务后生效
   ```
   sudo systemctl restart apache
   ```

#### HTTPS 设置

完成域名绑定之后，开始设置 HTTPS：

1. 运行 `sudo certbot` 即可自助设置 [HTTPS](/zh/solution-https.md)

2. 虚拟主机配置文件中增加下面的一行代码，使客户端和代理服务之间的连接所采用的传输协议
   ```
   # 以下适用于 Apache
   RequestHeader set X-Forwarded-Proto "https

   # 以下适用于 Nginx
   proxy_set_header   X-Forwarded-Proto $scheme;
   ```

3. 重启服务后生效

#### 集成

ONLYOFFICE Document Server 支持被 ownCloud, Nextcloud, Seafile 等网盘软件的文档预览与集成。

* [ownCloud 集成 ONLYOFFICE Document Server](http://support.websoft9.com/docs/owncloud/zh/solution-more.html#owncloud-文件预览与编辑)
* [Nextcloud 集成 ONLYOFFICE Document Server](http://support.websoft9.com/docs/nextcloud/zh/solution-more.html#nextcloud-文件预览与编辑)
* [Seafile 集成 ONLYOFFICE Document Server](https://support.websoft9.com/docs/seafile/zh/solution-office.html)

### ONLYOFFICE 文件预览与编辑

由 Websoft9 提供的 ONLYOFFICE 部署方案默认包含 ONLYOFFICE Document Server，并已完成设置，无需任何设置即可在线编辑和预览文档。

下面展现文档预览与编辑的设置原理，仅供后续个性化修改参考：

* 登录到 ONLYOFFICE ，依次打开：【设置】>【集成】>【文件服务】，你可以看到预配置：
  ![ONLYOFFICE 文件服务](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-preview-websoft9.png)

* 本地浏览器访问：*http://服务器公网IP:9002*，会看到 OnlyOffice Document Server 正在运行的提示 
   ![ONLYOFFICE document is running ](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-dkisrunning-websoft9.png)

> 请勿修改默认的文档配置，除非你打算采用其他文档服务替换它

### 域名绑定

绑定域名的前置条件是：已经完成域名解析（登录域名控制台，增加一个A记录指向服务器公网IP）  

完成域名解析后，从服务器安全和后续维护考量，需要完成**域名绑定**：

ONLYOFFICE 域名绑定操作步骤如下：

1. 确保域名解析已经生效  
2. 使用 SFTP 工具登录云服务器
3. 修改 [Nginx虚拟机主机配置文件](/zh/stack-components.md#nginx)，将其中的 **server_name** 项的值修改为你的域名
   ```text
   server
   {
   listen 80;
   server_name onlyoffice.yourdomain.com;  # 此处修改为你的域名
   ...
   }
   ```
4. 保存配置文件，重启 [Nginx 服务](/zh/admin-services.md#nginx)

### SSL/HTTPS

必须完成[域名绑定](/zh/solution-more.md)且可通过 HTTP 访问 ONLYOFFICE ，才可以设置 HTTPS。

ONLYOFFICE 预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。因此，除了虚拟主机配置文件之外，HTTPS 设置则不需要修改 Nginx 其他文件。

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

若参考上面的**快速指南**仍无法成功设置HTTPS访问，请阅读由Websoft9提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

《HTTPS 专题专题》方案包括：HTTPS前置条件、HTTPS 配置段模板、注意事项、详细步骤以及故障诊断等具体方案。


### ONLYOFFICE 设置语言

登录 ONLYOFFICE，在后台 【设置】>【通用】>【自定义】中设置语言

![ONLYOFFICE 设置语言](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-lanuageset-websoft9.png)


### 重置密码

常用的 ONLYOFFICE 重置密码相关的操作主要有修改密码和找回密码两种类型：

#### 修改密码

1. 登录 ONLYOFFICE 后台，依次打开：【Administrator】>【个人资料】，先完成**电子邮件验证**
  ![ONLYOFFICE 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-modifypw001-websoft9.png)

2. 重新回到个人资料页面，点击【Administrator】下的到下角，就会看到修改密码入口
  ![ONLYOFFICE 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-modifypw002-websoft9.png)

#### 找回密码

如果用户忘记了密码，建议通过邮件的方式找回密码：

1. 完成 [SMTP 设置](/zh/solution-smtp.md)

2. 打开 ONLYOFFICE 登录页面，点击【Forgot】开始通过邮件找回密码
  ![ONLYOFFICE 找回密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-forgetpw-websoft9.png)

### SMTP

大量用户实践反馈，使用**第三方 SMTP 服务发送邮件**是一种最稳定可靠的方式。  

请勿在服务器上安装sendmail等邮件系统，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，非常不稳定，且不易维护、诊断故障很困难。

下面以**QQ邮箱**为例，提供设置 ONLYOFFICE 发邮件的步骤：

1. 在网易邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.qq.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9@qq.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过163邮箱后台设置去获取的授权码
   ```

2. 登录 ONLYOFFICE 控制台，依次打开：【设置】>【集成】>【SMTP设置】

3. 准确填写 SMTP 参数
   ![ONLYOFFICE SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-smtp-1-websoft9.png)

   > 【主机登录】与【发件人电邮地址】必须保持一致，否则无法发送邮件。

4. 点击【发送邮件测试】

更多邮箱设置（QQ邮箱，阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)

### MySQL 数据管理

ONLYOFFICE 预装包中内置 MySQL 及可视化数据库管理工具 `phpMyadmin` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组9090端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP:9090*，进入phpMyAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)
3. 输入数据库用户名和密码([不知道密码？](#账号密码))
4. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

> 阅读Websoft9提供的 [《MySQL教程》](https://support.websoft9.com/docs/mysql/zh/admin-phpmyadmin.html) ，掌握更多的MySQL实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等


## 异常处理

#### 浏览器打开IP地址，无法访问 ONLYOFFICE（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### ONLYOFFICE 默认支持文档编辑与预览吗？

默认已经配置好，无需任何设置即可使用

#### 为什么 ONLYOFFICE 这么慢？

ONLYOFFICE 对内存要求比较高，建议最少 8G 内存

#### 本应用是否可以对外提供文档编辑与预览服务？

可以，*http://服务器公网IP:9002* 即服务地址