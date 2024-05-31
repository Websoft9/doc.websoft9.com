---
title: Drupal
slug: /drupal
tags:
  - CMS
  - 内容管理
  - 建站
---

import Meta from './_include/drupal.md';

<Meta name="meta" />

## 入门指南{#guide}

### 功能一览{#wizard}

Websoft9 控制台安装 Drupal 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

1. 默认首页
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-main-websoft9.png)

2. 登陆界面
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-install1-websoft9.png)

3. 后台
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-boardpage-websoft9.png)

### 设置多语言{#setlang}

Drupal 支持多语言，下面是安装并设置多语言的主要步骤：

1. 登录 Drupal，在后台 【管理】>【配置】>【地区和语言】中安装语言
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-addlanguage-websoft9.png)

2. 安装新语言后，根据实际需要，设置默认语言

### 安装扩展{#plugin}

Drupal 提供的 [Drupal Modules](https://www.drupal.org/project/project_module)包含大量的扩展，下面介绍如何安装它们

1. 打开 [Drupal Modules](https://www.drupal.org/project/project_module)网站，搜寻所需的扩展
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-searchformodule-websoft9.png)

2. 获取扩展的下载地址
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-dlmodule-websoft9.png)

3. 登录 Drupal 后台，打开安装扩展的界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-extend-websoft9.png)

4. 通过输入下载地址，在线安装扩展
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-installsmtp-websoft9.png)

5. 安装完成
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-moduleinstalled-websoft9.png)

6. 最后，需要到模块管理中启用刚安装的插件
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-enablemodule-websoft9.png)

### 安装主题{#theme}

Drupal 提供的 [Drupal Themes](https://www.drupal.org/project/project_theme) 包含大量的主题，下面介绍如何安装它们

1. 打开 [Drupal Themes](https://www.drupal.org/project/project_theme) 网站，搜寻所需的主题
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-searchthemes-websoft9.png)

2. 获取主题的下载地址
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-themesurl-websoft9.png)

3. 打开 【扩展管理】>【安装扩展】，输入下载地址，开始安装
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-installsmtp-websoft9.png)

4. 安装后，打开【外观】，找到已经在线安装的主题，启用它
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-themeenable-websoft9.png)

> 有些模板提供商，提供的模板压缩包中包含 Drupal 内核文件，这种情况下 **安装模板=安装Drupal**

## 配置选项{#configs}

- 配置文件：/path/sites/default/settings.php
- 多语言（✅）
- SMTP（✅）：安装[SMTP Authentication Support](https://www.drupal.org/project/smtp) 插件实现 SMTP
- [第三方 CLI](https://drupalconsole.com/) 
- [APIs](https://www.drupal.org/docs/drupal-apis)

## 管理维护{#administrator}

### 重置管理员密码{#resetpw}

参考：[官方重置密码](https://www.drupal.org/node/44164) 

### 更换 URL{#url}

更换域名后，修改 Drupal 根目录下 `.htaccess` 中域名有关的值

### 在线备份

通过安装 Drupal 扩展，可以实现后台在线备份：

1. 下载 [Backup and Migrate](https://www.drupal.org/project/backup_migrate)

2. 登录 Drupal 后台，通过上传压缩文件的方式安装 **Backup and Migrate** ，启用之

3. 打开：【管理】>【配置】，打开【Backup and Migrate】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-backupnow-websoft9.png)

4. 开始设置备份策略

5. 通过 **Backup and Migrate** 实现的备份可以在线恢复

### 基于 Composer 升级

- [Updating Drupal core via Composer](https://www.drupal.org/docs/updating-drupal/updating-drupal-core-via-composer#update-instructions)
- [Drupal Upgrade](https://www.drupal.org/docs/updating-drupal)



## 故障

#### 初始化 【安装翻译】时总是报错？

问题原因：安装翻译过程中需要从网络上下载翻译文件，可能会有网络超时导致错误  
解决方案：重试多次，直至成功

#### Drupal 状态报告有错误？（图）

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-status-websoft9.png)

请根据提示完成系统升级或设置，不过这个设置不是必须的，此“错误”称之为“警告”更为合适

#### Protecting against HTTP ...？

现象描述：Drupal8.x 版本以上，安装完后提示 Protecting against HTTP HOST Header attacks。  

解决方法：进入 Drupal 目录下的 settings.php 文件插入下面的代码：

```
$settings['trusted_host_patterns']=['^www\.webosft9\.com$'];
```

#### 安装完成后仍提示安全漏洞？

参阅：[Trusted Host settings](https://www.drupal.org/node/1992030)