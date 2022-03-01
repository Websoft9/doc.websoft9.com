---
sidebar_position: 2
slug: /mariadb/admin
tags:
  - MariaDB 
  - Cloude Native Database
---

# 维护参考


## 系统参数

MariaDB 预装包包含 MariaDB 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径
MariaDB 安装到 Linux 还是 Windows 系统，对应的路径有很大的差异，请根据实际情况参考：

#### Linux

##### MariaDB

MariaDB 配置文件: */etc/my.cnf*   
MariaDB 数据目录：*/data/mariadb*   
MariaDB 错误日志: */data/mariadb/mariadb.err*  
MariaDB Socket: */data/mariadb/mariadb.sock*

##### phpMyAdmin

phpMyAdmin 是一款可视化 MySQL 管理工具，在本项目中它基于 Docker 安装。  

phpMyAdmin directory：*/data/apps/phpmyadmin*  
phpMyAdmin docker compose file：*/data/apps/phpmyadmin/docker-compose.yml* 

#### Windows

* 目录：C:/websoft9/mariadb
* 配置文件：C:/websoft9/mariadb/etc/my.ini
* 数据文件目录:：C:/websoft9/mariadb/data

### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp` 看查看相关端口，下面列出可能要用到的端口：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| phpMyAdmin on Docker | 9090 | 通过 HTTP 访问 phpMyAdmin | 可选 |
| MariaDB | 3306 | 远程连接 MariaDB | 可选 |

### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Check all components version
sudo cat /data/logs/install_version.txt

# Linux Version
lsb_release -a

# MariaDB version
MariaDB -V

# MariaDB Version
docker -v
```

### 服务

使用由 Websoft9 提供的 MariaDB 部署方案，可能需要用到的服务如下：

#### Linux系统

##### MariaDB
```shell
sudo systemctl start mariadb
sudo systemctl stop mariadb
sudo systemctl restart mariadb
sudo systemctl status mariadb
```

##### Docker

```shell
sudo systemctl start docker
sudo systemctl restart docker
sudo systemctl stop docker
sudo systemctl status docker
```

#### Windows 系统

Windows下的镜像采用操作系统的服务管理功能，来实现 MariaDB 的启动、停止和重启操作
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/mysql-servicewin-websoft9.png)


## 备份

### MariaDB 备份

MariaDB 数据库备份主要通过**导出数据库**实现最小化的备份方案。

下面以列表的方式介绍这种备份：
```
- 备份范围: 数据库和应用程序
- 备份效果: 一般
- 备份频率: 一周最低1次，备份保留30天
- 恢复方式: 重新导入
- 技能要求：非常容易
- 自动化：无
```

通用的手动备份操作步骤如下：

1. 使用phpMyAdmin等可视化工具，导出数据库（建议SQL格式）
2. 或使用 **mysqldump** 工具导出（效率更高，通用性更强）
   ```
   mysqldump -uroot -p databasename>databasename.sql
   ```
2. 将备份文件下载到本地，备份工作完成

在 phpMyAdmin 中，【导出】相当于备份数据库，【导入】相当于恢复数据库。

#### 导出

1. 登录 phpMyAdmin，打开顶部的【导出】标签页
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-export-websoft9.png)

2. 选择合适的备份文件类型、备份存放方式，然后开始备份

3. 最好将备份文件下载到本地存放


## 恢复

### 导入恢复

1. 登录 phpMyAdmin，打开顶部的【导入】标签页，根据向导开始导入
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-import-websoft9.png)

2. 导入过程中可能会出现数据库字符集不兼容的情况，需要人工干预处理

## 升级

### 系统级更新

运行一条更新命令，即可完成系统级更新：

``` shell
#For Ubuntu&Debian
apt update && apt upgrade -y

#For Centos&Redhat
yum update -y
```
> 本部署包已预配置一个用于自动更新的计划任务。如果希望去掉自动更新，请删除对应的Cron


### MariaDB 更新升级

#### On Linux

上面的系统升级命令，支持小版本升级。例如：5.6.x to 5.6.y 或 5.7.x to 5.7.y

数据库大版本之间的差异较大，无法提供稳妥的升级方案

#### On Windows

Windows 上的 MySQL 升级分为两部分：

1. 使用Windows Update升级Windows系统
2. 下载最新的MySQL，停止MySQL服务，替换MySQL的旧文件


### 常见升级问题

#### 大版本升级后，无法更改数据库密码？
```
mysql_upgrade -u root -p 13456
```


## 故障处理

此处收集使用 MariaDB 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 导入数据库报错？

查看脚本里面是否有创建数据库的脚本

#### 数据库服务无法启动

数据库服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看数据库日志
cat /data/mariadb/mariadb.err
```

