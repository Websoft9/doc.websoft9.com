---
sidebar_position: 2
slug: /administration/db_change
---

# 更换为外部数据库

Websoft9 每个应用都预装了默认数据库，并且这些数据库也按照应用的要求进行了必要的个性化设置，确保用户可以直接使用。虽然如此，每个用户可能面临使用习惯、企业 IT 规范要求等不同的因素，导致需要更换默认数据库为用户自己的特定数据库。  

下面介绍如何更换数据库更换为外部目标数据库：  

## 准备

更换为外部目标数据库，了解最少需要做好如下准备：

* 充分阅读应用官方文档，确保外部目标数据库类型是受支持的且完成应用所需的必要配置
* 开启外部目标数据库类型的远程连接，确保可以被访问
* 针对已初始化的应用，备份原有的数据库

## 更换方式

由于 Websoft9 提供的应用数量较多，这些应用的数据库连接入口方式大致有如下几种方式：

* 初始化向导可视化界面中自行填写

* 配置文件

   - 非 Docker 应用，修改应用的配置文件（例如：WordPress 的 wp-config.php 文件）

   - Docker 应用，修改 [.env 文件](../administrator/parameter)中数据库相关的配置。例如：
     ```
      DB_MRAIADB_USER=root
      DB_MARIADB_PASSWORD=yourpassword
      DB_MARIADB_HOST=mariadb
      DB_MARIADB_PORT=3306
      DB_MARIADB_VERSION=10.6
     ```

## 更换后处理

更换为外部目标数据库后，需导入备份的数据库，并测试可用性。  




