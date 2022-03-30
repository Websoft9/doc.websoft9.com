---
sidebar_position: 3
slug: /memcached/admin
tags:
  - Memcached 
  - Cloud Native Database
---

# 维护参考

## 场景

## 故障速查

除以下列出的 Memcached 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。 


## 常见解答

#### 什么是 Memcached 客户端？

Memcached 客户端是用于与 Memcached-Server 进行通信的程序，Memcached 是通过 Telnet 来运行客户端命令的。

#### Memcached 需要密码才能登录吗？

无需设置密码验证

#### Memcached-admin 账号密码怎么来的？

通过 [Nginx auth_basic](./nginx#authbasic) 来设置

#### 如何修改 Memcached-admin 控制台密码？

参考： [Nginx auth_basic](./nginx#authbasic)

### Memcached 是否开启密码验证？

没有开启


