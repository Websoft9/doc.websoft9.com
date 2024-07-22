---
title: Prometheus
slug: /prometheus
tags:
  - 监控
  - 报警
  - 时序数据库
---

import Meta from './_include/prometheus.md';

<Meta name="meta" />

## 入门指南{#guide}

### 访问后台{#wizard}

1. Websoft9 控制台安装 Prometheus 后，通过 **我的应用** 查看应用详情，在 **访问** 标签页中获取访问信息

2. Prometheus 无需认证即可访问，如需控制访问，请通过 Websoft9 网关设置。
   ![](./assets/prometheus-backend-websoft9.png)

### 集成 Grafana {#grafana}

Grafana 可以作为 Promethus 的可视化呈现，具体参考：[GRAFANA SUPPORT FOR PROMETHEUS](https://prometheus.io/docs/visualization/grafana/)

## 配置选项{#configs}

- 配置文件（已挂载）：*/etc/prometheus/prometheus.yml* 
- 数据采集方式：主要使用拉取（Pull）方式，同时引入 Pushgateway 接受被采集端的推送数据，然后再从 Pushgateway 中拉取。 
- [basic auth](https://prometheus.io/docs/guides/basic-auth/#hashing-a-password)
- 连接 Alertmanager 和 Pushgateway：需执行增加配置文件实现连接

## 管理维护{#administrator}

## 故障
