---
title: screego
slug: /screego
tags:
  - P2P
  - 屏幕共享
  - 点对点
  - WebRTC
---

import Meta from './_include/screego.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 screego 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

1. 登录到 Websoft9 控制台，为 screego 应用设置 HTTPS 访问

   > screego 在安装时必须配置域名，否则不可用

2. 根据实际情况是否使用外部 TURN 服务器开始端口（可选）


### 快速使用

1. 访问 screego 的主界面，点击 " CREATE OR JOIN A ROOM" 创建一个房间

2. 将新房间的 URL 发给需要共享屏幕的其他客户端

3. 其他客户端打开 URL，便可以开始使用


## 配置选项{#configs}

- 两人以上使用（√）
- STUN/TURN 中继服务器（内置）

## 管理维护{#administrator}

## 故障

## 问题

#### WebRTC 连接原理？

客户端（浏览器）首先尝试**直连**。无人直连则使用 STUN 服务器进行**穿透**，无法穿透则通过 TURN 服务器进行**中转**。
