---
title: Parse
slug: /parse
tags:
  - npm
  - Node.js
  - BaaS
  - 后端即服务
  - 低代码开发
  - 开发框架
---

import Meta from './_include/parse.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 Parse 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

1. 由于 Parse 不可通过 IP 访问，故必须先做好域名绑定

2. 使用本地电脑的 Chrome 或 Firefox 浏览器访问域名，就进入 Parse Dashboard 登录页面
  ![Parse Dashboard 登录](https://libs.websoft9.com/Websoft9/DocsPicture/en/parseserver/ParseServer-loginpage-websoft9.png)

3. 输入账号和密码，登录后的界面如下
  ![Parse Dashboard 后台界面](https://libs.websoft9.com/Websoft9/DocsPicture/en/parseserver/parse-backend-websoft9.png)


## 配置选项{#configs}

- [Parse API](https://docs.parseplatform.org/parse-server/guide/#using-parse-sdks-with-parse-server)

## 管理维护{#administrator}

### 升级

Parse 采用 NPM 来管理升级

  ```
  # update server
  npm update -g  parse-server

  # update dashboard
  npm update -g  parse-dashboard
  ```

## 故障