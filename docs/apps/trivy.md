---
title: Trivy
slug: /trivy
tags:
  - 杀毒软件
  - 安全保护
  - Trivy
---

import Meta from './_include/trivy.md';

<Meta name="meta" />

## 入门指南{#guide}

### 扫描验证{#wizard}

1. Websoft9 控制台安装 Trivy 后，通过 **我的应用** 查看应用详情，在 **访问** 标签页中获取登录信息。  

2. 进入 Trivy 容器, 开始病毒扫描:
  ```
  trivy fs /scandir
  ```

## 配置选项{#configs}

- CLI（√）: `trivy`

## 管理维护{#administrator}

## 故障

#### 如何快速扫描?

进入容器，执行下列命令：
  ```
  apk add --no-cache python3 && ln -sf python3 /usr/bin/python 
  trivy fs  --scanners vuln /tmp/usr/share 
  ```