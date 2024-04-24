---
sidebar_position: 3
slug: /redmine/admin
tags:
  - Redmine
  - 项目管理
---

# Redmine Maintenance

This chapter is special guide for Redmine maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### Redmine Backup and Restore

Refer to the official documentation：[《RedmineBackupRestore》](https://redmine.org/projects/redmine/wiki/RedmineBackupRestore)

## Troubleshoot{#troubleshoot}

In addition to the Redmine issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### 新建工程，名称为中文的时候，系统报错？

数据库字符编码导致，需修改数据库字符编码为 utf8

## FAQ{#faq}

#### Redmine support multi-language?

Yes, you can use English,Chinese and more languages very easy

#### What SCMs does Redmine support?

SVN, CVS, Git, Mercurial and Bazaar

#### Does Redmine have an Enterprise Edition?

The official version is not available

#### What databases does Redmine support?

MySQL, PostgreSQL, SQlite, SQL Server