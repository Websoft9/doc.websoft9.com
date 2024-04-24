---
title: Redis
slug: /redis
tags:
  - 缓存
  - 数据库
---

import Meta from './_include/redis.md';

<Meta name="meta" />

## 入门指南{#guide}

### 开启身份验证

Redis 提供了身份访问控制 [ACL](https://redis.io/topics/acl) 功能，特别是从 Redis 6.0 之后，这些功能进一步增强。  

身份认证最简单的方式就是开启密码（对于外网访问是必须的）:

1. 编辑 Redis 配置文件，找到如下的配置项

```
# Warning: since Redis is pretty fast an outside user can try up to
# 150k passwords per second against a good box. This means that you should
# use a very strong password otherwise it will be very easy to break.
#
# requirepass foobared
```

2. 将 `# requirepass foobared` 修改为 `requirepass yourpassword`

   > 务必将密码设置成非常复杂的加强密码
   > 本地访问方式，如果关闭密码认证，任然可以连接访问；远程方式必须设置密码才能访问

3. 重启 Redis 服务后生效

### 设置访问绑定

默认情况下，Redis 允许服务器所有网卡的连接。

```
# By default Redis listens for connections from all the network interfaces
# available on the server. It is possible to listen to just one or multiple
# interfaces using the "bind" configuration directive, followed by one or
# more IP addresses.
#
# Examples:
#
# bind 192.168.1.100 10.0.0.1
# bind 127.0.0.1
```

* 如果需要限制所有外部访问，去掉"#"，重启服务。
* 如果要指定某个网卡，自行添加一行绑定项，例如： `bind 192.168.1.100 10.0.0.1`

> 此处的 bind 不是白名单的概念，而是服务器网卡绑定关系。

### 可视化管理

参考：[RedisInsight](./redisinsight.md)

### 持久化设置

Redis 支持 RDB 和 AOF 两种持久化方式：

* RDB：即通过快照技术，将内存中的数据生成一份副本并保存到磁盘指定的目录中；
* AOF：即通过协议文本的方式，将所有对数据库进行过写入的命令（及其参数）记录到 AOF 文件，以此达到记录数据库状态的目的，非常类似 MySQL 的二进制日志


## 配置选项{#configs}

- 实例支持的最多数据库数量：16 个
- 支持哪些数据结构：二进制字符串、列表、集合、哈希、位图、HyperLogLogs、流等
- 配置文件说明：/etc/redis/redis.conf

    | 配置名    | 配置说明                                   |
    | --------- | ------------------------------------------ |
    | port      | 端口                                       |
    | logfile   | 日志文件                                   |
    | dir       | Redis 工作目录（存放持久化文件和日志文件） |
    | daemonize | 是否已守护进程方式启动 Redis（yes 或 no）  |

  Redis 的配置可以通过修改 redis.conf 文件实现，也可以先通过 redis-cli 登录后，在运行 `CONFIG GET *` 命令查看。   

  设置配置项的 **语法格式：**

  redis 127.0.0.1:6379> CONFIG SET CONFIG_SETTING_NAME NEW_CONFIG_VALUE

  下面是设置范例：  

    ```
    127.0.0.1:6379> CONFIG SET loglevel "notice"
    OK
    ```

- [Redis API](https://docs.redis.com/latest/rs/references/rest-api/)
- [redis-cli](https://redis.io/topics/rediscli) 支持交互式模式和标准命令行两种使用方式：

    ```
    # 交互式模式（无密码验证），即进入 CLI 的随时待命状态
    $docker exec -it redis redis-cli
    127.0.0.1:6379>

    # 交互式模式（密码验证），即进入 CLI 的随时待命状态
    $docker exec -it redis  -h 127.0.0.1 -p 6379 -a 123456
    127.0.0.1:6379>

    # 标准命令行模式，即运行一条有明确目标的命令，执行完成后自动退出
    redis-cli help
    redis-cli incr mycounter
    redis-cli --stat
    redis-cli --bigkeys
    ```

    常用命令包括：

    | **Command** | **Description** |
    | --- | --- |
    | redis-benchmark | Performance test |
    | SAVE | Backup Data |
    | CONFIG GET dir | Restore Data |
    | INFO | Manage Redis services |

## 管理维护{#administrator}

### 重置密码

编辑 **Redis 配置文件** 中的参数 `requirepass` 的值即重置密码。
```
# Warning: since Redis is pretty fast an outside user can try up to
# 150k passwords per second against a good box. This means that you should
# use a very strong password otherwise it will be very easy to break.
#
# requirepass foobared

```
### 导出数据

1. docker exec 到 Redis 容器中，使用redis-cli工具运行**SAVE** 命令
  ```shell
  $ sudo docker exec -it redis redis-cli
  127.0.0.1:6379> SAVE
  OK
  ```
2. 备份文件 `dump.rdb` 存放在redis容器的 */var/lib/redis* 目录下


## 故障

#### Can't open PID file /var/run/redis.pid (yet?) after start: No such file or directory

问题：运行命令：sudo systemctl status redis，状态是active，但是下面有段报错信息：Can't open PID file /var/run/redis.pid (yet?) after start: No such file or directory  
原因：Redis自身的服务PID被其他服务占用  
方案：检查自行创建的服务是否占用了默认服务