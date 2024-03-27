---
title: PostgREST
slug: /postgrest
tags:
  - 数据库API
  - postgresql
  - postgrest
---

import Meta from './_include/postgrest.md';

<Meta name="meta" />

## 入门指南{#guide}

### 安装{#wizard}

Websoft9 控制台安装时，需要填写准确的 Postgresql 连接 URI，否则容器日志中会有错误。 

## 配置选项{#configs}

- 配置文件：可以通过环境变量传递配置项
- 连接 Postgre 数据库：应用**编排**修改 .env 文件中的 **W9_POSTGRESQL_URI_SET**


## 管理维护{#administrator}


## 故障

#### Database connection error?

确保 Postgresql 的 URI 准确无误，且可被 PostgREST 访问。  

