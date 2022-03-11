---
sidebar_position: 2
slug: /postgresql/admin
tags:
  - PostgreSQL
  - Cloud Native Database
---

# 维护参考

## 系统参数

PostgreSQL 预装包包含 PostgreSQL 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

PostgreSQL 安装到 Linux 还是 Windows 系统，对应的路径有很大的差异，请根据实际情况参考：

#### Linux

##### PostgreSQL

PostgreSQL 配置文件: */data/postgresql/config*   
PostgreSQL 数据目录：*/data/postgresql/pgdata*   
PostgreSQL 日志目录: */data/postgresql/log*  

> 以上列出的是通过软连接创建的目录，请通过 `locate pg_hba.conf` 这样的命令查询更多文件路径信息

##### phpPgAdmin 或 pgAdmin on Docker

phpPgAdmin 或 pgAdmin 是采用 Docker 方式来安装的  

> Docker 相关路径请查看我们编写的 [Docker 管理员手册](https://support.websoft9.com/docs/docker/zh/stack-components.html)

#### Windows

暂无

### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令 `netstat -tunlp` 看查看相关端口，下面列出可能要用到的端口：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| TCP | 9090 | 通过 HTTP 访问 phpPgAdmin | 可选 |
| TCP | 5432 | 远程连接PostgreSQL | 可选 |

### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Check all components version
sudo cat /data/logs/install_version.txt

# Linux Version
lsb_release -a

# PostgreSQL version
psql -V

# PostgreSQL Version
docker -v
```

### 服务

使用由 Websoft9 提供的 PostgreSQL 部署方案，可能需要用到的服务如下：

### Linux系统

#### PostgreSQL
```shell
sudo systemctl start postgresql
sudo systemctl restart postgresql
sudo systemctl stop postgresql
sudo systemctl status postgresql
```

#### Docker

```shell
sudo systemctl start docker
sudo systemctl restart docker
sudo systemctl stop docker
sudo systemctl status docker
```

#### pgAdmin

```shell
sudo docker start pgadmin
sudo docker restart pgadmin
sudo docker stop pgadmin
sudo docker stats pgadmin
```


#### phpPgAdmin

```shell
sudo docker start pgadmin
sudo docker restart pgadmin
sudo docker stop pgadmin
sudo docker stats pgadmin
```

### Windows 系统

Windows下的镜像采用操作系统的服务管理功能，来实现 PostgreSQL 的启动、停止和重启操作

## 备份

### 全局自动备份

所有的云平台都提供了全局自动备份功能，基本原理是基于**磁盘快照**：快照是针对于服务器的磁盘来说的，它可以记录磁盘在指定时间点的数据，将其全部备份起来，并可以实现一键恢复。

```
- 备份范围: 将操作系统、运行环境、数据库和应用程序
- 备份效果: 非常好
- 备份频率: 按小时、天、周备份均可
- 恢复方式: 云平台一键恢复
- 技能要求：非常容易
- 自动化：设置策略后全自动备份
```

不同云平台的自动备份方案有一定的差异，详情参考 [云平台备份方案](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

### PostgreSQL应用备份

PostgreSQL上的应用备份有多种[备份方案](https://www.postgresql.org/docs/12/backup.html)，常见包括：

* 使用 pg_dump, pg_dumpall, pgAdmin, phpPgAdmin等工具进行数据库导出（SQL转存）
* 使用 pg_basebackup等工具实现增量备份和基于时间的恢复
* 数据库文件目录直接复制

其中数据库文件目录直接复制等同于服务器快照备份，无需重复再做。

## 恢复

## 升级

### 系统级更新

运行一条更新命令，即可完成系统级更新：

``` shell
#For Ubuntu&Debian
apt update && apt upgrade -y

#For Centos&Redhat
yum update -y
```
> 本部署包已预配置一个用于自动更新的计划任务。如果希望去掉自动更新，请删除对应的Cron

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

此处收集使用 PostgreSQL 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 导入数据库报错？

查看脚本里面是否有创建数据库的脚本

#### 数据库服务无法启动

数据库服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看服务状态和日志
systemctl status postgresql
journalctl -u postgresql
```

#### 运行 psql 命令显示 "cannot be run as root Failure, exiting"？

为了安全考量，默认安装已经创建了一个数据库账号 `postgres`，如果使用 `root` 账号登录，请切换用户后再使用 psql
```
sudo -i -u postgres
```

## 常见问题

#### phpPgAdmin 与 pgAdmin 哪个更好？

pgAdmin

#### pgAdmin 支持多语言吗？

支持数十种语言（包含中文）

#### pgAdmin 是什么类型的客户端？

pgAdmin 是通过浏览器访问的客户端，即使在 Windows 下安装，也是间接调用浏览器来访问的

#### 什么是 PostgreSQL 的 Client 和 Server？

PostgreSQL Server 是指 PostgreSQL 程序本体，而 PostgreSQL Client 指采用TCP协议用于连接程序本地的客户端工具。  

它们是两个完全不同的程序，也就是说它们并需要同时安装到同一台服务上。

#### PostgreSQL 安装后有默认数据库吗？

有，名称为 postgres

#### 是否可以修改 PostgreSQL 根目录？

可以，但不建议修改，除非你需要将数据库整体迁移到数据盘

#### 数据库 postgres 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，采用 Docker 部署的 phpPgAdmin 或 pgAdmin，通过：*http://服务器公网IP:9090* 访问

#### 部署和安装有什么区别？

部署是将一序列软件按照不同顺序，先后安装并配置到服务器的过程，是一个复杂的系统工程。  
安装是将单一的软件拷贝到服务器之后，启动安装向导完成初始化配置的过程。  
安装相对于部署来说更简单一些。 

#### 云平台是什么意思？

云平台指提供云计算服务的平台厂家，例如：Azure,AWS,阿里云,华为云,腾讯云等

#### 实例，云服务器，虚拟机，ECS，EC2，CVM，VM有什么区别？

没有区别，只是不同厂家所采用的专业术语，实际上都是云服务器

#### 推荐一些不错的学习资料？

* [从pg_hba.conf文件谈谈postgresql的连接认证](https://www.cnblogs.com/flying-tiger/p/5983588.html?tdsourcetag=s_pcqq_aiomsg)