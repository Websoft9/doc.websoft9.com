---
sidebar_position: 2
slug: /docker/admin
tags:
  - Docker
  - DevOps
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../installation/setup/) 相关章节。

## 场景

### Portainer 备份

到 Portainer 的容器列表里面查看 portainer 的 volume 对应的服务器目录，在```/var/lib/docker/volumes```下可找到 volume 对应的目录名，将其备份即可。

### Portainer 升级

只需运行 ```docker pull portainer```就可以将 Portainer 升级到最新版本。


## 故障速查

除以下列出的 Portainer 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。 


## 问题解答

#### 怎么获得 Portainer 商业版秘钥？

需向官方申请商业版秘钥，目前企业版针对 5 个节点是免费的

#### 采用何种方式安装 Portainer？

采用 Docker 安装

#### 服务器中没有Portainer，如何安装？

可以将服务器当前镜像更换为Portainer镜像，也可以在当前镜像的基础通过命令安装

    ~~~
    #通过命令安装 Portainer

    docker volume create portainer_data
    docker run -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
    cd /usr/libexec/docker/
    sudo ln -s docker-runc-current docker-runc
    ~~~

