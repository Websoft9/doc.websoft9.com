---
sidebar_position: 3
slug: /rocketmq/study
tags:
  - RocketMQ
  - IT 架构
  - 中间件
---

# 原理学习

首先我们 学习 MQ 消息中间件不要陷入技术陷阱，先从日常生活中的例子出发，来理解它的原理。  

只要真正理解了原理，再结合技术实现去了解其架构。

## 原理解读

MQ 是为了解决大型软件组件之间的通信问题而产生的一种技术哲学：对海量的、不急迫的通信请求，设置一个中间环节更有效率。  

MQ 的原理一句话也可以说清楚：大型程序运行的时候，组件之间需要发送消息相互通信，频繁的直接通信会导致系统变得复杂而且运行效率低下。故，为了解决复杂性和效率，有人就发明了 MQ 这种中间程序，把消息比作信件，MQ就好比邮局。  

一个邮局所需的组织架构，对应软件世界的 MQ 就需要具备对应的架构：

* MQ 是消息传递服务（消息内容+发件人+收件人）
* MQ 为消息的发送人（生产者）和消息接收人（消费者）的中间桥梁
* MQ 支持分布式节点就比邮局的遍布全国的中转中心

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/rocketmq/rocketmq-arch001-websoft9.png)

故，一个 MQ 系统主要是由：**消息存储池 + 消息订单处理中心** 组成，消息订单处理中心好比邮局企业的大脑，一切的业务实践精华都在大脑中。

对 RocketMQ 而言，NameServer 就是消息订单处理中心， Broker 就是消息存储池。

## 分布式

RocketMQ 来源于阿里的电商业务最佳实践，故其天然有分布式的基因，所以你看到的 RocketMQ 的文档几乎理解起来非常困难。  

如果去繁就简，先不考虑分布式架构，RocketMQ 与 RabbitMQ 的差异也不大。  

阿里做覆盖全国网络的菜鸟物流用于处理现实世界的商品传递，阿里云做分布式MQ用于处理系统的消息传递本质上是一个原理。

## CLI

RocketMQ 提供了强大的的命令行工具 `mqadmin`  

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