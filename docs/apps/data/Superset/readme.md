---
sidebar_position: 1
slug: /superset
tags:
  - Superset
  - 大数据分析
  - BI
---

# 快速入门

[Apache Superset](https://superset.apache.org/) 是一个开源的数据探查与可视化平台（曾用名 Panoramix、Caravel ），该工具在可视化、易用性和交互性上非常有特色，用户可以轻松对数据进行可视化分析。Superset 也是一款企业级商业智能 Web 应用程序。

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-dash-websoft9.png)


在云服务器上部署 Superset 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 Superset，请先到 **域名控制台** 完成一个域名解析

## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

### Superset

* 管理员账号: `admin`
* 管理员密码: 存储在您的服务器中的文件中 */credentials/password.txt*  

### PostgreSQL

* 管理员账号：`superset`
* 管理员密码：存储在您的服务器中的文件中 */credentials/password.txt*  

> 需要登录PostgreSQL，请参考 [PostgreSQL 可视化管理](#postgresql-数据管理)

## Superset 安装向导

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入登录页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-login-websoft9.png)

2. 输入账号密码（[不知道账号密码？](#账号密码)），成功登录到 Superset 后台  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-console-websoft9.png)

3. 修改密码：【Superset Admin】>【Profiles】>【Reset my Password】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-resetpw-websoft9.png)

4. 修改语言：通过右上角国旗图标设置你所需的语言 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-setlanguagech-websoft9.png)
   
   > 在0.999及以上的版本中，Superset取消了菜单栏的语言设置，须通过修改配置文件进行语言设置，方法如下:
   > 1. 进入Superset容器：docker exec -it -u root superset_app bash  
   > 2. 安装 vim 编辑器：apt-get update && apt-get install vim 
   > 3. 编辑配置文件：vim superset/config.py  
   > 4. 找到本地化配置项，将值设为 zh ，切换为中文环境：BABEL_DEFAULT_LOCALE = 'zh'  
   > 5. Ctrl + D 退出容器，并重启容器：docker restart superset_app
   > 6. 重新打开Superset，查看中文界面
  

## Superset 入门向导

下面以连接 Superset 从 MySQL 数据源中获取数据进行分析作为范例：

1. 登录后，依次打开：【Data】>【Databases】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-database-websoft9.png)

2. 点击右上角【数据库】，输入要连接的数据地址、端口、库名以及驱动（[参考](https://docs.sqlalchemy.org/en/13/core/engines.html)）  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-connect-websoft9.png)

3. 点击【确认】，追加的数据库显示在列表中
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-connect-websoft9.png)

4. 依次打开菜单栏：【Data】>【Datesets】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-dataset-websoft9.png)

5. 点击追加Datasets，依次选择库、SCHEMA、Table，点击追加
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-selecttable-websoft9.png)

6. 新追加的表已经显示在Datasets一览了
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-datalist-websoft9.png)

