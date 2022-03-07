---
sidebar_position: 3
slug: /kafka/study
tags:
  - Kafka
  - IT 架构
  - 中间件
---

# 原理学习

## 概念

### 什么是消息队列（MQ）？

如果把计算机系统要处理的事情统称为消息，消息队列就是处理消息的容器。当应用服务器瞬时接受到大量消息时，无法一下子处理完成。于是把消息暂时储存到消息队列容器，然后慢慢执行。
MQ分解来看，就是一个转发器，生产者先将消息投递一个叫做「队列」的容器中，然后再从这个容器中取出消息，最后再转发给消费者，仅此而已。

### 什么是Kafka？

Kafka是Apache开源组织下的顶级项目，一个分布式消息队列系统，在大数据处理中性能卓越，日志领域应用很成熟。

### ZooKeeper在Kafka中起什么作用？

为了弄清Kafka和ZooKeeper的关系，我们需要先搞清楚以下几个名词：
 - Broker：Broker是Kafka实例，每个服务器上有一个或多个kafka的实例，我们姑且认为每个broker对应一台服务器。每个kafka集群内的broker都有一个不重复的编号。
 - Producer：Producer即生产者，消息的产生者，是消息的入口。
 - Topic：消息的主题，可以理解为消息的分类，kafka的数据就保存在topic。在每个broker上都可以创建多个topic。
 - Partition：Topic的分区，每个topic可以有多个分区，分区的作用是做负载，提高kafka的吞吐量。同一个topic在不同的分区的数据是不重复的，partition的表现形式就是一个一个的文件夹！
 - Replication:每一个分区都有多个副本，副本的作用是做备胎。当主分区（Leader）故障的时候会选择一个备胎（Follower）上位，成为Leader。在kafka中默认副本的最大数量是10个，且副本的数量不能大于Broker的数量，follower和leader绝对是在不同的机器，同一机器对同一个分区也只可能存放一个副本（包括自己）。
 - Message：每一条发送的消息主体。
 - Consumer：消费者，即消息的消费方，是消息的出口。
 - Consumer Group：我们可以将多个消费组组成一个消费者组，在kafka的设计中同一个分区的数据只能被消费者组中的某一个消费者消费。同一个消费者组的消费者可以消费同一个topic的不同分区的数据，这也是为了提高kafka的吞吐量！
 - Zookeeper：Kafka集群依赖ZooKeeper来保存集群的的元信息，简单来说ZooKeeper用于管理和协调Kafka代理。

Zookeeper在Kafka中的作用罗列如下：
1. Broker注册
每个Kafka服务器（即Broken）相互之间是独立的，那怎么把所有Broker作为集群来管理呢？Zookeeper有一个注册系统，专门用来进行Broker服务器列表记录的节点：/brokers/ids。每个Broker在启动时，都会到Zookeeper上进行注册，即到/brokers/ids下创建属于自己的节点，如/brokers/ids/[0...N]。Kafka使用了全局唯一的数字来指代每个Broker服务器，不同的Broker必须使用不同的Broker ID进行注册，创建完节点后，每个Broker就会将自己的IP地址和端口信息记录到该节点中去。其中，Broker创建的节点类型是临时节点，一旦Broker宕机，则对应的临时节点也会被自动删除。

2. Topic注册
在Kafka中，同一个Topic的消息会被分成多个分区并将其分布在多个Broker上，这些分区信息及与Broker的对应关系也都是由Zookeeper在维护，由专门的节点来记录，如：/borkers/topics。
Kafka中每个Topic都会以/brokers/topics/[topic]的形式被记录，如/brokers/topics/login和/brokers/topics/search等。Broker服务器启动后，会到对应Topic节点（/brokers/topics）上注册自己的Broker ID并写入针对该Topic的分区总数，如/brokers/topics/login/3->2，这个节点表示Broker ID为3的一个Broker服务器，对于"login"这个Topic的消息，提供了2个分区进行消息存储，同样，这个分区节点也是临时节点。

3. 消息消费进度Offset记录
在消费者对指定消息分区进行消息消费的过程中，需要定时地将分区消息的消费进度Offset记录到Zookeeper上，以便在该消费者进行重启或者其他消费者重新接管该消息分区的消息消费后，能够从之前的进度开始继续进行消息消费。Offset在Zookeeper中由一个专门节点进行记录，其节点路径为:/consumers/[group_id]/offsets/[topic]/[broker_id-partition_id]，节点内容就是Offset的值。

4. 消费者注册
消费者服务器在初始化启动时加入Consumer Group，注册到消费者分组。每个消费者服务器启动时，都会到Zookeeper的指定节点下创建一个属于自己的消费者节点，例如/consumers/[group_id]/ids/[consumer_id]，完成节点创建后，消费者就会将自己订阅的Topic信息写入该临时节点。

5. Leader选举
Zookeeper主导Kafka的Leader选举，选举过程过程比较复杂，这里不详细论述。这里主要说下选举的时机
 - 集群初始化启动时选举
 - 热加载了新的Kafka节点时
 - Leader节点挂掉的时候了解决方法

