---
title: Zookeeper
slug: /zookeeper
tags:
  - Web 面板
  - 可视化
  - GUI
---

import Meta from './_include/zookeeper.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 Zookeeper 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

### 客户端连接

1. 获取 Zookeeper 的容器名称

2. 运行下面的命令连接启动客户端连接 (your-zookeeper 为你的容器名称)
   ```
   docker run -it --rm --link your-zookeeper:zookeeper zookeeper zkCli.sh -server zookeeper
   ```

3. 连接成功后运行 `ls /` 查询 znode

### 设置 super_digest 认证

1. 客户端连接 Zookeeper 节点，运行 `getAcl /` 会看到下面的信息，表示节点面向任何用户开放
   ```
    [zk: zookeeper(CONNECTED) 3] getAcl /
    'world,'anyone
    : cdrwa
   ```

2. 运行下面的命令修改权限
   ```
   addauth digest super:yourpassword
   setAcl / digest:super:password:cdrwa
   ```

3. 再次运行 `getAcl /` 会发现出现 **Insufficient permission : /**


## 配置选项{#configs}

- ACL 认证模式（√）
- 配置文件（√），但未启用，采用环境变量设置

## 管理维护{#administrator}

## 故障
