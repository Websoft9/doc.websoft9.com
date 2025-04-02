---
title: Rclone
slug: /rclone
tags:
  - 云存储
  - 文件同步
  - Rclone
---

import Meta from './_include/rclone.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

1. Websoft9 控制台安装 Rclone 后，通过 **我的应用** 查看应用详情，在 **访问** 标签页中获取登录信息

2. 本地浏览器访问 URL，输入登陆验证信息后即可使用
 
### 执行同步

在可视化界面可以来源和目标的配置，但是不可以执行同步，需要进入容器执行如下命令:

   ```
   rclone sync <Source's Config_Name>:<bucket_name>  <Destination's Config_Name>:<bucket_name>
   ```

## 配置选项{#configs}

## 管理维护{#administrator}

## 故障