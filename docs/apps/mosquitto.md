---
title: Mosquitto
slug: /mosquitto
tags:
  - 物联网
  - MQTT
  - 消息
---

import Meta from './_include/mosquitto.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 Mosquitto 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

## 配置选项{#configs}

- 配置文件：mosquitto.config
- 用户认证（√）

## 管理维护{#administrator}


## 故障

#### 容器日志 Error: Address not available？

Mosquitto 2.0 requires you to configure listeners and authentication before it will allow connections from anything other than the loopback interface. 