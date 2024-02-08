---
sidebar_position: 3
slug: /mysql/admin
tags:
  - MySQL
  - Cloude Native Database
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup) 相关章节。


## 场景

### MySQL 备份与恢复{#backup}



### MySQL 大版本升级{#upgrade}

Linux 上数据库大版本之间的差异较大，无法提供稳妥的升级方案

Windows 上的 MySQL 升级分为两部分：

1. 使用Windows Update升级Windows系统
2. 下载最新的MySQL，停止MySQL服务，替换MySQL的旧文件

升级完成后，需要运行 `mysql_upgrade` 命令：
 
```
mysql_upgrade -u root -p 13456
```



## 故障排除{#troubleshoot}


除以下列出的 MySQL 故障问题之外， [通用故障处理](../troubleshoot) 专题章节提供了更多的故障方案。 





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

修改 [MySQL 配置文件](../mysql#path)

```
log-error=log_error=/var/log/mysql/error.log
```

#### 什么是数据库的冷备份和热备份？

冷备份就是停掉数据库服务，复制数据库文件进行备份；  
热备份就是在数据库运行中，实现不停机的备份，并保证数据库完整性。

#### 什么是 MySQL/MariaDB 二进制日志？

二进制日志（binlog）包含描述数据库更改的“操作”，例如创建表操作或更改表数据。 它还包含可能已进行更改的语句的操作（例如，不匹配任何行的 DELETE）。 二进制日志还包含有关每条语句使用更新数据的时间信息。

#### phpMyAdmin 是如何安装的？

采用 Docker 安装，保证 MySQL 环境具有良好的隔离性。

#### MySQL 8.0 默认字符集是？

Mysql8.0 以上安装完默认 character_set_server 为utf8mb4。



