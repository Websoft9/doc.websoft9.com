---
title: Gogs
slug: /gogs
tags:
  - Git
  - 代码仓库
  - DevOps
---

import Meta from './_include/gogs.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 Gogs 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

1. 使用本地电脑浏览器访问 URL，进入初始化页面  

2. 数据库设置：请选择 SQLite。如果选择其他数据库，需提前准可用的数据库

3. 应用基本设置：此项非常容易填错，务必参考下面的说明

   - 域名：使用浏览器当前访问的 URL（可能包含端口），去掉 `http://` 前缀， 保留后面的部分
   - 应用 URL：使用浏览器当前访问的 URL
   - SSH 端口：安装 Gogs 时，所设置的映射到服务器的端口
   - HTTP 端口：不修改

4. 设置管理账号和邮箱（ admin 是系统保留关键字，不可做用户名）

5. 安装成功后，进入系统后台

   ![](./assets/gogs-dashboard-websoft9.png)

## 配置选项{#configs}

- 命令行：`./gogs -h`
- [Web 钩子](https://gogs.io/docs/features/webhook)
- 多语言（✅）：自动适应浏览器语言，也可以在底部菜单进行选择

## 管理维护{#administrator}

## 故障