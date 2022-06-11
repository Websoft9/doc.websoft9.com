---
sidebar_position: 3
slug: /parseserver/admin
tags:
  - Pars Server
  - PaaS
  - Serverless
---

# Parse Server Maintenance

This chapter is special guide for Parse Server maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### Backup and Restore 

### Parse Server Upgrade

Parse Server uses NPM to manage upgrades

```
npm update -g  parse-server
```

### Parse Dashboard Upgrade

Parse Dashboard uses NPM to manage upgrades

```
npm update -g  parse-dashboard
```

## Troubleshoot{#troubleshoot}

In addition to the Parse Server issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.

## FAQ{#faq}

#### What the different between Parse and Parse Server?

Parse is a Serverless Paas which was stop opretion now. Parse Server is opensoure project to replace Parse and you can deploy it on your Cloud Server

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

#### What SDKs does Parse Server provide?

IOS, Android, JavaScript, .NET + Xamarin, PHP, Arduino, Embedded C, etc. 

#### Where is the database connection configuration of Parse Dashboard?

Parse Dashboard not need Database, its use text file for data storage

#### If there is no Domain name, can I deploy Parse Server?

No, you should bind Domain name fist