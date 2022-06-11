---
sidebar_position: 3
slug: /postgresql/admin
tags:
  - PostgreSQL
  - Cloud Native Database
---

# PostgreSQL Maintenance

This chapter is special guide for PostgreSQL maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### Change PGDATA Directory

1. Backup all files on you PGDATA */data/postgresql/pgdata* 
2. Change the PGDATA directory by different Linux distribution

   * RedHat/CentOS: modify the file **postgreql.service** 
      ```
      # cat postgresql.service directory
      systemctl cat postgreql.service 

      # modify the  Environment=PGDATA in the file postgresql.servce
      Environment=PGDATA=/var/lib/pgsql/11/data/
      ```
   * Ubuntu: modify the file **postgresql.conf** 
     ```
     data_directory =
     ```
3. Restore all data from your backup
4. Restart your PostgreSQL service

### PostgreSQL Backup for application

There three main methods for PostgreSQL backup: 

* User **pg_dump, pg_dumpall, pgAdmin, phpPgAdmin** to export databse(SQL dump)
* Use **pg_basebackup** for incremental backup and time-based recovery
* Database files copy and download directly

Database files copy is same with **snapshot backup** on your Cloud platform  

Get more details about backup, please refer to PostgreSQL official docs [PostgreSQL Backup](https://www.postgresql.org/docs/12/backup.html)

### PostgreSQL Upgrade

PostgreSQL provides a major version upgrade tool **pg_upgrade**. Upgrading is always more complicated, only the common parameters of **pg_upgrade** are listed here

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

## Troubleshoot{#troubleshoot}

In addition to the PostgreSQL issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### The error "cannot be run as root Failure, exiting" when running the command `psql`?

For the security, the user **postgres** has been created in the process of installation, if you want to use the customer tool (e.g psql, pg_upgrade) on your PostgreSQL server, you should change the user first

```
sudo -i -u postgres
```

## FAQ{#faq}

#### pgAdmin support multiply languages?

Yes

#### What type of client is pgAdmin?

pgAdmin is a web based client, even if installed under Windows, it is accessed indirectly by calling the browser

#### What are the Client and Server of PostgreSQL?

PostgreSQL Server refers to the PostgreSQL program ontology, and PostgreSQL Client refers to the client that uses TCP protocol to connect to the program local. They are two completely different programs, which means that they do not need to be installed on the same service at the same time.

#### What is the default database when completed the PostgreSQL deployment?

postgres

#### PostgreSQL 支持哪些数据类型？

PostgreSQL 支持官方的数据类型，包括：数据、JASON、JSONB 以及几何类型，还可以使用 SQL 命令创建自定义类型

#### PostgreSQL  C/S 架构组成部分？

PostgreSQL 本身是一个 C/S 架构的程序，即包括客户端程序和服务器程序。

* 客户端程序：psql, clusterdb, pgAdmin等
* 服务器程序：initdb, pg_ctl, postgres, postmaster, pg_upgrade等

#### PostgreSQL 有几种连接方式？

PostgreSQL 允许四种[连接方式](https://www.cnblogs.com/flying-tiger/p/5983588.html?tdsourcetag=s_pcqq_aiomsg)，主要包括：

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

