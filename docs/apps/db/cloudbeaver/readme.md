---
sidebar_position: 1
slug: /cloudbeaver
tags:
  - CloudBeaver
  - 虚拟桌面
  - 数据库可视化管理工具
---

# 快速入门

[CloudBeaver Community](https://github.com/dbeaver/cloudbeaver) 是一个开源的 Web 数据库可视化管理工具，前端基于 TypeScript 和 React 编写，支持 PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, DB2, Firebird, H2, Trino 等数据库。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-demogui-websoft9.png)

## 准备

部署 Websoft9 提供的 CloudBeaver 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 CloudBeaver 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  CloudBeaver，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程

##  CloudBeaver 初始化向导

### 详细步骤

1. 使用本地电脑浏览器访问：*http://域名* 或 *http://服务器公网IP*, 进入初始化页面
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

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。

## CloudBeaver 使用入门

> 需要了解更多 CloudBeaver 的使用，请参考[官方文档](https://cloudbeaver.io/docs/)



## CloudBeaver 常用操作

### 管理 MySQL

下面介绍如何使用 CloudBeaver 管理 MySQL 数据库

##### 准备

提前准备 MySQL 服务并确保 MySQL 的远程访问已开放。  

如果没有 MySQL 服务，请通过 [MySQL 应用](https://apps.websoft9.com/cloudbeaver) 快速部署一个自己的 MySQL 服务。

##### 配置

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

##### 准备

提前准备 PostgreSQL 服务并确保 PostgreSQL 的远程访问已开放。  

若没有 PostgreSQL 服务，请通过 [PostgreSQL 应用](https://apps.websoft9.com/postgresql) 快速部署一个自己的 PostgreSQL 服务。

##### 配置

1. 登录 CloudBeaver 控制台，打开：【Connection】>【Manual】，选择 **PostgreSQL**
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-openconn-websoft9.png)

2. 设置连接信息：主机地址、端口、账号密码（可以勾选是否保存），然后点击【Save】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-connsetting-websoft9.png)

3. 设置信息保存后，使用这个 PostgreSQL 连接，输入数据库的账号和密码
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-conlogin-websoft9.png)

4. 成功连接到 PostgreSQL，可以开始管理工作

### 管理 SQLServer

下面介绍如何使用 CloudBeaver 管理 SQLServer 数据库

##### 准备

提前准备 SQLServer 服务并确保 SQLServer 的远程访问已开放。  

若没有 SQLServer 服务，请通过 [SQLServer 应用](https://apps.websoft9.com/sqlserver) 快速部署一个自己的 SQLServer 服务。

##### 配置

1. 登录 CloudBeaver 控制台，打开：【Connection】>【Manual】，选择 **SQLServer**
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-openconn-websoft9.png)

2. 设置连接信息：主机地址、端口、账号密码（可以勾选是否保存），然后点击【Save】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-connsetting-websoft9.png)

3. 设置信息保存后，使用这个 SQLServer 连接，输入数据库的账号和密码
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-conlogin-websoft9.png)

4. 成功连接到 SQLServer，可以开始管理工作

### 管理 SQLite

下面介绍如何使用 CloudBeaver 管理 SQLite 数据库

##### 准备

提前准备 SQLite 服务并确保 SQLite 的远程访问已开放。  

若没有 SQLite 服务，请通过 [SQLite 应用](https://apps.websoft9.com/sqlite) 快速部署一个自己的 SQLite 服务。

##### 配置

1. 登录 CloudBeaver 控制台，打开：【Connection】>【Manual】，选择 **SQLite**
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-openconn-websoft9.png)

2. 设置连接信息：主机地址、端口、账号密码（可以勾选是否保存），然后点击【Save】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-openconnsqlite-websoft9.png)

3. 设置信息保存后，使用这个 SQLite 连接，输入数据库的账号和密码
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-conlogin-websoft9.png)

4. 成功连接到 SQLite，可以开始管理工作

### 管理 Oracle Database

下面介绍如何使用 CloudBeaver 管理 Oracle 数据库

##### 准备

提前准备 Oracle 服务并确保 Oracle 的远程访问已开放。  

若没有 Oracle 服务，请通过 [Oracle 应用](https://apps.websoft9.com/oracledatabase) 快速部署一个自己的 Oracle 服务。

##### 配置

1. 登录 CloudBeaver 控制台，打开：【Connection】>【Manual】，选择 **Oracle**
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-openconn-websoft9.png)

2. 设置连接信息：主机地址、端口、账号密码（可以勾选是否保存），然后点击【Save】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-connsetting-websoft9.png)

3. 设置信息保存后，使用这个 Oracle 连接，输入数据库的账号和密码
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-conlogin-websoft9.png)

4. 成功连接到 Oracle，可以开始管理工作

### 重置密码

常用的 CloudBeaver 重置密码相关的操作主要有修改密码和找回密码两种类型：

##### 修改密码

1. 登录 CloudBeaver 后台，右上角打开：【Administrator】>【User】，找到所需修改密码的账号对象
  ![CloudBeaver 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-modifypw-websoft9.png)

2. 开始修改密码，点击【Save】后生效

##### 找回密码

如果用户忘记了密码，只能通过[重置 CloudBeaver 容器](./docker#resetcontainer)的方式找回。

### 驱动管理

[Driver managements](https://cloudbeaver.io/docs/Driver-managements/)

### 导出数据

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-exportdata-websoft9.png)

## CloudBeaver 参数

CloudBeaver 应用中包含 Nginx, Docker 等组件，可通过 **[通用参数表](../setup/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 CloudBeaver 运行时所有的 Container：

```bash
CONTAINER ID   IMAGE                        COMMAND             CREATED       STATUS       PORTS                                       NAMES
34baab38d75f   dbeaver/cloudbeaver:latest   "./run-server.sh"   3 hours ago   Up 3 hours   0.0.0.0:8080->8978/tcp, :::8080->8978/tcp   cloudbeaver
```

下面仅列出 CloudBeaver 本身的参数：

### 路径{#path}

* CloudBeaver 配置文件： */data/apps/cloudbeaver/volumes/GlobalConfiguration/.dbeaver/data-sources.json*  

> data-sources.json 存放数据库连接信息

### 端口

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 9090   | CloudBeaver 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |

### 版本

控制台查看

### 服务

```shell
sudo docker start | stop | restart | stats cloudbeaver
```

### 命令行

### API

