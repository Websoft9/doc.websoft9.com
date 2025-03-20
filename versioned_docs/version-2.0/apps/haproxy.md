---
title: HAProxy
slug: /haproxy
tags:
  - HA
  - 负载均衡
  - HTTP 服务器
  - 高可用性
---

import Meta from './_include/haproxy.md';

<Meta name="meta" />

## 入门指南{#guide}

### 登陆设置密码{#wizard}

1. Websoft9 控制台安装 HAProxy 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息

2. 并在配置文件中设置密码。   

### 开启 HAProxy 监控

默认已经设置 HAProxy Statistics Report，通过 Websoft9 控制台应用管理界面中可查看。  

### 高可用性

通过部署 Keepalived 实现 HAProxy的高可用性

### 集群配置

只需在配置文件中添加需要管理的集群服务器信息即可启用 HAProxy 集群，范例如下：

  ```
  # [HTTP Site Configuration]
  listen  http_web 192.168.10.10:80
          mode http
          balance roundrobin  # Load Balancing algorithm
          option httpchk
          option forwardfor
          server server1 192.168.10.100:80 weight 1 maxconn 512 check
          server server2 192.168.10.101:80 weight 1 maxconn 512 check

  # [HTTPS Site Configuration]
  listen  https_web 192.168.10.10:443
          mode tcp
          balance source# Load Balancing algorithm
          reqadd X-Forwarded-Proto: http
          server server1 192.168.10.100:443 weight 1 maxconn 512 check
          server server2 192.168.10.101:443 weight 1 maxconn 512 check
  ```

## 配置选项{#configs}

- 配置文件（已挂载）：*/usr/local/etc/haproxy/haproxy.cfg*
- 命令行：`haproxy`
- [HAProxy APIS](https://www.haproxy.com/blog/haproxy-apis/)

## 管理维护{#administrator}

## 故障