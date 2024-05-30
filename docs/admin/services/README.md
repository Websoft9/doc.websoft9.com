---
sidebar_position: 1
slug: /backend-service
---

#  Websoft9 后台服务

在阅读本节内容之前，请先通过 [Websoft9 架构](./developer/architecture) 对 Websoft9 有一个全面的架构认知。  

## 关于

维护和管理 Websoft9 后台服务，实际上只需要关注两个技术组件：

- [容器组件](./parameter#docker-services)：构成 Websoft9 控制台的微服务
- Systemd 系统服务 websoft9.service：协调容器组件的调度和通信传递

## 设置后台服务

Websoft9 后台服务基于 Docker Compose 运行，只需在[Websoft9 容器编排文件目录](./parameter#path)找到相关文件即可轻松编排。  

### 为网关容器映射更多的宿主机端口{#proxy-bind-port}

修改 Websoft9 后台服务的 docker-compose.yml 文件的 **proxy** 服务，为它映射更多的 port 到宿主机。