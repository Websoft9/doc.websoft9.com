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

### 初始化{#wizard}

Websoft9 控制台安装 MQTTX 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

### 集成 RabbitMQ

1. 准备好 RabbitMQ

   - Websoft9 应用商店安装 RabbitMQ
   - RabbitMQ 容器命令行启用插件
     ```
     rabbitmq-plugins enable rabbitmq_mqtt
     rabbitmq-plugins enable rabbitmq_web_mqtt   
     ```

2. MQTTX 连接 RabbiMQ，并测试
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mqttx/mqttx-connect-rabbitmq-websoft9.png)


### 集成 EMQX

1. 准备好 EMQX

   - Websoft9 应用商店安装 EMQX
   - EMQX 配置 WebSocket 客户端连接，需开放 WebSocket 端口

    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mqttx/mqttx-config-emqx-websoft9.png)

2. MQTTX 连接 EMQX，并测试
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mqttx/mqttx-connect-emqx-websoft9.png)

## 配置选项{#configs}
## 管理维护{#administrator}


## 故障