---
sidebar_position: 1
slug: /alfresco
tags:
  - Alfresco
  - Collaboration and Productivity
  - ERP
---


# Alfresco Getting Started

[Alfresco Community Edition](https://www.alfresco.com/ecm-software/alfresco-community-editions) is open source Enterprise Content Management software that handles any type of content, allowing users to easily share and collaborate on content.

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/alfresco/alfresco-arcgui-websoft9.png)

If you have installed Websoft9 Alfresco, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Alfresco
4. [Get](./user/credentials) default username and password of Alfresco


## Alfresco Initialization{#init}

### Steps for you

1. Use local browser to access: *http://DNS* or *http://Server's Internet IP*. You will enter Alfresco login page.
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/alfresco/alfresco-login-websoft9.png)

2. Log in Alfresco web console. ([Don't have password?](./user/credentials)) 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/alfresco/alfresco-consolegui-websoft9.png)

> More guide about Alfresco, please refer to [Alfresco Documentation](https://docs.alfresco.com/content-services/community/using/content).


### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

**502 error ! Alfresco service not start?**

Alfresco need 5-10 minutes for boot starting


## Alfresco QuickStart

Below is the useful screenshots of Alfresco: 

- Main dashboard
  ![Alfresco dashboard](http://libs.websoft9.com/Websoft9/DocsPicture/en/alfresco/alfresco-adminui-websoft9.png)

- My document
  ![Alfresco document](http://libs.websoft9.com/Websoft9/DocsPicture/en/alfresco/alfresco-mydocs-websoft9.png)

- Document share
  ![Alfresco Document share](http://libs.websoft9.com/Websoft9/DocsPicture/en/alfresco/alfresco-sharedocs-websoft9.png)

- Add user
  ![Alfresco Add user](http://libs.websoft9.com/Websoft9/DocsPicture/en/alfresco/alfresco-addusers-websoft9.png)

- Add group
  ![Alfresco Add group](http://libs.websoft9.com/Websoft9/DocsPicture/en/alfresco/alfresco-addgroup-websoft9.png)

- Workflow management
  ![Alfresco Workflow management](http://libs.websoft9.com/Websoft9/DocsPicture/en/alfresco/alfresco-workflow-websoft9.png)


## Alfresco Setup

### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console
   
2. Log in Alfresco Console, configure SMTP (Need more research)

### Resetting Password

here are two main measures to reset password.

**Changing password**

Take the steps below: 

1. Login Alfresco, open 【Administrator】>【My Profile】 
  ![Alfresco modify password](https://libs.websoft9.com/Websoft9/DocsPicture/en/alfresco/alfresco-modifypw-websoft9.png)

2. Click【Change your Password】, start to change the password.

**Forgot Password**

Try to retrieve your password through database table as below: 

1. Use **SSH** to connect Alfresco instances

2. Run the `psql` of Alfresco
   ```
   docker exec -it alfresco-postgres psql -U alfresco -d alfresco
   ```

3. Modify password by below SQL command (The new password is set to `admin`)
   ```
   UPDATE alf_node_properties SET string_value='209c6174da490caeb422f3fa5a7ae634' WHERE node_id=4 and qname_id=10
   ```

4. Exit the `psql` of PostgreSQL, then restart all containers
   ```
   cd /data/wwwroot/alfresco
   docker-compose restart
   ```

## Reference sheet{#parameter}

 The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Alfresco


```bash
CONTAINER ID   IMAGE                                                  COMMAND                  CREATED             STATUS             PORTS                                                                                                                                                                                NAMES
3d2afa8a1cc7   alfresco/alfresco-acs-nginx:3.1.1                      "/entrypoint.sh"         About an hour ago   Up About an hour   80/tcp, 0.0.0.0:8080->8080/tcp, :::8080->8080/tcp                                                                                                                                    alfresco-proxy
b42251c78a71   alfresco/alfresco-search-services:2.0.1                "/bin/sh -c '$DIST_D…"   About an hour ago   Up About an hour   10001/tcp, 0.0.0.0:8083->8983/tcp, :::8083->8983/tcp                                                                                                                                 alfresco-solr6
a381a9646f4b   alfresco/alfresco-transform-core-aio:2.3.10            "/bin/sh -c 'java $J…"   About an hour ago   Up About an hour   0.0.0.0:8090->8090/tcp, :::8090->8090/tcp                                                                                                                                            alfresco-transform
af14e4d3cd86   alfresco/alfresco-content-repository-community:7.0.0   "catalina.sh run -se…"   About an hour ago   Up About an hour   8000/tcp, 8080/tcp, 10001/tcp                                                                                                                                                        alfresco-content
50059f56edff   postgres:13.1                                          "docker-entrypoint.s…"   About an hour ago   Up About an hour   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp                                                                                                                                            alfresco-postgres
692e2acf019d   alfresco/alfresco-activemq:5.16.1                      "/bin/sh -c '${ACTIV…"   About an hour ago   Up About an hour   0.0.0.0:5672->5672/tcp, :::5672->5672/tcp, 0.0.0.0:8161->8161/tcp, :::8161->8161/tcp, 0.0.0.0:61613->61613/tcp, :::61613->61613/tcp, 0.0.0.0:61616->61616/tcp, :::61616->61616/tcp   alfresco-activemq
ca3a6baf750e   alfresco/alfresco-share:7.0.0                          "/usr/local/tomcat/s…"   About an hour ago   Up About an hour   8000/tcp, 8080/tcp                                                                                                                                                                   alfresco-share
4a0c8d7e6c2e   dpage/pgadmin4                                         "/entrypoint.sh"         About an hour ago   Up About an hour   443/tcp, 0.0.0.0:9090->80/tcp, :::9090->80/tcp                                                                                                                                       pgadmin
```


### Path{#path}

Alfresco Install Directory： */data/apps/alfresco*  
Alfresco Data Directory： */data/apps/alfresco/data/alfresco* 

### Port{#port}

No special port


### Version{#version}

```shell
docker images |grep alfresco-share |awk '{print $2}'
```

### Service{#service}

```shell
sudo docker-compose start | stop | restart alfresco
```

### CLI{#cli}

暂未发现

### API

[ReST API Guide](https://docs.alfresco.com/content-services/latest/develop/rest-api-guide/)

