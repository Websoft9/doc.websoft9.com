---
sidebar_position: 3
slug: /fastpanel/admin
tags:
  - 故障
  - 路径
---


# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup) 相关章节。

## 场景

### FASTPANEL 备份

详情参考官方备份文档：[Creating backup plans](https://fastpanel.direct/wiki/en/creating-backup-plans-by-the-example-of-using-dropbox)

### FASTPANEL 升级

默认情况下，FASTPANEL 根据 Cron 调度程序设置的调度自动更新。您无需执行任何其他操作即可更新面板。
如果由于某种原因需要强制更新，请通过 SSH 执行以下控制台命令：
```
/usr/local/fastpanel2/app/updater
```

## 故障排除{#troubleshoot}

除以下列出的 FASTPANEL 故障问题之外， [通用故障处理](../troubleshoot) 专题章节提供了更多的故障方案。  

#### 进入初始化页面时，页面报警：面临潜在的安全风险？

这是因为没有申请Https证书提示的安全警告，请点击【接受风险并继续】继续操作即可。

## 问题解答{#faq}

#### FASTPANEL 支持多语言吗？

支持多语言（包含中文），通过控制台即可修改语言

