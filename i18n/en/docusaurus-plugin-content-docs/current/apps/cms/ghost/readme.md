---
sidebar_position: 1
slug: /ghost
tags:
  - Ghost
  - CMS
  - Website
  - Blog
---

# Ghost Getting Started

[Ghost](https://ghost.org) is the world's most popular open source headless Node.js CMS for professional publishing.  
It makes it simple to publish content online, grow an audience with email newsletters, and make money from premium memberships. Ghost is developed with Node.js. With front-end and back-end completely separated, it runs fast.

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/ghost/ghost-ui-websoft9.png)  

If you have installed Websoft9 Ghost, the following steps is for your quick start


## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. **[Get](./user/credentials)** default username and password of Ghost
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Ghost


## Ghost Initialization

### Steps for you

1. Use local Chrome or Firefox to access the URL *http://domain* or *http://Internet IP* to enter the frontend.
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/ghost/ghost-bootpage-websoft9.png)  

2. Access *http://domain/ghost* or *http://Internet IP/ghost* to enter the backend.
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/ghost/ghost-register001-websoft9.png)

3. Create your account with the email address as username. Don't set a too simple password.  

   
> More about how to use Ghost, please refer to official [Tutorials](https://ghost.org/tutorials/) and [FAQ](https://ghost.org/faq/).

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## Ghost QuickStart


## Ghost Setup

### SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console

2. Log in SendGrid console, and modify the related sections in configuration file mail
   ```
   "mail": {
       "transport": "SMTP",
       "options": {
           "service": "sendgrid",
           "auth": {
               "user": "websoft9smtp",
               "pass": "#fdfwwBJ8f"
           }
       }
   }
   ```
3. restart Ghost docker;
   ```
   cd /data/apps/ghost && docker-compose up -d && docker restart ghost
   ```
4. log in Ghost backend, open 【Manage】>【Staff】and test it by 【Invite People】.

### DNS Additional Configure（Modify URL）{#dns}

Complete **[Five steps for Domain](./administrator/domain_step)** ，Set the URL for Ghost:  

1. Modify the URL domain into yours in [Ghost configuration file](#path);
   ```
   {
   "url": "http://ghost.yourdomain.com",
   "server": {
      "port": 2368,
      "host": "0.0.0.0"
   },
   ```
2. Run the related commands. Above settings work after restarting the service.
   ```
   sudo systemctl restart nginx
   cd /data/apps/ghost && sudo docker-compose up -d && sudo docker restart ghost
   ```

### Personalization

**Menu**

It's convenient to design menu in Ghost. Just take the following steps:

1. login in Ghost, and click【SETTING】>【Design】in the left of menu;
  ![Ghost Menu Setting](https://libs.websoft9.com/Websoft9/DocsPicture/en/ghost/ghost-setmenus-websoft9.png)

2. design as you like and click【Save】.

**Theme**

Theme is the main tool to personalize the interface. There is a default theme. You can also upload themes by taking the following steps:

1. login in Ghost, click【SETTING】>【Design】 and then pull down the page to find the theme setting;

2. click【Theme Marketplace】, find the theme you want and download the compressed file for the theme, such as a zip file;
  ![Ghost Theme Setting](https://libs.websoft9.com/Websoft9/DocsPicture/en/ghost/ghost-setthemes-websoft9.png)

3. click【Upload a theme】and【Active】. 

Theme uploaded is stored in the directory */data/wwwroot/ghost/content/themes* on the server. You can modify the file included to make theme personalization at code level.

**Languages**

Default language is English and you can add translation files to your theme for any language by taking the following steps:

1. use SSH or SFTP to login in, and find the directory, locales in themes folder;

2. view json files to find your translation files;
![Ghost language setting](https://libs.websoft9.com/Websoft9/DocsPicture/en/ghost/ghost-listalllanguages-websoft9.png)

3. log in the Ghost backend, click 【General】 and add the translation file to 【Publication Language】.
![Ghost Language Setting](https://libs.websoft9.com/Websoft9/DocsPicture/en/ghost/ghost-setzhhans-websoft9.png)

**Code Injection**

Use code injection to insert third-party JavaScript code to Ghost website, such as Google analysis, etc.  
Once inserted, the code works on each page.

Steps are as follows:

1. login in Ghost and click【SETTING】>【Code Injection】in the left menu;
![Ghost Code Injection](https://libs.websoft9.com/Websoft9/DocsPicture/en/ghost/ghost-codeinjection-websoft9.png)

2. copy the code needed and click 【Save】.

**Subscription**

Ghost supports subscription, which encourages entrepreneurs who offer knowledge as business.

Steps are as follows:

1. login in Ghost and click【SETTING】>【Labs 】in the left menu;

2. set Enable members, Connect to Stripe, Subscription pricing and more.
  ![Ghost Subscription](https://libs.websoft9.com/Websoft9/DocsPicture/en/ghost/ghost-setsubs-websoft9.png)


## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Ghost

Run `docker ps` command, view all Containers when Ghost is running:

```bash
CONTAINER ID   IMAGE               COMMAND                  CREATED       STATUS       PORTS                                                  NAMES
3b1c248cc847   phpmyadmin:latest   "/docker-entrypoint.…"   2 hours ago   Up 2 hours   0.0.0.0:9090->80/tcp, :::9090->80/tcp                  phpmyadmin
cadf419ea7a8   ghost:latest        "docker-entrypoint.s…"   2 hours ago   Up 2 hours   0.0.0.0:9001->2368/tcp, :::9001->2368/tcp              ghost
e069a73a1f73   mysql:8.0           "docker-entrypoint.s…"   2 hours ago   Up 2 hours   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   ghost-db
```

### Path{#path}

Ghost installation directory： */data/apps/ghost*  
Ghost configuration file： */data/apps/ghost/data/ghost/config.production.json*  


### Port{#port}

No special port  

### Version{#version}

```
ls /data/apps/ghost/data/ghost/versions
```

### Service{#service}

```shell
sudo docker start | stop | restart | stats ghost
sudo docker start | stop | restart | stats ghost-db
sudo docker start | stop | restart | stats phpmyadmin
```

### CLI{#cli}

[Ghost CLI](https://ghost.org/docs/ghost-cli/)

### API

[Content API](https://ghost.org/docs/content-api/)