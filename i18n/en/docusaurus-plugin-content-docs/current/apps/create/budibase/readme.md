---
sidebar_position: 100
slug: /budibase
tags:
  - Low Code
  - Budibase
---

# Budibase Getting Started

[Budibase](https://budibase.com/) is an all-in-one low-code platform for building, designing, and automating business apps, such as; admin panels, forms, internal tools, client portals, and more. With Budibase, building CRUD apps takes minutes.

![Budibase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/budibase/budibase-main-websoft9.png)

If you have installed Websoft9 Budibase, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:9001,80** is allowed
3. Connect your Server and get **[default username and password](./user/credentials)** of Budibase
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Budibase

## Budibase Initialization

### Steps for you

1. Using local browser to visit the URL *http://DNS* or *http://Server's Internet IP*, you will enter initial wizard of Budibase

2. Register an administrator user
   
  ![Budibase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/budibase/budibase-installadmin-websoft9.png)

3. Log in and create an app

  ![Budibase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/budibase/budibase-createapp-websoft9.png)

4. Build applications: Budibuse builds applications from three aspects: Data, Design and Automate

  ![Budibase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/budibase/budibase-editapp-websoft9.png)

   - Data: Manage data sources, support building tables within Budibase for data modeling, and also support connecting to external data sources
   - Design: Page design, Budibase provides rich controls to build pages, and data controls are used for data binding and rendering
   - Automate: used to automate the design process, trigger conditions support data changes, Webhook, App Action and Cron
  
  ![Budibase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/budibase/budibase-automation-websoft9.png)

5. Data ： Based on Budibase for data modeling, create a new table Product , create a table structure through create column and create row, and add data records

  ![Budibase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/budibase/budibase-budibase-datasoure-websoft9.png)

  ![Budibase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/budibase/budibase-createtabel-websoft9.png)

  ![Budibase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/budibase/budibase-createrow-websoft9.png)

  **Using external data sources**
  
  ![Budibase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/budibase/budibase-datasource-websoft9.png)

6. Design ：use data controls to display data on the page, add a Data Provider control to the page, specify a data source, add a Table control, and bind the data source
   
  ![Budibase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/budibase/budibase-dataprovider-websoft9.png)

  ![Budibase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/budibase/budibase-datatable-websoft9.png)

**Control management: Select the control to manage the control in the left structure tree**

  ![Budibase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/budibase/budibase-element-amdin-websoft9.png)

**Budibase also supports the automatic generation of pages based on the data table, the generation of pages based on the addition, deletion and modification of the data table to realize the CURD of the data, refer to [Automatically generate pages](#quickstart)**

7. App preview: View the running effect of the program through the preview button
  
  ![Budibase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/budibase/budibase-app-preview-websoft9.png)

  ![Budibase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/budibase/budibase-app-view-websoft9.png)

8. App publish: After the application is created, publish the application through publish, and open the application through the application address 

  ![Budibase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/budibase/budibase-app-publish-websoft9.png)
. 

For more information, refer to  [official documentation](https://docs.budibase.com/docs/what-is-budibase)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  



## Budibase QuickStart

The following takes **Budibase automatically generates a data management system based on data tables** as a task to help users get started quickly:

1. Log in to Budibase and create a new app

  ![Budibase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/budibase/budibase-createapp-websoft9.png)

2. Based on Budibase for data modeling, create a new table Product 

  ![Budibase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/budibase/budibase-budibase-datasoure-websoft9.png)

  ![Budibase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/budibase/budibase-createtabel-websoft9.png)

  ![Budibase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/budibase/budibase-createrow-websoft9.png)

3. Generate the Product table management pages
   
  ![Budibase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/budibase/budibase-Autogenerated-screens-websoft9.png)

  ![Budibase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/budibase/budibase-Autogenerated-screens2-websoft9.png)

  ![Budibase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/budibase/budibase-Autogenerated-screens3-websoft9.png)

4. App preview
  
  ![Budibase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/budibase/budibase-Autogenerated-screens4-websoft9.png)


Refer to: [Official Documentation](https://docs.budibase.com/docs/quickstart-tutorials)


## Budibase Setup


## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Budibase

Run `docker ps`, view all containers when Budibase is running:  

```bash
CONTAINER ID   IMAGE                                      COMMAND                  CREATED          STATUS                              PORTS                                                 NAMES
0afe6a318523   budibase/proxy                             "/docker-entrypoint.…"   10 seconds ago   Up 8 seconds                        80/tcp, 0.0.0.0:9001->10000/tcp, :::9001->10000/tcp   budibase
ee8697b38071   budibase.docker.scarf.sh/budibase/apps     "docker-entrypoint.s…"   11 seconds ago   Up 9 seconds                        4001/tcp                                              budibase-bbapps
049c4009ef05   budibase.docker.scarf.sh/budibase/worker   "docker-entrypoint.s…"   11 seconds ago   Up 10 seconds                       4001/tcp                                              budibase-bbworker
b0ad03c4dc2d   curlimages/curl                            "/entrypoint.sh sh -…"   12 seconds ago   Exited (2) Less than a second ago                                                         docker-budibase_c                              ouch-init_1
c2b2cda7fda6   ibmcom/couchdb3                            "/docker-entrypoint.…"   14 seconds ago   Up 11 seconds                       4369/tcp, 5984/tcp, 9100/tcp                          budibase-couchdb
23c858bb3a59   redis                                      "docker-entrypoint.s…"   14 seconds ago   Up 12 seconds                       6379/tcp                                              budibase-redis
329b78c6506f   containrrr/watchtower                      "/watchtower --debug…"   14 seconds ago   Up 11 seconds                       8080/tcp                                              docker-budibase_w                              atchtower-service_1
45ef54d75f35   minio/minio                                "/usr/bin/docker-ent…"   14 seconds ago   Up 12 seconds (health: starting)    9000/tcp                                              budibase-minio

```

### Path{#path}

Budibase : /data/apps/budibase

### Port{#port}

In addition to common ports such as 80, 443, etc., the following ports may be used:

| Port | Use                                          | Necessity |
| ------ | --------------------------------------------- | ------ |
| 9001   | Budibase original port	 | Optional   |

### Version {#version}

docker inspect budibase | grep com.docker.compose.version

### Service {#service}

```shell
sudo docker start | stop | restart | status budibase
```

### CLI {#cli}

### API {#api}

Refer to :[API Reference](https://docs.budibase.com/docs/public-api)