---
sidebar_position: 3
slug: /parseserver/admin
tags:
  - Node
  - 平台即服务
  - Serverless
---



# 维护参考

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