---
sidebar_position: 3
slug: /mysql/admin
tags:
  - MySQL
  - Cloude Native Database
---

# MySQL/MariaDB Maintenance

This chapter is special guide for MySQL/MariaDB maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### MySQL/MariaDB Backup and Restore{#backup}

**Backup(export)**

1. Use visualization tools such as phpMyAdmin, [export](../mysql#phpmyadminexportimport)Database (recommended SQL format)

2. Use用 **mysqldump** export (more efficient and versatile)
   ```
   docker exec -it mysql mysqldump -uroot -p databasename>databasename.sql
   ```
3. Download the backup file locally and the backup is completed

**Restore(import)**

1. Log in to phpMyAdmin, open the [import] tab at the top, and start importing according to the wizard
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-import-websoft9.png)

2. Incompatibility of database character sets may occur during import, and manual intervention is required


### MySQL/MariaDB Upgrade{#upgrade}

**On Linux**

The system update command can update MySQL patch also, e.g: 5.6.x to 5.6.y or 5.7.x to 5.7.y

There are large differences between database distribution versions, which cannot provide a secure upgrade solution

**On Windows**

MySQL upgrade on Windows Server divided into two parts

1. Use Windows Update to upgrade Windows System
2. Dowload the lastest MySQL, stop the MySQL Services and replace the old files of MySQL

After upgrade , you need to run the `mysql_upgrade` command:
 
```
mysql_upgrade -u root -p 123456
```

### MySQL/MariaDB Migration{#migration}

The migration from MySQL to MySQL can be implemented quickly through data import and export.

However, migrations from other DBMSs to MySQL are best done using a migration tool such as: [MySQL Workbench: Database Migration](https://www.mysql.com/products/workbench/migrate/)

## Troubleshoot{#troubleshoot}

In addition to the MySQL/MariaDB issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### 

Check whether there is a database creation script in the script

#### Database service failed to start?

The main reasons why MySQL cannot be started are:
* Insufficient disk space (binary log file size grows too fast)
* Lock
* MySQL configuration file error

It is recommended to check through the command first: 

```shell
# View disk space
df -lh

# View memory usage
free -lh

# MySQL status
cd /data/apps/mysql && sudo docker compose ls

# View database logs
docker exec -it mysql cat /var/log/mysql/error.log
```

#### The database log file is too large, resulting in insufficient disk space?{#binlogexceed}

By default, mysql will automatically open the binlog. Binlog is mainly used to recover the database without backup. However, the binlog will take up a lot of space. If you don't clean it for a long time, the remaining disk space will be 0, which will affect the database or the server will not start.

If you have confidence in your own backup, you do not need the binlog function. Refer to the following steps to turn it off:

1. Edit [MySQL Configuration File] (../mysql#path) and comment out the binlog log   
  
  ```
  #log-bin=mysql-bin
  ```

2. Restart mysql
  ```
  sudo docker restart mysql
  ```

#### The database cannot be started due to insufficient disk space?

Add disk or add a new data file address:
```
innodb_data_file_path= /data/mysql/data1:2000M;/data2/mysql/data2:2000M:autoextend
```

#### MySQL container cannot be accessed remote?

There are three possible reasons for this problem:

1. Port mapping setting error, resulting in no network in the container  
2. The container does not have remote access permission  
3. MySQL 8.0 special setting requirements  

#### mysqladmin show errors in modifying common user password?

error:"Access denied; you need the SUPER privilege for this operation"   
Reason: the mysqladdin command requires super permission, but ordinary users do not have this permission by default.  
Scheme: use the command 'set password = password ("newpassword") to modify the password.   

#### It is difficult to delete all tables in the database at once?

The **foreign key constraint** between data tables causes that some data tables cannot be deleted.

#### Database deadlock?

Deadlocks are generally caused by application design problems, in which transaction operations are more likely to have deadlocks.
Once a deadlock occurs, you can use the following command to confirm the cause of the deadlock.

```
MariaDB [(none)]> show innodb status \G;
```
#### Prompt */var/lib/mysql/mysql.sock* is not exist?

Reason: when using tools such as mysqldump or mysqladmin, UNIX socket connection is used by default instead of TCP / IP. The socket file (mysql. Sock) may not be installed in * / var / lib / MySQL / MySQL Sock * directory.
Scheme: specify mysql Sock directory

## FAQ{#faq}

#### Can multiple MySQL instances be installed on a single server?

Theoretically, you can install more than one, but it is recommended to install one

#### What are MySQL client and server?

MySQL server refers to the MySQL program ontology, while MySQL client refers to the client that uses TCP protocol to connect to the local program. They are two completely different programs, that is, they need not be installed on the same service at the same time.

#### What is the test database in MySQL?

Before MySQL 5.7, a test database is included by default when MySQL is installed. This database is only used for testing.  
However, almost all users who can connect to MySQL have all the permissions of the test database, so there are certain security risks. 
From the perspective of information security, if you find the test database in the MySQL you are using, please *be sure to delete*.  

#### Can I modify the root directory of MySQL?

Yes, please refer the documentation [Modify MySQL Data Directory](../mysql#datadirectory)

#### What is the password for the database root user?

The password is stored in the server related file: `/credentials/password.txt`

#### Is there a web-base GUI database management tools?

Yes, phpMyAdmin is on it, visit by *http://Server Internet IP:9090*

#### How to prohibit external access to phpMyAdmin?

The cloud console security group closes port 9090

#### How to stop phpMyAdmin?

Stop the phpMyAdmin container:

```
sudo docker stop phpmyadmin
```

#### How to customize MariaDB error log file path?

Edit [MySQL/MariaDB configure file]

```
log_error=/var/log/mysql/error.log
```

#### What are cold backup and hot backup of a database?

Cold backup is to stop the database service and copy the database files for backup;  
Hot backup is to realize non-stop backup during the operation of the database and ensure the integrity of the database.

#### What is MySQL/MariaDB binary log?

Binary logs (binlogs) contain "operations" that describe database changes, such as creating table operations or changing table data.  
It also contains operations on statements that may have changed (for example, delete that does not match any rows). The binary log also  
contains information about when each statement used the update data.

#### What is phpMyAdmin install way？

Docker installation, to ensure good isolation of MySQL environment.

#### What is MySQL 8.0 default character set？

Mysql8.0 default character_set_server is utf8mb4



