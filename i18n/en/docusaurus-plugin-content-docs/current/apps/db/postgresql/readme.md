---
sidebar_position: 1
slug: /postgresql
tags:
  - PostgreSQL
  - Cloud Native Database
---

# PostgreSQL Getting Started

[PostgreSQL](https://www.postgresql.com/products/community/) is a powerful, open source object-relational database system with over 30 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin4-websoft9.png)

If you have installed Websoft9 PostgreSQL, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:9090,5432** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for PostgreSQL
4. [Get](./user/credentials) default username and password of PostgreSQL

## PostgreSQL Initialization

### Steps for you

1. Use the **SSH** to connect Server, and run these command below to view the installation information and running status
   ```
   sudo systemctl status postgresql
   ```
2. You can ge the message from SSH " Active: active (running)... " when PostgreSQL is running

3. Using SSH to connect PostgreSQL Server(or remote to Windows Server), run the following commands

```
sudo -i -u postgres
psql

psql (12.3)
Type "help" for help.

postgres=#
```

4. Login PostgreSQL with GUI tool pgAdmin


### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## Jenkins QuickStart

## PostgreSQL Setup

### Set remote connection{#remote}

If you want to use customer tool (e.g Navicat/pgAdmin) on your local computer to connect PostgreSQL Server, you should set your remote connection first.  

The database is a high-security application, set up remote access, at least two independent steps:

1. Enable **TCP:5432** port on your Cloud Platform

2. Modify the configuration file [postgresql.conf](#path) 
   ```
   #listen_addresses = 'localhost'

   is set to

   listen_addresses = '*'
   ```

3. Modify the configuration file [pg_hba.conf](#path) , add the following line at the end of it
   ```
   host    all             all             0.0.0.0/0            md5
   ```

4. Restart PostgreSQL
   ```
   systemctl restart postgresql
   ```

### Password Management

PostgreSQL customer tool can connect PostgreSQL server by **Unix socket** directly, so you can modify your password without authentication

```
# change to user postgres
sudo -u postgres psql

# modify your password
ALTER USER postgres WITH PASSWORD 'postgres';

#exit psql
\q
```

### GUI-pgAdmin{#pgadmin}

[pgAdmin](https://www.pgadmin.org/) is rich Open Source administration and development platform for PostgreSQL 

pgAdmin is built using Python and Javascript/jQuery. A desktop runtime written in C++ with Qt allows it to run standalone for individual users, or the web application code may be deployed directly on a webserver for use by one or more users through their web browser. 

We will introduce the basic managements about pgAdmin


**Login pgAdmin**

You can login to phpAdmin directly if you have deploy Websoft9 solution of PostgreSQL:

1. Local browser Chrome or Firefox access URL: *http://server's Internet IP:9090*, enter to pgAdmin
   ![login pgAdmin](https://libs.websoft9.com/Websoft9/DocsPicture/en/postgresql/pgadmin-loginui-websoft9.png)

2. Input pgAdmin administrator account([view username and password](./user/credentials)) and enter to console
   ![pgAdmin console](https://libs.websoft9.com/Websoft9/DocsPicture/en/postgresql/pgadmin-console-websoft9.png)


**Install pgAdmin Desktop**

pgAdmin can also used in you local computer:

1. [Download](https://www.pgadmin.org/download/) and install pgAdmin for Windows

2. Click the pgAdmin icon, you can see the pgAdmin running on your default browser

3. Set your pgAdmin master password first
  ![set pgAdmin password](https://libs.websoft9.com/Websoft9/DocsPicture/en/postgresql/pgadmin-setmasterpw-websoft9.png)

**Connect pgAdmin**

Once you have enter to pgAdmin console, you can connect PostgreSQL server now:

1. Click 【server】 to connect PostgreSQL server

2. Set your PostgreSQL database connection ([don't known password](./user/credentials))
  ![set pgAdmin connection](https://libs.websoft9.com/Websoft9/DocsPicture/en/postgresql/pgadmin-createserver-websoft9.png)

2. Login to console successfully
  ![phpPgadmin](https://libs.websoft9.com/Websoft9/DocsPicture/en/postgresql/pgadmin-console-websoft9.png)

**Create database**

1. Right mouse click 【Servers】>【Create】>【Database】, create new database
  ![pgAdmin create database](https://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin-createdb-websoft9.png)

2. Set your database name, Encoding..., then create it

**Create user**

PostgreSQL roles is similar with users

1. Right mouse click 【Servers】>【Create】>【Login/Group Role】, create new user
  ![pgAdmin create user](https://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin-createroles-websoft9.png)

2. Set your database username, password..., then create it

**Backup database**

1. Select the database you want to export, click 【Backup】button
  ![pgAdmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin-backupdb-websoft9.png)

2. Start you backup


## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage PostgreSQL 

通过运行`docker ps`，可以查看到 PostgreSQL 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```

下面仅列出 PostgreSQL 本身的参数：

### Path{#path}

PostgreSQL 配置文件目录: */data/postgresql/config*   
PostgreSQL 数据目录：*/data/postgresql/pgdata*   
PostgreSQL 日志目录: */data/postgresql/log*  

PostgreSQL 有两个重要的全局配置文件：

* postgresql.conf 主要负责配置文件位置、资源限制、集群负责等
* pg_hba.conf 主要负责客户端的连接和认证


### Port

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 9090   | 通过 HTTP 访问 phpPgAdmin	 | 可选   |
| 5432   | 远程连接PostgreSQL | 可选   |


### Version

```shell
# PostgreSQL version
psql -V
```

### Service

```shell
sudo systemctl start | stop | restart | status postgresql
sudo docker start | stop | restart | stats pgadmin
```

### CLI

Psql is the interactive terminal for working with Postgres. Theres an abundance of flags available for use when working with psql, but lets focus on some of the most important ones, then how to connect

**Connect psql by peer**

```shell
cd /usr/bin
su postgres
psql
```

**Connect psql from remote**

Enable the remote connection of PostgreSQL, then connect it
```shell
psql -U postgre -h localhost -W
```

### API

[PostgreSQL RESTful API](https://www.postgresql.org/about/news/postgresql-restful-api-1616/)


