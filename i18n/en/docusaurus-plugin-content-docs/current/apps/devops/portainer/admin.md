---
sidebar_position: 2
slug: /portainer/admin
tags:
  - Docker
  - DevOps
---

# Portainer  Maintenance

This chapter is special guide for Portainer maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### Portainer Backup and Restore

### Portainer Backup

Backup the volumes (```/var/lib/docker/volumes```) means backup all data.

### Portainer Upgrade

Just run the command ```docker pull portainer``, you can update Portainer very easily


## Troubleshoot{#troubleshoot}

In addition to the Portainer issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  


## FAQ{#faq}

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

