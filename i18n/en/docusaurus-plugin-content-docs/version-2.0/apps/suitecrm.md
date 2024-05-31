---
title: SuiteCRM
slug: /suitecrm
tags:
  - 企业管理
  - CRM
---

import Meta from './_include/suitecrm.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 SuiteCRM 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

1. 本地浏览器访问，进入登陆页面
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-init1-websoft9.png)

2. 根据向导提示，选择【Next】初始化设置
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-init2-websoft9.png)

3. 初始化设置完成，开始体验后台
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-init3-websoft9.png)

### 快速了解

- [API Versions](https://docs.suitecrm.com/developer/api/)


## 管理维护{#administrator}

### 配置 SMTP{#smtp}

1. 打开SuiteCRM->Administartor->Admin->Email->Email Setting，打开邮件发送设置项（Outgoing Mail Configuration）

2. 设置无误后，请点击“Send Test Email”进行测试以验证

### 安装中文包

SuiteCRM默认安装只有英文，需要中文或其他语言，需要下载语言包，然后通过后台进行安装，以中文为例，具体如下：

1.  下载[中文语言包](https://crowdin.com/project/suitecrmtranslations/zh-CN) – 存到本地电脑上
2.  以Admin身份进入SuiteCRM，进入 “admin-Admin Tools-Module loader”
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-lmodule-websoft9.png)
3.  Upload file->Install it->Commit
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-linstall-websoft9.png)
4.  Go to “Admin” enter “Repair” and apply “Quick repair and rebuild” for languages
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-repair-websoft9.png)
5.  退出 SuiteCRM
6.  先选择所需的语言，再登录
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-logincn-websoft9.png)

### 备份与恢复

详细请参照[SuiteCRM 备份](https://docs.suitecrm.com/developer/best-practices/#_backup)

### 升级

详细请参照[SuiteCRM 升级策略](https://docs.suitecrm.com/8.x/admin/installation-guide/upgrading/)



## 故障

#### SuiteCRM 安装向导连接数据库步骤，点击【Next】没有任何反应？

**问题原因**：经过排查，发现【Next】动作有文件404（估计是Ajax触发），即有文件无法下载程序没有反应
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-noresponse-websoft9.png)

**解决方案**：临时购买一台香港地区的Windows服务器，在这个服务器打开浏览器安装SuiteCRM即可

#### 无法在 Studio 中编辑字段 ，报错：无法检索数据

问题描述：在SuiteCRM 8 中，通过 Admin → Studio → Accounts → Fields → 弹出错误 - 无法检索数据   
解决方案：用[下载源码文件](https://github.com/myfluxi/SuiteCRM-Core/blob/30e44d2fb786389236f98182d304dc0a7a00cb55/public/legacy/modules/ModuleBuilder/views/view.modulefields.php) 替换 SuiteCRM 目录中 public/legacy/modules/ModuleBuilder/views/view.modulefields.php 文件