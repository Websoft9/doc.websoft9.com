---
sidebar_position: 5
slug: /user/dbgui
---

# 数据库

连接数据库除了登录服务器以命令行形式连接之外，还可以使用本地电脑客户端和预装的 Web 在线工具连接 

## 一览表

在连接数据库时，请参考下表：

| 名称                    | 用户名     | 数据库远程端口 | 可视化管理地址           | 开启远程   |
| ----------------------- | ---------- | ------------------------ | ------------------------ | ------------------------ |
| MySQL/Mariadb      | root       | 3306   | http://服务器公网IP:9090       |   [设置](../mysql#remote)     |
| PostgreSQL              | postgres   | 5432 | http://服务器公网IP:9090       |   [设置](../postgresql#remote)     |
| Mongodb                 | root | 27017 | http://服务器公网IP:9091       |   [设置](../mongodb#remote)     |
| Oracle                  | system     | 1521 | 无                     |                      |
| SQLServer               | sa         | 1433     | 登录服务器，使用 SQL Server Management Server| |

## Web 客户端管理{#webgui}

Web 可视化客户端与数据库在同一台服务器，所以不需要开启数据库自身的远程连接端口（更好的保护数据库）也可以连接数据库。  

连接数据库的时候，数据库 `HOST` 的值一般为数据库名称：mysql, postgresql 等。   

详细的使用方案参考：  

* [MySQL/Mariadb](../mysql#phpmyadmin)
* [PostgreSQL](../postgresql#pgadmin)
* [Mongodb](../mongodb#adminmongo)
* [Oracle](../cloudbeaver)
* [SQLServer](../cloudbeaver)

## 本地客户端管理

本地客户端连接数据库，需要先到云控制台安全组开启**一览表**中的数据库远程端口，然后才可以连接。   

数据库 `HOST` 的值为：服务器公网 IP + 数据库远程端口

如果您你没有熟悉的数据库本地客户端，我们推荐使用：[DBeaver Community](https://dbeaver.io/)




