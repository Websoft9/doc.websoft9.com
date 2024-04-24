---
sidebar_position: 1
slug: /sqlite
tags:
  - SQLite
  - DevOps
---

# SQLite Getting Started

[SQLite](https://sqlite.org) is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. SQLite is the most used database engine in the world. SQLite is built into all mobile phones and most computers and comes bundled inside countless other applications

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/sqlite/sqlite-gui-websoft9.png)


If you have installed Websoft9 SQLite, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:9090** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for SQLite
4. [Get](./user/credentials) default username and password of SQLite

## Jenkins Initialization

### Steps for you

1. Use **SSH** tool to connect Instance

2. Running the command `sqlite3`, you can see the below information
   ```
   [root@VM-0-11-centos ~]# sqlite3
   SQLite version 3.29.0 2019-07-10 17:32:03
   Enter ".help" for usage hints.
   Connected to a transient in-memory database.
   Use ".open FILENAME" to reopen on a persistent database.
   sqlite>
   ```
3. Verify [SQLite Web-based GUI](#gui) tool

> More guide about SQLite, please refer to [SQLite Documentation](https://sqlite.org/docs.html).

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  


## SQLite QuickStart

下面以 **SQLite 程序连接** 作为一个任务，帮助用户快速入门：

## SQLite Setup

### Connect Database to Application

开发需要连接 SQLite，首先需要保证已经安装了对应的 SQlite 连接模块：

* PHP 默认安装并启用了 SQLite 扩展
* Python  默认安装了 SQLite 模块
* Java 需自行安装[SQLite JDBC Driver](https://github.com/xerial/sqlite-jdbc/releases)

下面是一个典型的 PHP 连接 SQLite 的程序段：

```
<?php
   class MyDB extends SQLite3
   {
      function __construct()
      {
         $this->open('test.db');
      }
   }
   $db = new MyDB();
   if(!$db){
      echo $db->lastErrorMsg();
   } else {
      echo "Opened database successfully\n";
   }
?>
```

### Web-based GUI{#gui}

This deployment solution of SQLite includes web-based GUI tool `CloudBeaver`. 

We will show you how to manage SQLite by CloudBeaver below:  

**Prepare**

1. Use **SSH** to connect SQLite instance and create a database at [SQLite data file directory](#path)
   ```
   # Create database file
   cd /data/apps/cloudbeaver/volumes
   sqlite3 testDB.db
   
   # Add a table
   sqlite> CREATE TABLE COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL
   )
   ```

2. Login your Cloud Platform, and Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:9090** is allowed.

3. Complete [CloudBeaver installation wizard](./cloudbeaver)

**Connect Database**

Let's start to connect SQLite if we complete preparation:  

1. Login to CloudBeaver console and open: 【Connection】>【Manual】, select **SQLite**
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-openconn-websoft9.png)

2. Configure it as below and click 【Save】 button

   - **Driver** is SQLite by default
   - **Connection Name** can by any name if you want
   - **Database** must use the path as: */opt/cloudbeaver/workspace/* and with filename

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-openconnsqlite-websoft9.png)

3. Start to enable SQLite connection, you may need to input database username and password
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-conlogin-websoft9.png)

4. You can see the table you created when you connect SQLite successfully
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-listtable-websoft9.png)


## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage SQLite 

通过运行 `docker ps`，可以查看到 SQLite 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 SQLite 本身的参数：

### Path{#path}

SQLite 可执行程序： */usr/bin/sqlite3*  
SQLite 数据库文件目录： */data/apps/cloudbeaver/volumes*  

### Port

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 9090   | 通过 HTTP 访问 SQLite 可视化工具台 | 可选   |

### Version

```shell
sqlite3 --version
```

### CLI

SQLite provide `sqlite3` for user

**Manage command**

```
# Create a database
sqlite3 testDB.db

# Get help
sqlite3 --help

# Check version
sqlite3 --version
```

**Interactive command**

Run `sqlite3 testDB.db` command and go to SQLite interactive command status

```
# Get help
sqlite> .help

# Check database list
sqlite> .database

# Attach a database
sqlite> ATTACH DATABASE 'myDB.db' as 'TEST'

# Create table
sqlite> CREATE TABLE COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL
)

# Query table
sqlite> .tables
```
### API


