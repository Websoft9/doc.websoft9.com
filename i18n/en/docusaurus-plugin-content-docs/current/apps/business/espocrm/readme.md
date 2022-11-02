---
sidebar_position: 1
slug: /espocrm
tags:
  - EspoCRM
  - CRM
  - Customer Success
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

1. Using local Chrome or Firefox to visit *http://domain* or *http://Internet IP*, you will log in to EspoCRM ([Get](./user/credentials)username and password )

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/espocrm/espocrm-login-websoft9.png)

2. Log in to EspoCRM dashboard

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/espocrm/espocrm-main-websoft9.png)

> Refers to the [EspoCRM Documentation](https://docs.espocrm.com/) to get start your EspoCRM tutorial

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## EspoCRM QuickStart

Coming soon

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

Run `docker ps` command, view all Containers when EspoCRM is running:

```bash
CONTAINER ID   IMAGE               COMMAND                  CREATED          STATUS          PORTS                                               NAMES
b7518429ca6d   phpmyadmin:latest   "/docker-entrypoint.…"   29 minutes ago   Up 29 minutes   0.0.0.0:9090->80/tcp, :::9090->80/tcp               phpmyadmin
764219b50614   espocrm/espocrm     "docker-daemon.sh"       30 minutes ago   Up 29 minutes   80/tcp                                              espocrm-daemon
e16a2e7fef6d   mysql:8             "docker-entrypoint.s…"   30 minutes ago   Up 30 minutes   3306/tcp, 33060/tcp                                 espocrm-db
e768059102e7   espocrm/espocrm     "docker-entrypoint.s…"   30 minutes ago   Up 30 minutes   0.0.0.0:9001->80/tcp, :::9001->80/tcp               espocrm
f7a3374937b2   espocrm/espocrm     "docker-websocket.sh"    30 minutes ago   Up 29 minutes   80/tcp, 0.0.0.0:9002->8080/tcp, :::9002->8080/tcp   espocrm-websocket
```


### Path{#path}

EspoCRM installation directory:  */data/apps/espocrm*  
EspoCRM website directory:  */data/apps/espocrm/data/espocrm*  


### Port{#port}

No special port


### Version{#version}

```
sudo docker exec -i espocrm cat /var/www/html/data/config.php|grep "'version' =>" |cut -d">" -f2
```

### Service{#service}

```shell
sudo docker start | stop | restart | stats espocrm
sudo docker start | stop | restart | stats espocrm-db
sudo docker start | stop | restart | stats espocrm-daemon
sudo docker start | stop | restart | stats espocrm-websocket
sudo docker start | stop | restart | stats phpmyadmin
```

### CLI{#cli}

[Console Commands](https://docs.espocrm.com/administration/commands/)

### API
[EspoCRM REST API](https://docs.espocrm.com/development/api/)

