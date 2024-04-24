---
sidebar_position: 1
slug: /seafile
tags:
  - Seafile
  - File sync and share
  - knowledge Management
---

# Seafile Getting Started

[Seafile](https://www.seafile.com/home/) is an open source file sync&share solution designed for high reliability, performance and productivity. Sync, share and collaborate across devices and teams. Build your team's knowledge base with Seafile's built-in Wiki feature.

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/seafile/seafile-gui-websoft9.png)

If you have installed Websoft9 Seafile, the following steps is for your quick start


## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Jenkins.
4. [Get](./user/credentials) default username and password of Jenkins


## Seafile Initialization{#init}

### Steps for you

1. Using local Chrome or Firefox to visit the URL *http://domain name* or *http://Internet IP*, you will log in interface of Seafile
   ![Seafile login page](http://libs.websoft9.com/Websoft9/DocsPicture/en/seafile/seafile-login-websoft9.png)

2. Input Seafile's username and password[(Get it)](./user/credentials)
   ![Seafile console interface](http://libs.websoft9.com/Websoft9/DocsPicture/en/seafile/seafile-bk-websoft9.png)

3. Set or check your Seafile host URL（**Required, otherwise you cannot use the file upload function**）

   - SERVICE_URL：*http://Internt IP of Server*
   - FILE_SERVER_ROOT：*http://Internt IP of Server/seafhttp*

   ![Seafile console UI](https://libs.websoft9.com/Websoft9/DocsPicture/en/seafile/seafile-seturl-websoft9.png)

4. Start to use it

> More details for using Seafile, please use docs: ***[Seafile user guide](https://help.seafile.com/en/)*** and ***[Seafile Server Manual](http://manual.seafile.com/)***

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

**Can I have online document editing and preview in ownCloud?**

The image is pre-installed with [OnlyOffice docs](./onlyofficedocs), which can realize online document editing and preview through configuration, [reference configuration](./seafile/solution#onlyoffice)


## Seafile QuickStart

Below we are familiar with the use of Seafile through operations such as creating a library, creating files, editing files, setting permissions, and user sharing.

**Add & Edit file**

The following is the steps about how to create file and edit file:

1. Login to Seafile Console, and add 【New library】and 【New file】

   ![Seafile add library](https://libs.websoft9.com/Websoft9/DocsPicture/en/seafile/seafile-addlib-websoft9.png)

   ![Seafile add file](https://libs.websoft9.com/Websoft9/DocsPicture/en/seafile/seafile-addfile-websoft9.png)

2. Edit file online by **OnlyOffice Document Server**

   ![Seafile edit file](https://libs.websoft9.com/Websoft9/DocsPicture/en/seafile/seafile-editfile1-websoft9.png)

**User management**

The following is the steps about how to create user and group:

1. Click the icon of user and enter to【System Admin】, click【Add user】and【New Group】

   ![Seafile system admin](https://libs.websoft9.com/Websoft9/DocsPicture/en/seafile/seafile-system-websoft9.png)

   ![Seafile add user](https://libs.websoft9.com/Websoft9/DocsPicture/en/seafile/seafile-adduser-websoft9.png)

   ![Seafile add group](https://libs.websoft9.com/Websoft9/DocsPicture/en/seafile/seafile-addgroup-websoft9.png)

2. Set the user to a group

   ![Seafile user group](https://libs.websoft9.com/Websoft9/DocsPicture/en/seafile/seafile-addusertogroup-websoft9.png)

**Share file**

The following is the steps about how to share files to other user:

1. Enter to【My Library】, click share icon

   ![Seafile share file](https://libs.websoft9.com/Websoft9/DocsPicture/en/seafile/seafile-sharefile1-websoft9.png)


2. Set permission to【Read】or【Read-Write】

   ![Seafile file share](https://libs.websoft9.com/Websoft9/DocsPicture/en/seafile/seafile-sharefile-websoft9.png)

**Edit shared file**

The following is the steps about how to edit the shared files:

1. User another user to login Seafile(username: user1@websoft9)
   ![Seafile login page](https://libs.websoft9.com/Websoft9/DocsPicture/en/seafile/seafile-login1-websoft9.png)

2. Click 【Shared with me】 and edit the file you selected, then logout
   ![Seafile view shared file](https://libs.websoft9.com/Websoft9/DocsPicture/en/seafile/seafile-viewsharefile-websoft9.png)
   ![Seafile edit shared file](https://libs.websoft9.com/Websoft9/DocsPicture/en/seafile/seafile-editfile-websoft9.png)

3. Login with administrator user `me@example.com` and view the history version of file
   ![Seafile view the history version](https://libs.websoft9.com/Websoft9/DocsPicture/en/seafile/seafile-viewfileinfo1-websoft9.png)
   ![Seafile view the history version](https://libs.websoft9.com/Websoft9/DocsPicture/en/seafile/seafile-viewfileinfo-websoft9.png)

## Seafile Setup

### Import the Enterprise License{#importlicense}

If you have purchased the professional version from Seafile, the official will provide you with the authorization file seafile-license .txt.  

Copy the license to Seafile with the following command to complete the installation of the license file:  

```bash
cp seafile-license.txt /data/apps/seafile/data/seafile_data 
docker restart seafile
```

### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console

2. Use the SFTP to connect Server of Seafile, edit the Seafile configuration file [seahub_settings.py](#path)
   
3. Insert your SMPT items (refer to Seafile official docs [sending_email](https://download.seafile.com/published/seafile-manual/config/sending_email.md))
   ```
   EMAIL_USE_SSL = True
   EMAIL_HOST = 'smtp.sendgrid.net'
   EMAIL_HOST_USER = 'websoft9smtp'
   EMAIL_HOST_PASSWORD = '#fdfwwBJ8f'
   EMAIL_PORT = '465'
   DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
   SERVER_EMAIL = EMAIL_HOST_USER
   ```
4. Restart the Seafile service
   ```
   sudo docker restart seafile
   ``` 

### Modify the email notification signature

Log in to Seafile and go to Settings to modify the [SITE_NAME] values.

### Seafile document preview and editing

Refer to：[Seafile Integrate ONLYOFFICE Docs](./seafile/solution#onlyoffice)

### DNS Additional Configure（Modify URL）{#dns}

Complete **[Five steps for Domain](./administrator/domain_step)** ，Set the URL for Seafile:

Log in to the Seafile and modify the host address( SERVER_URL & FILE_SERVER_ROOT ). It must be modified, otherwise the file cannot be uploaded or downloaded normally.


### Configure HTTPS{#https}

### Manage Seafile Password 

We may **Modify** or **recover** Seafile administrator password

**Modify Seafile administrator password**

Log in Seafile, go to Users->Your Profile,update your password
![Seafile Modify Seafile administrator password](https://libs.websoft9.com/Websoft9/DocsPicture/en/seafile/seafile-modifypw-websoft9.png)

**Recover Seafile administrator password**

If you don't remember the Seafile administrator password, you can retrieve it in the following two ways.

**Recover by Email**

Seafile can retrieve the password by sending an email, but only if your Seafile site has already configured SMTP.
![Seafile Modify Seafile administrator password](https://libs.websoft9.com/Websoft9/DocsPicture/en/seafile/seafile-forgetpw-websoft9.png)

**Recover by database**

If the server does not support the function of sending email passwords, the database management panel phpmyadmin will modify it.

1. Log in to phpMyAdmin, find the *EmailUser* table of your Seafile database,Edit the user(e.g. your username is `me@example.com`)  
   ![Seafile database](https://libs.websoft9.com/Websoft9/DocsPicture/en/seafile/seafile-userspw-websoft9.png)
2. Replace the data with `PBKDF2SHA256$10000$7289a20ae4fc2329415b0645fa3d106019cc61952ae1bc2f9eeef7b30dc47d88$5418ac28f06bd84f2bb701a10dbea6b0bd30676c8042e1f73b9ce12aac302a8d`(MD5)
3. Click **run**
4. The new password is `123456` now

### Use the App{#client}

1. Go to [Seafile Website] (https://www.seafile.com/download/) to download the client  

2. Get client login SERVICE_URL: Log in to the Seafile backend, click your profile picture at the top right, and go to [System Settings] to get the SERVICE_URL

## Reference sheet{#parameter}

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Seafile

Run `docker ps` command, view all Containers when Seafile is running:

```bash
CONTAINER ID   IMAGE                          COMMAND                  CREATED       STATUS       PORTS                                       NAMES
824cc16f7950   phpmyadmin:latest              "/docker-entrypoint.…"   3 hours ago   Up 3 hours   0.0.0.0:9090->80/tcp, :::9090->80/tcp       phpmyadmin
fb9c795d5cef   seafileltd/seafile-mc:latest   "/sbin/my_init -- /s…"   3 hours ago   Up 3 hours   0.0.0.0:9001->80/tcp, :::9001->80/tcp       seafile
e237c52ccadd   mariadb:10.5                   "docker-entrypoint.s…"   3 hours ago   Up 3 hours   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp   seafile-db
ffd4eae50a9c   memcached:1.5.6                "memcached -m 256"       3 hours ago   Up 3 hours   11211/tcp                                   seafile-memcached
```



### Path{#path}

Seafile installation directory： */data/apps/seafile*  
Seafile data directory： */data/apps/seafile/data/seafile_data*  
Seafile log directory：*/data/apps/seafile/data/seafile_data/logs*  
Seafile configuration directory：*/data/apps/seafile/data/seafile_data/seafile/conf*  

> Seafile configuration files include seahub_settings.py, seafile.conf, etc

### Port{#port}

| Port | Use                                          | Necessity |
| ------ | --------------------------------------------- | ------ |
| 9002 | Access ONLYOFFICE Docs via http | Optional |

### Version{#version}

View through the Seafile backend


### Service{#service}

```shell
sudo docker start | stop | restart seafile
sudo docker start | stop | restart seafile-db
sudo docker start | stop | restart seafile-memcached
```

### CLI{#cli}

[Seafile client for a Cli server](https://help.seafile.com/syncing_client/linux-cli/)

### API

[Web AP](https://manual.seafile.com/develop/web_api_v2.1/)

