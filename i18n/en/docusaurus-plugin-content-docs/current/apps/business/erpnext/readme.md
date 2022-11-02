---
sidebar_position: 1
slug: /erpnext
tags:
  - ERPNext
  - 企业管理
  - ERP
---

# ERPNext Getting Started

[ERPNext](https://erpnext.com/) is 100% open source ERP,based on Python and node development, it has comprehensive functions, including accounting, human resources, manufacturing, website, e-commerce, CRM, asset management, customer service workbench and other comprehensive functions. It is very suitable as a substitute for SAP, which has been used by more than 5000 enterprise customers all over the world.
![](http://libs.websoft9.com/Websoft9/DocsPicture/en/erpnext/erpnext-adminui-websoft9.png)

If you have installed Websoft9 ERPNext, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for ERPNext
4. [Get](./user/credentials) default username and password of ERPNext

## ERPNext Initialization

### Steps for you

1. Using local Chrome or Firefox to visit the URL *http://DNS* or *http://Server's Internet IP*, you will enter installation wizard of ERPNext
   ![ERPNext login](https://libs.websoft9.com/Websoft9/DocsPicture/en/erpnext/erpnext-login-websoft9.png)

2. Log in to ERPNext web console([Don't have password?](./user/credentials)), select your language and go to next step 
   ![ERPNext install lang](https://libs.websoft9.com/Websoft9/DocsPicture/en/erpnext/erpnext-installlanguage-websoft9.png)

3. Follow the installation wizard to complete installation wizard

4. You can see the interface when you complete the installation successfully
   ![ERPNext background](https://libs.websoft9.com/Websoft9/DocsPicture/en/erpnext/erpnext-ok-websoft9.png)

   There may be an installation error prompt, then you should retry it again until success
   ![ERPNext wizard installation error](https://libs.websoft9.com/Websoft9/DocsPicture/zh/erpnext/erpnext-wizarderror-websoft9.png)

5. A search box is provided in the top menu for quick retrieval and access to all functions of ERPNext
   ![ERPNext quick search](https://libs.websoft9.com/Websoft9/DocsPicture/en/erpnext/erpnext-usersearch-websoft9.png)

6. Example: enter the 【user】 settings to manage all accounts
   ![ERPNext user management](https://libs.websoft9.com/Websoft9/DocsPicture/en/erpnext/erpnext-userlist-websoft9.png)

> More useful ERPNext guide, please refer to [ERPNext Documentation](https://docs.erpnext.com/)


### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

**ERPNext service can't start?**

Make sure your **hostname** of Server not include the str ".". e.g erpnext12.14.0 is a not regular for ERPNext

you can rename hostname by the following command

```
hostnamectl set-hostname erpnext
```

## ERPNext QuickStart

下面以 **ERPNext 构建企业ERP** 作为一个任务，帮助用户快速入门：



## ERPNext Setup

### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console

2. Log in ERPNext Console,set SMTP parameters in【Settings】>【Email Domain】
![ERPNext SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/erpnext/erpnext-smtp-websoft9.png)

3. After clicking **save**, it will verify SMTP and only the correct items can be saved successfully

### DNS Additional Configure（Modify URL）{#dns}

Complete **[Five steps for Domain](./administrator/domain_step)** ，Set the URL for ERPNext:

1. Use SSH to connect Server,,modify the environment variables and set the domain name：*/data/wwwroot/erpnext/.env*  
   
   ```
   ...
   APP_SITE_URL=your domain
   APP_SITE_NAME=`your domain`
   ...
   ```


2. Restart ERPNext
   ```
   docker-compose up -d 
   ```

### Reset password

There are two main measures to reset password.

### Change password

1. Log in to the background of ERPNext and open Settings > personal settings to find the password modification item
![ERPNext change password](https://libs.websoft9.com/Websoft9/DocsPicture/en/erpnext/erpnext-modifypw-websoft9.png)

2. Set the new password directly and take effect after saving

### Forgot Password

Try to retrieve your password by the following commands when forgot it.

````
sudo -H -u erpnext bash -c "cd /data/wwwroot/frappe-bench && export GIT_PYTHON_REFRESH=quiet && /usr/local/bin/bench set-admin-password newpassword"
````

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage ERPNext

Run `docker ps` command, view all Containers when ERPNext is running:

```bash
CONTAINER ID   IMAGE                        COMMAND                  CREATED          STATUS                    PORTS                                       NAMES
593c04bd4c02   phpmyadmin:latest            "/docker-entrypoint.…"   42 minutes ago   Up 42 minutes             0.0.0.0:9090->80/tcp, :::9090->80/tcp       phpmyadmin
20e2ac33e35b   redis:6.2-alpine             "docker-entrypoint.s…"   43 minutes ago   Up 43 minutes             6379/tcp                                    erpnext-redis
dea90210633b   frappe/erpnext-worker:v14    "bench worker --queu…"   43 minutes ago   Up 43 minutes                                                         erpnext-queue-default
ef18b6e52994   frappe/erpnext-worker:v14    "bench worker --queu…"   43 minutes ago   Up 42 minutes                                                         erpnext-queue-long
b4a168ab4534   frappe/erpnext-nginx:v14     "/docker-entrypoint.…"   43 minutes ago   Up 42 minutes             0.0.0.0:9001->8080/tcp, :::9001->8080/tcp   erpnext-frontend
c7950ea7a76b   frappe/erpnext-worker:v14    "bench schedule"         43 minutes ago   Up 43 minutes                                                          erpnext-scheduler
eba636cdaf31   mariadb:10.6                 "docker-entrypoint.s…"   43 minutes ago   Up 42 minutes (healthy)   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp   erpnext-db
7818fdaa4e72   frappe/frappe-socketio:v14   "docker-entrypoint.s…"   43 minutes ago   Up 42 minutes                                                         erpnext-websocket
971999ec36d3   frappe/erpnext-worker:v14    "/home/frappe/frappe…"   43 minutes ago   Up 43 minutes                                                         erpnext
ae93cdf7bb21   frappe/erpnext-worker:v14    "bench worker --queu…"   43 minutes ago   Up 42 minutes                                                         erpnext-queue-short
```


> erpnext is the main container


### Path{#path}

ERPNext installation directory:  */data/apps/erpnext*  
ERPNext website directory:  */data/apps/erpnext/data/sites*  
ERPNext database configuration file: */data/apps/erpnext/.env*  

### Port{#port}

No special port

### Version{#version}

```
cat /data/apps/erpnext/.env |grep  "APP_VERSION" |awk -F"=" '{print $2}'
```


### Service{#service}

```shell
sudo docker start | stop | restart | stats erpnext
sudo docker start | stop | restart | stats erpnext-db
sudo docker start | stop | restart | stats erpnext-scheduler
sudo docker start | stop | restart | stats erpnext-frontend
sudo docker start | stop | restart | stats erpnext-websocket
sudo docker start | stop | restart | stats erpnext-redis
sudo docker start | stop | restart | stats erpnext-queue-default
sudo docker start | stop | restart | stats erpnext-queue-long
sudo docker start | stop | restart | stats erpnext-queue-short
sudo docker start | stop | restart | stats phpmyadmin
```

### CLI{#cli}

[CLI to manage Multi-tenant deployments for Frappe apps](https://github.com/frappe/bench)

### API

[ERPNext API](https://frappeframework.com/docs/user/en/api)

