---
title: Vtiger CRM
slug: /vtiger
tags:
  - CRM
  - 客户关系管理
  - 销售管理
---

import Meta from './_include/vtiger.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 VtigerCRM 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

1. 进入安装向导
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-install001-websoft9.png)

2. 系统进入环境检测步骤，通过后进入下一步
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-install002-websoft9.png)

3. 填写您的数据库参数（[查看数据库账号密码](./user/credentials)）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-install003-websoft9.png)

4. 数据库连接正确，点击“Next”进入下一步
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-install004-websoft9.png)

5. 选择一个匹配的行业，然后进入下一步
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-install005-websoft9.png)

6. 选择需要安装的模块，建议全部勾选上，然后进入下一步
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-install006-websoft9.png)

7. 系统提示选择货币、时区等
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-install007-websoft9.png)

8. 点击“Get Started”，进入后台，体验系统的完整功能
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-backend-websoft9.png)

### 安装中文包

VtigerCRM 支持多国语言，中文包安装方法如下：

1.  到官方 [MarketPlace](https://marketplace.vtiger.com/app/listings)-Language Pack 下载 Chinese 简体中文语言包

2.  导入语言包：通过主菜单【Setting – CRM Setting – Module Management – Modules 】进入模块管理界面，点击右上角 “Import Module from Zip”按钮，进入导入模块管理界面，选择语言包进行导入。

    > 注意：导入时请直接选择语言包进行导入，不要勾选“ I accept with disclaimer and would like to proceed”否则无法导入。

3.  启用新的语言：右上角点击你的登录用户名->My Preferences-> Edit，点击 Language 后面的下拉框选择语言，然后保存
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/change-language-websoft9.jpg)

### 连接 Marketplace

在 VtigerCRM 右上角点齿轮图标进入后台设置界面，左侧菜单栏点击 Extension Store 进入官方扩展应用市场。点击应用市场右上角的 Login to Marketplace 登录或者注册应用市场。搜索 Chinese 找到简体中文语言包进行安装。

注意：语言包也可以通过官方扩展应用市场安装。


## 管理维护{#administrator}

### 配置 SMTP{#smtp}

1. 打开 VtigerCRM 左上角主菜单 : Settings > CRM Settings > CONFIGURATION > Outgoing Server
   
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/vtigercrm/vtiger-smtp-websoft9.png)

2. 保存设置，能检测通过，表明 SMTP 配置成功。可以在 Mail Manager 功能中测试邮件发送。

**收件箱 配置**

通过左侧主菜单 Mail Manager ，进入 Configure Mailbox ，配置收件箱
   
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/vtigercrm/vtiger-imap-websoft9.png)

  ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/vtigercrm/vtiger-imap1-websoft9.png)


### 升级

VtigerCRM 自身提供了升级功能和[升级文档](http://community.vtiger.com/help/vtigercrm/administrators/migration.html)。

升级是将**升级包**覆盖到已有源码上进行升级。新版本 VtigerCRM 安装完成后再导入旧版本数据的升级方案是不可行的。

## 故障

#### 更换域名，VtigerCRM 无法访问？

错误信息：*Invalid compiled template for 'modules/Install/Header.tpl'*  
问题原因：VtigerCRM 启动后会生成一个记录访问地址的缓存文件    
解决方案：使用下面的命令删除缓存文件  

```
- rm -rf path/test/templates_c/v7
- rm -rf path/vtigercrm/cache/*
```