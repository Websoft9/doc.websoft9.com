---
sidebar_position: 1
slug: /gogs
tags:
  - Gogs
  - DevOps
---

# Gogs Getting Started

[Gogs](https://github.com/gogs/gogs) 是一款极易搭建的自助 Git 仓库系统，相对于 GitLab 而言 Gogs 更加轻量级。 

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-guistart-websoft9.png)

If you have installed Websoft9 Gogs, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Gogs.
4. [Get](./user/credentials) default username and password of Gogs

## Gogs Initialization

### Steps for you

1. 使用本地电脑浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入初始化页面

2. 填写数据库连接信息（**[查看预装的数据库账号密码](./user/credentials)** ）

   - 数据库类型： MySQL
   - 数据库主机名填写：mysql:3306

    ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/gogs/gogs-installdb-websoft9.png)

2. 设置 Gogs 的应用基本参数   

   - 域名：公网IP 或 真实域名
   - SSH 端口： 10022， 可从 Gogs 根目录 .env 文件中查询
   - HTTP 端口： 80 或 3000，可从 Gogs 根目录 .env 文件中查询
   - 应用 URL：http://公网IP  或  http://域名:http端口

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/gogs/gogs-installset-websoft9.png)

3. 设置管理账号  

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/gogs/gogs-installadmin-websoft9.png)

4. 安装成功后，直接跳转到后台界面 

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/gogs/gogs-installss-websoft9.png)


### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

**安装的时候忘记设置管理账号？**  

创建管理员帐号并不是必须的，因为用户表中的第一个用户将自动获得管理员权限。


## Gogs QuickStart

## Gogs Setup

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Gogs

通过运行 `docker ps`，查看 Gogs 运行时所有的服务组件：   

```bash
CONTAINER ID   IMAGE               COMMAND                  CREATED          STATUS                    PORTS                                                                                NAMES
3cc976ef4fd5   mysql:5.7           "docker-entrypoint.s…"   19 minutes ago   Up 19 minutes             3306/tcp, 33060/tcp                                                                  gogs-db
d1bf1977d72b   gogs/gogs:latest    "/app/gogs/docker/st…"   19 minutes ago   Up 19 minutes (healthy)   0.0.0.0:3000->3000/tcp, :::3000->3000/tcp, 0.0.0.0:10022->22/tcp, :::10022->22/tcp   gogs
```


### Path{#path}

Gogs installation directory: */data/apps/gogs* 

### Port

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 3000   | Gogs 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |
| 10022   | Gogs SSH 端口 | 可选   |

### Version

```shell
docker inspect gogs | grep com.docker.compose.version
```

### Service

```shell
sudo docker start | stop | restart | stats gogs
```

### CLI

```
$ ./gogs -h
NAME:
   Gogs - A painless self-hosted Git service

USAGE:
   gogs [global options] command [command options] [arguments...]

VERSION:
   0.13.0+dev

COMMANDS:
   web      Start web server
   serv     This command should only be called by SSH shell
   hook     Delegate commands to corresponding Git hooks
   cert     Generate self-signed certificate
   admin    Perform admin operations on command line
   import   Import portable data as local Gogs data
   backup   Backup files and database
   restore  Restore files and database from backup
   help, h  Shows a list of commands or help for one command

GLOBAL OPTIONS:
   --help, -h     show help
   --version, -v  print the version


### API

Refer to ：[Webhook](https://gogs.io/docs/features/webhook)

