---
sidebar_position: 1.1
slug: /app-network
title: "Manage applications access"
---

# Manage applications access

Websoft9 provides a variety of [app access](./app-getdetail#access) and connectivity options to ensure smooth user-application and application-application interactions:  

Websoft9 的托管平台提供多样化的[应用访问](./app-getdetail#access)与连接选项，确保用户和应用、应用与应用的顺畅交互：  

- **公共网络访问**：允许通过互联网使用 `服务器公网IP:应用 HTTP 端口` 的方式直接访问应用，适用于公开服务。

- **局域网络访问**：在私密且受保护的局域网络内，仅局域网内部用户使用 `服务器内网IP:应用 HTTP 端口` 访问应用

- **[域名访问](./domain-set)**：通过网关为应用分配域名，简化用户的访问路径

- **[TCP/UDP代理访问](/gateway-proxy#stream)**：允许应用通过 TCP 或 UDP 协议的代理服务器进行通信

- **安全访问**：为应用[设置 HTTPS](./domain-https) 或 白名单[访问控制](./domain-auth)机制，保障数据和隐私

这些连接策略不仅加强了应用的可达性和安全性，还为不同的业务场景提供了灵活的解决方案。



