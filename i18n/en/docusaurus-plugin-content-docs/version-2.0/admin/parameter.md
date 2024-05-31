---
sidebar_position: 10.3
slug: /admin/parameter
---

# 参数

Websoft9 所涉及的服务器、网络、端口和路径等各种参数如下：  

## 目录{#path}

目录以及路径说明如下：

- **Websoft9 安装配置目录**：*/data/websoft9/source*
- **Websoft9 容器文件目录**：*/data/websoft9/source/docker*
- **Websoft9 系统配置目录**：*/opt/websoft9*  
- **Websoft9 插件目录**： */usr/share/cockpit*  
- **备份 Volumes 目录**： */data/websoft9/vl_backup*
- **Docker Volumes 目录**： */var/lib/docker/volumes* 

## 端口{#port}

用户可以通过 `netstat -tunlp` 查看服务器上已经用到的端口。      

下面是最常见的端口，请根据实际情况到安全组中 **开启或关闭** 它们：

### 应用访问

| 端口号 | 用途 |  必要性 |
| --- | --- | --- |
| 9000 | Websoft9 控制台 | 必选 |
| 80 | Websoft9 网关，应用 HTTP 访问| 必选 |
| 443 | Websoft9 网关，应用 HTTPS 访问 | 必选 |

### 服务器连接

| 端口号 | 用途 |  必要性 |
| --- | --- | --- |
| 21 | Linux 服务器 FTP 端口 | 可选 |
| 22 | Linux 服务器 SSH 端口 | 可选 |

## 网络{#network}

默认创建了名称为 websoft9 的网络，所有应用都在这个网络中运行，即容器在网络上是互联互通的。  

## 服务{#service}

在应用的维护和配置中，可能涉及到 Systemd 和 Docker 两种服务的启动，停止，重启，状态查询等操作。  

### Systemd 服务

包含：websoft9, docker, cockpit 三个 Systemd 服务：  

```
sudo systemctl start | top | restart | status docker
sudo systemctl start | top | restart | status cockpit
sudo systemctl start | top | restart | status websoft9
```

### Docker 服务

Websoft9 控制台的**容器管理界面**隐藏了对 Websoft9 容器的管理。故，通过 `docker ps | grep websoft9-` 命令查询：

```
$ docker ps | grep websoft9-
8039d81eb0a1   websoft9dev/apphub:0.0.6                 "/websoft9/script/en…"   32 hours ago   Up 32 hours             8080-8081/tcp                                                                      websoft9-apphub
cc55650540e6   websoft9dev/deployment:2.19.0            "/init_portainer"        32 hours ago   Up 32 hours (healthy)   8000/tcp, 9000/tcp, 9443/tcp                                                       websoft9-deployment
527a07615809   websoft9dev/git:1.20.4                   "/usr/bin/entrypoint…"   32 hours ago   Up 32 hours             22/tcp, 3000/tcp                                                                   websoft9-git
bbea45d00358   websoft9dev/proxy:2.10.4                 "/init /bin/sh -c '/…"   32 hours ago   Up 32 hours             0.0.0.0:80->80/tcp, :::80->80/tcp, 0.0.0.0:443->443/tcp, :::443->443/tcp, 81/tcp   websoft9-proxy
```