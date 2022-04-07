---
sidebar_position: 3
slug: /redmine/admin
tags:
  - Redmine
  - 项目管理
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup/) 相关章节。

## 场景

### 备份与恢复

相关备份方案，参考官方文档：[《RedmineBackupRestore》](https://redmine.org/projects/redmine/wiki/RedmineBackupRestore)

## 故障排除

除以下列出的 Redmine 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。 

#### 新建工程，名称为中文的时候，系统报错？

数据库字符编码导致，需修改数据库字符编码为 utf8

## 问题解答

#### Redmine 支持多语言？

支持英文、中文等多种语言

#### Redmine 支持哪些SCM？

SVN, CVS, Git, Mercurial and Bazaar

#### Redmine有企业版吗？

官方没有提供企业版

#### Redmine 支持哪些数据库？

支持 MySQL, PostgreSQL, SQlite, SQL Server 等多种数据库，本部署方案采用 MySQL 作为数据库。