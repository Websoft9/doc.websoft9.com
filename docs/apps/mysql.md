---
title: MySQL
slug: /mysql
tags:
  - 数据库
  - 关系型
  - RDS
  - MariaDB
---

import Meta from './_include/mysql.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 MySQL/MariaDB 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

1. 在容器中运行数据库登陆命令，连接数据库
   ```
   mysql -uroot -p
   ```
2. 登录成功会显示如下信息
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/mysql/mysql_command.png)

### Web 可视化管理

- [phpMyAdmin](./phpmyadmin)
- [CloudBeaver](./cloudbeaver#mysql)

## 配置选项{#configs}

- 配置文件目录：/etc/mysql/conf.d
- 初始化脚步目录：/docker-entrypoint-initdb.d
- 端口：3306
- 数据库主机名：容器名
- 外网端口：docker-compose 端口绑定
- [Connectors and APIs](https://dev.mysql.com/doc/index-connectors.html)
- 命令行
  * mysql
  * mysqladmin
  * mysqldump 
  * mysqlhotcopy
  * mysqlcheck
  * mysqlshow
  * mysqlimport
  * mysqlbinlog
  * myisampack

## 管理维护{#administrator}

### 设置 Binary Log

MySQL默认没有开启 Binary Log，修改 [MySQL 配置文件](#path)相关项

```
log_bin = mysql-bin      # enable Binary log
binlog_format = mixed    # Binary log format
expire_logs_days = 7     # Binary log expire time
```

### 设置 MySQL 远程访问{#remote}

进入到 MySQL 容器的命令模式，设置 MySQL 远程访问：

```
# 开启远程访问
mysql>  use mysql;
mysql>  update user set host = '%' where user = 'root';
```

### 修改密码

执行一下命令:
```
mysqladmin -u 用户名 -p 旧密码 password '新密码' 
```

### 重置密码

MySQL 容器重置密码的主要步骤描述：

1. 停止 MySQL 容器，运行一个新的临时 MySQL 容器，使用原 MySQL 的数据
2. 在临时容器中修改密码
3. 恢复原 MySQL 容器


### 备份（导出）

1. 使用 phpMyAdmin等可视化工具，[导出](./phpmyadmin#exportimport)数据库（建议SQL格式）

2. 或使用 **mysqldump** 工具导出（效率更高，通用性更强）
   ```
   mysqldump -uroot -p databasename>databasename.sql
   ```
3. 将备份文件下载到本地，备份工作完成


### 恢复（导入）

1. 登录 phpMyAdmin，打开顶部的【导入】标签页，根据向导开始导入
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-import-websoft9.png)

2. 导入过程中可能会出现数据库字符集不兼容的情况，需要人工干预处理


### 迁移{#migration}

MySQL 到 MySQL 的迁移，通常可以通过数据的**导入导出**快速实现。    

但是，其他 DBMS 到 MySQL 的迁移最好是使用迁移工具，例如：[MySQL Workbench: Database Migration](https://www.mysql.com/products/workbench/migrate/)

## 故障

#### 导入数据库报错？

查看脚本里面是否有创建数据库的脚本

#### 数据库服务无法启动？

导致 MySQL 无法启动的主要原因有：

* 磁盘空间不足（二进制日志文件大小增长过快）
* 死锁
* MySQL 配置文件错误

建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看数据库日志
docker logs container_name
```

#### MySQL 日志太大，导致磁盘空间不足？{#binlogexceed}

默认安装，mysql没有开启binlog，binlog是一个二进制格式的文件，用于记录用户对数据库**更新的****SQL语句****信息**，例如更改数据库表和更改内容的SQL语句都会记录到binlog里。

binlog主要用于出现没有备份的情况下，恢复数据库。但binlog会占用较大空间，如果用户开启binlog后长期不清理会让剩余磁盘空间为0，从而影响数据库或服务器无法启动

如果对自己的备份有信心，不需要binlog功能，参考如下步骤关闭之：

1. 编辑 [MySQL 配置文件](../mysql#path)
  ~~~
  #log_bin=mysql-bin 
  ~~~
2. 重启mysql
  ~~~
  sudo docker restart mysql
  ~~~

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
