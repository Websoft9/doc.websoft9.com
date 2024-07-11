---
sidebar_position: 1
slug: /backend-service
---

#  Websoft9 后台服务

在阅读本节内容之前，请先通过 [Websoft9 架构](./developer/architecture) 对 Websoft9 有一个全面的架构认知。  

## 服务

Websoft9 的后台服务，由如下两个部分组成：

- [容器服务](./parameter#docker-services)：Websoft9 控制台功能组件的多个容器服务
- websoft9.service：协调容器组件的调度和通信传递的 Systemd 服务

## 设置 Websoft9 容器服务

Websoft9 容器服务基于 Docker Compose 运行，通过其 [.env 文件](./parameter#path) 和 [docker-compose.yml 文件](./parameter#path) 进行设置。  

### 为网关容器映射更多的宿主机端口{#proxy-bind-port}

修改 Websoft9 后台服务的 docker-compose.yml 文件的 **proxy** 服务，为它映射更多的 port 到宿主机。