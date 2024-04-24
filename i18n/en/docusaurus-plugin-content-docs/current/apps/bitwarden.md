---
title: Bitwarden
slug: /bitwarden
tags:
  - 安全密码存储
  - 密码管理
  - bitwarden
---

import Meta from './_include/bitwarden.md';

<Meta name="meta" />

## 入门指南{#guide}


### 初始化{#wizard}

Websoft9 控制台安装 Bitwarden 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

1. 确保安装时已填写正确的 ID 和 Key。如果没有，需到 Bitwarden [申请](https://bitwarden.com/host) ，然后通过**应用编排**的方式重建容器  

2. 将 Bitwarden 应用设置为 HTTPS 访问（必须）

3. 通过域名访问 Bitwarden ，开始初始化（包含创建初始管理员账号）


## 配置选项{#configs}

## 管理维护{#administrator}

## 故障

#### 初始化无法创建账号 ？

必须使用 https 访问，否则创建账号失败。