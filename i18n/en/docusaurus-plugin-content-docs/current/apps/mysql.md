---
title: MySQL
slug: /mysql
tags:
  - Databases
  - Relational
  - RDS 
  - MariaDB
---

import Meta from './_include/mysql.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of MySQL at **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

### Testing Availability {#wizard}

1. Enter the CLI of the MySQL container and log in to test the availability
   ```
   mysql -u root -p
   ```
2. Successful login will enter MySQL CLI

### Graphical tools

Websoft9 App Store installs [phpMyAdmin](./phpmyadmin) or [CloudBeaver](./cloudbeaver#verify-cloudbeaver-installation), you can manage MySQL **without opening an external network**.

## Configuration options{#configs}

- Configuration file directory (mounted): /etc/mysql/conf.d
- Initialization script directory (mounted): /docker-entrypoint-initdb.d
- Port: 3306
- Master-slave replication (√): DDL and DML operations are replicated to the slave repository by binary logs, supporting one master and multiple slaves
- Database hostname: Container name
- External network port: user-defined selection during installation
- [Connectors and APIs](https://dev.mysql.com/doc/index-connectors.html)
- CLI
  * mysql
  * mysqladmin
  * mysqldump 
  * mysqlhotcopy
  * mysqlcheck
  * mysqlshow
  * mysqlimport
  * mysqlbinlog
  * myisampack

## Administer{#administrator}

### Setting up Binary Log

MySQL does not enable Binary Log enabled by default. Modify the relevant entries in [MySQL Configuration File](#configs).

```
log_bin = mysql-bin # enable Binary Log
binlog_format = mixed # Binary log format
expire_logs_days = 7 # Binary log expire time
```

### Setting up MySQL remote access {#remote}

Enter the CLI of the MySQL container and set up MySQL remote access:

```
# Enable remote access
mysql> use mysql;
mysql> update user set host = '%' where user = 'root';
```

### Change the password.

Execute the command as follows:
```
mysqladmin -u username -p old password password 'new password' 
```
### Reset password

To reset the password through a temporary container

1. Stop current MySQL container and run new MySQL container sharing storage with the old container.
2. Change the password in the new container and delete the new container.
3. Resume the original MySQL container


### Backup (export) 

- It is recommended to use a visualization tool such as phpMyAdmin, [Export](./phpmyadmin#manage-database) database (SQL format recommended)

- Developers can use **mysqldump** tool to export (more efficient and versatile)
   ```
   mysqldump -uroot -p databasename>databasename.sql
   ```

### Recover (import)

1. Login to phpMyAdmin, select  the **Import** at the top, and follow the wizard to start the import.

2. Database character set incompatibility may occur during the import process, requiring manual intervention. 

### Migration {#migration}

MySQL to MySQL migration can usually be quickly accomplished by **importing and exporting** data.    

However, other DBMS to MySQL migrations are best accomplished using a migration tool such as [MySQL Workbench: Database Migration](https://www.mysql.com/products/workbench/migrate/)


### Audit

1. install the **[Maria Audit Plugin](https://mariadb.com/kb/en/mariadb-audit-plugin/)** plugin
2. Set the audit log path

## Troubleshooting{#troubleshooting}

#### How to analyze database logs?

Mariadb logs are files that record daily operations and error messages for the MariaDB database and can be categorized into:

* Binary log (Binlog):  Log all database operations for database recovery. 
* Error log: for diagnosing problems
* Slow Query Log: records query statements that are executed inefficiently
* Generic Query Log: records all query operations

From a troubleshooting perspective, error logs and slow query logs are the key log  to consider

#### Importing a database reports an error?

Check the script to see if it contains a database creation script.

#### Database service cannot start?

The main reasons why MySQL fails to start are:

* Insufficient disk space (binary log file size is growing too fast)
* Deadlock
* MySQL configuration file error

It is recommended that you troubleshoot the problem by using the following commands  

```shell
# View disk space
df -lh

# Check memory usage
free -lh

# View database logs
docker logs container_name
```

#### Logs causing low disk space? {#binlogexceed}

- Clean up logs manually
- Consider commenting out configuration file entries `#log_bin=mysql-bin` Turn off binlogs

#### Data files exceeding upper limit?

When a single file exceeds the upper limit, it can cause the database to fail to start. In this case, add disk or add a new datafile address
```
innodb_data_file_path= /data/mysql/data1:2000M;/data2/mysql/data2:2000M:autoextend
```

#### MySQL container cannot be accessed remotely?

There are three possible reasons:

1. the port mapping is set incorrectly, resulting in the container not having a network
2. The container does not have remote access privileges enabled
3. MySQL 8.0 special setting requirements.

#### mysqladmin command reports an error ?

Error: “Access denied; you need the SUPER privilege for this operation”  
Reason: The mysqlamdin command requires SUPER privilege, which is not available to normal users by default.    

#### Cannot delete all tables?

Some tables cannot be deleted due to **Foreign Key Constraints** between tables.

#### Deadlock in database?

Deadlocks are usually caused by application design problems, among which transaction operations are more likely to have deadlocks.  

Once a deadlock occurs, you can use the following commands to confirm the cause of the deadlock:

```
MariaDB [(none)]> show innodb status \G;
```
