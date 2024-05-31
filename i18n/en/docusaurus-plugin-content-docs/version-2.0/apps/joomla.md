---
title: Joomla
slug: /joomla
tags:
  - CMS
  - 内容管理
  - 网站
  - 建站
---

import Meta from './_include/joomla.md';

<Meta name="meta" />

## 入门指南{#guide}

Websoft9 控制台安装 Joomla 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

### 扩展{#plugin}

Joomla 后台集成了 [Joomla! Extensions Directory™](https://extensions.joomla.org/) 大量的扩展，下面介绍如何安装它们

1. 登录 Joomla
2. 打开【扩展管理】>【安装扩展】，建议选择【从扩展目录安装】的方式在线寻找扩展
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-bkinstallext-websoft9.png)
3. 安装你所需的扩展

### 模板{#template}

Joomla 的模板安装，主要通过上传模板安装包的方式实现：

1. 准备好你的模板安装包（一般是 .zip 文件）

2. 登录 Joomla 后台

3. 打开 【扩展管理】>【安装扩展】，选择【上传安装包文件】的方式上传你的模板，开始安装
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-bkuploadext-websoft9.png)

4. 安装后，打开【扩展管理】>【模板管理】>【风格管理】，找到已经安装的模板，启用它
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-bkenabletemplate-websoft9.png)

> 有些模板提供商，提供的模板压缩包中包含 Joomla 内核文件，这种情况下 **安装模板=安装Joomla**

## 配置选项{#configs}

- SMTP（✅）：后台【系统管理】>【全局设置】>【服务器设置】，服务器邮件类型选择：SMTP
- 多语言（✅）：后台【扩展管理】>【语言管理】中安装语言，然后可选择所需的语言
- 组件多语言（✅）
- 缓存：后台【系统设置】>【清理过期缓存】
- 配置文件：/path/configuration.php
- [Joomla API](https://api.joomla.org/)

## 管理维护{#administrator}

### 在线备份

通过安装 Joomla 扩展，可以实现后台在线备份：

1. 下载 [Akeeda](https://www.akeebabackup.com/download.html)

2. 登录 Joomla 后台，通过上传压缩文件的方式安装 **Akeeda** 

3. 打开：【Dashboard】>【System】>【Control Panel】，找到【Backup is up-to-date】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-backup-websoft9.png)

4. 开始设置备份策略

5. 通过 Akeeda 实现的备份可以在线恢复
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-restore-websoft9.

### 在线升级

Joomla 提供了非常人性化的 [Joomla Upgrading](https://docs.joomla.org/Portal:Upgrading_Versions/zh-cn) 方案，根据系统的更新提示完成升级

1. 登录 Joomla 后台，如果有升级需求系统会显示升级提示
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-bkupgradets-websoft9.png)  

2. 根据提示进入升级中心，确认是否具备升级条件
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-update003-websoft9.png)

3. 升级中，请耐心等待
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-update004-websoft9.PNG)

4. 升级成功
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-update005-websoft9.PNG)

5. 扩展也可以在线升级
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-bkextupgrade-websoft9.png)


## 故障