# Changelog

本文件记录本项目的所有重要变更，遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/) 规范。

版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

---

## [Unreleased]

### Added

- 新增 `CONTRIBUTING.md` 贡献指南（由 `developer.md` 重命名并全面重写），包含分支策略、PR 规范、i18n 说明、文档原则和常见问题
- 新增 `DEVELOPMENT.md` 开发手册，包含环境配置、本地开发命令、模板系统说明、CI/CD 工作流说明、BMAD Quick Flow 使用指南和 App 文档创建标准流程
- 新增 `template/docs/zh/app.md` Quick Flow 专用 App 文档 Prompt 模板
- 新增 `.lycheeignore` broken-links 检查排除规则文件

### Changed

- `README.md` 全面重写：新增 CI badge、Tech Stack badge、快速开始、项目结构和文档链接
- `docs/readme.md` 更新为 next 版本说明
- `build_doc.yml`：升级 `checkout@master` → `@v4`，新增 yarn cache、concurrency 控制，删除调试步骤，修复 Docker 缩进，区分 dev/main 分支部署行为，apidocs 步骤设为 `continue-on-error: true`
- `check.yml`：全量重写，恢复 broken-links 检查（`lychee-action@v2`），新增 PR 触发
- `app_from_contentful.yml`：升级 `checkout@v2` → `@v4`、`setup-python@v2` → `@v5`，新增 pip cache，移除 `--override` 参数
- `json2md.yml`：升级 `checkout@v2` → `@v4`、`setup-python@v2` → `@v5`，新增 pip cache，curl 新增重试参数
- `update.yml`：升级 `checkout@v2` → `@v4`

### Removed

- 删除 `Notes.md`（内容已迁移至 `CONTRIBUTING.md`）
- 删除 `add_apps.md`（纯占位文件）

---

<!-- 版本链接占位 -->
[Unreleased]: https://github.com/Websoft9/doc.websoft9.com/compare/HEAD...HEAD

