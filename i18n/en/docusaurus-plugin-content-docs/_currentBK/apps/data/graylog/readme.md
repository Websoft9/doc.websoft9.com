---
sidebar_position: 1
slug: /graylog
tags:
  - Graylog
  - Data Analysis
  - Log Management
---

# Graylog Getting Started

[Graylog](https://graylog.org) is on a mission to make Log Management and SIEM easier, faster, more affordable, and more effective. 

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/graylog/graylog-gui-websoft9.png)

If you have installed Websoft9 Graylog, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Graylog
4. [Get](./user/credentials) default username and password of Graylog

## Graylog Initialization

### Steps for you

1. Using local Chrome or Firefox to visit the URL *http://DNS* or *http://Server's Internet IP*, you can see the login page of Graylog.
   ![login Graylog websoft9](https://libs.websoft9.com/Websoft9/DocsPicture/en/graylog/graylog-login-websoft9.png)

2. Input the login account and enter to Graylog Console([Don't have password?](./user/credentials))  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/graylog/graylog-console-websoft9.png)

3. if you want to bind domain for Graylog, refer to [here](./administrator/domain_step)

> More useful Graylog guide, please refer to [Configuring Graylog](https://docs.graylog.org/en/latest/pages/configuration.html)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## Graylog QuickStart

正在编写

## Graylog Setup

### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console

2. Refer to [Official email setting](https://docs.graylog.org/en/3.3/pages/configuration/server.conf.html#email) by editing the email Graylog configuration file: */etc/graylog/server/server.conf*

3. Modify the items **[transport_email](https://docs.graylog.org/en/3.3/pages/configuration/server.conf.html#email)**  of Graylog configuration file

4. Restart Graylog service
   ```
   sudo docker restart graylog
   ```

### Reset Password

Try to reset your password if you can't use email to reset it:

1. Use SSH tool to login Server, then run the below commands
   ```
   new_password=admin123@graylog
   sha_password=$(echo -n $new_password | sha256sum | awk '{ print $1 }')
   sudo sed -i "s/8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918/$sha_password/g" /data/wwwroot/graylog/.env
   ```

2. You new password is `admin123@graylog` now after docker-compose recreate
   ```
   cd /data/wwwroot/graylog && sudo docker-compose up -d
   ```

> You can set the new_password to any string if you want

### Configure Graylog

Every [configuration option](https://docs.graylog.org/docs/server-conf) can be set via environment variables.. Simply prefix the parameter name with **GRAYLOG_** and put it all in upper case.  

For example, setting up the SMTP configuration for sending Graylog alert notifications via email, the **docker-compose.yml** would look like this:  

```
version: '2'
  services:
    mongo:
      image: "mongo:4.2"
      # Other settings [...]
    elasticsearch:
      image: docker.elastic.co/elasticsearch/elasticsearch-oss:7.10.2
      # Other settings [...]
    graylog:
      image: graylog/graylog:4.2
      # Other settings [...]
      environment:
        GRAYLOG_TRANSPORT_EMAIL_ENABLED: "true"
        GRAYLOG_TRANSPORT_EMAIL_HOSTNAME: smtp
        GRAYLOG_TRANSPORT_EMAIL_PORT: 25
        GRAYLOG_TRANSPORT_EMAIL_USE_AUTH: "false"
        GRAYLOG_TRANSPORT_EMAIL_USE_TLS: "false"
        GRAYLOG_TRANSPORT_EMAIL_USE_SSL: "false"
```

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Graylog


Run `docker ps` command, view all Containers when Graylog is running:

```
CONTAINER ID   IMAGE                                                  COMMAND                  CREATED              STATUS                        PORTS                                                                                                                                                                                                                           NAMES
aba3f411351a   websoft9dev/mongocompass:v1.31                         "/dockerstartup/kasm…"   39 seconds ago       Up 37 seconds                 4901/tcp, 5901/tcp, 0.0.0.0:9091->6901/tcp, :::9091->6901/tcp                                                                                                                                                                   mongocompass
8285b315009a   graylog/graylog:4.3                                    "/usr/bin/tini -- wa…"   About a minute ago   Up About a minute (healthy)   0.0.0.0:1514->1514/tcp, 0.0.0.0:1514->1514/udp, :::1514->1514/tcp, :::1514->1514/udp, 0.0.0.0:12201->12201/tcp, 0.0.0.0:12201->12201/udp, :::12201->12201/tcp, :::12201->12201/udp, 0.0.0.0:9001->9000/tcp, :::9001->9000/tcp   graylog
7795d2333c74   docker.elastic.co/elasticsearch/elasticsearch:7.16.3   "/bin/tini -- /usr/l…"   About a minute ago   Up About a minute             9200/tcp, 9300/tcp                                                                                                                                                                                                              graylog-elasticsearch
04dc27b0962c   mongo:4.2                                              "docker-entrypoint.s…"   About a minute ago   Up About a minute             27017/tcp                                          "docker-entrypoint.s…"   8 minutes ago   Up 3 minutes             0.0.0.0:9091->1234/tcp, :::9091->1234/tcp                                                                                                                                                                                       adminmongo
```

### Path{#path}

Graylog installation directory::  */data/apps/graylog*  
Graylog data directory:  */data/apps/graylog/data/graylog/graylog_data*  
Graylog plugin directory:  */data/apps/graylog/data/graylog/graylog_plugin*  

### Port{#port}

No special port

### Version

```shell
# Graylog Version
docker images |grep graylog/graylog |awk '{print $2}'
```

### Service

```shell
sudo docker  start | stop | restart | status graylog
sudo docker  start | stop | restart | status graylog-mongo
sudo docker  start | stop | restart | status graylog-elasticsearch
sudo docker  start | stop | restart | status mongocompass
```

### CLI


### API

[Graylog API] (https://docs.graylog.org/v1/docs/rest-api) Using the REST API 2.0 specification, even the Graylog web interface specifically uses the Graylog REST API to interact with the Graylog cluster.

API access mode: *https://IP/api/api-browser/global/index.html*, without /global/index.html is inaccessible.
