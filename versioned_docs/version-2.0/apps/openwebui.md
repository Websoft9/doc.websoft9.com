---
title: Open WebUI
slug: /openwebui
tags:
  - AI模型
  - 机器学习
  - Open WebUI
---

import Meta from './_include/openwebui.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

1. Websoft9 控制台安装 Open WebUI 后，通过 **我的应用** 查看应用详情，在 **访问** 标签页中获取访问 URL

2. 根据向导创建管理员账号

3. 左上角 **选择一个模型**, 搜索 `tinydolphin`, 点击即可下载模型

4. 选择 `tinydolphin`模型，可以开始使用聊天功能


### 通过 GPU 运行

1. 创建此应用程序时选择 **cuda** 版本

2. **编排 > 马上修改**，将 `docker-compose-gpu.yml` 更改为 `docker-compose.yml`

3. 重新创建此应用

## 配置选项{#configs}

- 多语言（√）
- 设置 Ollama URL：**设置 > 管理员设置**

## 管理维护{#administrator}

## 故障