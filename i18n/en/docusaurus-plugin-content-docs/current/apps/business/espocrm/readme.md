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

1. Using local Chrome or Firefox to visit *http://domain* or *http://Internet IP*, you will enter the configuration interface of installation
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/espocrm/ep01.png)

2. Agree license, go to next step
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/espocrm/ep02.png)

3. Then configure the database connection information([Don't know password?](./user/credentials)) and set administrator account
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/espocrm/ep03.png)

4. Wait the installing  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/espocrm/ep04.png)

5. Set system configuration
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/espocrm/ep06.png)

5. Set your SMTP (Optional)
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/espocrm/ep07.png)

6. Install successfully  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/espocrm/ep08.png)

7. Log in to EspoCRM dashboard
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/espocrm/ep10.png)

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

2. 待EspoCRM安装完成后，点击右上角菜单->admin，点击Email项
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-smtp-1-websoft9.png)

3. 根据下图的设置，完成SMTP参数的设置
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-smtp-2-websoft9.png)
	* Server 处请填写 smtp 服务器的地址 ；
	* Port 处请填写正确的端口号；
	* Auth 处勾选表示发邮件需要验证账号
	* Security 处请邮件服务器支持的连接协议；
	* UseName 处请输入自己的邮箱地址 ；
	* Password 处请输入SMTP密码或授权码（不同于邮箱密码）

4. 设置完成后，请点击“Send Test Email”测试设置是否成功

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

