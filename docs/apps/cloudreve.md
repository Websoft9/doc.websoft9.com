---
title: Cloudreve
slug: /cloudreve
tags:
  - 企业网盘
  - 下载
  - 文档管理
  - 对象存储
---

import Meta from './_include/cloudreve.md';

<Meta name="meta" />

## 入门指南{#guide}

### 登录验证{#wizard}

1. Websoft9 控制台安装 Cloudreve 后，通过 "我的应用" 查看应用详情

2. 在"我的应用" 管理界面的 **容器**标签页中查看 Cloudreve 容器的日志，获得初始化账号密码

3. 登录验证 Cloudreve 可用性

### 接入外部存储

1. 登录 Cloudreve 后，通过 **管理界面 > 存储策略 > 添加存储策略**
   - AccessKey 是必填项
   - 上传路径在 Cloudreve 中的挂载点

2. 存储配置的最后一步 **跨域策略** 选择自动配置，如果配置通过，则说明接入外部存储成功

3. 启用外部存储：**管理界面 > 用户组** 编辑用户组，选择**存储策略**

> Cloudreve 开源版仅支持同个用户组一次对应一个存储策略（包括默认的容器策略）

### 启用离线下载

Websoft9 提供的 Cloudreve 应用默认安装了离线下载 RPC  服务，只需要参考一下步骤启用它：

1. Websoft9 控制台 "我的应用" 中获取 Cloudreve 的 RPC 账号信息

1. 进入 **个人中心 > 管理面板 > 离线下载节点**，编辑此节点

2. 启用离线下载任务，填写 RPC 账号信息

4. 连接下载

### 文档编辑与预览

参考：[Cloudreve wopi](https://docs.cloudreve.org/use/wopi) (√): ONLYOFFICE, CODE

## 配置选项{#configs}

- 多语言（✅）
- [wopi](https://docs.cloudreve.org/use/wopi) (√): ONLYOFFICE, CODE
- RPC 服务 (√)

## 管理维护{#administrator}

## 故障
