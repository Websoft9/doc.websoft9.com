---
title: Symfony
slug: /symfony
tags:
  - Symfony
  - PHP
  - 开发工具
---

import Meta from './_include/symfony.md';

<Meta name="meta" />

## 入门指南 {#guide}

### 初始化 {#wizard}

在 Websoft9 控制台安装 Symfony 后，打开 **我的应用** > **Symfony**，通过应用的访问地址确认 Symfony 初始页面可以正常加载。

### 部署自己的项目 {#project}

应用启动后会提供 Symfony starter 项目。准备好自己的应用代码后，将项目部署到应用使用的 `/var/www/html` 目录，替换 starter 项目。修改代码或容器配置后，按需重建应用。

### 连接数据库 {#database}

默认部署不包含数据库，Symfony skeleton 默认也不依赖数据库。若应用需要数据库，先在项目中安装 Doctrine ORM 或 DBAL，再在应用 `.env` 中配置 `DATABASE_URL`，连接已部署并可访问的外部数据库。

## 最佳实践

### 独立管理数据库 {#external-database}

将数据库作为独立服务部署，并为应用配置专用数据库和用户。更新 `DATABASE_URL` 后重建应用，并检查应用日志确认数据库连接成功。备份时分别备份 Symfony 项目数据和数据库数据。

## 配置选项 {#configs}

| 配置项 | 说明 | 默认值/位置 |
|--------|------|------------|
| Web Console | Symfony Web 访问端口 | 8080 |
| `/var/www/html` | Symfony 应用代码目录 | `symfony_app` 持久化卷 |
| `DATABASE_URL` | Doctrine ORM/DBAL 数据库连接字符串 | 需要时在应用 `.env` 中设置 |
| PHP 运行时 | 使用 Server Side Up PHP FrankenPHP 镜像 | PHP 8.5 |
| Symfony 版本 | 当前支持版本 | 8.1.11；也可使用 `latest` |

生产环境建议固定 Symfony 版本，不要依赖可能变化的 `latest` 标签。

## 管理维护 {#administrator}

### 升级

在 Websoft9 控制台升级应用。升级前备份 `/var/www/html` 中的项目数据以及外部数据库；根据项目依赖兼容性选择 Symfony 版本。

### 备份与恢复

备份应用的 `symfony_app` 持久化卷和独立数据库。恢复时将应用数据还原到 `/var/www/html`，恢复数据库，并检查 `.env` 中的 `DATABASE_URL`。

## 故障排除 {#troubleshooting}

#### 初始页面无法打开或应用启动失败？

查看应用的 Compose 日志，确认服务是否成功启动，并检查防火墙或云安全组是否放行访问端口。

#### 应用无法连接数据库？

确认项目已安装 Doctrine ORM/DBAL，`DATABASE_URL` 的地址、端口、数据库名和凭据正确，并且该数据库可从应用容器访问。

## 参考 {#references}

- [Symfony 官方安装文档](https://symfony.com/doc/current/setup.html)
- [Symfony Docker 文档](https://symfony.com/doc/current/setup/docker.html)
- [FrankenPHP 镜像文档](https://serversideup.net/open-source/docker-php/docs/image-variations/frankenphp)
