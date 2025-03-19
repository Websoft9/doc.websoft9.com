---
title: Chronograf
slug: /chronograf
tags:
  - InfluxDB管理
  - InfluxDB可视化
  - chronograf 
---

import Meta from './_include/chronograf.md';

<Meta name="meta" />

## 入门指南{#guide}

### 连接 InfluxDB {#wizard}

下面以连接 InfluxDB2.x 为例，详细介绍连接方式：

1. 准备好需要管理的 InfluxDB 

2. 访问 Chronograf，增加一个 InfluxDB 连接，首选勾选 **InfluxDB v2 Auth**，然后填写如下参数：
   
   - Connection URL: InfluxDB 的访问 URL
   - Connection Name： 自定义
   - Organization：InfluxDB 的 organization（必填项）
   - Token：InfluxDB 的 token


## 配置选项{#configs}

- 连接多个数据库（√）
- 支持的 InfluxDB 版本：InfluxDB 1.x, InfluxDB 2.x

## 管理维护{#administrator}


## 故障
