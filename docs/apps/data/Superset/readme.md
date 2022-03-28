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

部署 Websoft9 提供的 Superset 之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网 IP 地址**
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 和 **TCP:9001** 端口是否开启
3. 在服务器中查看 Superset 的 **[默认账号和密码](./setup/credentials#getpw)**
4. 若想用域名访问 Superset，务必先完成**[域名五步设置](./dns#domain)** 过程

## Superset 初始化向导

### 详细步骤

1. 使用本地电脑浏览器访问网址：_http://域名_ 或  *http://服务器公网 IP*, 进入登录页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-login-websoft9.png)

2. 输入账号密码（[不知道账号密码？](./setup/credentials#getpw)），成功登录到 Superset 后台  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-console-websoft9.png)

3. 修改密码：【Superset Admin】>【Profiles】>【Reset my Password】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-resetpw-websoft9.png)

4. 修改语言：通过右上角国旗图标设置你所需的语言
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-setlanguagech-websoft9.png)

   > 在 0.999 及以上的版本中，Superset 取消了菜单栏的语言设置，须通过修改配置文件进行语言设置，方法如下:
   >
   > 1. 进入 Superset 容器：docker exec -it -u root superset_app bash
   > 2. 安装 vim 编辑器：apt-get update && apt-get install vim
   > 3. 编辑配置文件：vim superset/config.py
   > 4. 找到本地化配置项，将值设为 zh ，切换为中文环境：BABEL_DEFAULT_LOCALE = 'zh'
   > 5. Ctrl + D 退出容器，并重启容器：docker restart superset_app
   > 6. 重新打开 Superset，查看中文界面

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或 **[FAQ](./faq#setup)** 尝试快速解决问题：

**Superset 密码正确，但仍然登录失败？**

参阅：[此处](./Superset/admin#loginfail)

## Superset 使用入门

下面以连接 Superset 从 MySQL 数据源中获取数据进行分析作为范例：

1. 登录后，依次打开：【Data】>【Databases】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-database-websoft9.png)

2. 点击右上角【数据库】，输入要连接的数据地址、端口、库名以及驱动（[参考](https://docs.sqlalchemy.org/en/13/core/engines.html)）  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-connect-websoft9.png)

3. 点击【确认】，追加的数据库显示在列表中
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-connect-websoft9.png)

4. 依次打开菜单栏：【Data】>【Datesets】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-dataset-websoft9.png)

5. 点击追加 Datasets，依次选择库、SCHEMA、Table，点击追加
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-selecttable-websoft9.png)

6. 新追加的表已经显示在 Datasets 一览了
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-datalist-websoft9.png)

> 需要了解更多 Superset 的使用，请参考官方文档：[Superset documentation](https://superset.apache.org/docs/intro)

## 常用操作

### Superset 安装数据库驱动

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

### Superset 连接数据库

以 SQL Server 为例：

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

2. 将 Logo 更名为 _superset-logo-horiz_

3. 运行下面的命令，更换 Superset 官方默认 Logo

   ```
   docker cp /data/superset-logo-horiz.png superset_app:/app/superset/static/assets/images/superset-logo-horiz.png
   ```

   > superset_app 为 SuperSet 容器名称。

4. 刷新 Superset 后台页面，查看更换效果

### 配置 SMTP

Superset 配置 SMTP 发邮件的步骤：

1. 在邮箱管理控制台获取 [SMTP](./automation/smtp) 相关参数

2. 修改[Superset 配置文件](#path)，增加如下的 SMTP 配置段，设置好自己的参数。

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

## 参数

Superset 应用中包含 Nginx, Docker, Redis 等组件，可通过 **[通用参数表](../setup/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 Knowage 运行时所有的 Container：

```
CONTAINER ID   IMAGE                           COMMAND                  CREATED              STATUS                                 PORTS                               NAMES
453f04935734   apache/superset:latest          "/usr/bin/docker-ent…"   About a minute ago   Up About a minute (healthy)            0.0.0.0:8088->8088/tcp              superset_app
5477e7693ef3   apache/superset:latest          "/usr/bin/docker-ent…"   About a minute ago   Up About a minute (healthy)            8088/tcp                            superset_worker
d6670fa1bc11   apache/superset:latest          "/usr/bin/docker-ent…"   About a minute ago   Up About a minute (healthy)            8088/tcp                            superset_worker_beat
17689f5d6ebb   postgres:10                     "docker-entrypoint.s…"   About a minute ago   Up About a minute                      0.0.0.0:5432->5432/tcp              superset_db
06bf52f4b856   redis:3.2                       "docker-entrypoint.s…"   About a minute ago   Up About a minute                      127.0.0.1:6379->6379/tcp            superset_cache
```

下面仅列出 Superset 本身的参数：

### 路径{#path}

Superset 源码目录：_/data/wwwroot/superset_  
Superset 数据目录：_/data/wwwroot/superset_home_  
Superset 配置目录：_/data/wwwroot/superset/docker_  
Superset 配置文件：_/data/wwwroot/superset/docker/pythonpath_dev/superset_config.py_

### 端口{#port}

| 端口号 | 用途                                           | 必要性 |
| ------ | ---------------------------------------------- | ------ |
| 9001   | Superset 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |

### 版本

```shell
# Superset Version
docker exec -it superset_app /bin/bash -c 'cat /app/superset-frontend/package.json |grep version'
```

### 服务

```shell
sudo docker  start | stop | restart | status superset_app
sudo docker  start | stop | restart | status superset_worker
sudo docker  start | stop | restart | status superset_worker_beat
sudo docker  start | stop | restart | status superset_db
sudo docker  start | stop | restart | status superset_cache
```

### 命令行

Superset 提供了强大的的命令行工具 `superset`

使用 **SSH** 登录到云服务器，登录到容器后即可使用 CLI

```
# 登录到 Superset 容器
docker exec -it superset_app bash

# 运行 CLI 命令
superset
```

主要参数如下：

```
Usage: superset [OPTIONS] COMMAND [ARGS]...

  This is a management script for the Superset application.

Options:
  --version  Show the flask version
  --help     Show this message and exit.

Commands:
  db                        Perform database migrations.
  export-dashboards         Export dashboards to JSON
  export-datasource-schema  Export datasource YAML schema to stdout
  export-datasources        Export datasources to YAML
  fab                       FAB flask group commands
  flower                    Runs a Celery Flower web server Celery Flower
                            is...

  import-dashboards         Import dashboards from JSON
  import-datasources        Import datasources from YAML
  init                      Inits the Superset application
  load-examples             Loads a set of Slices and Dashboards and a...
  load-test-users           Loads admin, alpha, and gamma user for testing...
  refresh-druid             Refresh druid datasources
  routes                    Show the routes for the app.
  run                       Run a development server.
  set-database-uri          Updates a database connection URI
  shell                     Run a shell in the app context.
  sync-tags                 Rebuilds special tags (owner, type, favorited...
  update-datasources-cache  Refresh sqllab datasources cache
  version                   Prints the current version number
  worker                    Starts a Superset worker for async SQL query...
```

### API

[Superset API](https://superset.apache.org/docs/api) 采用 REST API 2.0 规范。
