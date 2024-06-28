---
title: Caddy
slug: /caddy
tags:
  - HTTP 服务器
  - https
  - 微服务
  - 云原生
---

import Meta from './_include/caddy.md';

<Meta name="meta" />

## 入门指南{#guide}

Websoft9 提供的 Caddy 应用两个用途：

- 直接运行静态网站
- 作为反向代理服务

下面我们分别对它的使用方法做出详细的说明

### 部署静态网站

1. Websoft9 控制台安装 Caddy 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取访问信息

2. 参考 [基于程序环境部署应用](runtime) 部署静态网站

### 反向代理其他应用

参考下面的步骤，体验 Caddy 反向代理的能力：

1. Websoft9 控制台 "应用商店" 分别运行一个 **Netdata** 和 **Caddy**

2. 通过 "我的应用" > "Caddy" 的**编排** 标签页中修改 src/Caddyfile 为如下的内容
   ```
   :80 {
    reverse_proxy http://netdata_h31py:19999
   }
   ```

3. 重启 Caddy 应用，访问 Caddy 的 URL，就会发现应用已指向了 Netdata 的页面

在 Websoft9 托管平台中，上面的 Netdata 访问的路由： 用户 > Websoft9 网关 > Caddy > Netdata


## 配置选项{#configs}

- 容器中应用根目录：*/srv*
- Caddy 容器端口：80
- 监控所有 URL 的通配符写法： `:80`
- [API](https://caddyserver.com/docs/quick-starts/api)
- CLI：`caddy help`
- 配置[模板](https://caddy.community/c/wiki/13)
- Caddy 配置文件：*/etc/caddy/Caddyfile*，已挂载到编排文件 /src/Caddyfile。 

## 管理维护{#administrator}

## 故障
