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

### 导入企业版 License{#importlicense}

如果您已经向 Seafile 软件商购买了专业版，官方会向您提供授权文件 seafile-license.txt。

通过下面的命令，拷贝授权至 Seafile，即可完成授权文件的安装:

```bash
cp seafile-license.txt /data/wwwroot/seafile/seafile-data/seafile/
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

### 修改邮件通知签名

在[邮件模板](https://manual-cn-origin.seafile.com/config/customize_email_notifications)文件中 "Seafile 团队" 实际上对应后台的【site_name】字段。所以，如果想将邮件通知中默认签名 "Seafile 团队" 修改成自己的签名，方案如下：

登录到 Seafile 修改网站名称即可：
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-sitename-email-websoft9.png)

### Seafile document preview and editing

Refer to：[Seafile Integrate ONLYOFFICE Docs](./seafile/solution#onlyoffice)

### DNS Additional Configure（Modify URL）{#dns}

Complete **[Five steps for Domain](./administrator/domain_step)** ，Set the URL for Seafile:

1. Use the SFTP to connect your Server
2. Modify [Docker-compose file](#path)
   ```text
   ...
    - SEAFILE_SERVER_HOSTNAME=seafile.websoft9.cn # Specifies your host name.
   ...
   ```
   set the item **SEAFILE_SERVER_HOSTNAME** to your domain

3. Save it and then restart Docker-compose [service](#service)
   ```
   sudo cd /data && docker-compose up -d
   ```

### Configure HTTPS{#https}

下面是对 Seafile 官方文档：[向Let's encrypt申请SSL证书](https://manual-cn-origin.seafile.com/deploy/deploy_with_docker#xiang-lets-encrypt-shen-qing-ssl-zheng-shu) 的实践解读，验证可用：

**前置条件**

1. 在云控制台开启 **TCP:443** 端口
2. 完成域名解析，确保 Seafile 可以通过域名访问
3. 登录 Seafile 后台，修改主机地址
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-seturl-websoft9.png)

**基本设置**

Seafile deployment package has installed the SSL module of Nginx and open Certificate Authority **[Let's Encrypt](https://letsencrypt.org/)** for you configure the HTTPS quickly and conveniently.

1. Use the SFTP to connect Server, edit [docker-compose](#path) configuration file
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-editconfig-websoft9.png)

2. You should modify three items at least, then save it
   ```
   - Remove # to enable "443:443"
   - SEAFILE_SERVER_LETSENCRYPT set to **true**
   - SEAFILE_SERVER_HOSTNAME set to you domain
   ```

3. Run the compose command to rebuild them
   ```
   sudo cd /data && docker-compose up -d
   ```

4. HTTPS settings completed

The steps above is from  Seafile official docs: [Let's encrypt SSL certificate](https://download.seafile.com/published/seafile-manual/deploy/deploy_with_docker.md)

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

### 使用客户端{#client}

1. 到[官网](https://www.seafile.com/download/)下载客户端

2. 获取客户端登录 SERVICE_URL ：登录到 Seafile 后台，点击右上方个人头像，进入【系统设置】获取 SERVICE_URL

   ![Seafile](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-client-web-websoft9.jpg)

3. 在手机上打开 Seafile 客户端，输入上面获取的 SERVICE_URL 和[账号](./user/credentials)，点击登录

   ![Seafile](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-client-login-websoft9.jpg)

4. 客户端主界面

   ![Seafile](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-client-main-websoft9.jpg)

## Reference sheet{#parameter}

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Seafile

通过运行`docker ps`，可以查看到 Seafile 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE                              COMMAND                  CREATED             STATUS              PORTS                                         NAMES
958e4cbc8dbe        seafileltd/seafile-mc:latest       "/sbin/my_init -- /s…"   14 hours ago        Up 9 minutes        0.0.0.0:80->80/tcp, 0.0.0.0:443->443/tcp      seafile
80c266262079        phpmyadmin/phpmyadmin:latest       "/docker-entrypoint.…"   14 hours ago        Up 9 minutes        0.0.0.0:9090->80/tcp                          phpmyadmin
cea7ee7b8f2a        memcached:1.5.6                    "memcached -m 256"       14 hours ago        Up 9 minutes        11211/tcp                                     seafile-memcached
43881d791ed6        seafileltd/elasticsearch:5.6.16    "/docker-entrypoint.…"   14 hours ago        Up 9 minutes        3306/tcp                                      seafile-elasticsearch
a4498231bb29        onlyoffice/documentserver:latest   "/bin/sh -c /app/ds/…"   39 hours ago        Up 9 minutes        0.0.0.0:9002->80/tcp, 0.0.0.0:9003->443/tcp   onlyoffice-documentserver
```


下面仅列出 Seafile 本身的参数：

### Path{#path}

Seafile 存储目录： */data/wwwroot/seafile/seafile-data*  
Seafile 日志目录： */data/wwwroot/seafile/seafile-data/logs*

seafile-memcached 存储目录： */data/wwwroot/seafile/seafile-data*  
seafile-memcached 日志目录： */data/wwwroot/seafile/seafile-data/logs*

seafile-elasticsearch 存储目录： */data/wwwroot/seafile/seafile-elasticsearch*  
seafile-elasticsearch 日志目录： */data/wwwroot/seafile/seafile-data/logs*

> Seafile 配置文件包括 seahub_settings.py, seafile.conf等

### Port{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 9002 | 通过 http访问 OnlyOffice Docs on Docker | 可选 |

### Version{#version}

Seafile 控制台查看  

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-aboutversion-websoft9.png)

### Service{#service}

```shell
sudo docker start | stop | restart seafile
```

### CLI{#cli}

[Seafile client for a Cli server](https://help.seafile.com/syncing_client/linux-cli/)

### API

[Web AP](https://manual.seafile.com/develop/web_api_v2.1/)

