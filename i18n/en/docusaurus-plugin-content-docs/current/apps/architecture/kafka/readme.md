---
sidebar_position: 1
slug: /kafka
tags:
  - Kafka
  - IT Architecture
  - Broker
---
 
# Kafka Getting Started

[Apache Kafka](https://kafka.apache.org/) is an open-source stream-processing software platform developed by LinkedIn and donated to the Apache Software Foundation, written in Scala and Java. The project aims to provide a unified, high-throughput, low-latency platform for handling real-time data feeds.

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/kafka/kafka-gui-websoft9.png)

If you have installed Websoft9 Kafka, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:9092,2181** is allowed
3. **[Get](./user/credentials)** default username and password of Kafka
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Kafka

## Kafka Installation Check

Use you **SSH** to login Server, run the following commands

```
systemctl status kafka
systemctl status zookeeper
bash /opt/kafka/bin/kafka-configs.sh
```

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  
  
## Kafka QuickStart

Refer to the Kafka official docs for your quick start: [Kafka Quickstart](https://kafka.apache.org/quickstart)

## Kafka Setup

### Kafka GUI

This deployment package includes Kafka and Web-GUI tool **CMAK** for Kafka Cluster management. 

Follow the steps below to use it:

1. Use the Chrome or FireFox to access URL *http://Server's Internet IP:9091*, go to CMAK login page ([Don't know password?](./user/credentials))

2. Create new Kafka Cluster when login successfully
   ![Create kafka cluster](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kafka/kafka-addcluster001-websoft9.png)

3. CMAK connect Kafka successfully
   ![Create kafka cluster](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kafka/kafka-addcluster002-websoft9.png)
  
### 日志管理

**启用默认日志清理策略**

Kafka 默认设置保留 7 天日志，但默认并为启用日志清理策略。运行如下命令后启用：

```
# 打开日志删除策略
sed -i '/log.retention.hours=168/i\log.cleanup.policy=delete' /opt/kafka/config/server.properties

# 重启Kafka
systemctl restart kafka
```

**自定义日志清理策略**

用户可以自定义日志清理策略，具体步骤如下：

1. 修改 */opt/kafka/config/server.propertie*  文件中相关的参数
    ```
    log.cleanup.policy=delete #添加 启用删除策略配置段
    log.retention.hours=168    #默认7天
    log.retention.check.interval.ms=300000 #默认每5分钟检查一次
    log.segment.bytes=1073741824 #默认每个segment的大小为1GB
    ```

2. 修改后重启 Kafka 服务
    ```
    systemctl restart kafka
    ```

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Kafka

通过运行 `docker ps`，可以查看到 Kafka 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```
  
### Path{#path}

Kafka installation directory:*/opt/kafka*  
Kafka installation log directory:*/opt/kafka/logs*  
Kafka bin directory: */opt/kafka/bin*  
Kafka configuration directory: */opt/kafka/config* 
  
### Port{#port}

| Port | Use                                          | Necessity |
| ------ | --------------------------------------------- | ------ |
| 9092 | Kafka | Optional |
| 2181 | Zookeeper | Optional |
| 9091 | CMAK | Optional |

### Version{#version}

```shell
# Kafka version
ls /opt/kafka/libs | grep kafka_

# CMAK version
docker exec -it cmak bash -c 'ls /cmak/lib/cmak.cmak-*-assets.jar'

```

### Service{#service}

```shell
sudo systemctl start | stop | restart | status kafka
bash /opt/kafka/bin/kafka-server-start.sh

sudo systemctl start | stop | restart | status zookeeper
bash /opt/kafka/bin/zookeeper-server-start.sh

sudo docker start | stop | restart | stats cmak
```
  
### CLI{#cli}
  
```
# kafka
bin/kafka-console-consumer.sh --bootstrap-server youip:port --consumer.config consumer.properties --topic my-topic

# ZooKeeper client
zkCli.sh -server IP:2181
```
  
### API

Refer to [Kafka APIS](https://kafka.apache.org/documentation/#api) and [Kafka Clients](https://cwiki.apache.org/confluence/display/KAFKA/Clients)