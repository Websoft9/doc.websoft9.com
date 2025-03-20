---
title: RocketMQ
slug: /rocketmq
tags:
  - RocketMQ 
  - IT 架构
  - 中间件
---

import Meta from './_include/rocketmq.md';

<Meta name="meta" />

## 入门指南{#guide}

### 验证 RocketMQ{#verification}

1. Websoft9 控制台安装 RocketMQ 后，通过 **我的应用** 查看应用详情，在 **访问** 和 **容器** 标签页中获取相关信息。

2. 进入 **nameserver** 容器运行下列命令， 查看集群列表。  
    ```
    sh-4.2$ ./mqadmin clusterList -n localhost:9876
    #Cluster Name           #Broker Name            #BID  #Addr                  #Version              #InTPS(LOAD)     #OutTPS(LOAD)  #Timer(Progress)        #PCWait(ms)  #Hour         #SPACE    #ACTIVATED
    DefaultCluster          ff0d7f2d94c3            0     172.18.0.10:10911      V5_2_0                 0.00(0,0ms)       0.00(0,0ms)  0-0(0.0w, 0.0, 0.0)               0  477942.14     0.5400          true
    ```

3. 进入 **broker** 容器运行下列命令，查看 Broker 状态。
    ```
    [rocketmq@ff0d7f2d94c3 bin]$ ./mqadmin brokerStatus -n rocketmq_rymr8-rmqnamesrv:9876 -b localhost:10911
    EndTransactionQueueSize         : 0
    EndTransactionThreadPoolQueueCapacity: 100000
    bootTimestamp                   : 1720575200001
    brokerActive                    : true
    brokerVersion                   : 453
    brokerVersionDesc               : V5_2_0
    commitLogDirCapacity            : Total : 99.8 GiB, Free : 46.9 GiB.
    ...
    ```

4. 进入 **broker** 容器运行下列命令，生产一组消息。 

    ```
    [rocketmq@ff0d7f2d94c3 bin]$ sh tools.sh org.apache.rocketmq.example.quickstart.Producer
    ...
    SendResult [sendStatus=SEND_OK, msgId=AC12000A02CF7E6CBB7A2FBE0ED003DC, offsetMsgId=AC12000A00002A9F00000000000B1472, messageQueue=MessageQueue [topic=TopicTest, brokerName=ff0d7f2d94c3, queueId=1], queueOffset=751]
    SendResult [sendStatus=SEND_OK, msgId=AC12000A02CF7E6CBB7A2FBE0ED003DD, offsetMsgId=AC12000A00002A9F00000000000B1564, messageQueue=MessageQueue [topic=TopicTest, brokerName=ff0d7f2d94c3, queueId=2], queueOffset=751]
    ```

5. 进入 **broker** 容器运行下列命令，消费一组消息。

    ```
    [rocketmq@ff0d7f2d94c3 bin]$ sh tools.sh org.apache.rocketmq.example.quickstart.Consumer
    ...
    06:26:26,005 |-INFO in org.apache.rocketmq.logging.ch.qos.logback.classic.model.processor.RootLoggerModelHandler - Setting level of ROOT logger to INFO
    06:26:26,005 |-INFO in org.apache.rocketmq.logging.ch.qos.logback.core.model.processor.AppenderRefModelHandler - Attaching appender named [DefaultAppender] to Logger[ROOT]
    06:26:26,006 |-INFO in org.apache.rocketmq.logging.ch.qos.logback.core.model.processor.DefaultProcessor@cb0ed20 - End of configuration.
    06:26:26,007 |-INFO in org.apache.rocketmq.common.logging.JoranConfiguratorExt@8e24743 - Registering current configuration as safe fallback point

    Consumer Started
    ...
    ConsumeMessageThread_please_rename_unique_group_name_4_16 Receive New Messages: [MessageExt [brokerName=ff0d7f2d94c3, queueId=1, storeSize=242, queueOffset=863, sysFlag=0, bornTimestamp=1720593053737, bornHost=/172.18.0.10:56962, storeTimestamp=1720593053737, storeHost=/172.18.0.10:10911, msgId=AC12000A00002A9F00000000000CBB84, commitLogOffset=834436, bodyCRC=1149360467, reconsumeTimes=0, preparedTransactionOffset=0, toString()=Message{topic='TopicTest', flag=0, properties={CONSUME_START_TIME=1720593068458, MSG_REGION=DefaultRegion, UNIQ_KEY=AC12000A03057E6CBB7A2FBF1C2901B4, CLUSTER=DefaultCluster, MIN_OFFSET=0, TAGS=TagA, WAIT=true, TRACE_ON=true, MAX_OFFSET=1004}, body=[72, 101, 108, 108, 111, 32, 82, 111, 99, 107, 101, 116, 77, 81, 32, 52, 51, 54], transactionId='null'}]]
    ```

## 配置选项{#configs}

- Cli (√)： mqadmin
- 配置文件： 在 `bin/runserver.sh` 和 `bin/runbroker.sh` 中配置启动内存
- 控制台： [RocketMQ Dashboard](https://rocketmq.apache.org/docs/deploymentOperations/04Dashboard)
- SDK (√)

## 管理维护{#administrator}

## 故障
