---
sidebar_position: 2
slug: /docker/admin
tags:
  - Docker
  - DevOps
---

# 维护参考


## 系统参数

Portainer 预装包包含 Portainer 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

#### Docker

Docker 根目录: */var/lib/docker*  
Docker 镜像目录: */var/lib/docker/image*   
Docker daemon.json 文件：默认没有创建，请到 */etc/docker* 目录下根据需要自行创建   

#### Portainer

Portainer 数据卷：*/var/lib/docker/volumes/portainer_data/_data* 


### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

本应用建议开启的端口如下：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| Portainer | 9000 | 通过 HTTP 访问 Portainer | 必须 |

### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Check all components version
sudo cat /data/logs/install_version.txt

# Linux Version
lsb_release -a

# Docker Version
docker -v
```

### 服务

使用由 Websoft9 提供的 Docker 部署方案，可能需要用到的服务如下：

#### Docker系统服务

```shell
sudo systemctl start docker
sudo systemctl restart docker
sudo systemctl stop docker
sudo systemctl status docker
```

#### Docker-compose服务

```
#创建容器编排
sudo docker-compose up

#创建容器编排并重建有变化的容器
sudo docker-compose up -d

#启动/重启
sudo docker-compose start
sudo docker-compose stop
sudo docker-compose restart
```

#### 运行时容器管理

> 终止命令 `stop` 会从进程中释放容器的资源，但不会删除容器

```shell
#示例：mysql
sudo docker pause mysql
sudo docker stop mysql

#示例：redis
sudo docker pause redis
sudo docker stop redis
```


## Portainer 备份

到 Portainer 的容器列表里面查看 portainer 的 volume 对应的服务器目录，在```/var/lib/docker/volumes```下可找到 volume 对应的目录名，将其备份即可。

## Portainer 升级

只需运行 ```docker pull portainer```就可以将 Portainer 升级到最新版本。

## Portaniner 绑定域名

域名绑定可在 [配置Nginx实现端口转发](/zh/solution-portainer.md#设置-nginx-配置文件实现端口转发) 章节中将 server_name 改成自己的域名即可。


## 故障处理

我们收集使用 Portainer 过程中最常见的故障，供您参考：


## 常见问题

#### 如何通过 Portainer 运行容器内部命令？

在此以连接到 MySQL 容器为例进行说明：

1. 返回到容器列表，点击下图中 MySQL 的 **Quick actions** 一栏下的 **>_** 图标；
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/potainer/portainer-containerlist-websoft9.png)
2. 在新打开的页面，点击 **Connetc** 按钮，连接到容器；
    ![](http://libs-websoft9-com.oss-cn-qingdao.aliyuncs.com/Websoft9/DocsPicture/zh/potainer/portainer-createdatabase-websoft9.png)
3. 接下来就可以在命令窗口中输入```mysql -uroot -ppassword;"```,其中 “password” 为您在自己设置的数据库密码，这样就可以开始使用数据库命令对 MySQL 进行管理了；
