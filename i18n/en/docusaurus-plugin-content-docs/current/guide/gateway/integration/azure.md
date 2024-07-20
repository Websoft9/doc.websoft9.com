---
sidebar_position: 1.3
slug: /gateway-azure
---

# Azure 应用程序网关

[Azure 应用程序网关](https://learn.microsoft.com/zh-cn/azure/application-gateway/overview)是一种 Web 流量（OSI 第 7 层）负载均衡器，可用于管理 Web 应用程序的流量。 传统负载均衡器在传输层（OSI 层 4 - TCP 和 UDP）进行操作，并基于源 IP 地址和端口将流量路由到目标 IP 地址和端口。

## 原理

![](./assets/azure-gateway-overview.png)

## 与 Websoft9 集成

Websoft9 托管平台与 Azure 应用程序网关无缝集成， ：

- 用 Azure 应用程序网关 直接替代 Websoft9 网关（应用部署在 Azure 虚拟机时）
- 保留 Websoft9 网关，Azure 应用程序网关，安全和路由服务