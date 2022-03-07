---
sidebar_position: 1
slug: /memcached
tags:
  - Memcached 
  - Cloud Native Database
---

# 快速入门

[Memcached](https://www.memcached.org/) 是一个自由开源的，高性能，分布式内存对象缓存系统。是一种基于内存的key-value存储，用来存储小块的任意数据（字符串、对象）。这些数据可以是数据库调用、API调用或者是页面渲染的结果。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/memcached/memcached-gui-websoft9.png)

在云服务器上部署 Memcached 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:11211** 端口是否开启
3. 若想用域名访问 Memcached，请先到 **域名控制台** 完成一个域名解析

## 账号密码


通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

### Memcached

默认没有开启密码验证 

### Memcached-admin

* 管理员账号：*`admin`*
* 管理员密码：存储在您的服务器中的文件中 */credentials/password.txt*  

> 本部署方案通过 [Nginx 验证访问功能](/zh/stack-components.md#nginx) 来设置 Memcached-admin 账户密码


## Memcached 安装向导

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

> 需要了解更多Memcached的使用，请参考：[Memcached Wiki](https://github.com/memcached/memcached/wiki)

## 常用操作

### 可视化管理

Memcached 预装方案中内置可视化数据库管理工具 `Memcached-admin` ，使用请参考如下步骤：

1. 登录云控制台，开启服务器[安全组9090端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP:9090*，进入登录页面

3. 输入数据库用户名和密码，进入控制面板
  ![Memcached-admin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/memcached/memcached-gui-websoft9.png)

### 集群

详细部署方案请参考[官方文档](https://github.com/memcached/memcached/wiki/ClusterMaint)

## 异常处理

#### Telnet 无法连接 Memcached？

请检查服务器是否已安装 telnet，同时查看云控制台安全组 **11211 端口**是否开启

#### 本部署是否提供Web版的可视化管理工具？

已提供

#### 本部署是如何安装 Memcached 的？

Docker
