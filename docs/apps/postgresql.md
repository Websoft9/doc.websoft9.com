---
title: PostgreSQL
slug: /postgresql
tags:
  - 数据库
  - 关系型
  - SQL
---

import Meta from './_include/postgresql.md';

<Meta name="meta" />

## 入门指南{#guide}

### 连接数据库

docker exec 到容器，即可使用 psql 连接数据库

    ```
    $ psql -d postgresql -U postgresql
    psql (15.0 (Debian 15.0-1.pgdg110+1))
    Type "help" for help.
    
    postgresql=#
    ```

### 图形化工具{#pgadmin}

参考：[pgAdmin](./pgadmin)

### 开启远程访问

PostgreSQL 应用默认已经绑定到宿主机外网端口，只需要确保安全组放通对应的端口即可。  

如果取消了容器与宿主机的端口绑定，而是采用网关的 **Streams** 转发模式，需要确保：

1. postgresql.conf 有配置项 `listen_addresses = '*'`
2. pg_hba.conf 有配置项 `host    all             all             0.0.0.0/0            md5`

## 配置选项{#configs}

##### 默认账号

PostgreSQL 本身并没有固定的管理员账号，但 Websoft9 设置 `postgres` 作为默认账号名称。  

##### 支持的数据类型

PostgreSQL 支持官方的数据类型，包括：数据、JASON、JSONB 以及几何类型，还可以使用 SQL 命令创建自定义类型

##### C/S 架构组成部分

PostgreSQL 本身是一个 C/S 架构的程序，即包括客户端程序和服务器程序。

* 客户端程序：psql, clusterdb, pgAdmin等
* 服务器程序：initdb, pg_ctl, postgres, postmaster, pg_upgrade等

##### 连接方式

PostgreSQL 允许四种[连接方式](https://www.cnblogs.com/flying-tiger/p/5983588.html?tdsourcetag=s_pcqq_aiomsg)，主要包括：

* local: 基于 Unix 域套接字的连接方法，域套接字是进程间的一种非网络通信机制，效率高，安全可靠
* host: 基于 TCP/IP 的连接，允许非 SSL 连接，默认值只允许 localhost 本地连接。
* hostssl: 基于 TCP/IP 的 SSL 加密连接
* hostnossl: 基于 TCP/IP 的非 SSL 连接

##### 认证方法

PostgreSQL 常见的[认证方法](https://www.postgresql.org/docs/current/auth-methods.html)包括：

* reject: 拒绝某一网段的少数特定主机
* md5: 双种MD5加密
* password: 明文密码
* scram-sha-256: 基于SASL的加密认证，是 PostgreSQL 最安全的认证方式，但不支持 10 以下的版本
* trust： 完全信任
* peer：基于 unix socket 免密连接

##### 配置文件

PostgreSQL 有两个重要的全局配置文件：

* postgresql.conf 主要负责配置文件位置、资源限制、集群负责等
* pg_hba.conf 主要负责客户端的连接和认证

##### 命令行

PSQL 是 PostgreSQL 自带的命令行客户端工具，有非常丰富的功能。  

先切换到 postgre 用户，在运行 `psql` 命令，即可使用 psql 连接数据库

```

$ docker exec -it postgresql psql --help
psql is the PostgreSQL interactive terminal.

Usage:
  psql [OPTION]... [DBNAME [USERNAME]]
```

##### API

[PostgreSQL RESTful API](https://www.postgresql.org/about/news/postgresql-restful-api-1616/)


## 管理维护{#administrator}

### 密码管理

对于 PostgreSQL 来说，由于可以通过 Unix 套字节在无需验证的情况下登录数据库，因此修改密码和重置密码操作相同：
  ```
  $ psql -d postgresql -U postgresql

  # 修改密码
  $ ALTER USER postgres WITH PASSWORD 'postgres';

  $ exit psql \q
  ```
### PostgreSQL 备份与恢复

PostgreSQL上的应用备份有多种[备份方案](https://www.postgresql.org/docs/12/backup.html)，常见包括：

* 使用 pg_dump, pg_dumpall, pgAdmin, phpPgAdmin等工具进行数据库导出（SQL转存）
* 使用 pg_basebackup等工具实现增量备份和基于时间的恢复
* 数据库文件目录直接复制


## 故障

#### 运行 psql 命令显示 "cannot be run as root Failure, exiting"？

为了安全考量，默认安装已经创建了一个数据库账号 `postgres`，如果使用 `root` 账号登录，请切换用户后再使用 psql
```
sudo -i -u postgres
```