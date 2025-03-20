---
sidebar_position: 2.0
slug: /connectdb
---

# 连接应用的数据库

Websoft9 提供了两种数据库连接方式：Web 在线连接和本地客户端连接。   

虽然两者均受支持，我们建议优先考虑使用基于 [Web 的在线连接工具](./dbtools)。这种方式通过**内网连接**，不仅更加稳定可靠，而且简化了数据库的访问和管理过程。选择 Web 在线工具可以避免安装和维护本地客户端软件，使得数据库操作更加高效和直接。

## 条件

在线连接并管理数据库的所需的两个要素：

- **准备数据库管理工具**

  - 通过 Websoft9 控制台 [安装在线数据库管理工具](./dbtools) 
  - 或准备本地客户端

- 获取准确的数据库网络连接信息（主机名，账号，密码，端口等）

  - [获取应用的数据库连接信息](./app-getdetail#db)
  - [数据库默认账号、端口对照表](./app-getdetail#db)


## Web 在线连接

使用 Web 在线工具连接数据库，请参考对应的[数据库工具](./apps/#数据库)相关文档：  

- [phpMyAdmin](./phpmyadmin)
- [pgAdmin](./pgadmin)
- [CloudBeaver](./cloudbeaver)
- [RedisInsight](./redisinsight)
- [更多工具...](./apps/#数据库)

## 本地客户端连接

尽管我们不建议直接从本地客户端连接到远程数据库，但以下是我们为此目的提供的参考方案，请按需谨慎使用。

以 MySQL 为例，进行任务说明：

1. 采用以下的方式之一，将数据库容器 3306 端口暴露到外网：

   - [基于 Websoft9 网关进行 Streams 转发到宿主机](./gateway-proxy#stream)（推荐）
   - [基于 SSH tunnel 进行转发到宿主机](./gateway-tunnel#ssh-port)
   - [更新 MySQL 应用的部署](./app-compose)，在 docker-compose.yml 文件中 expose 端口到宿主机


3. 本地客户端使用服务器的 IP 和 服务器对应的端口连接 MySQL 

