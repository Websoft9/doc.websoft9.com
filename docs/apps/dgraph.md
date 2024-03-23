---
title: Dgraph
slug: /dgraph
tags:
  - Web 面板
  - 可视化
  - GUI
---

import Meta from './_include/dgraph.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

1. Websoft9 控制台安装 Dgraph 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息

2. 【Launch Latest 】，进入 Console 界面

### 测试公开的实例

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

## 配置选项{#configs}

## 管理维护{#administrator}

## 故障