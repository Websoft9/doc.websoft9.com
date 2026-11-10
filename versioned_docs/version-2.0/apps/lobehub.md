---
title: LobeHub
slug: /lobehub
tags:
  - LobeHub
  - AI
  - 大语言模型
---

import Meta from './_include/lobehub.md';

<Meta name="meta" />

## 入门指南 {#guide}

### 初始化 {#wizard}

在 Websoft9 控制台安装 LobeHub 后，打开 **我的应用** > **LobeHub**，从 **访问** 标签页获取应用地址和凭据。使用凭据登录 LobeHub 管理控制台。

### 使用 LobeHub {#usage}

登录后可在 LobeHub 控制台使用应用功能。有关模型配置、对话和其他功能的详细说明，请参阅 [LobeHub 自托管文档](https://lobehub.com/docs/self-hosting/platform/docker-compose)。

### 修改密码 {#password}

在 Websoft9 控制台打开应用的 **Compose** 标签页，更新 `.env` 中的密码并保存，然后重建应用。

## 最佳实践

### 配置域名和 HTTPS {#https}

在线社区功能需要通过已配置域名的 HTTPS 访问。先为应用配置域名并启用 HTTPS，再重新加载页面。

### 备份应用数据 {#data}

LobeHub 使用 PostgreSQL、Redis 和 RustFS 保存数据，应用数据分别位于对应的持久化卷中。升级或重建前备份这些数据卷。覆盖 `bucket.config.json` 时使用单文件挂载。

## 配置选项 {#configs}

| 配置项 | 说明 | 默认值/位置 |
|--------|------|------------|
| Web Console | LobeHub Web 访问端口 | 3210 |
| PostgreSQL | 关系型数据持久化目录 | `/var/lib/postgresql/data` |
| Redis | 缓存数据持久化目录 | `/data` |
| RustFS | 对象存储数据持久化目录 | `/data` |
| Bucket 配置 | 对象存储配置文件 | `./src/bucket.config.json` |

具体环境变量请查看应用 **Compose** 页面的 `.env`。修改配置后重建应用。

## 管理维护 {#administrator}

### 升级

通过 Websoft9 控制台升级 LobeHub。生产环境建议固定应用版本；升级前备份 PostgreSQL、Redis 和 RustFS 数据卷。

### 备份与恢复

分别备份并恢复 PostgreSQL、Redis 和 RustFS 的持久化数据卷。如使用自定义 bucket 配置，还应备份 `bucket.config.json`。

## 故障排除 {#troubleshooting}

#### 应用无法启动？

查看应用的 Compose 日志，确认 LobeHub 及关联服务是否正常启动。

#### 在线社区无法加载？

该功能需要通过配置了 HTTPS 的域名访问。检查应用域名和 HTTPS 设置后重新加载。

#### 应用页面无法访问？

检查应用访问地址，并确认服务器防火墙或云安全组允许 3210 端口。

## 参考 {#references}

- [LobeHub 自托管文档](https://lobehub.com/docs/self-hosting/platform/docker-compose)
- [LobeHub 项目](https://github.com/lobehub/lobehub)
- [LobeHub 发布记录](https://github.com/lobehub/lobehub/releases)
