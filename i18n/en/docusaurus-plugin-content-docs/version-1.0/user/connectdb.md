---
sidebar_position: 3
slug: /user/dbgui
---

# Manage Database from GUI

You can use the local computer client and pre-installed Web-based GUI tools to connect to the database.

## Database Sheet

| Database name                   | Username     | Remote port | Web-based GUI           |  Enable Remote  |
| ----------------------- | ---------- | ------------------------ | ------------------------ | ------------------------ |
| MySQL/Mariadb      | root       | 3306   | Y       |   [Detail](../mysql#remote)     |
| PostgreSQL              | postgres   | 5432 | Y       |   [Detail](../postgresql#remote)     |
| Mongodb                 | root | 27017 | Y       |   [Detail](../mongodb#remote)     |
| Oracle                  | system     | 1521 | Y                     |                      |
| SQLServer               | sa         | 1433     | N | Use SQL Server Management Server on your Instance|

## Web-based GUI

Web-based GUI tool to connect database, you don't need to enable remote port of Database.  

`HOST` value is database name, e.g: mysql, postgresql 

Refer to:   

* [MySQL/Mariadb](../mysql#phpmyadmin)
* [PostgreSQL](../postgresql#pgadmin)
* [Mongodb](../mongodb#mongodb-web-gui)
* [Oracle](../cloudbeaver)
* [SQLServer](../cloudbeaver)

## Local clients

Local clients to connect database, you  need to enable remote port of Database, then connect it.  

`HOST` value is **Internet IP + remote IP**     

Recommend you use open source database client: [DBeaver Community](https://dbeaver.io/)




