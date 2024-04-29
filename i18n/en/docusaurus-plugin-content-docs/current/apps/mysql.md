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

Websoft9 控制台安装 MySQL/MariaDB 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

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

### 主从复制

MariaDB 主从复制是将主数据库的 DDL 和 DML操作通过二进制日志传到复制服务器（也叫从库），然后在从库上对这些日志重新执行（也叫重做），从而使得从库和主库的数据保持同步。

MariaDB 支持一台主库向多台从库进行复制，从库同时也可以作为其他服务器的主库，实现链状架构。

主从复制应用场景：

* 主库出现问题，可以快速切换到从库提供服务
* 从库上执行查询操作，降低主库的访问压力
* 从库上执行备份，避免备份期间影响主库的服务

> 由于复制是异步的或半同步的，所以主从之间的数据总是存在一定的差距。


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

#### 日志太大，磁盘空间不足？{#binlogexceed}

默认安装，MySQL 没有开启 binlog。  

binlog 是一个二进制格式的文件，用于记录用户对数据库**更新的****SQL语句****信息**，例如更改数据库表和更改内容的SQL语句都会记录到binlog里。

binlog 可用于出现没有备份的情况下，恢复数据库。

binlog会占用较大空间，如果用户开启binlog后长期不清理会让剩余磁盘空间为0，从而影响数据库或服务器无法启动

关闭 binlog，只需在配置文件中注释它 `#log_bin=mysql-bin `


#### 数据文件超过上限？

当单个数据文件超过上线时，会导致数据库无法启动。  

此时，需增加磁盘或增加一个新的数据文件地址
```
innodb_data_file_path= /data/mysql/data1:2000M;/data2/mysql/data2:2000M:autoextend
```

#### MySQL 容器无法远程访问？

导致这个问题的可能原因有三点：

1. 端口映射设置错误，导致容器没有网络
2. 容器没有开启远程访问权限
3. MySQL 8.0 特殊设置要求

#### mysqladmin 命令报错 ？

错误："Access denied; you need the SUPER privilege for this operation"  
原因：mysqlamdin 命令需 SUPER 权限，而普通用户默认没有这个权限。    

#### 删除数据库中的所有表失败？

数据表之间的**外键约束**导致有些数据表无法删除

#### 数据库出现死锁？

死锁一般是应用程序设计问题导致，其中事务操作出现死锁的几率更大。  

一旦出现死锁，可以用如下命令确认死锁的原因：

```
MariaDB [(none)]> show innodb status \G;
```

## 原理学习


![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mariadb/mariadb-structure-websoft9.png)

对于 MySQL/MariaDB 管理员来说，需要掌握的知识要点包括：

* MySQL/MariaDB 安装
* SQL 语句
* 基础概念：存储引擎、字符集
* 可视化管理：使用 phpMyAdmin 等可视化工具管理数据库
* 高级管理技术：升级、客户端工具使用、日志管理、备份恢复、监控
* 优化技术：锁、连接池、并发参数、负载均衡、集群、主从、读写分离
* 安全技术：注入

下面，我们把以上要点做一个简单的阐述，希望对你的学习有一定的帮助。


### 基础概念

数据库系统与应用软件系统有着较大的差异，它是存储、检索和计算海量规范化数据的系统，因此它有些独特的基本概念需要用户了解：

#### SQL

SQL 是数据库的一种操作语言（命令），只要登录到数据库后，就可以使用它来操作数据库

* 在命令行下，直接可以运行 SQL 语句
* 在可视化下，打开【运行SQL】的窗口，就可以运行 SQL 语句


SQL 主要分为三种类型：

1. 数据库定义语言（DDL）：主要用于创建或修改数据库、数据段、表、列、索引等对象，主要包括 create、drop、alter 等
2. 数据库操纵语言（DML）：主要用于添加或更新数据库记录等，主要包括 insert、delete、update 等
3. 数据库控制语句（DCL）：主要用于控制权限和访问，主要包括 grant、revoke 等

下面是一些常用的 SQL 命令：

```
# 登录数据库
mysql -u root –p
Enter password:


MariaDB> create database dbname;     #特别注意有分号
MariaDB> show  databases;            #查看数据库
MariaDB> exit;                       #退出数据库控制台，特别注意有分号
MariaDB> drop database 数据库名称;    #删除数据库
MariaDB> show databases;             #查看数据库
MariaDB> alter table tablename raname mytable             #更改表名称
```

在学习中，我们无需熟记每一条语句，而是要有能力根据官方参考手册去定位"做什么事情可能会采用什么语句"。

