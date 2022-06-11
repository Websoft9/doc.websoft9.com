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

   > Elastic 开源版 License 不允许第三方的分发行为，但允许用户免费使用，所以拉取镜像的动作由用户自行操作。


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

ELK 的数据源多种多样，这里用常见的logs file为 Logstash 的输入为例，步骤如下：

1. 在 [Logstash 的配置文件](#path)中设置索引"mytest"，并重启容器
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

2. 验证 Elasticsearch 和 Logstash 是否成功连接，索引数据是否生效(通过 URL 验证：http://服务器公网 IP:9200/cat/indices?v)

  ![ELK 验证](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizardindex-websoft9.png)

3. 登陆 Kibana，点击【Manage】，再点击右侧菜单的【Index Patterns】

  ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard1-websoft9.png)

  ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard2-websoft9.png)

  ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard3-websoft9.png)

4. 检索"mytest"，根据提示完成创建

  ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard4-websoft9.png)

  ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard5-websoft9.png)

5. 索引在 Kibana 创建成功，可以用时间条件在此检索数据

  ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard6-websoft9.png)

  ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard7-websoft9.png)

## ELK Stack Setup

### Connecting Logstash to Elasticsearch

Logstash 作为数据的采集者，它是如何将数据传输到 Elasticsearch 这个数据存储中的呢？

1. 编辑 [Logstash 配置文件](#path)

2. 新增一个 pipeline 的配置文件，其内容如下：
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

  > 以上配置段中的 **output** 需要使用 elasticsearch 的数据库连接账号。

### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console

2. Log in ELK Console.
3. Enter the SMTP settings.
![Metabase SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-smtp-websoft9.png)
4. Click the **Test Connection**. You will get the feedback *"no errors were..."* if SMTP is valid.

### Reset Password

There are two main measures to reset password.

**Changing password**

登录 Kibana 后，右上角用户图标的【用户配置文件】即可修改密码

**Forgot Password**

如果用户忘记了密码，需通过重新运行容器的方式重置密码：

```
cd /data/wwwroot/elk
docker-compose down && docker-compose up -d
```

`.env`文件中的 **DB_ES_PASSWORD** 变量即重置后的密码


## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage ELK

通过运行`docker ps`，可以查看到 ELK 运行时所有的 Container：

```
CONTAINER ID   IMAGE                  COMMAND                  CREATED         STATUS         PORTS                                                                                                                                                                        NAMES
4c27ee6b8e98   logstash:7.13.4        "/usr/local/bin/dock…"   4 minutes ago   Up 4 minutes   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp, 0.0.0.0:5044->5044/tcp, :::5044->5044/tcp, 0.0.0.0:9600->9600/tcp, 0.0.0.0:5000->5000/udp, :::9600->9600/tcp, :::5000->5000/udp   elk-logstash
babdf8193e8d   kibana:7.13.4          "/bin/tini -- /usr/l…"   4 minutes ago   Up 4 minutes   0.0.0.0:9001->5601/tcp, :::9001->5601/tcp                                                                                                                                    elk-kibana
de14eb80b9f9   elasticsearch:7.13.4   "/bin/tini -- /usr/l…"   4 minutes ago   Up 4 minutes   0.0.0.0:9200->9200/tcp, :::9200->9200/tcp, 0.0.0.0:9300->9300/tcp, :::9300->9300/tcp
```

下面仅列出 ELK 本身的参数：

### Path{#path}

ELK Stack 包含：Elasticsearch, Kibana, Logstash 等组件

ELK installation directory： */data/wwwroot/elk*  
ELK 配置目录： */data/wwwroot/elk/src*  
ELK 配置容器配置文件： */data/wwwroot/elk/.env*  

Logstash 配置文件： */data/wwwroot/elk/src/logstash/pipelinelogstash.conf*  
Kibana 配置文件： */data/wwwroot/elk/src/kibana/config/kibana.yml*   
Elasticsearch 配置文件： */data/wwwroot/elk/src/elasticsearch/config/elasticsearch.yml*  

### Port{#port}

| 端口号 | 用途                                         | 必要性 |
| ------ | -------------------------------------------- | ------ |
| 9001   | kibana 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |
| 9200   | Elasticsearch HTTP | 可选   |
| 9300   | Elasticsearch TCP | 可选   |
| 9600   | Logstash API | 可选   |
| 5000   | Logstash TCP | 可选   |
| 5044   | Logstash TCP	 | 可选   |

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

[ELK API](https://www.elastic.co/guide/en/elasticsearch/reference/current/http-clients.html) 采用 REST API 2.0 规范。
