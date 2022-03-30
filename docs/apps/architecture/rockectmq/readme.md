---
sidebar_position: 1
slug: /rocketmq
tags:
  - RocketMQ 
  - IT 架构
  - 中间件
---

# 快速入门

[RocketMQ](http://rocketmq.apache.org/) 是阿里主导开发的分布式开源消息队列系统，是一个低延迟、高并发、高可用、高可靠的分布式消息中间件。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketmq/rocketmq-console-websoft9.png)

部署 Websoft9 提供的 RocketMQ 之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:9003** 端口已经开启
3. 在服务器中查看 RocketMQ 的 **[默认账号和密码](./setup/credentials#getpw)**  
4. 若想用域名访问  RocketMQ ，务必先完成 **[域名五步设置](./dns#domain)** 过程

## RocketMQ 初始化向导

### 详细步骤

1. 使用 SSH 登录到 RocketMQ 所在服务器后，运行如下命令，检查 RocketMQ 服务状态
   ```
   sudo systemctl status mqnamesrv
   sudo systemctl status mqbroker
   ```
2. 使用本地浏览器访问可视化工具 [RocketMQ-Console](#gui)，进一步验证。

   ![RocketMQ-Console](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketmq/rocketmq-console-websoft9.png)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。

## RocketMQ 使用入门{#start}

下面以 **使用 RocketMQ 发送（生产者）和接受消息（消费者）** 作为一个任务，帮助用户快速入门：

> 建议开始下面的步骤之前，先花5分钟时间阅读由通俗易懂的 [物流系统与消息队列](https://blog.websoft9.com/mq-equal-scm/) 

1. 对实验所需准备的工具或程序做出说明

   * 发送人（本实验对应的是一个程序）：*/data/rocketmq/bin/tools.sh*
   * 接收人（本实验对应的是一个程序）：*/data/rocketmq/bin/tools.sh*
   * 消息信件：示例代码生成 `org.apache.rocketmq.example.quickstart.Producer` （Java 类）
   * 消息存储地： **RabbitMQ Broker**
   * 消息订单处理中心：**NAMESRV_ADDR** 用于根据消息存储地资源情况进行消息的动态分配

2. 使用 SSH 登录到 RocketMQ 服务器，运行下面命令，以发件人的身份发送消息
   ```
   export NAMESRV_ADDR=localhost:9876
   cd /data/rocketmq/bin
   sh tools.sh org.apache.rocketmq.example.quickstart.Producer
   ```

3. 发送成功会收到 *SendResult [sendStatus=SEND_OK, msgId= ...* 之类的反馈结果

4. 在运行下面的命令，以收件人的身份接受消息
   ```
   cd /data/rocketmq/bin
   sh tools.sh org.apache.rocketmq.example.quickstart.Consumer
   ```
5. 接受成功会收到 *ConsumeMessageThread_%d Receive New Messages: [MessageExt...* 之类的反馈结果

6. 登录到可视化界面 [RocketMQ-Console](#gui) 中可更直观的查看运行结果
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketmq/rocketmq-send-websoft9.png)

> 需要了解更多 RocketMQ 的使用，请参考官方文档：[RocketMQ Documentation](http://rocketmq.apache.org/docs/quick-start/)


## RocketMQ 常用操作

### 收发消息示例

对于如何发送消息以及接受消息，本文档章节：[RocketMQ 使用入门](#start) 中有详细的讲解。

### 可视化工具 RocketMQ-Console-NG{#gui}

RocketMQ 扩展项目中提供了管理和监控 RocketMQ 的可视化工具：[RocketMQ-Console-NG ](https://github.com/apache/rocketmq-externals/tree/master/rocketmq-console)：  

1. 使用本地电脑浏览器访问：*http://服务器公网IP:9003*, 进入登陆页面

   ![RocketMQ-Console-NG 登录页面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketmq/rocketmq-loginonly-websoft9.png)

2. 输入账号密码（[不知道账号密码？](./setup/credentials#getpw)），成功登录到 RocketMQ 后台

   ![RocketMQ-Console](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketmq/rocketmq-console-websoft9.png)

3. 设置自己喜欢的语言

   ![RocketMQ-Console 语言设置](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketmq/rocketmq-language-websoft9.png)

3. 接下来便可以在可视化界面查看驾驶舱、集群、消费者等信息（[参考](https://github.com/apache/rocketmq-externals/blob/master/rocketmq-console/doc/1_0_0/UserGuide_CN.md)官网文档）


### 修改 RocketMQ-Console 密码

RocketMQ-Console 工具默认没有提供账号管理功能，但部署方案中通过在 Nginx 的密码功能实现。  
 
需修改密码，请修改 */etc/nginx/.htpasswd/htpasswd.conf* 后，然后重启 Nginx 服务。


### 修改 RocketMQ 运行内存

分别修改如下两个配置文件：

* *rocketmq/bin/runserver.sh* 文件中 Java 启动内存大小（非必要）
* */data/rocketmq/bin/runbroker.sh* 文件中 Java 启动内存大小（非必要）



## 参数

RocketMQ 应用中包含 Nginx, Docker 等组件，可通过 **[通用参数表](./setup/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 RocketMQ 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```

下面仅列出 RocketMQ 本身的参数：

### 端口

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 9003   | 通过 HTTP 访问 RocketMQ-Console-Ng  | 可选   |
| 9876 | RocketMQ Name Server  | 可选   |


### 版本

```shell
ls /data/rocketmq/lib |grep rocketmq-broker
```

### 服务

```shell
sudo systemctl start | stop | restart | status mqnamesrv
sudo systemctl start | stop | restart | status mqbroker

sudo docker start | stop | restart | status rocketmq-console

```

### 命令行

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

### API





