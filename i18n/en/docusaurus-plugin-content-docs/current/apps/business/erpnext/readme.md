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

通过运行`docker ps`，可以查看到 ERPNext 运行时所有的 Container：

```bash
CONTAINER ID   IMAGE                        COMMAND                  CREATED             STATUS             PORTS                                       NAMES
949746dc0e88   frappe/frappe-socketio:v13   "docker-entrypoint.s…"   About an hour ago   Up About an hour                                               erpnext-socketio
030c4324b810   frappe/erpnext-worker:v13    "docker-entrypoint.s…"   About an hour ago   Up About an hour                                               erpnext-schedule
5816692bb579   frappe/erpnext-worker:v13    "docker-entrypoint.s…"   About an hour ago   Up About an hour                                               erpnext-worker-long
09b2e2242549   frappe/erpnext-worker:v13    "docker-entrypoint.s…"   About an hour ago   Up About an hour                                               erpnext-worker-short
2252928c2230   frappe/erpnext-worker:v13    "docker-entrypoint.s…"   About an hour ago   Up About an hour                                               erpnext-worker-default
4108b4ca06d5   redis:latest                 "docker-entrypoint.s…"   About an hour ago   Up About an hour   6379/tcp                                    erpnext-redis-cache
bbe639069a28   redis:latest                 "docker-entrypoint.s…"   About an hour ago   Up About an hour   6379/tcp                                    erpnext-redis-queue
29f4870961b4   mariadb:10.3                 "docker-entrypoint.s…"   About an hour ago   Up About an hour   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp   erpnext-mariadb
9aecda1e6f3e   redis:latest                 "docker-entrypoint.s…"   About an hour ago   Up About an hour   6379/tcp                                    erpnext-redis-socketio
a404ca45d127   frappe/erpnext-nginx:v13     "/docker-entrypoint.…"   About an hour ago   Up About an hour   0.0.0.0:8000->80/tcp, :::8000->80/tcp       erpnext-nginx
39d908b3132e   frappe/erpnext-worker:v13    "docker-entrypoint.s…"   About an hour ago   Up About an hour                                               erpnext-worker
```

> erpnext-worker-default 为项目主容器

下面仅列出 ERPNext 本身的参数：

### Path{#path}

ERPNext 路径:  */data/wwwroot/erpnext*  
ERPNext 数据库配置文件: */data/wwwroot/erpnext/.env*  
ERPNext 日志路径:  */data/wwwroot/erpnext/volumes/erpnext-logs-vol*  
ERPNext 应用路径 : */data/wwwroot/frappe-bench/volumes/erpnext-site-vol*  
ERPNext 附件路径:  */data/wwwroot/frappe-bench/volumes/erpnext-assets-vol*     
ERPNext 备份位置：*/var/lib/docker/volumes/docker-erpnext_sites-vol/_data/IP/private/backups*  

### Port{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 8080   | ERPNext 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |


### Version{#version}

控制台查看

### Service{#service}

```shell
sudo docker start | stop | restart | stats erpnext-worker-default
```

### CLI{#cli}

[CLI to manage Multi-tenant deployments for Frappe apps](https://github.com/frappe/bench)

### API

参考： [ERPNext API](https://frappeframework.com/docs/user/en/api)

