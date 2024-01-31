---
sidebar_position: 3
slug: /mongodb/admin
tags:
  - MongoDB
  - Cloud Native Database
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup) 相关章节。

## 场景

### MongoDB 应用备份

运行下列命令，可将数据文件备份在 MongoDB 应用目录下列文件夹：data/mongo_data/dump/admin

1. 进入 MongoDB 容器
   ```
   docker exec -it mongodb cd /data/db
   ```
2. 使用 **mongodump** 工具，导出数据库
   ```
   # 备份
   mongodump --authenticationDatabase admin --username root --password PASSWORD -d DATABASE_NAME -h localhost

   # 查看备份
   cd dump/admin && ls 
   ```
3. 使用 **mongorestore** 工具，恢复数据库
   ```
   mongorestore --authenticationDatabase admin --username root --password PASSWORD PATH_TO_BACKUP_FILE

   ```

详情参考官方文档：[MongoDB Backup Methods](https://docs.mongodb.com/manual/core/backups/)

### MongoDB 更新升级

请参考官方文档：[Upgrade to the Latest Revision of MongoDB](https://docs.mongodb.com/manual/tutorial/upgrade-revision/)

### MongoDB 数据迁移

可以，通过修改 */data/apps/mongodb/src/mongod.conf* 配置文件


## 故障排除{#troubleshoot}

除以下列出的 MongoDB 故障问题之外， [通用故障处理](../troubleshoot) 专题章节提供了更多的故障方案。 

#### MongoDB compass 无法连接数据库？

检查27017端口，bindIP和账户认证等连接字段是否满足条件

## 问题解答

#### 什么是 MongoDB 的 Client 和 Server？

MongoDB Server 是指 MongoDB 程序本体，而 MongoDB Client 指采用TCP协议用于连接程序本地的客户端。它们是两个完全不同的程序，也就是说它们并需要同时安装到同一台服务上。

#### mongod 和 mongo 命令有什么区别？

mongod 是 MongoDB 的服务端管理命令，用于启动数据库服务。  
mongo 是用于访问 MongoDB 服务的客户端。  

#### MongoDB Community vs MongoDB Enterprise？

MongoDB社区是MongoDB的源代码，可免费使用。  
MongoDB Enterprise是MongoDB企业高级订阅的一部分，包括对MongoDB部署的全面支持。MongoDB Enterprise还添加了以企业为中心的功能，如LDAP和Kerberos支持、磁盘加密和审计。

#### 无身份验证可直接访问 MongoDB？

可以，默认安装时 MongoDB 开启了访问控制，当关闭认证后无需 MongoDB 用户名密码就可以访问。
 > MongoDB [访问控制参考](https://docs.mongodb.com/manual/tutorial/enable-authentication/)

#### MongoDB 中的 admin 数据库是什么？

安装 MongoDB 时会默认包含一个 admin 数据库，如果你创建管理员账户就必须存储到这个admin中

#### MongoDB 提供哪些安全认证？

MongoDB提供各种功能，如身份验证、访问控制和加密，以保护MongoDB部署的安全。一些主要的安全功能包括： 

| Authentication | Authorization | TLS/SSL | Enterprise Only |
| :--- | :--- | :--- | :--- |
| [Authentication](https://docs.mongodb.com/manual/core/authentication/)<br />[SCRAM](https://docs.mongodb.com/manual/core/security-scram/)<br />[x.509](https://docs.mongodb.com/manual/core/security-x.509/) | [Role-Based Access Control](https://docs.mongodb.com/manual/core/authorization/)<br />[Enable Auth](https://docs.mongodb.com/manual/tutorial/enable-authentication/)<br />[Manage Users and Roles](https://docs.mongodb.com/manual/tutorial/manage-users-and-roles/) | [TLS/SSL (Transport Encryption)](https://docs.mongodb.com/manual/core/security-transport-encryption/)<br />[Configure mongod and mongos for TLS/SSL](https://docs.mongodb.com/manual/tutorial/configure-ssl/)<br />[TLS/SSL Configuration for Clients](https://docs.mongodb.com/manual/tutorial/configure-ssl-clients/) | [Kerberos Authentication](https://docs.mongodb.com/manual/core/kerberos/)<br />[LDAP Proxy Authentication](https://docs.mongodb.com/manual/core/security-ldap/)<br />[Encryption at Rest](https://docs.mongodb.com/manual/core/security-encryption-at-rest/)<br />[Auditing](https://docs.mongodb.com/manual/core/auditing/) |

> MongoDB还提供了 [安全检查列表](https://docs.mongodb.com/manual/administration/security-checklist/) 保护MongoDB部署的建议操作列表。

#### MongoDB 支持哪些平台？

所支持的平台，查看：[列表](https://docs.mongodb.com/manual/administration/production-notes/#prod-notes-supported-platforms)

#### MongoDB 提供官方有哪些工具？

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

#### 除 MongoDB Compass 之外，还有哪些客户端工具？

更多可选的 Web 端：

- [mongo-express](https://github.com/mongo-express/mongo-express) - Web-based admin interface built with Express
- [mongoadmin](https://github.com/thomasst/mongoadmin) - Admin interface built with Django
- [mongri](https://github.com/dongri/mongri) - Web-based user interface written in JavaScript
- [Rockmongo](https://github.com/iwind/rockmongo) - PHPMyAdmin for MongoDB, sort of

更多可选的客户端：

- [dbKoda](https://www.dbkoda.com/) - Cross-platform and open-source IDE
- [MongoHub](https://github.com/jeromelebel/MongoHub-Mac) - Mac native client
- [Mongotron](http://mongotron.io/) - Cross-platform and open-source client built with Electron
- [NoSQLBooster](https://nosqlbooster.com/) - Feature-rich but easy-to-use cross-platform IDE (formerly MongoBooster)
- [Nosqlclient](https://github.com/nosqlclient/nosqlclient) - Cross-platform, self hosted and easy to use management tool (formerly Mongoclient)
- [Robo 3T](https://github.com/Studio3T/robomongo) - Free, native and cross-platform shell-centric GUI (formerly Robomongo)
- [Studio 3T](https://studio3t.com/) - Cross-platform GUI, stable and powerful (formerly MongoChef)


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

### MongoDB 中数据库、用户和角色关系？

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

