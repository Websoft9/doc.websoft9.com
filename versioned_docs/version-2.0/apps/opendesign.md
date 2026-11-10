---
title: OpenDesign
slug: /opendesign
tags:
  - OpenDesign
  - 设计协作
  - AI
---

import Meta from './_include/opendesign.md';

<Meta name="meta" />

## 入门指南 {#guide}

### 初始化 {#wizard}

在 Websoft9 控制台安装 OpenDesign 后，打开 **我的应用** > **OpenDesign**，从 **访问** 标签页获取访问地址和凭据。登录后进入 OpenDesign 控制台。

### 开始使用 {#usage}

登录后即可使用 OpenDesign 控制台中的功能。应用具体功能和操作方式请参阅 [OpenDesign 官方网站](https://open-design.ai)及项目文档。

### 修改密码 {#password}

1. 在 Websoft9 控制台打开 OpenDesign 的 **Compose** 标签页。
2. 修改 `.env` 中的密码并保存。
3. 重建应用，使配置生效。

## 最佳实践

### 保留应用数据 {#data}

应用数据保存在 `/app/.od` 对应的 `opendesign_data` 持久化卷中。升级或重建应用前备份该卷。覆盖配置文件时只挂载单个只读文件，不要替换整个配置目录。

## 配置选项 {#configs}

| 配置项 | 说明 | 默认值/位置 |
|--------|------|------------|
| Web Console 和 API | Web 界面及 API 端口 | 7456 |
| 应用数据 | OpenDesign 持久化数据目录 | `opendesign_data` 卷，挂载到 `/app/.od` |
| 密码 | 在应用 `.env` 中更新 | 修改后需重建应用 |
| 镜像版本 | 当前支持版本 | 0.24.1；也可使用 `latest` |
| 配置文件 | 使用只读单文件挂载覆盖 | 配置文件位于镜像中 |

生产环境建议固定镜像版本。

## 管理维护 {#administrator}

### 升级

通过 Websoft9 控制台升级 OpenDesign。升级前备份 `opendesign_data` 卷；升级或修改配置后按控制台提示重建应用。

### 备份与恢复

备份并恢复 `opendesign_data` 持久化卷。若自行覆盖配置文件，恢复时逐个还原对应的只读挂载文件，不要用目录挂载覆盖镜像中的整套配置。

## 故障排除 {#troubleshooting}

#### 应用无法启动？

查看应用的 Compose 日志，确认镜像和服务启动状态。

#### 页面无法访问？

确认应用访问地址正确，检查服务器防火墙或云安全组是否放行 7456 端口。

#### 修改密码后仍无法登录？

确认已在 Compose 页面的 `.env` 中保存密码，并重建应用后再尝试登录。

## 参考 {#references}

- [OpenDesign 官方网站](https://open-design.ai)
- [OpenDesign 项目文档](https://github.com/nexu-io/open-design)
- [OpenDesign 发布记录](https://github.com/nexu-io/open-design/releases)