> 需要了解更多 Superset 的使用，请参考官方文档：[Superset documentation](https://superset.apache.org/docs/intro)


## 常用操作

### 配置文件

Superset 配置文件 [superset_config.py](https://github.com/apache/superset/blob/master/superset/config.py) 是自定义配置 Superset 功能的主要入口。

### 安装数据库驱动

Superset 支持数十种数据库，但 Superset Docker 镜像默认并没有安装[数据库的驱动](https://superset.apache.org/docs/databases/installing-database-drivers)（连接程序）。  

因此，需要用户进入到容器后手动安装，具体如下：

```
# 进入 Superset 容器，以 root 身份运行命令
docker exec -it --user root superset_app bash

# 范例：安装 MySQL 驱动
pip install mysqlclient

# 范例：安装 PostgreSQL 驱动
pip install psycopg2	
```

更多驱动参考官方[Database dependencies](https://superset.apache.org/docs/databases/installing-database-drivers)

### Superset 连接 SQL Server数据库（Superset connect to MS SQL server database ）

```
# 进入 Superset 容器，以 root 身份运行命令
docker exec -it -u root superset_app bash

# 安装 MSSQL 驱动
pip install pymssql

# 在 SuperSet 中连接 SQLServer Database
#  E.g mssql+pymssql://sa:passwd123@192.168.16.1:1433/test
mssql+pymssql://username:password@server ip:port/database 

```

### 重置密码

常用的 Superset 重置密码相关的操作主要有修改密码和找回密码两种类型：

#### 修改密码

登录 Superset 后台，修改密码：【Settings】>【User】>【Info】

![Superset 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-resetpw-websoft9.png)

#### 找回密码

如果用户忘记了密码，需要通过修改数据库中的数据表的方式找回：

1. 使用 **SSH**连接服务器，运行如下命令连接数据库
   ```
   docker exec -it superset_db psql -U superset
   ```

2. 在**数据库命令模式下**，运行如下的 SQL 语句后，用户 admin 的密码就被设置为`admin123`。
   ```
   update ab_user set password='pbkdf2:sha256:150000$w8vfDHis$b9c8fa353137417946766ed87cf20510da7e1e3a7b79eef37426330abef552bf' where username='admin';
   ```

### 更换 Logo

如果打算用自己的 Logo 更换 Superset 容器中默认的 Logo，具体的步骤如下：

1. 使用 SFTP 上传你的 Logo 到服务器 /data 目录下

2. 将 Logo 更名为 *superset-logo-horiz*

3. 运行下面的命令，更换 Superset 官方默认 Logo
   ```
   docker cp /data/superset-logo-horiz.png superset_app:/app/superset/static/assets/images/superset-logo-horiz.png
   ```

   > superset_app 为 SuperSet 容器名称。

4. 刷新 Superset 后台页面，查看更换效果

### 域名绑定

当服务器上只有一个网站时，不做域名绑定也可以访问网站。但从安全和维护考量，**域名绑定**不可省却。

以示例网站为例，域名绑定操作步骤如下：

1. 确保域名解析已经生效  
2. 使用 SFTP 工具登录云服务器
3. 修改 [Nginx虚拟机主机配置文件](/维护参考.mdd#nginx)，将其中的 **server_name** 项的值修改为你的域名
   ```text
   server
   {
   listen 80;
   server_name www.example.com;  # 此处修改为你的域名
   ...
   }
   ```
4. 保存配置文件，重启 [Nginx 服务](/维护参考.md#nginx-1)

### SSL/HTTPS

网站完成域名绑定且可以通过HTTP访问之后，方可设置HTTPS。

Superset 预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。

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
3. 重启Nginx服务

#### 专题指南

若参考上面的**简易步骤**仍无法成功设置HTTPS访问，请阅读由Websoft9提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

HTTPS专题指南方案包括：HTTPS前置条件、HTTPS 配置段模板、注意事项、详细步骤以及故障诊断等具体方案。

### SMTP

大量用户实践反馈，使用**第三方 SMTP 服务发送邮件**是一种最稳定可靠的方式。  

请勿在服务器上安装sendmail等邮件系统，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，非常不稳定，且不易维护、诊断故障很困难。

下面以**网易邮箱**为例，提供设置 Superset 发邮件的步骤：

1. 在网易邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.163.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9@163.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过163邮箱后台设置去获取的授权码
   ```
2. 编辑 [Superset 配置文件](/zh/stack-components.md#superset)，增加如下的 SMTP 配置段，设置好自己的参数。
   ```
   # smtp server configuration
   EMAIL_NOTIFICATIONS = True  # all the emails are sent using dryrun
   SMTP_HOST = 'smtp.163.com'
   SMTP_STARTTLS = True
   SMTP_SSL = True
   SMTP_USER = 'websoft9@163.com'
   SMTP_PORT = 465
   SMTP_PASSWORD = '#wwBJ8'
   SMTP_MAIL_FROM = 'websoft9@163.com'
   ```

3. 重启 Superset 容器后生效
   ```
   sudo docker restart superset_app
   ```
更多邮箱设置（QQ邮箱，阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)


### PostgreSQL 数据管理

Superset 预装包中内置 PostgreSQL 容器以及可视化管理工具 pgAdmin。  

本部署方案支持如下两种 PostgreSQL 管理方式：

#### 可视化管理

1. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP:9090*，进入 pgAdmin
   ![登录pgAdmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin-loginui-websoft9.png)

2. 输入 pgAdmin 管理员的用户名和密码([查看账号密码](#账号密码))之后，进入控制台
   ![pgAdmin 控制台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin-console-websoft9.png)

3. 在控制台点击【添加服务器】，连接PostgreSQL服务器

4. 设置所需管理的 PostgreSQL 数据库连接信息([不知道密码？](#账号密码)))
  ![设置pgAdmin连接信息](https://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin-setconnection-websoft9.png)

5. 成功连接
  ![pgAdmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin-console-websoft9.png)

#### 命令管理

可以登录容器后使用命令对 PostgreSQL 进行操作。

1. 使用 SSH 登录服务器后，运行`docker ps`命令获取 Name 或 ID

2. 进入 postgresql 容器操作界面

   ```
   docker exec -it superset_db psql -U superset
   ```
3. 接下来可以使用命令操作 PostgreSQL 

> 阅读 Websoft9 提供的 [《PostgreSQL教程》](https://support.websoft9.com/docs/postgresql/zh/) ，掌握更多的 PostgreSQL 实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等


## 异常处理

#### 浏览器打开IP地址，无法访问 Superset（白屏没有结果）？

您的服务器对应的安全组 80 端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### Superset 采用的哪种安装方式？

本项目基于 Docker 安装


