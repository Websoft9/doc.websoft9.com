---
title: EspoCRM
slug: /espocrm
tags:
  - CRM
  - 客户关系管理
  - 销售管理
  - 市场
  - 营销
  - 联系人
---

import Meta from './_include/espocrm.md';

<Meta name="meta" />

## 入门指南{#guide}

### 功能一览{#wizard}

Websoft9 控制台安装 EspoCRM 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

- 登录页面
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-login-websoft9.png)

- 后台
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-main-websoft9.png)


## 配置选项{#configs}

- 多语言（✅）：通过右上角设置入口 > Preferences 中设置
- 移动端（✅）
- SMTP（✅）
- 命令行：[Console Commands](https://docs.espocrm.com/administration/commands/)
- API：[EspoCRM REST API](https://docs.espocrm.com/development/api/)

## 管理维护{#administrator}

### 配置 SMTP{#smtp}

EspoCRM支持第三方的SMTP发送邮件模式，具体如下：

1. 在邮箱管理控制台获取 [SMTP](./administrator/smtp) 相关参数
   
2. 待EspoCRM安装完成后，点击右上角菜单->admin，点击【电子邮件账户】进行个人邮箱的添加或编辑
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-smtp-1-websoft9.png)

3. 根据下图的设置，进行收发邮件的设置，分别设置 IMAP/SMTP 参数

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-smtp-2-websoft9.png)

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-smtp-3-websoft9.png)

4. 设置完成后，请点击“Send Test Email”测试设置是否成功

## 故障