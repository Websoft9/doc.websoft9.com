---
title: Scratch
slug: /scratch
tags:
  - Scratch
  - 少儿编程
---

import Meta from './_include/scratch.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 Scratch 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

1. 浏览器直接访问，就进入了Scratch
   ![Scratch初始化页面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/scratch/scratch-gui-websoft9.png)

2. Scratch首次加载数据超过 20 M，如果您的网络带宽不足的话，加载会很慢，耐心等待

### 快速了解

Scratch 支持多语言（包含中文），系统默认根据浏览器自动选择语言，并可以实时切换。

- 支持登录吗？不支持
- [scratch-www](https://github.com/LLK/scratch-www) vs [scratch-gui](https://github.com/LLK/scratch-gui)


## 管理维护{#administrator}

## 故障

#### Scratch 无法加载或访问很慢？{#slowy}

Scratch首次加载数据超过20M。例如：您使用的是2M带宽，那么理想情况下的加载时间为：20000k/(128k/s×2)=78s。显然，如果带宽不足，速度会非常慢。  

另外，Scratch 会加载 Google 统计资源，也会导致访问异常或较慢。  

#### Scratch 背景和角色图标无法在线获取？{#assets}

问题原因：Scratch 预制的角色图标和背景图片都是存放在官方的服务器，由于网络问题，目前这些资源都无法在线获取。  
解决办法：[下载](https://libs.websoft9.com/apps/scratch/asset.zip) 到本地电脑，然后通过**上传**的方式使用。 