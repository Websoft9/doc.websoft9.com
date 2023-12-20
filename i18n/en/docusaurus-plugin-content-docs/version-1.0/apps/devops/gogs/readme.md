---
sidebar_position: 1
slug: /gogs
tags:
  - Gogs
  - DevOps
---

# Gogs Getting Started

[Gogs](https://gogs.io/) is a painless self-hosted Git service.This project aims to build a simple, stable and extensible self-hosted Git service that can be setup in the most painless way. With Go, this can be done with an independent binary distribution across ALL platforms that Go supports, including Linux, macOS, Windows and ARM. 

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-guistart-websoft9.png)

If you have installed Websoft9 Gogs, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Gogs.
4. [Get](./user/credentials) default username and password of Gogs

## Gogs Initialization

### Steps for you

1. Using local Chrome or Firefox to visit the URL https://DNS or https://Server's Internet IP, you can access the initialization page.

2. Connect to the database（**[default username and password](./user/credentials)** ）

   - Database Type： MySQL
   - Host：gogs-db

    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-db-websoft9.png)

2. Set the Gogs parameters   

   - Domain：Public IP or DNS
   - SSH Port： 10022 (Can be obtained or modified from the Gogs root .env file)
   - HTTP Port： 80 
   - Application URL：http://IP  or  http://DNS

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-admin-websoft9.png)

3. Set up an administrative account  

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-installadmin-websoft9.png)

4. Complete the settings and enter the Dashboard

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-dashboard-websoft9.png)


### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  


## Gogs QuickStart

## Gogs Setup

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Gogs

Run `docker ps` command, view all Containers when Gogs is running:：   

```bash
CONTAINER ID   IMAGE               COMMAND                  CREATED          STATUS                    PORTS                                                                                NAMES
3cc976ef4fd5   mysql:5.7           "docker-entrypoint.s…"   19 minutes ago   Up 19 minutes             3306/tcp, 33060/tcp                                                                  gogs-db
d1bf1977d72b   gogs/gogs:latest    "/app/gogs/docker/st…"   19 minutes ago   Up 19 minutes (healthy)   0.0.0.0:3000->3000/tcp, :::3000->3000/tcp, 0.0.0.0:10022->22/tcp, :::10022->22/tcp   gogs
```


### Path{#path}

Gogs installation directory: */data/apps/gogs* 

### Port

| Port | Use                                          | Necessity |
| ------ | --------------------------------------------- | ------ |
| 10022  | Gogs SSH | Optional   |

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

