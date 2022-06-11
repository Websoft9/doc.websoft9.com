---
sidebar_position: 1
slug: /dolibarr
tags:
  - Dolibarr
  - CRM
  - 客户成功
---

# Dolibarr Getting Started

[Dolibarr](https://www.dolibarr.org/onlinedemo.php) is a software suite for small and micro enterprises, freelancers and other enterprises, which used for resource planning and customer relationship management. You can use one web suite to manage all of your business by Dolibarr Management SoftwareDiscourseDiscourse Reviews

![](http://libs.websoft9.com/Websoft9/DocsPicture/en/dolibarr/dolibarr-gui-websoft9.png)

If you have installed Websoft9 Dolibarr, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Dolibarr
4. [Get](./user/credentials) default username and password of Dolibarr

## Dolibarr Initialization

### Steps for you

1. Using local Chrome or Firefox to visit *http://domain* or *http://Internet IP*, you will enter the configuration interface of installation
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/dolibarr/dolibarr-check-websoft9.png)

2. Agree license and environment, go to next step
3. Then configure the database connection information([Don't know password?](./user/credentials))
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/dolibarr/dolibarr-dbconf-websoft9.png)

4. Check database connection
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/dolibarr/dolibarr-confss-websoft9.png)

5. Set your administrator account
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/dolibarr/dolibarr-adminconf-websoft9.png)

6. Install successfully 
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/dolibarr/dolibarr-installss-websoft9.png)

7. Log in Dolibarr
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/dolibarr/dolibarr-login-websoft9.png)

8. Dolibarr dashboard
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/dolibarr/dolibarr-backend-websoft9.png)

9. Go to “Home->Setup->Company/Foundation” and edit informations for company or foundation you want to manage.
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/dolibarr/dolibarr-setupcompany-websoft9.png)

> Refers to the [Dolibarr Documentation](https://docs.dolibarr.com/) to get start your Dolibarr tutorial

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## Dolibarr QuickStart

下面以 **Dolibarr 构建企业CRM** 作为一个任务，帮助用户快速入门：

## Dolibarr Setup


### Modules

Activation of modules is the second mandatory step. What modules you will activate depends on what you want to do with Dolibarr. In most cases, you may want to use all modules. You have to activate one by one each module you plan to use. For example, to manage a company, you might activate modules: Third party, Invoices and Products, but probably a lot of more modules.

To activate a module you want, go to page “Home->Setup->Modules” and click the button ‘on/off’ in the “Status” column to enable it.

![](http://libs.websoft9.com/Websoft9/DocsPicture/en/dolibarr/dolibarr-setupmodules-websoft9.png)



## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Dolibarr 

通过运行`docker ps`，可以查看到 Dolibarr 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 Dolibarr 本身的参数：

### Path{#path}

Dolibarr 路径:  */data/wwwroot/dolibarr*  

### Port{#port}

无特殊端口

### Version{#version}

Dolibarr  控制台查看

### Service{#service}

```shell
sudo docker start | stop | restart | stats dolibarr
```

### CLI{#cli}

无

### API

[Module Web Services API REST](https://wiki.dolibarr.org/index.php?title=Module_Web_Services_API_REST_(developer))