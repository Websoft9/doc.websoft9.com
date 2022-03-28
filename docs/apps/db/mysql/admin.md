---
sidebar_position: 3
slug: /mysql/admin
tags:
  - MySQL
  - Cloude Native Database
---

# 维护参考


## 场景

### MySQL 备份与恢复

##### 备份（导出）

1. 使用 phpMyAdmin等可视化工具，[导出](../mysql#phpmyadminexportimport)数据库（建议SQL格式）

2. 或使用 **mysqldump** 工具导出（效率更高，通用性更强）
   ```
   mysqldump -uroot -p databasename>databasename.sql
   ```
2. 将备份文件下载到本地，备份工作完成


##### 恢复（导入）

1. 登录 phpMyAdmin，打开顶部的【导入】标签页，根据向导开始导入
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-import-websoft9.png)

2. 导入过程中可能会出现数据库字符集不兼容的情况，需要人工干预处理


### MySQL 大版本升级

Linux 上数据库大版本之间的差异较大，无法提供稳妥的升级方案

Windows 上的 MySQL 升级分为两部分：

1. 使用Windows Update升级Windows系统
2. 下载最新的MySQL，停止MySQL服务，替换MySQL的旧文件

升级完成后，需要运行 `mysql_upgrade` 命令：
 
```
mysql_upgrade -u root -p 13456
```



## 故障处理


除以下列出的 MySQL 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。 


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

#### 日志文件太大，导致磁盘空间不足？

默认安装，mysql会自动开启binlog，binlog是一个二进制格式的文件，用于记录用户对数据库**更新的****SQL语句****信息**，例如更改数据库表和更改内容的SQL语句都会记录到binlog里。

binlog主要用于出现没有备份的情况下，恢复数据库。但binlog会占用较大空间，长期不清理会让剩余磁盘空间为0，从而影响数据库或服务器无法启动

如果对自己的备份有信心，不需要binlog功能，参考如下步骤关闭之：

1. 编辑 [MySQL 配置文件](/zh/stack-components.md#mysql)，注释掉 binlog 日志
  ~~~
  #log-bin=mysql-bin  
  ~~~
2. 重启mysql
  ~~~
  systemctl restart mysqld
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


## 问题解答

#### 单台服务器上可安装多个 MySQL实例？

理论上可以安装多个，但建议安装一个

#### 什么是 MySQL 的 Client 和 Server？

MySQL Server 是指 MySQL 程序本体，而 MySQL Client 指采用TCP协议用于连接程序本地的客户端。它们是两个完全不同的程序，也就是说它们并需要同时安装到同一台服务上。

#### MySQL 中的 test 数据库是什么？

在MySQL5.7 版本之前，安装 MySQL 时会默认包含一个 test 数据库，该数据库仅仅用来测试使用，但是所有能连接到MySQL的用户，几乎都拥有test库的所有权限，因此存在一定的安全隐患。从信息安全角度考虑，如果您发现您使用的 MySQL 中有该 test 数据库，请**务必删除**。

#### 是否可以修改 MySQL 根目录？

可以，但不建议修改

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置 phpMyAdmin

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



