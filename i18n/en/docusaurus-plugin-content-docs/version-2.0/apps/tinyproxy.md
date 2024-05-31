---
title: Tinyproxy
slug: /tinyproxy
tags:
  - 轻量代理
  - 代理服务器
  - tinyproxy
---

import Meta from './_include/tinyproxy.md';

<Meta name="meta" />

## 入门指南{#guide}

### 通过代理使用 git clone

下面我们介绍如何使用 Tinyproxy 来实现 git clone:

1. 在控制台修改编排 .env 文件中的 ALLOWED，重建应用后生效

2. 使用下面的 git clone 命令
    ```
    git -c http.proxy=http://TinyproxyURL:Port clone --depth=1 https://github.com/Websoft9/docker-library
    ```


## 配置选项{#configs}

- 白名单设置：编排.env 文件的 ALLOWED，设置 0.0.0.0/0 表示允许所有 IP 访问

## 管理维护{#administrator}


## 故障
