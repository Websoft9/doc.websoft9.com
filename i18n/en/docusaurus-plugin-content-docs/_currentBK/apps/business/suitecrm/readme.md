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

1. Using local Chrome or Firefox to visit *http://domain* or *http://Internet IP*, you will enter login page
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-init1-websoft9.png)

2. According to the wizard prompt, select [Next] to initialize the settings
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-init2-websoft9.png)

3. The initialization setting is completed, and start to experience the background
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-init3-websoft9.png)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## SuiteCRM QuickStart

The following uses **SuiteCRM to build an enterprise CRM** as a task to help users get started quickly:

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


## SuiteCRM reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage SuiteCRM 

By running `docker ps`, you can view all Containers when SuiteCRM is running:

```bash
CONTAINER ID   IMAGE                         COMMAND                  CREATED          STATUS                 PORTS                                                                               NAMES
f705c84dd8d1   bitnami/suitecrm:latest       "/opt/bitnami/script…"   27 seconds ago   Up 26 seconds          8443/tcp, 0.0.0.0:9002->8080/tcp, :::9002->8080/tcp                                 suitecrm
5d2d02d4c02e   mariadb:10.6                  "docker-entrypoint.s…"   29 seconds ago   Up 26 seconds          0.0.0.0:3306->3306/tcp, :::3306->3306/tcp                                           suitecrm-db
````

### Path{#path}

SuiteCRM installation directory: */data/apps/suitecrm*  
SuiteCRM Site Directory: */data/apps/suitecrm/data/suitecrm*  

### Port{#port}

No special port

### Version{#version}

```
docker exec -i suitecrm cat /bitnami/suitecrm/VERSION
```

### Service{#service}

```shell
sudo docker start | stop | restart | stats suitecrm
```

### CLI{#cli}

No

### API

[API Versions](https://docs.suitecrm.com/developer/api/)

