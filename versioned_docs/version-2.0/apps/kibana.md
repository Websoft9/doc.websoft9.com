---
title: Kibana
slug: /kibana
tags:
  - Elastic
  - 可视化
  - 数据分析
---

import Meta from './_include/kibana.md';

<Meta name="meta" />

## 入门指南{#guide}

### 连接 Elasticsearch{#wizard}

Websoft9 控制台安装 Kibana 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

1. 提前准备 Elasticsearch 的 Enrollment Token 和账号密码等信息

2. 登录 Kibana 的初始化界面，输入 [Elasticsearch Enrollment Token](./elasticsearch#token) 信息验证（首次登陆需要）

3. 验证通过后，会出现要求输入用户名和密码的界面
 
4. 验证用户名和密码后，可以进入可视化控制台

## 配置选项{#configs}

- kibana.yml 的[配置项](https://www.elastic.co/guide/en/kibana/current/settings.html)与镜像环境变量具有[转换关系](https://www.elastic.co/guide/en/kibana/current/docker.html#environment-variable-config)

## 管理维护{#administrator}

## 故障