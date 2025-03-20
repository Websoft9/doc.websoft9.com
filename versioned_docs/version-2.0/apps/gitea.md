---
title: Gitea
slug: /gitea
tags:
  - Gogs
  - Gitlab
  - DevOps
---

import Meta from './_include/gitea.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

1. Websoft9 控制台安装 Gitea 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息

2. 根据安装向导完成初始化，请勿修改 **一般设置** 项目中的任何参数

   - 基础 URL：安装向导程序自动获取浏览器 URL 填充
   - HTTP 服务端口：此处为容器端口，不可以更改
   - SSH 服务端口：此处为容器端口和对应的宿主机端口，已经通过环境变量设置，不可以更改
   - 数据库设置：请选择 SQLite。如果选择其他数据库，需提前准备可用的数据库


3. 管理员帐号设置 或 登陆后注册第一个账号（均为管理员账号）

## 配置选项{#configs}

- 多语言（✅）
- 配置文件：*gitea/conf/app.ini*

## 管理维护{#administrator}

## 故障
