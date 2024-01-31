---
sidebar_position: 3
slug: /drupal/admin
tags:
  - Drupal
  - CMS
  - 建站系统
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup) 相关章节。

## 场景

### 在线备份

通过安装 Drupal 扩展，可以实现后台在线备份：

1. 下载 [Backup and Migrate](https://www.drupal.org/project/backup_migrate)

2. 登录 Drupal 后台，通过上传压缩文件的方式安装 **Backup and Migrate** ，启用之

3. 打开：【管理】>【配置】，打开【Backup and Migrate】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-backupnow-websoft9.png)

4. 开始设置备份策略

5. 通过 **Backup and Migrate** 实现的备份可以在线恢复


### 基于 Composer 升级

Drupal 目前没有提供后台可视化升级，但可以通过命令行的方式升级。

> 在升级之前请做好服务器的快照备份，这个是必须的步骤，因为谁都无法保证升级 100% 成功。

1. 登录 Drupal 后台，如果有升级需求系统会显示升级提示
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-update-websoft9.png)  

2. 参考官方文档 [Updating Drupal core via Composer](https://www.drupal.org/docs/updating-drupal/updating-drupal-core-via-composer#update-instructions)，完成升级

> 更多升级详情，请参考官方升级文档 [Drupal Upgrade](https://www.drupal.org/docs/updating-drupal)


## 故障排除

#### 初始化 【安装翻译】时总是报错？

问题原因：安装翻译过程中需要从网络上下载翻译文件，可能会有网络超时导致错误  
解决方案：重试多次，直至成功

#### Drupal 状态报告有错误？（图）

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-status-websoft9.png)

请根据提示完成系统升级或设置，不过这个设置不是必须的，此“错误”称之为“警告”更为合适

#### Protecting against HTTP ... 错误？

现象描述：Drupal8.x 版本以上，安装完后提示 Protecting against HTTP HOST Header attacks。  

解决方法：进入 Drupal 目录下的 settings.php 文件插入下面的代码：

```
$settings['trusted_host_patterns']=['^www\.webosft9\.com$'];
```

#### Drupal 安装完成后仍提示安全漏洞？

参阅：[Trusted Host settings](https://www.drupal.org/node/1992030)

## 问题解答

#### Drupal 支持多语言吗？

支持多语言（包含中文），建议在初始化安装的时候安装多语言
