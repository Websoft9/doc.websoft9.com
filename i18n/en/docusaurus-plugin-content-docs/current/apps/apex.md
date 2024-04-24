---
title: APEX
slug: /apex
tags:
  - 低代码
  - Oracle 数据库
  - 表格
---

import Meta from './_include/apex.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 APEX 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

1. 本地浏览器打开访问地址（Apex 安装和启动时间都比较长，可能会超过 10 分钟或以上），进入登录页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-init-websoft9.png)

2. 输入账号密码
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-chpwd-websoft9.png)  

3. 密码修改完成后，开始体验后台
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-index-websoft9.png)    

### 快速了解

APEX 支持多语言（包含中文），通过控制台即可修改语言。  

- [API](https://apex.oracle.com/api)

### 基于模板数据创建 APP

1. 完成初始化向导后，点击创建新的workspace
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-createwp-websoft9.png)

2. 输入工作区名，并创建新的schema
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-createschema-websoft9.png)

3. 输入工作区管理用户名、密码及邮件地址,点击下一步直至工作区创建成功
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-createuser-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-createdone-websoft9.png)

4. 注销退出，使用上步骤3设定的用户和密码登陆
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-exit-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-applogin-websoft9.png)

5. 根据模本数据创建一个APP应用
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-appcreate-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-appinstall-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-template-websoft9.png)

6. 运行创建的APP，开始体验
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-runapp-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-appok-websoft9.png)

  > 新建的工作区才是APEX应用APP的工作区，默认internal是管理工作区

### 导入csv 创建 APP

1. 点击创建APP，选择从一个文件创建APP
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-imp01-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-imp02-websoft9.png)

2. 选择csv数据文件并根据提示导入
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-imp03-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-imp04-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-imp05-websoft9.png)

3. 点击【App Builder】，新APP已经创建，登陆即可开始体验
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-imp06-websoft9.png)

## 配置选项{#configs}

- 多语言（✅）

## 管理维护{#administrator}

### APEX 导入与导出

APEX 可以在控制台非常方便的将工作区，应用 APP 导入导出进行备份

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-list-websoft9.png) 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-import-websoft9.png) 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-export-websoft9.png) 

## 故障