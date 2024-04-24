---
title: Answer
slug: /answer
tags:
  - 问答平台
  - 论坛社区
  - answer
---

import Meta from './_include/answer.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 Answer 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  


## 配置选项{#configs}

- 多语言（✅）


## 管理维护{#administrator}


## 故障

#### 自动安装失败?

Answer 自动安装失败的原因可能有两点：

1. Answer 镜像所有的环境变量都需要设置，否则就不会切换到自动安装模式
2. Answer 容器启动后，如果在第一时刻没有连接到可用的数据库，自动安装就会跳过，不会尝试等待或再次安装