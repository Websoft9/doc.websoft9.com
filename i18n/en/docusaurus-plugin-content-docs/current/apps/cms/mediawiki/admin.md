---
sidebar_position: 3
slug: /mediawiki/admin
tags:
  - Mediawiki
  - CMS
  - 知识管理
  - 博客系统
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup/) 相关章节。

## 场景

### MediaWiki 升级

升级请参考官方文档 [MediaWiki Upgrading](https://www.mediawiki.org/wiki/Manual:Upgrading/zh)

## 故障排除

除以下列出的 MediaWiki 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。 


## 问题解答

#### MediaWiki 支持多语言吗？

支持多语言（包含中文），后台可以[设置语言](../mediawiki#setlang)

#### MediaWiki 能上传多媒体文件吗？

可以，但需要提前[启用 MediaWiki 文件上传](../mediawiki#upload)功能