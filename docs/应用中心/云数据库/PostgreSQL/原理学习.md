---
sidebar_position: 3
slug: /postgresql/study
tags:
  - PostgreSQL
  - Cloud Native Database
---

# 原理学习

PostgreSQL 是由 PostgreSQL 社区志愿者开发的开源关系型数据库系统，它源于 UC Berkeley 大学 1977 年的 Ingres 计划。它稳定可靠，有很多前言的技术特征，并且性能卓越，在数据完整性和正确性方面赢得了良好的市场声誉。

## 概念

### 数据类型

PostgreSQL 支持官方的数据类型，包括：数据、JASON、JSONB 以及几何类型，还可以使用 SQL 命令创建自定义类型

### C/S 架构

PostgreSQL 本身是一个 C/S 架构的程序，即包括客户端程序和服务器程序。

* 客户端程序：psql, clusterdb, pgAdmin等
* 服务器程序：initdb, pg_ctl, postgres, postmaster, pg_upgrade等

## 配置

PostgreSQL 有两个重要的全局配置文件：postgresql.conf, pg_hba.conf。它们提供了很多可配置的参数，这些参数从不同层面影响着数据库的行为

* postgresql.conf 配置文件主要负责配置文件位置、资源限制、集群负责等
* pg_hba.conf 配置文件主要负责客户端的连接和认证

### 连接方式

PostgreSQL 允许四种连接方式，包括：

* local: 基于 Unix 域套接字的连接方法，域套接字是进程间的一种非网络通信机制，效率高，安全可靠
* host: 基于 TCP/IP 的连接，允许非 SSL 连接，默认值只允许 localhost 本地连接。
* hostssl: 基于 TCP/IP 的 SSL 加密连接
* hostnossl: 基于 TCP/IP 的非 SSL 连接

### 认证方法

PostgreSQL 常见的[认证方法](https://www.postgresql.org/docs/current/auth-methods.html)包括：

* reject: 拒绝某一网段的少数特定主机
* md5: 双种MD5加密
* password: 明文密码
* scram-sha-256: 基于SASL的加密认证，是 PostgreSQL 最安全的认证方式，但不支持 10 以下的版本
* trust： 完全信任
* peer：基于 unix socket 免密连接

## CLI：PSQL

PSQL 是 PostgreSQL 自带的命令行客户端工具，有非常丰富的功能。本节介绍 PSQL 常用的功能和用法。

### 连接数据库

先切换到 postgre 用户，在运行 `psql` 命令，即可使用 psql 连接数据库

```
sudo -i -u postgres
psql

psql (12.3)
Type "help" for help.

postgres=#
```
