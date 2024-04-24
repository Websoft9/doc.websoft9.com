---
sidebar_position: 3
slug: /erpnext/admin
tags:
  - ERPNext
  - 企业管理
  - ERP
---

# ERPNext Maintenance

This chapter is special guide for ERPNext maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### ERPNext Backup

#### **Automatic backups(scheduled tasks)**

1. Log in to ERPNext and open: Settings> System Settings  
   ![ERPNext backup](https://libs.websoft9.com/Websoft9/DocsPicture/zh/erpnext/erpnext-autobk-websoft9.png)

2. Wait for the scheduled task to execute  


#### **Manual backup**

[Manual backup](https://frappeframework.com/docs/user/en/bench/reference/backup) ERPNext：

1. Enter the ERPNext container  
   ```
   docker exec -it erpnext-worker-default  bash
   ```
2. Run the backup command  

   ```
   # Query the project folder name (IP or DNS)
   ls

   # backup  
   bench --site 121.41.86.118 backup
   ```

#### Get the backup file  

Backup files are stored in persistent storage for ERPNext.  

   > Download fails at Download Backups in the background, the cause remains to be investigated. You can download it directly from the path above.  


## Troubleshoot{#troubleshoot}

In addition to the ERPNext issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### Error in Chrome when modify password?

This error is not attribute to ERPNext server, once you have upgraded you local Chrome, it solved

#### Why I get the message "You should not run this command as root" when run bench?

The bench commands only can run for the user name frapper, you must change the user first
```shell
su - frapper
```

#### Error prompt in the last step of the ERPNext installation wizard?

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/erpnext/erpnext-wizarderror-websoft9.png)
Cause: unknown  
Solution: repeat the installation several times until successful


## FAQ{#faq}

#### Which install solution for this ERPNext?

Use Docker installation, you can access our [Docker-Compose for ERPNext](https://github.com/Websoft9/docker-erpnext) open source project on Github

#### Can I install ERPNext by **Manual installation**?

Yes, the general installation process of ERPNext is as follows:

1. Use the **bench** command to initialize a Frappe framework
2. Install ERPNext app
3. Create a site with the same name as ERPNext
4. Connect the site with the app


#### What are the relationship and difference between Frappe, bench and ERPNext?

[ERPNext](https://github.com/frappe/erpnext) is based on Frappe for free ERP framework development.  
[Frappe](https://github.com/frappe/frappe) is a framework for rapid development of JS and Python integrated applications.  
[Bench](https://github.com/frappe/bench) is a CLI tool of Frappe framework, which used to create and manage Frappe by commands.

#### Why should create *site* for ERPNext installation?

Frappe framework is mainly composed of two parts: app and site. App is the back-end Python code, and site is the front-end part for handling HTTP requests.

#### What databases does ERPNext support?

MariaDB and PostgreSQL

#### How to change the permissions of filesytem?

Change owner(group) or permissions like below:

```shell
chown -R apache.apache /data/wwwroot/erpnext
find /data/wwwroot/erpnext -type d -exec chmod 750 {} \;
find /data/wwwroot/erpnext -type f -exec chmod 640 {} \;
```