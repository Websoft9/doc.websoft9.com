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

### Superset Upgrade

You can upgrade as follows:

```
cd /data/apps/superset
sudo docker compose down
# such as: upgrade version=2.0.1
sudo sed -i 's/APP_VERSION=.*/APP_VERSION=2.0.1/g' /data/apps/superset/.env
cd /tmp && git clone https://github.com/apache/superset
git checkout 2.0
rm -rf /data/apps/superset/src/docker
cp -r docker /data/apps/superset/src
docker compose up -d

```

 > This upgrade method is only for reference, and it may not be successful in the case of a large version span, please contact customer service.

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

#### Does Google Authentication support it?

SuperSet only provides email login by default, and more login methods need to refer to：[Flask-AppBuilder](https://flask-appbuilder.readthedocs.io/en/latest/security.html#supported-authentication-types)
