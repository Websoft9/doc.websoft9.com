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

1. Websoft9 控制台安装 Gitea 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息 

2. 登陆后注册账号，注册后的第一个账号默认为管理员账号

## 配置选项{#configs}

- 多语言（✅）
- 配置文件：gitea/conf/app.ini
- URL: 主要来源于客户端的浏览器，不是环境变量，故不必设置各种与URL或domain有关的环境变量。
- SSH_PORT 是容器的，也是宿主机的
- HTTP_PORT 是容器的

## 管理维护{#administrator}


## 故障