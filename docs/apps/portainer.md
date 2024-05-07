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

Websoft9 已内置运行的 Portainer，建议直接使用 Websoft9 控制台 "容器" 管理功能。   

如果您已经在 Websoft9 应用商店额外安装 Portainer，请参考下面的指引：

### 初始化

1. Websoft9 控制台安装 Portainer 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取访问网站。  
   ![](./assets/portainer-register-websoft9.png)

2. 根据向导完成管理员账号设置，进入后台后，系统提示设置 Environments

   - 管理本机的容器（推荐方案）：删除本次安装的 Portainer，直接使用 Websoft9 控制台 "容器" 管理功能

   - 管理本机的容器：修改 Portaier 编排文件，取消 `/var/run/docker.sock` 那行的注释，重建应用后生效

   - 管理非本机的容器，请根据 Environments 提示设置连接方式

3. 完成 Environments 设置及连接后，方可开始管理容器

### 操作指南

参考：[Websoft9 容器指南](./function/container)

## 配置选项

- 企业版免费范围：5 个节点是免费的
- [Portainer CLI](https://docs.portainer.io/advanced/cli)
- [Portainer API](https://docs.portainer.io/api/access)

## 管理维护{#administrator}

## 故障

#### Portainer 无法进入初始页面？

问题原因：为了安全性，Portainer 安装好后几分钟内没进入初始化页面会锁定页面   
解决方案：重启 Portainer 应用