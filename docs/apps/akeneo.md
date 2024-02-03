---
title: Akeneo
slug: /akeneo
tags:
  - 产品主数据
  - pim
  - 电商
---

import Meta from './_include/akeneo.md';

<Meta name="meta" />

## 入门指南

### 连接 App Store {#Appstore}  

Akeneo 通过 App Store 通过扩展应用。连接到 App Store 需要2个步骤：  

1. 给用户授权管理App Store。依次点击：System - Users - Roles - Administrator - Permissions - System - Manager apps / Open apps  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/akeneo/akeneo-appmanager-websoft9.png)

2. 配置 AKENEO_PIM_URL ：修改 /data/apps/akeneo/data/akeneo/.env.local 文件，将 AKENEO_PIM_URL 值修改成服务器 IP 或域名，比如 AKENEO_PIM_URL=http://100.100.100.100 

### 设置多语言{#setlan}

Akeneo 完美支持多语言，下面以中文作为范例：  

1. 设置登陆页面为中文：点击 System - Configuration 进行设置  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/akeneo/akeneo-setlanguage01-websoft9.png)
   
2. 设置后台页面为中文：点击右上角个人头像进行设置  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/akeneo/akeneo-setlanguage02-websoft9.png)

## 管理维护

### 备份与恢复

参考：[Akeneo 备份管理](https://docs.akeneo.com/6.0/technical_architecture/technical_information/operation_processes.html#backup-management)

### 升级

参考：[Akeneo 升级](https://docs.akeneo.com/6.0/migrate_pim/upgrade_major_version.html#upgrade-from-5-0-to-6-0)

### 数据导入导出

参阅官方文档： [Import and Export data](https://docs.akeneo.com/6.0/import_and_export_data/index.html)

## 故障