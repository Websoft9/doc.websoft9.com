---
title: 'Workflows & Build Scripts 全面优化'
slug: 'workflows-build-scripts-optimization'
created: '2026-03-04'
status: 'done'
stepsCompleted: [1, 2, 3, 4]
tech_stack: ['GitHub Actions', 'Python 3.x', 'Node.js 20', 'yarn', 'lychee', 'Docusaurus 3.5']
files_to_modify:
  - '.github/workflows/build_doc.yml → ci.yml'
  - '.github/workflows/check.yml'
  - '.github/workflows/update.yml'
  - '.github/workflows/app_from_contentful.yml → sync-contentful.yml'
  - '.github/workflows/json2md.yml → sync-catalog.yml'
  - '.github/dependabot.yml'
  - 'builds/gen_allapps.py'
  - 'builds/gen_md_from_contenful.py → sync_contentful.py'
  - 'builds/json2md.py → gen_app_index.py'
  - 'DEVELOPMENT.md'
code_patterns: []
test_patterns: []
---

# Tech-Spec: Workflows & Build Scripts 全面优化

**Created:** 2026-03-04

---

## Overview

### Problem Statement

当前 CI/CD 工作流存在以下问题：
1. **逻辑漏洞**：`check.yml`（lychee 外链检查）与 `build_doc.yml` 完全独立并行，导致 check 失败时 build 仍然执行（白白消耗资源），且 PR 保护门形同虚设。
2. **缓存策略次优**：`build_doc.yml` 使用 `actions/cache@v4` 缓存 `node_modules/`，而 yarn 官方推荐用 `setup-node` 内置 `cache: 'yarn'`（缓存 `~/.yarn/cache`，与 CI 环境独立，复用性更好）。
3. **脚本 Bug**：`builds/gen_allapps.py` 在写文件失败时调用 `sys.exit(1)`，但文件头未 `import sys`，触发时会抛 `NameError` 掩盖真实错误。
4. **Actions 版本过旧**：`stefanzweifel/git-auto-commit-action@v4`（最新 v5）、`peter-evans/create-pull-request@v5`（最新 v7）未跟进。
5. **update.yml 缺少 setup-node**：直接执行 `yarn install` 未声明 Node 版本，依赖 runner 预装，不可靠。

### Solution

1. **合并串行化**：将 `check.yml` 的 lychee job 并入 `build_doc.yml`，形成 `check → build` 串行流水，check 失败即跳过 build，消除资源浪费和 PR 保护漏洞。
2. **缓存优化**：改用 `setup-node` 内置 `cache: 'yarn'`，移除手动 `actions/cache` 步骤，符合 yarn 官方最佳实践。
3. **依赖自动化**：删除 `update.yml`（半自动化伪方案），用 `.github/dependabot.yml` 替代，覆盖 npm 包 + GitHub Actions 版本，每周自动提 PR。
4. **Actions 升级**：`git-auto-commit-action@v4 → v5`。
5. **脚本修复**：`gen_allapps.py` 补 `import sys`，消除隐性 NameError。
6. **命名规范化**：统一 workflow name（`CI` / `Sync from Contentful` / `Sync App Catalog`）、job id，文件名用 `git mv` 语义化重命名，同步修正 `contenful` 拼写错误。

### Scope

**In Scope：**
- `build_doc.yml` → `ci.yml`：合并 lychee check job（Task 1）、优化 yarn 缓存（Task 2）、命名规范（Task 7）、文件重命名（Task 9）
- `check.yml`：删除（Task 1）
- `update.yml`：删除，用 `dependabot.yml` 替代（Task 3）
- `app_from_contentful.yml` → `sync-contentful.yml`：升级 git-auto-commit-action v5（Task 4）、命名（Task 7）、文件重命名（Task 9）
- `json2md.yml` → `sync-catalog.yml`：升级 git-auto-commit-action v5（Task 4）、步骤整合（Task 8）、命名（Task 7）、文件重命名（Task 9）
- `builds/gen_allapps.py`：修复 `import sys`（Task 5）
- `builds/gen_md_from_contenful.py` → `builds/sync_contentful.py`：修正拼写错误（Task 9）
- `builds/json2md.py` → `builds/gen_app_index.py`：语义化重命名（Task 9）
- `DEVELOPMENT.md`：更新 CI 说明表格（Task 6）
- `.github/dependabot.yml`：新建（Task 3）

