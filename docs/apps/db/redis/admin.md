---
sidebar_position: 3
slug: /redis/admin
tags:
  - Redis
  - Cloud Native Database
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup) 相关章节。

## 场景

### Redis 备份

1. 使用SSH登录服务器，使用redis-cli工具运行**SAVE** 命令
  ```shell
  $ sudo docker exec -it redis redis-cli
  127.0.0.1:6379> SAVE
  OK
  ```
2. 备份文件 `dump.rdb` 存放在redis容器的 */var/lib/redis* 目录下

### Redis 升级

详细请参照 [Redis 升级](https://docs.redis.com/latest/rs/installing-upgrading/upgrading/)

## 故障排除{#troubleshoot}

除以下列出的 Redis 故障问题之外， [通用故障处理](../troubleshoot) 专题章节提供了更多的故障方案。

#### Can't open PID file /var/run/redis.pid (yet?) after start: No such file or directory

问题：运行命令：sudo systemctl status redis，状态是active，但是下面有段报错信息：Can't open PID file /var/run/redis.pid (yet?) after start: No such file or directory  
原因：Redis自身的服务PID被其他服务占用  
方案：检查自行创建的服务是否占用了默认服务

#### 端口被占用？

如果运行多个 Redis 实例，需保证每个实例的配置文件中的端口不同，否则会导致端口被占用。


## 问题解答

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
$ sudo docker exec -it redis redis-cli
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

#### 修改 RedisInsight 访问端口？

编辑 Redis 环境变量文件 **/data/apps/redis/.env**，修改【APP_GUI_PORT】值即可

#### 远程无法连接 Redis？

请检查服务器对应的安全组6379端口是否开启（入规则），且Redis配置文件中是否允许外部访问

#### 是否提供 Web 版的可视化管理工具？

已安装官方可视化管理工具：[RedisInsight](../redis#redisinsight)

