---
title: RocketMQ
slug: /rocketmq
tags:
  - RocketMQ 
  - IT 架构
  - 中间件
---

import Meta from './_include/rocketmq.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 RocketMQ 后，通过【我的应用】进入它的编辑窗口，在**访问**标签页中获取登录地址和账号。  

1. 使用本地浏览器访问可视化工具 [RocketMQ-Console](#gui)，进一步验证。

   ![RocketMQ-Console](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketmq/rocketmq-console-websoft9.png)

2. 测试其可用性


### 发送消息与接收消息{#start}

下面以 **使用 RocketMQ 发送（生产者）和接受消息（消费者）** 作为一个任务，帮助用户快速入门：

> 建议开始下面的步骤之前，先花5分钟时间阅读由通俗易懂的 [物流系统与消息队列](https://blog.websoft9.com/mq-equal-scm/) 

1. 对实验所需准备的工具或程序做出说明

   * 发送人（本实验对应的是一个程序）：*/data/rocketmq/bin/tools.sh*
   * 接收人（本实验对应的是一个程序）：*/data/rocketmq/bin/tools.sh*
   * 消息信件：示例代码生成 `org.apache.rocketmq.example.quickstart.Producer` （Java 类）
   * 消息存储地： **RabbitMQ Broker**
   * 消息订单处理中心：**NAMESRV_ADDR** 用于根据消息存储地资源情况进行消息的动态分配

2. 使用 SSH 登录到 RocketMQ 服务器，运行下面命令，以发件人的身份发送消息
   ```
   export NAMESRV_ADDR=localhost:9876
   cd /data/rocketmq/bin
   sh tools.sh org.apache.rocketmq.example.quickstart.Producer
   ```

3. 发送成功会收到 *SendResult [sendStatus=SEND_OK, msgId= ...* 之类的反馈结果

4. 在运行下面的命令，以收件人的身份接受消息
   ```
   cd /data/rocketmq/bin
   sh tools.sh org.apache.rocketmq.example.quickstart.Consumer
   ```
5. 接受成功会收到 *ConsumeMessageThread_%d Receive New Messages: [MessageExt...* 之类的反馈结果

6. 登录到可视化界面 [RocketMQ-Console](#gui) 中可更直观的查看运行结果
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketmq/rocketmq-send-websoft9.png)


## 管理维护{#administrator}

### 命令行

RocketMQ 提供了强大的的命令行工具 `mqadmin`  

### 修改 RocketMQ 运行内存

分别修改如下两个配置文件：

* *rocketmq/bin/runserver.sh* 文件中 Java 启动内存大小（非必要）
* */data/rocketmq/bin/runbroker.sh* 文件中 Java 启动内存大小（非必要）

### 可视化工具 RocketMQ-Console-NG{#gui}

RocketMQ 扩展项目中提供了管理和监控 RocketMQ 的可视化工具：[RocketMQ-Console-NG ](https://github.com/apache/rocketmq-externals/tree/master/rocketmq-console)：  

1. 使用本地电脑浏览器访问, 进入登陆页面

   ![RocketMQ-Console-NG 登录页面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketmq/rocketmq-loginonly-websoft9.png)

2. 输入账号密码（[不知道账号密码？](./user/credentials)），成功登录到 RocketMQ 后台

   ![RocketMQ-Console](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketmq/rocketmq-console-websoft9.png)

3. 设置自己喜欢的语言

   ![RocketMQ-Console 语言设置](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketmq/rocketmq-language-websoft9.png)

3. 接下来便可以在可视化界面查看驾驶舱、集群、消费者等信息（[参考](https://github.com/apache/rocketmq-externals/blob/master/rocketmq-console/doc/1_0_0/UserGuide_CN.md)官网文档）



## 故障

#### RocketMQ 的消息丢失？

消息将最多保存3天，未使用超过3天的消息将被删除。