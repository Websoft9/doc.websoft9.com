---
title: Portainer
slug: /portainer
tags:
  - 容器
  - 可视化
  - k8s
  - Docker
---

import Meta from './_include/portainer.md';

<Meta name="meta" />

## 入门指南{#guide}

Websoft9 集成 Portainer 作为唯一个容器可视化管理平台，100% 保持其原生性。

所以，Portainer 的使用参考：[Websoft9 容器指南](./function/container)

### 设置 Environments

Portainer 应用启动后，默认没有设置任何 Environments（包括本机 local）：

- 如果你想要管理本机，建议直接使用 Websoft9 内置的 Portainer (Websoft9 控制台 > 容器)
- 如果你想管理其他服务器，请通过 Portainer 菜单的 Administration > Environment-related > Environments 增加本管理的节点


## 配置选项

- 企业版免费范围：5 个节点是免费的
- [Portainer CLI](https://docs.portainer.io/advanced/cli)
- [Portainer API](https://docs.portainer.io/api/access)

## 管理维护{#administrator}

## 故障

#### Portainer 无法进入初始页面？

为了安全性，Portainer 安装好后几分钟内没进入初始化页面会锁定页面。须重启 Portainer 应用即可进入初始化页面。