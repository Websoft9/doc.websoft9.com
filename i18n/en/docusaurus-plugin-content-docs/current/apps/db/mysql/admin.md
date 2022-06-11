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

1. 使用 phpMyAdmin等可视化工具，[导出](../mysql#phpmyadminexportimport)数据库（建议SQL格式）

2. 或使用 **mysqldump** 工具导出（效率更高，通用性更强）
   ```
   mysqldump -uroot -p databasename>databasename.sql
   ```
3. 将备份文件下载到本地，备份工作完成

**Restore(import)**

1. 登录 phpMyAdmin，打开顶部的【导入】标签页，根据向导开始导入
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-import-websoft9.png)

2. 导入过程中可能会出现数据库字符集不兼容的情况，需要人工干预处理


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
mysql_upgrade -u root -p 13456
```

### MySQL/MariaDB Migration{#migration}

The migration from MySQL to MySQL can be implemented quickly through data import and export.

However, migrations from other DBMSs to MySQL are best done using a migration tool such as: [MySQL Workbench: Database Migration](https://www.mysql.com/products/workbench/migrate/)

## Troubleshoot{#troubleshoot}

In addition to the MySQL/MariaDB issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### 导入数据库报错？

查看脚本里面是否有创建数据库的脚本

#### 数据库服务无法启动？

导致 MySQL 无法启动的主要原因有：

* 磁盘空间不足（二进制日志文件大小增长过快）
* 锁死
* MySQL 配置文件错误

建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# MySQL 状态
sudo systemctl status mysql

# 查看数据库日志
cat /data/mariadb/mariadb.err
log-error=/data/mysql/log.err
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
  systemctl restart mysqld
  ```

#### 磁盘空间不足导致数据库无法启动？

增加磁盘或增加一个新的数据文件地址
```
innodb_data_file_path= /data/mysql/data1:2000M;/data2/mysql/data2:2000M:autoextend
```

#### MySQL 容器无法远程访问？

导致这个问题的可能原因有三点：

1. 端口映射设置错误，导致容器没有网络
2. 容器没有开启远程访问权限
3. MySQL 8.0 特殊设置要求

#### mysqladmin 修改普通用户密码报错 ？

错误："Access denied; you need the SUPER privilege for this operation"  
原因：mysqlamdin 命令需 SUPER 权限，而普通用户默认没有这个权限。    
方案：使用 `set password=password("newpassword")` 命令修改密码  

#### 一次性删除数据库中的所有表难以成功？

数据表之间的**外键约束**导致有些数据表无法删除

#### 数据库出现死锁？

死锁一般是应用程序设计问题导致，其中事务操作出现死锁的几率更大。  

一旦出现死锁，可以用如下命令确认死锁的原因：

```
MariaDB [(none)]> show innodb status \G;
```
#### 提示 */var/lib/mysql/mysql.sock* 不存在？

原因：使用 mysqldump 或 mysqladmin 等工具时，默认使用 Unix 套接字连接，而不是 TCP/IP。而这个套接字文件（mysql.sock）由于安装原因，并不会一定在 */var/lib/mysql/mysql.sock* 目录。  
方案： 配置文件中指定 mysql.sock 目录


## FAQ{#faq}

#### 单台服务器上可安装多个 MySQL实例？

理论上可以安装多个，但建议安装一个

#### 什么是 MySQL 的 Client 和 Server？

MySQL Server 是指 MySQL 程序本体，而 MySQL Client 指采用TCP协议用于连接程序本地的客户端。它们是两个完全不同的程序，也就是说它们并需要同时安装到同一台服务上。

#### MySQL 中的 test 数据库是什么？

在MySQL5.7 版本之前，安装 MySQL 时会默认包含一个 test 数据库，该数据库仅仅用来测试使用，但是所有能连接到MySQL的用户，几乎都拥有test库的所有权限，因此存在一定的安全隐患。从信息安全角度考虑，如果您发现您使用的 MySQL 中有该 test 数据库，请**务必删除**。

#### Can I modify the root directory of MySQL?

Yes, please refer the documentation [Modify MySQL Data Directory](../mysql#datadirectory)

#### What is the password for the database root user?

The password is stored in the server related file: `/credentials/password.txt`

#### Is there a web-base GUI database management tools?

Yes, phpMyAdmin is on it, visit by *http://Server Internet IP:9090*

#### 如何禁止外界访问 phpMyAdmin？

云控制台安全组关闭 9090 端口

#### 如何停止 phpMyAdmin？

停止 phpMyAdmin 容器即可：

```
sudo docker stop phpmyadmin
```

#### 如何自定义 MariaDB 错误日志文件路径？

修改 MySQL/MariaDB 配置文件中下面的参数即可

```
log-error=/data/mysql/log.err
```

#### 什么是数据库的冷备份和热备份？

冷备份就是停掉数据库服务，复制数据库文件进行备份；  
热备份就是在数据库运行中，实现不停机的备份，并保证数据库完整性。

#### 什么是 MySQL/MariaDB 二进制日志？

二进制日志（binlog）包含描述数据库更改的“操作”，例如创建表操作或更改表数据。 它还包含可能已进行更改的语句的操作（例如，不匹配任何行的 DELETE）。 二进制日志还包含有关每条语句使用更新数据的时间信息。

#### phpMyAdmin 是如何安装的？

采用 Docker 安装，保证 MySQL 环境具有良好的隔离性。

#### MySQL 8.0 默认字符集是？

Mysql8.0 以上安装完默认 character_set_server 为utf8mb4