**Out of Scope：**
- apidocs Docker 步骤的取舍（需业务确认，保持 `continue-on-error: true` 不动）
- 脚本功能逻辑重写（只修 bug，不改行为）
- `gen_allapps.py` / `gen_allcatalogs.py` 重命名（命名可接受，不改）

---

## Context for Development

### Codebase Patterns

- **GitHub Actions 版本锁定策略**：本项目已统一使用 `@v4`（checkout、setup-node 等），新增 action 应锁定到主版本号，避免 `@master`/`@latest`
- **lychee 配置**：`.lycheeignore` 已存在，排除 libs.websoft9.com、support.websoft9.com 等不稳定外链
- **Python 脚本模式**：均使用 `argparse`，通过命令行参数接受 JSON 输入 + Markdown 输出路径
- **双语并行**：zh/en 文档路径对称，脚本通常接受两次调用（zh 一次，en 一次）

### Files to Reference

| File | Purpose |
| ---- | ------- |
| `.github/workflows/build_doc.yml` | 主构建/部署 workflow（Task 1/2/7/9 改造后为 `ci.yml`） |
| `.github/workflows/check.yml` | 独立 lychee 检查（Task 1 合并后删除） |
| `.github/workflows/app_from_contentful.yml` | Contentful 生成（Task 4/7/9 后为 `sync-contentful.yml`） |
| `.github/workflows/json2md.yml` | JSON→Markdown 生成（Task 4/7/8/9 后为 `sync-catalog.yml`） |
| `.github/workflows/update.yml` | Docusaurus 升级（Task 3 中删除） |
| `builds/gen_allapps.py` | 生成 allapps.md（Task 5 修复 import sys） |
| `builds/gen_md_from_contenful.py` | Contentful 数据同步（Task 9 重命名为 `sync_contentful.py`） |
| `builds/json2md.py` | 生成 App 目录索引（Task 9 重命名为 `gen_app_index.py`） |
| `.lycheeignore` | lychee 排除规则（check job 合并后继续沿用） |

### Technical Decisions

- **合并方向**：lychee job 并入 `build_doc.yml`，而非把 build 并入 `check.yml`，原因是 build_doc.yml 是主流程，Cloudflare 部署也在此文件，合并后权责清晰。
- **check.yml 处置**：合并后删除 `check.yml`，避免两个 workflow 同时在 PR 上触发造成混乱。
- **setup-node cache 键**：改为 `cache: 'yarn'`（依据 `yarn.lock` 或 `package.json` 自动生成缓存键），与现有 `hashFiles('**/package.json')` 手动策略等效但更规范。
- **lychee job 在 push to main 时不运行**：main 分支应已经过 dev/PR 的 check，main push 只跑 build + deploy，避免 main 部署被外链问题阻塞。

---

## Implementation Plan

### Tasks

- [x] **Task 1：合并 lychee check job 到 build_doc.yml，删除 check.yml**
  - 文件：`.github/workflows/build_doc.yml`、`.github/workflows/check.yml`
  - 在 `build_doc.yml` 中新增 `check` job（仅 PR 和 push to dev 时触发，main push 跳过）
  - `build` job 添加 `needs: check`（仅当 check job 存在时，main push 不受影响）
  - **实现逻辑**：使用 job-level `if` 条件控制 check 只在非 main 时运行；build job 使用 `if: always() && (needs.check.result == 'success' || needs.check.result == 'skipped')`
  - 删除 `check.yml`

