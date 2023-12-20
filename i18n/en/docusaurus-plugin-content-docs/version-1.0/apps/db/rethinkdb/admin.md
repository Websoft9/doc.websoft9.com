---
sidebar_position: 3
slug: /rethinkdb/admin
tags:
  - RethinkDB
  - Cloud Native Database
---

# RethinkDB Maintenance

This chapter is special guide for RethinkDB maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### RethinkDB Backup and Restore

You can use `export/import` for RethinkDB backup and restore

**Backup**

```
# export the db file
rethinkdb export abc.db

# export the dump file
rethinkdb dump [options]
```

**Backup**

```
rethinkdb import -d [options]
```

### RethinkDB Upgrade

There no upgrade cli from RethinkDB documentation, but it have [Migrating](https://rethinkdb.com/docs/migration/) solution for upgrade


## Troubleshoot{#troubleshoot}

In addition to the RethinkDB issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### Error in Chrome when modify RethinkDB password?

You should clear Chrome cache or open incognito tab to access RethinkDB


## FAQ{#faq}

#### If there have RethinkDB CLI?

Yes, `rethinkdb -h` for CLI help

#### Is there a web-base GUI database management tools?

Yes, visit by *http://Server's Internet IP*

#### `rethinkdb repl` 命令如何密码登录？

```
rethinkdb repl --password-file /tmp/pw
```

其中 /tmp/pw 为存放密码明文的文件。

#### RethinkDB 提供哪些驱动？

我们提供 Ruby，Python，Java和JavaScript / Node.js的官方驱动程序。社区支持的驱动程序支持十多种其他语言，包括C＃/。NET，Go和PHP。

#### 可否命令行修改 RethinkDB 控制台密码？

参考：[Nginx auth_basic](../nginx#authbasic)

#### Can I visit RethinkDB web console by *http://IP:8080*?

No, RethinkDB web console now allow visit from 127.0.0.1

#### RethinkDB 使用的是什么查询语言？

RethinkDB 不支持传统是数据库语言 SQL 。但是，RethinkDB的查询语言 [ReQL](https://rethinkdb.com/docs/introduction-to-reql/) 几乎可以执行 SQL 所能做的一切，包括表联接和聚合功能，并且功能强大，表达力强且易于学习。  
ReQL还可以完成SQL无法完成的许多工作，包括将查询与JavaScript表达式和map-reduce混合使用。

#### RethinkDB 权限如何控制？

权限存储在 permissions 系统表中。虽然您可以通过修改该表中的文档来更改权限，但使用grant命令要方便得多。

默认支持四种权限：

* read
* write
* config
* connect

有三种权限范围：  

* 表（仅影响表）
* 数据库（影响数据库和其中的表）
* 全局（影响所有数据库和其中的表）

#### RethinkDB 系统表有什么作用？

RethinkDB 维护特殊的[系统表](https://rethinkdb.com/docs/system-tables/)，其中包含有关服务器、数据库、单个表和集群问题的配置和状态信息。


#### RethinkDB vs MongoDB？

RethinkDB 是一个与 MongoDB 对标的开源数据库，RethinkDB 定位于实时数据库应用：

- 协作式Web和移动应用程序
- 流分析应用
- 多人游戏
- 实时市场
- 连接的设备

#### 如何设置 RethinkDB 的初始密码？

默认管理员用户名为 `admin`，密码为空。通过服务端命令行，可以很方便的设置管理员密码：

```
rethinkdb --initial-password yourpassword
```
