---
sidebar_position: 1
slug: /mediawiki
tags:
  - Mediawiki
  - CMS
  - Knowledge Management
  - Blog
---

# MediaWiki Getting Started

[MediaWiki](https://mediawiki.org) is a free and open-source wiki software package written in PHP. It serves as the platform for Wikipedia and the other Wiki projects, used by hundreds of millions of people each month. MediaWiki is localised in over 350 languages and its reliability and robust feature set have earned it a large and vibrant community of third-party users and developers.

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mediawiki/mediawikiui.gif)  

If you have installed Websoft9 MediaWiki, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. **[Get](./user/credentials)** default username and password of MediaWiki 
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for MediaWiki 

## MediaWiki Initialization

### Steps for you

1. Using local Chrome or Firefox to visit the URL *https://domain* or *https://Internet IP*  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mediawiki/mediawiki-install1-websoft9.png)

2. Enter the username and password ([Don't know the account password?] ](./user/credentials)) to log in to Mediawiki  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mediawiki/mediawiki-install2-websoft9.png)

3. Go to the MediaWiki backend   
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mediawiki/mediawiki-install3-websoft9.png)

> More useful MediaWiki guide, please refer to [MediaWiki Sysadmin Docs](https://www.mediawiki.org/wiki/Sysadmin_hub)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

#### Can I re-install MediaWiki?

Visit URL *http://Internet IP/mw-config/index.php?page=Restart&lastPage=Install*  to start reinstall

![](http://libs.websoft9.com/Websoft9/DocsPicture/en/mediawiki/Mediawiki-reinstall-websoft9.png)

## MediaWiki QuickStart

下面以 **使用 MediaWiki 构建知识管理系统** 作为一个任务，帮助用户快速入门：

## MediaWiki Setup

### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console  

2. Edit your MediaWiki's configuration file `LocalSettings.php` in the root directory  

3. Search the variable `$wgSMTP`, set the values
   ```
    $wgSMTP = array(
    'host'     => "smtp.163.com", 
    'IDHost'   => "example.com",      // Email's domain name, optional
    'port'     => 465,                 
    'auth'     => true,               
    'username' => "websoft9@163.com",     
    'password' => "#wwBJ8"       
    );
   ```
4. Search the variable `$wgEnableEmail`, set the value
   ```
   $ wgEnableEmail = true
   ```
5. Search the variablea `$wgEnableEmail`, set it as your email address
   ```
   $wgEmergencyContact = "websoft9@163.com";
   $wgPasswordSender = "websoft9@163.com";
   ```
6. Save it  

7. Restart [PHP-FPM Service](#service)  

8. Test email sending

### Install plugin{#plugin}

Refer to [Manual:Extensions](https://www.mediawiki.org/wiki/Manual:Extensions)

### Create&Edit page{#page}

Refer to MediaWiki official docs: [Help:Starting_a_new_page](https://www.mediawiki.org/wiki/Help:Starting_a_new_page/en)

### VisualEditor{#edit}

Refer to MediaWiki official docs: [Help:Starting_a_new_page](https://www.mediawiki.org/wiki/Help:VisualEditor/User_guide/en)

### Change interface{#theme}

Changing interface includes: modify logo, set navigation, modify css and so on

Refer to MediaWiki official docs: [Help:FAQ:Changing Interface](https://www.mediawiki.org/wiki/Manual:FAQ#Changing_the_interface)

### Upload files{#upload}

You can't upload files from MediaWiki by default, you need to enable it first  

Refer to MediaWiki official docs: [Help:FAQ:Enabel Uploading](https://www.mediawiki.org/wiki/Manual:FAQ#How_do_I_enable_uploading?)

### Languages{#setlang}

Refer to MediaWiki official docs: [Help:FAQ:Language](https://www.mediawiki.org/wiki/Manual:FAQ#How_do_I_change_the_interface_language?)

### set MainPage{#sethomepage}

Refer to MediaWiki official docs: [Help:FAQ:Chage Main Page](https://www.mediawiki.org/wiki/Manual:FAQ#How_do_I_change_which_page_is_the_main_page?)

### Using Composer{#composer}

Websoft9's MediaWiki have installed the Composer by default  

Refer to MediaWiki official docs: [Help:Composer](https://www.mediawiki.org/wiki/Composer/en) 

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage MediaWiki

Run `docker ps` command, view all Containers when MediaWiki is running:  

```bash
CONTAINER ID   IMAGE                      COMMAND                  CREATED          STATUS          PORTS                                                 NAMES
88ba09aae88d   bitnami/mediawiki:latest   "/opt/bitnami/script…"   11 minutes ago   Up 11 minutes   8443/tcp, 0.0.0.0:9005->8080/tcp, :::9005->8080/tcp   mediawiki
9f651002908f   mysql:5.7                  "docker-entrypoint.s…"   11 minutes ago   Up 11 minutes   3306/tcp, 33060/tcp                                   mediawiki-db
```

### Path{#path}

MediaWiki installation directory: */data/apps/mediawiki*     
MediaWiki configuration file: */data/apps/mediawiki/data/mediawiki/LocalSettings.php*    
MediaWiki extension directory： */data/apps/mediawiki/data/mediawiki/extensions*     

### Port{#port}

No special port  

### Version{#version}

```
sudo docker exec -i mediawiki grep -rn "MediaWiki " /bitnami/mediawiki/LocalSettings.php|awk -F"MediaWiki " '{print $2}'
```


### Service{#service}

```shell
sudo docker start | stop | restart | stats mediawiki
sudo docker start | stop | restart | stats mediawiki-db
```

### CLI{#cli}

None

### API

[API:Main_page](https://www.mediawiki.org/wiki/API)