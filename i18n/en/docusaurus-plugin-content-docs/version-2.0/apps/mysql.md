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

1. When completing the installation of MySQL in the **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

### Testing Availability {#wizard}

1. Access the CLI of the MySQL container and log in to test availability
   ```
   mysql -u root -p
   ```
2. A successful login will take you to the MySQL CLI

### Graphical tools

The Websoft9 App Store provides [phpMyAdmin](./phpmyadmin) and [CloudBeaver](./cloudbeaver#verify-cloudbeaver-installation) for managing MySQL, **without opening an external network**.

## Configuration options{#configs}

- Configuration file directory (mounted): /etc/mysql/conf.d
- Initialization script directory (mounted): /docker-entrypoint-initdb.d
- Port: 3306
- Master-slave replication (√): DDL and DML operations are replicated to the slave repository using binary logs, supporting one master and multiple slaves
- Database hostname: Container name
- External network port: user-defined selection during installation
- [Connectors and APIs](https://dev.mysql.com/doc/index-connectors.html)
- CLI tools:
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

Binary Log is not enabled by default in MySQL. Modify the relevant entries in the [MySQL Configuration File](#configs).

```
log_bin = mysql-bin # enable Binary Log
binlog_format = mixed # Binary log format
expire_logs_days = 7 # Binary log expire time
```

### Setting up MySQL remote access {#remote}

Access the CLI of the MySQL container and set up remote access:

```
# Enable remote access
mysql> use mysql;
mysql> update user set host = '%' where user = 'root';
```

### Changing the password.

To change the password, execute the following command:
```
mysqladmin -u username -p old password password 'new password' 
```
### Resetting the Password

To reset the password through a temporary container

1. Stop the current MySQL container and run a new MySQL container sharing storage with the old container.
2. Change the password in the new container and then delete the new container.
3. Resume the original MySQL container


### Backup (export) 

- It is recommended to use a visualization tool such as phpMyAdmin to [Export](./phpmyadmin#manage-database) the database (SQL format is recommended)

- Developers can use the **mysqldump** tool for exporting, which is more efficient and versatile:
   ```
   mysqldump -uroot -p databasename>databasename.sql
   ```

### Recover (import)

1. Log in to phpMyAdmin, select **Import** at the top, and follow the wizard to start the import.

2. Database character set incompatibility may occur during the import process, requiring manual intervention. 

### Migration {#migration}

Migrating from MySQL to MySQL is usually accomplished quickly by **importing and exporting** data.    

However, migrations from other DBMS to MySQL are best handled using a migration tool such as [MySQL Workbench: Database Migration](https://www.mysql.com/products/workbench/migrate/)


### Audit

1. install the **[Maria Audit Plugin](https://mariadb.com/kb/en/mariadb-audit-plugin/)** plugin
2. Set the audit log path

## Troubleshooting{#troubleshooting}

#### How to analyze database logs?

MariaDB logs include files that record daily operations and error messages, categorized as follows:

* Binary log (Binlog):  Log all database operations for recovery. 
* Error log: For diagnosing problems
* Slow Query Log: Records inefficiently executed query statements.
* Generic Query Log: Records all query operations

From a troubleshooting perspective, focus on error logs and slow query logs.

#### Importing a database reports an error?

Check the script to ensure it includes a database creation script.

#### Database service cannot start?

Common reasons for MySQL startup failure include:

* Insufficient disk space (binary log file size is growing too quickly)
* Deadlocks
* MySQL configuration file errors

Use the following commands to troubleshoot:

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
- Consider commenting out `#log_bin=mysql-bin` in the configuration file to turn off binary logs

#### Data files exceeding upper limit?

When a single file exceeds the upper limit, it can prevent the database from starting. In such cases, add disk space or specify a new data file path:
```
innodb_data_file_path= /data/mysql/data1:2000M;/data2/mysql/data2:2000M:autoextend
```

#### MySQL container cannot be accessed remotely?

Possible reasons include:

1. Incorrect port mapping, resulting in no network access for the container.
2. The container does not have remote access privileges enabled
3. Special setting requirements for MySQL 8.0.

#### `mysqladmin` Command reports an error ?

Error: “Access denied; you need the SUPER privilege for this operation”  
Reason: The `mysqlamdin` command requires SUPER privilege, which is not available to normal users by default.    

#### Cannot delete all tables?

Some tables cannot be deleted due to **Foreign Key Constraints** between tables.

#### Deadlock in database?

Deadlocks are typically caused by application design issues, particularly with transaction operations. 

To confirm the cause of a deadlock, use the following command:

```
MariaDB [(none)]> show innodb status \G;
```
