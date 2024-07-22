---
title: TeamCity
slug: /teamcity
tags:
  - DevOps
  - CI
  - 流水线
---

import Meta from './_include/teamcity.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

1. Websoft9 控制台安装 TeamCity 后，通过 "我的应用" 查看应用详情
   - 在 "访问" 标签页中获取访问 URL
   - 在 "数据库" 标签页获取数据库账号信息  

2. 访问 URL 进入初始化页面，点击 "proceed" 开始后续步骤

3. **Database connection setup** 步骤填写应用预制的数据库：

   - database type: MySQL（选择后需点击下载 JDBC 驱动的链接）   
   - Database host：从 TeamCity 应用管理界面获取
   - Database Name: `teamcity`
   - User name: `teamcity` 或 `root`
   - Password: 从 TeamCity 应用管理界面获取

5. 依次完成创建账号等后续步骤后，登录 TeamCity 后台
   ![](./assets/teamcity-main-websoft9.png)

6. 修正 Server URL：**Administration** > **Global Settings**

### 连接 TeamCity Agent

TeamCity 应用默认已启动  TeamCity Agent。  

连接它，需进入 TeamCity 后台： **Agents > UNAUTHORIZED AGENTS** 中进行 **Authorize** 操作


## 配置选项{#configs}

- 设置 Server URL：TeamCity 控制台 **Administration > Global Settings**

## 管理维护{#administrator}

## 故障

#### Agent 无法连接到 TeamCity?

TeamCity Agent 连接 TeamCity 时，不支持主机名中包含 "_"，确保符合这个要求。
