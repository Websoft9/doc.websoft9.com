---
sidebar_position: 1
slug: /portainer
tags:
  - Docker
  - DevOps
---

# 快速入门

[Portainer](https://www.portainer.io) 是一个可视化的 Docker 操作界面，提供状态显示面板、应用模板快速部署、容器镜像网络数据卷的基本操作（包括上传下载镜像，创建容器等操作）、事件日志显示、容器控制台操作、Swarm集群和服务等集中管理和操作、登录用户管理和控制等功能。功能十分全面，基本能满足中小型单位对容器管理的全部需求。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/docker/portainer/portainer-sc001-websoft9.png)

部署 Websoft9 提供的 Portainer 之后，请参考下面的步骤快速入门。


## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 若想用域名访问  Portainer，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程

## Portainer 初始化向导

### 详细步骤

1. 使用 SSH 连接服务器，运行下面的命令，查看 Docker 的安装信息和运行状态
   ```
   sudo docker info
   sudo systemctl status docker
   ```
   运行服务状态查询命令，Docker 正常运行会得到 " Active: active (running)... " 的反馈

2. 通过本地浏览器访问：*http://服务器公网IP*， 直接进入 Portainer 界面
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/docker/portainer/portainer-login-websoft9.png)

> Portainer官方容器启动后，如果不设置初始密码，会提示超时，需要执行`sudo docker restart portainer`

3. 自行设置管理员账号密码，点击【Create user】

4. 选择【Local】作为镜像连接选项，然后点击【Connect】
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/docker/portainer/portainer-loginconnect-websoft9.png)

5. 进入Portainer后台管理界面，点击Local项目就可以开始使用Portainer
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/docker/portainer/portainer-bkselect-websoft9.png)

6. 通过 Portainer 查看运行容器，你会发现 Portainer 本身也是运行在容器中的
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/docker/portainer/portainer-pcontainer-websoft9.png)

