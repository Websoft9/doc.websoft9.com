---
sidebar_position: 3
slug: /canvas/admin
tags:
  - Canvas
  - 在线学习管理
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup) 相关章节。

## 场景

### 升级

Canvas升级有点小复杂，详情参考官方升级文档：[Upgrading Canvas](https://github.com/instructure/canvas-lms/wiki/Upgrading)

## 故障排除

#### 如何查看错误日志？

通过如下两种日志检索关键词 **Failed** 或者 **error** 查看错误

* Canvas 日志：`/data/wwwroot/canvas/log/production.log`
* Apache 日志：`/data/logs/apache`

#### 403 访问权限错误？

需要确保 Canvas 根目录具有 canvas 和 www-data 两个用户的权限

#### 文件上传，不能下载

现象描述：文件上传后，下载出现"无法访问网站 找不到canvas.example.com服务器IP地址 "
解决办法：

1. 找到 [Apache 虚拟主机配置文件](../administrator/parameter)，将 ServerName 值修改为实际域名
2. 找到 [Canvas 域名配置文件](../canvas#path)，将 production 配置节点的 **domain** 值修改为实际域名


## 问题解答

#### Canvas 开源版是否提供移动端？

支持手机浏览器、Android 和 IOS 移动端。 详情参考：[mobile-guide](https://community.canvaslms.com/community/answers/guides/mobile-guide)

#### Canvas 支持中文吗

支持包括中文、英文等二十多种语言

#### Canvas 怎么安装插件？

参考: [安装插件](../canvas#plugin)

#### 快速重置 Canvas 管理员密码？

Canvas 官方没有提供方案。

#### Canvas 云版本与 OpenSource 区别？

有。具体参考 [code differences between the open source and hosted offerings](https://github.com/instructure/canvas-lms/wiki/FAQ#does-canvas-support-any-extensions)

#### Canvas 根目录需 canvas 和 apache 权限？

是的。拥有者是 canvas，同时通过 setfacl 额外给 www-data 赋予权限

```
setfacl -m u:www-data:rx -R /data/wwwroot/canvas
```
#### 推荐一个国内学习 Canvas 的网站？

小编认为[上海交通大学教育技术中心](https://v.sjtu.edu.cn/guide/)还不错
