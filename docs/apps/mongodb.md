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

Websoft9 控制台安装 MongoDB 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

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

#### 修改管理员密码

  ```
  > db = db.getSiblingDB('admin')
  admin
  > db.changeUserPassword("root", "NEWPASSWORD")
  > exit
  ```


## 配置选项{#configs}
  
- [配置文件](https://docs.mongodb.com/v4.0/reference/configuration-options/#conf-file)（已挂载）：*/etc/mongod.conf*  

- 开启公网访问：修改配置文件中的字段 `bindIp: 0.0.0.0`

- 服务端命令：`mongod`

- 客户端命令：`mongo`

- 命令：mongod 是 MongoDB 的服务端管理命令，mongo 是用于访问 MongoDB 服务的客户端

- 无身份验证访问（√）：参考 [访问控制](https://docs.mongodb.com/manual/tutorial/enable-authentication/) 设置

- 默认数据库 admin：全局管理权限的数据库用户必须存储在这个 admin 数据库中


## 管理维护{#administrator}

### 关闭 MongoDB 访问认证

Websoft9 控制台修改**编排文件**，注释 **MONGO_INITDB_** 开头的环境变量，重建应用

### 忘记管理员密码

1. 关闭 MongoDB 访问认证

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