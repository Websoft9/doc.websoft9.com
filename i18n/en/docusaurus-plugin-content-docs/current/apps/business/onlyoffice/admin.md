---
sidebar_position: 3
slug: /onlyoffice/admin
tags:
  - ONLYOFFICE Workspace
  - 企业管理
  - CRM
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup) 相关章节。

## 场景

## 故障排除

除以下列出的 ONLYOFFICE 故障问题之外， [通用故障处理](../troubleshoot) 专题章节提供了更多的故障方案。

#### ONLYOFFICE 显示502错误？

首先通过命令 `sudo docker logs onlyofficecommunityserver`，查看是否有错误日志。  

一般是由文件权限不足或数据连接问题导致。

#### 重装数据库导致 ONLYOFFICE 无法运行？

ONLYOFFICE 对数据库的配置有严格的要求，保证符合如下要求：

```
echo "[mysqld]
sql_mode = 'NO_ENGINE_SUBSTITUTION'
max_connections = 1000
max_allowed_packet = 1048576000
group_concat_max_len = 2048
log-error = /var/log/mysql/error.log" > /app/onlyoffice/mysql/conf.d/onlyoffice.cnf
```

## 问题解答

#### ONLYOFFICE 是否支持中文？

支持，可以在线切换多种语言

#### Community Edition vs Enterprise Edition？

参考官方说明 [Compare Community Edition and Enterprise Edition](https://github.com/ONLYOFFICE/CommunityServer#compare-community-edition-and-enterprise-edition)

#### 能否介绍 ONLYOFFICE 各种版本的关系？

OnlyOffice的产品家族比较复杂，根据官方的介绍，可以分为：

* ENTERPRISE EDITION：企业版
* COMMUNITY EDITION：开源版
* INTEGRATION EDITION：比如集成了 ownCloud 的版本
* DEVELOPER EDITION：开发者版本

其中每一个版本都是由：ONLYOFFICE WorkSpace, ONLYOFFICE docs 组成。  

COMMUNITY EDITION 是一个完全免费的版本。DEVELOPER EDITION 是适用于开发者的[收费版本](https://www.onlyoffice.com/zh/developer-edition-prices.aspx)。

#### ONLYOFFICE 开源版并发连接数有限制吗？

并发连接数不超过 20个（Up to 20 Simultaneous connections）

#### ONLYOFFICE Docs 并发连接数是什么？

参阅：[ONLYOFFCE Docs](../onlyofficedocs/admin#onlyofficedocsmaxconn) 相关文档

#### ONLYOFFICE 默认支持文档编辑与预览吗？

默认已经配置好，无需任何设置即可使用

#### 本应用是否可以对外提供文档服务？

可以，*http://服务器公网IP:9002* 即文档预览与编辑服务地址

