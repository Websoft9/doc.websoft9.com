---
sidebar_position: 3
slug: /zentao/admin
tags:
  - ZenTao（禅道）
  - 项目管理
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../installation/setup/) 相关章节。

## 场景

### 在线备份与恢复

ZenTao 后台提供了非常简单实用的在线备份功能，使用方法如下：

1. 登录 ZenTao 后台，打开：【管理】>【数据】，进入备份页面，设置备份策略。
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-backupstr-websoft9.png)

2. 点击备份操作
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-backup-websoft9.png)

3. 在线实现的备份可以在线恢复（还原）

4. ZenTao 提供的回收站功能，也可以恢复手工删除的数据
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-recycle-websoft9.png)

### 手工升级

ZenTao 通过手工上传代码的方式进行升级。在升级之前请做好服务器的快照备份，这个是必须的步骤，因为谁都无法保证升级 100% 成功。

1. [下载](https://www.zentao.net/download.html)最新源码，解压
2. 上传并覆盖服务器上的 ZenTao 源码
3. 本地浏览器访问: _http://服务器公网 IP/upgrade.php_ 开始升级
4. 如果升级过程报错" Uncaught Error: Call to a member function query() on null in li..."，请给 `zentao/www` 和 `zentao/tmp` 目录递归加下 777 权限后再试

> 更多升级详情，请参考官方升级文档 [ZenTao 通过源代码方式升级(通用)](https://www.zentao.net/book/zentaopmshelp/67.html)

## 故障速查

除以下列出的 Zentao 故障问题之外，[通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案：

#### 密码输入错误多次被锁，怎么解决？

1. 10 分钟后会自动解锁。
2. 管理员登录，组织 → 用户 操作栏里有解锁按钮。

## 常见问题

#### ZenTao 支持多语言吗？

支持中英文

#### ZenTao 开源版是免费的吗？

基于 ZPL 协议发布，源代码开放，不限商用。当然您也可以购买官方的[企业版、集团办](https://www.zentao.net/page/professional.html)等

#### 为什么要注册 ZenTao 官网账号？

[注册](https://www.zentao.net/user-register.html)官网账号，你可以将 ZenTao 系统与官网连接，在线安装插件。

#### ZenTao 提供客户端吗？

禅道手机客户端 IOS 版本和安卓版本， 专为禅道专业版和企业版用户提供。