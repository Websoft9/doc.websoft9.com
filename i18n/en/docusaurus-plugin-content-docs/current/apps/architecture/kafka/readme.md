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
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:9092,2181** 端口已经开启
3. 在服务器中查看 kafka 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  kafka ，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程

## Kafka 初始化向导

使用SSH登录到服务器后，运行如下几个命令，检查 Kafka是否正确安装

```
systemctl status kafka
systemctl status zookeeper
bash /opt/kafka/bin/kafka-configs.sh
```

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
sed -i '/log.retention.hours=168/i\log.cleanup.policy=delete' /opt/kafka/config/server.properties

# 重启Kafka
systemctl restart kafka
```

#### 自定义日志清理策略

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

## 参数

Kafka 应用中包含 Nginx, CMAK, Docker, Zookeeper, Java 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。

通过运行 `docker ps`，可以查看到 Kafka 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 Kafka 本身的参数：

### 路径{#path}

#### Kafka

Kafka 安装目录：*/opt/kafka*  
Kafka 日志目录：*/opt/kafka/logs*  
Kafka bin目录：*/opt/kafka/bin*  
Kafka 配置目录：*/opt/kafka/config*  

#### CMAK

[CMAK](https://github.com/yahoo/CMAK) 是管理 Kafka 集群的可视化工具，基于 Docker 安装

CMAK 安装目录： */data/apps/cmak*  

#### Zookeeper

Zookeeper 配置文件路径：/opt/zookeeper/conf/  
Zookeeper 日志文件：/opt/zookeeper/tmp/zookeeper.out  


### 端口

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 9092   | Kafka | 可选   |
| 2181   | Zookeeper | 可选   |
| 9091   | CMAK  | 可选   |

### 版本

```shell
# Kafka version
ls /opt/kafka/libs | grep kafka_

# CMAK version
docker exec -it cmak bash -c 'ls /cmak/lib/cmak.cmak-*-assets.jar'

```

### 服务

```shell
sudo systemctl start | stop | restart | status kafka
bash /opt/kafka/bin/kafka-server-start.sh

sudo systemctl start | stop | restart | status zookeeper
bash /opt/kafka/bin/zookeeper-server-start.sh

sudo docker start | stop | restart | stats cmak
```

### 命令行

```
# kafka
bin/kafka-console-consumer.sh --bootstrap-server youip:port --consumer.config consumer.properties --topic my-topic

# ZooKeeper client
zkCli.sh -server IP:2181
```

### API

[Kafka APIS](https://kafka.apache.org/documentation/#api) 和 [Kafka Clients](https://cwiki.apache.org/confluence/display/KAFKA/Clients)