> 需要了解更多 Docker 的使用，请参考官方文档：[Docker Documentation](https://docs.docker.com/)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

## Portainer 使用入门

下面以部署一个 WordPress 网站为场景，描述 Portainer 的使用：  

### 部署 MySQL 容器

下面详细介绍通过 Portainer 部署MySQL：

1. 登录 Portainer ，打开【Containers】>【Add container】
    ![createcontainer](http://libs.websoft9.com/Websoft9/DocsPicture/zh/potainer/portainer-addcontainer-websoft9.png)

2. 设置容器运行所需的参数（下面示图并描述重点设置部分）   
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/potainer/portainer-mysql-websoft9.png)

   * Name 为自定义的容器名称
   * Image 为容器镜像名称，例如"mysql:5.6" 系统会自动到[DockerHub](https://hub.docker.com/)中拉取MySQL5.6
   * Network ports configuration：建议开启【Publish all exposed network ports...】 以保证容器中的服务可以通过服务器端口被外界访问。如果不开启，需手工建立准确的映射关系(**难度系数有点高**)。
   * Env 环境变量设置：添加如所示的容器环境变量，对于MySQL镜像来说，数据库 root 密码**MySQL_ROOT_PASSWORD** 为必填变量，其他更多可选变量查看 [ MySQL镜像说明](https://hub.docker.com/_/mysql)
   * Restart policy：建议选择【Always】，使得容器无论在什么情况下停止总会自动重新启动；

3. 点击 Deploy the container 创建容器；
    
4. 如果服务器安全组的 3306 端口已经开放，现在就可以在本地通过远程连接 MySQL 数据库

### 部署 WordPress 容器

下面详细介绍通过 Portainer 部署 WordPress 以及使用上一步的 MySQL 作为数据存储：

1. 登录 Portainer ，打开【Containers】>【Add container】
   ![createcontainer](http://libs.websoft9.com/Websoft9/DocsPicture/zh/potainer/portainer-addcontainer-websoft9.png)

2. 设置容器运行所需的参数（下面示图并描述重点设置部分）   
   ![wordpress](http://libs.websoft9.com/Websoft9/DocsPicture/zh/potainer/portainer-wordpress-websoft9.png)

   * Name 为自定义的容器名称
   * Image 为容器镜像名称，例如"wordpress" 系统会自动到[DockerHub](https://hub.docker.com/)中拉取WordPress
   * Network ports configuration：建议开启【Publish all exposed network ports...】 以保证容器中的服务可以自动匹配服务器端口被外界访问。如果不开启，需手工建立准确的映射关系(**难度系数有点高**)。
   * Restart policy：建议选择【Always】，使得容器无论在什么情况下停止总会自动重新启动；

3. 点击 Deploy the container 创建容器，创建成功后查看映射的服务器端口号；
    
4. 本地浏览器访问：*http://服务器公网IP：端口* 即可访问 WordPress 的初始化安装界面
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/potainer/portainer-startinstall-1-websoft9.png)

5. 此处如果你打算使用MySQL容器，数据库主机地址填写的是 **服务器公网IP:端口**
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/potainer/portainer-startinstall-2-websoft9.png)

6. 数据库验证通过后，系统提示正式“进行安装” 
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-install003-websoft9.png)


### Nginx 容器绑定域名

以上一章节中的 Wordpress 网站作为示例，在 WordPress 部署完成后，需要在浏览器内输入 *http://公网IP地址：端口* 的形式访问网站，但我们不加端口就能访问域名，所以这时就要用到 Nginx 的端口转发功能。  

我们使用使用一款可视化的 Nginx 管理器：[Nginx Proxy Manager](https://hub.docker.com/r/jc21/nginx-proxy-manager)


### FileBrowser 容器管理文件

1. 进入到 Portainer 页面，选择左边的 **App Templates** 选项，往下找到 **File browser** 容器模板，单击选择；
    ![filebowser-1](http://libs.websoft9.com/Websoft9/DocsPicture/zh/potainer/portainer-filebrowser-1-websoft9.png)
2. 按照下图创建 File browser 容器；
    ![filebowser-2](http://libs.websoft9.com/Websoft9/DocsPicture/zh/potainer/portainer-filebrowser-2-websoft9.png)
3. 进入到容器列表，单击刚刚创建的 File browser 容器，点击 **Duplicate/Edit** 按钮，进入到修改容器信息页面；
    ![filebowser-3](http://libs.websoft9.com/Websoft9/DocsPicture/zh/potainer/portainer-filebrowser-3-websoft9.png)
4. 按照下图，将 File browser 的 volume 值修改为 和 Nginx 的 volume 值相同；
    ![filebowser-4](http://libs.websoft9.com/Websoft9/DocsPicture/zh/potainer/portainer-filebrowser-4-websoft9.png)

## Portainer 常用操作

#### 运行容器命令

在此以连接到 MySQL 容器为例进行说明：

1. 返回到容器列表，点击下图中 MySQL 的 **Quick actions** 一栏下的 **>_** 图标；
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/potainer/portainer-containerlist-websoft9.png)
2. 在新打开的页面，点击 **Connetc** 按钮，连接到容器；
    ![](http://libs-websoft9-com.oss-cn-qingdao.aliyuncs.com/Websoft9/DocsPicture/zh/potainer/portainer-createdatabase-websoft9.png)
3. 接下来就可以在命令窗口中输入```mysql -uroot -ppassword;"```,其中 “password” 为您在自己设置的数据库密码，这样就可以开始使用数据库命令对 MySQL 进行管理了；


## 参数

Portainer 应用中包含 Docker, Portainer 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。 

通过运行 `docker ps`，查看 Portainer 运行时所有的服务组件：   

```bash
CONTAINER ID   IMAGE                           COMMAND                  CREATED        STATUS                  PORTS                                                                               NAMES
c47fe38db3bf   portainer/portainer-ce:latest   "/portainer"             2 months ago   Up 13 days              8000/tcp, 9443/tcp, 0.0.0.0:9091->9000/tcp, :::9091->9000/tcp                       portainer
```

### 路径{#path}

Portainer 数据目录：*/data/apps/portainer/data/portainer*   

### 端口

除 80, 443 等常见端口需开启之外，以下端口可能会用到：  

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 9091  | 通过 HTTP 访问 Portainer  | 可选   |

### 版本

```shell
curl https://github.com/portainer/portainer/releases |grep Release |grep tag |head -1 |cut -d/ -f6 |cut -c 1-6
```

### 服务

```shell
sudo docker start | restart | stop | stats portainer
```

### 命令行

[Portainer CLI](https://docs.portainer.io/v/ce-2.9/advanced/cli)

### API

[Portainer API](https://docs.portainer.io/v/ce-2.9/api/docs)
