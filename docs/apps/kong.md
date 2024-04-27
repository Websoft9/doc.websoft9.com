---
title: Kong
slug: /kong
tags:
  - API
  - 网关
  - Nginx
---

import Meta from './_include/kong.md';

<Meta name="meta" />

## 入门指南{#guide}

### 验证安装{#wizard}

Websoft9 控制台安装 Kong 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

1. Kong 共有 Kong HTTP, Kong Admin API, Kong GUI 三个服务，需按需开启端口

   - 如果配置域名访问： 仅需开启 Kong Admin API 端口
   - 如果是端口访问：需开启 Kong HTTP, Kong Admin API, Kong GUI 所有端口

2. 本地浏览器访问 Kong Manager 界面：
   - 域名访问：`http://域名/admin`
   - IP 访问：`http://IP:Kong GUI Port/admin`

3. 验证 Kong HTTP 服务
   ```
   curl -i -X GET --url http://URL/services
   ```

4. 通过 Kong Manager 后台或 curl 配置 Kong Admin API

### Kong Manager 认证访问

Kong Manager OSS 默认不支持账号密码访问，需用户通过 **Websoft9 网关** 界面为它设置访问控制。

### Kong Admin API 认证访问

要为 Kong Admin API 设置认证访问，您可以使用 Kong 自身的认证插件。Kong 提供了多种认证插件，例如 Key Authentication、Basic Authentication、OAuth 2.0 Authentication 等。  

具体参考：[Authentication Reference](https://docs.konghq.com/gateway/latest/kong-plugins/authentication/reference/)


## 配置选项{#configs}

- 可视化管理控制台 Kong Manager OSS（√）：仅企业版支持账号密码认证

- [Kong CLI](https://docs.konghq.com/gateway/latest/reference/cli) (√)

- 管理端访问方式：URL/admin（更改了 Kong 的默认设置）

- 端口说明：
  - Kong HTTP Port（网关 HTTP 服务 API 端口）
  - Kong Admin API Port（管理端 API 服务端口）
  - Kong GUI Port（管理端可视化控制台端口）

## 管理维护{#administrator}

## 故障