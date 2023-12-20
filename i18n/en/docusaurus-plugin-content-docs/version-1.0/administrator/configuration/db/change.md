---
sidebar_position: 2
slug: /administration/db_change
---

# Use external database

Although there have installed database for Websoft9, but you maybe want to use an external database for you application for some reason.  

This section will show you how to change default database to external database: 

## Prepare

更换为外部目标数据库，了解最少需要做好如下准备：

* 充分阅读应用官方文档，确保外部目标数据库类型是受支持的且完成应用所需的必要配置
* 开启外部目标数据库类型的远程连接，确保可以被访问
* 针对已初始化的应用，备份原有的数据库

## Change database

You have main two ways to change your database according your application:  

* Change database at the **Installation wizard of GUI**

* Change your database at your configuration file:  

   - For Docker-based application, change it from  [.env file](../administrator/parameter) like below
        ```
      DB_MRAIADB_USER=root
      DB_MARIADB_PASSWORD=yourpassword
      DB_MARIADB_HOST=mariadb
      DB_MARIADB_PORT=3306
      DB_MARIADB_VERSION=10.6
     ```

   - For not Docker-based application, change the configuration directly

## Follow-up after Change database

After changing to an external target database, you need to import the backup database and test the availability.




