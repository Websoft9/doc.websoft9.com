---
sidebar_position: 1
slug: /gogs
tags:
  - Gogs
  - DevOps
---

# 快速入门

[Gogs](https://github.com/gogs/gogs) 是一款极易搭建的自助 Git 仓库系统，相对于 GitLab 而言 Gogs 更加轻量级。 

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-guistart-websoft9.png)



部署 Websoft9 提供的 Gogs 之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80和10022** 端口已经开启
3. 在服务器中查看 Gogs 的 **[默认管理员账号和密码](./user/credentials)**  
4. 若想用域名访问  Gogs，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程

## Gogs 安装向导

### 详细步骤

1. 使用本地电脑浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入初始化页面

2. 填写数据库连接信息（**[查看预装的数据库账号密码](./user/credentials)** ）

   - 数据库类型： MySQL
   - 数据库主机名填写：mysql:3306

    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-installdb-websoft9.png)

2. 设置 Gogs 的应用基本参数   

   - 域名：公网IP 或 真实域名
   - SSH 端口： 10022， 可从 Gogs 根目录 .env 文件中查询
   - HTTP 端口： 80 或 9001，可从 Gogs 根目录 .env 文件中查询
   - 应用 URL：http://公网IP  或  http://域名:http端口

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-db-websoft9.png)

3. 设置管理账号  

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-admin-websoft9.png)

4. 安装成功后，直接跳转到后台界面 

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-installss-websoft9.png)


### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。

**安装的时候忘记设置管理账号？**  

创建管理员帐号并不是必须的，因为用户表中的第一个用户将自动获得管理员权限。


## Gogs 常用操作

### 设置语言

页面右下方点击语言项可快速设置多国语言。  

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-language-websoft9.png)

## Gogs 参数

Gogs 应用中包含 Docker, MySQL 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。 

通过运行 `docker ps`，查看 Gogs 运行时所有的服务组件：   

```bash
CONTAINER ID   IMAGE              COMMAND                  CREATED          STATUS                    PORTS                                                                                NAMES
1146da16e5e7   mysql:5.7          "docker-entrypoint.s…"   18 minutes ago   Up 18 minutes             3306/tcp, 33060/tcp                                                                  gogs-db
2ad58951f177   gogs/gogs:latest   "/app/gogs/docker/st…"   18 minutes ago   Up 18 minutes (healthy)   0.0.0.0:10022->22/tcp, :::10022->22/tcp, 0.0.0.0:9001->3000/tcp, :::9001->3000/tcp   gogs```

### 路径{#path}

Gogs 安装目录: */data/apps/gogs* 
Gogs 数据目录: */data/apps/gogs/src/gogs_data* 

### 端口

除 80, 443 等常见端口需开启之外，以下端口可能会用到：  

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 10022   | Gogs SSH 端口 | 可选   |

### 版本

```shell
sudo docker exec -it gogs ./gogs --version
```

### 服务

```shell
sudo docker start | stop | restart | stats gogs
```

### 命令行

```
$ sudo docker exec -it gogs ./gogs -h
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
```

### API

参考：[Web 钩子](https://gogs.io/docs/features/webhook)

