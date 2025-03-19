---
title: Traefik
slug: /traefik
tags:
  - HTTP Server
  - 方向代理
  - 证书
  - 网关
---

import Meta from './_include/traefik.md';

<Meta name="meta" />

## 入门指南{#guide}

### 启用 Dashboard{#wizard}

1. Websoft9 控制台安装 Traefik 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取访问信息

2. 可选：通过 Websoft9 网关，将 Traefik Dashboard 的 8080 端口转发到外网访问

## 配置选项{#configs}

- 容器端口：80 是 HTTP 服务端口，8080 是 Dashboard 端口

## 管理维护{#administrator}


## 故障

#### 无法访问 Traefik Dashboard？

8080 端口由于安全考虑，没有直接映射到宿主机