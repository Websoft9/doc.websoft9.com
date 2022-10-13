---
sidebar_position: 1
slug: /zentao
tags:
  - ZenTao（禅道）
  - 项目管理
---

# ZenTao Getting Started

[ZenTao](https://www.zentao.pm)  is an Open Source software released under ZPL license. It integrates with Product Management, Project Management, QA Management, Document Management, Todos Management, Company Management etc. ZenTao is the best choice for software project management.

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/zentao/zentao-gui-websoft9.png)

If you have installed Websoft9 Jenkins, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for ZenTao
4. [Get](./user/credentials) default username and password of ZenTao

## ZenTao Initialization

### Steps for you

1. Using local Chrome or Firefox to visit the URL *https://domain* or *https://Internet IP*, start to install  

2. Choose a language, go to next step 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/zentao/zentao-installstart-websoft9.png)

3. Accept LICENSE and check the environment for ZenTao
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/zentao/zentao-installsyscheck-websoft9.png)

4. System initialization has set the database parameters, click Next
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/zentao/zentao-installdbconf-websoft9.png)

5. Set your administrator account for ZenTao
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/zentao/zentao-installadmin-websoft9.png)

6. Installed successfully, please delete the `install.php` in the ZenTao directory
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/zentao/zentao-installss-websoft9.png)

7. ZenTao Log in
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/zentao/zentao-login-websoft9.png)

8. ZenTao dashboard
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/zentao/zentao-gui-websoft9.png)

9. Register [ZenTao official account](https://www.zentao.net/user-register.html), make your ZenTao connect to ZenTao's plugins Marketplace

> Refer to [ZenTao Manual](https://www.zentao.pm/book/zentaomanual/) to get more details

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## ZenTao QuickStart

## ZenTao Setup

### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console

2. Login ZenTao, open:【Admin】>【Message】>【Mail】, select **SMTP** as the mail

3. Fill in the correct SMTP items
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/zentao/zentao-smtp-websoft9.png)

4. After the setting is completed, a message notification is triggered to verify that SMTP is correct.

### Set Languages

ZenTao supports multiple languages. Here are the main steps to install and set up multiple languages:
![](https://libs.websoft9.com/Websoft9/DocsPicture/en/zentao/zentao-changelanguage-websoft9.png)

### Install Plugin

ZenTao have provided [Plugins Marketplace](https://www.zentao.net/extension-browse.html) for you to extend functions of ZenTao

1. Log in ZenTao, search the plugins you want to use
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/zentao/zentao-dlplugins-websoft9.png)

2. Intall plugin

> You can download plugin and unzip it, then upload to */zentao/module* for installing also

## ZenTao recover administrator password

If you don't remember your administrator password, please user phpMyAdmin to modify **zt_user** table of ZenTao's database, make the password of your adminitrator's value is `e10adc3949ba59abbe56e057f20f883e`, then your new password is `123456`

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-recoverpw-websoft9.png)

### Integrate Git

Refer to [Integrate Git](https://www.zentao.pm/book/zentaomanual/free-open-source-project-management-software-git-105.html)

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage ZenTao

Run `docker ps`, view all containers when ZenTao is running:  

```bash
CONTAINER ID   IMAGE                    COMMAND                  CREATED         STATUS         PORTS                                   NAMES
bbe3b0d3441d   easysoft/zentao:latest   "bash -c 'cat /my_cm…"   8 minutes ago   Up 8 minutes   0.0.0.0:9003->80/tcp, :::9003->80/tcp   zentao
0c04db7cc20a   mysql:5.7                "docker-entrypoint.s…"   8 minutes ago   Up 8 minutes   3306/tcp, 33060/tcp                     zentao-db

```

### Path {#path}

ZenTao installation directory: */data/apps/zentao*  
ZenTao source code path: */data/apps/zentao/data/zentao*  
ZenTao configuration file: */data/apps/zentao/data/zentao/config/config.php*  

### Port{#port}

no special port

### Version

```shell
# ZenTao Version
cat /data/apps/zentao/data/zentao/VERSION
````

### Service

```shell
sudo docker start | stop | restart | stats zentao
sudo docker start | stop | restart | stats zentao-db
````

### Cli

ZenTao provides a set of command operations, please refer to the official documentation for details: [Initialization Management Script](https://www.zentao.net/book/zentaopmshelp/35.html)

### API

[ZenTao API](https://www.zentao.net/book/api/setting-369.html) All request results are in JSON format, and whether the request is successful is judged according to the status of the returned result.
