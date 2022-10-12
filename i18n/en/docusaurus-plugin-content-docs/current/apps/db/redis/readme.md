---
sidebar_position: 1
slug: /redis
tags:
  - Redis
  - Cloud Native Database
---

# Redis Getting Started

[Redis](https://redis.io/) is an open source (BSD licensed), in-memory data structure store, used as a database, cache and message broker. It supports data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs, geospatial indexes with radius queries and streams. Redis has built-in replication, Lua scripting, LRU eviction, transactions and different levels of on-disk persistence, and provides high availability via Redis Sentinel and automatic partitioning with Redis Cluster.  

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redis/redis-gui-websoft9.png)

If you have installed Websoft9 Redis, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:8001,6379** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Redis
4. [Get](./user/credentials) default username and password of Redis

## Redis Initialization

### Steps for you

1. Use **SSH** tool to connect Redis Server

2. Run the following command to view the Redis service, STATUS is running, indicating that the Redis service is normal
   ````
   $ cd /data/apps/redis && sudo docker compose ls
   NAME STATUS CONFIG FILES
   redis running(2) /data/apps/redis/docker-compose.yml

   ````
3. Run the version query command
   ````
   $ sudo docker exec -it redis redis-server -v

   Redis server v=2.8.24 sha=00000000:0 malloc=jemalloc-3.6.0 bits=64 build=ba7fac81f854c786
   ````
4. Run the Redis CLI command
   ````
   $ docker exec -it redis redis-cli
   127.0.0.1:6379>

   //password login
   $ docker exec -it redis redis-cli -h 127.0.0.1 -p 6379 -a <password>
   127.0.0.1:6379>
   ````
   
