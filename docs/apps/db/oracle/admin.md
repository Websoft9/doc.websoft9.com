---
sidebar_position: 3
slug: /oracle/admin
tags:
  - 故障
  - 路径
---


# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup) 相关章节。

## 场景

### Oracle 导出和导入

Oracle Data Pump 支持将数据和元数据从一个数据库高速移动到另一个数据库。 

导出和导入命令如下：  

* expdp
* impdp

### Oracle 备份与恢复

Oracle 备份与恢复主要通过 Recovery Manager (RMAN) 实现。  

```
$ docker exec -it oracle rman

Recovery Manager: Release 21.0.0.0.0 - Production on Fri Jul 8 03:52:17 2022
Version 21.3.0.0.0

Copyright (c) 1982, 2021, Oracle and/or its affiliates.  All rights reserved.

RMAN>
```

### Oracle 升级

本应用基于 Docker 安装，其升级采用通用的 Docker 应用升级方案即可。 

### Oracle 数据库复制

Oracle GoldenGate 是一种异步、基于日志的实时数据复制产品。

### Oracle 集群

Oracle 集群又称之为 Oracle Real Application Clusters (Oracle RAC)，它支持多个实例共享对 Oracle 数据库的访问。  

Oracle Clusterware 是实现 Oracle RAC 的工具。  

## 故障排除{#troubleshoot}

除以下列出的 Oracle 故障问题之外， [通用故障处理](../troubleshoot) 专题章节提供了更多的故障方案。  

#### Error "ORA-28040: No matching authentication protocol"？

问题原因： 客户端与服务端的协议版本不一致   
解决方案： 升级客户端

####  ORA-28009: connection as SYS should be as SYSDBA or SYSOPER？

问题原因： 连接数据库时用户与默认的 role 不匹配    
解决方案： 连接信息中的 role  选择为 SYSDBA or SYSOPER

## 问题解答{#faq}

#### Oracle 企业版或标准版免费吗？

不免费，需获得 Oracle 官方授权方可使用

#### Oracle 多数据库架构？

从 12c 之后，Oracle 开始支持多个数据库实例，并逐渐演化成现在的多租户架构。  

![](https://docs.oracle.com/en/database/oracle/oracle-database/21/cncpt/img/cncpt389.png)

* 从 Oracle Database 21c 开始，“数据库”特指多租户容器数据库 (CDB)、可插拔数据库 (PDB)或应用程序容器的数据文件。
* CDB 是 Oracle 对数据库（PDB）的逻辑分组，多个数据库在逻辑上可以组合成一个 CDB。

#### SID 和 Service Name 区别？

SID 是数据库实例唯一的名称。 Service Name 是向监听（TNS）注册后的别名。可以给同一个数据库实例配置多个 Service Name。  

所以，大多数情况下， SID 和 Service Name 名称是相同的。  

#### 表空间和模式对象（ Segment）？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle/oracle-concepttablespaces-websoft9.jpg)

* 表空间：对数据库的逻辑划分，每个表空间包含一个或多个物理的数据库文件。表空间是 Oracle 数据库恢复的最小单位，容纳着许多数据库实体，如表、视图、索引、聚簇、回退段和临时段等。
* 模式对象：数据库用户拥有一个与用户名同名的数据库模式。

#### Oracle 数据库有哪些可视化管理工具？

* EM：企业管理器，主要是监控作用
* Oracle SQL Developer：可以导入导出、编写 SQL 脚本等
* ORDS：是 Oracle Web 化的中间件，提供 API，PL/SQL 等能力，集成了 Oracle SQL Developer
* APEX：是基于 ORDS 的一个无代码开发平台

#### PL/SQL 是什么？

PL/SQL 是 Oracle 服务端的存储过程编程语言

#### Oracle 网络服务必须配置吗？

Oracle 网络服务在分布式异构计算环境中提供企业范围的连接解决方​​案。Oracle Net 是 Oracle Net Services 的一个组件，它支持从客户端应用程序到数据库的网络会话。  

所以，在单机环境下，它不是必须的配置。  

#### Oracle 用户信息保存在哪里？

保存在 sys 下的 user$ 表里面：

```
select * from sys.user$;
```
