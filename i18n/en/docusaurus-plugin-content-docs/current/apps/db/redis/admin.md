---
sidebar_position: 3
slug: /redis/admin
tags:
  - Redis
  - Cloud Native Database
---

# Redis Maintenance

This chapter is special guide for Redis maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### Redis Backup

1. Use SSH to connect Redis server, then run the `SAVE` on redis-cli
```shell
[root@w9 ~]# redis-cli
127.0.0.1:6379> SAVE
OK
```
2. You can find the bakcup file `dump.rdb` in the  */var/lib/redis*

### Redis Upgrade

There's not need to upgrade under the version 5.0.x. 

How upgrade from Redis 5.0 to 6.0? we suggest you install 6.0 to replace 5.0:

1. Backup Redis configuration files

2. Run this shell to reinstall Redis
   ```
   wget -N https://raw.githubusercontent.com/Websoft9/ansible-linux/main/scripts/install.sh; bash install.sh -r redis
   ```
3. Restore backup configuration file

4. Fix the if need


## Troubleshoot{#troubleshoot}

In addition to the Redis issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### Can't open PID file /var/run/redis.pid (yet?) after start: No such file or directory

问题：运行命令：sudo systemctl status redis，状态是active，但是下面有段报错信息：Can't open PID file /var/run/redis.pid (yet?) after start: No such file or directory  
原因：Redis自身的服务PID被其他服务占用  
方案：检查自行创建的服务是否占用了默认服务

#### 端口被占用？

如果运行多个 Redis 实例，需保证每个实例的配置文件中的端口不同，否则会导致端口被占用。


## FAQ{#faq}

#### What is the Redis client?

Redis client is a program used to communicate with Redis-Server, for example: redis-cli is client tool

#### What's relationship between Redis Labs and Redis?

[Redis Labs](https://redislabs.com/) is the parent company of Redis, that is, Redis is a product of Redis Labs.

#### Does Redis need a password to log in?

No password authentication required

#### What is Redis default user？

Redis have not users

#### Redis supports multiple databases？

Multiple redis instances can be run on a server. Each instance has 16 databases, the default is db0.

![Redis DataBases](https://libs.websoft9.com/Websoft9/DocsPicture/en/redis/redis-database-websoft9.png)

> redis-cli how to change database

```
# Interactive mode (no password verification), immediately entering the standby state of the CLI
[root@iZj6calfqlbdkbj5cxjnf9Z ~]# redis-cli
127.0.0.1:6379>

# Change default database 0 to 1
redis 127.0.0.1:6379> SELECT 1

```

#### Redis Communication Version vs Redis Enterprise Version

* Redis Communication Version: High performance data caching service compatible with open source redis, suitable for standard redis usage scenarios without special business requirements.
* Redis Enterprise Version: The Enterprise version of redis service developed on the basis of redis Community Edition has launched a variety of different forms of products based on DRAM, NVM, ESSD cloud disk and other storage media from the three core dimensions of access delay, persistence requirements and overall cost, so as to provide you with stronger performance, more data structures and more flexible storage methods to meet the business requirements in different scenarios.

#### What data structures does Redis support?

Redis is not a plain key-value store, it's data structures server, supporting different [kinds of values](https://redis.io/topics/data-types-intro)

#### Is there a web-GUI tool for Redis?

Yes, installed [RedisInsight](../redis#redisinsight)


#### Is it possible to modify the source path of Redis?

No

#### Modify the RedisInsight access port?

1. Use WinSCP to connect Server
2. Edit [Nginx vhost configuration file](../nginx#virtualHosx)
3. Edit the value of the parameter `listen`
   ```
   server {
    listen 8002;
    server_name _;
    ...
   ```
4. Save it and [Restart Nginx Service](../administrator/parameter#service)

#### Can't connect Redis from remote?

1. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:6379** is allowed
2. Check your **Redis configuration file** that Redis allowed from Internet