#### 数据库日志文件太大，导致磁盘空间不足？

默认安装，mysql会自动开启binlog，binlog是一个二进制格式的文件，用于记录用户对数据库**更新的****SQL语句****信息**，例如更改数据库表和更改内容的SQL语句都会记录到binlog里。

binlog主要用于出现没有备份的情况下，恢复数据库。但binlog会占用较大空间，长期不清理会让剩余磁盘空间为0，从而影响数据库或服务器无法启动

如果对自己的备份有信心，不需要binlog功能，参考如下步骤关闭之：

1. 编辑 [MariaDB 配置文件](/zh/stack-components.md#mariadb)，注释掉 binlog 日志
  ~~~
  #log-bin=mysql-bin  
  ~~~
2. 重启 MySQL 服务
  ~~~
  sudo systemctl restart mariadb
  ~~~

#### MariaDB 容器无法远程访问？

导致这个问题的可能原因有三点：

1. 端口映射设置错误，导致容器没有网络
2. 容器没有开启远程访问权限
3. MariaDB 某些版本的特殊要求

#### mysqladmin 修改普通用户密码 "Access denied; you need the SUPER privilege for this operation"？

原因：mysqlamdin 命令需 SUPER 权限，而普通用户默认没有这个权限。  
方案：使用 `set password=password("newpassword")` 命令修改密码

#### 一次性删除指定数据库中的所有表为什么难以成功？

数据表之间的**外键约束**导致有些数据表无法删除

#### 数据库出现死锁？

死锁一般是应用程序设计问题导致，其中事务操作出现死锁的几率更大。  

一旦出现死锁，可以用如下命令确认死锁的原因：

```
MariaDB [(none)]> show innodb status \G;
```

#### 磁盘空间不足导致数据库无法启动？

增加磁盘或增加一个新的数据文件地址
```
innodb_data_file_path= /data/mariadb/data1:2000M;/data2/mariadb/data2:2000M:autoextend
```

#### 提示 */var/lib/mysql/mysql.sock* 不存在？

原因：使用 mysqldump 或 mysqladmin 等工具时，默认使用 Unix 套接字连接，而不是 TCP/IP。而这个套接字文件（mysql.sock）由于安装原因，并不会一定在 */var/lib/mysql/mysql.sock* 目录。  
方案： 配置文件中指定 mysql.sock 目录

## 常见问题

#### MariaDB 是完全免费的吗？

MariaDB Community Server   是免费开源版，MariaDB Enterprise Server 是收费开源版  

详情[对比参考](https://mariadb.com/pricing/)

#### 单台服务器上是否可以安装多个 MariaDB 实例？

支持，但实际上不建议

#### 什么是 MariaDB 的 Client 和 Server？

MariaDB Server 是指 MariaDB 程序本体，而 MariaDB Client 指采用TCP协议用于连接程序本地的客户端。它们是两个完全不同的程序，也就是说它们并需要同时安装到同一台服务上。


#### MariaDB 中的 test 数据库是什么？

在MariaDB5.7 版本之前，安装 MariaDB 时会默认包含一个 test 数据库，该数据库仅仅用来测试使用，但是所有能连接到MariaDB的用户，几乎都拥有test库的所有权限，因此存在一定的安全隐患。从信息安全角度考虑，如果您发现您使用的 MariaDB 中有该 test 数据库，请**务必删除**。

#### 是否可以修改 MariaDB 根目录？

可以，但不建议修改

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin

#### 如何停止 phpMyAdmin？

停止 phpMyAdmin 容器即可：

```
sudo docker stop phpmyadmin
```

#### 如何自定义 MariaDB 错误日志文件路径？

修改配置文件中下面的参数即可
```
log-error=/data/mariadb/log.err
```

#### 什么是数据库的冷备份和热备份？

冷备份就是停掉数据库服务，复制数据库文件进行备份；  
热备份就是在数据库运行中，实现不停机的备份，并保证数据库完整性。