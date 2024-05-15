---
sidebar_position: 6
slug: /container
---

# 运行和管理容器

Websoft9 集成 Portainer 作为唯一个容器可视化管理平台，100% 保持其原生性。  

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9/websoft9-portainer.png)

[Portainer](https://docs.portainer.io/) 是一个开源工具，用于管理容器化应用程序。它提供了一个直观的基于 Web 的用户界面，使用户能够轻松地管理 Docker、Kubernetes、Docker Swarm 和其他容器化环境。Portainer 旨在帮助简化容器管理过程，并使得不论是新手还是有经验的系统管理员都能轻松上手。

## 操作

### 查看容器内部服务

- 监听的端口和服务：`netstat -tulnp`
- 进程：`ps aux`
- 活动进程：`top`

### Docker Compose 升级容器

Docker Compose 启动的多个容器，升级只需运行如下三条命令：

```
docker-compose down
docker-compose pull
docker-compose up -d
```

### 使用 Docker 安装应用

Websoft9 提供了一个包含 200+ 的 [Docker compose 模板](https://github.com/Websoft9/docker-library)，只需 Docker Compose 命令启动，即可安装任何想要的应用。  

[Docker-library](https://github.com/Websoft9/docker-library)：由 Websoft9 维护的 Docker Compose 模板，支持 200+ 开源应用

### 在 Portainer 中安装应用{#installapp}

如果 Websoft9 应用商店不满足安装需求，用户可以在容器管理平台中自定义安装 Docker 应用

- Docker-Compose 应用的自定义安装：【容器】>【Stacks】>【Add Stack】
- Docker 容器自定义安装：【容器】>【Containers】>【Add Container】

### 接入 K8s

Websoft9 容器管理平台可以通过 Environments 方便的接入 K8s，将多个集群纳入到统一的管理界面。  

### 容器中运行命令{#docker-exec}

Portainer 提供了可视化的运行容器命令的功能，它等同于 **docker exec -it**。

1. 在容器列表，点击下图中 MySQL 的 **Quick actions** 一栏下的 **>_** 图标；
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/potainer/portainer-containerlist-websoft9.png)

2. 在新打开的页面，点击 **Connetc** 按钮，准备连接；
    ![](http://libs-websoft9-com.oss-cn-qingdao.aliyuncs.com/Websoft9/DocsPicture/zh/potainer/portainer-createdatabase-websoft9.png)

    - Command：选择可用的命令执行（三选一，总有一个可用）
    - user: 默认 root（推荐）

3. 点击 "Connect"，成功连接到即可运行命令

## 常见问题？

#### 可以删除已有的 Environments 吗？

不可以删除默认的 local， 否则会导致应用无法管理。

####  Websoft9 应用 VS Portarner Stack ？

Websoft9 的应用中的容器是通过 Portainer 的 Stack API 创建的，故 Portainer 可以管理应用对应的容器。  

但是，Websoft9 应用还有更多的内容， 即它们不能完全化为等号

#### 可以修改 Portainer 的管理员账号吗?

不能修改，因为 Portainer 完全进行了深度集成

#### 容器 root 用户赋予宿主机权限？

如果 Dockerfile 没有创建普通用户，容器就会默认以 root 用户权限运行。  

容器的 root 与宿主机的 root 是同一个用户，但容器 root 的权限是有限的，加上 `--privileged=true`，就等同于宿主机 root 权限

#### Named Volumes 对比 Bind Mounts？

|          | Named Volumes                  | Bind Mounts                   |
| -------- | ------------------------------ | ----------------------------- |
| 路径     | /var/lib/docker/volumes 目录下 | 任意位置                      |
| 启用方式 | my-volume:/usr/local/data      | /path/to/data:/usr/local/data |
| 预先定义 | 可以先定义，也可以不定义       | 不需要                        |
| 名称     | my-volume_default 或 my-volume | data                          |
| 文件权限 | 权限宽松                       | 受制于宿主机文件权限          |
| 空目录下数据方向 | 容器 → Named Volume                   | Bind Volume  → 容器                |
| 非空目录下数据方向 | Named Volume  → 容器                   | Bind Volume  → 容器                |
