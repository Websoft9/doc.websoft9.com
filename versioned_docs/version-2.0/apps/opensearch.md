---
title: OpenSearch
slug: /opensearch
tags:
  - 搜索引擎
  - 数据可观测
  - opensearch
---

import Meta from './_include/opensearch.md';

<Meta name="meta" />

## 入门指南{#guide}

### OpenSearch Dashboard{#dashboard}

Websoft9 控制台安装 OpenSearch 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

## 配置选项{#configs}

- [vm.max_map_count=262144](https://opensearch.org/docs/latest/opensearch/install/important-settings/) on Linux (应用启动时自动设置)

## 管理维护{#administrator}

## 故障

#### OpenSearch 无法启动？

确保宿主机参数 [vm.max_map_count=262144](https://opensearch.org/docs/latest/opensearch/install/important-settings/) 

#### 面板无法连接到 OpenSearch？

确保 OPENSEARCH_HOSTS 不包含下划线 _
