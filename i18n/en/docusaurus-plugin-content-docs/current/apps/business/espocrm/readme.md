---
sidebar_position: 1
slug: /espocrm
tags:
  - EspoCRM
  - CRM
  - 客户成功
---

# EspoCRM Getting Started

[EspoCRM](https://demo.espocrm.com/) is an Open Source CRM (Customer Relationship Management) software that allows you to see, enter and evaluate all your company relationships regardless of the type. People, companies or opportunities – all in an easy and intuitive interface.It’s a web application with a frontend designed as a single page application based on backbone.js and a REST API backend written in PHP.

![](http://libs.websoft9.com/Websoft9/DocsPicture/en/espocrm/espocrm-gui-websoft9.jpg)

If you have installed Websoft9 EspoCRM, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for EspoCRM
4. [Get](./user/credentials) default username and password of EspoCRM

## EspoCRM Initialization

### Steps for you

1. Using local Chrome or Firefox to visit *http://domain* or *http://Internet IP*, you will log in to EspoCRM (enter [account password](./user/credentials))

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/espocrm/espocrm-login-websoft9.png)

2. Log in to EspoCRM dashboard

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/espocrm/spocrm-main-websoft9.png)

> Refers to the [EspoCRM Documentation](https://docs.espocrm.com/) to get start your EspoCRM tutorial

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## EspoCRM QuickStart

下面以 **EspoCRM 构建企业CRM** 作为一个任务，帮助用户快速入门：


## EspoCRM Setup

### Set Languages

EspoCRM support more than 14+ languages,how to configure the language after installation?

1. Administrator->Settings,change the language and save it
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/espocrm/EspoCRM-language-websoft9.png)
2. Refresh EspoCRM


### Extension Packages

Extensions allow you to add extra functionality to EspoCRM. They can be installed by Administrator panel->Customization->Extensions
![](http://libs.websoft9.com/Websoft9/DocsPicture/en/espocrm/EspoCRM-extension-websoft9.png)

### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console

2. Log in to EspoCRM, click the menu in the upper right corner -> admin, click [Email Account] to add or edit your personal Email 

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-smtp-1-websoft9.png)

3. Settings for sending and receiving emails: Set IMAP/SMTP parameters separately

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-smtp-2-websoft9.png)

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-smtp-3-websoft9.png)

4. After the setting is completed, please click "Send Test Email" to test 

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage EspoCRM 

通过运行`docker ps`，可以查看到 EspoCRM 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 EspoCRM 本身的参数：

### Path{#path}

EspoCRM 路径:  */data/wwwroot/espocrm*  

### Port{#port}

无特殊端口


### Version{#version}

控制台查看

### Service{#service}

```shell
sudo docker start | stop | restart | stats espocrm
```

### CLI{#cli}

[Console Commands](https://docs.espocrm.com/administration/commands/)

### API
[EspoCRM REST API](https://docs.espocrm.com/development/api/)

