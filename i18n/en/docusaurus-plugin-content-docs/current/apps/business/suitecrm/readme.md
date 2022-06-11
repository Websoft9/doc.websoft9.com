---
sidebar_position: 1
slug: /suitecrm
tags:
  - SuiteCRM
  - 企业管理
  - CRM
---

# SuiteCRM Getting Started

[SuiteCRM](https://suitecrm.com/demo/) is a fork of SugarCRM Community Edition. Massively extended, SuiteCRM delivers Workflow, Reporting, Portal, Quotes, Products, Invoices, Accounts, Contacts, Opportunities, Projects, Responsive mobile theme, Email marketing campaigns, Knowledge Base, Outlook and Thunderbird integration, Contracts, Leads, Activities and much more.

![](http://libs.websoft9.com/Websoft9/DocsPicture/en/suitecrm/suitecrm-gui-websoft9.png)

If you have installed Websoft9 SuiteCRM, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for SuiteCRM
4. [Get](./user/credentials) default username and password of SuiteCRM

## SuiteCRM Initialization

### Steps for you

1. Using local Chrome or Firefox to visit *http://domain* or *http://Internet IP*, you will enter the configuration interface of installation

2. Agree license, go to next step
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/suitecrm/suitecrm-accept-websoft9.png)

3. Environment check
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/suitecrm/suitecrm-check-websoft9.png)

4. Then configure the database connection information([Don't know password?](./user/credentials) and set administrator account
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/suitecrm/suitecrm-installdb-websoft9.png)

   > Email is your system ID, not collected by anyone because it stored in your Cloud Server

5. Wait the installing  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/suitecrm/suitecrm-installing-websoft9.png)


6. Set your SMTP (Optional)
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-smtp-websoft9.png)

7. Install successfully, log in to SuiteCRM  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-login-websoft9.png)

8. SuiteCRM dashboard
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-backend-websoft9.png)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## SuiteCRM QuickStart

下面以 **SuiteCRM 构建企业CRM** 作为一个任务，帮助用户快速入门：

## SuiteCRM Setup

### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console
   
2. Go to SuiteCRM->Administartor->Admin->Email->Email Setting->Outgoing Mail Configuration
   
3. Fill in the correct SMTP Parameters
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-smtp-2-websoft9.png)
    - SMTP Mail Server
    - SMTP Port
    - Use SMTP Authentication
    - Enable SMTP over SSL or TLS
    - Use Name
    - Password
    - Allow users to use this account for...

4. After the settings are correct, please click "Send Test Email" to Test to verify

### Set Chinese Language

SuiteCRM support multi-language.Below is a example for adding Chinese language in SuiteCRM

1. [Find and Download](https://crowdin.com/project/suitecrmtranslations) the language package
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/suitecrm/suitecrm-dllanguge-websoft9.png)

2. Administrator->MODULE LOADER,upload the language package,then install it
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/suitecrm/suitecrm-uploadlanguage-websoft9.png)
3. Afer the intallation,you can receive the message “The language package is ready to be installed.”
4. go to Administrator->admin->system-Language,now you can see the new language item
5. Log out,and log in again,you can see the language selections upper one the account
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/suitecrm/suitecrm-languageitems-websoft9.png)


## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage SuiteCRM 

通过运行`docker ps`，可以查看到 SuiteCRM 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 SuiteCRM 本身的参数：

### Path{#path}

SuiteCRM 路径:  */data/wwwroot/suitecrm*  
SuiteCRM 配置文件: */data/wwwroot/suitecrm/config.php*

### Port{#port}

无特殊端口

### Version{#version}

控制台查看

### Service{#service}

```shell
sudo docker start | stop | restart | stats suitecrm
```

### CLI{#cli}

无

### API

[API Versions](https://docs.suitecrm.com/developer/api/)

