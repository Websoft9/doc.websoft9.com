---
sidebar_position: 1
slug: /memcached
tags:
  - Memcached 
  - Cloud Native Database
---

# 快速入门

[Memcached](https://www.memcached.org/) 是一个自由开源的，基于内存的key-value存储的高性能，分布式内存对象缓存系统。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/memcached/memcached-gui-websoft9.png)

## 准备

部署 Websoft9 提供的 Memcached 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 TCP：**11211 和 9090** 端口已经开启
3. 在服务器中查看 Memcached 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  Memcached，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程

## Memcached 初始化向导

### 详细步骤

1. 通过 SSH 工具连接 Memcached服务器，安装 telnet
   ```
   yum install telnet
   ```

2. 运行 telnet 命令，连接 Memcached
   ```
   telnet 127.0.0.1 11211
   Trying 127.0.0.1...
   Connected to 127.0.0.1.
   Escape character is '^]'.
   ```
3. 连接成功，系统进入 Memcached 命令行输入状态，输入命令 `stats`
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
4. 输入命令 `quit` 退出系统

5. 体验 Memcached 可视化管理工具 [Memcached-admin](#可视化管理)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

**Telnet 无法连接 Memcached？**   

请检查服务器是否已安装 telnet，同时查看云控制台安全组 **TCP:11211** 端口是否开启

## Memcached  使用入门

> 需要了解更多Memcached的使用，请参考：[Memcached Wiki](https://github.com/memcached/memcached/wiki)

## Memcached 常用操作

### 图形化 Web 端

Memcached 预装方案中内置可视化数据库管理工具 `Memcached-admin` ，使用请参考如下步骤：

1. 登录云控制台，开启 Memcached-admin 所需的[端口](#port)

2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP:9090*，进入登录页面

3. 输入数据库用户名和密码，进入控制面板
  ![Memcached-admin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/memcached/memcached-gui-websoft9.png)

### 集群

参考：[ClusterMaint](https://github.com/memcached/memcached/wiki/ClusterMaint)



## Memcached 参数

Memcached 应用中包含 Nginx, Docker, Memcached-admin 等组件，可通过 **[通用参数表](./setup/parameter)** 查看路径、服务、端口等参数。

通过运行 `docker ps`，可以查看到 Memcached 运行时所有的 Container：

```
CONTAINER ID   IMAGE                                 COMMAND                  CREATED             STATUS             PORTS                                           NAMES
5f7322ff5805   memcached:latest                      "docker-entrypoint.s…"   About an hour ago   Up About an hour   0.0.0.0:11211->11211/tcp, :::11211->11211/tcp   memcached
e4e671827a3e   hatamiarash7/memcached-admin:latest   "docker-php-entrypoi…"   4 minutes ago   Up 4 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp           memcached-admin
```

下面仅列出 Memcached 本身的参数：

### 路径{#path}

Memcached 配置文件：*path/.env*  
Memcached-admin 配置文件：*path/.env*  


### 端口{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 11211   | 远程访问 Memcached | 可选   |
| 9090  | 通过 Nginx 远程访问 Memcached 可视化工具| 可选   |


### 版本

```shell
# Memcached version
docker inspect  memcached | grep MEMCACHED_VERSION
```

### 服务

```shell
sudo docker start | stop | restart | stats memcached
sudo docker start | stop | restart | stats memcached-admin
```

### 命令行

#### 客户端

Memcached 是通过 Telnet 来运行客户端命令的：

1. 远程登录到服务器，运行 telnet 命令，连接到 Memcached
```
telnet 127.0.0.1 11211
Trying 127.0.0.1...
Connected to 127.0.0.1.
Escape character is '^]'.
```

2. 在交互式中输入 `stats` 查询系统信息

> 详情查看[官方文档](https://github.com/memcached/memcached/wiki/Commands)

#### 服务端

Memcached 没有传统意义上的客户端，只有服务端命令 `memcached -h`，但本项目中采用 Docker 部署 Memcached，虽不能直接使用服务端命令，但可以预先配置再启动容器。 

服务端设置，需要在运行容器的时候带入配置参数，具体操作步骤：    

1. 编辑 Memcached 容器编排文件 *path/docker-compose.yml*，修改增加更多的 **command** 项，然后保存
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

2. 重新创建容器后生效
   ```
   cd path
   sudo docker-compose up -d
   ```

### API

无