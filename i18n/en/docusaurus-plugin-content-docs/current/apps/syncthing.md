---
title: Syncthing
slug: /syncthing
tags:
  - 文件夹实时同步
  - 可视化
  - GUI
---

import Meta from './_include/syncthing.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

1. Websoft9 控制台安装 Syncthing 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息

2. 登录后，系统会提示设置账号（建议完成此项设置）
   
   - 常规 > API 密钥（建议）
   - 图形化界面 > 图形管理界面用户名和图形管理界面密码（强烈建议）

### 服务器同步

Syncthing 主要用于多台服务器之间同步文件或文件夹。下面介绍具体的操作（假设为服务器A，服务器B）：

1. 确保两台服务器都已经安装 Syncthing

2. 登录服务器A 上的 Syncthing，添加一个远程设备，此时会自动发现服务器B 的 设备 ID，勾选即可

3. 登录服务器B 上的 Syncthing，会收到服务器A 的连接请求，点击 "+添加设备" 根据向导完成连接

4. 分别在两台服务器的 Syncthing 控制台分别点击 "+添加文件夹"

   - 常规 > 文件夹 ID（A 和 B 使用同一个 ID）
   - 常规 > 文件夹路径
   - 共享（勾选）

5. 所有设置完成，即可自动同步

## 配置选项{#configs}

- 多语言（✅）

## 管理维护{#administrator}

## 故障