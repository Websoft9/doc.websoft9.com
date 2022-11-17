---
sidebar_position: 100
slug: /akeneo
tags:
  - Akeneo
---

# Akeneo Getting Started

[Akeneo](https://www.akeneo.com/) is an open source Product Experience Management (PXM) and Product Information Management (PIM) software product. Helps merchants and brands deliver engaging customer experiences across all sales channels, improve product data quality, and simplify product catalog management. Using Akeneo as product infrastructure management can transform business models and reduce product enrichment costs.

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/akeneo/akeneo-main-websoft9.png)

If you have installed Websoft9 Akeneo, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Connect your Server and get **[default username and password](./user/credentials)** of Akeneo
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Akeneo

## Akeneo Initialization

### Steps for you

1. Using local browser to visit the URL *http://DNS* or *http://Server's Internet IP*, you will enter initial wizard of Akeneo
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/akeneo/akeneo-login-websoft9.png)

2. login to your Akeneo([Don't have password?](./user/credentials))
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/akeneo/akeneo-product-websoft9.png)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## Akeneo QuickStart

The following takes **Akeneo data import and export** as a task to help users get started quickly:

For details, please refer to [Akeneo Data Import and Export](https://docs.akeneo.com/6.0/import_and_export_data/index.html)

## Akeneo Setup

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Akeneo

Run `docker ps`, view all containers when Akeneo is running:  

```bash
CONTAINER ID   IMAGE                                                      COMMAND                  CREATED         STATUS         PORTS                                                  NAMES
7d46c77c8bc7   phpmyadmin:latest                                          "/docker-entrypoint.…"   6 minutes ago   Up 6 minutes   0.0.0.0:9090->80/tcp, :::9090->80/tcp                  phpmyadmin
db9a7668dad3   websoft9dev/akeneo:latest                                  "/entrypoint.sh /usr…"   7 minutes ago   Up 6 minutes   0.0.0.0:9001->80/tcp, :::9001->80/tcp                  akeneo
6ecce79ee4c1   mysql:8.0                                                  "docker-entrypoint.s…"   7 minutes ago   Up 6 minutes   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   akeneo-mysql
8ea176b3bf04   docker.elastic.co/elasticsearch/elasticsearch-oss:7.10.1   "/tini -- /usr/local…"   7 minutes ago   Up 6 minutes   0.0.0.0:9200->9200/tcp, :::9200->9200/tcp, 9300/tcp    akeneo-elasticsearch
```

### Path{#path}

Akeneo installation directory: */data/apps/akeneo*  
Akeneo configuration file: */data/apps/akeneo/000-default.conf*  
Akeneo Site Directory: */data/apps/akeneo/data/akeneo*     

### Port{#port}

In addition to common ports such as 80, 443, etc., the following ports may be used:

No special port

### Version {#version}

```
docker exec -i akeneo  grep "pim-community-dev/tree" /var/www/html/composer.lock |awk -F"/v" '{print $2}'
```

### Service {#service}

```shell
sudo docker start | stop | restart | stats akeneo
sudo docker start | stop | restart | stats akeneo-elasticsearch
sudo docker start | stop | restart | stats akeneo-mysql
```

### CLI {#cli}

No

### API {#api}

Akeneo adopts the [REST API](https://api.akeneo.com/documentation/introduction.html) specification.