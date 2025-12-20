---
title: HuggingChat
slug: /huggingchat
tags:
  - AI聊天助手
  - 聊天机器人
  - HuggingChat
---

import Meta from './_include/huggingchat.md';

<Meta name="meta" />

## 入门指南{#guide}  

### 登录后台{#console}

Websoft9 控制台安装 HuggingChat 后，通过 **我的应用** 查看应用详情，在 **访问** 标签页中获取访问 URL。  

### 模型获取与授权

Websoft9 控制台安装的 HuggingChat，还不能立即进行 AI 聊天，需要进行如下步骤:

1. 在 [Hugging Face 官网](https://huggingface.co/)注册账号。

2. 在个人设置中生成一个 Access Token。这个 Token 是您从平台下载某些模型和与 API 交互的“密钥”。

3. [编排 HuggingChat 应用](https://support.websoft9.com/docs/app-compose#dynamic)，将 `.env文件中的 OPENAI_API_KEY_SET` 设置成步骤2生成的 Token

4. 重建应用后即可选择合适的模型进行 AI 聊天

## 配置选项{#configs}

## 管理维护{#administrator}

## 故障