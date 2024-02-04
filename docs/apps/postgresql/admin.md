---
sidebar_position: 3
slug: /postgresql/admin
tags:
  - PostgreSQL
  - Cloud Native Database
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup) 相关章节。

## 场景


## 故障排除{#troubleshoot}

除以下列出的 PostgreSQL 故障问题之外， [通用故障处理](../troubleshoot) 专题章节提供了更多的故障方案。 



## 常见问题

#### 什么是 PostgreSQL 的 Client 和 Server？

PostgreSQL Server 是指 PostgreSQL 程序本体，而 PostgreSQL Client 指采用TCP协议用于连接程序本地的客户端工具。  

它们是两个完全不同的程序，也就是说它们并需要同时安装到同一台服务上。

#### PostgreSQL 有默认数据库吗？

有，名称为 postgres



#### pgAdmin 支持多语言吗？

支持数十种语言（包含中文）

#### pgAdmin 是什么类型的客户端？

pgAdmin 是通过浏览器访问的客户端，即使在 Windows 下安装，也是间接调用浏览器来访问的