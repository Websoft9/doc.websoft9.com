---
sidebar_position: 1
slug: /kafka
tags:
  - Kafka
  - IT 架构
  - 中间件
---

# 快速入门

[Apache Kafka](https://kafka.apache.org) 是由Apache软件基金会开发的一个开源流处理平台，由Scala和Java编写。Kafka是一种高吞吐量的分布式发布订阅消息系统，它可以处理消费者规模的网站中的所有动作流数据。 这种动作（网页浏览，搜索和其他用户的行动）是在现代网络上的许多社会功能的一个关键因素。 这些数据通常是由于吞吐量的要求而通过处理日志和日志聚合来解决。

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/kafka/kafka-gui-websoft9.png)

在云服务器上部署 Kafka 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:9092,2181** 端口是否开启

## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

### Kafka

无账号密码认证

### CMAK

* 管理员账号: `admin`
* 管理员密码: 存储在您的服务器中的文件中 */credentials/password.txt*  

## Kafka 安装向导

使用SSH登录到服务器后，运行如下几个命令，检查Kafka是否正确安装

```
systemctl status kafka
systemctl status zookeeper
bash /opt/kafka/bin/kafka-configs.sh
```

> 需要了解更多 Kafka 的使用，请参考官方文档：[Kafka Quickstart](https://kafka.apache.org/quickstart)

## Kafka 入门向导

Coming soon...


## 常用操作

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

### 可视化工具

本预装包中内置 Kafka 可视化集群管理工具 `CMAK` ，使用请参考如下步骤：

1. 登录云控制台，开启服务器安全组[9091端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP:9091*，进入 CMAK 登录页面([不知道密码？](/zh/stack-accounts.md))

3. 成功登录后，开始新建集群
   ![创建kafka集群](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kafka/kafka-addcluster001-websoft9.png)

4. CMAK 成功连接 Kafka
   ![创建kafka集群成功](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kafka/kafka-addcluster002-websoft9.png)

> 更多使用参考[官方文档](https://github.com/yahoo/CMAK)

## 异常处理

#### 运行 *kafka-run-class.sh* 显示 **java: not found...**的错误？

这是Java环境变量缺失导致的问题，请设置环境变量：$JAVA_HOME=/usr/bin/java

#### 本部署环境中是否已经包含Java？

是的

