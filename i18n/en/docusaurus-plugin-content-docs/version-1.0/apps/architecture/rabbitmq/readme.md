---
sidebar_position: 1
slug: /rabbitmq
tags:
  - RabbitMQ
  - IT Architecture
  - Broker
---

# RabbitMQ Getting Started

[RabbitMQ](https://rabbitmq-server.apache.org/) is the most widely deployed open source message broker. With more than 35,000 production deployments of RabbitMQ world-wide at small startups and large enterprises, RabbitMQ is the most popular open source message broker.

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/rabbitmq-gui-websoft9.png)  

If you have installed Websoft9 RabbitMQ, the following steps is for your quick start


## Preparation

1. Get the **Internet IP** on your Cloud Platform
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:15672** is allowed
3. **[Get](./user/credentials)** default username and password of RabbitMQ
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for RabbitMQ.

## RabbitMQ Initialization

### Steps for you

1. Using local Chrome or Firefox to visit the URL *http://DNS:15672* or *http://Internet IP:15672*, you will enter installation wizard of RabbitMQ
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/rabbitmq-login-websoft9.png)

2. Log in to RabbitMQ web console([Don't have password?](./user/credentials))  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/rabbitmq-bk-websoft9.png)

3. Set you new password from: 【Users】>【Admin】>【Permissions】>【Update this user】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/rabbitmq-pw-websoft9.png)

> More useful RabbitMQ guide, please refer to [RabbitMQ Documentation](https://www.rabbitmq.com/documentation.html)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## RabbitMQ QuickStart
  
This task【receives/ delivers Messages】 is for your RabbitMQ QuickStart:

## RabbitMQ Setup

The following is based on [RabbitMQ official documentation] (https://www.rabbitmq.com/documentation.html), distilling common operations for reference:  

### Create User

The user for RabbitMQ web console is also the user for RabbitMQ Server. You can use the default administrator user **admin** or create more by RabbitMQ web console

1. Use you local Chrome or Firefox to visit URL: *http://Internet IP:15672*, login to RabbitMQ console
2. Open the 【Admin】>【Add a user】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/rabbitmq-createuser-websoft9.png)
3. Set your username, password and tag(Role for RabbitMQ)

### Remote connection

You can use the local MQ tools to connect RabbitMQ server remote if you want. 
Following is using the [QueueExplorer](https://www.cogin.com/mq/index.php) to describe the steps for connection:

1. Download and install [QueueExplorer](https://www.cogin.com/mq/download.php)
2. Enable the **TCP:5672** and **TCP:15672** ports of your Security Group of your Cloud Platform
3. Open the QueueExplorer, fill the your credentials for RabbitMQ
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/queueexplorer-rabbtimq001-websoft9.png)
4. Connect successfully
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/queueexplorer-rabbtimq002-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/queueexplorer-rabbtimq003-websoft9.png)

### Config TLS/SSL

RabbitMQ config TLS/SSL, need following 4 steps：

1. Install tls-gen

```bash
git clone https://github.com/michaelklishin/tls-gen tls-gen
cd tls-gen/basic
# private key password
make PASSWORD=bunnies
make verify
make info
ls -l ./result
cp -r result/ /etc/rabbitmq/ssl/  
```

2. Add follow content into `/etc/rabbitmq/rabbitmq.config`

```
ssl_options.cacertfile = /etc/rabbitmq/ssl/ca_certificate.pem
ssl_options.certfile   = /etc/rabbitmq/ssl/server_certificate.pem
ssl_options.keyfile    = /etc/rabbitmq/ssl/server_key.pem
ssl_options.verify     = verify_peer
ssl_options.fail_if_no_peer_cert = false
```
3. Restart RabbitMQ service `systemctl restart rabbitmq`

4. Verification

```bash
rabbitmq-diagnostics listeners
```

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage RabbitMQ

Run `docker ps` command, view all Containers when RabbitMQ is running:

```bash
CONTAINER ID   IMAGE                      COMMAND                  CREATED          STATUS          PORTS                                                                                                                                                                                  NAMES
9b2d4c09de70   rabbitmq:3.10-management   "docker-entrypoint.s…"   37 minutes ago   Up 37 minutes   0.0.0.0:4369->4369/tcp, :::4369->4369/tcp, 5671/tcp, 0.0.0.0:5672->5672/tcp, :::5672->5672/tcp, 15671/tcp, 15691-15692/tcp, 0.0.0.0:15672->15672/tcp, :::15672->15672/tcp, 25672/tcp   rabbitmq
```

### Path{#path}
  
RabbitMQ installation directory:  * /data/apps/rabbitmq*  
RabbitMQ configuration directory:  */data/apps/rabbitmq/data/rabbitmq_config*  
RabbitMQ data directory:  */data/apps/rabbitmq/data/rabbitmq_data*  
  
### Port{#port}

| Port | Use                                          | Necessity |
| ------ | --------------------------------------------- | ------ |
| 15672 | HTTP requests for RabbitMQ Console| Required |
| 5672 | RabbitMQ connect Port | Optional |
| 4369 | Erlang distribution | Optional |

### Version{#version}

```shell
# RabbitMQ version
docker exec -i rabbitmq rabbitmqctl version
```

### Service{#service}

```shell
sudo docker start | stop | restart | stats rabbitmq
```

### CLI{#cli}

```
# RabbitMQ CLI
docker exec -it rabbitmq rabbitmqctl
```
  
### API

[Client Documentation](https://www.rabbitmq.com/dotnet-api-guide.html)