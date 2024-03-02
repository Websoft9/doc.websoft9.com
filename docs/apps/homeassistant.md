---
title: Home Assistant
slug: /homeassistant
tags:
  - 物联网
  - IoT
  - 家庭助理
---

import Meta from './_include/homeassistant.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 Home Assistant 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

### 连接 MQTT

Home Assistant 应用默认并不包括 MQTT 服务，建议在 Websoft9 控制台安装开源 MQTT 服务器 [Eclipse Mosquitto](./mosquitto)。   

安装完成后，参考：[MQTT Configuration](https://www.home-assistant.io/integrations/mqtt) 完成连接与配置。  


## 配置选项{#configs}

- [配置文件 configuration.yaml](https://www.home-assistant.io/docs/configuration/)：已挂载到持久化目录中
- [Home Assistant Add-ons](https://github.com/home-assistant/addons)：Add-ons 可安：MariaDB, Nginx 等应用，故仅 Linux 原生安装可用，容器版不可用。

## 管理维护{#administrator}


## 故障