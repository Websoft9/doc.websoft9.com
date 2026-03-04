---
title: SigNoz
slug: /signoz
tags:
  - 云原生 APM
  - 观测性平台
  - SigNoz
---

import Meta from './_include/signoz.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

1. Websoft9 控制台安装 SigNoz 后，通过 **我的应用** 查看应用详情，在 **访问** 标签页中获取 URL  

2. 本地浏览器访问 URL，注册后即可使用

### 监控应用

1. [编排 SigNoz 应用](https://support.websoft9.com/docs/app-compose#dynamic)，编辑 `docker-compose.yml`文件，映射 otel-collector 的端口到外网

2. 使用 OpenTelemetry SDK [集成](https://signoz.io/docs/instrumentation/)到你的应用中

3. 配置 OTLP 导出器指向
    - gRPC: `http://yourip:4317`
    - HTTP: `http://yourip:4318`

## 配置选项{#configs}

## 管理维护{#administrator}

## 故障