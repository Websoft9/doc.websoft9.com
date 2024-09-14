---
title: YouTrack
slug: /youtrack
tags:
  - 敏捷开发
  - 项目管理
  - YouTrack
---

import Meta from './_include/youtrack.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

1. Websoft9 控制台安装 YouTrack 后，通过 **我的应用** 查看应用详情

    - 在 **访问** 标签页中获取 **URL**
    - 在 **容器** 标签页中获取 **主容器ID**

2. 本地浏览器访问步骤1的 **URL**，进入初始化页面

3. 运行命令获取 Token，初始化页面输入Token 进入下一步

    ```
    docker exec 步骤1获取的主容器ID cat /opt/youtrack/conf/internal/services/configurationWizard/wizard_token.txt
    ```

4. 页面点击 **Set up**，按照向导提示完成初始化即可开始使用 YouTrack

### 更改 Base URL

详细请参照: [更改 Base URL](https://www.jetbrains.com/help/youtrack/server/change-base-url-listen-port.html)

## 配置选项{#configs}

- 多语言（√）

## 管理维护{#administrator}

## 故障