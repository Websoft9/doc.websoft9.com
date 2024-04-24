---
sidebar_position: 1
slug: /moodle
tags:
  - Moodle
  - elearning
---

# Moodle Getting Started

[Moodle](https://moodle.org) is a learning platform designed to provide educators, administrators and learners with a single robust, secure and integrated system to create personalised learning environments.Moodle is built by the Moodle project which is led and coordinated by Moodle HQ, an Australian company of 30 developers which is financially supported by a network of over 60 Moodle Partner service companies worldwide.

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodlegui-websoft9.jpg)  

If you have installed Websoft9 Moodle, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. **[Get](./user/credentials)** default username and password of Moodle
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Moodle  

## Moodle Initialization

### Steps for you

1. Using local Chrome or Firefox to visit the URL *https://domain name* or *https://Internet IP*, enter to Moodle login page  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-install1-websoft9.png)

2.  Click [Login] to enter the login page, log in to the backend, ([Don't know the account password?](./user/credentials))
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-install3-websoft9.png)

3. Set up site information
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-newsite-websoft9.png) 

4. [Set the site language](#setlanguge)

5. [Register a Moodle account](#register) to connect Moodle official website for more extension

> More useful Moodle guide, please refer to [Moodle Documentation](https://docs.moodle.org)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## Moodle QuickStart


## Moodle Setup


### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console

2. Log in to Moodle console as administrator  

3. Open **Site administrator** > **Server** > **Email** > **Outgoing mail configuration**
   ![Moodle SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/moodle-smtp-websoft9.png)
   ![Moodle SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/moodle-smtps-websoft9.png)  

4. Click the **Test outgoing mail configuration** to test your settings

### Register your Moodle site{#register}

Once completed your Moodle installation wizard, suggest you to register Moodle's website account. This account can help you to get upgrade message, get share course of Moodle.NET, install plugins online

1. Log in Moodle console as administrator  

2. Open **Site administrator** > **Registation**
   ![Moodle register](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/moodle-registermd-websoft9.png)  

3. When you completed it, Moodle.net may stay in touch and provide you with important things for your Moodle site

### Moodle languages{#setlanguge}

1. Log in Moodle console as administrator  

2. Open **Site administrator** > **Language**
   ![Moodle Language](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-languageset-websoft9.png)

3. Set it by yourself  
   ![Moodle Language](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-languagepacks-websoft9.png)  
 
   * Language settings: choose your language online
   * Language customization: edit your language files online
   * Language packs: upload your language packs
4. Switch languages
   ![Moodle languages](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-mutlanguage-websoft9.png)


  
### Moodle Mobile{#client}

1. Log in Moodle console as administrator  

2. Open **Site administrator** > **Mobile app** > **Mobile settings**
   ![moodle-apps](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/moodle-app-1-websoft9.png)  

3. Check **Enable web services for mobile devices** is selected
   ![moodle-apps](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/moodle-app-2-websoft9.png)  

4. Save settings  

5. Install [Moodle APPS](https://download.moodle.org/mobile/) in your phone  

6. Open the Moodle app in your phone, configure the Moodle's URL to your app and start to use it
   ![moodle-apps](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-mobile-websoft9.png)
   

### Moodle plugins{#plugin}

Moodle is very scalable platform, most of function were as plugins. Moodle have installed 400+ plugins by default and you can install plugins from [Plugins Marketplace](https://moodle.org/plugins/) to extend your functions

1. Log in Moodle console as administrator  

2. Open **Site administrator** > **Plugins** 
   ![moodle plugins](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/moodle-plugins-websoft9.png)  

3. Click **Plugins Overview** to list all plugins installed, you can disable and uninstall it also  

4. Visit [Plugins Marketplace](https://moodle.org/plugins/) to search more plugins,and download 

5. Start to install plugins in the Moodle's console
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/moodle-intallplugins001-websoft9.png)  

6. Upload plugin online
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/moodle-intallplugins-uploadfile-websoft9.png) 

> More details about manage plugins please refer to official docs [Moodle Plugins](https://docs.moodle.org/37/en/Installing_plugins)

### Moodle theme{#theme}

The Moodle theme is also a plugin, so to install a new theme, install it first by [Install Plugin](#plugin).   

1. Log in Moodle console as administrator  

2. Visit [Plugins Marketplace](https://moodle.org/plugins/) to search more themes,and download  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/moodle-mktheme-websoft9.png)

3. [Install the theme](#plugin)

4. Use themes
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/moodle-addtheme001-websoft9.png)


### Reset Password{#resetpwd}

There are two main measures to reset Moodle's password：

**Changing password**

Take the steps below:

1. log in the Moodle console, click 【Profile】 link of user icon on the top menu, then click the **setting icon**
  ![Moodle console modify password](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/moodle-modifypw-websoft9.png)

2. start to change the password.

**Forgot Password**

If you have forgotten the password of Moodle, two methods for you tor retrieve it:

* Retrieve it by Email from login page (you must completed the [SMTP settings](./administrator/smtp))
* Retrieve it by modify database

Follow the steps of retrieve database by modify database:

1. Login [phpMyAdmin](./administrator/parameter#managedb), and find the database table *mdl_user*

  ![Moodle user table](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/moodle-phpmyadminuser-websoft9.png)

2. Edit the 【admin】user, replace the column `password` 's value to `21232f297a57a5a743894a0e4a801fc3`

3. Click 【Go】 button, the password has been set to `admin`

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Moodle

Run `docker ps` command, view all Containers when Moodle is running:

```bash
CONTAINER ID   IMAGE                  COMMAND                  CREATED       STATUS       PORTS                                                 NAMES
0df736525a31   phpmyadmin:latest      "/docker-entrypoint.…"   2 hours ago   Up 2 hours   0.0.0.0:9090->80/tcp, :::9090->80/tcp                 phpmyadmin
91e032f7426b   bitnami/moodle:4       "/opt/bitnami/script…"   2 hours ago   Up 2 hours   8443/tcp, 0.0.0.0:9001->8080/tcp, :::9001->8080/tcp   moodle
ea1b14f31de8   bitnami/mariadb:10.6   "/opt/bitnami/script…"   2 hours ago   Up 2 hours   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp             moodle-db
```

### Path{#path}

Moodle installation directory:  */data/apps/moodle*  
Moodle configuration file:  */data/apps/moodle/data/moodle_data/config.php*  
Moodle installation directory： */data/apps/moodle/data/moodledata_data*  

### Port{#port}

No special port

### Version{#version}

```
docker exec -i moodle cat /bitnami/moodle/version.php  | grep "\$release" | awk '{print $3}' | sed 's/^.//'
```

### Service{#service}

```shell
sudo docker start | stop | restart | stats moodle
sudo docker start | stop | restart | stats moodle-db
sudo docker start | stop | restart | stats phpmyadmin
```

### CLI{#cli}

[Administration via command line](https://docs.moodle.org/311/en/Administration_via_command_line)

```
$ cd /path/to/your/moodle/dir
$ sudo -u apache /usr/bin/php admin/cli/somescript.php --params
$ sudo -u apache /usr/bin/php admin/cli/install.php --help
```

### API

[Core APIs](https://docs.moodle.org/dev/Core_APIs)