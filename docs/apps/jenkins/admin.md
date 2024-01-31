---
sidebar_position: 3
slug: /jenkins/admin
tags:
  - Jenkins
  - DevOps
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup) 相关章节。

## 场景

### Jenkins 备份与恢复

[Backup plugin](https://plugins.jenkins.io/backup/) 提供对 Jenkins 的备份和恢复功能。  

### Jenkins 升级

Jenkins 内置升级功能，操作简单：

1. 登陆Jenkins后台，如果当前版本不是最新的稳定版本，会在右上角警告栏出现提示
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-warning-websoft9.png)

2. 点击警告，在弹出页面选择自动升级
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-selectauto-websoft9.png)

3. 在升级页面等待直到自动升级完成
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-autoupdate-websoft9.png)

4. 重启jenkins服务，Jenkins已经更新到最新稳定版  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-updatecok-websoft9.png)


## 故障排除

除以下列出的 Jenkins 故障问题之外， [通用故障处理](../troubleshoot) 专题章节提供了更多的故障方案。  

## 问题解答

#### Jenkins 是否支持中文？

支持，可以很方便的切换多语言（包括中文），Jenkins根据浏览器的语言显示文本，详情参照[Jenkins 语言设置](https://www.jenkins.io/doc/book/using/using-local-language/)。

#### 如何扩展 Jenkins 的功能？

[安装插件](../jenkins#installplugin)以扩展其功能。 