Zookeeper用来管理Kafka，它没和生产者发生关系，只和消费者发生关系，如下图：
 ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kafka/kafka-relation-websoft9.png)

### 生产者如何找到Leader分区的呢？

Kafka集群时，每个Kafka节点都是对等，是通过Zookeeper对不同的topic选举出Leader分区。生产者发送消息时，如何知道哪个节点是Leader分区呢? 简单描述一下步骤：
1. 生产者程序启动后，第一次发元数据请求，发给任意一台，都会返回所有元数据信息，包含你需要信息的Leander分区在哪里
2. 生产者将Leader分区缓存下来，当发送消息时，就从缓存找到Leader分区，直接将消息发送给Leader分区
3. 假如经过一段时间，增加了新的kafka服务器，导致leader分区重新选举，生产者不知情还继续将消息发送给之前的那个分区，这时会返回失败信息。这时将重复1,2保证能正常发送信息。



## Kafka集群

### 为什么要使用Kafka集群？

Kafka对大数据处理性能优越，一般使用Kafka时，系统数据量都非常大。当数据量几何级数增长时，需要考虑两个要素：数据处理能力和容灾备份能力，使用Kafka集群就刚好解决了这两个问题。所以现实当中，一般Kafka应用会使用Kafka集群。

### Kafka集群结构

 ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kafka/kafka-relation-websoft9.png)

我们Kafka集群方案中集群特点：
1. Kafka搭建了集群，Zookeeper也搭建了集群管理Kafka
2. 每个Kafka节点同时也是ZooKeeper节点
3. 消息生产时和Kafka集群连接，消费时需要先通过Zookeeper找到消费位置offset,再连接Kafka集群获取消息
 ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kafka/kafka-cluster1-websoft9.png)
 
 ### 如何搭建Zookeeper和Kafka集群？

我们可以把集群想象成为一个整体，对外连接时作为一个对象工作，具体需要哪个节点工作时再内部协调。因此，我们的集群方案就是，先搭建集群的一个节点，其他复制这个节点后修改即可。
下面我们通过一个节点(172.31.57.62)为例来记录详细步骤：（假设我们使用局域网3台服务器172.31.57.62，172.31.57.63，172.31.57.64搭建集群）
1. 下载[Kafka](https://archive.apache.org/dist/kafka/2.7.1/kafka_2.13-2.7.1.tgz)，解压到/opt下，并改名为kafka
2. 编辑修改config/zookeeper.properties
```
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# the directory where the snapshot is stored.
dataDir=/opt/kafka/zookeeper
dataLogDir=/opt/kafka/log/zookeeper
# the port at which the clients will connect
clientPort=2181
# disable the per-ip limit on the number of connections since this is a non-production config
maxClientCnxns=0
# Disable the adminserver by default to avoid port conflicts.
# Set the port to something non-conflicting if choosing to enable this
admin.enableServer=false
# admin.serverPort=8080
tickTime=2000
initLimit=10
syncLimit=5

server.1=172.31.57.62:2888:3888
server.2=172.31.57.63:2888:3888
server.3=172.31.57.64:2888:3888
```
3. 进入zookeeper，创建ID文件

```
cd zookeeper
echo 1 > myid
```

4. 创建Zookeeper服务，启动

```
[Unit]
Description=Apache Kafka server (broker1)
After=network.target  zookeeper.service
[Service]
Type=simple
User=root
Group=root
ExecStart=/opt/kafka/bin/zookeeper-server-start.sh /opt/kafka/config/zookeeper.properties
ExecStop=/opt/kafka/bin/zookeeper-server-stop.sh
Restart=on-failure
[Install]
WantedBy=multi-user.target
```

```
systemctl daemon-reload
systemctl restart zookeeper
```

5. 编辑Kafka配置文件

```
# With the same id
broker.id=1
# Change the IP address to your own
listeners=PLAINTEXT://172.31.57.62:9092
# logs dir
log.dirs=/opt/kafka/logs

zookeeper.connect=172.31.57.62:2181,172.31.57.63:2181,172.31.57.64:2181
```

6. 创建Kafka服务，启动

```
/etc/systemd/system/kafka.service
[Unit]
Description=Apache Kafka server (broker1)
After=network.target  zookeeper.service
[Service]
Type=simple
User=root
Group=root
ExecStart=/opt/kafka/bin/kafka-server-start.sh /opt/kafka/config/server.properties
ExecStop=/opt/kafka/bin/kafka-server-stop.sh
Restart=on-failure
[Install]
WantedBy=multi-user.target
```

```
systemctl daemon-reload
systemctl restart kafka
```

7,复制上面节点到服务器（172.31.57.63），将步骤3的myid修改成2，步骤5中broker.id修改成2，步骤5中listeners修改成该服务器地址；其他节点依次类推

8，注意当所有相关节点服务器都启动后，才会显示正常，否则会报错
