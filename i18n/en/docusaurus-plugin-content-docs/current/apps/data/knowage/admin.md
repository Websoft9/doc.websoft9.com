---
sidebar_position: 3
slug: /knowage/admin
tags:
  - Knowage
  - Data Analysis
  - BI
---

# Knowage Maintenance

This chapter is special guide for Knowage maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

## Troubleshoot{#troubleshoot}

In addition to the Knowage issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

## FAQ{#faq}

#### Knowage support multi-languages?

Yes

#### Install knowledge in this way?

The repository use the Docker installation

#### What the relationship between Knowage and SpagoBI?

Knowage is the evolution of SpagoBI

#### If there is no domain name, can I deploy Knowage?

Yes, visit Knowage by *http://Server's Internet IP:8080/knowage* or *http://Server's Internet IP*

#### What is the password for the database root user?

The password is stored in the server related file: `/credentials/password.txt`

#### Is there a web-base GUI database management tools?

Yes, phpMyAdmin is on it, visit by *http://Server's Internet IP:9090*

#### How to change the permissions of filesytem?

Change owner(group) or permissions like below:

```shell
chown -R knowage.knowage /data/wwwroot/knowage
find /data/wwwroot/knowage -type d -exec chmod 750 {} \;
find /data/wwwroot/knowage -type f -exec chmod 640 {} \;
```

