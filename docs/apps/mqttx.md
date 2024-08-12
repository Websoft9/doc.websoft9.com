---
title: MQTTX
slug: /mqttx
tags:
  - Web 面板
  - 可视化
  - GUI
---

import Meta from './_include/mqttx.md';

<Meta name="meta" />

## 入门指南{#guide}

### 测试访问{#wizard}

1. Websoft9 控制台安装 MQTTX 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取访问信息。 

2. 创建一个连接

   - Client ID 是自动生成的
   - 服务器地址：协议和地址、端口是被连接的服务的值

   ![](./assets/mqttx-connection-websoft9.png)

### 集成 RabbitMQ

1. 准保 RabbitMQ

   1. Websoft9 应用商店安装 RabbitMQ
   2. RabbitMQ 容器命令行启用插件
      ```
      rabbitmq-plugins enable rabbitmq_mqtt
      rabbitmq-plugins enable rabbitmq_web_mqtt   
      ```

2. MQTTX 中新建 RabbiMQ 连接，确保主机、端口、账号和连接协议准确

### 集成 EMQX

1. 准备 EMQX

   1. Websoft9 应用商店安装 EMQX
   2. EMQX Dashboard 打开：**问题分析 > WebSocket 客户端** 页面，为默认的 WebSocket 连接设置**用户名、密码和协议版本**

2. MQTTX 中新建 EMQX 连接，确保主机、端口、账号和连接协议准确

## 配置选项{#configs}

- 多语言（√）

## 管理维护{#administrator}

## 故障
