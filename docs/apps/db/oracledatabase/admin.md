---
sidebar_position: 3
slug: /oracledatabase/admin
tags:
  - Oracle Database
  - Cloude Native Database
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup/) 相关章节。

## 场景

## 故障排除{#troubleshoot}

除以下列出的 Oracle Database 故障问题之外， [通用故障处理](../troubleshoot) 专题章节提供了更多的故障方案。 

## 问题解答

#### Oracle 支持多数据库吗？

支持

#### CDB 是什么？

CDB 是 Oracle 对数据库（PDB）的逻辑分组，多个数据库在逻辑上可以组合成一个 CDB。

#### Oracle 支持多个 CDB 吗？

有待研究

#### 表空间是什么？

表空间是对表的逻辑分组，多个表可以在逻辑上组合成一个表空间。 为了避免表空间中的表名冲突，Oracle 在表名上会带上用户，以杜绝冲突的可能性。  

#### Oracle 数据库有哪些可视化管理工具？

* EM：企业管理器，主要是监控作用
* Oracle SQL Developer：可以导入导出、编写 SQL 脚本等
* ORDS：是 Oracle Web 化的中间件，提供 API，PL/SQL 等能力，集成了 Oracle SQL Developer
* APEX：是基于 ORDS 的一个无代码开发平台