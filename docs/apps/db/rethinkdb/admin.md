---
sidebar_position: 3
slug: /rethinkdb/admin
tags:
  - RethinkDB
  - Cloud Native Database
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup/) 相关章节。

## 场景

### RethinkDB 备份
RethinkDB 主要通过导出的实现备份，通过导入实现恢复：

```
# 导出普通数据库文件
rethinkdb export abc.db

# 导出压缩格式数据库文件
rethinkdb dump [options]
```

### RethinkDB 恢复

```
rethinkdb import -d [options]
```

### RethinkDB 升级

官方没有提供版本升级命令，只提供了一个升级后的数据迁移方案：[Migrating](https://rethinkdb.com/docs/migration/)


## 故障处理

除以下列出的 RethinkDB 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。 

#### RethinkDB 改密后，登录控制台报错？

浏览器缓存导致，打开新的无痕窗口或清空缓存即可。


## 常见问题

#### 是否有 RethinkDB 的 CLI 工具？

有，安装后存在cli命令，通过 `rethinkdb -h`查看使用详细

#### `rethinkdb repl` 命令如何密码登录？

```
rethinkdb repl --password-file /tmp/pw
```

其中 /tmp/pw 为存放密码明文的文件。

#### RethinkDB 提供哪些驱动？

我们提供 Ruby，Python，Java和JavaScript / Node.js的官方驱动程序。社区支持的驱动程序支持十多种其他语言，包括C＃/。NET，Go和PHP。

#### 可否命令行修改 RethinkDB 控制台密码？

参考：[Nginx auth_basic](../nginx#authbasic)

#### 通过端口可直接访问 RethinkDB 吗？

不可以，为了安全考量默认仅支持 127.0.0.1 访问，所以需通过 Nginx 转发。

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
