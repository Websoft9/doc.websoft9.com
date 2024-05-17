---
sidebar_position: 6
slug: /container
---

# 管理容器的生命周期

Websoft9 控制台是为管理应用的生命周期的而设计。实际托管中，也需要对容器的生命周期进行管理。

## 管理工具

- Docker 官方客户端工具：[docker](https://docs.docker.com/engine/) 命令和 [docker compose](https://docs.docker.com/compose/) 命令
- 可视化 Web 工具：Websoft9 集成 [Portainer](./portainer) 作为唯一个容器可视化管理平台，100% 保持其原生性。  

   Websoft9 控制台的 "网关" 菜单即可进入 Portainer:  
  ![](./assets/websoft9-portainer.png)


## 运行容器

Websoft9 完全兼容 Docker，所以用户可以不依赖于 Websoft9 控制台而直接使用 Docker 客户端工具部署由多容器组成的应用。  

Websoft9 提供了一个包含 200+ 开源 [Docker compose 模板](https://github.com/Websoft9/docker-library)，只需 `docker compose` 命令启动，即可安装任何想要的应用。  


## 升级多容器

Docker Compose 升级应用只需运行如下三条命令：

```
docker-compose down
docker-compose pull
docker-compose up -d
```