---
sidebar_position: 3
slug: /parseserver/admin
tags:
  - Node
  - 平台即服务
  - Serverless
---



# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup) 相关章节。

## 场景

### Parse Server 升级

Parse Server 采用 NPM 来管理升级

```
npm update -g  parse-server
```

### Parse Dashboard 升级

Parse Dashboard 采用 NPM 来管理升级

```
npm update -g  parse-dashboard
```

## 故障处理

除以下列出的 Parse Server 故障问题之外， [通用故障处理](../troubleshoot) 专题章节提供了更多的故障方案。 

## 常见问题

#### Parse 与 Parse Server 有什么区别？

Parse是一个在线的 Serverless 托管平台，现已停止运营。Parse Server 是开源 Parse 的功能，由用户自行下载部署到服务器的开源项目。

#### Parse Server 有哪些功能？

它提供的基础功能包括:

- 用户的登录注册
- 用户身份的认证
- 数据存储 && 灵活查询
- 文件存储
- 实时查询
- 消息推送
- 缓存服务
- 与云平台很好的对接
- 自定义业务逻辑与Hook机制

#### Parse Server 提供了哪些SDK？

IOS, Android, JavaScript, .NET + Xamarin, PHP, Arduino, Embedded C等 

#### Parse Dashboard 如何存储数据？ 

Parse Dashboard 不需要数据库支持，数据存储在文本文件中

#### 没有域名是否可以部署 Parse Server ？

不可以，必须绑定域名