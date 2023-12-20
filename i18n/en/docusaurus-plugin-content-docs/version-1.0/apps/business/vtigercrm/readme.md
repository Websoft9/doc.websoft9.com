---
sidebar_position: 1
slug: /vtiger
tags:
  - VtigerCRM
  - CRM
  - 客户成功
---

# VtigerCRM Getting Started

[Vtiger Community Edition](https://www.vtiger.com/open-source-crm/) is an opensource CRM system that helps you create and automate a better customer journey.Vtiger CRM enables sales, support, and marketing teams to organize and collaborate to measurably improve customer experiences and business outcomes. Vtiger CRM also includes email, inventory, project management, and other tools, providing a complete the business management suite.

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-gui-websoft9.png)

If you have installed Websoft9 VtigerCRM, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for VtigerCRM
4. [Get](./user/credentials) default username and password of VtigerCRM

## VtigerCRM Initialization

### Steps for you

1. Using local Chrome or Firefox to visit *http://domain* or *http://Internet IP*, you will enter the configuration interface of installation
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-install001-websoft9.png)

2. Environment check, go to next step
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-install002-websoft9.png)

3. Then configure the database connection information([Don't know password?](./user/credentials))
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-install003-websoft9.png)

4. Check the database connection, go to next step
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-install004-websoft9.png)

5. Select one industry for your VtigerCRM
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/vtigercrm/vg06.png)

6. Select the modules you want to installed
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-install006-websoft9.png)

7. Select the Currency, Time zone
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-install007-websoft9.png)

8. VtigerCRM dashboard
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-backend-websoft9.png)

> Refers to the [VtigerCRM Help](https://www.vtiger.com/help/) to get start your VtigerCRM tutorial

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## VtigerCRM QuickStart

下面以 **VtigerCRM 构建企业CRM** 作为一个任务，帮助用户快速入门：


## VtigerCRM Setup

### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console
   
2. Open the main menu on the left side of VtigerCRM: Settings > CRM Settings > CONFIGURATION > Outgoing Server
   
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/vtigercrm/vtiger-smtp-websoft9.png)

3. Save the settings, the test can pass, and the SMTP configuration is successful. Mail delivery can be tested in **Mail Manager**.

**Inbox Configuration**

From the main menu **Mail Manager** , click **Configure Mailbox** to configure the inbox
   
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/vtigercrm/vtiger-imap-websoft9.png)

  ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/vtigercrm/vtiger-imap1-websoft9.png)

### Set Chinese Language

VtigerCRM 支持多国语言，中文包安装方法如下：

1.  到官方 [MarketPlace](https://marketplace.vtiger.com/app/listings)-Language Pack 下载 Chinese 简体中文语言包

2.  导入语言包：通过主菜单【Setting – CRM Setting – Module Management – Modules 】进入模块管理界面，点击右上角 “Import Module from Zip”按钮，进入导入模块管理界面，选择语言包进行导入。

    > 注意：导入时请直接选择语言包进行导入，不要勾选“ I accept with disclaimer and would like to proceed”否则无法导入。

3.  启用新的语言：右上角点击你的登录用户名->My Preferences-> Edit，点击 Language 后面的下拉框选择语言，然后保存
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/change-language-websoft9.jpg)

### Install apps

在 VtigerCRM 右上角点齿轮图标进入后台设置界面，左侧菜单栏点击 Extension Store 进入官方扩展应用市场。点击应用市场右上角的 Login to Marketplace 登录或者注册应用市场。搜索 Chinese 找到简体中文语言包进行安装。

注意：语言包也可以通过官方扩展应用市场安装。

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage VtigerCRM 

通过运行`docker ps`，可以查看到 VtigerCRM 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 VtigerCRM 本身的参数：

### Path{#path}

VtigerCRM 目录:  */data/wwwroot/vtigercrm*   
VtigerCRM 升级路径： *http://URL/migrate*

### Port{#port}

无特殊端口


### Version{#version}

控制台查看

### Service{#service}

```shell
sudo docker start | stop | restart | stats vtigercrm
```

### CLI{#cli}

无

### API

[Server APIs](https://community.vtiger.com/help/vtigercrm/developers/server-apis.html)

