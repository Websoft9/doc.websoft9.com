---
sidebar_position: 1
slug: /redmine
tags:
  - Redmine
  - Project Management
---

# Redmine Getting Started

[Redmine](https://www.redmine.org/) Redmine is a flexible project management web application. Written using the Ruby on Rails framework, it is cross-platform and cross-database.

![Redmine interface](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-gui-websoft9.jpg)


If you have installed Websoft9 Jenkins, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Redmine
4. [Get](./user/credentials) default username and password of Redmine


## Redmine Initialization{#init}

### Steps for you

1. Using local Chrome or Firefox to visit the URL *http://DNS* or *http://Instance's Internet IP*, you will enter the register interface of Redmine

2. Click the 【Log in】 link, enter your username and password([Don't know password?](./user/credentials))
   ![Redmine login](https://libs.websoft9.com/Websoft9/DocsPicture/en/redmine/redmine-login-websoft9.png)

3. You can see the reminder for password modification in the Redmine console
   ![Redmine modify password](https://libs.websoft9.com/Websoft9/DocsPicture/en/redmine/redmine-resetpwf-websoft9.png)

4. Open 【project】and create new project
   ![Redmine new project](https://libs.websoft9.com/Websoft9/DocsPicture/en/redmine/redmine-createproject-websoft9.png)

5. Go to 【Administration】>【Settings】>【display】 to set the project's language
   ![Redmine set language](https://libs.websoft9.com/Websoft9/DocsPicture/en/redmine/redmine-language-websoft9.png)

6. Go to 【Administration】>【Settings】>【user】 to set the user's language interface(is different from Project's language)
   ![Redmine SSH key](https://libs.websoft9.com/Websoft9/DocsPicture/en/redmine/redmine-userlanguage-websoft9.png)
   
7. Activate a new registered user: Go to【Administration】>【Users】, select a registered user in the 【Status】 option, and then activate the user, the user can log in.

> More useful Redmine guide, please refer to [Redmine guide](https://www.redmine.org/projects/redmine/wiki/Guide)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

**Sometimes 502 error when running?**

Redmine need at leaset 2G free memory, If the memory is less than 2, there will be a 502 error.

## Redmine QuickStart


## Redmine Setup

### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console

2. Use SSH or SFTP to connect Server, modify `configuration.yml` and add the following **SMTP segment** to the **production** part: 
   ```
   production:
   delivery_method: :smtp
   smtp_settings:
      address: smtp.exmail.qq.com
      port: 465
      ssl: true
      enable_starttls_auto: true
      domain: websoft9.com
      authentication: :login
      user_name: help@websoft9.com
      password: ********

   ```
3. Restart Redmine service
   ```
   sudo docker restart redmine
   ```
4. Configure host: Administration - Settings - General - HoHost name and pathst

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/redmine/redmine-sethost-websoft9.png)

5. Configure Email sender address: Administration - Settings - Email Notification - Emission Email address, save it, and click "Send a test Email" to test
   
![](https://libs.websoft9.com/Websoft9/DocsPicture/en/redmine/redmine-smtp-websoft9.png)

> Redmine provides  official documentation for SMTP: [Email Configuration](https://www.redmine.org/projects/redmine/wiki/EmailConfiguration)

### Plugin

You can use the Redmine's [plugins](https://www.redmine.org/plugins) to extend functions:

**Install plugin**

The following is a sample for how to install special plugin:  

1. Access Redmine plugin [Ajax Redmine Issue Dynamic Edit](https://www.redmine.org/plugins/redmine_issue_dynamic_edit) page, and get the download URL

2. Use **SFTP** to login Server, run the following commands
   ```
   cd /data/wwwroot/redmine
   wget https://www.redmine.org/attachments/download/25386/redmine_issue_dynamic_edit.zip
   unzip redmine_issue_dynamic_edit.zip 
   docker cp redmine_issue_dynamic_edit redmine:/usr/src/redmine/plugins
   ```

4. Restart Redmine container service
   ```
   sudo docker restart redmine
   ```
   
5. Login to Redmine console to enable you plugin
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-installplugindy-websoft9.png)

**Uninstall plugin**

1. Use **SFTP** to login Server, and delete the plugin at: */data/wwwroot/redmine/plugins*
2. Restart Redmine service
   ```
   sudo docker restart redmine
   ```

### LDAP

Please read the official docs: https://www.redmine.org/projects/redmine/wiki/RedmineLDAP


## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Redmine

Run `docker ps` command, view all Containers when Redmine is running:

```bash
CONTAINER ID   IMAGE               COMMAND                  CREATED          STATUS          PORTS                                                  NAMES
635cd1609242   phpmyadmin:latest   "/docker-entrypoint.…"   21 minutes ago   Up 21 minutes   0.0.0.0:9090->80/tcp, :::9090->80/tcp                  phpmyadmin
bcd0b75f04d7   redmine:4.2         "bash -c 'cat /my_cm…"   21 minutes ago   Up 21 minutes   0.0.0.0:9001->3000/tcp, :::9001->3000/tcp              redmine
b171c341fa90   mysql:5.7           "docker-entrypoint.s…"   21 minutes ago   Up 21 minutes   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   redmine-db
```



### Path{#path}

Redmine installation directory：*/data/apps/redmine*  
Redmine site directory:：*/data/apps/redmine/data/redmine*  
Redmine configuration directory：*/data/apps/redmine/data/redmine/config*  

### Port{#port}

No special port

### Version{#version}

```shell
docker inspect redmine:latest |grep REDMINE_VERSION |head -1 |cut -d= -f2
```

### Service{#service}

```shell
sudo docker start | stop | restart redmine
sudo docker start | stop | restart redmine-db
sudo docker start | stop | restart phpmyadmin
```

### CLI{#cli}

[Redmine-CLI](https://pypi.org/project/Redmine-CLI/)

### API

[Redmine API](https://www.redmine.org/projects/redmine/wiki/Rest_api)
