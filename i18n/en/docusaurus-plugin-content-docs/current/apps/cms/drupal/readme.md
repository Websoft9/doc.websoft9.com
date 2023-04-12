---
sidebar_position: 1
slug: /drupal
tags:
  - Drupal
  - CMS
  - 建站系统
---

# Drupal Getting Started

[Drupal](https://www.drupal.org/)  is content management software. It’s used to make many of the websites and applications you use every day. Drupal has great standard features, like easy content authoring, reliable performance, and excellent security. But what sets it apart is its flexibility; modularity is one of its core principles. Its tools help you build the versatile, structured content that dynamic web experiences need.

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-gui-websoft9.png)


## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. **[Get](./user/credentials)** default username and password of Drupal
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Drupal
 

## Drupal Initialization

### Steps for you

1. Use the Chrome or Firefox browser on the local computer to access the URL: *http://domain name* or *http://server public IP*, enter the home page
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-main-websoft9.png)

2. Click [login in], enter the user name and password ([do not know the account password?](./user/credentials))
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-install1-websoft9.png)

3. Enter the Drupal backend to experience the full functionality
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-boardpage-websoft9.png)

> More useful Drupal guide, please refer to [Drupal Documentation](https://www.drupal.org/documentation)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## Drupal QuickStart

Coming soon...

## Drupal Setup

### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console  

2. Copy [SMTP Authentication Support](https://www.drupal.org/project/smtp) plugin URL and install it
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-installsmtp001-websoft9.png)

3. Open:【Manage】>【Extend】, select【SMTP Authentication Support】and click 【install】 button
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-installsmtp002-websoft9.png)

4. Open:【Manage】>【Configuration 】, click【SMTP Authentication Support】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-setsmtp001-websoft9.png)

5. Set the SMTP configuration items
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-setsmtp002-websoft9.png)
   
    * Select "SMTP" for sending mode and "SSL/TLS" for encryption mode;  
    * Enter the sender's email address;  
    * Select "Login" for authentication method and check the "Require authentication" option;  
    * Enter the SMTP server address and SMTP server port number;  
    * Enter the email address that matches the sender's email address;  
    * Enter the authorization code or password of the SMTP service of the email address;  
    * Storage credentials;  


6. Select【Enable debugging】when complete setting and will send test mail

4. Test it

### DNS Additional Configure (Modify URL){#dns}

Drupal needs to change the DNS, in addition to the [Drupal configuration file](#path), you also need to modify the DNS in the '.htaccess' in the Drupal root directory.

### Set languages{#setlang}

Drupal supports multiple languages. Here are the main steps to install and set up multiple languages:

1. Log in Drupal, go to【Manage】>【Configuration】>【Regional and Language】, install your languge
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-addlanguage-websoft9.png)

2. After installing a new language, set the default language according to actual needs.

### Install plugin{#installplugin}

[Drupal Modules](https://www.drupal.org/project/project_module) have lots of Modules, below is the step for you to install it

1. Visit [Drupal Modules](https://www.drupal.org/project/project_module) website, and search the Module you want to use
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-searchformodule-websoft9.png)

2. Get the dowload URL of your Module
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-dlmodule-websoft9.png)

3. Log in Drupal,open the Extend installation interface  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-extend-websoft9.png)

4. Go to【Mange】>【Extend】>【Install Extend】, input the URL for Extend installation  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-install_manager_module-websoft9.png)

5. Install successfully
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-moduleinstalled-websoft9.png)

6. At last, enable the Theme you have installed online
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-enablemodule-websoft9.png)

### Install Themes{#theme}

[Drupal Themes](https://www.drupal.org/project/project_theme) have lots of Themes, below is the step for you to install it

1. Visit [Drupal Themes](https://www.drupal.org/project/project_theme) website, and search the Theme you want to use
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-searchthemes-websoft9.png)

2. Get the dowload URL of your Theme
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-themesurl-websoft9.png)

3. Open【Mange】>【Extend】>【Install Extend】, input the URL for Extend installation 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-install_manager_module-websoft9.png)

4. Then, open【Appearance】 page, enable the Theme you have installed online
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-completeinstall-theme-websoft9.png)

> Some Themes's zip package may have the Drupal core, at this time **Install Theme= Install Drupal**

### Reset password{#resetpwd}

If you don't remember your administrator password, please refer to the docs [here](https://www.drupal.org/node/44164) to reset it

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Drupal

Run `docker ps` command, view all Containers when Drupal is running:

```bash
CONTAINER ID   IMAGE                   COMMAND                  CREATED         STATUS         PORTS                                                  NAMES
55468e3adc82   phpmyadmin:latest       "/docker-entrypoint.…"   6 minutes ago   Up 6 minutes   0.0.0.0:9090->80/tcp, :::9090->80/tcp                  phpmyadmin
55ed815ca707   bitnami/drupal:latest   "/opt/bitnami/script…"   7 minutes ago   Up 7 minutes   8443/tcp, 0.0.0.0:9001->8080/tcp, :::9001->8080/tcp    drupal
77f0ab094626   mysql:5.7               "docker-entrypoint.s…"   7 minutes ago   Up 7 minutes   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   drupal-db

```

### Path{#path}

Drupal installation directory: */data/apps/drupal*  
Drupal website directory: */data/apps/drupal/data/drupal*  
Drupal configuration file: */data/apps/drupal/data/drupal/sites/default/settings.php*

### Port{#port}

No special port

### Version{#version}

```
docker exec -it drupal cat /opt/bitnami/drupal/core/lib/Drupal.php |grep -i "const version" |awk -F "'" '{print  $2}'
```

### Service{#service}

```shell
sudo docker start | stop | restart | stats drupal
sudo docker start | stop | restart | stats drupal-db
sudo docker start | stop | restart | stats phpmyadmin
```

### CLI{#cli}

The community provides Drupal with a [third-party CLI] (https://drupalconsole.com/) 

### API

[Drupal APIs](https://www.drupal.org/docs/drupal-apis)