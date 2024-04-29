---
title: Penpot
slug: /penpot
tags:
  - 原型设计
  - 设计协同
  - 用户界面
  - 画布
---

import Meta from './_include/penpot.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 Penpot 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  


## 配置选项{#configs}
## 管理维护{#administrator}

## 故障

#### 项目的封面图片无法显示？

问题描述：当采用 **IP:端口** 访问 Penpot 时，所创建的项目封面图片无法显示    
问题原因：应用的环境变量 PENPOT_PUBLIC_URI 没有包含端口    

#### 无法完成首次用户注册？

需确保 backend 容器的环境变量 **PENPOT_FLAGS** 中包含：disable-secure-session-cookies