#### SQL 模式

SQL 模式是 SQL 的标准。由于不同厂商、不同的发展阶段，导致有不同的 SQL 标准出现。

比较流行的 SQL Mode 包括：ANSI、TRADITIONAL 和 STRICT_TRANS_TABLES 等 

#### 存储引擎

MariaDB 存储引擎就是指数据库表的类型，存储引擎决定了表在计算机中的存储方式。

运行 `show engines;` 命令，就会列出所有支持的存储引擎类型：

```
MariaDB [(none)]> show engines;
+--------------------+---------+-------------------------------------------------------------------------------------------------+--------------+------+------------+
| Engine             | Support | Comment                                                                                         | Transactions | XA   | Savepoints |
+--------------------+---------+-------------------------------------------------------------------------------------------------+--------------+------+------------+
| CSV                | YES     | Stores tables as CSV files                                                                      | NO           | NO   | NO         |
| MRG_MyISAM         | YES     | Collection of identical MyISAM tables                                                           | NO           | NO   | NO         |
| MEMORY             | YES     | Hash based, stored in memory, useful for temporary tables                                       | NO           | NO   | NO         |
| Aria               | YES     | Crash-safe tables with MyISAM heritage. Used for internal temporary tables and privilege tables | NO           | NO   | NO         |
| MyISAM             | YES     | Non-transactional engine with good performance and small data footprint                         | NO           | NO   | NO         |
| SEQUENCE           | YES     | Generated tables filled with sequential values                                                  | YES          | NO   | YES        |
| InnoDB             | DEFAULT | Supports transactions, row-level locking, foreign keys and encryption for tables                | YES          | YES  | YES        |
| PERFORMANCE_SCHEMA | YES     | Performance Schema                                                                              | NO           | NO   | NO         |
+--------------------+---------+-------------------------------------------------------------------------------------------------+--------------+------+------------+
8 rows in set (0.000 sec)
```

值得注意的是，只有 **InnoDB** 引擎才支持 **事务处理**。

#### 字符集

MySQL的字符集问题主要是两个概念，一个是 **Character Sets**，一个是 **Collations**，前者是字符内容及编码，后者是对前者进行校对的规则。这两个参数集可以在数据库实例、单个数据库、表、列，连接等四个级别指定。

运行 `SHOW CHARACTER SET;` 命令，就会列出所有支持的存储引擎类型：

```
MariaDB [(none)]> SHOW CHARACTER SET;
+----------+-----------------------------+---------------------+--------+
| Charset  | Description                 | Default collation   | Maxlen |
+----------+-----------------------------+---------------------+--------+
| big5     | Big5 Traditional Chinese    | big5_chinese_ci     |      2 |
| dec8     | DEC West European           | dec8_swedish_ci     |      1 |
| cp850    | DOS West European           | cp850_general_ci    |      1 |
| hp8      | HP West European            | hp8_english_ci      |      1 |
| koi8r    | KOI8-R Relcom Russian       | koi8r_general_ci    |      1 |
| latin1   | cp1252 West European        | latin1_swedish_ci   |      1 |
| latin2   | ISO 8859-2 Central European | latin2_general_ci   |      1 |
| swe7     | 7bit Swedish                | swe7_swedish_ci     |      1 |
| ascii    | US ASCII                    | ascii_general_ci    |      1 |
| ujis     | EUC-JP Japanese             | ujis_japanese_ci    |      3 |
| sjis     | Shift-JIS Japanese          | sjis_japanese_ci    |      2 |
| hebrew   | ISO 8859-8 Hebrew           | hebrew_general_ci   |      1 |
| tis620   | TIS620 Thai                 | tis620_thai_ci      |      1 |
| euckr    | EUC-KR Korean               | euckr_korean_ci     |      2 |
| koi8u    | KOI8-U Ukrainian            | koi8u_general_ci    |      1 |
| gb2312   | GB2312 Simplified Chinese   | gb2312_chinese_ci   |      2 |
| greek    | ISO 8859-7 Greek            | greek_general_ci    |      1 |
| cp1250   | Windows Central European    | cp1250_general_ci   |      1 |
| gbk      | GBK Simplified Chinese      | gbk_chinese_ci      |      2 |
| latin5   | ISO 8859-9 Turkish          | latin5_turkish_ci   |      1 |
| armscii8 | ARMSCII-8 Armenian          | armscii8_general_ci |      1 |
| utf8     | UTF-8 Unicode               | utf8_general_ci     |      3 |
| ucs2     | UCS-2 Unicode               | ucs2_general_ci     |      2 |
| cp866    | DOS Russian                 | cp866_general_ci    |      1 |
| keybcs2  | DOS Kamenicky Czech-Slovak  | keybcs2_general_ci  |      1 |
| macce    | Mac Central European        | macce_general_ci    |      1 |
| macroman | Mac West European           | macroman_general_ci |      1 |
| cp852    | DOS Central European        | cp852_general_ci    |      1 |
| latin7   | ISO 8859-13 Baltic          | latin7_general_ci   |      1 |
| utf8mb4  | UTF-8 Unicode               | utf8mb4_general_ci  |      4 |
| cp1251   | Windows Cyrillic            | cp1251_general_ci   |      1 |
| utf16    | UTF-16 Unicode              | utf16_general_ci    |      4 |
| utf16le  | UTF-16LE Unicode            | utf16le_general_ci  |      4 |
| cp1256   | Windows Arabic              | cp1256_general_ci   |      1 |
| cp1257   | Windows Baltic              | cp1257_general_ci   |      1 |
| utf32    | UTF-32 Unicode              | utf32_general_ci    |      4 |
| binary   | Binary pseudo charset       | binary              |      1 |
| geostd8  | GEOSTD8 Georgian            | geostd8_general_ci  |      1 |
| cp932    | SJIS for Windows Japanese   | cp932_japanese_ci   |      2 |
| eucjpms  | UJIS for Windows Japanese   | eucjpms_japanese_ci |      3 |
+----------+-----------------------------+---------------------+--------+
40 rows in set (0.000 sec)
```

