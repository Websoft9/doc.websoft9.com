---
title: Traefik
slug: /traefik
tags:
  - Web 面板
  - 可视化
  - GUI
---

import Meta from './_include/traefik.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 Traefik 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  



## 配置选项{#configs}


## 管理维护{#administrator}


## 故障

#### 无法访问 Traefik Dashboard 和 API ？

8080 端口由于安全考虑，没有直接绑定到宿主机。Nginx proxy 的 location /dashboard {} 方案也无法达成目标