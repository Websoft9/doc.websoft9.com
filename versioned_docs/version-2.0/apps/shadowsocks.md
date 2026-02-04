---
title: Shadowsocks
slug: /shadowsocks
tags:
  - 代理
  - 加速
---

import Meta from './_include/shadowsocks.md';

<Meta name="meta" />

## 入门指南{#guide}

Shadowsocks 需要遵循中国法律，请勿违法使用或用于非法用途。    

Websoft9 应用商店并不提供 Shadowsocks 的自动部署，本文档仅介绍 Shadowsocks 的使用参考。

### Docker Compose 部署文件

#### 服务端

```
services:
  shadowsocks:
    image: shadowsocks/shadowsocks-libev
    container_name: shadowsocks-libev
    restart: always
    environment:
      - PASSWORD=<Your password here>
      - METHOD=aes-128-gcm
    ports:
      - "8389:8388"
      - "8389:8388/udp"
```

> aes-128-gcm 的加密算法对性能影响最小

#### 客户端

客户端容器编排文件：  

```
services:
  webapp:
    image: ghcr.io/shadowsocks/sslocal-rust:latest
    container_name: $W9_ID
    restart: unless-stopped
    volumes:
      - ./config.json:/etc/shadowsocks-rust/config.json
    ports:
      - 1099:1088  
volumes:
  data:
```

客户端配置文件 config.json：

```
{
  "server": "<example.com>", 
  "server_port": <server_port>,            
  "password": "<Your password here>",    
  "method": "aes-128-gcm",      
  "local_address": "0.0.0.0",     
  "local_port": 1088,           
  "mode": "tcp_and_udp"
}
```
### 网络缓存优化

如果需要为 Shadowsocks 提供匹配的服务器网络缓存优化，具体的几个核心指标参考如下：

```
sudo sysctl -w net.core.rmem_max=2097152       # 2MB
sudo sysctl -w net.core.wmem_max=2097152       # 2MB
sudo sysctl -w net.core.rmem_default=524288    # 512KB
sudo sysctl -w net.core.wmem_default=524288    # 512KB
sudo sysctl -w net.ipv4.tcp_rmem="4096 524288 2097152"  # min 4KB, default 512KB, max 2MB
sudo sysctl -w net.ipv4.tcp_wmem="4096 524288 2097152"  # min 4KB, default 512KB, max 2MB
```

## 配置选项{#configs}

- 加密算法更改：修改环境变量 **METHOD**

## 管理维护{#administrator}

### 负载均衡

有两种负载均衡方案：

- 服务端负载均衡：使用 HAProxy 将多个 Shadowsocks 服务包装为一个对外的服务
- 客户端负载均衡：在 Shadowsocks 客户端的配置中，设置多个 Shadowsocks 服务端以及负载策略

前者是比较简单的。  

## 故障

#### 代理失效？

定期重启可以解决大部分时候的代理失效问题
