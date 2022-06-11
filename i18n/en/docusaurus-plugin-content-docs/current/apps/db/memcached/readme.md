---
sidebar_position: 1
slug: /memcached
tags:
  - Memcached 
  - Cloud Native Database
---

# Memcached Getting Started

[Memcached](https://www.memcached.org) is a free & open source, high-performance, distributed memory object caching system, generic in nature, but intended for use in speeding up dynamic web applications by alleviating database load.

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/memcached/memcached-gui-websoft9.png)

If you have installed Websoft9 Memcached, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:11211,9090** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Memcached
4. [Get](./user/credentials) default username and password of Memcached

## Memcached Initialization

### Steps for you

1. Use **SSH** tool to connect Memcached Server, then install Telnet
   ```
   yum install telnet
   ```

2. Use the telnet to connect Memcached
   ```
   telnet 127.0.0.1 11211
   Trying 127.0.0.1...
   Connected to 127.0.0.1.
   Escape character is '^]'.
   ```
3. Run the command `stats` to show all Memcached STAT when connection successful
   ```
   STAT pid 651
   STAT uptime 891
   STAT time 1585225158
   STAT version 1.4.15
   STAT libevent 2.0.21-stable
   STAT pointer_size 64
   STAT rusage_user 0.005846
   STAT rusage_system 0.017539
   STAT curr_connections 10
   STAT total_connections 12
   STAT connection_structures 11
   STAT reserved_fds 20
   STAT cmd_get 0
   STAT cmd_set 0
   STAT cmd_flush 0
   STAT cmd_touch 0
   STAT get_hits 0
   STAT get_misses 0
   STAT delete_misses 0
   STAT delete_hits 0
   STAT incr_misses 0
   STAT incr_hits 0
   STAT decr_misses 0
   STAT decr_hits 0
   STAT cas_misses 0
   STAT cas_hits 0
   STAT cas_badval 0
   STAT touch_hits 0
   STAT touch_misses 0
   STAT auth_cmds 0
   STAT auth_errors 0
   STAT bytes_read 52
   STAT bytes_written 21
   STAT limit_maxbytes 67108864
   STAT accepting_conns 1
   STAT listen_disabled_num 0
   STAT threads 4
   STAT conn_yields 0
   STAT hash_power_level 16
   STAT hash_bytes 524288
   STAT hash_is_expanding 0
   STAT bytes 0
   STAT curr_items 0
   STAT total_items 0
   STAT expired_unfetched 0
   STAT evicted_unfetched 0
   STAT evictions 0
   STAT reclaimed 0
   END

   ```
4. Run the command `quit` if you want to exist Memcached

5. Test Memcached Web-based GUI tool [Memcached-admin](#gui)

> More useful Memcached guide, please refer to [Memcached Wiki](https://github.com/memcached/memcached/wiki)


### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

**Can't connect Memcached by Telnet?**

Please make sure you Telnet installed and port **11211** enabled

## Memcached  QuickStart

> 需要了解更多Memcached的使用，请参考：[Memcached Wiki](https://github.com/memcached/memcached/wiki)

## Memcached Setup

### Memcached GUI{#gui}

Memcached deployment package includes Web-GUI tool Memcached-admin for monitor

Follow the steps below to use it:

1. Login Cloud Console, make sure the **TCP:9090** port is allowed on **[Inbound of Security Group Rule](./administrator/firewall#security)**.

2. Use the Chrome or FireFox to access URL *http://Server's Internet IP:9090*.  

3. Enter username and password of MySQL. ([Don't know password?](./user/credentials))  

4. Start to manage Memcached-admin now.  
  ![Memcached-admin](https://libs.websoft9.com/Websoft9/DocsPicture/en/memcached/memcached-gui-websoft9.png)



### Memcached Cluster

More details about refer to [Memcached Cluster](https://github.com/memcached/memcached/wiki/ClusterMaint)



## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Memcached 


通过运行 `docker ps`，可以查看到 Memcached 运行时所有的 Container：

```
CONTAINER ID   IMAGE                                 COMMAND                  CREATED             STATUS             PORTS                                           NAMES
5f7322ff5805   memcached:latest                      "docker-entrypoint.s…"   About an hour ago   Up About an hour   0.0.0.0:11211->11211/tcp, :::11211->11211/tcp   memcached
e4e671827a3e   hatamiarash7/memcached-admin:latest   "docker-php-entrypoi…"   4 minutes ago   Up 4 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp           memcached-admin
```

下面仅列出 Memcached 本身的参数：

### Path{#path}

Memcached 配置文件：*path/.env*  
Memcached-admin 配置文件：*path/.env*  


### Port{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 11211   | 远程访问 Memcached | 可选   |
| 9090  | 通过 Nginx 远程访问 Memcached 可视化工具| 可选   |


### Version

```shell
# Memcached version
docker inspect  memcached | grep MEMCACHED_VERSION
```

### Service

```shell
sudo docker start | stop | restart | stats memcached
sudo docker start | stop | restart | stats memcached-admin
```

### CLI

**Telnet client**

Memcached does not provide specific client. However, standard tools like telnet are enough to test container. Under Linux it is possible to connect by CLI command. We can invoke telnet from host machine, to connect to running Memcached server

1. Use SSH to connect Sever and use Telnet connect Memcached
```
telnet 127.0.0.1 11211
Trying 127.0.0.1...
Connected to 127.0.0.1.
Escape character is '^]'.
```

2. Then, input `stats` command to list all configuration of Memcached

More details please refer to docs: [Memcached Commands](https://github.com/memcached/memcached/wiki/Commands)

**Commandline Arguments**

If you want to configure Memcached Server, you should configure [Commandline Arguments](https://github.com/memcached/memcached/wiki/ConfiguringServer#commandline-arguments) by like below steps:  

1. Use SFTP to connect Server and edit */data/db/memcached/docker-compose.yml* file, add more items for **command** parameter
    ```
    version: '3.8'
    services:
    memcached:
        image: memcached:${APP_VERSION}
        container_name: ${APP_CONTAINER_NAME}
        restart: always
        command:
        - '-m 800'
    ```

2. Recreate containers
   ```
   cd /data/db/memcached
   sudo docker-compose up -d
   ```

### API

