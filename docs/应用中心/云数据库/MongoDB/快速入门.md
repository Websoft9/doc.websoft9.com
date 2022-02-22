---
sidebar_position: 1
slug: /mongodb
tags:
  - MongoDB
  - Cloud Native Database
---

# 快速入门

[MongoDB](https://www.mongodb.com/zh) 是通用、基于文档的分布式数据库，帮助现代应用程序开发人员迎接云时代的到来。它在类似 JSON 的文档内存储数据。这种面对数据的数据存储方法非常自然，比传统的排/列模型更加直观和强大。MongoDB 也是一个真正的具有全套工具的数据平台，能帮助开发人员、分析师和数据科学家等各类人群更方便地处理数据。

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mongodb/mongodb-gui-websoft9.png)

在云服务器上部署 MongoDB 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 登录云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:27017** 和 **TCP:9091** 端口是否开启

## 账号密码

使用MongoDB，可能会用到的几组账号密码如下：

### MongoDB

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器指定文件中   

  - Linux 系统  

     **密码存储路径**：*/credentials/password.txt*    
     **获取方式**： 建议通过云控制台的命令终端，运行下图*所示命令，获取数据库密码   
     ```
     cat /credentials/password.txt
     ```

  - Windows 系统  

     **密码存储路径**：*C:/credentials/password.txt*     
     **获取方式**： 远程桌面到服务器，打开此文件即可   

 > 需要登录MongoDB，请参考 [图形化工具：adminMongo](/zh/solution-gui.md)


## MongoDB 安装向导

部署 MongoDB 之后，依次完成下面的步骤，验证其可用性

### 检测 MongoDB 安装

1. 使用 SSH 连接 MongoDB 所在的服务器，运行下面的命令，查看 MongoDB 的安装信息和运行状态
   ```
   sudo systemctl status mongod
   ```
2. 运行服务状态查询命令，MongoDB 正常运行会得到 " Active: active (running)... " 的反馈


### 命令方式连接 MongoDB

1. 使用 SHH 登录到 MongoDB 所在的服务器，运行 `mongo` 命令（MongoDB Shell）
   ~~~
   mongo

   ---
   MongoDB shell version v4.0.18
   connecting to: mongodb://127.0.0.1:27017/?gssapiServiceName=mongodb
   Implicit session: session { "id" : UUID("e5c50eca-e51b-482e-b0bd-24edc2d1e433") }
   MongoDB server version: 4.0.18
   Welcome to the MongoDB shell.
   For interactive help, type "help".
   For more comprehensive documentation, see
         http://docs.mongodb.org/
   Questions? Try the support group
         http://groups.google.com/group/mongodb-user
   ~~~

2. 分别列出默认数据库和用户
   ```
   # 列出所有数据库
   show dbs

   # 切换到 admin 数据库，列出所有用户
   use admin
   show users
   ```

