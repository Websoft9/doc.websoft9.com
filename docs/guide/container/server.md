---
sidebar_position: 3
slug: /docker-server
---

# 设置 Docker 服务端

本章介绍使用 Websoft9 托管应用过程中，可能需要对 Docker 服务端进行的设置。   

## 任务指南


### 安装 Docker{#install}

如果您的服务器尚未安装 Docker，请使用如下命令安装它：

```
wget -O - https://websoft9.github.io/websoft9/install/install_docker.sh | bash
```

### 更换默认镜像仓库{#imagespeed}

Docker 默认从 Dockerhub 下载镜像。如果想更换仓库地址，请参考如下步骤：

1. 自行准备新的仓库地址或选择[第三方镜像仓库](./imagehub)


2. 向 */etc/docker/daemon.json* 文件（文件不存新建即可）中插入仓库地址（支持多个）
    ```
    {
      "registry-mirrors": ["https://registry.docker-cn.com","http://hub-mirror.c.163.com"]
    }
    ```

3. 重启 Docker 服务后生效

### 容器持久化存储设置{#volume}

Websoft9 使用 Named Volumes 作为容器的持久化方案。 

## 相关内容

- [Docker 服务端配置参数](./parameter#path)
- [Docker 命令行](./parameter#cmd)
- [开启 Docker API 外部访问](https://docs.docker.com/reference/cli/dockerd/#daemon-socket-option)

## 参考文档

- [Docker 官方文档](https://docs.docker.com/)

## 故障{#troubleshoot}

#### docker-containerd.socket: timeout?

请关闭 SELinux，如果 SELinux 开启会导致 docker 无法启动。  

#### Windows 中 Docker 无法启动？

检查您的 Windows 是否安装了 360 之类的安全软件，如果有请卸载它。  


