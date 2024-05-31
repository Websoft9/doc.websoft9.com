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

### 连接 MQTT

Home Assistant 应用默认并不包括 MQTT 服务，故：

1. 准备好 MQTT服务或者在 Websoft9 应用商店安装开源 MQTT 服务器 [Eclipse Mosquitto](./mosquitto)。   

2. 参考：[MQTT Configuration](https://www.home-assistant.io/integrations/mqtt) 完成连接与配置。  


## 配置选项{#configs}

- [配置文件](https://www.home-assistant.io/docs/configuration/)目录（已挂载）：/config
- [Home Assistant Add-ons](https://github.com/home-assistant/addons)：仅 Linux 原生安装可用，容器版不可用。

## 管理维护{#administrator}


## 故障

#### 无法通过域名访问 Home Assistant？

目前能仅通过 IP 和端口来访问，通过 Nginx 转发到域名还没有方案