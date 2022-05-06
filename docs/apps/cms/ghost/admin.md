---
sidebar_position: 3
slug: /ghost/admin
tags:
  - Ghost
  - CMS
  - 建站系统
  - 博客系统
---
# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup/) 相关章节。

## 场景

## 故障排除

除以下列出的 Ghost 故障问题之外， [通用故障处理](../troubleshoot) 专题章节提供了更多的故障方案。 

#### 无法打开默认主题 casper 文件夹？

官方表示，casper 是内核的组成部分，仅自上传的主题方可修改。


## 问题解答

#### Ghost 支持中文吗？

Ghost 的后台不支持中文，但是前台支持中文（需主题中有中文）

#### Ghost 中的 Post 与 Page 有什么区别？

Post 是文章的意思，每一篇博客文章即一个 Post；Page 是页面的意思，网站中的首页，公司介绍等都可称之为 Page。  

在 Ghost 系统中，每一个新建的 Page，都需要在主题中有对应的模板文件与之匹配。

#### Ghost 有哪些用户角色？

参考官方文档 [Managing your team in Ghost](https://ghost.org/help/managing-your-team/)

#### Ghost 是否可修改默认主题 casper ？

不支持，只可以修改自上传的主题。
