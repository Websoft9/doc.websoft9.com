---
sidebar_position: 2
slug: /administrator/upgrade_app
---

# Application Upgrade

Different application have different upgrade solution, you can refer to each application administrator guide for upgrade.  

The two main upgrade methods are described below:  

## Online Upgrade

Online Upgrade use the application's upgrade CLI or GUI to upgrade version. It is a recommend solution.  

You can find the online upgrade solution from every [Application Docs](../apps).  

## Manual Upgrade

In this section, we only introduce the upgrade process for Docker-based applications (universal and strong).  

It main process is: pull the image > delete the container > rebuild the container

1. Backup your application
   ```
   cp  /data/wwwroot/appname /data/wwwroot/appname_bk
   ```

2. Modify your APP_VERSION at [.env file](../administrator/parameter) on your application root directory

3. Pull new Docker image
   ```
   cd /data/wwwroot/appname
   docker-compose pull
   ```

4. Delete old container and recreate new container
    ```
    docker-compose down
    docker-compose up -d
    ```