---
title: Strapi
slug: /strapi
tags:
  - 后端即服务
  - 无头内容管理系统
  - strapi
---

import Meta from './_include/strapi.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

1. Websoft9 控制台安装 Strapi 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

2. Strapi 容器启动首次启动时，会在线拉取外部软件包，需要等待几分钟后才能进入初始页面

### 自建数据模型

1. **Plugins > Content-type Builder** 增加一个数据集，假如名为为：websoft9

2. Users 菜单下增加一个用户，设置角色为 public

3. **Settings > USERS & PERMISSIONS PLUGIN > Roles** 编辑 public role，使之有权限访问 websoft9 数据集

4. 访问下面的 URL 便可以获取数据

   ```
   # 获取所有数据
   http://URL/websoft9
   
   # 获取第 1 条数据
   http://URL/websoft9/1
   ```


## 配置选项{#configs}

- 多语言（✅）

## 管理维护{#administrator}

## 故障

#### Strapi 首次启动报错？

问题分析：Strapi 首次启动会安装 **Node** 以及从 Github 下载软件包，可能由于网络问题导致失败。   
解决方案：确保服务器可以顺利访问 npm 仓库和 Github
