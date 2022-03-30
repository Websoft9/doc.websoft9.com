---
sidebar_position: 3
slug: /postgresql/admin
tags:
  - PostgreSQL
  - Cloud Native Database
---

# 维护参考

## 场景

### 迁移

1. 备份 */data/postgresql/pgdata* 目录下的所有数据
2. 根据不同的操作系统分别设置

   * RedHat/CentOS  修改 **postgreql.service** 文件中数据目录的环境变量
      ```
      # 查看postgresql.service位置
      systemctl cat postgreql.service 

      # 在 postgresql.servce 中找到下面这行，修改之
      Environment=PGDATA=/var/lib/pgsql/11/data/
      ```
   * Ubuntu  修改 **postgresql.conf** 文件中数据目录
     ```
     data_directory =
     ```
3. 恢复数据到新的目录
4. 重启 PostgreSQL 服务

### PostgreSQL应用备份

PostgreSQL上的应用备份有多种[备份方案](https://www.postgresql.org/docs/12/backup.html)，常见包括：

* 使用 pg_dump, pg_dumpall, pgAdmin, phpPgAdmin等工具进行数据库导出（SQL转存）
* 使用 pg_basebackup等工具实现增量备份和基于时间的恢复
* 数据库文件目录直接复制

其中数据库文件目录直接复制等同于服务器快照备份，无需重复再做。

### PostgreSQL 更新升级

PostgreSQL 提供了大版本升级工具 pg_upgrade。升级总是比较复杂，这里只列出 pg_upgrade 常用参数

```
pg_upgrade --help

pg_upgrade upgrades a PostgreSQL cluster to a different major version.

Usage:
  pg_upgrade [OPTION]...

Options:
  -b, --old-bindir=BINDIR       old cluster executable directory
  -B, --new-bindir=BINDIR       new cluster executable directory
  -c, --check                   check clusters only, don't change any data
  -d, --old-datadir=DATADIR     old cluster data directory
  -D, --new-datadir=DATADIR     new cluster data directory
  -j, --jobs=NUM                number of simultaneous processes or threads to use
  -k, --link                    link instead of copying files to new cluster
  -o, --old-options=OPTIONS     old cluster options to pass to the server
  -O, --new-options=OPTIONS     new cluster options to pass to the server
  -p, --old-port=PORT           old cluster port number (default 50432)
  -P, --new-port=PORT           new cluster port number (default 50432)
  -r, --retain                  retain SQL and log files after success
  -U, --username=NAME           cluster superuser (default "root")
  -v, --verbose                 enable verbose internal logging
  -V, --version                 display version information, then exit
  -?, --help                    show this help, then exit

Before running pg_upgrade you must:
  create a new database cluster (using the new version of initdb)
  shutdown the postmaster servicing the old cluster
  shutdown the postmaster servicing the new cluster

When you run pg_upgrade, you must provide the following information:
  the data directory for the old cluster  (-d DATADIR)
  the data directory for the new cluster  (-D DATADIR)
  the "bin" directory for the old version (-b BINDIR)
  the "bin" directory for the new version (-B BINDIR)

For example:
  pg_upgrade -d oldCluster/data -D newCluster/data -b oldCluster/bin -B newCluster/bin
or
  $ export PGDATAOLD=oldCluster/data
  $ export PGDATANEW=newCluster/data
  $ export PGBINOLD=oldCluster/bin
  $ export PGBINNEW=newCluster/bin
  $ pg_upgrade

Report bugs to <pgsql-bugs@postgresql.org>.
```

## 故障处理

除以下列出的 PostgreSQL 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。 

#### 运行 psql 命令显示 "cannot be run as root Failure, exiting"？

为了安全考量，默认安装已经创建了一个数据库账号 `postgres`，如果使用 `root` 账号登录，请切换用户后再使用 psql
```
sudo -i -u postgres
```

## 常见问题

#### 什么是 PostgreSQL 的 Client 和 Server？

PostgreSQL Server 是指 PostgreSQL 程序本体，而 PostgreSQL Client 指采用TCP协议用于连接程序本地的客户端工具。  

它们是两个完全不同的程序，也就是说它们并需要同时安装到同一台服务上。

#### PostgreSQL 有默认数据库吗？

有，名称为 postgres

#### PostgreSQL 支持哪些数据类型？

PostgreSQL 支持官方的数据类型，包括：数据、JASON、JSONB 以及几何类型，还可以使用 SQL 命令创建自定义类型

#### PostgreSQL  C/S 架构组成部分？

PostgreSQL 本身是一个 C/S 架构的程序，即包括客户端程序和服务器程序。

* 客户端程序：psql, clusterdb, pgAdmin等
* 服务器程序：initdb, pg_ctl, postgres, postmaster, pg_upgrade等

#### PostgreSQL 有几种连接方式？

PostgreSQL 允许四种[连接方式](https://www.cnblogs.com/flying-tiger/p/5983588.html?tdsourcetag=s_pcqq_aiomsg)，包括：

* local: 基于 Unix 域套接字的连接方法，域套接字是进程间的一种非网络通信机制，效率高，安全可靠
* host: 基于 TCP/IP 的连接，允许非 SSL 连接，默认值只允许 localhost 本地连接。
* hostssl: 基于 TCP/IP 的 SSL 加密连接
* hostnossl: 基于 TCP/IP 的非 SSL 连接

#### PostgreSQL 有几种认证方法？

PostgreSQL 常见的[认证方法](https://www.postgresql.org/docs/current/auth-methods.html)包括：

* reject: 拒绝某一网段的少数特定主机
* md5: 双种MD5加密
* password: 明文密码
* scram-sha-256: 基于SASL的加密认证，是 PostgreSQL 最安全的认证方式，但不支持 10 以下的版本
* trust： 完全信任
* peer：基于 unix socket 免密连接

#### pgAdmin 支持多语言吗？

支持数十种语言（包含中文）

#### pgAdmin 是什么类型的客户端？

pgAdmin 是通过浏览器访问的客户端，即使在 Windows 下安装，也是间接调用浏览器来访问的