---
title: Logstash
slug: /logstash
tags:
  - ELK
  - 数据采集
  - 日志收集
  - 输入输出
---

import Meta from './_include/logstash.md';

<Meta name="meta" />

## 入门指南{#guide}

Websoft9 控制台安装 Logstash 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

### 采集（输入）数据

在 Logstash 的配置文件中，您需要指定一个或多个输入插件来定义数据的来源。Logstash 提供了许多内置的输入插件，例如 File、TCP、UDP、HTTP 等。您可以根据您的需求选择适当的输入插件，并配置其相关参数。

### 过滤数据

如果您需要对采集的数据进行处理或转换，您可以配置一些过滤插件。过滤插件可以帮助您解析、修改或丰富数据。Logstash 提供了多种过滤插件，例如 grok、mutate、date 等。您可以根据数据的结构和需求选择适当的过滤插件，并配置其参数。

### 输出数据

#### 到 Elasticsearch 

参考：[Elasticsearch 连接 Logstash](./elasticsearch#logstash)

#### 到 Kafka

1. 先安装 Kafka 插件
2. 配置文件中增加一段连接配置
   ```
   output {
      kafka {
        bootstrap_servers => "kafka_host:port"  # Kafka 服务器的主机和端口
        topic_id => "your_topic"  # Kafka 主题的名称
      }
    }
   ```

## 配置选项{#configs}

- Logstash 配置文件：*/path/logstash/pipeline/logstash.conf*  


## 管理维护{#administrator}

## 故障