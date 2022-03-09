---
sidebar_position: 1
slug: /docker
---

# Docker 参考

## Docker 更新升级

上面的命令会同时升级 Docker 程序本体

#### 容器升级

#### Docker 命令升级

以正在运行的 MySQL 容器为例，如果没有持久化卷，容器的升级步骤：

```
#更新镜像
docker pull mysql

#停止容器
docker stop my-mysql-container

#删除容器
docker rm my-mysql-container

#重载容器
docker run --name=my-mysql-container --restart=always \
  -e MYSQL_ROOT_PASSWORD=mypwd -v /my/data/dir:/var/lib/mysql -d mysql
```

#### Docker-Compose 命令升级

如果使用的是 Docker-Compose 启动的容器，升级容器只需运行如下三条命令：

```
docker-compose down -v
docker-compose pull
docker-compose up -d
```

## 问题速查

#### 不知道容器所需的端口怎么办？

建议开启【Publish all exposed network ports...】 以保证容器中的服务可以自动匹配服务器端口被外界访问。如果不开启，需自行到[DockerHub](https://hub.docker.com/)网站查看端口。

#### 容器的端口与服务器的端口有什么区别？

容器端口需要通过服务器端口做映射，才可以被互联网用户访问。


#### 单台服务器上是否可以跑多个容器？

只要服务器资源允许，单台服务器上可以运行成百上千个容器

#### 什么是Docker的C/S模式？

Docker安装后，在宿主机（服务器）端会运行一个 Docker Daemon 守护进程，同时也安装一个Docker客户端与这个守护进程通信。但客户端与守护进程是分离的，即可以在任何地方运行客户端，然后通过远程与守护进程通信。
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/docker/docker-cs-websoft9.png)

#### 是否可以通过SSH连接容器？

在Container上的 console 控制台可以很方便的使用命令操作
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/docker/portainer/portainer-console-websoft9.png)

#### 一个容器中可以运行多个应用吗？

可以。但是从微服务架构角度看，建议一个容器运行单个应用或单个进程

#### 容器中的服务是否可以被互联网访问？

通过与宿主机（服务器）进行端口映射，实现被互联网用户访问

#### 是否有可视化的 Docker 管理工具？

有，推荐使用 Portainer

#### 是否可以修改 Docker 根目录？

可以，但不建议修改



