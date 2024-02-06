---
title: MongoDB
slug: /mongodb
tags:
  - 文档数据库
  - 云数据库
  - JASON
---

import Meta from './_include/mongodb.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 MongoDB 后，通过【我的应用】进入它的编辑窗口，在**访问**标签页中获取登录地址和账号。  

### 命令行连接

1. 进入 MongoDB 容器中，运行 MongoDB Shell 命令
   ~~~
   $ mongosh admin -u root -p YOURPASSWORD
   MongoDB shell version v5.0.10
   connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
   ...
   ~~~

2. 分别列出默认数据库和用户
   ```
   # 列出所有数据库
   show dbs

   # 切换到 admin 数据库，列出所有用户
   use admin
   show users
   ```

### 图形化 Web 端

Websoft9 提供了一个基于 Web 访问的 [MongoDB Compass](./mongocompass#wizard) 应用。


### 规划数据模型

MongoDB 作为一种数据库，与传统的 RDBMS 的使用方式也有相似之处，即规划数据模型，建立数据库范式。只有这种，才能更好的发挥数据库的性能。  

![](http://libs.websoft9.com/Websoft9/DocsPicture/en/mongodb/mongodb-datamodel-websoft9.png)

数据规划的主要设计要点包括：

* 使用数据范式
* 使用嵌入式文档反范式
* 使用固定集合
* 考虑文档增大
* 规划索引、分片和复制
* 规划数据生命周期


### 命令速查

下面列出最常用的 MongoDB 命令供用户参考：  

#### 显示、创建和切换数据库

```shell

> show dbs
admin     0.000GB
config    0.000GB
local     0.000GB

# 创建test数据库（如果不存在test数据库，就会自动创建它）
> use test
switched to db test

# 显示当前数据库
> db
test

# 显示当前所有用户数据
> show users

#3 插入数据到数据库
> db.test.insert({"name":"company"})
WriteResult({ "nInserted" : 1 })
```


#### 删除数据库
```
> show dbs
admin     0.000GB
config    0.000GB
local     0.000GB
test      0.000GB
websoft9  0.000GB

> use test
switched to db test
> use test
> db.dropDatabase()
{ "dropped" : "test", "ok" : 1 }
> show dbs
admin     0.000GB
config    0.000GB
local     0.000GB
websoft9  0.000GB
```

#### 创建管理员账号

```
> mongo
> use admin
switched to db admin
> db.createUser( { user: "webs_admin", pwd: "websoft9", roles: ["userAdminAnyDatabase"] } )
Successfully added user: { "user" : "webs_admin", "roles" : [ "userAdminAnyDatabase" ] }


# 显示账号
> show users
{
        "_id" : "admin.webs_admin",
        "user" : "webs_admin",
        "db" : "admin",
        "roles" : [
                {
                        "role" : "userAdminAnyDatabase",
                        "db" : "admin"
                }
        ],
        "mechanisms" : [
                "SCRAM-SHA-1",
                "SCRAM-SHA-256"
        ]
}
```


## 配置选项{#configs}
  
- [配置文件](https://docs.mongodb.com/v4.0/reference/configuration-options/#conf-file)：*/path/src/mongod.conf*  
   ```
    processManagement:
      fork: true
    net:
      bindIp: localhost
      port: 27017
    storage:
      dbPath: /var/lib/mongo
    systemLog:
      destination: file
      path: "/var/log/mongodb/mongod.log"
      logAppend: true
    storage:
      journal:
          enabled: true
  ```
- 服务端命令：`mongod`
- 开启公网访问：配置文件 `bindIp: 0.0.0.0` 配置段
- MongoDB Shell 是 MongoDB 自带 JavaScript shell，有两种方式与数据库进行交互：
  * 命令行交互式操作
  * 运行存放在文件中的命令脚本（例如：shell_script.js）


## 管理维护{#administrator}

### 关闭 MongoDB 访问认证

默认情况下 MongoDB 容器认证已开启，如需关闭认证，删除容器中的账号类环境变量

### 修改密码

参考下面的命令，修改已经创建的管理员账号root的密码

  ```
    $ docker exec -it mongodb mongo admin -u root -p YOURPASSWORD
    MongoDB shell version v4.0.18
    connecting to: mongodb://127.0.0.1:27017/?gssapiServiceName=mongodb
    > db = db.getSiblingDB('admin')
    admin
    > db.changeUserPassword("root", "NEWPASSWORD")
    > exit
  ```

### 忘记管理员密码

1. Websoft9 控制台修改**编排文件**，注释 **MONGO_INITDB_** 开头的环境变量，重建应用

2. 进入 mongodb 容器中运行重置密码命令
   ```
   mongo
   > db = db.getSiblingDB('admin')
   admin
   > db.changeUserPassword("root", "NEWPASSWORD")
   ```
3. 复原编排文件，重建应用

### 备份

**mongodump** 和 **mongorestore** 是自带的 MongoDB 备份与恢复工具（[MongoDB Backup Methods](https://docs.mongodb.com/manual/core/backups/) ）

1. 进入 MongoDB 容器
2. 使用 **mongodump** 工具，导出数据库
   ```
   # 备份
   mongodump --authenticationDatabase admin --username root --password PASSWORD -d DATABASE_NAME -h localhost
   ```
3. 使用 **mongorestore** 工具，恢复数据库
   ```
   mongorestore --authenticationDatabase admin --username root --password PASSWORD PATH_TO_BACKUP_FILE
   ```


## 故障

#### MongoDB compass 无法连接？

端口，bindIP 和账户认证等连接字段是否满足条件

## 问答

#### MongoDB 的 Client 和 Server？

MongoDB Server 是指 MongoDB 程序本体，而 MongoDB Client 指采用TCP协议用于连接程序本地的客户端。它们是两个完全不同的程序，也就是说它们并需要同时安装到同一台服务上。

#### mongod vs mongo 命令？

- mongod 是 MongoDB 的服务端管理命令，用于启动数据库服务。  
- mongo 是用于访问 MongoDB 服务的客户端。  

#### 可否无身份验证？

可以，默认安装时 MongoDB 开启了[访问控制](https://docs.mongodb.com/manual/tutorial/enable-authentication/)，当关闭认证后无需 MongoDB 用户名密码就可以访问。

#### admin 数据库是什么？

安装 MongoDB 时会默认包含一个 admin 数据库，如果你创建管理员账户就必须存储到这个 admin 中

#### 官方有哪些工具？

MongoDB 官方主要工具如下：

**MongoDB Atlas Open Service Broker**  
学习如何使用Atlas Open Service Broker在Kubernetes内部署Atlas集群和管理数据库用户。

**MongoDB BI Connector**  
MongoDB BI连接器参考指南。学习如何使用商业智能工具和SQL查询存储在MongoDB中的数据。

**MongoDB Charts**  
MongoDB图表参考指南。学习如何快速轻松地创建MongoDB数据的可视化。 

**MongoDB Command Line Interface**  
学习如何使用MongoDB命令行界面与MongoDB部署快速交互，以简化测试和脚本编写。

**MongoDB Compass**  
MongoDB Compass参考指南。学习使用MongoDB Compass的图形用户界面查看和分析存储在MongoDB中的数据。 

**MongoDB Database Tools**  
用于与MongoDB集群接口的工具，如导入/导出数据。 

**MongoDB Kafka Connector**  
学习如何将Kafka主题中的数据持久化为MongoDB中的数据接收器，以及如何将MongoDB的更改发布为Kafka topics中的数据源。

**MongoDB Kubernetes Operator**  
学习如何使用Kubernetes操作符在Kubernete上运行MongoDB Enterprise，并配置Cloud或Ops Manager进行备份和监控。

**MongoDB Spark Connector**  
MongoDB火花连接器参考指南。了解如何将MongoDB与Apache Spark结合使用。


#### 什么是 NoSQL？

NoSQL 即 Not only SQL的简称，并非 Not SQL，也即意味着 NoSQL 数据库也有着类似 SQL 的查询概念。 NoSQL 是一个包罗万象的术语，涵盖了除传统的关系型数据库（RDBMS）之外的所有数据库。NoSQL 试图放弃关系型数据库的传统结构，让开发人员能够以更接近系统数据流需求的方式实现模型。当前有多种不同的 NoSQL 技术，包括：

* 文档存储数据库
* 健/值数据库
* 列存储数据库
* 图存储数据库

MongoDB 就属于文档存储数据库的杰出代表。文档数据库采用面向文档的方法存储数据，其背后的理念是，可以将单个实体的所有数据存放在一个文档中，而文档以**集合**的形式组合起来。  

MongoDB 采用 BSON（一种轻量级的二进制JSON）格式存储数据，每个文档最大不能超过16MB，避免查询占用太多内存或频繁访问文件系统，因此性能非常高。

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mongodb/mongodb-gui-websoft9.png)

#### SQL vs MongoDB ？

MongoDB中的基本概念是文档、集合和数据库。让我们以SQL为例，帮助您更好地理解MongoDB。

| SQL Term/concept | MongoDB Term/concept | explain |
| :--- | :--- | :--- |
| database | database | Database Instance |
| table | collection | databae table/collection |
| row | document | table row/document |
| column | field | Data field/domain |
| index | index | index |
| table joins |   | MongoDB no this |
| primary key | primary key | keyPrimary key, MongoDB automatically sets the _id field as the primary key |

通过下面的例子，我们还可以更直观地理解Mongo中的一些概念：

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mongodb/nosqlvssql-websoft9.png)

#### MongoDB 有哪些数据类型？

MongoDB 的数据类型非常类似 JavaScript 对象。

**字符串** - 这是用于存储数据的最常用的数据类型。MongoDB中的字符串必须为`UTF-8`。

**整型** - 此类型用于存储数值。 整数可以是`32`位或`64`位，具体取决于服务器。

**布尔类型** - 此类型用于存储布尔值(`true` / `false`)值。

**双精度浮点数** - 此类型用于存储浮点值。

**最小/最大键** - 此类型用于将值与最小和最大`BSON`元素进行比较。

**数组** - 此类型用于将数组或列表或多个值存储到一个键中。

**时间戳** - `ctimestamp`，当文档被修改或添加时，可以方便地进行录制。

**对象** - 此数据类型用于嵌入式文档。

**对象** - 此数据类型用于嵌入式文档。

**Null** - 此类型用于存储`Null`值。

**符号** - 该数据类型与字符串相同; 但是，通常保留用于使用特定符号类型的语言。

**日期** - 此数据类型用于以UNIX时间格式存储当前日期或时间。您可以通过创建日期对象并将日，月，年的日期进行指定自己需要的日期时间。

**对象ID** - 此数据类型用于存储文档的ID。

**二进制数据** - 此数据类型用于存储二进制数据。

**代码** - 此数据类型用于将JavaScript代码存储到文档中。

**正则表达式** - 此数据类型用于存储正则表达式。

### 数据库、用户和角色关系？

通过阅读下面的代码理解用户、数据库和角色的关系

```
use reporting
db.createUser(
  {
    user: "reportsUser",
    pwd: "12345678",
    roles: [
       { role: "read", db: "reporting" },
       { role: "read", db: "products" },
       { role: "read", db: "sales" },
       { role: "readWrite", db: "accounts" }
    ]
  }
)
```
对 MongoDB 来说，每个用户都存在一个数据库中（区别于 MySQL 中所有的用户存储在一个系统数据库中）  

系统默认，会自动创建 admin 数据库，这是一个特殊数据库，提供了普通数据库没有的功能，对于具备全局管理权限的数据库用户，必须存储在这个 admin 数据中。

