---
sidebar_position: 1
slug: /rocketmq
tags:
  - RocketMQ
  - IT Architecture
  - Broker
---

# RocketMQ Getting Started

[RocketMQ](http://rocketmq.apache.org/) is a distributed open source message queuing system developed by Alibaba, and it is a distributed message middleware with low latency, high concurrency, high availability and high reliability.

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/rocketmq/rocketmq-console-websoft9.png)  

If you have installed Websoft9 RocketMQ, the following steps is for your quick start


## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:9876** is allowed
3. **[Get](./user/credentials)** default username and password of RocketMQ
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for RocketMQ

## RocketMQ Initialization

### Steps for you

1. Use **SSH** to connect RocketMQ and run the following commands to check for the status of RocketMQ
   ```
   sudo systemctl status mqnamesrv
   sudo systemctl status mqbroker
   ```
2. Use local Chrome or Firefox to access [RocketMQ-Console](#gui) to verify more
   ![RocketMQ-Console](https://libs.websoft9.com/Websoft9/DocsPicture/en/rocketmq/rocketmq-console-websoft9.png)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## RocketMQ QuickStart{#start}

This chapter we will introduce a details for you how to use RocketMQ to send messages (producer) and consume messages(consumer)  

1. Explain the tools or procedures required for the experiment

   * producer: */data/rocketmq/bin/tools.sh*
   * consumer: */data/rocketmq/bin/tools.sh*
   * Messages: produce from the Java Class `org.apache.rocketmq.example.quickstart.Producer`  
   * Messages storage:  **RabbitMQ Broker**
   * Message order management: **NAMESRV_ADDR** 

2. Use **SSH** to connect RocketMQ Server, run the following command to send message as producer.
   ```
   export NAMESRV_ADDR=localhost:9876
   cd /data/rocketmq/bin
   sh tools.sh org.apache.rocketmq.example.quickstart.Producer
   ```

3. You can see the feedback message *SendResult [sendStatus=SEND_OK, msgId= ...* when send successfully

4. Run the following command to send message as consumer.
   ```
   cd /data/rocketmq/bin
   sh tools.sh org.apache.rocketmq.example.quickstart.Consumer
   ```
5. You can see the feedback message *ConsumeMessageThread_%d Receive New Messages: [MessageExt...* when receive successfully

6. Login to GUI tool [RocketMQ-Console](#gui) to query more information
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/rocketmq/rocketmq-send-websoft9.png)

> More guide about RocketMQ, please refer to [RocketMQ Documentation](http://rocketmq.apache.org/docs/quick-start/).

## RocketMQ Setup

### Message sample

Refer to the docs[RocketMQ QuickStart](#start) to send message and receive message

### Web-based GUI{#gui}

RocketMQ external project have Web-based GUI tool [RocketMQ-Console-NG ](https://github.com/apache/rocketmq-externals/tree/master/rocketmq-console) to manage RocketMQ, this deployment solution have installed by default.  

1. Use local Chrome or Firefox to access the URL: *http://Server's Internet IP:9003* to it
   ![RocketMQ-Console-NG login](https://libs.websoft9.com/Websoft9/DocsPicture/en/rocketmq/rocketmq-loginonly-websoft9.png)

2. Log in RocketMQ-Console-Ng console ([Don't have password?](./user/credentials)) and enter to the console interface.  
   ![RocketMQ-Console-NG](https://libs.websoft9.com/Websoft9/DocsPicture/en/rocketmq/rocketmq-console-websoft9.png)

3. Set your language
   ![RocketMQ-Console language](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketmq/rocketmq-language-websoft9.png)

4. You can refer to official docs [UserGuide](https://github.com/apache/rocketmq-externals/blob/master/README.md) for more experience
   ![RocketMQ-Console-NG](https://libs.websoft9.com/Websoft9/DocsPicture/en/rocketmq/rocketmq-error-websoft9.png)

### Modify the password of RocketMQ-Console

Modify the password for the file:*/etc/nginx/.htpasswd/htpasswd.conf* and restart Nginx service

### 修改 RocketMQ 运行内存

分别修改如下两个配置文件：

* *rocketmq/bin/runserver.sh* 文件中 Java 启动内存大小（非必要）
* */data/rocketmq/bin/runbroker.sh* 文件中 Java 启动内存大小（非必要）

## Reference sheet

The RocketMQ deployment package contains Nginx, Docker, etc. The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage RocketMQ   

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```

### Path{#path}
  
RocketMQ installation directory: */data/rocketmq*  
RocketMQ logs directory: */data/logs/rocketmq*  
RocketMQ configuration file: */data/config/rocketmq* 
  
### Port{#port}

| Port | Use                                          | Necessity |
| ------ | --------------------------------------------- | ------ |
| 9003 | HTTP to access RocketMQ-Console-Ng | Optional |
| 9876 | RocketMQ Broker Server | Required |

### Version{#version}

```shell
ls /data/rocketmq/lib |grep rocketmq-broker
```

### Service{#service}

```shell
sudo systemctl start | stop | restart | status mqnamesrv
sudo systemctl start | stop | restart | status mqbroker

sudo docker start | stop | restart | status rocketmq-console

```

### CLI{#cli}

RocketMQ provides a powerful cli tool `mqadmin`  

```
$ mqadmin 
The most commonly used mqadmin commands are:
   updateTopic          Update or create topic
   deleteTopic          Delete topic from broker and NameServer.
   updateSubGroup       Update or create subscription group
   deleteSubGroup       Delete subscription group from broker.
   updateBrokerConfig   Update broker's config
   updateTopicPerm      Update topic perm
   topicRoute           Examine topic route info
   topicStatus          Examine topic Status info
   topicClusterList     get cluster info for topic
   brokerStatus         Fetch broker runtime status data
   queryMsgById         Query Message by Id
   queryMsgByKey        Query Message by Key
   queryMsgByUniqueKey  Query Message by Unique key
   queryMsgByOffset     Query Message by offset
   QueryMsgTraceById    query a message trace
   printMsg             Print Message Detail
   printMsgByQueue      Print Message Detail
   sendMsgStatus        send msg to broker.
   brokerConsumeStats   Fetch broker consume stats data
   producerConnection   Query producer's socket connection and client version
   consumerConnection   Query consumer's socket connection, client version and subscription
   consumerProgress     Query consumers's progress, speed
   consumerStatus       Query consumer's internal data structure
   cloneGroupOffset     clone offset from other group.
   clusterList          List all of clusters
   topicList            Fetch all topic list from name server
   updateKvConfig       Create or update KV config.
   deleteKvConfig       Delete KV config.
   wipeWritePerm        Wipe write perm of broker in all name server
   resetOffsetByTime    Reset consumer offset by timestamp(without client restart).
   updateOrderConf      Create or update or delete order conf
   cleanExpiredCQ       Clean expired ConsumeQueue on broker.
   cleanUnusedTopic     Clean unused topic on broker.
   startMonitoring      Start Monitoring
   statsAll             Topic and Consumer tps stats
   allocateMQ           Allocate MQ
   checkMsgSendRT       check message send response time
   clusterRT            List All clusters Message Send RT
   getNamesrvConfig     Get configs of name server.
   updateNamesrvConfig  Update configs of name server.
   getBrokerConfig      Get broker config by cluster or special broker!
   queryCq              Query cq command.
   sendMessage          Send a message
   consumeMessage       Consume message
   updateAclConfig      Update acl config yaml file in broker
   deleteAccessConfig   Delete Acl Config Account in broker
   clusterAclConfigVersion List all of acl config version information in cluster
   updateGlobalWhiteAddr Update global white address for acl Config File in broker
   getAccessConfigSubCommand List all of acl config information in cluster

See 'mqadmin help <command>' for more information on a specific command.
```

### API