字符集其实就是一套文字符号及编码，对应的文字及编码，可以将人类可以识别的内容与计算机可以识别的信息进行互相转换。  

#### 视图

视图（View）是从一个或多个表中导出来的新表，且这个表是虚拟表。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mariadb/mariadb-whatisview-websoft9.png)

视图的基本上起着类似筛选的作用，并避免重复建表。


#### 索引

索引（Index）顾名思义是为了便于快速检索数据而建立的指向表（专业术语称之为：指针），类似新华字典中的音序表。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mariadb/mariadb-whatisindex-websoft9.png)

#### 触发器

触发器（Triggers）是由 Insert、Update、Delete 等事件触发的某种特定操作，满足这些触发器的触发条件时，数据库系统就会执行触发器自定义的程序语句。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mariadb/mariadb-whatistrigger-websoft9.png)

#### 事务

事务（Transaction）主要用于处理操作量大，复杂度高的数据。比如说，在人事系统中，你删除一个员工，你既需要删除人员的基本资料，也要删除和该人员相关的信息，如工资条，考勤数据等等，这样，这些数据库操作语句就构成一个事务。

事务以 begin 语句开始，以 commit 语句结束：

```
mysql> begin;  # 开始事务
Query OK, 0 rows affected (0.00 sec)
 
mysql> insert into runoob_transaction_test value(5);
Query OK, 1 rows affected (0.01 sec)
 
mysql> insert into runoob_transaction_test value(6);
Query OK, 1 rows affected (0.00 sec)
 
mysql> commit; # 提交事务
Query OK, 0 rows affected (0.01 sec)
```

一般来说，事务是必须满足4个条件（ACID）：：原子性（Atomicity，或称不可分割性）、一致性（Consistency）、隔离性（Isolation，又称独立性）、持久性（Durability）。

通俗的解释如下：**“要么成功，要么不成功后复原。”**

#### 存储过程

存储过程（Procedure）就是在数据库中预先编写基于 SQL 的程序段，以便应用程序调用。 

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mariadb/mariadb-whatisprocedure-websoft9.png)

既然是程序段，它当然会支持常见的程序语法：函数、条件判断、循环等。

通俗的解释：“数据库 SQL 编程”

#### 分区

分区（Partition）是一种物理数据库设计技术，主要把逻辑上的单个表从物理上划分为数十个物理分区。  

其主要目的是为了在特定的 SQL 操作中减少数据读写的总量以缩减响应时间。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mariadb/mariadb-whatispartition-websoft9.png)

### 高级管理

#### 用户权限

MariaDB 用户主要包括 root 用户和普通用户，其中 root 用户即管理员，它具有最高级的数据库权限。 

> 一般来说，用户不会去更改 root 用户的设置，下面我们重点介绍普通用户。

用户管理包含两方面的知识要点：

* 用户账号信息
* 用户账号权限

