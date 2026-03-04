---
title: "{{AppName}}"
prompt_version: "1.0"
usage: "在 BMAD Barry QD 模式下，使用此模板引导 AI 填充 App 文档内容"
reference_example: "versioned_docs/version-2.0/apps/wordpress.md"
---

# Quick Flow App 文档 Prompt 模板

## 使用说明

1. 将 `{{AppName}}` 替换为实际的应用名称（如 `WordPress`、`GitLab`）
2. 在 BMAD Barry QD 模式中告知：`请帮我填充 {appname} 的 App 文档，参考模板：template/docs/zh/app.md`
3. Barry 将根据以下结构生成完整文档内容

---

## Prompt 指令

你是一名专业的技术文档工程师，请帮我为 **{{AppName}}** 编写 Websoft9 应用文档。

### 背景信息

- **平台**：Websoft9（Multi-application Self-hosted PaaS）
- **目标读者**：使用 Websoft9 控制台部署并使用 {{AppName}} 的用户
- **参考样例**：`versioned_docs/version-2.0/apps/wordpress.md`（阅读此文件了解标准结构和写作风格）
- **语言**：中文，技术术语保留英文原文

### 文档结构要求

请按以下结构填充 `versioned_docs/version-2.0/apps/{{appname}}.md` 文件：

```markdown
---
title: {{AppName}}
slug: /{{appname}}
tags:
  - {{AppName}}
  - （相关分类标签，如 CMS、数据库、开发工具等）
---

import Meta from './_include/{{appname}}.md';

<Meta name="meta" />


## 入门指南 {#guide}

### 初始化 {#wizard}

Websoft9 控制台安装 {{AppName}} 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取访问信息。

（描述安装后的初始化步骤：默认账号、首次登录、初始配置等）

### （核心功能 1 标题）{#feature1}

（描述最常用的核心功能场景，步骤清晰，必要时附截图说明）

### （核心功能 2 标题，可选）{#feature2}

（第二个常用功能场景）


## 最佳实践

### （典型集成或高级用例）

（描述与其他 Websoft9 应用集成的场景，或企业级使用的最佳实践）


## 配置选项 {#configs}

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| （关键配置参数名） | （说明） | （默认值） |

（列出 3-5 个最重要的配置选项，来源于应用的官方配置文档）


## 管理维护 {#administrator}

### 升级

（描述如何通过 Websoft9 控制台升级 {{AppName}} 版本）

### 备份与恢复

（描述数据备份策略和恢复步骤）


## 故障排除 {#troubleshooting}

#### {{AppName}} 无法访问？

（原因分析 + 排查步骤）

#### （其他常见问题）

（原因分析 + 解决方案）
```

### 质量要求

1. **准确性**：所有步骤描述必须基于 {{AppName}} 的真实功能，不能虚构
2. **完整性**：入门指南必须覆盖安装后的完整初始化流程
3. **一致性**：写作风格与 `wordpress.md` 保持一致（简洁、步骤化、用户视角）
4. **锚点规范**：所有二级标题使用语义化英文锚点（格式：`{#anchor-name}`）
5. **截图占位**：需要截图的位置用 `![](./assets/{{appname}}-feature-websoft9.png)` 占位
6. **中英文混排**：技术名词（如 API、CLI、Docker）保留英文，说明文字使用中文

### 参考信息来源

在生成内容时，请参考以下来源（按优先级）：

1. `versioned_docs/version-2.0/apps/{{appname}}.md`（现有骨架文件，如有内容则基于此扩充）
2. `versioned_docs/version-2.0/apps/wordpress.md`（标准参考样例）
3. {{AppName}} 官方文档（基于你的训练知识）
