---
sidebar_position: 2
slug: /kafka/solution
tags:
  - Kafka
  - IT Architecture
  - Broker
  
---

# Kafka Solution
  
You can use Kafka integrated other software for IT Architecture.


## Kafka and Zookeeper

### What role does zookeeper play in Kafka?
In order to understand the relationship between Kafka and zookeeper, we need to understand the following nouns first:

- Broker: a broker is an instance of Kafka. There are one or more instances of Kafka on each server. We think that each broker corresponds to one server. Brokers in each Kafka cluster have a unique number.
- Producer: producer is the producer, the producer of the message, and the entry of the message.
- Topic: the topic of the message can be understood as the classification of the message. Kafka's data is saved in topic. Multiple topics can be created on each broker.
- Partition: the partition of a topic. Each topic can have multiple partitions. The partition is used to load and improve the throughput of Kafka. The data of the same topic in different partitions is not repeated. The expression of partition is one folder after another!
- Replication: each partition has multiple replicas. The replica is used as a spare tire. When the main partition (leader) fails, a spare tire (follower) will be selected as the leader. In Kafka, the default maximum number of replicas is 10, and the number of replicas cannot be greater than the number of brokers. The follower and leader are definitely on different machines. The same machine can only store one replica (including itself) for the same partition.
- Message: the body of each message sent.
- Consumer: the consumer, that is, the consumer of the message, is the export of the message.
- Consumer group: we can form multiple consumer groups into a consumer group. In Kafka's design, data in the same partition can only be consumed by one consumer in the consumer group. Consumers of the same consumer group can consume data from different partitions of the same topic, which is also to improve the throughput of Kafka!
- Zookeeper: the Kafka cluster relies on zookeeper to save the meta information of the cluster. In short, zookeeper is used to manage and coordinate the Kafka agent.

The role of zookeeper in Kafka is listed as follows:

1. Broker registration
Each Kafka server (i.e. broker) is independent from each other. How can all brokers be managed as a cluster? Zookeeper has a registration system, which is used to record the broker server list: / brokers / IDs. When each broker is started, it will register with zookeeper, that is, create its own node under / brokers / IDS, such as / brokers / IDS / [0... N]. Kafka uses a globally unique number to refer to each broker server. Different brokers must register with different broker IDs. After creating a node, each broker will record its own IP address and port information in the node. The node type created by the broker is a temporary node. Once the broker goes down, the corresponding temporary node will be automatically deleted.

2. Topic registration
In Kafka, messages of the same topic are divided into multiple partitions and distributed on multiple brokers. The partition information and the corresponding relationship with brokers are also maintained by zookeeper and recorded by special nodes, such as: / brokers / topics.
Each topic in Kafka will be recorded in the form of / brokers / topics / [Topic], such as / brokers / topics / login and / brokers / topics / search. After the broker server is started, it will register its broker ID on the corresponding topic node (/ brokers / topics) and write the total number of partitions for the topic, such as / brokers / topics / login / 3 - > 2. This node represents a broker server with broker ID of 3. For the message of "login", two partitions are provided for message storage. Similarly, this partition node is also a temporary node.

3. Message consumption progress offset record
During the process of message consumption by a consumer on a specified message partition, it is necessary to regularly record the consumption progress offset of the partition message on zookeeper, so that after the consumer restarts or other consumers take over the message consumption of the message partition again, the message consumption can continue from the previous progress. Offset is recorded by a special node in zookeeper. The node path is: / consumers / [group_id] / offsets / [Topic] / [broker_id-partition_id]. The node content is the value of offset.

4. Consumer registration
The consumer server joins the consumer group when it is initialized and registered with the consumer group. When each consumer server is started, it will create its own consumer node under the specified node of zookeeper, for example, / consumers / [group_id] / IDS / [consumer_id]. After the node is created, consumers will write the topic information subscribed to by themselves into the temporary node.

5. Leader election
Zookeeper dominates Kafka's leader election. The election process is relatively complicated, and will not be discussed in detail here. Here we will mainly talk about the timing of the election
- Cluster initialization (election at startup)
- When a new Kafka node is hot loaded
- It's time for the leader node to hang up. Solution:

Zookeeper is used to manage Kafka. It has no relationship with producers but only with consumers, as shown in the following figure:
 ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kafka/kafka-relation-websoft9.png)

### How does the producer find the leader partition?

In Kafka cluster, each Kafka node is peer-to-peer, and the leader partition is selected by zookeeper for different topics. How do producers know which node is the leader partition when sending messages? Briefly describe the following steps:

1. After the producer program is started, the first time it sends a metadata request to any one, all metadata information will be returned. Where is the Leander partition containing the information you need
2. The producer caches the leader partition. When sending a message, it finds the leader partition from the cache and directly sends the message to the leader partition
3. If a new Kafka server is added after a period of time, leading to the re-election of the leader partition, the producer continues to send the message to the previous partition without knowing it, and the failure information will be returned. At this time, 1 and 2 will be repeated to ensure that information can be sent normally.



