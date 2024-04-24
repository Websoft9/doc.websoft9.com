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

Websoft9 控制台安装 Gogs 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

1. 使用本地电脑浏览器访问，进入初始化页面。进入页面底部选择合适的语言。  
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-language-websoft9.png)

2. 设置数据库连接

   - 数据库类型： MySQL
   - 主机名：gogs-db

    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-db-websoft9.png)

2. 设置 Gogs 的应用基本参数

   - 域名：公网IP 或 真实域名
   - SSH 端口： 10022，可从 Gogs 编排的 .env 文件中查询
   - HTTP 端口： 80
   - 应用 URL：`http://公网IP`  或  `http://域名:端口`

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-admin-websoft9.png)

3. 设置管理账号  

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-installadmin-websoft9.png)

4. 安装成功后，进入系统后台

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-dashboard-websoft9.png)

## 配置选项{#configs}

- 命令行：`./gogs -h`
- [Web 钩子](https://gogs.io/docs/features/webhook)
- 多语言（✅）
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-language-websoft9.png)

## 管理维护{#administrator}

## 故障