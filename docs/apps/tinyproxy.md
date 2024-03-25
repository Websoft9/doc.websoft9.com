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

### 开启允许客户端地址

在控制台修改编排 .env 文件中的 ALLOWED 地址，添加你需要代理的服务器IP，重建应用后即可使用。

### 如何使用代理 git clone?

开启允许客户端地址后，执行下面命令：

```
git -c http.proxy=http://Tinyproxy服务端IP:TinyproxyPort clone --depth=1 https://github.com/Websoft9/docker-library
```


## 配置选项{#configs}



## 管理维护{#administrator}



## 故障
