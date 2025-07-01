---
title: Varnish
slug: /varnish
tags:
  - HTTP 缓存
  - 反向代理
  - Varnish
---

import Meta from './_include/varnish.md';

<Meta name="meta" />

## 入门指南{#guide}

### 反向代理应用

1. Websoft9 控制台安装 Varnish 后，通过 **我的应用** 查看应用详情

2. 点击**我的应用 > 编排 > 马上修改**，编辑 `src/default.vcl`

3. 修改.host和.port 分别为 Websoft9 控制台安装应用的容器ID和容器内部端口

4. 重建应用，HTTP 缓存生效，访问应用速度大大加快

## 配置选项{#configs}

## 管理维护{#administrator}

## 故障
