---
title: Mosquitto
slug: /mosquitto
tags:
  - 物联网
  - MQTT
  - 消息队列
---

import Meta from './_include/mosquitto.md';

<Meta name="meta" />

## 入门指南{#guide}

### 开启认证

Mosquitto 开启认证有[多种方式](https://mosquitto.org/documentation/authentication-methods/)，下面我们介绍其中的[密码文件](https://mosquitto.org/man/mosquitto_passwd-1.html)方式：

1. 进入 Mosquitto 容器，参考下面的命令创建一个密码文件（文件名、用户名和密码均可自定义）
    ```
    mosquitto_passwd -H sha512  -c -b /mosquitto/config/passwd_file yourusername yourpasssord
    ```

2. 修改配置文件中的如下两项（必须）：

   - password_file 设置为： */mosquitto/passwd_file*
   - allow_anonymous 设置为： false

3. 重建应用后生效

### 可视化管理

参考：[MQTTX](./mqttx)

## 配置选项{#configs}

- 配置文件（已挂载）：*/mosquitto/config/mosquitto.conf*
- 用户认证（√）

## 管理维护{#administrator}


## 故障

#### 容器日志 Error: Address not available？

Mosquitto 2.0 要求您在允许从除了回环接口以外的任何地方连接之前，必须配置监听器和身份验证。
