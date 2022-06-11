---
sidebar_position: 3
slug: /drupal/admin
tags:
  - Drupal
  - CMS
  - 建站系统
---

# Drupal Maintenance

This chapter is special guide for Drupal maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### Backup and Restore

This section provides Drupal online backup solution

1. Download module [Backup and Migrate](https://www.drupal.org/project/backup_migrate)

2. Log in Drupal console as administrator, install **Backup and Migrate** by uploading package

3. Go to【Manage】>【configuration】, open【Backup and Migrate】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-backupnow-websoft9.png)

4. Set your backup policy

5. You can also restore your data online by **Backup and Migrate**   

### Upgrade

Drupal don't have online Upgrade function, but Drupal have Upgrade solution by **CLI**

1. Log in Drupal, you can see the upgrade reminder if there have latest version of Drupal
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-update-websoft9.png)  

2. Refer to [Updating Drupal core via Composer](https://www.drupal.org/docs/updating-drupal/updating-drupal-core-via-composer#update-instructions) to start Upgrade

> More details about upgrade, please refer to [Drupal Upgrade](https://www.drupal.org/docs/updating-drupal)


## Troubleshoot{#troubleshoot}

In addition to the Drupal issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

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

Refer to [Trusted Host settings](https://www.drupal.org/node/1992030)

## FAQ{#faq}

#### Drupal support multi-language?

Yes
