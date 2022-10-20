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
   cd /data/apps/postgresql && sudo docker compose ls
   ```
2. You can ge the message from SSH "STATUS: running(1) " when PostgreSQL is running

3. Using SSH to connect PostgreSQL Server(or remote to Windows Server), run the following commands

    ```
    $ docker exec -it postgresql bash
    $ psql -d postgresql -U postgresql
    psql (15.0 (Debian 15.0-1.pgdg110+1))
    Type "help" for help.
    
    postgresql=#

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
   sudo docker restart postgresql
   ```

### Password Management

PostgreSQL customer tool can connect PostgreSQL server by **Unix socket** directly, so you can modify your password without authentication

```
$ docker exec -it postgresql bash
$ psql -d postgresql -U postgresql

# modify your password
$ ALTER USER postgres WITH PASSWORD 'postgres';

$ exit psql \q
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


## PostgreSQL reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage PostgreSQL 

Run `docker ps`, view all containers when PostgreSQL is running: 


```bash
CONTAINER ID   IMAGE                   COMMAND                  CREATED         STATUS         PORTS                                            NAMES
7e91744ee643   dpage/pgadmin4:latest   "/entrypoint.sh"         3 seconds ago   Up 1 second    443/tcp, 0.0.0.0:9090->80/tcp, :::9090->80/tcp   pgadmin
9218c5167c4b   postgres:latest         "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp        postgresql```
```

### Path{#path}

PostgreSQL install directory:  */data/apps/postgresql*   
PostgreSQL data directory: */data/apps/postgresql/data/postgres* 

### Port

| Port Number | Purpose | Necessity |
| ------ | ------------------------------------------ --- | ------ |
| 9090 | Access phpPgAdmin via HTTP | Optional |
| 5432 | Remote connection to PostgreSQL | optional |

### Version

```shell
# PostgreSQL version
docker exec -it postgresql psql -V
```

### Service

```shell
sudo docker start | stop | restart | stats postgresql
sudo docker start | stop | restart | stats pgadmin
```

### CLI

Psql is the interactive terminal for working with Postgres. Theres an abundance of flags available for use when working with psql, but lets focus on some of the most important ones, then how to connect

**Connect psql by peer**

```shell

$ docker exec -it postgresql psql --help
psql is the PostgreSQL interactive terminal.

Usage:
  psql [OPTION]... [DBNAME [USERNAME]]
``` -U postgre -h localhost -W
```

### API

[PostgreSQL RESTful API](https://www.postgresql.org/about/news/postgresql-restful-api-1616/)


