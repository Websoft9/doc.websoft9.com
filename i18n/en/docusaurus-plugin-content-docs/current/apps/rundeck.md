---
title: Rundeck
slug: /rundeck
tags:
  - 自动化系统
  - DevOps
  - Runbook
---

import Meta from './_include/rundeck.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

1. Websoft9 控制台安装 Rundeck 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

2. 登录后立即修改密码


## 配置选项{#configs}

- 多语言（√）

## 管理维护{#administrator}

## 故障

#### 通过 IP 无法访问 Rundeck ？

需要将环境变量 **RUNDECK_GRAILS_URL** 修改为 http://$W9_URL:W9_HTTP_PORT_SET ， 重建应用后生效。