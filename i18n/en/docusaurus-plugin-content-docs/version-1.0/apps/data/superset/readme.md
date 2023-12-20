---
sidebar_position: 1
slug: /superset
tags:
  - Superset
  - Data Analysis
  - BI
---

# superset Getting Started

[Apache Superset](https://superset.apache.org/) (incubating) is a modern, enterprise-ready business intelligence web application

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-dash-websoft9.png)

If you have installed Websoft9 superset, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80**  is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for superset
4. [Get](./user/credentials) default username and password of superset

## Superset Initialization

### Steps for you

1. Using local browser to access URL *http://DNS* or *http://Instance's Internet IP*, enter login page
   ![superset login page](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-login-websoft9.png)

2. Log in to Superset web console([Don't have password?](./user/credentials))  
   ![superset login page](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-console-websoft9.png)

3. Modiyf your password by: 【Super Admin】>【Profile】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-resetpw-websoft9.png)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

**Superset password is correct, but login still fails**

refer to [here](./Superset/admin#loginfail)

## Superset QuickStart

The following is an example of Superset connecting MySQL data source for analysis:

1. Add data source: After logging in Superset, open:【Data】>【Databases】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-database-websoft9.png)

2. Click 【DATABASE】 in the upper right corner, enter the data server address, port, database name and driver to be connected ([More Reference](https://docs.sqlalchemy.org/en/13/core/engines.html)）  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-connect-websoft9.png)
   
   > mysql://username:password@server:port/database name  

3. Click 【ADD】, the added database will be displayed in the list
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-connect-websoft9.png)

4. Add data table(datasets): Open the menu in turn:【Data】>【Datesets】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-dataset-websoft9.png)

5. Click Add Datasets, select datasource, SCHEMA, Table in turn, and click 【ADD】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-selecttable-websoft9.png)

6. The newly added table has been displayed in the Datasets list.
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-datalist-websoft9.png)

7. Data source added successfully 

