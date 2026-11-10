---
title: Canvas
slug: /canvas
tags:
  - Canvas
  - LMS
  - 在线学习
---

import Meta from './_include/canvas.md';

<Meta name="meta" />

## 入门指南 {#guide}

### 初始化 {#wizard}

在 Websoft9 控制台安装 Canvas 后，打开 **我的应用** > **Canvas**，在 **访问** 标签页获取地址和账号信息。使用提供的账号登录 Canvas 管理控制台。管理员邮箱、密码和账户名称通过 `CANVAS_LMS_ADMIN_EMAIL`、`CANVAS_LMS_ADMIN_PASSWORD`、`CANVAS_LMS_ACCOUNT_NAME` 在首次启动时初始化。

### 管理课程 {#courses}

登录 Canvas 后，可通过管理控制台进入账户和课程相关功能，按需设置账户及组织课程。Canvas 的数据和配置保存在应用持久化卷及配置文件中；有关具体教学功能的使用，请参阅 [Canvas 官方文档](https://github.com/instructure/canvas-lms/wiki/Production-Start)。

### 配置邮件 {#email}

Canvas 的邮件服务器配置文件为 `outgoing_mail.yml`。如需启用邮件通知，请在部署环境中按邮件服务商参数配置 SMTP，并确认域名和邮件链接可以由用户访问。

## 最佳实践

### 首次管理员配置 {#first-admin}

首次启动完成后，使用初始化的管理员账号登录并检查账户设置。上述管理员环境变量仅首次启动时生效；修改后不会自动覆盖已初始化的账户。

### 持久化数据 {#data}

Canvas 使用 PostgreSQL 和 Redis，并将数据库、缓存、Bundle、临时文件及上传资源分别保存到持久化卷。升级前备份相关数据卷和自定义配置文件。

## 配置选项 {#configs}

| 配置项 | 说明 | 默认值/位置 |
|--------|------|------------|
| 管理员邮箱 | 首次初始化管理员账户邮箱 | `CANVAS_LMS_ADMIN_EMAIL` |
| 管理员密码 | 首次初始化管理员密码 | `CANVAS_LMS_ADMIN_PASSWORD` |
| 账户名称 | 首次初始化 Canvas 账户名称 | `CANVAS_LMS_ACCOUNT_NAME` |
| SMTP | 外发邮件设置 | `./src/outgoing_mail.yml` |
| 持久化数据 | PostgreSQL、Redis、Bundle、临时文件及资源 | 按应用卷配置 |

管理员初始化变量只在首次启动时读取。修改应用环境变量或配置后，按控制台要求重建应用。

## 管理维护 {#administrator}

### 升级

Canvas 升级涉及应用和数据迁移。升级前先通过 Websoft9 控制台备份应用数据卷及配置，再参考 [Canvas 官方升级说明](https://github.com/instructure/canvas-lms/wiki/Upgrading)执行升级。

### 备份与恢复

通过 Websoft9 控制台备份并恢复 Canvas 的持久化数据卷，包括 PostgreSQL、Redis、上传资源和应用文件。需要还原配置时，恢复 `database.yml`、`domain.yml`、`redis.yml`、`outgoing_mail.yml` 等对应文件。

## 故障排除 {#troubleshooting}

#### 应用无法启动？

检查 Canvas 的 Compose 日志和应用健康状态。首次启动或升级期间可能需要等待初始化完成。

#### 忘记管理员密码或修改初始化信息未生效？

`CANVAS_LMS_ADMIN_EMAIL`、`CANVAS_LMS_ADMIN_PASSWORD` 和 `CANVAS_LMS_ACCOUNT_NAME` 仅首次启动生效；后续修改环境变量不会自动重置已存在的数据或账户。

#### 邮件通知无法工作？

检查 `outgoing_mail.yml` 中的 SMTP 配置、网络连通性和域名配置，并确认通知中的链接可通过用户的访问地址打开。

## 参考 {#references}

- [Canvas 官方生产部署说明](https://github.com/instructure/canvas-lms/wiki/Production-Start)
- [Canvas 官方升级说明](https://github.com/instructure/canvas-lms/wiki/Upgrading)
- [Canvas 项目](https://github.com/instructure/canvas-lms)
