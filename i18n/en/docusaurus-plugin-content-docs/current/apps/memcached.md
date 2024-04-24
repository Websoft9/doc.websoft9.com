---
title: Memcached
slug: /memcached
tags:
  - 缓存数据库
  - 内存计算
  - 加速
---

import Meta from './_include/memcached.md';

<Meta name="meta" />

## 入门指南{#guide}

Websoft9 控制台安装 Memcached 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

### Telnet 连接

1. 运行 telnet 命令，连接 Memcached

   ```
   telnet 127.0.0.1 11211
   Trying 127.0.0.1...
   Connected to 127.0.0.1.
   Escape character is '^]'.
   ```

3. 连接成功，系统进入 Memcached 命令行输入状态，输入命令 `stats`

   ```
   $ stats
   STAT pid 651
   STAT uptime 891
   STAT time 1585225158
   STAT version 1.4.15
   STAT libevent 2.0.21-stable
   ...
   ```
   
### 图形化 Web 端

Memcached 数据库管理工具 **Memcached-admin** ，使用请参考如下步骤：

1. 本地浏览器访问后，进入登录页面

2. 输入数据库用户名和密码，进入控制面板
  ![Memcached-admin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/memcached/memcached-gui-websoft9.png)


## 配置选项{#configs}

- 客户端命令：[Memcached Commands](https://github.com/memcached/memcached/wiki/Commands) 是通过 Telnet 来运行的
- 服务端命令：`memcached -h`

## 管理维护{#administrator}

### 集群

参考：[ClusterMaint](https://github.com/memcached/memcached/wiki/ClusterMaint)


## 故障