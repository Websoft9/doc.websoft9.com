---
sidebar_position: 1
slug: /dolibarr
tags:
  - Dolibarr
  - CRM
  - 客户成功
---

# Dolibarr Getting Started

[Dolibarr](https://www.dolibarr.org/onlinedemo.php) is a software suite for small and micro enterprises, freelancers and other enterprises, which used for resource planning and customer relationship management. You can use one web suite to manage all of your business by Dolibarr Management SoftwareDiscourseDiscourse Reviews

![](http://libs.websoft9.com/Websoft9/DocsPicture/en/dolibarr/dolibarr-gui-websoft9.png)

If you have installed Websoft9 Dolibarr, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Dolibarr
4. [Get](./user/credentials) default username and password of Dolibarr

## Dolibarr Initialization

### Steps for you

1. Using local Chrome or Firefox to visit *http://domain* or *http://Internet IP*,access login page
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/dolibarr/dolibarr-init1-websoft9.png)

2. Input user and password ([do not know the account password?](./user/credentials)), click "login"

3. Dolibarr dashboard
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/dolibarr/dolibarr-backend-websoft9.png)

4. Go to “Home->Setup->Company/Foundation” and edit informations for company or foundation you want to manage.
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/dolibarr/dolibarr-setupcompany-websoft9.png)

> Refers to the [Dolibarr Documentation](https://docs.dolibarr.com/) to get start your Dolibarr tutorial

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## Dolibarr QuickStart

This task **Dolibarr builds enterprise CRM** is for your Dolibarr  QuickStart

## Dolibarr Setup

### Modules

Activation of modules is the second mandatory step. What modules you will activate depends on what you want to do with Dolibarr. In most cases, you may want to use all modules. You have to activate one by one each module you plan to use. For example, to manage a company, you might activate modules: Third party, Invoices and Products, but probably a lot of more modules.

To activate a module you want, go to page “Home->Setup->Modules” and click the button ‘on/off’ in the “Status” column to enable it.

![](http://libs.websoft9.com/Websoft9/DocsPicture/en/dolibarr/dolibarr-setupmodules-websoft9.png)



## Dolibarr reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Dolibarr 

Run `docker ps`, view all containers when Dolibarr  is running:

```bash
CONTAINER ID   IMAGE                         COMMAND                  CREATED          STATUS                    PORTS                                                                               NAMES                                                                                                gitlab-runner
ae306d549ced   tuxgasy/dolibarr:15.0.2       "docker-run.sh apach…"   28 minutes ago   Up 28 minutes             0.0.0.0:9002->80/tcp, :::9002->80/tcp                                               dolibarr
a8043dc3d226   mariadb:latest                "docker-entrypoint.s…"   28 minutes ago   Up 28 minutes             3306/tcp                                                                            dolibarr-db

```

### Path{#path}

Dolibarr installation directory: */data/apps/dolibarr*  
Dolibarr site directory: */data/apps/dolibarr/data/dolibarr_html*  
Dolibarr Documents Directory: */data/apps/dolibarr/data/dolibarr_documents*  

### Port{#port}

No special port

### Version{#version}

```
sudo docker images |grep tuxgasy/dolibarr |awk '{print $2}'
```

### Service{#service}

```shell
sudo docker start | stop | restart | stats dolibarr
sudo docker start | stop | restart | stats dolibarr-db
```

### CLI{#cli}

no

### API

[Module Web Services API REST](https://wiki.dolibarr.org/index.php?title=Module_Web_Services_API_REST_(developer))