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

自动安装失败的原因可能有两点：
1. 和自动安装相关的环境变量没有设置，具体请在编排中查看 **.env** 文件
2. **docker-compose.yml** 中没有指定主容器对数据库的依赖，需要数据库检查状态成功后再启动主容器
