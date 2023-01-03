---
sidebar_position: 1
slug: /cloudbeaver
tags:
  - CloudBeaver
  - Cloud Database Manager
---

# CloudBeaver Getting Started

[CloudBeaver](https://github.com/dbeaver/cloudbeaver) is a web-based database GUI tool which provides rich web interface. Server itself is a Java application, web part is written on TypeScript and React. You can use it to manage PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, DB2, Firebird, H2, Trino 

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-demogui-websoft9.png)

If you have installed Websoft9 CloudBeaver, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for CloudBeaver
4. [Get](./user/credentials) default username and password of CloudBeaver

## CloudBeaver Initialization

### Steps for you

1. Use local browser to access the URL *http://Server's Internet IP*. enter to CloudBeaver wizard
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-wizard001-websoft9.png)

2. Set your username and password, then click 【Next】 button
   ![init CloudBeaver](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-wizard002-websoft9.png)

3. Continue click【Next】 and click 【FINISH】 to complete it
   ![init CloudBeaver](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-wizard003-websoft9.png)

4. You can see a SQlite demo connection now
   ![init CloudBeaver](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-wizard004-websoft9.png)

5. Go to: 【Administrator】>【Connection Management】, delete【SQLite - Chinook (Sample)】 to avoid security trouble
   ![初始化 CloudBeaver](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-wizard005-websoft9.png)

6. Go to home page, you can't see the SQLite demo now

> More guide about CloudBeaver, please refer to [CloudBeaver Documentation](https://cloudbeaver.io/docs/).

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  


## CloudBeaver QuickStart

> 需要了解更多 CloudBeaver 的使用，请参考[官方文档](https://cloudbeaver.io/docs/)


## CloudBeaver Setup

### Manage MySQL

**Prepare**

You should prepare a MySQL service which can be access from you CloudBeaver server.  

If you don't have MySQL service, you can get it from [MySQL application](https://apps.websoft9.com/cloudbeaver) 

**Settings**

1. Login to CloudBeaver console and open: 【Connection】>【Manual】, select **MySQL**
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-conmysql001-websoft9.png)

2. Set the connections: host, port and credential, then click 【Save】button.
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-conmysql002-websoft9.png)

3. Start to enable MySQL connection, you may need to input database username and password
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-conmysql003-websoft9.png)

4. You can manage your MySQL when connect successfully now
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-conmysql004-websoft9.png)

### Manage PostgreSQL

Below we will introduce how to manage PostgreSQL by CloudBeaver

**Prepare**

You should prepare a PostgreSQL service which can be access from you CloudBeaver server.  

If you don't have PostgreSQL service, you can get it from [PostgreSQL application](https://apps.websoft9.com/postgresql) 

**Settings**

1. Login to CloudBeaver console and open: 【Connection】>【Manual】, select **PostgreSQL**
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-openconn-websoft9.png)

2. Set the connections: host, port and credential, then click 【Save】button.
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-connsetting-websoft9.png)

3. Start to enable PostgreSQL connection, you may need to input database username and password
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-conlogin-websoft9.png)

4. You can manage your PostgreSQL when connect successfully now

### Manage SQLServer

Below we will introduce how to manage SQLServer by CloudBeaver

**Prepare**

You should prepare a SQLServer service which can be access from you CloudBeaver server.  

If you don't have SQLServer service, you can get it from [SQLServer application](https://apps.websoft9.com/sqlserver) 

**Settings**

1. Login to CloudBeaver console and open: 【Connection】>【Manual】, select **SQLServer**
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-openconn-websoft9.png)

2. Set the connections: host, port and credential, then click 【Save】button.
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-connsetting-websoft9.png)

3. Start to enable SQLServer connection, you may need to input database username and password
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-conlogin-websoft9.png)

4. You can manage your SQLServer when connect successfully now

### Manage SQLite

Below we will introduce how to manage SQLite by CloudBeaver

**Prepare**

You should prepare a SQLite service which can be access from you CloudBeaver server.  

If you don't have SQLite service, you can get it from [SQLite application](https://apps.websoft9.com/sqlite) 

**Settings**

1. Login to CloudBeaver console and open: 【Connection】>【Manual】, select **SQLite**
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-openconn-websoft9.png)

2. Set the connections: host, port and credential, then click 【Save】button.
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-openconnsqlite-websoft9.png)

3. Start to enable SQLite connection, you may need to input database username and password
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-conlogin-websoft9.png)

4. You can manage your SQLite when connect successfully now

### Manage Oracle Database

Below we will introduce how to manage Oracle by CloudBeaver

**Prepare**

You should prepare a Oracle service which can be access from you CloudBeaver server.  

If you don't have Oracle service, you can get it from [Oracle application](https://apps.websoft9.com/oracledatabase) 

**Settings**

1. Login to CloudBeaver console and open: 【Connection】>【Manual】, select **Oracle**
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-openconn-websoft9.png)

2. Set the connections: host, port and credential, then click 【Save】button.
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-connsetting-websoft9.png)

3. Start to enable Oracle connection, you may need to input database username and password
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-conlogin-websoft9.png)

4. You can manage your Oracle when connect successfully now

### Resetting Password

There are two main measures to reset password.

**Changing password**

Take the steps below:

1. Login to CloudBeaver, Go to【Administrator】>【User】 of top right menu and find your account
  ![CloudBeaver modify password](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-modifypw-websoft9.png)

2. Modify password and click 【Save】

**Forgot Password**

Retrieve your password need to recreate container

1. Use **SSH** to connect CloudBeaver instance

2. Run the below commands
   ```
   cd /data/apps/cloudbeaver
   docker-compose down -v
   docker-compose pull
   docker-compose up -d
   `


### Drivers

[Driver managements](https://cloudbeaver.io/docs/Driver-managements/)

### Export data

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-exportdata-websoft9.png)


## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage CloudBeaver 


通过运行`docker ps`，可以查看到 CloudBeaver 运行时所有的 Container：

```bash
CONTAINER ID   IMAGE                        COMMAND             CREATED       STATUS       PORTS                                       NAMES
34baab38d75f   dbeaver/cloudbeaver:latest   "./run-server.sh"   3 hours ago   Up 3 hours   0.0.0.0:8080->8978/tcp, :::8080->8978/tcp   cloudbeaver
```

下面仅列出 CloudBeaver 本身的参数：

### Path{#path}

* CloudBeaver 配置文件： */data/apps/cloudbeaver/data/cloudbeaver/GlobalConfiguration/.dbeaver/data-sources.json*  

> data-sources.json 存放数据库连接信息

### Port

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 9090   | CloudBeaver 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |

### Version

控制台查看

### Service

```shell
sudo docker start | stop | restart | stats cloudbeaver
```

### CLI

### API

