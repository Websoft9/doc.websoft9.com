---
sidebar_position: 3.1
slug: /runtime/docker
tags:
  - 运行环境
  - runtime
  - Docker
---

# For Docker App

基于 Docker 模板环境部署镜像类应用，需要用户具备一定的 [Docker Compose](https://docs.docker.com/compose/) 知识，否则难以为继。 

## 原理

通过 Websoft9 应用商店安装 Docker 模板环境后，便自动创建一个 **可以被 Websoft9 控制台管理的应用 Demo**，这是它的逻辑。  

接下来，用户的工作便是通过[Docker 应用个性化编排](./runtime#dockercompose)，将 Demo 转变成自己真正所需的应用


## 配置选项{#configs}

- W9_PROXY_PORT_SET 为目标应用主容器的端口，确保在安装时正确设置

## 部署网站{#deploy}

参考：[App Runtime 入门指南](../runtime#quick)

## 问题与故障