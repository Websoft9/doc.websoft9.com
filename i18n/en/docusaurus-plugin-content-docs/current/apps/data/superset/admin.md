---
sidebar_position: 3
slug: /superset/admin
tags:
  - Superset
  - Data Analysis
  - BI
---

# Superset Maintenance

This chapter is special guide for Superset maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### Backup and Restore

### Upgrade

## Troubleshoot{#troubleshoot}

In addition to the Superset issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### Install database drivers error "[Errno 13] Permission denied"?

You should running Superset container by command `docker exec -it --user root superset_app bash`, then instal drivers

#### I am sure use correct password, but Superset Invalid login?{#loginfail}

Error information: Invalid login, Please try again  
Reason: need more research  
Solution: Run the command `cd /data/wwwroot/superset && docker-compose restart` to restart all containers  

## FAQ{#faq}

####  Does Superset support multiple languages?

Yes, but dev version only English

#### How can I running Superset container as root user?

```
docker exec -it --user root superset_app bash
```

#### How to change the permissions of filesytem?

Change owner(group) or permissions like below:

```shell
chown -R superset.superset /data/wwwroot/superset
find /data/wwwroot/superset -type d -exec chmod 750 {} \;
find /data/wwwroot/superset -type f -exec chmod 640 {} \;
```

#### 是否支持 Google Authentication？

SuperSet 默认只提供了邮件登录，更多登录方式使用需参考其框架文档：[Flask-AppBuilder](https://flask-appbuilder.readthedocs.io/en/latest/security.html#supported-authentication-types)
