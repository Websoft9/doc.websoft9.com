---
title: Apache Traffic Server
slug: /trafficserver
tags:
  - HTTP 缓存
  - 反向代理
  - trafficserver
---

import Meta from './_include/trafficserver.md';

<Meta name="meta" />

## 入门指南{#guide}

### WordPress 设置 Apache Traffic Server 缓存

1. 分别在 Websoft9 控制台安装 WordPress 和 Apache Traffic Server 两个应用
   > 确保 Apache Traffic Server 配置的域名是最终提供给用户访问的域名

2. 编辑 Apache Traffic Server 应用的 `remap.config` 文件中相关参数，将 WordPress 容器名作为连接点
   ```
    map / http://wordpress_7l1io/
   ```

3. 重建 Apache Traffic Server 应用后，Apache Traffic Server 已经将 WordPress 缓存

4. 访问 Apache Traffic Server 所绑定的域名，便发现访问速度大大提升   

## 配置选项{#configs}

## 管理维护{#administrator}

## 故障