> More useful Redis guide, please refer to [Redis Documentation](https://redis.io/documentation)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## Redis QuickStart

> To learn more about the use of Redis, please refer to: [Redis Documentation](https://redis.io/documentation)

## Redis Setup

### Redis remote connection{#remote}

Although we don't suggest you access Redis from Internet, but sometime you may need to do this.  

e.g. Using **RedisInsight**.

Then, you need to configure your redis remote by the following steps:

**Set port**

Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:6379** is allowed

**Bind IP**

You should check your [Redis configuration file](#path) the following segment

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
* If you need to restrict all external access, remove the "#" and restart the service.
* If you want to specify a certain network card, add a line of binding items yourself, for example: `bind 192.168.1.100 10.0.0.1`

> The bind here is not a concept of a whitelist, but a binding relationship between server network cards.

**Enable password**

Redis provided Access Control List [ACL](https://redis.io/topics/acl), after Redis 6.0, These features have been enhanced.

Enable password is need for Internet access, the easiest way to authenticate is to set a password:

1. Edit [Redis config file](#path),find the item below

```
# Warning: since Redis is pretty fast an outside user can try up to
# 150k passwords per second against a good box. This means that you should
# use a very strong password otherwise it will be very easy to break.
#
# requirepass foobared
```

2. Set password from `# requirepass foobared` to `requirepass yourpassword`
   > Be sure to set the password whic is a very complex  password
   > For local access mode, if password authentication is turned off, you can still connect to access; for remote access, you must set a password to access

3. After [restart Redis service](#service), it will take effect


### Redis GUI（RedisInsight）{#redisinsight}

We suggest you use the GUI tool **RedisInsight** ([Download](https://redislabs.com/redisinsight/) | [Licence](https://redislabs.com/redis-insight-license-terms)) powered by **Redis Labs** to manage your Redis. It's a web-base GUI which can be installed on Windows, Linux, Mac OS.

RedisInsight is very powerful. It integrates management, monitoring, configuration and analysis, and can even run CLI commands.

**Preconditions**

View [Redis remote connection](#remote), confirm matching the basic condition.

**Steps**

RedisInsight realize the unity of multiple platforms, it have the same steps: 

1. Start RedisInsight, access init page
   * Using local Chrome or Firefox to visit the URL  *https://Internet IP:8002*, open the web RedisInsight
   * Double click RedisInsight icon, open local client RedisInsight

   ![Start RedisInsight](https://libs.websoft9.com/Websoft9/DocsPicture/en/redis/redisinsight-login-websoft9.png)

2. Select 【Connect to a Redis Server】
   ![Select RedisInsight connect way](https://libs.websoft9.com/Websoft9/DocsPicture/en/redis/redisinsight-connect001-websoft9.png)

3. Input connect information 
   ![Login RedisInsight](https://libs.websoft9.com/Websoft9/DocsPicture/en/redis/redisinsight-connect002-websoft9.png)
   
   * HOST：localhost (recommendation) or  Internet IP (Redis open remote)
   * Port：6379
   * Name：redis

4. Connect success
   ![RedisInsight connection](https://libs.websoft9.com/Websoft9/DocsPicture/en/redis/redisinsight-connectss-websoft9.png)

5. RedisInsight has powerful functions, including management, monitoring, configuration and analysis, and can even run cli commands
   ![RedisInsight console](https://libs.websoft9.com/Websoft9/DocsPicture/en/redis/redisinsight-consolegui-websoft9.png)


### Persistence

Redis supports RDB and AOF persistence way:

* RDB：through snapshot technology, a copy of the data in memory is generated and saved to the specified directory on the disk
* AOF：In other words, all commands (and their parameters) that have been written to the database are recorded to the AOF file by means of protocol text, so as to achieve the purpose of recording database status, which is very similar to the binary log of MySQL


### Multiple instances

Redis is a dictionary hash structure storage server, one Redis has 16 dictionary hash(form 0 to 15, default 0), The client can specify which dictionary to store the data in. It is very similar to building a database in a relational database.

Usually, we will start multiple redis instances on one server:

1. Prepare the ports required for the second instance, example for port: 6378

2. Copy redis.conf file, named redis_6378.conf

3. Fill in the configuration item correctly
    | Configuration item    | Configuration description                                   |
    | --------- | ------------------------------------------ |
    | port      | server port                    |
    | logfile   | log files                                   |
    | dir       | Redis work directory |
    | daemonize | Whether it has been started in daemons mode Redis(yes or no)  |

4. Start service
    ```
    redis-server /etc/redis/redis_6378.conf
    ```

 
### Reset Password

Edit [Redis Config](#path) parameter `requirepass` of value, can reset the password
```
# Warning: since Redis is pretty fast an outside user can try up to
# 150k passwords per second against a good box. This means that you should
# use a very strong password otherwise it will be very easy to break.
#
# requirepass foobared
```

### CONFIG

You can configure Redis by modify `redis.conf` file, and run the **CONFIG** command of redis-cli by SSH  

**Get configuration items**

run the command `CONFIG GET *` to list all configuration items

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

run the command: `CONFIG GET CONFIG_SETTING_NAME` to get the specified item

```
127.0.0.1:6379> CONFIG GET loglevel
1) "loglevel"
2) "notice"
```

**Edit configuration item**

You can modify the `redis.conf` file directly or use `CONFIG set` for configuration

**commands Syntax format:**

redis 127.0.0.1:6379> CONFIG SET CONFIG_SETTING_NAME NEW_CONFIG_VALUE

Following is example:  

```
127.0.0.1:6379> CONFIG SET loglevel "notice"
OK
```


## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Redis 

By running `docker ps`, you can view all Containers when Redis is running:

```bash
CONTAINER ID   IMAGE                           COMMAND                  CREATED          STATUS          PORTS                                       NAMES
4635ce332949   redislabs/redisinsight:latest   "bash ./docker-entry…"   33 seconds ago   Up 31 seconds   0.0.0.0:8001->8001/tcp, :::8001->8001/tcp   redis-gui
a232e91f522e   redis:7.0                       "redis-server /etc/r…"   33 seconds ago   Up 31 seconds   0.0.0.0:6379->6379/tcp, :::6379->6379/tcp   redis
```

### Path{#path}

Redis installation directory: */data/apps/redis*
Redis configuration file: */data/apps/redis/src/redis.conf*
Redis data directory: */data/apps/redis/data/redis_data*

### port

| Port Number | Purpose | Necessity |
| ------ | ------------------------------------------ --- | ------ |
| 6379 | Redis | optional |
| 8001 | HTTP access to RedisInsight | Required |


### Version

```shell
docker exec -it redis redis-server -v
````

### Serve

```shell
sudo docker start | stop | restart | stats redis
sudo docker start | stop | restart | stats redis-gui
````

### CLI

[redis-cli](https://redis.io/topics/rediscli)  is the Redis command line interface, a simple program that allows to send commands to Redis, and read the replies sent by the server, directly from the terminal.

Redis CLI supports two usage modes: interactive mode and standard command line:

```
# Interactive mode (no password verification), immediately entering the standby state of the CLI
$docker exec -it redis redis-cli
127.0.0.1:6379>

# Interactive mode (password verification), immediately entering the standby state of the CLI
$docker exec -it redis redis-cli -h 127.0.0.1 -p 6379 -a 123456
127.0.0.1:6379>

# Standard command line mode, that is to run a command with a clear goal and exit automatically after execution
redis-cli help
redis-cli incr mycounter
redis-cli --stat
redis-cli --bigkeys
```
**Command line usage**

| **Command** | **Description** |
| --- | --- |
| redis-benchmark | Performance test |
| SAVE | Backup Data |
| CONFIG GET dir | Restore Data |
| INFO | Manage Redis services |

### API

[REST API](https://docs.redis.com/latest/rs/references/rest-api/)