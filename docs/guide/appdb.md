---
sidebar_position: 2
slug: /guide/appdb
---

# 管理/更换应用的数据库

Websoft9 采用微服务架构部署应用，每个应用的数据库都进行了必要的预配置，且它们是独立运行的，应用间数据互不干扰。  

## 管理数据库

管理数据库的所需的两个要素：

- 准备数据库管理工具
- 获取准确的数据库连接信息（主机名，账号，密码，端口等）

### 可视化管理工具

虽然 Websoft9 在默认情况下，没有安装任何一个数据库管理工具。但是，我们在应用商店的【数据库】>【管理与迁移】类目提供了诸多热门的 Web 版的数据库管理工具。  

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9/websoft9-appstore-dbmanagelist.png)

### 获取连接信息

Websoft9 所有应用考虑了用户需要的：数据库主机名、账号和密码等，可以通过其管理页面的【数据库】标签页查看。

### 连接信息对照（表）

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


## 更换数据库

用户可能面临使用习惯、企业 IT 规范要求等不同的因素，导致需要更换默认数据库为用户自己的特定数据库（外部）。  

下面介绍如何更换数据库更换为外部目标数据库：  

### 准备

更换为外部目标数据库，了解最少需要做好如下准备：

* 充分阅读应用法人官方文档，确保外部目标数据库类型是受支持的且完成应用所需的必要配置
* 开启数据库的远程连接，确保可以被 Websoft9 应用访问
* 针对已初始化的应用，备份原有的数据库

### 开始更换

每个应用的数据库连接信息和存放地有一定的差异，但它的原理是相同的。下面介绍典型的更换数据库的主要操作：

1. 在 Websoft9 控制【我的应用】中，进入应用设置状态，点击[编排](../quick/manageapp#reup)标签页

2. 更改 .env 或 docker-compose.yml （文件二选一）应用的连接数据库信息。

> 此操作为高级操作，需慎重操作


### 更换后处理

更换为外部目标数据库后，需导入备份的数据库，并测试可用性。  