- [x] **Task 2：build_doc.yml 改用 setup-node 内置 yarn cache**
  - 文件：`.github/workflows/build_doc.yml`
  - 删除 `actions/cache@v4` 步骤
  - 在 `actions/setup-node@v4` 中添加 `cache: 'yarn'`

- [x] **Task 3：删除 update.yml，新增 dependabot.yml**
  - 文件：删除 `.github/workflows/update.yml`，新建 `.github/dependabot.yml`
  - **理由**：`update.yml` 需手动触发、硬编码少数包名、无法覆盖全部依赖，属于半自动化伪方案；Dependabot 是 GitHub 官方自动化依赖升级方案
  - `dependabot.yml` 内容：
    ```yaml
    version: 2
    updates:
      - package-ecosystem: "npm"
        directory: "/"
        schedule:
          interval: "weekly"
          day: "monday"
        open-pull-requests-limit: 3
        labels:
          - "dependencies"
      - package-ecosystem: "github-actions"
        directory: "/"
        schedule:
          interval: "weekly"
          day: "monday"
        open-pull-requests-limit: 5
        labels:
          - "dependencies"
    ```
  - **说明**：同时扫描 npm 包（`package.json`）和 GitHub Actions 版本，每周一自动提 PR，PR 上附带 changelog 和安全公告

- [x] **Task 4：升级 git-auto-commit-action v4 → v5**
  - 文件：`.github/workflows/app_from_contentful.yml`、`.github/workflows/json2md.yml`
  - 将 `stefanzweifel/git-auto-commit-action@v4` 改为 `@v5`

- [x] **Task 5：修复 gen_allapps.py 缺失 import sys**
  - 文件：`builds/gen_allapps.py`
  - 在文件头部 `import json` 后添加 `import sys`

- [x] **Task 6：更新 DEVELOPMENT.md CI 工作流说明表格**
  - 文件：`DEVELOPMENT.md`
  - check.yml 独立触发条件说明已不适用（已并入 build_doc.yml），更新表格描述

- [x] **Task 7：统一规范 Workflow 和 Job 命名**
  - 文件：所有 `.github/workflows/*.yml`
  - Workflow `name` 改动：
    - `build_doc.yml`：`Docs Build and Upload to Cloudflare` → `CI`
    - `app_from_contentful.yml`：`Generate Apps header and appdocs files` → `Sync from Contentful`
    - `json2md.yml`：`Generate Apps list for docs` → `Sync App Catalog`
    - ~~`update.yml`~~：已在 Task 3 中删除，无需改名
  - Job ID 改动：
    - `build_doc.yml`：`build` job 保持，新增 `check` job（Task 1 已规划）
    - `app_from_contentful.yml`：job id `build` → `generate`
    - `json2md.yml`：job id `build` → `generate`
  - **理由**：`CI / check` 和 `CI / build` 在 PR Checks 面板语义清晰；`Check Action` 是无意义命名；统一首字母大写风格

- [x] **Task 8：整合 json2md.yml 的 6 个分散步骤为 1 个步骤**
  - 文件：`.github/workflows/json2md.yml`
  - 当前：6 个独立 step（每个脚本各调用 zh、en 两次，共 6 次），UI 噪音大
  - 目标：合并为单个 `Generate all Markdown files` step，按语言分组（zh 一组、en 一组），脚本逻辑不变
  - 合并后结构：
    ```yaml
    - name: Generate all Markdown files
      run: |
        # zh
        python builds/json2md.py --json_file ./extracted/media/json/product_zh.json --output_file versioned_docs/version-2.0/apps/README.mdx --ignore-list template/meta/skip_applink.json
        python builds/gen_allcatalogs.py --json_file ./extracted/media/json/catalog_zh.json --output_file versioned_docs/version-2.0/apps/_include/allcatalogs.md
        python builds/gen_allapps.py --json_file ./extracted/media/json/product_zh.json --output_file versioned_docs/version-2.0/apps/_include/allapps.md
        # en
        python builds/json2md.py --json_file ./extracted/media/json/product_en.json --output_file i18n/en/docusaurus-plugin-content-docs/version-2.0/apps/README.mdx --ignore-list template/meta/skip_applink.json
        python builds/gen_allcatalogs.py --json_file ./extracted/media/json/catalog_en.json --output_file i18n/en/docusaurus-plugin-content-docs/version-2.0/apps/_include/allcatalogs.md
        python builds/gen_allapps.py --json_file ./extracted/media/json/product_en.json --output_file i18n/en/docusaurus-plugin-content-docs/version-2.0/apps/_include/allapps.md
    ```
  - **注**：Task 9 完成后此处脚本调用名称需同步改为 `builds/gen_app_index.py`；`app_from_contentful.yml` 重命名后其 4 个脚本调用名也需更新为 `builds/sync_contentful.py`

