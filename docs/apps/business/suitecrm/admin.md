---
sidebar_position: 3
slug: /suitecrm/admin
tags:
  - SuiteCRM
  - 企业管理
  - CRM
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup) 相关章节。

## 场景

## 故障排除

除以下列出的 SuiteCRM 故障问题之外， [通用故障处理](../troubleshoot) 专题章节提供了更多的故障方案。

#### SuiteCRM 安装向导连接数据库步骤，点击【Next】没有任何反应？

**问题原因**：经过排查，发现【Next】动作有文件404（估计是Ajax触发），即有文件无法下载程序没有反应
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-noresponse-websoft9.png)

**解决方案**：临时购买一台香港地区的Windows服务器，在这个服务器打开浏览器安装SuiteCRM即可

#### 无法在 Studio 中编辑字段 ，报错：无法检索数据

在SuiteCRM 8 中，通过 Admin → Studio → Accounts → Fields → 弹出错误 - 无法检索数据，可以通过修复文件文件解决：
用下列文件替换SuiteCRM 目录中 public/legacy/modules/ModuleBuilder/views/view.modulefields.php 文件
https://github.com/myfluxi/SuiteCRM-Core/blob/30e44d2fb786389236f98182d304dc0a7a00cb55/public/legacy/modules/ModuleBuilder/views/view.modulefields.php

## 问题解答