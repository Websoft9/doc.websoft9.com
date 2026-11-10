---
title: QwenPaw
slug: /qwenpaw
tags:
  - QwenPaw
  - AI Agent
  - 大语言模型
---

import Meta from './_include/qwenpaw.md';

<Meta name="meta" />

## 入门指南 {#guide}

### 初始化 {#wizard}

在 Websoft9 控制台安装 QwenPaw 后，从 **访问** 标签页打开 Hub 地址，并使用部署时设置的管理员凭据登录。首次启动需要联网安装 Hub 所需组件，等待服务健康检查通过后再开始使用。

### 管理用户和运行时 {#users}

1. 在 Hub 中打开 **User Management** 创建用户，或根据注册策略允许用户自行注册。
2. 用户登录后会获得独立的 QwenPaw runtime、工作区、凭据和会话。
3. 用户可在个人 Console 的 **Settings → Models** 中添加模型提供商及 API key，或选择本地模型。

### 管理注册方式 {#registration}

通过环境变量 `QWENPAW_HUB_REGISTRATION_MODE` 设置注册方式：`open` 允许开放注册，`invite` 使用邀请模式，`closed` 关闭自助注册。限制为可信团队使用时，可设置为 `closed` 并由管理员创建用户。

## 最佳实践

### 仅向可信用户开放 {#trusted-users}

QwenPaw Hub 是早期版本，适用于可信团队，不适用于相互不信任的用户。Hub 的本地 runtime 后端需要容器以特权模式运行；首次启动还需要网络访问以安装依赖。请限制 Hub 的访问范围，并设置适当的注册策略。

## 配置选项 {#configs}

| 配置项 | 说明 | 默认值/位置 |
|--------|------|------------|
| Hub Console | Hub Web 控制台端口 | 8000 |
| `W9_URL` | Hub 对外访问地址来源；用于生成 `QWENPAW_HUB_PUBLIC_BASE_URL` | Websoft9 应用地址 |
| `QWENPAW_HUB_REGISTRATION_MODE` | 自助注册模式 | `open` |
| `W9_LOGIN_USER` / `W9_LOGIN_PASSWORD` | 首次启动时初始化 Hub 管理员 | 首次启动生效 |
| `/app/working` | QwenPaw 数据目录 | `qwenpaw_data` 持久化卷 |

修改 `.env` 后重建应用。首次创建的管理员信息只在首次启动时写入。

## 管理维护 {#administrator}

### 升级

通过 Websoft9 控制台升级应用。升级前备份 `qwenpaw_data` 持久化卷，并在升级后确认 Hub 与用户 runtime 均正常运行。

### 备份与恢复

备份挂载到 `/app/working` 的持久化数据。恢复时将数据还原到对应卷，再启动应用并检查 Hub 的 **Runtimes** 页面状态。

## 故障排除 {#troubleshooting}

#### 首次启动时间较长？

首次启动会安装 Hub 的 Docker SDK 和 `bubblewrap`，需要网络连接，可能需要等待数分钟。查看 Compose 日志确认安装进度。

#### 无法创建或启动用户 runtime？

确认容器按应用配置以特权模式运行，并在 Hub 的 **Runtimes** 页面查看错误信息。

#### Hub 无法通过访问地址打开？

确认 `W9_URL` 与用户实际访问的 URL 一致，并检查端口及防火墙或云安全组规则。

## 参考 {#references}

- [QwenPaw 官方快速入门](https://qwenpaw.agentscope.io/docs/quickstart)
- [QwenPaw Hub 文档](https://qwenpaw.agentscope.io/docs/hub)
- [QwenPaw 项目文档](https://github.com/agentscope-ai/QwenPaw)
