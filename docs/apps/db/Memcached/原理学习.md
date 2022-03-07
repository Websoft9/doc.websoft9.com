---
sidebar_position: 3
slug: /memcached/study
tags:
  - Memcached 
  - Cloud Native Database
---

# 原理学习

## 命令与系统配置

Memcached 没有传统意义上的客户端，只有服务端命令 `memcached -h`，但本项目中采用 Docker 部署 Memcached，虽不能直接使用服务端命令，但可以预先配置再启动容器。  

### 服务端

服务端设置，需要在运行容器的时候带入配置参数，具体操作步骤：  

1. 编辑 Memcached 容器编排文件 */data/db/memcached/docker-compose.yml*，修改增加更多的 **command** 项，然后保存
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
   cd /data/db/memcached
   sudo docker-compose up -d
   ```

### 客户端

直接使用 Telnet 连接到 Memcached，便可以运行 Memcached 操作命令

1. 远程登录到服务器，运行 telnet 命令，连接到 Memcached
```
telnet 127.0.0.1 11211
Trying 127.0.0.1...
Connected to 127.0.0.1.
Escape character is '^]'.
```

2. 在交互式中输入 `stats` 查询系统信息

> 详情查看[官方文档](https://github.com/memcached/memcached/wiki/Commands)