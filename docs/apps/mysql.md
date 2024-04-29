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

### 测试可用性{#wizard}

Websoft9 控制台安装 MySQL/MariaDB 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

1. 进入 MySQL 容器的命名模式，登录测试可用性
   ```
   mysql -uroot -p
   ```
2. 登录成功会进入 MySQL 客户端模式

### 图形化工具

Websoft9 应用商店安装 [phpMyAdmin](./phpmyadmin) 或 [CloudBeaver](./cloudbeaver#mysql) 后，可以在**不需要开启外网**的情况下管理 MySQL


## 配置选项{#configs}

- 配置文件目录（已挂载）：/etc/mysql/conf.d
- 初始化脚步目录（已挂载）：/docker-entrypoint-initdb.d
- 端口：3306
- 主从复制（√）：DDL 和 DML 操作通过二进制日志复传到从库，支持一主多从
- 数据库主机名：容器名
- 外网端口：安装时用户自定义选
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

MySQL默认没有开启 Binary Log，修改 [MySQL 配置文件] (#configs)相关项

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

通过临时容器重置密码：

1. 停止 MySQL 容器，运行一个新的临时 MySQL 容器与旧容器共享存储目录
2. 在临时容器中修改密码，再删除临时容器
3. 恢复运行原 MySQL 容器


### 备份（导出）

- 推荐使用 phpMyAdmin等可视化工具，[导出](./phpmyadmin#exportimport)数据库（建议SQL格式）

- 开发者可以使用 **mysqldump** 工具导出（效率更高，通用性更强）
   ```
   mysqldump -uroot -p databasename>databasename.sql
   ```

### 恢复（导入）

1. 登录 phpMyAdmin，打开顶部的【导入】标签页，根据向导开始导入

2. 导入过程中可能会出现数据库字符集不兼容的情况，需要人工干预处理


### 迁移{#migration}

MySQL 到 MySQL 的迁移，通常可以通过数据的**导入导出**快速实现。    

但是，其他 DBMS 到 MySQL 的迁移最好是使用迁移工具，例如：[MySQL Workbench: Database Migration](https://www.mysql.com/products/workbench/migrate/)


### 审计

1. 安装 **[Maria Audit Plugin](https://mariadb.com/kb/en/mariadb-audit-plugin/)** 插件
2. 设置审计日志路径


## 问题与故障

#### 如何分析数据库日志？

Mariadb 日志是记录 MariaDB 数据库日常操作和错误信息的文件，可以分为：

* 二进制日志（Binlog）：记录所有操作数据库的动作，适用于恢复数据库
* 错误日志：适用于诊断问题
* 慢查询日志：记录执行效率较低的查询语句
* 通用查询日志：记录所有的查询操作

从排查故障的角度看，**错误日志和慢查询日志**是需要重点考虑的日志对象。

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

#### 日志导致磁盘空间不足？{#binlogexceed}

- 手工清理日志
- 考虑注释配置文件项 `#log_bin=mysql-bin` 关闭 binlog

#### 数据文件超过上限？

当单个数据文件超过上线时，会导致数据库无法启动。此时，需增加磁盘或增加一个新的数据文件地址
```
innodb_data_file_path= /data/mysql/data1:2000M;/data2/mysql/data2:2000M:autoextend
```

#### MySQL 容器无法远程访问？

可能原因有三点：

1. 端口映射设置错误，导致容器没有网络
2. 容器没有开启远程访问权限
3. MySQL 8.0 特殊设置要求

#### mysqladmin 命令报错 ？

错误："Access denied; you need the SUPER privilege for this operation"  
原因：mysqlamdin 命令需 SUPER 权限，而普通用户默认没有这个权限。    

#### 无法删除所有表？

数据表之间的**外键约束**导致有些数据表无法删除

#### 数据库出现死锁？

死锁一般是应用程序设计问题导致，其中事务操作出现死锁的几率更大。  

一旦出现死锁，可以用如下命令确认死锁的原因：

```
MariaDB [(none)]> show innodb status \G;
```