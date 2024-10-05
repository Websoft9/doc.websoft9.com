---
title: Kafka
slug: /kafka
tags:
  - MQ
  - Message Queues
  - Message Middleware
---

import Meta from './_include/kafka.md';

<Meta name="meta" />

## Getting started{#guide}

### Visualize Kafka Cluster Management 

Install the [Redpanda Console](./redpandaconsole) from the **Websoft9 App Store** to visually manage your Kafka cluster.

## Configuration options{#configs}

- Authentication and Authorization Control: Kafka mirrors support various authentication and authorization mechanisms, which need to be configured manually.
- Custom Configuration: It is recommended to set up through environment variables.
- CLI
  ```
  /opt/bitnami/kafka/bin/kafka
  /opt/bitnami/kafka/bin/kafka-console-consumer.sh --bootstrap-server yourip:port --consumer.config consumer.properties --topic my-topic

  # ZooKeeper client
  zkCli.sh -server IP:2181
  ```
- [Kafka APIS](https://kafka.apache.org/documentation/#api)
- [Kafka Clients](https://cwiki.apache.org/confluence/display/KAFKA/Clients)

## Administer{#administrator}

Refer to the [Bitnami Kafka Docs](https://github.com/bitnami/containers/tree/main/bitnami/kafka) for additional information

## Troubleshooting{#troubleshooting}

