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

### Oracle 备份与恢复

### Oracle 升级

## 故障排除{#troubleshoot}

除以下列出的 Oracle 故障问题之外， [通用故障处理](../troubleshoot) 专题章节提供了更多的故障方案。  

#### 更改域名导致无法访问 Oracle ？

#### 访问 Oracle 出现 502 错误？{#502}


## 问题解答{#faq}

#### Oracle 支持多语言吗？

支持多语言（包含中文），通过控制台即可修改语言

#### Oracle 支持多个数据库吗？

从 12c 之后，Oracle 开始支持多个数据库。（通过 CDB 技术实现）

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


