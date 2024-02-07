---
title: Kafka
slug: /kafka
tags:
  - MQ
  - 消息队列
  - 消息中间件
---

import Meta from './_include/kafka.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 Kafka 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

### 日志管理

配置文件有如下日志相关的配置项：

```
log.cleanup.policy=delete #添加 启用删除策略配置段
log.retention.hours=168    #默认7天
log.retention.check.interval.ms=300000 #默认每5分钟检查一次
log.segment.bytes=1073741824 #默认每个segment的大小为1GB
```

## 配置选项{#configs}

- 配置文件：/opt/bitnami/kafka/config/server.propertie
- 命令行
  ```
  # kafka
  /opt/bitnami/kafka/bin/kafka-console-consumer.sh --bootstrap-server yourip:port --consumer.config consumer.properties --topic my-topic

  # ZooKeeper client
  zkCli.sh -server IP:2181
  ```
- [Kafka APIS](https://kafka.apache.org/documentation/#api)
- [Kafka Clients](https://cwiki.apache.org/confluence/display/KAFKA/Clients)

## 管理维护{#administrator}

### 升级

官方文档：[Upgrading From Previous Versions](https://kafka.apache.org/documentation/#upgrade)

### Kafka 集群

另见由 Websoft9 提供的 Kafka 集群解决方案。

## 故障