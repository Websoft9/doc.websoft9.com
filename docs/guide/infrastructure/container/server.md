---
sidebar_position: 3
slug: /docker
---

# 设置 Docker 服务端

本章介绍使用 Websoft9 托管应用过程中，可能需要的 Docker 相关操作。   

## 指南

### 安装 Docker{#install}

如果您的服务器尚未安装 Docker，请使用如下命令安装它：

```
wget -O - https://websoft9.github.io/websoft9/install/install_docker.sh | bash
```

### 使用 Docker 安装应用

Websoft9 提供了一个包含 200+ 的 [Docker compose 模板](https://github.com/Websoft9/docker-library)，只需 Docker Compose 命令启动，即可安装任何想要的应用。  

### 更换默认镜像仓库{#imagespeed}

Docker 默认从 Dockerhub 下载镜像。如果想更换仓库地址，请参考如下步骤：

1. 自行准备新的仓库地址或从如下仓库中选择
   ```
   #1 Docker 中文社区
   https://registry.docker-cn.com

   #2 网易仓库
   http://hub-mirror.c.163.com

   #3 腾讯仓库
   https://mirror.ccs.tencentyun.com
   ```

2. 向 */etc/docker/daemon.json* 文件（此文件不存在时，新建即可）中插入一个或多个仓库地址
    ```
    # 一个仓库
    {
      "registry-mirrors": ["https://mirror.ccs.tencentyun.com"]
    }

    # 多个仓库
    {
      "registry-mirrors": ["https://registry.docker-cn.com","http://hub-mirror.c.163.com"]
    }
    ```

3. 重启服务后生效
    ```
    sudo systemctl daemon-reload
    sudo systemctl restart docker
    ```

### 远程 API 访问设置{#enableapi}

Docker 服务提供了丰富的 API 接口，默认只能在本地以 **socket** 通讯方式访问 API。

```
curl --unix-socket /var/run/docker.sock  http://docker/version
```

如果需添加远程访问 [Docker API](https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-socket-option)，需修改 [Docker系统服务](#path)，然后在 **ExecStart** 这一行添加 `-H tcp://0.0.0.0:2375`

```
ExecStart=/usr/bin/dockerd -H fd://   --containerd=/run/containerd/containerd.sock -H tcp://0.0.0.0:2375
```

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

## 配置选项

- 路径

    Docker 根目录: */var/lib/docker*  
    Docker 镜像目录: */var/lib/docker/image*   
    Docker daemon.json 文件：默认没有创建，请到 */etc/docker* 目录下根据需要自行创建   
    Portainer 数据卷：*/var/lib/docker/volumes/portainer_data/_data*    
    Docker 系统服务： */lib/systemd/system/docker.service*  

- 端口：Docker daemon 来允许远程API访问，它会监听一个 TCP 端口，默认是 2375 或 2376（TLS）
- 命令行：`docker -h`, `docker compose -h`
- 系统服务
  ```shell
  sudo systemctl start docker
  sudo systemctl restart docker
  sudo systemctl stop docker
  sudo systemctl status docker
  ```

## 推荐资源

- [Docker-library](https://github.com/Websoft9/docker-library)：由 Websoft9 维护的 Docker Compose 模板，支持 200+ 开源应用

- 主流的公共镜像仓库

    * [DockerHub](https://hub.docker.com/)
    * [Amazon ECR Public Gallery](https://gallery.ecr.aws/)
    * [Microsoft Artifact Registry](https://mcr.microsoft.com/)
    * [Oracle Container Registry](https://container-registry.oracle.com/)
    * [image at Github](https://github.com/search?q=wordpress+image&type=registrypackages)

## 问题与故障{#troubleshoot}

#### 容器应用无法远程访问？{#noremote}

导致这个问题的可能原因有三点：

1. 端口没有正确映射到宿主机
2. 容器内部拒绝远程访问
3. 服务器安全组对应的端口没有开放

#### docker-containerd.socket: timeout?

请关闭 SELinux，如果 SELinux 开启会导致 docker 无法启动。  

#### Windows 中 Docker 无法启动？

检查您的 Windows 是否安装了 360 之类的安全软件，如果有请卸载它。  

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
