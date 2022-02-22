---
sidebar_position: 3
slug: /mysql/study
tags:
  - MySQL
  - Cloude Native Database
---

# 原理学习

对于 MySQL 管理员来说，需要掌握的知识要点包括：

* MySQL 安装
* 运行 SQL 语句
* 开发技术：存储引擎、字符集
* 可视化管理：使用 phpMyAdmin 等可视化工具管理数据库
* 高级维护技术：升级、客户端工具使用、日志管理、备份恢复、监控
* 优化技术：锁、连接池、并发参数、负载均衡、集群、主从、读写分离
* 安全技术：注入

下面，我们把以上要点做一个简单的阐述，希望对你的学习有一定的帮助。

## MySQL 安装原理
  
对于 Windows 系统，官方提供了一键安装包和解压免安装包两种方式  
对于 Linux 系统，官方提供了 rpm/deb 自动安装包和源码编译安装包两种方式。  

Websoft9 云原生项目采用的是 rpm/deb 自动安装包的方式。

## SQL 介绍

SQL 是数据库的一种操作语言（命令），只要登录到数据库后，就可以使用它来操作数据库

* 在命令行下，直接可以运行 SQL 语句
* 在可视化下，打开【运行SQL】的窗口，就可以运行 SQL 语句


SQL 主要分为三种类型：

1. 数据库定义语言（DDL）：主要用于创建或修改数据库、数据段、表、列、索引等对象，主要包括 create、drop、alter 等语句
2. 数据库操纵语言（DML）：主要用于添加或更新数据库记录等，主要包括 insert、delete、update 等语句
3. 数据库控制语句（DCL）：主要用于控制权限和访问，主要包括 grant、revoke 等语句

下面是一些常用的 SQL 命令：

```
# 登录数据库
mysql -u root –p
Enter password:


MySQL> create database dbname;     #特别注意有分号
MySQL> show  databases;            #查看数据库
MySQL> exit;                       #退出数据库控制台，特别注意有分号
MySQL> drop database 数据库名称;    #删除数据库
MySQL> show databases;             #查看数据库
MySQL> alter table tablename raname mytable             #更改表名称
```

在学习中，我们无需熟记每一条语句，而是要有能力根据官方参考手册去定位"做什么事情可能会采用什么语句"。


## 开发要点

MySQL 开发无疑博大精深，在我们工作过程中，最常见的要点为：

### 存储引擎

### 字符集

MySQL 技术体系中分为：

* 字符集（character set），用于存储字符串的方式，例如 utf8mb4
* 排序字符集（collation），用于定义了比较字符串的方式，例如 utf8mb4-general_ci

可见排序字符集的前缀是字符集。

Mysql8.0以上安装完默认character_set_server 为utf8mb4


### 视图

### 存储过程

### 触发器

### 事物控制

### SQL Mode

### 分区

## 优化技术

## 安全技术

## 参阅

本文档的撰写过程中，我们参考了大量的书籍和博客，下面列出主要来源：

* 《深入浅出MySQL 数据库开发、优化与维护管理（第二版）》 人民邮电出版社