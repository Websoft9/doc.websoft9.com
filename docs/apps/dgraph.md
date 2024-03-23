---
title: Dgraph
slug: /dgraph
tags:
  - 图数据库
  - 分布式
  - NoSQL
---

import Meta from './_include/dgraph.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

1. Websoft9 控制台安装 Dgraph 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息

2. 【Launch Latest 】，进入 Console 界面

### 测试公开的数据库节点

1. Metal 可以先连接到官方公开的实例 https://play.dgraph.io 上，用于测试。

2. 连接成功后运行下面代码，便可以运行得到关系图
   ```
   {
    user(func: eq(name, "Alice")) {
        name
        friend {
        name
        age
        }
    }
    }
   ```

### 测试本应用的数据库节点（alpha）

1. 连接到 http://URL:port 

   - URL 不支持容器名称，必须是公网 IP 或 域名
   - port 是 alpha（数据库）节点的外网端口

2. 无需密码即可登录

> groot 密码设置是企业版功能（ACL）

## 配置选项{#configs}

- Dgraph 应用包含三个节点：zero(集群), alpha（数据库）, ratel（图形化）
- ACL：企业版功能

## 管理维护{#administrator}

## 故障

#### ratel 加载不完整？

应用自身包含一些外部 js 导致

#### ratel 无密码即可访问？

是的，建议通过 **网关** 进行密码控制

#### whitelist and token 有什么用？

控制对数据库的管理操作，例如：建表。但是无法控制查询，即任何外部连接都可以查询。