在 MariaDB 中，一个用户的账号是有：**username:host:password** 三个部分组成的。

MariaDB 默认有一个名为 **mysql** 的数据库，它的下面存储的都是用户账号、用户权限相关的表，用户登录数据库，就根据这些表来判断用户具备哪些权限，从而实现权限控制。

与用户权限有关的表包括（按优先级排序）：

【user】>【db】>【host】>【table-priv】>【columns-priv】>【proc-priv】

权限大小维度看，又依次为：系统、数据库、表、视图、索引、存储过程等

下面是 user 表的表结构信息：

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mariadb/mariadb-usertable-websoft9.png)

有一个特殊命令 **grant**，它是用于给其他用户（包括自身）授权的命令操作。

#### 备份还原

先明确与备份有关的名词：

从备份的对象数据格式来说，备份分为：

* 逻辑备份：将数据库【导出】而实现的备份
* 物理备份：拷贝数据库的物理文件而实现的备份

从备份时数据库状态来说，备份又可以分为：

* 冷备份：数据库停机后备份
* 热备份：数据库不停机备份（必须保持数据的完整性）

MariaDB 支持三种备份和还原方式：

* 备份恢复工具：mysqldump 或 mysqlhotcopy 等
* 复制数据目录
* 导出导入表

mysqldump 是官方提供的命令，简单实用：

```
# 分别备份一个、多个和所有数据库
mysqldump -u usename -p dbname > dbname.sql
mysqldump -u usename -p dbname1 dbname12 > dbname.sql
mysqldump -u usename -p --all-database > all-database.sql
```

#### 日志

Mariadb 日志是记录 MariaDB 数据库日常操作和错误信息的文件，可以分为：

* 二进制日志（Binlog）
* 错误日志
* 慢查询日志
* 通用查询日志

二进制日志记录所有操作数据库的动作，适用于恢复数据库；  
错误日志适用于诊断问题；  
慢查询日志用于记录执行效率较低的查询语句；  
通用查询日志记录所有的查询操作；  

从排查故障的角度看，错误日志和慢查询日志是需要重点考虑的日志对象。

#### 监控

数据库监控主要是通过监控工具，主动发现异常，并推动后续的故障运维流程。  

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mariadb/mariadb-monitorgui-websoft9.png)

数据库监控相关的开源软件包括：

* Nagios
* Cacti
* Zabbix
* Ganglia

#### 优化

优化是通过分析数据库的某个时间周期的状况，通过参数调整和计算资源改善实现数据库性能的提升。  

下面我们重点介绍优化入门方法：

1. 登录 MariaDB 数据库
2. 运行 `show status like 'vaule' ` 语句查看性能相关的参数，诊断整体性能
   ```
    MariaDB [(none)]> show status like 'connections';
    +---------------+-------+
    | Variable_name | Value |
    +---------------+-------+
    | Connections   | 12    |
    +---------------+-------+
    1 row in set (0.000 sec)
   ```
   * connection: 连接次数
   * uptime: 服务器上线时间
   * slow_queries: 慢查询次数
   * com_select：查询操作次数
   * com_insert: 插入操作次数
   * com_update：更新操作次数
   * com_delete：删除操作次数

3. 采用索引和视图减少数据库检索
4. 将大表（字段很多）拆分成多个小表
5. 分析和优化表 `analyze table name;`
6. 优化服务器配置
7. 优化 my.cnf 中的缓存和内存配置项（**高手才能驾驭**）

#### 安全

数据库独特的安全风险来源于 **SQL 注入** 问题。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mariadb/mariadb-whatissqlinject-websoft9.png)

#### 审计

全球数字经济发展蓬勃，伴随的数据安全成为重大的隐患。各国目前都出台了与网络安全相关的法律，对于数据保护、隐私管理作出了明确的规定。  

数据库的安全是重中之重。数据库审计是对数据库资源利用率和权限的跟踪，特别是监视和记录用户数据库操作，审计满足日益严格的合规性要求。

审计可以基于多种因素，包括单个操作（例如，执行的SQL语句的类型），也可以基于多种因素的组合（例如，用户名，应用程序，时间等）。执行常规的数据库日志分析可以增强内部安全措施通过回答诸如谁更改了关键数据，何时更改关键数据等问题。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mariadb/mariadb-audit-websoft9.png)

如何开始启动 MariaDB 的审计呢？

1. 安装 **[Maria Audit Plugin](https://mariadb.com/kb/en/mariadb-audit-plugin/)** 插件
2. 设置审计日志路径
