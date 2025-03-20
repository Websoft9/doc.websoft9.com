---
title: MongoDB Compass
slug: /mongocompass
tags:
  - MongoDB
  - 桌面
  - 数据库管理
---

import Meta from './_include/mongocompass.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 MongoDB Compass 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

1. 浏览器访问后，登陆到 Mongo Compass 所在的桌面

2. 点击桌面的 MongoDB Compass 图标，进入MongoDB Compass
   ![](./assets/mongodbcompass-click-websoft9.png)

3. 点击**New Connection**，展开 **Advanced Connection Options**，输入连接信息和账号
   ![](./assets/mongodbcompass001-websoft9.png)

   > 不建议使用 URI 的方式，它受限于字符串格式

4. 连接成功，进入控制台
   ![](./assets/mongodbcompass002-websoft9.png)

## 配置选项{#configs}

## 管理维护{#administrator}

## 故障

#### Mongo Compass 内存消耗大？

是的，Mongo Compass 不是一个真正意义上的 Web 应用，它是 Websoft9 基于包含桌面的特殊容器而构建
