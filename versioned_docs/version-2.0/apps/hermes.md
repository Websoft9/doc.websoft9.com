---
title: Hermes Agent
slug: /hermes
tags:
  - Hermes Agent
  - AI Agent
  - 大语言模型
---

import Meta from './_include/hermes.md';

<Meta name="meta" />

## 入门指南 {#guide}

### 初始化 {#wizard}

在 Websoft9 控制台安装 Hermes Agent 后，从 **访问** 标签页打开 Dashboard，使用部署设置的 `W9_LOGIN_USER` 和 `W9_LOGIN_PASSWORD` 进行 HTTP Basic Auth 登录。

### 配置模型并开始对话 {#model}

Hermes Agent 需要配置 LLM 提供商才能使用。打开应用 **Compose** 标签页，在 `.env` 中设置提供商 API key（例如 `OPENROUTER_API_KEY`），保存并重建应用。然后在 Dashboard 选择模型并开始对话。

### 使用 OpenAI 兼容 API {#api}

配置模型提供商后，OpenAI 兼容 API 服务会在 8642 端口启动。API 请求需使用 `W9_POWER_PASSWORD` 作为 Bearer token。仪表盘密码也由该变量驱动；修改后重建应用。

## 最佳实践

### 持久化 Agent 状态 {#persistence}

配置、环境变量、会话、记忆、技能和日志均保存在 `/opt/data` 对应的持久化数据卷中。镜像本身不保存运行状态，因此重建容器或升级时需保留此数据卷。

### 安全配置 Dashboard {#security}

Dashboard 使用 HTTP Basic Auth。保持 `HERMES_DASHBOARD_BASIC_AUTH_*` 认证配置，并确保 `W9_POWER_PASSWORD` 至少 16 个字符。仅向可信用户开放 API 和管理界面。

## 配置选项 {#configs}

| 配置项 | 说明 | 默认值/位置 |
|--------|------|------------|
| Dashboard | Hermes Web Dashboard 端口 | 9119 |
| OpenAI 兼容 API | API 服务端口，配置提供商 key 后启动 | 8642 |
| Dashboard 用户名和密码 | Dashboard Basic Auth 凭据 | `W9_LOGIN_USER` / `W9_LOGIN_PASSWORD` |
| `W9_POWER_PASSWORD` | Dashboard 密码及 API Bearer token | 至少 16 个字符 |
| LLM 提供商 API key | 启用模型及 API 服务所需 | 在 `.env` 中设置，例如 `OPENROUTER_API_KEY` |
| `/opt/data` | Agent 配置、会话、记忆、技能和日志 | `hermes_data` 持久化卷 |

## 管理维护 {#administrator}

### 升级

通过 Websoft9 控制台更新 `W9_VERSION` 并重建容器。镜像是无状态的，升级时保留 `/opt/data` 数据卷即可保留 Agent 状态。首次拉取镜像可能需要较长时间。

### 备份与恢复

备份并恢复挂载到 `/opt/data` 的持久化卷。该目录包含 Agent 的运行配置和用户数据；恢复后检查 Dashboard 认证、模型提供商配置及会话状态。

## 故障排除 {#troubleshooting}

#### Dashboard 无法访问？

确认 Dashboard 的认证变量已配置、`W9_POWER_PASSWORD` 至少 16 个字符，并等待健康检查通过。首次拉取镜像可能需要较长时间。

#### API 端口未启动？

API 服务只有在 `.env` 中配置 LLM 提供商 API key 后才会启动。保存 key 并重建应用，然后检查服务状态。

#### Agent 提示提供商错误？

检查 `.env` 中是否已配置有效的 LLM 提供商 API key，并在重建应用后重新尝试。

## 参考 {#references}

- [Hermes Agent Docker 用户指南](https://hermes-agent.nousresearch.com/docs/user-guide/docker)
- [Hermes Agent 项目](https://github.com/NousResearch/hermes-agent)
- [Hermes Agent 发布记录](https://github.com/NousResearch/hermes-agent)
