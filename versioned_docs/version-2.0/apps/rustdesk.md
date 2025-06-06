---
title: RustDesk 
slug: /rustdesk
tags:
  - 远程支持
  - 远程桌面
  - RustDesk
---

import Meta from './_include/rustdesk.md';

<Meta name="meta" />

## 入门指南{#guide}

### 远程连接

以两台 Windows 为例，下面描述远程连接的过程:

1. 两台连接的 windows 分别下载 RustDesk [客户端](https://github.com/rustdesk/rustdesk/releases/download/1.4.0/rustdesk-1.4.0-x86_64.exe)并安装

2. 打开客户端连接工具，**设置 > 网络 > ID/中继服务器** 设置  
   - ID服务器：部署 RustDesk 的IP或者域名  
   - Key: RustDesk volumes 下 **id_ed25519.pub**的内容

3. 将受控端的 ID 和一次性密码给控制客户端，即可开始远程连接

## 配置选项{#configs}

## 管理维护{#administrator}