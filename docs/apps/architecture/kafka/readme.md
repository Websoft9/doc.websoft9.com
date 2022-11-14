---
sidebar_position: 1
slug: /kafka
tags:
  - Kafka
  - IT 架构
  - 中间件
---

# 快速入门

[Apache Kafka](https://kafka.apache.org) 一个开源流处理平台，由 Scala 和 Java 编写。Kafka 是一种高吞吐量的分布式发布订阅消息系统，它可以处理消费者规模的网站中的所有动作流数据（网页浏览，搜索和其他用户的行动）。

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/kafka/kafka-gui-websoft9.png)

部署 Websoft9 提供的 kafka 之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:9091,9092,2181** 端口已经开启
3. 在服务器中查看 kafka 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  kafka ，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程

## Kafka 初始化向导

### 详细步骤

使用SSH登录到服务器后，运行如下几个命令，检查 Kafka是否正确安装

```
cd /data/apps/kafka && sudo docker compose ls
```
Kafka 正常运行会得到 " STATUS: running(3) " 的反馈

### 碰到问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。

## Kafka 使用入门

[Kafka Quickstart](https://kafka.apache.org/quickstart) 或以 **Github 上的项目通过 Kafka 自动构建部署** 作为一个任务，帮助用户快速入门：

## Kafka 常用操作

### 可视化工具{#gui}

本预装包中内置 Kafka 可视化集群管理工具 [CMAK](https://github.com/yahoo/CMAK) ，使用请参考如下步骤：

1. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP:9091*，进入 CMAK 登录页面([不知道密码？](./user/credentials))

2. 成功登录后，开始新建集群
   ![创建kafka集群](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kafka/kafka-addcluster001-websoft9.png)

3. CMAK 成功连接 Kafka
   ![创建kafka集群成功](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kafka/kafka-addcluster002-websoft9.png)

### 日志管理

#### 启用默认日志清理策略

Kafka 默认设置保留 7 天日志，但默认并为启用日志清理策略。运行如下命令后启用：

```
# 打开日志删除策略
docker exec -it kafka sed -i '/log.retention.hours=168/i\log.cleanup.policy=delete' /opt/bitnami/kafka/config/server.properties

# 重启 [Kafka 服务](#service)
sudo docker restart kafka
```

#### 自定义日志清理策略

用户可以自定义日志清理策略，具体步骤如下：

1. 进入kafka容器
    ```
    sudo docker exec -it kafka bash
    ```

2. 修改 */opt/bitnami/kafka/config/server.propertie*  文件中相关的参数
    ```
    log.cleanup.policy=delete #添加 启用删除策略配置段
    log.retention.hours=168    #默认7天
    log.retention.check.interval.ms=300000 #默认每5分钟检查一次
    log.segment.bytes=1073741824 #默认每个segment的大小为1GB
    ```

3. 重启  [Kafka 服务](#service)
    ```
    sudo docker restart kafka
    ```

## 参数

Kafka 应用中包含 Nginx, CMAK, Docker, Zookeeper等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。

通过运行 `docker ps`，可以查看到 Kafka 运行时所有的 Container：

```bash
CONTAINER ID   IMAGE                                         COMMAND                  CREATED          STATUS          PORTS                                                                     NAMES
e628a73126fd   bitnami/kafka:2.8                             "/opt/bitnami/script…"   36 minutes ago   Up 36 minutes   0.0.0.0:9092->9092/tcp, :::9092->9092/tcp                                 kafka
219ebeafc96c   bitnami/zookeeper:latest                      "/opt/bitnami/script…"   36 minutes ago   Up 36 minutes   2888/tcp, 3888/tcp, 0.0.0.0:2181->2181/tcp, :::2181->2181/tcp, 8080/tcp   kafka-zookeeper
84ff90680786   ghcr.io/eshepelyuk/dckr/cmak-3.0.0.5:latest   "/cmak/bin/cmak -Dpi…"   36 minutes ago   Up 36 minutes   0.0.0.0:9091->9000/tcp, :::9091->9000/tcp                                 kafka-cmak
```

### 路径{#path}

Kafka 安装目录：*/data/apps/kafka*  
Kafka 数据目录：*/data/apps/kafka/data/kafka_data*  
Kafka 配置目录：*/data/apps/kafka/data/kafka_data/kafka/config*   
Zookeeper 数据目录：*/data/apps/kafka/data/zookeeper_data*   

### 端口

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 9092   | Kafka | 必须   |
| 2181   | Zookeeper | 必须   |
| 9091   | CMAK  | 可选   |

### 版本

```shell
# Kafka version
docker exec -i kafka /opt/bitnami/kafka/bin/kafka-topics.sh --version

# CMAK version
docker exec -it kafka-cmak bash -c 'ls /cmak/lib/cmak.cmak-*-assets.jar'|awk -F"-" '{print $2}'

```

### 服务

```shell
sudo docker start | stop | restart kafka
sudo docker start | stop | restart kafka-cmak
sudo docker start | stop | restart kafka-zookeeper
```

### 命令行

```
# kafka
docker exec -it kafka /opt/bitnami/kafka/bin/kafka-console-consumer.sh --bootstrap-server yourip:port --consumer.config consumer.properties --topic my-topic

# ZooKeeper client
docker exec -it kafka-zookeeper zkCli.sh -server IP:2181
```

### API

[Kafka APIS](https://kafka.apache.org/documentation/#api) 和 [Kafka Clients](https://cwiki.apache.org/confluence/display/KAFKA/Clients)