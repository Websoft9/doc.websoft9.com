---
sidebar_position: 1
slug: /elk
tags:
  - ELK Stack
  - Data Analysis
---

# ELK Stack Getting Started

[ELK](https://elk-server.apache.org/) is the most widely deployed open source message broker. With more than 35,000 production deployments of ELK world-wide at small startups and large enterprises, ELK is the most popular open source message broker.

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-gui-websoft9.gif)

If you have installed Websoft9 ELK Stack, the following steps is for your quick start


## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for ELK Stack
4. [Get](./user/credentials) default username and password of ELK Stack
5. Log in the cloud server, run the following command, pull the ELK-related Docker image and start the container


   ```
   cd /data/wwwroot/elk && docker-compose pull && docker-compose up -d
   ```

   > The Elastic Open Source License does not allow third-party distribution, but allows users to use it for free. Therefore, if you use this solution to deploy Elastic, you should first execute the above command to pull the Elastic image yourself.  


## ELK Stack Initialization

### Steps for you

1. Use local Chrome or Firefox to access the URL *http://DNS* You will enter installation wizard of ELK.
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-login-websoft9.png)

2. Log in ELK web console. ([Don't have password?](./user/credentials)) 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-bkreminder-websoft9.png)

3. Set you new password from: 【Users】>【Admin】>【Permissions】>【Update this user】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-dashboard-websoft9.png)

> More guide about ELK, please refer to [ELK Documentation](https://www.elk.com/documentation.html).

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.   


## ELK Stack QuickStart

ELK supports a variety of data sources, here we use the common logs file as an input to Logstash as an example, the steps are as follows:  

1. Set the index "mytest" in [Logstash configuration file](#path) and restart the container  

   ```
   input{
      file{
         path => "/var/log/yum.log"
         type => "elasticsearch"
         start_position => "beginning"
      }
   }

   output {
      elasticsearch {
         hosts => "elasticsearch:9200"
         user => "elastic"
         password => "xxxxx"
                  index => "mytest"
      }
   }
   ```

   ```
   cd /data/wwwroot/elk
   docker-compose down
   docker-compose up -d
   ```

2. Verify that Elasticsearch and Logstash are successfully connected and that the index data is valid (verified by URL: http:// server public IP: 9200/cat/indices?v)  

  ![ELK 验证](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizardindex-websoft9.png)

3. Log in to Kibana, click [Manage], and then click [Index Patterns] in the right menu  

  ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard1-websoft9.png)

  ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard2-websoft9.png)

  ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard3-websoft9.png)

4. Search for "mytest" and follow the prompts to complete the creation  

  ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard4-websoft9.png)

  ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard5-websoft9.png)

5. The index is created successfully in Kibana, and you can retrieve data here with a timestamp  

  ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard6-websoft9.png)

  ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard7-websoft9.png)

## ELK Stack Setup

### Connecting Logstash to Elasticsearch

As the data collector, how does Logstash transfer data to Elasticsearch?  

1. Edit [Logstash Confiugration file](#path)

2. Add a new pipeline configuration file:  
   ```
   input{
      file{
         path => "/var/log/*.log"
         type => "elasticsearch"
         start_position => "beginning"
      }
   }

   ## Add your filters / logstash plugins configuration here

   output {
      elasticsearch {
         hosts => "elasticsearch:9200"
         user => "elastic"
         password => "elastic123"
                  index => "mytest"
      }
   }
   ```

  > **output** in the configuration requires the database connection account of Elasticsearch.  

### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console

2. Log in ELK Console.
3. Enter the SMTP settings.
![Metabase SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-smtp-websoft9.png)
4. Click the **Test Connection**. You will get the feedback *"no errors were..."* if SMTP is valid.

### Reset Password

There are two main measures to reset password.

**Changing password**

Log in to Kibana and click User Profile in the upper right corner of the user icon to change the password  

**Forgot Password**

If you forget your password, you can reset it by rerunning the container:  

```
cd /data/wwwroot/elk
docker-compose down && docker-compose up -d
```

The **DB_ES_PASSWORD** variable in the `.env` file is the password after the reset


## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage ELK

Run `docker ps` command, view all Containers when ELK is running:  

```
CONTAINER ID   IMAGE                  COMMAND                  CREATED         STATUS         PORTS                                                                                                                                                                        NAMES
4c27ee6b8e98   logstash:7.13.4        "/usr/local/bin/dock…"   4 minutes ago   Up 4 minutes   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp, 0.0.0.0:5044->5044/tcp, :::5044->5044/tcp, 0.0.0.0:9600->9600/tcp, 0.0.0.0:5000->5000/udp, :::9600->9600/tcp, :::5000->5000/udp   elk-logstash
babdf8193e8d   kibana:7.13.4          "/bin/tini -- /usr/l…"   4 minutes ago   Up 4 minutes   0.0.0.0:9001->5601/tcp, :::9001->5601/tcp                                                                                                                                    elk-kibana
de14eb80b9f9   elasticsearch:7.13.4   "/bin/tini -- /usr/l…"   4 minutes ago   Up 4 minutes   0.0.0.0:9200->9200/tcp, :::9200->9200/tcp, 0.0.0.0:9300->9300/tcp, :::9300->9300/tcp
```


### Path{#path}

The ELK Stack consists of components such as Elasticsearch, Kibana, Logstash, etc  

ELK installation directory： */data/apps/elk*  
ELK configuration directory： */data/apps/elk/src*  
Logstash configuration file： */data/apps/elk/src/logstash/pipelinelogstash.conf*  
Kibana configuration file： */data/apps/elk/src/kibana/config/kibana.yml*   
Elasticsearch configuration file： */data/apps/elk/src/elasticsearch/config/elasticsearch.yml*  

### Port{#port}

| Port | Use                                         | Necessity |
| ------ | -------------------------------------------- | ------ |
| 9200   | Elasticsearch HTTP | Required  |
| 9600   | Logstash API | Optional   |

### Version

```shell
docker exec -it elk-elasticsearch bin/elasticsearch --version
```

### Service

```shell
sudo docker  start | stop | restart | status elk-elasticsearch
sudo docker  start | stop | restart | status elk-logstash
sudo docker  start | stop | restart | status elk-kibana
```

### CLI

[SQL CLI](https://www.elastic.co/guide/en/elasticsearch/reference/current/sql-cli.html)

### API

[ELK API](https://www.elastic.co/guide/en/elasticsearch/reference/current/http-clients.html) adopts the REST API 2.0 specification.