- [x] **Task 9：文件名规范化（workflow 文件 + 脚本文件）**
  - **Workflow 文件重命名**（用 `git mv`，保留 Git history）：
    - `build_doc.yml` → `ci.yml`
    - `app_from_contentful.yml` → `sync-contentful.yml`
    - `json2md.yml` → `sync-catalog.yml`
  - **Build 脚本重命名**（用 `git mv`）：
    - `builds/gen_md_from_contenful.py` → `builds/sync_contentful.py`（同步修正拼写错误 `contenful→contentful`）
    - `builds/json2md.py` → `builds/gen_app_index.py`
  - **同步更新所有引用**（workflow 内的脚本调用路径）：
    - `sync-contentful.yml`：4 处 `python builds/gen_md_from_contenful.py` → `python builds/sync_contentful.py`
    - `sync-catalog.yml`：6 处脚本调用中 `json2md.py` → `gen_app_index.py`
  - **同步更新 DEVELOPMENT.md**：CI 工作流表格中的文件名引用

### Acceptance Criteria

- [x] **AC 1**：Given 一个 PR 向 dev 提交且 lychee 检测到 broken link，When CI workflow 运行，Then `CI / check` job 失败，`CI / build` job 状态为 `skipped`，不产生任何 build 产物
- [x] **AC 2**：Given 一个 PR 向 dev 提交且 lychee 未发现问题，When CI workflow 运行，Then `CI / check` 通过后 `CI / build` 自动触发，PR Checks 面板显示两个独立 job
- [x] **AC 3**：Given push 到 main 分支，When CI workflow 触发，Then `CI / check` job 被跳过（`if` 条件不满足），`CI / build` 正常运行并触发 Cloudflare Pages 部署
- [x] **AC 4**：Given `ci.yml`（原 `build_doc.yml`）的 build job，When 检查 setup-node 步骤，Then 有 `cache: 'yarn'` 字段，文件中无独立 `actions/cache` 步骤
- [x] **AC 5**：Given `.github/workflows/` 目录，When 列出所有文件，Then 不存在 `update.yml`，存在 `dependabot.yml`，且 `dependabot.yml` 包含 `npm` 和 `github-actions` 两个 ecosystem 配置块
- [x] **AC 6**：Given `sync-contentful.yml` 和 `sync-catalog.yml`，When 检查 `git-auto-commit-action` 版本字段，Then 均为 `@v5`
- [x] **AC 7**：Given `builds/gen_allapps.py`，When 检查文件顶部 import 语句，Then 第 1-2 行同时包含 `import json` 和 `import sys`
- [x] **AC 8**：Given `.github/workflows/` 目录，When 列出所有文件，Then 存在 `ci.yml`、`sync-contentful.yml`、`sync-catalog.yml`，不存在 `build_doc.yml`、`app_from_contentful.yml`、`json2md.yml`
- [x] **AC 9**：Given `builds/` 目录，When 列出所有 Python 文件，Then 存在 `sync_contentful.py`、`gen_app_index.py`，不存在 `gen_md_from_contenful.py`、`json2md.py`
- [x] **AC 10**：Given `sync-catalog.yml` 的 generate job，When 检查所有 steps，Then 只有 1 个生成步骤（`Generate all Markdown files`），该步骤包含 6 个 Python 命令且按 `# zh` / `# en` 注释分组
- [x] **AC 11**：Given `DEVELOPMENT.md` CI 工作流说明表格，When 查找 workflow 文件名，Then 所有文件名引用与实际文件名一致（`ci.yml`、`sync-contentful.yml`、`sync-catalog.yml`），无独立 `check.yml` 条目

