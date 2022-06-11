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

1. Using local Chrome or Firefox to visit the URL *https://domain* or *https://Internet IP*, start to install    
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/mediawiki/mw01.png)

2. Choose a language to continue
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/mediawiki/mw02.png)

3. Acccept the license and Continue
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/mediawiki/mw03.png)

4. Fill in database configuration
   > It's  easy to make mistakes on this step. If have mistakes, you can [Re-install Mediawiki]
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/mediawiki/mediawiki-setdbconnstr-websoft9.png)

   - Database name: mediawiki (MySQL on this Image has a database instance name mediwiki)
   - Database username: root
   - Database password: [Don't know password?](./user/credentials)
   
   If you don't want to use the mediawiki as Database name,please create your database first. If you don't want to use the root as Database username,please create your user first

5. Set database character,Click "Continue";  
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/mediawiki/mw05.png)

6. Set the site name, administrator account, password and mail,Click "Continue";
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/mediawiki/mw06.png)

7. Click "Continue";  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/mediawiki/mw07.png)

8. Click "Continue";  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/mediawiki/mw08.png)

9. Click "Continue";  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/mediawiki/mw09.png)

10. Download the file and upload it to the server directory:/data/wwwroot/mediawiki
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/mediawiki/mw10.png)

11. OK, it has been installed successfully.

12. Use http://domain  to go to your index page.
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/mediawiki/mw11.png)

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

7. Restart [PHP-FPM Service](/zh/admin-services.html#php-fpm)  

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

通过运行 `docker ps`，可以查看到 MediaWiki 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```

### Path{#path}

MediaWiki installation directory: */data/wwwroot/mediawiki*  
MediaWiki configuration file: */data/wwwroot/mediawiki/LocalSettings.php* 

### Port{#port}

| Port | Use                                          | Necessity |
| ------ | --------------------------------------------- | ------ |
| 8080   | MediaWiki original port | Optional   |


### Version{#version}

控制台查看

### Service{#service}

```shell
sudo docker start | stop | restart | stats mediawiki
```

### CLI{#cli}

None

### API

[API:Main_page](https://www.mediawiki.org/wiki/API:Main_page/zh)