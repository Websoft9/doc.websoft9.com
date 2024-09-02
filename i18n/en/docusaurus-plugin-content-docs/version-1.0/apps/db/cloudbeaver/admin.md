---
sidebar_position: 3
slug: /cloudbeaver/admin
tags:
  - CloudBeaver
  - Cloud Database Manager
---

# CloudBeaver Maintenance

This chapter is special guide for CloudBeaver maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### CloudBeaver Upgrade

This deployment solution is based on Docker and so you can upgrade CloudBeaver by the standard process of Docker:  

> You should complete an image or snapshot backup for instance before upgrade

1. Use **SFTP** to login Server, modify **APP_VERSION** in the **.env** file of CloudBeaver directory

2. Go to the code-server root directory, then pull new images
   ```
   cd /data/apps/cloudbeaver
   docker-compose pull
   ```
3. Delete old container and recreate new container
   ```
   docker-compose down -v
   docker-compose up -d
   ```


## Troubleshoot{#troubleshoot}

In addition to the Jenkins issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

## FAQ{#faq}

#### Does CloudBeaver support multiple languages?

Yes, you can switch language online.

#### CloudBeaver 支持哪些数据库？

默认支持 

#### What kind of driver does CloudBeaver use to connect to the database?

JDBC Driver

#### Can I create Database from CloudBeaver?

NO

#### Can I access CloudBeaver from other port?

Yes, you need to modify [Nginx vhost configuration file](../nginx#nginx-configure-wizard), and change **server_name** 's `listen 80` to `listen 8090` as sample
