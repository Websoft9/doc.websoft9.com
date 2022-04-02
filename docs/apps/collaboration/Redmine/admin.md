---
sidebar_position: 3
slug: /redmine/admin
tags:
  - Redmine
  - 项目管理
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../installation/setup/) 相关章节。

## 场景

### 备份与恢复

相关备份方案，参考官方文档：[《RedmineBackupRestore》](https://redmine.org/projects/redmine/wiki/RedmineBackupRestore)

### 升级

Redmine 采用 Docker 部署，其升级流程：拉取镜像 > 删除容器 > 重建容器

> Redmine 升级之前请完成服务器的快照备份，以防不测。

1. 使用 SSH 登录服务，进入到 redmine 目录后，拉取最新版本镜像
   ```
   cd /data/wwwroot/redmine
   docker-compose pull
   ```
   > 系统会自动拉取最新版镜像，如果没有镜像可拉取，则无需更新

2. 停止并删除当前的 Redmine 容器

   ```
   docker-compose down -v
   ```

3. 重新创建 Redmine 容器
   ```
   docker-compose up -d
   

## 故障速查

#### Redmine 无法启动？

数据库服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看日志
docker logs redmine
```

#### 新建工程，名称为中文的时候，系统报错？

数据库字符编码导致，需修改数据库字符编码为 utf8

## 常见问题

#### Redmine 支持多语言？

支持英文、中文等多种语言

#### Redmine 支持哪些SCM？

SVN, CVS, Git, Mercurial and Bazaar

#### Redmine有企业版吗？

官方没有提供企业版

#### Redmine 支持哪些数据库？

支持 MySQL, PostgreSQL, SQlite, SQL Server 等多种数据库，本部署方案采用 MySQL 作为数据库。

#### 是否有可视化的数据库管理工具？

已经安装 PHPMyAdmin 作为数据库管理工具

#### 如何禁止 phpMyAdmin 访问？

在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:9090** 端口是否开启，开启代表可以访问，反之则不可访问

#### 是否可以修改Redmine的源码路径？

不建议修改
