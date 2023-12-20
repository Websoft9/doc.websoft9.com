---
sidebar_position: 1
slug: /portainer
tags:
  - Docker
  - DevOps
---

# Portainer Getting Started

[Portainer](https://www.portainer.io) was developed to help customers adopt Docker container technology and accelerate time-to-value. It has never been so easy to build, manage and maintain your Docker environments. Portainer is easy to use software that provides an intuitive interface for both software developers and IT operations. Portainer gives you a detailed overview of your Docker environments and allows you to manage your containers, images, networks and volumes. Portainer is simple to deploy - you are just one Docker command away from running Portainer anywhere.


![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/docker/portainer/portainer-sc001-websoft9.png)

If you have installed Websoft9 Portainer, the following steps is for your quick start


## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:9000** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Portainer
4. 如果你部署了包含 Portainer 的Docker环境，请直接登录使用。否则，请先安装 Portainer：
    ~~~
    #通过命令安装 Portainer

    docker volume create portainer_data
    docker run -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
    cd /usr/libexec/docker/
    sudo ln -s docker-runc-current docker-runc
    ~~~

## Portainer Initialization

### Steps for you

If you have deployed the Portainer, please login it directly. Otherwise, please install it first referring to the commands below:

~~~
#Commands for installing Portainer

docker volume create portainer_data
docker run -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
cd /usr/libexec/docker/
sudo ln -s docker-runc-current docker-runc
~~~

1. Use local Chrome or Firefox to visit: *http://Internet IP:9000* , enter to Portainer GUI
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/docker/portainer/portainer-login-websoft9.png)

2. Set the administrator username and password, then click【Create user】

3. Select teh 【Local】for connection, then click the 【Connect】
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/docker/portainer/portainer-loginconnect-websoft9.png)

4. Now, you can see the Portainer console and click 【Local】to configure Portainer
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/docker/portainer/portainer-bkselect-websoft9.png)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## Portainer QuickStart

下面以部署一个 WordPress 网站为场景，描述 Portainer 的使用：  

**Start MySQL Container**

The following details the deployment of MySQL through Portainer:

1. Login Portainer, open【Containers】>【Add container】
    ![createcontainer](http://libs.websoft9.com/Websoft9/DocsPicture/zh/potainer/portainer-addcontainer-websoft9.png)

2. Set the parameters required for container operation (shown below and describe key settings)
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/potainer/portainer-mysql-websoft9.png)

   * Name: define your container name
   * Image: image name in [DockerHub](https://hub.docker.com/)
   * Network ports configuration：suggest your enable【Publish all exposed network ports...】
   * Env: variable of image, e.g. the root password**MySQL_ROOT_PASSWORD** is required variable. More variable please read the [ MySQL image docs](https://hub.docker.com/_/mysql)
   * Restart policy：suggest your select 【Always】

3. Click【Deploy the container】 to start Container
    
4. If you want to connect MySQL remotely, please enable your Server's Port 3306 of Security Group

**Start WordPress Container**

The following details the deployment of WordPress through Portainer and WordPress installation:

1. Login Portainer, open【Containers】>【Add container】
   ![createcontainer](http://libs.websoft9.com/Websoft9/DocsPicture/zh/potainer/portainer-addcontainer-websoft9.png)

2. Set the parameters required for container operation (shown below and describe key settings) 
   ![wordpress](http://libs.websoft9.com/Websoft9/DocsPicture/zh/potainer/portainer-wordpress-websoft9.png)

   * Name: define your container name
   * Image: image name in [DockerHub](https://hub.docker.com/)
   * Network ports configuration：suggest your enable【Publish all exposed network ports...】
   * Env: suggest you set the MySQL variables for container at this step
   * Restart policy：suggest your select 【Always】

3. Click【Deploy the container】 to start Container
    
4. Use you local Firefox or Chrome to visit: *http://Internet IP:port* you can see the WordPress installation interface
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/potainer/portainer-startinstall-1-websoft9.png)

5. If you want to use the MySQL container for WordPress, Database host format is **Internet IP:port**  
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/docker/portainer/wp04.png)



**Nginx 容器绑定域名**

以上一章节中的 Wordpress 网站作为示例，在 WordPress 部署完成后，需要在浏览器内输入 *`http://公网IP地址：端口`* 的形式访问网站，但我们不加端口就能访问域名，所以这时就要用到 Nginx 的端口转发功能。  

我们使用使用一款可视化的 Nginx 管理器：[Nginx Proxy Manager](https://hub.docker.com/r/jc21/nginx-proxy-manager)


**FileBrowser 容器管理文件**

1. 进入到 Portainer 页面，选择左边的 **App Templates** 选项，往下找到 **File browser** 容器模板，单击选择；
    ![filebowser-1](http://libs.websoft9.com/Websoft9/DocsPicture/zh/potainer/portainer-filebrowser-1-websoft9.png)
2. 按照下图创建 File browser 容器；
    ![filebowser-2](http://libs.websoft9.com/Websoft9/DocsPicture/zh/potainer/portainer-filebrowser-2-websoft9.png)
3. 进入到容器列表，单击刚刚创建的 File browser 容器，点击 **Duplicate/Edit** 按钮，进入到修改容器信息页面；
    ![filebowser-3](http://libs.websoft9.com/Websoft9/DocsPicture/zh/potainer/portainer-filebrowser-3-websoft9.png)
4. 按照下图，将 File browser 的 volume 值修改为 和 Nginx 的 volume 值相同；
    ![filebowser-4](http://libs.websoft9.com/Websoft9/DocsPicture/zh/potainer/portainer-filebrowser-4-websoft9.png)

## Portainer Setup

### 运行容器命令

在此以连接到 MySQL 容器为例进行说明：

1. 返回到容器列表，点击下图中 MySQL 的 **Quick actions** 一栏下的 **>_** 图标；
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/potainer/portainer-containerlist-websoft9.png)
2. 在新打开的页面，点击 **Connetc** 按钮，连接到容器；
    ![](http://libs-websoft9-com.oss-cn-qingdao.aliyuncs.com/Websoft9/DocsPicture/zh/potainer/portainer-createdatabase-websoft9.png)
3. 接下来就可以在命令窗口中输入```mysql -uroot -ppassword;"```,其中 “password” 为您在自己设置的数据库密码，这样就可以开始使用数据库命令对 MySQL 进行管理了；


## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Portainer

下面仅列出 Portainer 本身的参数：

### Path{#path}

Portainer 数据卷：*/var/lib/docker/volumes/portainer_data/_data*   


### Port

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 9000   | 通过 HTTP 访问 Portainer  | 必选   |

### Version

```shell
sudo docker respect portainer
```

### Service

```shell
sudo docker start | restart | stop | stats portainer
```

### CLI

[Portainer CLI](https://docs.portainer.io/v/ce-2.9/advanced/cli)

### API

[Portainer API](https://docs.portainer.io/v/ce-2.9/api/docs)
