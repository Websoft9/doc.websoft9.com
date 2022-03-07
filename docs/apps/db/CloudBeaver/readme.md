---
sidebar_position: 1
slug: /cloudbeaver
tags:
  - CloudBeaver
  - 虚拟桌面
  - 数据库可视化管理工具
---

# 快速入门

[CloudBeaver Community](https://github.com/dbeaver/cloudbeaver) 是一个开源的 Web 数据库可视化管理工具，前端基于 TypeScript 和 React 编写，支持 PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, DB2, Firebird, H2, Trino 等数据库

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-demogui-websoft9.png)


在云服务器上部署 CloudBeaver 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 CloudBeaver，请先到 **域名控制台** 完成一个域名解析

## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

### CloudBeaver

初始化时自行设置 

##  CloudBeaver 安装向导

1. 使用本地电脑浏览器访问网址：*http://服务器公网IP*, 进入初始化页面
   ![初始化 CloudBeaver](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-wizard001-websoft9.png)

2. 设置用户名和密码，然后点击【Next】进入下一步
   ![初始化 CloudBeaver](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-wizard002-websoft9.png)

3. 继续点击【Next】进入下一步，最后点击【FINISH】完成初始化
   ![初始化 CloudBeaver](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-wizard003-websoft9.png)

4. 默认已经存在一个 SQlite 的演示连接
   ![初始化 CloudBeaver](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-wizard004-websoft9.png)

5. 通过：【Administrator】>【Connection Management】，删除【SQLite - Chinook (Sample)】，避免遭受 SQL 注入攻击
   ![初始化 CloudBeaver](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-wizard005-websoft9.png)

6. 再回到主页，默认的 SQLite 演示连接已经不存在

> 需要了解更多 CloudBeaver 的使用，请参考[官方文档](https://cloudbeaver.io/docs/)



## 常用操作

### 管理 MySQL

下面介绍如何使用 CloudBeaver 管理 MySQL 数据库

#### 准备

提前准备 MySQL 服务并确保 MySQL 的远程访问已开放。  

如果没有 MySQL 服务，请通过 [MySQL 应用](https://apps.websoft9.com/cloudbeaver) 快速部署一个自己的 MySQL 服务。

#### 配置

1. 登录 CloudBeaver 控制台，打开：【Connection】>【Manual】，选择 **MySQL**
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-conmysql001-websoft9.png)

2. 设置连接信息：主机地址、端口、账号密码（可以勾选是否保存），然后点击【Save】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-conmysql002-websoft9.png)

3. 设置信息保存后，使用这个 MySQL 连接，输入数据库的账号和密码
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-conmysql003-websoft9.png)

4. 成功连接到 MySQL，可以开始管理工作
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-conmysql004-websoft9.png)


### 管理 PostgreSQL

下面介绍如何使用 CloudBeaver 管理 PostgreSQL 数据库

#### 准备

提前准备 PostgreSQL 服务并确保 PostgreSQL 的远程访问已开放。  

若没有 PostgreSQL 服务，请通过 [PostgreSQL 应用](https://apps.websoft9.com/postgresql) 快速部署一个自己的 PostgreSQL 服务。

#### 配置

1. 登录 CloudBeaver 控制台，打开：【Connection】>【Manual】，选择 **PostgreSQL**
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-openconn-websoft9.png)

2. 设置连接信息：主机地址、端口、账号密码（可以勾选是否保存），然后点击【Save】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-connsetting-websoft9.png)

3. 设置信息保存后，使用这个 PostgreSQL 连接，输入数据库的账号和密码
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-conlogin-websoft9.png)

4. 成功连接到 PostgreSQL，可以开始管理工作

### 管理 SQLServer

下面介绍如何使用 CloudBeaver 管理 SQLServer 数据库

## 准备

提前准备 SQLServer 服务并确保 SQLServer 的远程访问已开放。  

若没有 SQLServer 服务，请通过 [SQLServer 应用](https://apps.websoft9.com/sqlserver) 快速部署一个自己的 SQLServer 服务。

#### 配置

1. 登录 CloudBeaver 控制台，打开：【Connection】>【Manual】，选择 **SQLServer**
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-openconn-websoft9.png)

2. 设置连接信息：主机地址、端口、账号密码（可以勾选是否保存），然后点击【Save】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-connsetting-websoft9.png)

3. 设置信息保存后，使用这个 SQLServer 连接，输入数据库的账号和密码
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-conlogin-websoft9.png)

