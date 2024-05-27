---
sidebar_position: 3.0
slug: /app-connectdb
---

# 连接并管理应用的数据库

Websoft9 采用微服务架构部署应用，每个应用的数据库都进行了必要的预配置，且它们是独立运行的，应用间数据互不干扰。  

为了安全考虑，数据库容器的端口不允许绑定在宿主机上，禁止直接通过本地客户端直接连接。   

我们推荐通过应用商店安装 [phpMyAdmin](../mysql#phpmyadmin), pgAdmin 等可视化 Web 工具来以内网的方式管理数据库，既安全又简单。  

## 条件

管理数据库的所需的两个要素：

- 准备数据库管理工具
- 获取准确的数据库连接信息（主机名，账号，密码，端口等）

## 启动管理工具

虽然 Websoft9 在默认情况下，没有安装任何一个数据库管理工具。但是，我们在应用商店的【数据库】>【管理与迁移】类目提供了诸多热门的 Web 版的数据库管理工具。  

![](./assets/websoft9-appstore-dbmanagelist.png)

## 获取连接信息

Websoft9 所有应用考虑了用户需要的：数据库主机名、账号和密码等，可以通过其管理页面的【数据库】标签页查看。

## 参考

### 数据库连接信息对照（表）

下面我们在列出常见的数据库与管理工具对应表，供您参考：

| 数据库          | 管理员   | 端口  | Web 版管理工具          |
| --------------- | -------- | ----- | ----------------------- |
| MySQL           | root     | 3306  | phpMyadmin, CloudBeaver |
| MariaDB         | root     | 3306  | phpMyadmin, CloudBeaver |
| PostgreSQL      | postgres | 5432  | pgAdmin, CloudBeaver    |
| SQL Server      | sa       | 1433  | CloudBeaver             |
| MongoDB         | root     | 27017 | MongoDB Compass           |
| Oracle Database | system   | 1521  | CloudBeaver             |
| Redis           | 空       | 6379  | RedisInsight            |


## 故障
