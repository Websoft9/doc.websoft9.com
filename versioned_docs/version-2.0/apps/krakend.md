---
title: KrakenD
slug: /krakend
tags:
  - 统一网关
  - API 网关
  - KrakenD
---

import Meta from './_include/krakend.md';

<Meta name="meta" />

## 入门指南{#guide}  

### 登录后台{#console}

Websoft9 控制台安装 KrakenD 后，通过 **我的应用** 查看应用详情，在 **访问** 标签页中获取登录信息。  

### 添加上游 API

1. [编排 KrakenD 应用](https://support.websoft9.com/docs/app-compose#dynamic)，将 `src/krakend.json` 的 endpoints数组增加一项，如下

```
{
  "endpoint": "/api/users",
  "method": "GET",
  "timeout": "5000ms",
    {
      "url_pattern": "/api/users",
      "host": ["http://localhost:9000"],
      "method": "GET"
    }
  ]
}
```

2. 重建应用后即可通过统一路径访问上游API


## 配置选项{#configs}

## 管理维护{#administrator}

## 故障
