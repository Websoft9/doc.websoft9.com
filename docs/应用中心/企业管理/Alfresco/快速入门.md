---
sidebar_position: 1
slug: /alfresco
tags:
  - Alfresco
  - 企业管理
  - ERP
---

# 快速入门

[Alfresco Community Edition](https://www.alfresco.com/ecm-software/alfresco-community-editions) 是开源的企业内容管理系统，它面向大中型客户，作为一个灵活、可扩展的 ECM 平台，Alfresco Content Services 支持一系列用例，包括内容服务、信息治理、上下文搜索和洞察力，与领先业务应用程序 SAP, IBM Lotus, Microsoft Office, SharePoint 和 Google Docs 等轻松集成。

![Alfresco 系统架构](https://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-arcgui-websoft9.png)


在云服务器上部署 Alfresco 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 Alfresco，请先到 **域名控制台** 完成一个域名解析

## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

## Alfresco

* 管理员账号: `admin`
* 管理员密码: `admin` 或 存储在您的服务器中的文件中 */credentials/password.txt*  

### PostgreSQL

* 管理员账号：*`alfresco`*
* 管理员密码：存储在您的服务器中的文件中 */credentials/password.txt*  

### pgAdmin

* 管理员账号：*`user@domain.com`*
* 管理员密码：存储在您的服务器中的文件中 */credentials/password.txt*  

## Alfresco 安装向导

1. 使用本地电脑的浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入登陆界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-login-websoft9.png)

2. 输入账号密码（[不知道账号密码？](#账号密码)），成功登录到 Alfresco 后台  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-consolegui-websoft9.png)

3. Alfresco会自动根据浏览器语言来选择程序语言

> 需要了解更多 Alfresco 的使用，请参考官方文档：[Alfresco Documentation](https://docs.alfresco.com/content-services/community/using/content/) 和 [Alfresco Videos](https://docs.alfresco.com/content-services/latest/tutorial/video/)

## Alfresco 入门向导

现在开始针对于如何使用 Alfresco 传输数据，进行完整的说明：

- 后台仪表盘
  ![Alfresco台仪表盘](http://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-adminui-websoft9.png)

- 我的文档
  ![Alfresco我的文档](http://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-mydocs-websoft9.png)

- 共享文档
  ![Alfresco共享文档](http://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-sharedocs-websoft9.png)

- 增加多用户
  ![Alfresco增加多用户](http://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-addusers-websoft9.png)

- 增加组（部门）
  ![Alfresco增加组（部门）](http://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-addgroup-websoft9.png)

- 工作流（审批）
  ![Alfresco工作流（审批）](http://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-workflow-websoft9.png)



## 常用操作

### 域名绑定

绑定域名的前置条件是：已经完成域名解析（登录域名控制台，增加一个A记录指向服务器公网IP）  

完成域名解析后，从服务器安全和后续维护考量，需要完成**域名绑定**：

Alfresco 域名绑定操作步骤：

1. 确保域名解析已经生效  
2. 使用 SFTP 工具登录云服务器
3. 修改 [Nginx虚拟机主机配置文件](/维护参考.md#nginx)，将其中的 **server_name** 项的值修改为你的域名
   ```text
   server
   {
   listen 80;
   server_name alfresco.yourdomain.com;  # 此处修改为你的域名
   ...
   }
   ```
4. 保存配置文件，重启 [Nginx 服务](/维护参考.md#nginx-1)

### SSL/HTTPS

必须完成[域名绑定](#域名绑定)且可通过 HTTP 访问 Alfresco ，才可以设置 HTTPS。

Alfresco 预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。因此，除了虚拟主机配置文件之外，HTTPS 设置则不需要修改 Nginx 其他文件。

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
3. 重启[Nginx服务](/维护参考.md#nginx-1)

#### 专题指南

若参考上面的**快速指南**仍无法成功设置HTTPS访问，请阅读由Websoft9提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

《HTTPS 专题专题》方案包括：HTTPS前置条件、HTTPS 配置段模板及故障诊断等具体方案。

### SMTP

大量用户实践反馈，使用**第三方 SMTP 服务发送邮件**是一种最稳定可靠的方式。  

请勿在服务器上安装sendmail等邮件系统，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，非常不稳定，且不易维护、诊断故障很困难。

下面以**网易邮箱**为例，提供设置 Alfresco 发邮件的步骤：

1. 在网易邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.163.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9@163.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过163邮箱后台设置去获取的授权码
   ```
2. 登录 Alfresco 控制台，设置 SMTP 参数（暂未找到具体方案）


更多邮箱设置（QQ邮箱，阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)


### 重置密码

常用的 Alfresco 重置密码相关的操作主要有修改密码和找回密码两种类型：

#### 修改密码

1. 登录 Alfresco 后台，右上角依次打开：【Administrator】>【我的个人档案】
  ![Alfresco 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-modifypw-websoft9.png)

2. 点击【更改密码】，开始修改密码

#### 找回密码

如果用户忘记了密码，需要通过修改[数据库](#postgresql-数据库管理)中的密码信息来重置密码：

1. 使用 **SSH** 连接到 Alfresco 所在的服务器

2. 进入到 alfresco 数据库的 PSQL 交互式状态
   ```
   docker exec -it alfresco-postgres psql -U alfresco -d alfresco
   ```

3. 运行如下的修改密码命令（新的密码为 **admin**）
   ```
   UPDATE alf_node_properties SET string_value='209c6174da490caeb422f3fa5a7ae634' WHERE node_id=4 and qname_id=10
   ```

4. 退出容器交互式模式，回到服务器命令行中重启所有容器后生效
   ```
   cd /data/wwwroot/alfresco
   docker-compose restart
   ```

### PostgreSQL 数据库管理

Superset 预装包中内置 PostgreSQL 容器以及可视化管理工具 pgAdmin。  

本部署方案支持如下两种 PostgreSQL 管理方式：

#### 可视化管理

1. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP:9090*，进入 pgAdmin
   ![登录pgAdmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin-loginui-websoft9.png)

2. 输入 pgAdmin 管理员的用户名和密码([查看账号密码](/zh/stack-accounts.md#postgresql))之后，进入控制台
   ![pgAdmin 控制台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin-console-websoft9.png)

3. 在控制台点击【添加服务器】，连接PostgreSQL服务器

4. 设置所需管理的 PostgreSQL 数据库连接信息([不知道密码？](/zh/stack-accounts.md#postgresql))
  ![设置pgAdmin连接信息](https://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin-setconnection-websoft9.png)

5. 成功连接
  ![pgAdmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin-console-websoft9.png)

#### 命令管理

可以登录容器后使用命令对 PostgreSQL 进行操作。

1. 使用 SSH 登录服务器后，运行 `docker ps` 命令获取 Name 或 ID

2. 进入 postgresql 容器操作界面

   ```
   docker exec -it alfresco-postgres psql -U alfresco -d alfresco
   ```
3. 接下来可以使用命令操作 PostgreSQL 

> 阅读 Websoft9 提供的 [《PostgreSQL教程》](https://support.websoft9.com/docs/postgresql/zh/) ，掌握更多的 PostgreSQL 实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等

### 文档管理

## 异常处理

#### 浏览器打开IP地址，无法访问 Alfresco（白屏没有结果）？

您的服务器对应的安全组 80 端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容。  

实际上，Alfresco 服务默认绑定在 8080 端口，即也可通过：*http://服务器公网IP:8080* 访问它

#### Alfresco 服务启动失败？

Alfresco 开机启动最少需要 10 分钟，请耐心等待

#### 本方案中 Alfresco 采用哪种安装方式？

Docker 安装
