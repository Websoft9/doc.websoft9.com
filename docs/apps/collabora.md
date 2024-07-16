---
title: Collabora
slug: /collabora
tags:
  - 文档预览与编辑
  - 文档中间件
  - CODE
---

import Meta from './_include/collabora.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 Collabora 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

### 集成 Nextcloud 

Nextcloud 官方对 Collabora 有较好的[集成](https://www.collaboraoffice.com/code/quick-tryout-nextcloud-docker/)。

1. Nextcloud 安装 **Collabora Online - Built-in CODE Server** 应用

2. **管理设置 > 管理 > 内建服务器(CODE)**，安装 Nextcloud Office 插件

3. **管理设置 > 管理 > Nextcloud Office > 使用您的自有服务器**，填写 Collabora Online 访问URL

4. 保存成功即可使用

## 配置选项{#configs}

- 支持多语言（√）：默认支持中文
- 管理后台（√）
- 配置文件转换成环境变量（√）
- 域名访问（√）

## 管理控制台

Collabora CODE 提供了 [Admin Console](https://sdk.collaboraonline.com/docs/installation/Configuration.html#admin-console) 用于监控运行状态。

## 管理维护{#administrator}

## 故障