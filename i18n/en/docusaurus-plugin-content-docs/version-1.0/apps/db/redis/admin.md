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
  $ sudo docker exec -it redis redis-cli
  127.0.0.1:6379> SAVE
  OK
  ```
2. You can find the bakcup file `dump.rdb` in the redis container path:  */var/lib/redis*

### Redis Upgrade

Refer to [Redis upgrade](https://docs.redis.com/latest/rs/installing-upgrading/upgrading/)

## Troubleshoot{#troubleshoot}

In addition to the Redis issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### Can't open PID file /var/run/redis.pid (yet?) after start: No such file or directory

Problem: Run the command: sudo systemctl status redis, the status is active, but there is an error message below: Can't open PID file /var/run/redis.pid (yet?) after start: No such file or directory
Reason: Redis's own service PID is occupied by other services
Scenario: Check whether the self-created service occupies the default service

#### Port occupied?

If running multiple Redis instances, make sure that the ports in the configuration files of each instance are different, otherwise the ports will be occupied.

## FAQ{#faq}

#### What is the Redis client?

Redis client is a program used to communicate with Redis-Server, for example: redis-cli is client tool

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
$ sudo docker exec -it redis redis-cli
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

Edit the Redis environment variable file **/data/apps/redis/.env** and modify the value of [APP_GUI_PORT]

#### Can't connect Redis from remote?

1. Check your **[Inbound of Security Group Rule](../administrator/firewall#security)** of Cloud Console to ensure the **TCP:6379** is allowed
2. Check your **Redis configuration file** that Redis allowed from Internet

#### Is there a web version of the visual management tool?

Official visual management tool installed: [RedisInsight](../redis#redisinsight)
