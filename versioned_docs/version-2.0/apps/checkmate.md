---
title: Checkmate
slug: /checkmate
tags:
  - 网站监控
  - 实时报警
  - Checkmate
---

import Meta from './_include/checkmate.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

1. Websoft9 控制台安装 RAGFlow 后，通过 **我的应用** 查看应用详情，在 **访问** 标签页中获取访问URL

2. 本地浏览器访问URL，根据提示完成注册即可使用 

## 配置选项{#configs}

- 多语言，但不支持中文（√）

## 管理维护{#administrator}

## 故障

#### MongoDB 容器不断重启，应用无法正常访问？

故障描述：MongoDB 无法正常启动，查看日志提示对AVX指令集不支持 
问题原因：MongoDB 4.2 及以上版本需要 CPU 支持 AVX 指令集，否则无法启动  
解决方案：更换支持 AVX 指令集的 CPU 进行部署 