> More useful Superset guide, please refer to [Superset documentation](https://superset.apache.org/docs/intro)

## Superset Setup

### Install Database Drivers

You’ll need to install the required packages for the database you want to use as your metadata database as well as the packages needed to connect to the databases.  

The below is the command how to install drivers

```
# Access Superset container as root user
docker exec -it --user root superset_app bash

# sample1
pip install mysqlclient

# sample2
pip install psycopg2	
```

Refer to more [Supported Databases and Dependencies](https://superset.apache.org/docs/databases/installing-database-drivers)

### Superset connect to MS SQL server database 

```
# Access Superset container as root user
docker exec -it -u root superset_app bash

# Install MSSQL driver
pip install pymssql

# Log in to Superset, use the following connection string to add SQLServer Database
#  E.g mssql+pymssql://sa:passwd123@192.168.16.1:1433/test
mssql+pymssql://username:password@server ip:port/database 

```

### Replace Logo

If you want to replace logo of Superset Container, please refer to below steps:  

1. Use **SFTP** to upload you png logo to the directory */data` 

2. Rename it to *superset-logo-horiz*

3. Run the below command to replace Superset official logo
   ```
   docker cp /data/superset-logo-horiz.png superset_app:/app/superset/static/assets/images/superset-logo-horiz.png
   ```
   > superset_app is the  SuperSet container name

4. Refresh the Superset console


### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console

2. Add the below SMTP Configuration section to [Superset configuration file](#path) correct the items
   ```
   # smtp server configuration
   EMAIL_NOTIFICATIONS = True  # all the emails are sent using dryrun
   SMTP_HOST = 'smtp.163.com'
   SMTP_STARTTLS = True
   SMTP_SSL = True
   SMTP_USER = 'websoft9@163.com'
   SMTP_PORT = 465
   SMTP_PASSWORD = '#wwBJ8'
   SMTP_MAIL_FROM = 'websoft9@163.com'
   ```
3. Saved and restart Superset container
   ```
   sudo docker restart superset_app
   ```
  

### Reset Password

There are two main measures to reset password.

**Changing password**

Take the steps below:

Login to Superset console, open:【Settings】>【User】>【Info】 to modify password

![Superset modify password](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-resetpw-websoft9.png)


**Forgot Password**

Try to retrieve your password by the flowing steps:  

1. Use **SSH** to connect Server, run the below command to login database
   ```
   docker exec -it superset_db psql -U superset
   ```

2. At the mode of **Database CLI interaction**, run the below SQL command, then you password is `admin123` now.
   ```
   update ab_user set password='pbkdf2:sha256:150000$w8vfDHis$b9c8fa353137417946766ed87cf20510da7e1e3a7b79eef37426330abef552bf' where username='admin';
   ```

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Superset

Run `docker ps` command, view all Containers when Superset is running:

```
CONTAINER ID   IMAGE                           COMMAND                  CREATED              STATUS                                 PORTS                               NAMES
453f04935734   apache/superset:latest          "/usr/bin/docker-ent…"   About a minute ago   Up About a minute (healthy)            0.0.0.0:8088->8088/tcp              superset_app
5477e7693ef3   apache/superset:latest          "/usr/bin/docker-ent…"   About a minute ago   Up About a minute (healthy)            8088/tcp                            superset_worker
d6670fa1bc11   apache/superset:latest          "/usr/bin/docker-ent…"   About a minute ago   Up About a minute (healthy)            8088/tcp                            superset_worker_beat
17689f5d6ebb   postgres:10                     "docker-entrypoint.s…"   About a minute ago   Up About a minute                      0.0.0.0:5432->5432/tcp              superset_db
06bf52f4b856   redis:3.2                       "docker-entrypoint.s…"   About a minute ago   Up About a minute                      127.0.0.1:6379->6379/tcp            superset_cache
```


### Path{#path}

Superset installation directory： */data/apps/superset*  
Superset data directory： */data/apps/superset/superset_home*  
Superset configuration directory： */data/apps/superset/src/docker*  
Superset configuration file： */data/apps/superset/src/docker/pythonpath_dev/superset_config.py*

### Port{#port}

No special port  

### Version

```shell
# Superset Version
docker exec -it superset_app /bin/bash -c 'cat /app/superset-frontend/package.json |grep version'
```

### Service

```shell
sudo docker  start | stop | restart | status superset-app
sudo docker  start | stop | restart | status superset-worker
sudo docker  start | stop | restart | status superset-worker_beat
sudo docker  start | stop | restart | status superset-db
sudo docker  start | stop | restart | status superset-cache
```

### CLI

Superset have CLI `superset` for administrator.  

Use **SSH** to login Server, and run the following command to Superset container

```
# Login to Superset container
docker exec -it superset_app bash

# Run the Superset CLI command
superset
```

Main options and commands:  

```
Usage: superset [OPTIONS] COMMAND [ARGS]...

  This is a management script for the Superset application.

Options:
  --version  Show the flask version
  --help     Show this message and exit.

Commands:
  db                        Perform database migrations.
  export-dashboards         Export dashboards to JSON
  export-datasource-schema  Export datasource YAML schema to stdout
  export-datasources        Export datasources to YAML
  fab                       FAB flask group commands
  flower                    Runs a Celery Flower web server Celery Flower
                            is...

  import-dashboards         Import dashboards from JSON
  import-datasources        Import datasources from YAML
  init                      Inits the Superset application
  load-examples             Loads a set of Slices and Dashboards and a...
  load-test-users           Loads admin, alpha, and gamma user for testing...
  refresh-druid             Refresh druid datasources
  routes                    Show the routes for the app.
  run                       Run a development server.
  set-database-uri          Updates a database connection URI
  shell                     Run a shell in the app context.
  sync-tags                 Rebuilds special tags (owner, type, favorited...
  update-datasources-cache  Refresh sqllab datasources cache
  version                   Prints the current version number
  worker                    Starts a Superset worker for async SQL query...
```

### API

[Superset API](https://superset.apache.org/docs/api) 
