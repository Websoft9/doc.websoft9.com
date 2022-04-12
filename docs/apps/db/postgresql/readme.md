---
sidebar_position: 1
slug: /postgresql
tags:
  - PostgreSQL
  - Cloud Native Database
---

# 快速入门

[PostgreSQL](https://www.postgresql.org/) 社区志愿者开发的开源关系型数据库系统，它源于 UC Berkeley 大学 1977 年的 Ingres 计划。它稳定可靠，有很多前言的技术特征，并且性能卓越，在数据完整性和正确性方面赢得了良好的市场声誉。


![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin4-websoft9.png)

## 准备

部署 Websoft9 提供的 PostgreSQL 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:5432,9090** 端口已经开启
3. 在服务器中查看 PostgreSQL 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  PostgreSQL，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程


## PostgreSQL 初始化向导

### 详细步骤

部署 PostgreSQL 之后，依次完成下面的步骤，验证其可用性

1. 查看服务状态：SSH 连接服务器，运行下面的命令，查看 PostgreSQL 的安装信息和运行状态
   ```
   sudo systemctl status postgresql
   ```
   PostgreSQL 正常运行会得到 " Active: active (running)... " 的反馈

2. 连接 PostgreSQL：SSH 连接服务器，以 `postgre` 用户后运行 `psql` 命令，即可使用 psql 连接数据库
    ```
    sudo -i -u postgres
    psql

    psql (12.3)
    Type "help" for help.

    postgres=#
    ```

3. 使用可视化管理工具 pgAdmin 

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。

## PostgreSQL 常用操作

### 设置远程访问{#remote}

本地电脑连接 PostgreSQL 时，需设置 PostgreSQL 远程访问：

1. 云控制台安全组开启 **TCP:5432** 端口
2.  修改 [postgresql.conf](#path) 文件
   ```
   #listen_addresses = 'localhost'

   修改为

   listen_addresses = '*'
   ```

3. 修改 [pg_hba.conf](#path) 文件，增加如下一行到文件末尾
   ```
   host    all             all             0.0.0.0/0            md5
   ```

4. 重启 PostgreSQL 后生效
   ```
   sudo systemctl restart postgresql
   ```

### 密码管理

对于 PostgreSQL 来说，由于可以通过 Unix 套字节在无需验证的情况下登录数据库，因此修改密码和重置密码操作相同：

```
# 切换到 postgres 用户
sudo -u postgres psql

# 修改密码
ALTER USER postgres WITH PASSWORD 'postgres';

#exit psql
\q
```

### 图形化工具{#pgadmin}

可以采用 PostreSQL 官方提供的[pgAdmin](https://www.pgadmin.org/) 或[第三方客户端工具](./tools#dbclient)在本地管理数据库。

pgAdmin 支持 Linux, Unix, Mac, Windows 等多种桌面操作系统，它采用**调用浏览器**运行，所以它既是 Web 端，也是客户端。  

本节介绍 pgAdmin 连接和管理数据库等常见操作

#### 登录 pgAdmin

我们的部署方案默认安装了 pgAdmin， 可以直接采用如下方式使用：

1. 本地电脑浏览器访问：*http://服务器公网IP:9090*，进入 pgAdmin
   ![登录pgAdmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin-loginui-websoft9.png)

2. 输入 pgAdmin 管理员的用户名和密码([查看账号密码](./user/credentials))之后，进入控制台
   ![pgAdmin 控制台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin-console-websoft9.png)

#### pgAdmin 客户端

pgAdmin 也支持本地电脑 Windows 客户端：

1. [下载](https://www.pgadmin.org/download/) pgAdmin Windows 版

2. 安装完成后，双击 pgAdmin 图标，会启动默认浏览器中打开 pgAdmin

3. 根据提示，先设置一个 pgAdmin 管理密码
  ![设置pgAdmin管理密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin-setmasterpw-websoft9.png)

#### 连接数据库

登录到 pgAdmin 之后，就可以创建数据库连接来管理 PostgreSQL：

1. 设置所需管理的 PostgreSQL 数据库连接信息([不知道密码？](/zh/stack-accounts.md#postgresql))
  ![设置pgAdmin连接信息](https://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin-setconnection-websoft9.png)

2. 成功连接
  ![phpPgadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin-console-websoft9.png)

#### 创建数据库

1. 鼠标右键一次点击：【Servers】>【Create】>【Database】，创建数据库
  ![pgAdmin 创建数据库](https://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin-createdb-websoft9.png)

2. 设置数据库名称、编码等信息，创建数据库

#### 创建用户

PostgreSQL 中创建用户就是创建 Role

1. 鼠标右键一次点击：【Servers】>【Create】>【Login/Group Role】，创建用户
  ![pgAdmin 创建用户](https://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin-createroles-websoft9.png)

2. 设置用户名称、密码等信息，创建用户

#### 备份数据库

1. 选择需要备份的数据库，点击【Backup】操作
  ![pgAdmin 创建数据库](https://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin-backupdb-websoft9.png)

2. 备份并下载到本地



## 参数

PostgreSQL 应用中包含 Docker, pgAdmin 等组件，可通过 **[通用参数表](../setup/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 PostgreSQL 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```

下面仅列出 PostgreSQL 本身的参数：

### 路径{#path}

PostgreSQL 配置文件目录: */data/postgresql/config*   
PostgreSQL 数据目录：*/data/postgresql/pgdata*   
PostgreSQL 日志目录: */data/postgresql/log*  

PostgreSQL 有两个重要的全局配置文件：

* postgresql.conf 主要负责配置文件位置、资源限制、集群负责等
* pg_hba.conf 主要负责客户端的连接和认证


### 端口

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 9090   | 通过 HTTP 访问 phpPgAdmin	 | 可选   |
| 5432   | 远程连接PostgreSQL | 可选   |


### 版本

```shell
# PostgreSQL version
psql -V
```

### 服务

```shell
sudo systemctl start | stop | restart | status postgresql
sudo docker start | stop | restart | stats pgadmin
```

### 命令行

PSQL 是 PostgreSQL 自带的命令行客户端工具，有非常丰富的功能。  

先切换到 postgre 用户，在运行 `psql` 命令，即可使用 psql 连接数据库

```
sudo -i -u postgres
psql

psql (12.3)
Type "help" for help.

postgres=#
```

### API

[PostgreSQL RESTful API](https://www.postgresql.org/about/news/postgresql-restful-api-1616/)


