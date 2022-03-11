---
sidebar_position: 2
slug: /redis/admin
tags:
  - Redis
  - Cloud Native Database
---

# 维护参考

## 系统参数

Redis 预装包包含 Redis 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

#### Redis

Redis 配置文件： */etc/redis.conf*  
Redis 数据目录： */var/lib/redis*  
Redis 日志文件： */var/log/redis/redis.log*  
Redis 默认数据库： *redis*  

#### RedisInsight

RedisInsight 安装目录： */data/redisinsight*  
RedisInsight 日志文件： */data/logs/redisinsight*  
RedisInsight 配置文件： */data/redisinsight/redisinsight.config*  

访问方式：*http://服务器公网IP:8002*  

### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp` 看查看相关端口，下面列出可能要用到的端口：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| Redis | 6379 | 远程访问Redis | 可选 |
| RedisInsight | 8002 | HTTP 访问 RedisInsight  | 可选 |


### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Linux Version
lsb_release -a

# Redis version
redis-server -v
```

### 服务


使用由Websoft9提供的Redis部署方案，可能需要用到的服务如下：

#### Redis

```shell
sudo systemctl start redis
sudo systemctl stop redis
sudo systemctl restart redis
sudo systemctl status redis
```

#### RedisInsight

```shell
sudo systemctl start redisinsight
sudo systemctl stop redisinsight
sudo systemctl restart redisinsight
sudo systemctl status redisinsight
```

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

### 程序手工备份

程序手工本地备份是通过**下载应用程序源码和导出数据库文件**实现最小化的备份方案。

下面以列表的方式介绍这种备份：
```
- 备份范围: 数据库和应用程序
- 备份效果: 一般
- 备份频率: 一周最低1次，备份保留30天
- 恢复方式: 重新导入
- 技能要求：非常容易
- 自动化：无
```
通用的手动备份操作步骤如下：

1. 使用SSH登录服务器，使用redis-cli工具运行**SAVE** 命令
```shell
[root@w9 ~]# redis-cli
127.0.0.1:6379> SAVE
OK
```
2. 备份文件 `dump.rdb` 存放在 */var/lib/redis* 目录下

## 恢复

## 升级

### 系统级更新

运行一条更新命令，即可完成系统级（包含rethinkdb小版本更新）更新：

``` shell
#For Ubuntu&Debian
apt update && apt upgrade -y

#For Centos&Redhat
yum update -y
```
> 本部署包已预配置一个用于自动更新的计划任务。如果希望去掉自动更新，请删除对应的 Cron

### Redis升级

除了 Redis 5.0 以上版本之外，Redis已经是各个发行版的最新版本。

如何更新 Redis 5.0  到 Redis 6.0 ？ 由于 Redis 安装简单，因此大版本的升级，我们建议采用重装的方式

1. 备份 Redis 配置文件
2. 运行下面的命令重装 Redis
   ```
   wget -N https://raw.githubusercontent.com/Websoft9/ansible-linux/main/scripts/install.sh; bash install.sh -r redis
   ```
3. 还原备份配置文件


## 故障处理

此处收集使用 Redis 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 数据库服务无法启动

数据库服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 重启服务
sudo systemctl restart redis

# 查看磁盘空间
df -lh

# 查看内存使用
free -lh
```

#### Can't open PID file /var/run/redis.pid (yet?) after start: No such file or directory

问题：运行命令：sudo systemctl status redis，状态是active，但是下面有段报错信息：Can't open PID file /var/run/redis.pid (yet?) after start: No such file or directory  
原因：Redis自身的服务PID被其他服务占用  
方案：检查自行创建的服务是否占用了默认服务

#### 端口被占用？

如果运行多个 Redis 实例，需保证每个实例的配置文件中的端口不同，否则会导致端口被占用

## 常见问题

#### 什么是Redis客户端？

Redis 客户端是用于与Redis-Server进行通信的程序，例如：redis-cli 就是典型的客户端工具

#### Redis 数据库默认的用户名是？

没有用户名的概念

#### Redis 支持多数据库吗？

单服务器可运行多个 Redis 实例，每个实例有16个数据库(每库类似哈希表)，默认数据库为 db0。

![Redis DataBases](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redis/redis-database-websoft9.png)

> redis-cli 如何切换数据库

```
# Interactive mode (no password verification), immediately entering the standby state of the CLI
[root@iZj6calfqlbdkbj5cxjnf9Z ~]# redis-cli
127.0.0.1:6379>

# Change default database 0 to 1
redis 127.0.0.1:6379> SELECT 1

```

#### Redis社区版 vs Redis企业版

* Redis社区版：兼容开源Redis的高性能数据缓存服务，适用于标准的、无特殊业务需求的Redis使用场景。
* Redis企业版：在Redis社区版的基础上开发的强化版Redis服务，从访问延时、持久化需求、整体成本这三个核心维度考量，基于DRAM、NVM和ESSD云盘等存储介质，推出了多种不同形态的产品，为您提供更强的性能、更多的数据结构和更灵活的存储方式，满足不同场景下的业务需求。

#### Redis Labs 与 Redis 有什么关系？

[Redis Labs](https://redislabs.com/) 是 Redis 的母公司，即 Redis 是 Redis Labs 公司旗下的产品。

#### Redis需要密码才能登录吗？

可以无需设置密码验证，只要外网访问才需要开启数据库密码

#### Redis 支持哪些数据结构？

Redis不是简单的键值存储，它实际上是一个数据结构服务器，支持不同类型的值。包括：二进制字符串、列表、集合、哈希、位图、HyperLogLogs、流等

#### 是否有可视化的数据库管理工具？

部分Redis镜像已经安装 RedisInsight 这个可视化管理工具，如果没有安装，可以自行安装。

#### 是否可以修改Redis的源码路径？

不可以修改