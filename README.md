# Websoft9 文档站

[![Build Status](https://github.com/Websoft9/doc.websoft9.com/actions/workflows/build_doc.yml/badge.svg)](https://github.com/Websoft9/doc.websoft9.com/actions/workflows/build_doc.yml)
[![Check Status](https://github.com/Websoft9/doc.websoft9.com/actions/workflows/check.yml/badge.svg)](https://github.com/Websoft9/doc.websoft9.com/actions/workflows/check.yml)
[![Docusaurus](https://img.shields.io/badge/Docusaurus-3.5.1-brightgreen)](https://docusaurus.io/)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

[Websoft9](https://github.com/Websoft9/websoft9) 官方文档站的源码仓库，基于 [Docusaurus 3.5.1](https://docusaurus.io/) 构建，部署于 [Cloudflare Pages](https://pages.cloudflare.com/)。

**在线访问**：[https://support.websoft9.com](https://support.websoft9.com)

---

## 技术栈

| 技术 | 版本 | 用途 |
|------|------|------|
| Docusaurus | 3.5.1 | 文档框架 |
| Node.js | >= 18 | 运行环境 |
| yarn | >= 1.22 | 包管理器 |
| GitHub Actions | — | CI/CD |
| Cloudflare Pages | — | 静态托管部署 |
| Algolia Search | — | 全文搜索 |
| Python 3 / Jinja2 | — | 内容生成脚本 |

---

## 快速开始

```bash
# 克隆仓库
git clone https://github.com/Websoft9/doc.websoft9.com.git
cd doc.websoft9.com

# 安装依赖
yarn install

# 启动本地开发服务器（中文）
npm run start -- --host 0.0.0.0 --port 3000

# 启动本地开发服务器（英文）
npm run start -- --host 0.0.0.0 --port 3000 --locale en

# 生产构建
yarn build
```

---

## 项目结构

```
versioned_docs/version-2.0/   # 中文主文档（当前发布版本）
i18n/en/                      # 英文翻译文档
builds/                       # Python 内容生成脚本
template/                     # 模板文件（Jinja2 + Quick Flow Prompt）
.github/workflows/            # CI/CD 工作流（5个）
src/                          # Docusaurus 自定义组件
static/                       # 静态资源
```

---

## 国际化（i18n）

本站支持 **中文（默认）** 和 **英文** 两种语言。

- 中文主文档：`versioned_docs/version-2.0/`
- 英文翻译：`i18n/en/docusaurus-plugin-content-docs/version-2.0/`

---

## 参与贡献

- 📖 **[CONTRIBUTING.md](CONTRIBUTING.md)** — 分支策略、PR 规范、文档原则
- 🛠️ **[DEVELOPMENT.md](DEVELOPMENT.md)** — 本地开发、模板系统、BMAD AI 辅助、App 文档创建流程
- 📋 **[CHANGELOG.md](CHANGELOG.md)** — 版本变更记录

> 所有 PR 请提交到 **`dev` 分支**，Owner 不接受直接向 `main` 提交的 PR。


## Contribute for it

It based on [Docusaurus](https://docusaurus.io/) and you just need to edit markdown files for it.

### DevOps workflow

- You can only add PR to **dev branch**, owner don't accept any PR for **main branch**

- Automation for dev

  | Task/Stage                     | Submit PR | Merge PR |
  | ------------------------------ | --------- | -------- |
  | Grammarly and Spell check      | √         |          |
  | Broken links check             | √         | √        |
  | Checking for i18n file matches | √         |          |
  | npm run                        | √         |          |

- Mannual actions for dev

  - build and deploy
  - create head files, applist files and other format file

- Automation for main

  - Broken links check
  - Build and publish

### i18n

We only provide English and Chinese language support.

- **English files**: /i18n/docusaurus-plugin-content-docs/current
- **Chinese files**: /docs

If you want use tools for translation, we suggest you:

1. Use [DeepL](https://www.deepl.com/) and [Google Translate](https://translate.google.com/) to translate at first.
2. Then use [DeepL Write](https://www.deepl.com/zh/write) checking the results of translations.

### CLI

```
# Install
yarn install

# Development 
npm run start -- --host 0.0.0.0  --port 3000
npm run start -- --host 0.0.0.0  --port 3000  --locale en

# Build
yarn build
npm run serve -- --host 0.0.0.0  --port 3000

# Create i18n language
yarn run write-translations -- --locale zh-cn

# Upgrade Docusaurus 
yarn upgrade @docusaurus/core@latest @docusaurus/preset-classic@latest
```
