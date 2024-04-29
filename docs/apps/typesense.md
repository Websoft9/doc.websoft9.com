---
title: Typesense
slug: /typesense
tags:
  - 即时搜索
  - 网站全文搜索
  - typesense
  - Algolia
---

import Meta from './_include/typesense.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

1. Websoft9 控制台安装 Typesense 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息 

2. 浏览器访问：URL+路径 **health** 可查看 Typesense 服务是否正常启动
    ```
    # test health
    curl "http://URL/health"

    # test collections
    curl "http://URL/collections" -H "X-TYPESENSE-API-KEY: f324f596-f07b-XP7bz4lUmA@Ln6XH"
    ```

## 配置选项{#configs}

- Scraper Config File 配置：docker-compose.yml 中 typesense-scraper 容器的环境变量 **CONFIG**
- 架构：typesense-scraper 是数据爬虫，typesense 是数据存储和搜索引擎

## 管理维护{#administrator}

## 故障
