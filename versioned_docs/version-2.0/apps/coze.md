---
title: Coze
slug: /coze
tags:
  - 编程助手
  - AI 智能体
  - Coze
---

import Meta from './_include/coze.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

1. Websoft9 控制台安装 Coze 后，通过 **我的应用** 查看应用详情，在 **访问** 标签页中获取访问 URL 。  

2. 本地浏览器访问 URL，完成注册流程。

### 设置 AI 模型

Websoft9 控制台安装的 Coze，还不能使用其主体功能，需要进行如下步骤:

1. [编排 HuggingChat 应用](https://support.websoft9.com/docs/app-compose#dynamic)，编辑 `.env`文件，设置如下变量（以Deepseek模型为例）

   ```
   MODEL_PROTOCOL_0="ark"
   MODEL_OPENCOZE_ID_0="100001"
   MODEL_NAME_0="deepseek"                      # 模型名称（可自定义）
   MODEL_ID_0="deepseek-reasoner"               # 供应商给出的模型ID
   MODEL_API_KEY_0="sk-xxxxxxxxxxxxxxxxxxxxxxx" # API密钥
   MODEL_BASE_URL_0="https://api.deepseek.com"  # 模型基础url
   ```

2. 重建应用后创建 AI 智能体开始工作了

## 配置选项{#configs}

## 管理维护{#administrator}

## 故障
