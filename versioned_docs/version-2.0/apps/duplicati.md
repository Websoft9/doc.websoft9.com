---
title: Duplicati
slug: /duplicati
tags:
  - 增量备份
  - 备份恢复软件
  - duplicati
---

import Meta from './_include/duplicati.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

1. Websoft9 控制台安装 Duplicati 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息

2. 本地浏览器访问 URL，输入管理员密码后即可使用


### 备份指南

参考：[Websoft9 备份](./backup-websoft9)


## 配置选项{#configs}

- 多语言（✅）
- 备份路径设置：应用编排 .env 文件的 SOURCE_PATH 和 BACKUP_PATH


## 管理维护{#administrator}

## 故障

#### 安装多个 Duplicati 异常？

问题原因： Duplicati 默认绑定了宿主机的**固定路径**，所以安装第二个 Duplicati 时会使用同一个路径，因此尝试权限问题。   
解决方案： 不建议安装多个 Duplicati
