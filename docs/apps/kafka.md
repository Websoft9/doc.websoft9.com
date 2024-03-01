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

### 可视化管理 Kafka 集群

通过 Websoft9 应用商店，安装 [Redpanda Console](./redpandaconsole) 实现可视化管理 Kafka 集群

## 配置选项{#configs}

- 认证授权控制：Kafka 镜像支持多种认证授权机制，需自行设置
- 自定义配置：建议通过环境变量设置
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

参考：[Bitnami Kafka Docs](https://github.com/bitnami/containers/tree/main/bitnami/kafka)

## 故障