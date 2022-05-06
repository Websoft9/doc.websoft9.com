---
sidebar_position: 3
slug: /cockpit/admin
tags:
  - 故障
  - 路径
---


# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup/) 相关章节。

## 场景

### 子目录配置域名

Cockpit 配置域名有一定的特殊之处（[方案来源](https://caddy.community/t/example-cockpit/8283)）：

1. 先修改/etc/cockpit/cockpit.conf

```
[WebService]
Origins = https://example.com wss://example.com
ProtocolHeader = X-Forwarded-Proto
UrlRoot=/cockpit
```

2. 然后配置 proxy （以 Caddy 为例）
```
example.com {
    reverse_proxy /cockpit/* localhost:9090 {
        transport http {
            tls_insecure_skip_verify
        }
    }
}
```

## 故障排除

除以下列出的 Cockpit 故障问题之外， [通用故障处理](../troubleshoot) 专题章节提供了更多的故障方案。 

## 问题解答