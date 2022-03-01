---
sidebar_position: 1
slug: /redmine
tags:
  - Redmine
  - 项目管理
---

# 快速入门

[Redmine](https://www.redmine.org/) 是用RUBY开发的基于WEB的项目管理软件，提供项目管理、WIKI、新闻台等功能，集成版本管理系统GIT、SVN、CVS等等。通过WEB 形式把成员、任务、文档、讨论以及各种形式的资源组织在一起，推动项目的进度。

![Redmine界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-gui-websoft9.jpg)

## 演示

快速了解 Redmine，请查看：[官方演示](http://demo.redmine.org)  

> 使用Redmine官方演示过程中若需要填写个人资料、获取Cookie、显示广告、付费等，这些都是官方行为，由此产生的安全问题以及商业纠纷与我司无关。

在云服务器上部署 Redmine 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 Redmine，请先到 **域名控制台** 完成一个域名解析

## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-getpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

### Redmine

* Redmine 用户名：`admin`  
* Redmine 密  码：存储在您的服务器中的文件中 */credentials/password.txt*  

### MySQL

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器中的文件中 */credentials/password.txt*  


> 需要登录MySQL，请参考 [MySQL可视化管理](#mysql-数据管理)


## Redmine 安装向导

1. 使用本地 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入Redmine主页。

2. 点击【登录】，进入系统（[不知道账号密码？](/zh/stack-accounts.md)）
   ![Redmine 密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-login-websoft9.png)

3. 进入 Redmine 控制台，系统提示修改密码 
   ![Redmine 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-resetpwf-websoft9.png)

4. 打开：【项目】，新建一个项目
   ![Redmine 新建项目](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-createproject-websoft9.png)

5. 通过：【管理】>【配置】>【显示】，设置 Redmine 项目区语言
   ![Redmine 设置语言](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-language-websoft9.png)

6. 通过：【管理】>【配置】>【用户】，设置 Redmine 用户语言（区别于项目区语言）
   ![Redmine SSH key](https://libs.websoft9.com/Websoft9/DocsPicture/en/redmine/redmine-userlanguage-websoft9.png)
   
7. 激活新注册用户：通过【管理】>【用户】，在【状态】选项中选择 已注册用户，然后激活用户，该用户才能登陆。

> 需要了解更多 Redmine 的使用和配置，请参考官方文档：[Redmine guide](https://www.redmine.org/projects/redmine/wiki/Guide)


## Redmine 入门向导

下面以创建一个项目作为范例来介绍 Redmine 的基本使用入门：

1. 登录 Redmine，依次打开：【项目】>【创建项目】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-createproject001-websoft9.png)

2. 填写上面标题和英文缩写，保存
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-createproject002-websoft9.png)

3. 打开项目页面，开始工作
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-createproject003-websoft9.png)

4. [安装插件](/zh/solution-more.md#插件)，增加更多所需的功能


## 常用操作

### 域名绑定

绑定域名的前置条件是：已经完成域名解析（登录域名控制台，增加一个A记录指向服务器公网IP）  

完成域名解析后，从服务器安全和后续维护考量，需要完成**域名绑定**：

Redmine 域名绑定操作步骤：

1. 确保域名解析已经生效  
2. 使用 SFTP 工具登录云服务器
3. 修改 [Nginx虚拟机主机配置文件](/维护参考.md#nginx)，将其中的 **server_name** 项的值修改为你的域名
   ```text
   server
   {
   listen 80;
   server_name rabbitmq.yourdomain.com;  # 此处修改为你的域名
   ...
   }
   ```
4. 保存配置文件，重启 [Nginx 服务](/维护参考.md#nginx-1)

### SSL/HTTPS

网站完成[域名绑定](/zh/solution-more.html#域名绑定)且可以通过HTTP访问之后，方可设置HTTPS。

Redmine预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。

> 除了虚拟主机配置文件之外，HTTPS设置无需修改 Web 服务器的任何其他文件

#### 自动部署

如果没有申请证书，只需在服务器中运行一条命令`sudo certbot`便可以启动免费证书**自动**申请和部署

```
sudo certbot
```

#### 手动部署

如果你已经申请了证书，只需三个步骤，即可完成 HTTPS 配置：

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件：*/etc/nginx/conf.d/default.conf*，插入**HTTPS 配置段** 到 Redmine 的 *server{ }* 中
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
3. 修改 ssl_certificate, ssl_certificate_key 的值，保存
4. 重启 [Nginx 服务](/维护参考.md#nginx-1) 后生效
   ```
   sudo systemctl restart nginx
   ```

#### 专题指南

若参考上面的**快速指南**仍无法成功设置HTTPS访问，请阅读由Websoft9提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

HTTPS专题指南方案包括：HTTPS前置条件、HTTPS 配置段模板、注意事项、详细步骤以及故障诊断等具体方案。

### SMTP

大量用户实践反馈，使用**第三方 SMTP 服务发送邮件**是一种最稳定可靠的方式。  

请勿尝试在服务器上安装sendmail等发邮件方案，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，导致不稳定、不易维护、诊断故障困难。

下面以**QQ企业邮箱**为例，提供设置 Redmine 发邮件的步骤：

1. 在QQ邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.exmail.qq.com
   SMTP port: 465 or 587 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: xxxx@xx.com
   SMTP password: #wwBJ8    //需要注意的是密码中不能包含单引号，否则出错
   ```
2. 通过 SFTP 连接服务器，修改 `configuration.yml` 文件，找到 “production:”, 在 production 下面添加并完善你的 SMTP 参数:  
   ```
    email_delivery: #(前面2个空格）
    delivery_method: :smtp #（前面4个空格）
    smtp_settings: #（前面4个空格）
    address: "SMTPSERVER"	#（前面6个空格）
    port: 587	#（前面6个空格）
    domain: "YouDomain"	#（前面6个空格）
    authentication: :login #（前面6个空格）
    user_name: "YouEmail" #（前面6个空格）
    password: "YouPassword" #（前面6个空格）
    ```
    > 注意缩进/空格,按照规定格式配置，否则redmine报错

3. 重启 Redmine 服务后生效
   ```
   sudo docker restart redmine
   ```

Redmine 官方提供了数十种不同 SMTP 配置方法，请参考官方文档： [Email Configuration](https://www.redmine.org/projects/redmine/wiki/EmailConfiguration)

### 插件管理

通过 Redmine 提供的[插件中心](https://www.redmine.org/plugins)可以扩展它的功能：

#### 安装插件

下面以一个具体的插件为例说明如何安装插件：  

1. 进入[Ajax Redmine Issue Dynamic Edit](https://www.redmine.org/plugins/redmine_issue_dynamic_edit) 插件页面，获取其下载地址

2. 使用 SFTP 登录服务，分别运行如下命令
   ```
   # 进入 Redmine 目录
   cd /data/wwwroot/redmine
   wget https://www.redmine.org/attachments/download/25386/redmine_issue_dynamic_edit.zip
   unzip redmine_issue_dynamic_edit.zip 
   docker cp redmine_issue_dynamic_edit redmine:/usr/src/redmine/plugins
   ```

4. 重启 Redmine 容器服务
   ```
   sudo docker restart redmine
   ```
   
5. 登陆 Redmine 控制台查看插件
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-installplugindy-websoft9.png)

#### 卸载插件

1. 使用 SFTP 删除 /data/wwwroot/redmine/plugins 对应的插件
2. 重启 Redmine 容器生效
   ```
   sudo docker restart redmine
   ```

### 更改数据库

在使用 Redmine 的过程中，如果更换了数据库密码，会导致系统无法访问。

此时，需要通过如下步骤完成数据库更改操作：

1. 使用 SFTP 连接服务器，修改 */data/wwwroot/redmine/docker-compose.yml* 文件中的数据库信息
2. 重新运行 Remine 容器服务
   ```
   cd /data/wwwroot/redmine
   docker-compose up -d
   ```
如果更换数据库（例如：MySQL更换到 PostgreSQL），则需要完成数据库迁移工作。

### LDAP

参考官方文档：https://www.redmine.org/projects/redmine/wiki/RedmineLDAP

### MySQL 数据管理

Remine 预装包中内置 MySQL 及可视化数据库管理工具 `phpMyadmin` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组80端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP:9090*，进入phpMyAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)
3. 输入数据库用户名和密码([不知道密码？](/zh/stack-accounts.md))
4. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

> 阅读Websoft9提供的 [《MySQL教程》](https://support.websoft9.com/docs/mysql/zh/admin-phpmyadmin.html) ，掌握更多的MySQL实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等


## 异常处理

#### 浏览器打开IP地址，无法访问 Redmine（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### Redmine能打开，但总是出现502错误？

Redmine 所需内存最低为2G，若服务器配置较低或并发访问超过服务器计算能力，会出现502错误

#### 本部署包采用的哪个数据库来存储 Redmine 数据？

MySQL

