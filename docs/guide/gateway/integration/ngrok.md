---
sidebar_position: 1.3
slug: /gateway-ngrok
---

# ngrok 安全隧道网关

[ngrok](https://ngrok.com/) 是一个非常流行的安全隧道工具，将两个计算环境，通过 SSH 协议建立虚拟通道，实现应用 Internet 访问。  

- ngrok 为隧道访问提供一个免费域名
- 无需任何复杂而的设置，仅一条命令即可

## 原理

![](./assets/ngrok-arch.png)

## 与 Websoft9 集成

在应用所在的服务器上运行 `ngrok` 转发命令，即可方便的发布应用访问地址

## 相关阅读

- [自建安全隧道网关服务端](https://www.baeldung.com/linux/ssh-tunneling-and-proxying)