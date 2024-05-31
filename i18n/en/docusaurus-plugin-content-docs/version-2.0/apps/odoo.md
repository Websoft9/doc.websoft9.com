---
title: Odoo
slug: /odoo
tags:
  - ERP
  - 企业管理
  - 财务
  - SAP 替代品
  - CRM
  - 建站
  - 产品管理
  - MRP
  - HR
  - 设备管理
---

import Meta from './_include/odoo.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 Odoo 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。 

#### 安装向导

1. 使用本地浏览器后，进入初始化页面
   ![Odoo 社区版初始化页面](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-startcreatedb-websoft9.png)

2. 填写好所有参数，点击【create database】按钮，开始初始化安装。
   > 其中 Email 和 Password 是登录账号密码，务必牢记之

3. 初始化安装完成后，登录后台，安装所需的 APP
  ![Odoo APPS](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-consoleui-websoft9.png)

#### 试用企业版

Websoft9 是 Odoo 企业版的合作伙伴。如果想使用企业版，请[联系我们](./helpdesk#contact)获取使用授权。然后：

1. 完成初始化后，提示一旦安装第一个应用之后，系统就会提示要求注册订阅号（You will be able to register your database once you have installed your first app.）
  ![Odoo 注册提示](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-registersb000-websoft9.png)

2. 系统提示 **Register your subscription or buy a subscription**，请输入试用码
  ![Odoo 注册提示](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-registersb001-websoft9.png)

3. 开始试用企业版  
  ![Odoo 注册提示](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-registersb002-websoft9.png)

> 免费试用期结束之后，数据库会被被清空。请提前了解 [Odoo 订阅](https://www.odoo.com/zh_CN/pricing)。需折扣可以直接[联系我们](./helpdesk#contact)。

### 数据库管理器{#dbadmin}

Odoo 自带一个数据库管理器，参考：  

1. 在 Odoo 登录界面点击【Manage Database】链接    
![Odoo manage database](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-loginpage-websoft9.png)

2. 点击【set a master password】给数据库设置一个主密码保护数据库（非常重要）  
![Odoo set a password](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-setmasterpw-websoft9.png)

3. 设置密码  
![Odoo set a password](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-setapw-websoft9.png)

4. 选择操作项，管理数据库  
![Odoo set a password](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-manages-websoft9.png)

#### 新增

Odoo 支持多租户（多企业组织），增加一个数据库就等于增加一个企业。  

多个企业共同使用一套 Odoo，采用不同的账号登录，相互不干扰。

1. 点击【create database】，输入密码，设置名称
   ![Odoo 新增数据库](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-multidb-websoft9.png)

2. 新增完成后，你会看到数据库管理界面列出新增的数据库

#### 备份

1. 输入密码，选择备份格式，点击【Backup】
   ![Odoo 备份](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-managesbk-websoft9.png)

2. 备份完成后，系统会自动下载备份数据（zip文件）

#### 复制

可以完整复制一个企业组织，作为新企业组织的数据

1. 输入密码，设置名称，点击【Continue】
![Odoo set a pssword](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-managesdp-websoft9.png)

2. 复制成功后，数据库管理栏目会列出新复制的数据库

#### 删除

请谨慎操作

#### 恢复

数据库被删除后，可以通过备份进行恢复

1. 输入密码，选择备份文件，命名恢复后的数据库名称，点击【Continue】
![Odoo set a pssword](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-managesrs-websoft9.png)

1. 数据库恢复过程中可能会出现"413 Request Entity Too Large"，[解决办法](./odoo/admin#attachment)

#### 修改主密码

修改主密码是一项非常重要的安全操作。

### 管理 Odoo

本章列出使用 Odoo 过程中最常见的一些配置

#### 基础设置

Odoo 后台提供了设置界面，参考：

1. 登录 Odoo 后，打开点击左上角的设置图标，打开【Settings】项
   ![Odoo设置界面](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-settingspanel-websoft9.png)
2. 接下来可以进行：安装apps，设置语言，增加用户，企业初始化等操作

#### 设置企业 Logo

![Odoo 设置logo](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-settingslogo-websoft9.png)

#### 增加语言{#setlang}

1. 通过【Settings】控制台增加一个语言
  ![Odoo 增加语言](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-settingslangs-websoft9.png)
2. 转到【Administrator】>【Prefrences】  
  ![Odoo 用户管理](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-pref-websoft9.png)
3. 给用户设置语言
  ![Odoo 设置语言](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-language002-websoft9.png)

#### 开发者模式{#dev-mode}

Odoo 默认是管理者模式，如果需要深度设置，请先开启开发者模式

1. 登录 Odoo 后，打开点击左上角的设置图标，打开【Settings】项
2. 在 Settings 界面的右下点击【Active the developer mode】
   ![Odoo 开发者模式](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-enabledev-websoft9.png)
3. 在开发者模式下，Settings 控制台的功能更多了

#### Apps 市场

Odoo除了基础模块之外，通过[Odoo Apps 市场](https://www.odoo.com/apps/modules)提供了大量优质的第三方模块。通过使用第三方模块，用户可以快速找到所需的功能，以免费或极小的代价满足需求，快速上线业务，这是Odoo开源生态的带给用户的巨大价值，商业ERP在这方面是无法取代的。

#### 导出 PDF 文件

安装 Invoice, Purchase 等模块可以测试 print to PDF 功能

  ![Odoo 打印PDF](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-printtopdf-websoft9.png)

## 配置选项{#configs}

- 多语言（✅）
- 应用场景：ERP, 采购，库存，财务，营销，CRM，生产，人事，服务支持、电子商务、建站
- Odoo 配置文件： */path/data/odoo_config/odoo.conf*  
- [Command-line interface: odoo-bin](https://www.odoo.com/documentation/16.0/reference/cmdline.html)
- [API](https://www.odoo.com/documentation/14.0/developer/misc/api/odoo.html)
- 社区版在线升级到企业版（✅）

## 管理维护{#administrator}

### 配置 SMTP{#smtp}

Odoo 的 SMTP 需通过安装 **Discuss** 模块来实现：
   
1. 登录 Odoo 控制台，安装 SMTP 所需的 **Discuss** 模块
   ![Odoo SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-discussmodule-websoft9.png)

2. 通过：【Settings】>【General Settings】>【Discuss】开始配置邮箱
   ![Odoo SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-gsetmail-websoft9.png)

3. 填写 SMTP 参数
   ![Odoo SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-smtps-websoft9.png)

   Odoo 15
   ![Odoo SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-smtp-websoft9.png)

5. 点击【Test Connection】

### 开启 PostgreSQL 远程连接

Odoo 默认安装的 PostgreSQL 并不会启用数据库账号，官方解决方案：https://www.odoo.com/documentation/13.0/setup/deploy.html#postgresql

### 在线升级

Odoo 后台提供了 [Odoo Update](https://www.odoo.com/documentation/master/setup/update.html) 能力，让升级工作变得非常简单。参考下面的步骤完成升级：

1. 登录 Odoo 后台，[启动开发者模式](../odoo#dev-mode)
2. 通过 【Settings】>【Updates】开始更新 Odoo 主程序
   ![Odoo升级提示](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-upgradesui-websoft9.png)
3. 升级成功会有 “Well done...” 的提示
4. 点击 【Update Apps list】，开始更新 Odoo 模块


## 故障

#### 安装了 Demo 数据，想删除它?

官方并没有提供 Demo data 的删除工具，建议直接删除数据库，然后再新增（此时不再勾选 Demo data）

#### 如何查看 Odoo 错误日志？

最简单的方式是通过 SSH 连接服务器，运行`odoo`这个命令，就会显示错误日志以及 Odoo 的运行情况

#### 恢复数据库、上传附件等操作，出现 “413 Request Entity Too Large” 错误？{#attachment}

这是由于 Nginx 默认安装下，上传文件最大为 1M，因此需要修改 Nginx 这个限制：
1. 使用 WinSCP 远程连接服务器
2. 编辑 [Nginx 虚拟机主机配置文件](../nginx#virtualHosx)
3. 插入一行 `client_max_body_size 0;` 解除上传文件限制的配置项
   ```
   server {
    listen 80;
    server_name _;
    client_max_body_size 0; #解除上传文件限制
    ...
   ```
4. 保存并[重启 Nginx 服务](../administrator/parameter#service)

#### 总出现数据库设置提醒？

  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/odoo/odoo-setpasswodrem-websoft9.png)

这个提醒的是要求你尽快给数据库设置一个高强度的管理员密码，如果不设置将面临很大的风险。一旦设置后，此界面就不会再弹出了

#### PDF 无法打印中文

Odoo11 之前的版本，在使用 Odoo 打印功能时，下载的PDF文件只有英文，没有中文，导致打印不完整。

**问题原因**：系统环境里没有下载所需的中文字体

**解决方案**：执行以下命令下载字体

  ~~~
  sudo apt-get install ttf-wqy-zenhei
  sudo apt-get install ttf-wqy-microhei
  ~~~

#### Command pg_dump not found？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/odoo/odoo-backuperror-websoft9.png)

现象：Odoo 备份数据时，报错：Command pg_dump not found  
原因：PostgreSQL 的备份命令没有找到
方案：需要进一步查看PostgreSQL安装问题，还是Odoo本身的问题

#### 数据库连接配置信息？

Odoo 采用 [Peer Authentication](https://www.postgresql.org/docs/16/auth-methods.html#AUTH-PEER) 方式连接 PostgreSQL，即以操作系统用户登录数据库，无需密码。

#### 控制台看不到更新提示？

此功能只能在开发者模式下使用，请确保你的 Odoo 控制台是否已经切换成[开发者管理模式](./odoo#dev-mode)

