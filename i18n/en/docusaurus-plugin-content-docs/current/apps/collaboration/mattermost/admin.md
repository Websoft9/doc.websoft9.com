---
sidebar_position: 3
slug: /mattermost/admin
tags:
  - Mattermost
  - 团队协作
  - 团队通讯
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup/) 相关章节。

## 场景

## 故障排除

除以下列出的 Mattermost 故障问题之外， [通用故障处理](../troubleshoot) 专题章节提供了更多的故障方案。 

## 问题解答

#### Mattermost 与 Slack 有什么区别？

阅读：[Mattermost vs Slack](https://mattermost.com/mattermost-vs-slack/)

#### Mattermost Server, Mattermost Team Edition, Matttermost Enterprise Edition?

Mattermost Server 是它的产品的服务器端（后端）  
[Mattermost Team Edition](https://docs.mattermost.com/developer/manifesto.html?highlight=mattermost%20team%20edition) 是它的开源版本    
Matttermost Enterprise Edition 是它的企业版本  

目前官方提供了一致性的软件包下载，安装后默认就是 Enterprise Edition 的程序，但用户界面只有开源版的功能，如果需要企业版的功能，需要通过导入企业版秘钥实现升级。

#### Mattermost 有移动客户端吗？

提供，[下载地址](https://mattermost.com/download/#mattermostApps)

#### Mattermost支持多语言吗？

支持，[参考设置](../mattermost#setlang)