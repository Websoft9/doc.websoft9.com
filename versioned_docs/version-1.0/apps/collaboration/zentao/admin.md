---
sidebar_position: 3
slug: /zentao/admin
tags:
  - ZenTao（禅道）
  - 项目管理
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup) 相关章节。

## 场景

### ZenTao 备份与恢复

ZenTao 后台提供了非常简单实用的在线备份功能，使用方法如下：

1. 登录 ZenTao 后台，打开：【管理】>【数据】，进入备份页面，设置备份策略。
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-backupstr-websoft9.png)

2. 点击备份操作
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-backup-websoft9.png)

3. 在线实现的备份可以在线恢复（还原）

4. ZenTao 提供的回收站功能，也可以恢复手工删除的数据
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-recycle-websoft9.png)

### ZenTao 升级

请参考官方升级文档 [ZenTao 升级](https://www.zentao.net/book/zentaopmshelp/67.html)

## 故障排除{#troubleshoot}

除以下列出的 Zentao 故障问题之外，[通用故障处理](../troubleshoot) 专题章节提供了更多的故障方案：

#### 密码输入错误多次被锁，怎么解决？

1. 10 分钟后会自动解锁。
2. 管理员登录，组织 → 用户 操作栏里有解锁按钮。

## 问题解答{#faq}

#### ZenTao 支持多语言吗？

支持中英文

#### ZenTao 开源版是免费的吗？

基于 ZPL 协议发布，源代码开放，不限商用。当然您也可以购买官方的[企业版、集团办](https://www.zentao.net/page/professional.html)等

#### 为什么要注册 ZenTao 官网账号？

[注册](https://www.zentao.net/user-register.html)官网账号，你可以将 ZenTao 系统与官网连接，在线安装插件。

#### ZenTao 提供客户端吗？

禅道手机客户端 IOS 版本和安卓版本， 专为禅道专业版和企业版用户提供。