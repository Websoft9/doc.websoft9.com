---
title: SQLite
slug: /sqlite
tags:
  - 云数据库
  - SQL
---

import Meta from './_include/sqlite.md';

<Meta name="meta" />

## 入门指南{#guide}

### 验证安装{#wizard}

1. Websoft9 控制台安装 SQLite 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取访问信息。  

2. 进入 SQLite 容器的命令模式，运行 `sqlite3` 命令
   ```
   [root@VM-0-11-centos ~]# sqlite3
   SQLite version 3.29.0 2019-07-10 17:32:03
   Enter ".help" for usage hints.
   Connected to a transient in-memory database.
   Use ".open FILENAME" to reopen on a persistent database.
   sqlite>
   ```

## 配置选项{#configs}

- cli：`sqlite3 --help` 

## 管理维护{#administrator}

- 升级：二进制替换 + sqlite3.conf 迁移

## 故障