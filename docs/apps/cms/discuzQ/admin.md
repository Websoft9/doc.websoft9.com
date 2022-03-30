---
sidebar_position: 3
slug: /discuzq/admin
tags:
  - Discuz!Q
  - CMS
  - 建站系统
  - 博客系统
---

# 维护指南

## 场景

### 备份与恢复

### 升级

Discuz!Q 采用 Docker 部署，其升级流程：拉取镜像 > 删除容器 > 重建容器

> Discuz!Q 升级之前请完成服务器的快照备份，以防不测。

1. 使用 SSH 登录服务，进入到 Discuz!Q  目录后，拉取最新版本镜像
   ```
   cd /data/wwwroot/discuzq
   docker-compose pull
   ```
   > 系统会自动拉取最新版镜像，如果没有镜像可拉取，则无需更新

2. 停止并删除当前的 Discuz!Q  容器

   ```
   docker-compose down -v
   ```

3. 重新创建 Discuz!Q  容器
   ```
   docker-compose up -d
   


## 故障速查

除以下列出的 Discuz!Q 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。 



## 问题解答

#### [Discuz!Q](https://discuz.com/) 与 Discuz 有什么关系和区别？

从品牌上讲，DiscuzQ 是全新架构的 Discuz。但从代码角度看，它们完全不一样。Discuz!Q 的前后端完全分离，后端基于 Laravel，前端基于 Vue.js 和 uni-app，易于二次开发和扩展。




