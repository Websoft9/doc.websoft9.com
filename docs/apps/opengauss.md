---
title: openGauss
slug: /opengauss
tags:
  - 数据库
  - 关系型
  - SQL
---

import Meta from './_include/opengauss.md';

<Meta name="meta" />

## 入门指南{#guide}


### 连接数据库

1. Websoft9 控制台安装 openGauss 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取用户名和密码

2. 进入 openGauss 容器的命令模式，使用 gsql 连接数据库

    ```
    $ su - omm
    $ gsql -d postgres -U gaussdb
    # 输入访问标签页中获取密码
    Password for user gaussdb: 
    gsql ((openGauss 6.0.0 build aee4abd5) compiled at 2024-09-29 19:14:27 commit 0 last mr  )
    Non-SSL connection (SSL connection is recommended when requiring high-security)
    Type "help" for help.

    openGauss=>
    ```

## 配置选项{#configs}

- CLI

## 管理维护{#administrator}

## 故障
