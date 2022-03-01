---
sidebar_position: 1
slug: /redis
tags:
  - Redis
  - Cloud Native Database
---

# 快速入门

[Redis](https://redis.io/) 是一个由Salvatore Sanfilippo写的key-value存储系统。Redis是一个开源的使用ANSI C语言编写、遵守BSD协议、支持网络、可基于内存亦可持久化的日志型、Key-Value数据库，并提供多种语言的API。它通常被称为数据结构服务器，因为值（value）可以是 字符串(String), 哈希(Hash), 列表(list), 集合(sets) 和 有序集合(sorted sets)等类型。  

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redis/redis-gui-websoft9.png)

在云服务器上部署 Redis 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:6379** 和 **TCP:8002**端口是否开启
3. 若想用域名访问 Redis，请先到 **域名控制台** 完成一个域名解析

## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

### Redis

* 管理员账号：*`无`*
* 管理员密码：存储在您的服务器中的文件中 */credentials/password.txt*  

> 通过 [Redis 配置文件](/zh/components.md#redis)的`requirepass`字段设置密码


## Redis 安装向导

1. 通过 SSH 工具连接 Redis服务器

2. 运行 Redis Service 命令
   ```
   ubuntu@redis:~$ sudo systemctl status redis 
   redis.service - redis
   Loaded: loaded (/lib/systemd/system/redis.service; enabled; vendor preset: en
   Active: active (running) since Mon 2020-02-03 10:03:09 UTC; 2h 27min ago
   Process: 31972 ExecStart=/usr/local/bin/redis-server /etc/redis/redis.conf (co
   Main PID: 31973 (redis-server)
   ```
3. 运行版本查询命令
   ```
   ubuntu@redis:~$ sudo redis-server -v
   Redis server v=2.8.24 sha=00000000:0 malloc=jemalloc-3.6.0 bits=64 build=ba7fac81f854c786
   ```
4. 运行 Redis CLI 命令
   ```
   ubuntu@redis:~$ redis-cli
   127.0.0.1:6379>

   //密码登录
   redis-cli -h 127.0.0.1 -p 6379 -a <password>
   127.0.0.1:6379>
   ```
   
5. PHP 连接 redis 读写操作

   ```
   <?php
   
   $redis = new Redis();
   $redis->connect('127.0.0.1', 6379);
   $redis->auth('password');
   $redis->set('Websoft9', 9);
   echo $redis->get('Websoft9'); 

   ?>
   
   ```

> 需要了解更多Redis的使用，请参考：[Redis Documentation](https://redis.io/documentation)

## 常用操作

### 远程访问控制

虽然不建议将 Redis 公开到 Internet 直接访问，但是有些特殊场景下，比如：使用 RedisInsight 客户端，就需要设置 Redis 的远程访问。  

数据库是高安全应用，设置远程访问，最少需三个独立的步骤：

#### 设置安全组

一般来说，Redis使用的是6379端口。  

首先，我们要登录到云控制台，打开云服务器所在的安全组中，保证 **TCP:6379** 端口是开启的。

#### 设置绑定（非必要）

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

#### 开启身份验证

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

### 可视化管理

我们推荐使用官方提供免费可视化管理工具 RedisInsight（[下载](https://redislabs.com/redisinsight/) | [Licence](https://redislabs.com/redis-insight-license-terms)） 。它是一个基于浏览器运行的GUI工具，支持 Windows，Linux和Mac OS系统运行。

#### 前置条件

查看[远程访问控制](/zh/solution-remote.md)文档，确保符合其中描述的条件。

#### 使用

RedisInsight 实现了多平台统一性，只要打开 RedisInsight 界面，使用方式是一模一样的：  

1. 打开 RedisInsight 界面
  
   * 本地浏览器访问：*http://服务器公网IP:8002* ，即可打开服务器上安装的 RedisInsight
   * 启动桌面的 RedisInsight 图标，打开本地安装的 RedisInsight

   ![打开RedisInsight](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redis/redisinsight-login-websoft9.png)

2. 选择【Connect to a Redis Server】
   ![选择RedisInsight连接方式](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redis/redisinsight-connect001-websoft9.png)

3. 输入连接信息（[不知道密码](/zh/stack-accounts.md#redis)）
   ![登录RedisInsight](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redis/redisinsight-connect002-websoft9.png)
   
   * HOST：localhost （推荐） 或 服务器公网IP（Redis已开启远程的状态）
   * Port：6379
   * Name：redis

4. 成功建立一个连接
   ![RedisInsight连接](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redis/redisinsight-connectss-websoft9.png)

5. RedisInsight 的功能十分强大，集管理、监控、配置和分析于一体，甚至还可以运行CLI命令。
   ![RedisInsight后台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redis/redisinsight-consolegui-websoft9.png)

### 持久化

Redis 支持 RDB 和 AOF 两种持久化方式：

* RDB：即通过快照技术，将内存中的数据生成一份副本并保存到磁盘指定的目录中；
* AOF：即通过协议文本的方式，将所有对数据库进行过写入的命令（及其参数）记录到 AOF 文件，以此达到记录数据库状态的目的，非常类似 MySQL 的二进制日志

### 多实例

Redis是一个字典结构的存储服务器，一个 Redis 实例对应多个字典（默认支持16个字典，从0开始编号），客户端可以指定将数据存储在哪个字典中。非常类似在关系数据库中建库。

虽然 Redis 没有多数据库，但通常我们会在一台服务器上启动多个 Redis 实例：

1. 准备好第二个实例所需的端口，假如为：6378

2. 复制现有的 redis.conf 文件，命名为 redis_6378.conf

3. 正确填写配置项
    | 配置名    | 配置说明                                   |
    | --------- | ------------------------------------------ |
    | port      | 端口                                       |
    | logfile   | 日志文件                                   |
    | dir       | Redis 工作目录（存放持久化文件和日志文件） |
    | daemonize | 是否已守护进程方式启动 Redis（yes 或 no）  |

4. 启动服务
    ```
    redis-server /etc/redis/redis_6378.conf
    ```

### 修改 RedisInsight 访问端口

编辑 [Nginx 虚拟主机配置文件](/zh/stack-components.md#nginx) 中的参数 `listen` 的值即重置密码。

```
server {
    listen 8002;
    server_name example.yourdomain.com;
```
 
### 重置密码

编辑 [Redis 配置文件](/zh/stack-components.md#redis) 中的参数 `requirepass` 的值即重置密码。
```
# Warning: since Redis is pretty fast an outside user can try up to
# 150k passwords per second against a good box. This means that you should
# use a very strong password otherwise it will be very easy to break.
#
# requirepass foobared
```
### 系统配置

Redis 的配置可以通过修改 redis.conf 文件实现，也可以先通过 redis-cli 登录后，在运行 **CONFIG** 命令查看或设置配置项。  

**CONFIG** 可以查询配置项，也可以编辑配置项：

#### 查询配置项

Redis CONFIG 命令格式范例如下： 

通过运行：`CONFIG GET *` 命令，查询所有配置项

```
  127.0.0.1:6379> CONFIG GET *
  1) "dbfilename"
  2) "dump.rdb"
  3) "requirepass"
  4) ""
  5) "masterauth"
  6) ""
  7) "unixsocket"
  8) ""
  9) "logfile"
 10) "/var/log/redis.log"
 11) "pidfile"
 12) "/var/run/redis.pid"
 13) "maxmemory"
 14) "0"
 15) "maxmemory-samples"
 16) "3"
 17) "timeout"
 18) "0"
 19) "tcp-keepalive"
 20) "0"
 21) "auto-aof-rewrite-percentage"
 22) "100"
 23) "auto-aof-rewrite-min-size"
 24) "67108864"
 25) "hash-max-ziplist-entries"
 26) "512"
 27) "hash-max-ziplist-value"
 28) "64"
 29) "list-max-ziplist-entries"
 30) "512"
 31) "list-max-ziplist-value"
 32) "64"
 33) "set-max-intset-entries"
 34) "512"
 35) "zset-max-ziplist-entries"
 36) "128"
 37) "zset-max-ziplist-value"
 38) "64"
 39) "hll-sparse-max-bytes"
 40) "3000"
 41) "lua-time-limit"
 42) "5000"
 43) "slowlog-log-slower-than"
 44) "10000"
 45) "latency-monitor-threshold"
 46) "0"
 47) "slowlog-max-len"
 48) "128"
 49) "port"
 50) "6379"
 51) "tcp-backlog"
 52) "511"
 53) "databases"
 54) "16"
 55) "repl-ping-slave-period"
 56) "10"
 57) "repl-timeout"
 58) "60"
 59) "repl-backlog-size"
 60) "1048576"
 61) "repl-backlog-ttl"
 62) "3600"
 63) "maxclients"
 64) "10000"
 65) "watchdog-period"
 66) "0"
 67) "slave-priority"
 68) "100"
 69) "min-slaves-to-write"
 70) "0"
 71) "min-slaves-max-lag"
 72) "10"
 73) "hz"
 74) "10"
 75) "repl-diskless-sync-delay"
 76) "5"
 77) "no-appendfsync-on-rewrite"
 78) "no"
 79) "slave-serve-stale-data"
 80) "yes"
 81) "slave-read-only"
 82) "yes"
 83) "stop-writes-on-bgsave-error"
 84) "yes"
 85) "daemonize"
 86) "yes"
 87) "rdbcompression"
 88) "yes"
 89) "rdbchecksum"
 90) "yes"
 91) "activerehashing"
 92) "yes"
 93) "repl-disable-tcp-nodelay"
 94) "no"
 95) "repl-diskless-sync"
 96) "no"
 97) "aof-rewrite-incremental-fsync"
 98) "yes"
 99) "aof-load-truncated"
100) "yes"
101) "appendonly"
102) "no"
103) "dir"
104) "/data/redis"
105) "maxmemory-policy"
106) "volatile-lru"
107) "appendfsync"
108) "everysec"
109) "save"
110) "900 1 300 10 60 10000"
111) "loglevel"
112) "notice"
113) "client-output-buffer-limit"
114) "normal 0 0 0 slave 268435456 67108864 60 pubsub 33554432 8388608 60"
115) "unixsocketperm"
116) "0"
117) "slaveof"
118) ""
119) "notify-keyspace-events"
120) ""
121) "bind"
122) ""
```

通过运行：`CONFIG GET CONFIG_SETTING_NAME` 命令，查询指定项

```
127.0.0.1:6379> CONFIG GET loglevel
1) "loglevel"
2) "notice"
```
#### 编辑配置项

你可以通过修改 `redis.conf` 文件或使用 CONFIG set 命令来修改配置。

**语法格式：**

redis 127.0.0.1:6379> CONFIG SET CONFIG_SETTING_NAME NEW_CONFIG_VALUE

下面是设置范例：  

```
127.0.0.1:6379> CONFIG SET loglevel "notice"
OK
```

## 异常处理

#### 远程无法连接 Redis？

请检查服务器对应的安全组6379端口是否开启（入规则），且Redis配置文件中是否允许外部访问

#### 本部署是否提供 Web 版的可视化管理工具？

已安装官方可视化管理工具：[RedisInsight](/zh/solution-gui.md)