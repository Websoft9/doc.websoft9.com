---
sidebar_position: 19
---

# 数据库

本节主要针对数据库相关的配置场景进行详细的说明。

## 数据库端口以及可视化管理

下面列出就数据库和操作系统的的默认账号，供用户参考：

不同的数据库有一定的差异，具体如下：

| 名称                    | 用户名     | 可视化管理地址           |
| ----------------------- | ---------- | ------------------------ |
| MySQL/Mariadb PHP环境中 | root       | http://服务器公网IP/phpmyadmin |
| MySQL/Mariadb 其他      | root       | http://服务器公网IP:9090       |
| PostgreSQL              | postgres   | http://服务器公网IP:9090       |
| Mongodb                 | root | http://服务器公网IP:9091       |
| Oracle                  | system     | 暂无                     |
| SQLServer               | sa         | 登录服务器，使用 SQL Server Management Server|  
| RethinkDB               | admin         | 登录服务器，http://服务器公网IP |  
| CouchDB              | admin         | 登录服务器，http://服务器公网IP |  
| Neo4j              | neo4j         | 登录服务器，http://服务器公网IP |  


## 使用外部数据库替换绑定数据库