> 需要了解更多 MongoDB 的使用，请官方文档 [MongoDB Administration](https://docs.mongodb.com/manual/administration/)

## 常用操作

### 开启远程访问

1. 修改 MongDB 配置文件 *etc/mongod.conf*
   ```
   #1 将authorization由disabled设置为enabled
   security:
   authorization: enabled

   #2 将 bindIP 修改为 0.0.0.0 或 本地电脑公网IP
   net:
      port: 27017
      bindIp: 0.0.0.0
   ```
   > 0.0.0.0 代表任意公网IP均可访问

2. 重启MongoDB服务
   ```
   systemctl restart mongod

### 密码管理

#### 修改密码

参考下面的命令，修改已经创建的管理员账号root的密码

```
mongo admin --u root --p YOURPASSWORD
MongoDB shell version v4.0.18
connecting to: mongodb://127.0.0.1:27017/?gssapiServiceName=mongodb
> db = db.getSiblingDB('admin')
admin
> db.changeUserPassword("root", "NEWPASSWORD")
> exit
```

#### 重置密码

重置密码即已经忘记密码的情况下，通过特殊手段重新设置新密码的过程。

1. 修改 MongDB 配置文件 *etc/mongod.conf*，将authorization由disabled设置为enabled
   ```
   security:
   authorization: disabled

   ```
2. 重启MongoDB服务
   ```
   systemctl restart mongod
   ```
3. 重新设置密码
   ```
   mongo
   > db = db.getSiblingDB('admin')
   admin
   > db.changeUserPassword("root", "NEWPASSWORD")
   ```

4. 重复第1步，但将authorization由enabled设置为disabled
5. 重启MongoDB服务

### 图形化工具

MongoDB的图形化工具分为桌面版和Web版两种形式，每种形式的工具都有一些比较受欢迎的工具：

#### 桌面版
- [MongoDB Compass Community](https://www.mongodb.com/download-center/compass) - A free tool for developing with MongoDB and includes a subset of the features of Compass.
- [dbKoda](https://www.dbkoda.com/) - Cross-platform and open-source IDE
- [MongoHub](https://github.com/jeromelebel/MongoHub-Mac) - Mac native client
- [Mongotron](http://mongotron.io/) - Cross-platform and open-source client built with Electron
- [NoSQLBooster](https://nosqlbooster.com/) - Feature-rich but easy-to-use cross-platform IDE (formerly MongoBooster)
- [Nosqlclient](https://github.com/nosqlclient/nosqlclient) - Cross-platform, self hosted and easy to use management tool (formerly Mongoclient)
- [Robo 3T](https://github.com/Studio3T/robomongo) - Free, native and cross-platform shell-centric GUI (formerly Robomongo)
- [Studio 3T](https://studio3t.com/) - Cross-platform GUI, stable and powerful (formerly MongoChef)

#### Web 版

- [adminMongo](https://github.com/mrvautin/adminMongo) - Web-based user interface to handle connections and databases needs
- [mongo-express](https://github.com/mongo-express/mongo-express) - Web-based admin interface built with Express
- [mongoadmin](https://github.com/thomasst/mongoadmin) - Admin interface built with Django
- [mongri](https://github.com/dongri/mongri) - Web-based user interface written in JavaScript
- [Rockmongo](https://github.com/iwind/rockmongo) - PHPMyAdmin for MongoDB, sort of

下面以两种流行的工具为例，介绍如何使用图形化工具。

#### 前置工作

使用图形化工具之前务必开启MongoDB的访问认证，并设立用户密码，以保证足够的安全性。  

1. 修改 MongDB 配置文件 *etc/mongod.conf*
   ```
   #1 将authorization由disabled设置为enabled
   security:
   authorization: enabled

   #2 将 bindIP 修改为 0.0.0.0 或 本地电脑公网IP
   net:
      port: 27017
      bindIp: 0.0.0.0
   ```
   > 0.0.0.0 代表任意公网IP均可访问

2. 重启MongoDB服务
   ```
   systemctl restart mongod
   ```
3. 开启服务器安全组 **TCP:27017** 端口，保证MongoDB服务可以被外部外网访问。

以上条件准备好之后，就可以根据选择合适的图形化界面工具

##### adminMongo

adminMongo 是一款在线web版工具，默认已经安装到了MongoDB部署方案中

1. 开启服务器安全组 **TCP：9091** 端口

2. 本地电脑浏览器访问：*http://服务器公网IP:9091* 打开adminMongo界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mongodb/adminmongo-connect001-websoft9.png)

3. 以连接字符串为例（这里的IP地址是公网IP或本地IP）
   ```
   # 默认连接到config数据库，172.17.0.1为内网IP
   mongodb://root:1cTFecwTEs@172.17.0.1:27017/admin
   # 默认连接到config数据库
   mongodb://root:1cTFecwTEs@40.114.115.58
   # 默认连接到admin数据库
   mongodb://root:1cTFecwTEs@40.114.115.58/admin
   mongodb://parse:AxXFcV5zSz@40.114.115.58/parse
   ```

4. 开始连接
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mongodb/adminmongo-connect002-websoft9.png)

5. 连接成功，进入 adminMongo 控制面板
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mongodb/adminmongo-connect003-websoft9.png)

6. 使用完成后，请删除连接
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mongodb/adminmongo-connect004-websoft9.png)

##### MongoDB Compass

1. [下载](https://www.mongodb.com/products/compass)并安装 MongoDB Compass
2. 填写准确的字段，连接 MongoDB
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mongodb/mongodbcompass001-websoft9.png)
3. 连接成功，进入控制台
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mongodb/mongodbcompass002-websoft9.png)


## 异常处理

#### 浏览器无法访问 adminMongo（白屏没有结果）？

您的服务器对应的安全组9091端口没有开启（入规则），导致浏览器无法它

#### MongoDB 默认启用账号认证吗？

没有，请修改配置文件 /etc/mongod.conf，将 authorization 字段设置为 enabled