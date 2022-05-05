---
sidebar_position: 1
slug: /sqlite
tags:
  - SQLite
  - DevOps
---

# 快速入门

[SQLite](https://sqlite.org) 是一个 C 语言库，它实现了一个小型、快速、自包含、高可靠性、功能齐全的 SQL 数据库引擎。SQLite 是世界上使用广泛的数据库引擎之一。SQLite 内置于所有手机和大多数计算机中，并捆绑在人们每天使用的无数其他应用程序中。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlite/sqlite-gui-websoft9.png)


## 准备

部署 Websoft9 提供的 SQLite 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:9090** 端口已经开启
3. 在服务器中查看 SQLite 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  SQLite，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程


## SQLite 初始化向导

### 详细步骤

1. 使用 SSH 工具，连接到服务器

2. 运行 `sqlite3` 命令，显然类型下面的结果，即表明运行正常
   ```
   [root@VM-0-11-centos ~]# sqlite3
   SQLite version 3.29.0 2019-07-10 17:32:03
   Enter ".help" for usage hints.
   Connected to a transient in-memory database.
   Use ".open FILENAME" to reopen on a persistent database.
   sqlite>
   ```

3. 验证 [SQLite 可视化](#gui)管理工具

> 需要了解更多 SQLite 的使用，请参考官方文档：[SQLite 教程](https://www.sqlite.net.cn/tutorial/2.html)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。


## SQLite 使用入门

下面以 **SQLite 程序连接** 作为一个任务，帮助用户快速入门：

## SQLite 常用操作

### 程序连接

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

### 图形化工具{#gui}

本部署方案中预装 SQLite 数据库管理工具 `CloudBeaver` 。  

下面我们完成的介绍如何使用可视化工具管理 SQLite。

#### 准备

1. 使用 SSH 连接 SQLite 所在的服务器，在 [SQLite 数据文件目录](#path)下创建一个数据库
   ```
   # 创建数据库
   cd /data/apps/cloudbeaver/volumes
   sqlite3 testDB.db
   
   # 增加表
   sqlite> CREATE TABLE COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL
   )
   ```

2. 登录云控制台，开启服务器 安全组 9090 端口

3. 完成 [CloudBeaver 初始化](./cloudbeaver)


#### 配置

完成上述准备工作后，我们开始连接 SQLite 数据库：  

1. 登录 CloudBeaver 控制台，打开：【Connection】>【Manual】，选择 **SQLite**
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-openconn-websoft9.png)

2. 参考下面的建议，设置连接信息，然后点击【Save】

   - Driver 保持默认的 SQLite
   - Connection Name 设置为一个便于识别的名字即可
   - Database 为 SQLite 数据库文件的路径，路径前缀必须是：**/opt/cloudbeaver/workspace/**，再接上文件名称

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-openconnsqlite-websoft9.png)

3. 设置信息保存后，使用这个 SQLite 连接，输入数据库的账号和密码
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-conlogin-websoft9.png)

4. 成功连接到 SQLite，发现可以看到之前创建的 Company 表
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-listtable-websoft9.png)

## SQLite 参数

SQLite 应用中包含 Nginx, Docker, CloudBeaver 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。

通过运行 `docker ps`，可以查看到 SQLite 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 SQLite 本身的参数：

### 路径{#path}

SQLite 可执行程序： */usr/bin/sqlite3*  
SQLite 数据库文件目录： */data/apps/cloudbeaver/volumes*  

### 端口

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 9090   | 通过 HTTP 访问 SQLite 可视化工具台 | 可选   |

### 版本

```shell
sqlite3 --version
```

### 命令行

SQLite 提供了强大的的命令行工具 `sqlite3`  

##### 程序命令行

```
# 创建数据库
sqlite3 testDB.db

# 查看帮助
sqlite3 --help

# 查看版本
sqlite3 --version
```

##### 交互式命令行

以 `sqlite3 testDB.db` 命令，进入 SQLite 运行状态后，开始使用数据库交互式命令行

```
# 获取帮助
sqlite> .help

# 查询数据库列表
sqlite> .database

# 附件一个数据库。
# 数据库名称 main 和 temp 被保留用于主数据库和存储临时表及其他临时数据对象的数据库，不可用于附加
sqlite> ATTACH DATABASE 'myDB.db' as 'TEST'

# 创建表
sqlite> CREATE TABLE COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL
)

# 查询表
sqlite> .tables

````

### API


