---
sidebar_position: 1
slug: /joomla
tags:
  - Joomla
  - CMS
---

# Joomla Getting Started

[Joomla](https://joomla.org/) is a free and open-source content management system (CMS) for publishing web content. Over the years Joomla! has won several awards. It is built on a model -view-controller web application framework that can be used independently of the CMS that allows you to build powerful online applications.

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-gui-websoft9.jpg)  

If you have installed Websoft9 Joomla, the following steps is for your quick start


## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. [Get](./user/credentials) default username and password of Joomla
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Joomla.


## Joomla Initialization

### Steps for you

1. Using local Chrome or Firefox to visit the URL *https://domain* or *https://Internet IP*  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-install3-websoft9.png)

2. Log in Joomla backend (URL is *http://domain/administrator*)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-wizard6-websoft9.png)

3. You can use the Joomla backend to setup your site now, [Get Password](./user/credentials)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-wizard7-websoft9.png)

> Refer to [Joomla admin_manual](https://docs.joomla.org/Main_Page) to get more details

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  
  
#### Joomla not the latest version?

Completed the Joomla initial installation, the login console can be updated online to the latest version with one click.

## Joomla QuickStart

下面以 **使用 Joomla 构建内容管理系统** 作为一个任务，帮助用户快速入门：

## Joomla Setup

### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console  

2. Log in Joomla backend, open【System】>【Global configuration】>【Server】>【Mail Settings】, mailer is set to **smtp**, 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-opensmtp-websoft9.jpg)

3. Fill in the your correct SMTP items
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-smtpsettings-websoft9.png)
   

    * Select "SMTP" for sending mode and "SSL/TLS" for encryption mode;  
    * Enter the sender's email address;  
    * Select "Login" for authentication method and check the "Require authentication" option;  
    * Enter the SMTP server address and SMTP server port number;  
    * Enter the email address that matches the sender's email address;  
    * Enter the authorization code or password of the SMTP service of the email address;  
    * Storage credentials;  

4. Click "Send test email" to test your SMTP settings

     
### Joomla languages{#setlang}

Joomla supports multiple languages. Here are the main steps to install and set up multiple languages:

1. Log in Joomla, go to【Extension】>【Language(s)】>【installed】, install the languages you want
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-bkinstalllan-websoft9.png)

2. Then set your default language of Joomla Site or Administrator
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-bkenablelang-websoft9.png)


### Joomla extension{#plugin}

[Joomla! Extensions Directory™](https://extensions.joomla.org/) provided lots of extensions for you:

1. Log in Joomla  

2. Go to【Extensions】>【Install】>【Install from Web】and search the extensions
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-bkinstallext-websoft9.png)  

3. Install them online


### Joomla install template{#template}

You can upload your template package to install it:

1. Prepare your template (.zip file)

2. Log in Joomla backend

3. Open 【Extensions】>【Install】, select the tab【Upload package file】to install template
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-upload_install.png)

4. When have completed the installation, go to 【Extensions】>【Templates】>【Styles】, enable your template as default template
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-bkenabletemplate-websoft9.png)

> Some template zip package may have the Joomla source code, at this time **Install template=Install Joomla**


### Joomla Cache

Joomla backend have cache management function, refer to this picture:

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-opencache-websoft9.png)

### Joomla reset administrator password{#setpwd}

If you don't remember your administrator password, please refer to the docs [here](https://docs.joomla.org/How_do_you_recover_or_reset_your_admin_password%3F/en) to reset it


## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Joomla

Run `docker ps` command, view all Containers when Joomla is running:

```bash
CONTAINER ID   IMAGE               COMMAND                  CREATED             STATUS             PORTS                                                 NAMES
d25075df271f   phpmyadmin:latest   "/docker-entrypoint.…"   About an hour ago   Up About an hour   0.0.0.0:9090->80/tcp, :::9090->80/tcp                 phpmyadmin
5c64467e167f   bitnami/joomla:4    "/opt/bitnami/script…"   About an hour ago   Up About an hour   8443/tcp, 0.0.0.0:9001->8080/tcp, :::9001->8080/tcp   joomla
9a027cdd4220   mariadb:10.6        "docker-entrypoint.s…"   About an hour ago   Up About an hour   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp             joomla-db
```

### Path{#path}
  
Joomla installation directory:  */data/apps/joomla*  
Joomla website directory： */data/apps/joomla/data/joomla* 
Joomla configuration file: */data/apps/joomla/data/joomla/configuration.php*   

### Port{#port}

No special port  

### Version{#version}

```shell
sudo docker exec -i joomla cat /bitnami/joomla/language/en-GB/install.xml |grep "<version>"
```

### Service{#service}

```shell
sudo docker start | stop | restart | stats joomla
sudo docker start | stop | restart | stats joomla-db
sudo docker start | stop | restart | stats phpmyadmin
```

### CLI{#cli}



### API

[Joomla! API Documentation](https://api.joomla.org/)