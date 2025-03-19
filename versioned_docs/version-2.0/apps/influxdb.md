---
title: InfluxDB
slug: /influxdb
tags:
  - 时间序列数据库
  - 物联网数据库
  - influxdb
---

import Meta from './_include/influxdb.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

1. Websoft9 控制台安装 InfluxDB 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息

2. 根据安装向导创建组织、用户和 bucket，完成后点击 **Get Started** 进入 Dashboard 开始使用


## 配置选项{#configs}

- Dashboard：InfluxDB2.x 以上自带

- 配置参数的三种设置方式：

  - 容器配置文件：*/etc/influxdb2/config.yml*
  - 容器环境变量
  - 容器 docker-compose.yml 文件中的 command （优先级最高）

## 管理维护{#administrator}

## 故障
