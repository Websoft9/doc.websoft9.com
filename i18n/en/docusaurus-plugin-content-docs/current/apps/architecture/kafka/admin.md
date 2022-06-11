---
sidebar_position: 3
slug: /kafka/admin
tags:
  - Kafka
  - IT Architecture
  - Broker
---

# Kafka Maintenance

This chapter is special guide for Kafka maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### Backup and Restore   

### Upgrade

You can upgrade your Kafka by the following steps:

1. Prepare for upgrade
   ```
   # stop Kafka,Zookeeper service
   systemctl stop kafka
   systemctl stop zookeeper

   # rename the dir of Kafka for backup
   mv /opt/kafka  /opt/kafkaBK
   ```
2. [Download Kafka](https://kafka.apache.org/downloads) and unzip it, then upload to the directory: */opt* and renamed it to *kafka*
3. Run the following modify permissions
   ```
   chown -R kafka. /opt/kafka
   ```
4. Restart [Kafka services](/zh/admin-services#kafka)

### Kafka 集群

Kafka对大数据处理性能优越，一般使用Kafka时，系统数据量都非常大。当数据量几何级数增长时，需要考虑两个要素：数据处理能力和容灾备份能力，使用Kafka集群就刚好解决了这两个问题。所以现实当中，一般Kafka应用会使用Kafka集群。

**Kafka集群结构**

 ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kafka/kafka-relation-websoft9.png)

我们Kafka集群方案中集群特点：
1. Kafka搭建了集群，Zookeeper也搭建了集群管理Kafka
2. 每个Kafka节点同时也是ZooKeeper节点
3. 消息生产时和Kafka集群连接，消费时需要先通过Zookeeper找到消费位置offset,再连接Kafka集群获取消息
 ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kafka/kafka-cluster1-websoft9.png)
  
**搭建Zookeeper和Kafka集群**

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

5. 编辑Kafkaconfiguration file

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

7. 复制上面节点到服务器（172.31.57.63），将步骤3的myid修改成2，步骤5中broker.id修改成2，步骤5中listeners修改成该服务器地址；其他节点依次类推

8. 注意当所有相关节点服务器都启动后，才会显示正常，否则会报错
  
## Troubleshoot{#troubleshoot}

In addition to the Kafka issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  
  
#### Kafka service can't start?

1. Use the debug mode of `bash /opt/kafka/bin/kafka-server-start.sh` and you can see the errors
2. Search the keywords **Failed** or **error** from logs: */data/logs*
  
#### Run the command "kafka-topics.sh", java not found?

You should add a variable $JAVA_HOME=/usr/bin/java

## FAQ{#faq}
  
#### How can I enable the debug mode of Kafka service?

```
systemctl stop kafka zookeeper
bash /opt/kafka/bin/kafka-server-start.sh
```
  
#### Is Java included in this deployment solution?

Yes
  
#### Is a web-based GUI management tool for Kafka?

Yes, refer to [CMAK](../kafka#gui)
  
#### CMAK 中无法支持所需的 Kafka 版本？

CMAK 并不是支持所有 Kafka 版本，具体以使用为准

#### CMAK 连接 Kafaka2.4 以下报错？

错误信息： Yikes! KeeperErrorCode = Unimplemented for /kafka-manager/mutex Try again. ([issue](https://github.com/yahoo/CMAK/issues/748))   
解决方案： 暂无

但出现上述错误的情景中，Zookeeper 客户端是可以连接 Zookeeper 服务端的  