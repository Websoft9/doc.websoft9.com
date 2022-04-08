---
sidebar_position: 1
slug: /vtiger
tags:
  - VtigerCRM
  - CRM
  - 客户成功
---

# 快速入门

[Vtiger Community Edition](https://www.vtiger.com/open-source-crm/) 一套开源的客户关系管理系统(CRM)，它是基于 SugarCRM 开发的一个衍生版本。适合中小企业从业务、市场、销售、采购、库存、客服等全程跟踪客户，实现销售自动化，获取更多订单。  

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-gui-websoft9.png)

## 准备

部署 Websoft9 提供的 VtigerCRM 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 VtigerCRM 的 **[默认账号和密码](./setup/credentials)**  
4. 若想用域名访问  VtigerCRM **[域名五步设置](./dns#domain)** 过程


## VtigerCRM 初始化向导{#init}

### 详细步骤

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-install001-websoft9.png)

2. 系统进入环境检测步骤，通过后进入下一步
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-install002-websoft9.png)

3. 填写您的数据库参数（[查看数据库账号密码](./setup/credentials)）
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


> 需要了解更多 VtigerCRM 的使用，请参考官方文档：[Vtiger Help](https://www.vtiger.com/help/)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：


## VtigerCRM 使用入门

下面以 **VtigerCRM 构建企业CRM** 作为一个任务，帮助用户快速入门：


## VtigerCRM 常用操作

### 配置 SMTP{#smtp}

1. 在邮箱管理控制台获取 [SMTP](./automation/smtp) 相关参数
   
2. 打开VtigerCRM->设置按钮 > CRM Settings > Outgoing Server
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-smtp-websoft9.png)

3. 设置无误后，请点击“Send Test Email”进行测试以验证

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

## 参数{#parameter}

VtigerCRM 应用中包含 PHP, Nginx, Docker, MySQL, phpMyAdmin 等组件，可通过 **[通用参数表](./setup/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 VtigerCRM 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 VtigerCRM 本身的参数：

### 路径{#path}

VtigerCRM 目录:  */data/wwwroot/vtigercrm*   
VtigerCRM 升级路径： *http://URL/migrate*

### 端口{#port}

无特殊端口


### 版本{#version}

控制台查看

### 服务{#service}

```shell
sudo docker start | stop | restart | stats vtigercrm
```

### 命令行{#cli}

无

### API

[Server APIs](https://community.vtiger.com/help/vtigercrm/developers/server-apis.html)

