---
title: CoreDNS
slug: /coredns
tags:
  - Web 面板
  - 可视化
  - GUI
---

import Meta from './_include/coredns.md';

<Meta name="meta" />

## 入门指南{#guide}

### 快速配置{#wizard}

1. Websoft9 控制台安装 CoreDNS 后，通过 **我的应用** 查看应用详情，点击 **编排** 页面的 **马上修改** 开始配置

2. `.env` 文件中的 **W9_INNERIP_SET** 环境变量的值确保是 CoreDNS 容器的宿主机的内网 IP 地址

3. 默认提供了两个配置文件，您可以根据这个配置文件进行个性化设置

   - Corefile: 主配置文件，包含引入的其他配置文件以及 hosts 映射设置
   - db.demo.inner：[Zone file](https://coredns.io/plugins/file/) 模板，其中配置了一个泛域名解析


## 配置选项{#configs}

## 管理维护{#administrator}

## 故障
