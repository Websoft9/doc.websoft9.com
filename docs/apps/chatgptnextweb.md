---
title: ChatGPT Next Web
slug: /chatgptnextweb
tags:
  - ChatGPT
  - AI
  - OpenAI
  - 人工智能
  - 聊天
---

import Meta from './_include/chatgptnextweb.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 ChatGPT Next Web 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

1. 点击 ChatGPT Next Web 右下角的 **设置** 按钮

2. 找到设置项的 **访问密码**，设置从 Websoft9 控制台获得的密码

3. 模型（Model）列表中选择一个所需的项

3. 开始使用

### 切换 Azure 服务

Azure 提供了优化后的 OpenAPi 服务，ChatGPT Next Web 支持 Azure AI 的接入

1. 编辑 ChatGPT Next Web 编排文件 .env

2. 删除 OpenAI 的可以，输入 Azure 相关的信息
   ```
   AZURE_URL=
   AZURE_API_KEY=
   AZURE_API_VERSION=2023-12-01-preview
   ```

3. 重建应用后生效

### 节省成本

- 尽量使用**新的聊天**，减少不必要的连续对话：连续对话会消耗大量算力
- 选用 preview 模型：preview 是官方提供的预览版模型，定价是正式版的1/5

## 配置选项{#configs}

- 多语言（√）
- 多模型提供商（√）
- OpenAI 多版本（√）
- 多用户（√）
- 移动端（√）

## 故障