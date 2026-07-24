---
sidebar_position: 2.0
slug: /parameter
---

# 配置参数

Websoft9 所涉及的服务器、网络、端口和路径等各种参数如下：  

## 目录或路径{#path}

Websoft9 控制台相关目录以及路径说明如下：

- **Websoft9 安装目录**：*/opt/websoft9*
- **Websoft9 数据持久化目录**：*/opt/websoft9/data*  
- **Websoft9 备份目录**： */opt/websoft9/data/backups*
- **Websoft9 应用持久化存储目录**： */var/lib/docker/volumes* 

Docker 相关的目录：

- Docker Volumes（命名数据卷）：*/var/lib/docker/volumes*    
- Docker 镜像目录: */var/lib/docker/image*   
- Docker 程序目录: */var/lib/docker*  
- Docker 服务端配置文件：*/etc/docker/daemon.json*    
- Docker 系统服务： */lib/systemd/system/docker.service*  

## 端口{#port}

用户可以通过 `netstat -tunlp` 查看服务器上已经用到的端口。      

下面是最常见的端口，请根据实际情况到安全组中 **开启或关闭** 它们：

### 应用访问{#apps-port}

| 端口号 | 用途 |  必要性 |
| --- | --- | --- |
| 9000 | Websoft9 控制台 | 必选 |
| 80 | Websoft9 控制台，Websoft9 网关，应用 HTTP 访问| 必选 |
| 443 | Websoft9 网关，应用 HTTPS 访问 | 必选 |
| 9001-9999| 应用外网访问 | 可选 |


### 服务器管理{#server-port}

| 端口号 | 用途 |  必要性 |
| --- | --- | --- |
| 21 | Linux 服务器 FTP 端口 | 可选 |
| 22 | Linux 服务器 SSH 端口 | 可选 |
| 2375 或 2376（TLS） | Docker daemon 监听 API | 可选 |

## 网络{#network}

默认创建了名称为 **websoft9** 的网络，所有应用都在这个网络中运行，即容器在网络上是互联互通的。  

## 服务{#service}

在应用的维护和配置中，可能涉及到 Systemd 和 Docker 两种服务的启动，停止，重启，状态查询等操作。  

### Systemd 服务{#systemd}

Websoft9 以 Docker 容器方式运行，涉及的 Systemd 服务主要是 Docker：  

```
sudo systemctl start | stop | restart | status docker
```

### Docker 服务{#docker-services}

Websoft9 以单容器方式运行，通过 `docker ps | grep websoft9` 命令查询：

```
$ docker ps | grep websoft9
abc123def456   websoft9dev/websoft9:latest   ...   Up 2 hours   0.0.0.0:80->80/tcp, 0.0.0.0:443->443/tcp, 0.0.0.0:9000->9000/tcp   websoft9
```

## 命令行

- Docker 命令行：`docker -h`, `docker compose -h`
- [Websoft9 命令行](./cli)