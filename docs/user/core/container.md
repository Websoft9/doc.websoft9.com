---
sidebar_position: 6
slug: /user/container
---

# 容器

Websoft9 集成 Portainer 作为唯一个容器可视化管理平台，100% 保持其原生性。  

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9/websoft9-portainer.png)

[Portainer](https://docs.portainer.io/) 是一个开源工具，用于管理容器化应用程序。它提供了一个直观的基于 Web 的用户界面，使用户能够轻松地管理 Docker、Kubernetes、Docker Swarm 和其他容器化环境。Portainer 旨在帮助简化容器管理过程，并使得不论是新手还是有经验的系统管理员都能轻松上手。

## 操作

### 安装个性化应用

如果 Websoft9 应用商店不满足安装需求，用户可以在容器管理平台中自定义安装 Docker 应用

- Docker-Compose 应用的自定义安装：【容器】>【Stacks】>【Add Stack】
- Docker 容器自定义安装：【容器】>【Containers】>【Add Container】

### 接入 K8s

Websoft9 容器管理平台可以通过 Environments 方便的接入 K8s，将多个集群纳入到统一的管理界面。  

## 常见问题？

#### 可以删除已有的 Environments 吗？

不可以删除默认的 local， 否则会导致应用无法管理。

####  Websoft9 应用 VS Portarner Stack ？

Websoft9 的应用中的容器是通过 Portainer 的 Stack API 创建的，故 Portainer 可以管理应用对应的容器。  

但是，Websoft9 应用还有更多的内容， 即它们不能完全化为等号

#### 可以修改 Portainer 的管理员账号吗?

不能修改，因为 Portainer 完全进行了深度集成