4. 成功连接到 SQLServer，可以开始管理工作

### 管理 SQLite

下面介绍如何使用 CloudBeaver 管理 SQLite 数据库

#### 准备

提前准备 SQLite 服务并确保 SQLite 的远程访问已开放。  

若没有 SQLite 服务，请通过 [SQLite 应用](https://apps.websoft9.com/sqlite) 快速部署一个自己的 SQLite 服务。

#### 配置

1. 登录 CloudBeaver 控制台，打开：【Connection】>【Manual】，选择 **SQLite**
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-openconn-websoft9.png)

2. 设置连接信息：主机地址、端口、账号密码（可以勾选是否保存），然后点击【Save】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-openconnsqlite-websoft9.png)

3. 设置信息保存后，使用这个 SQLite 连接，输入数据库的账号和密码
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-conlogin-websoft9.png)

4. 成功连接到 SQLite，可以开始管理工作

### 管理 Oracle Database

下面介绍如何使用 CloudBeaver 管理 Oracle 数据库

#### 准备

提前准备 Oracle 服务并确保 Oracle 的远程访问已开放。  

若没有 Oracle 服务，请通过 [Oracle 应用](https://apps.websoft9.com/oracledatabase) 快速部署一个自己的 Oracle 服务。

#### 配置

1. 登录 CloudBeaver 控制台，打开：【Connection】>【Manual】，选择 **Oracle**
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-openconn-websoft9.png)

2. 设置连接信息：主机地址、端口、账号密码（可以勾选是否保存），然后点击【Save】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-connsetting-websoft9.png)

3. 设置信息保存后，使用这个 Oracle 连接，输入数据库的账号和密码
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-conlogin-websoft9.png)

4. 成功连接到 Oracle，可以开始管理工作


### 域名绑定

绑定域名的前置条件是：已经完成域名解析（登录域名控制台，增加一个A记录指向服务器公网IP）  

完成域名解析后，从服务器安全和后续维护考量，需要完成**域名绑定**：

CloudBeaver 域名绑定操作步骤：

1. 确保域名解析已经生效  
2. 使用 SFTP 工具登录云服务器
3. 修改 [Nginx虚拟机主机配置文件](/zh/stack-components.md#nginx)，将其中的 **server_name** 项的值修改为你的域名
   ```text
   server
   {
   listen 80;
   server_name cloudbeaver.yourdomain.com;  # 此处修改为你的域名
   ...
   }
   ```
4. 保存配置文件，重启 [Nginx 服务](/zh/admin-services.md#nginx)

### SSL/HTTPS

必须完成[域名绑定](/zh/solution-more.md)且可通过 HTTP 访问 CloudBeaver ，才可以设置 HTTPS。

CloudBeaver 预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。因此，除了虚拟主机配置文件之外，HTTPS 设置则不需要修改 Nginx 其他文件。

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
3. 重启[Nginx服务](/zh/admin-services.md#nginx)

#### 专题指南

若参考上面的**快速指南**仍无法成功设置HTTPS访问，请阅读由Websoft9提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

《HTTPS 专题专题》方案包括：HTTPS前置条件、HTTPS 配置段模板及故障诊断等具体方案。

### 重置密码

常用的 CloudBeaver 重置密码相关的操作主要有修改密码和找回密码两种类型：

#### 修改密码

1. 登录 CloudBeaver 后台，右上角打开：【Administrator】>【User】，找到所需修改密码的账号对象
  ![CloudBeaver 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-modifypw-websoft9.png)

2. 开始修改密码，点击【Save】后生效

#### 找回密码

如果用户忘记了密码，只能通过重置 CloudBeaver 容器的方式找回：

1. 使用 SSH 工具连接  CloudBeaver 服务器

2. 依次运行下面的命令
   ```
   cd /data/apps/cloudbeaver
   docker-compose down -v
   docker-compose pull
   docker-compose up -d
   ```

### 驱动管理

参考官方文档[Driver managements](https://cloudbeaver.io/docs/Driver-managements/)

### 导出数据

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-exportdata-websoft9.png)



## 异常处理

#### 浏览器打开IP地址，无法访问 CloudBeaver（白屏没有结果）？

您的服务器对应的安全组 80 端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 是否可以通过其他端口访问 CloudBeaver？
 
9090，默认 80 端口是通过 Nginx 转发 9090 端口后结果