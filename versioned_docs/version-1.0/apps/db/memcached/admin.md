---
sidebar_position: 3
slug: /memcached/admin
tags:
  - Memcached 
  - Cloud Native Database
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup) 相关章节。

## 场景

## 故障排除{#troubleshoot}

除以下列出的 Memcached 故障问题之外， [通用故障处理](../troubleshoot) 专题章节提供了更多的故障方案。 


## 常见解答

#### 什么是 Memcached 客户端？

Memcached 客户端是用于与 Memcached-Server 进行通信的程序，Memcached 是通过 Telnet 来运行客户端命令的。

#### Memcached 是否开启密码验证？

没有开启

#### Memcached 需要密码才能登录吗？

无需设置密码验证

#### 如何修改 Memcached-admin 控制台密码？

参考： [Nginx auth_basic](../nginx#authbasic)