---

## Additional Context

### Dependencies

- **Task 1 + Task 7 + Task 9 完成后**，GitHub 分支保护规则需手动更新：将 required status check 由 `Check Action / Broken Links Check` 改为 `CI / build`（新 workflow name + job id）。这属于 GitHub 仓库设置，不在代码范围内，需 Owner 手动配置。
- **Task 9 建议执行顺序**：Tasks 1-8 全部完成并验证后，最后执行 Task 9 文件重命名，避免中途切换文件名增加调试难度。

### Testing Strategy

- 本地无法直接测试 GitHub Actions，验证方式为：
  1. push 到 feat 分支 → 在 GitHub Actions 页面观察 job 依赖关系是否正确
  2. 提 PR to dev → 确认 `CI / check` 先于 `CI / build` 运行
  3. 手动触发 `sync-contentful.yml` → 确认 git-auto-commit-action@v5 + 脚本新名称兼容性
  4. Task 9 后：`git log --follow builds/sync_contentful.py` 确认历史可追溯

### Notes

- `gen_md_from_contenful.py` 拼写 bug（`contenful`）在 Task 9 中作为重命名的一部分一并修正，无需单独处理
- apidocs Docker 步骤维持 `continue-on-error: true` 不动，不列入本次 Tasks
- `gen_allapps.py` 和 `gen_allcatalogs.py` 命名可接受，不重命名
- `update.yml` 删除后，如需临时手动升级依赖，直接本地执行 `yarn upgrade` 提 PR 即可
- Dependabot 自动 PR 合并策略由仓库 Owner 在 GitHub Settings 中决定（可开启 auto-merge）
- **⚠️ 分支保护规则需 Owner 手动更新**：所有 Tasks 完成后，将 required status check 由 `Check Action / Broken Links Check` 改为 `CI / build`
- 本 spec 在当前分支 `feat/docs-cicd-bmad-standardization` 上实现

---

## Senior Developer Review (AI)

**Reviewer:** Barry (Quick Flow Solo Dev)  
**Date:** 2026-03-05  
**Commit reviewed:** `e2e48415`  
**Review commit:** `97cd4213`

### Findings Summary

| # | 级别 | 问题 | 处理 |
|---|------|------|------|
| H-1 | 🔴 HIGH | `cache: 'yarn'` 与 `yarn.lock` 未提交不兼容，缓存完全失效 | 已修复：恢复 `actions/cache@v4` |
| H-2 | 🔴 HIGH | `sync-catalog.yml` checkout 缺少 `fetch-depth: 0` | 已修复：添加 `fetch-depth: 0` |
| M-1 | 🟡 MEDIUM | `DEVELOPMENT.md` 缓存说明与实际实现不一致 | 已修复：更新为 `actions/cache@v4` 说明 |
| M-2 | 🟡 MEDIUM | lychee 上传步骤 `if: always()` 导致无错时产生 warning | 已修复：改为 `if: failure()` |
| L-1 | 🟢 LOW | `dependabot.yml` 缺少 `target-branch: dev` | 未自动修复，Owner 确认后支 取 |
| L-2 | 🟢 LOW | `sync-contentful.yml` 注释中 `Write 权限` 误导 | 未修复 |
| L-3 | 🟢 LOW | `ci.yml` `on.push.paths` 未覆盖 `builds/**` | 继承问题，未修复 |

**结论：** 4 个 HIGH/MEDIUM 问题全部修复并已推送。
