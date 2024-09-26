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
    - 在 **容器** 标签页中 exec 进入主容器，运行下面的命令，获取初始化 **Token**
      ```
      cat /opt/youtrack/conf/internal/services/configurationWizard/wizard_token.txt
      ```

2. 本地浏览器访问 URL， 根据向导依次完成后续步骤


### 更换 Base URL

参考官方文档: [Change the Base URL or Listen Port](https://www.jetbrains.com/help/youtrack/server/change-base-url-listen-port.html)

## 配置选项{#configs}

- 多语言（√）

## 管理维护{#administrator}

## 故障