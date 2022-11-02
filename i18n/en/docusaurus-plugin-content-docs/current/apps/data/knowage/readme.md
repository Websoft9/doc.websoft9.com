---
sidebar_position: 1
slug: /knowage
tags:
  - Knowage
  - Data Analysis
  - BI
---

# Knowage Getting Started

[Knowage](https://www.knowage-suite.com) is the full capabilities open source suite for modern business analytics over traditional sources and big data systems. Its features, such as data federation, mash-up, data/text mining and advanced data visualization, give comprehensive support to rich and multi-source data analysis. The suite is composed of several modules, each one conceived for a specific analytical domain. They can be used individually as complete solution for a certain task, or combined with one another to ensure full coverage of user’ requirements.

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/knowage/knowage-gui-websoft9.png)

If you have installed Websoft9 Knowage, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Knowage
4. [Get](./user/credentials) default username and password of Knowage

## Knowage Initialization

### Steps for you

1. Using local Chrome or Firefox to visit the URL *http://DNS* or *http://Server's Internet IP*, you will enter login page of Knowage
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/knowage/knowage-login-websoft9.png)

   > You can visit Knowage by the URL: *http://Internet IP:8080/knowage* also

2. Log in to Knowage web console([Don't have password?](./user/credentials)), go to dashboard of Knowage 

3. Go to  Profile Management->Users Management to change the password of Administrator
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/knowage/knowage-changepw-websoft9.png)

4. Go 【Server Settings】>【Configuration Management】 to configure Knowage
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/knowage/knowage-confmanagement-websoft9.png)

> More useful Knowage guide, please refer to [Knowage Documentation](https://knowage-suite.readthedocs.io/)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

**Can't get to the login page?**

Because Knowage has high requirements for computing resources, although the server with 4G memory can also run, the initialization process is relatively slow, please wait a few minutes and try again.  

## Knowage QuickStart


## Knowage Setup

### Connect data source{#datasource}

Take connecting to MySQL as an example, log in to Knowage, enter the main panel, and select > [Data source].


### Data modeling{#datamodel}


## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Knowage

Run `docker ps` command, view all Containers when Knowage is running:

```
CONTAINER ID   IMAGE                                              COMMAND                  CREATED        STATUS                 PORTS                               NAMES
3b30d327e903   mariadb:10.3                                       "docker-entrypoint.s…"   2 hours ago    Up 2 hours             0.0.0.0:3307->3306/tcp              knowage-mariadb-server
a28572948615   knowagelabs/knowage-server-docker:8.0.0-SNAPSHOT   "./entrypoint.sh ./a…"   2 hours ago    Up 2 hours (healthy)   0.0.0.0:8080->8080/tcp              knowage-server
90d49e9971bf   mariadb:10.3                                       "docker-entrypoint.s…"   2 hours ago    Up 2 hours             3306/tcp                            knowage-mariadb-cache
fa5d3ce16865   knowagelabs/knowage-python-docker:8.0.0-SNAPSHOT   "./entrypoint.sh gun…"   2 hours ago    Up 2 hours (healthy)   5000/tcp                            knowage-python
7fbfe56727d5   knowagelabs/knowage-r-docker:8.0.0-SNAPSHOT        "./entrypoint.sh r k…"   2 hours ago    Up 2 hours (healthy)   5001/tcp                            knowage-r
```



### Path{#path}

Knowage installation directory： */data/apps/knowage*  
Knowage resource directory： */data/apps/knowage/data/resources*  


### Port{#port}

No special port  

### Version

```shell
# Knowage Version
docker images |grep knowagelabs |awk '{print $2}' |head -1 |cut -d- -f1
```

### Sevice

```shell
sudo docker  start | stop | restart | status knowage-server
sudo docker  start | stop | restart | status knowage-python
sudo docker  start | stop | restart | status knowage-r
sudo docker  start | stop | restart | status knowage-mariadb-server
sudo docker  start | stop | restart | status knowage-mariadb-cache
```

### CLI


### API

[Knowage API](https://knowage.docs.apiary.io) adopts the REST API 2.0 specification.   
The REST API is designed to manage the lifecycle of Knowage analytical documents and datasets.