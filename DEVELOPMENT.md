# 开发手册（Development Guide）

本手册面向本仓库的文档维护者和内容贡献者，涵盖本地开发环境搭建、工具链使用、CI/CD 工作流说明、BMAD AI 辅助开发，以及新增 App 文档的完整标准流程。

---

## 环境要求

| 工具 | 版本要求 | 说明 |
|------|----------|------|
| Node.js | >= 18 | 推荐使用 LTS 版本 |
| yarn | >= 1.22 | 包管理器（`yarn.lock` 不提交到版本库） |
| Python | >= 3.8 | 构建脚本依赖 |
| Git | >= 2.x | 版本控制 |

---

## 本地开发命令

```bash
# 安装依赖
yarn install

# 启动本地开发服务器（中文，默认）
npm run start -- --host 0.0.0.0 --port 3000

# 启动本地开发服务器（英文）
npm run start -- --host 0.0.0.0 --port 3000 --locale en

# 构建生产包
yarn build

# 本地预览构建结果
npm run serve -- --host 0.0.0.0 --port 3000

# 生成 i18n 翻译文件（新增翻译语言时使用）
yarn run write-translations -- --locale zh-cn

# 升级 Docusaurus（生成 PR，不直接 push）
yarn upgrade @docusaurus/core@latest @docusaurus/preset-classic@latest
```

> **注意**：`yarn.lock` 已在 `.gitignore` 中，**不提交**。CI 通过 `actions/cache@v4` + `hashFiles('**/package.json')` 缓存 `node_modules/`。

---

## 项目结构说明

```
versioned_docs/version-2.0/   # 中文主文档（当前版本）
i18n/en/                      # 英文翻译文档
builds/                       # Python 构建脚本
template/
  meta/                       # Jinja2 模板（Contentful 内容生成）
  docs/zh/                    # Quick Flow 专用 Prompt 模板
.github/workflows/            # CI/CD 工作流
```

---

## 模板系统

本项目使用两套模板系统：

### 1. Jinja2 App 模板（`template/meta/`）

由 `sync-contentful.yml` 自动调用，从 Contentful CMS 生成 App 文档的 `_include/` 元数据片段和 App 文档骨架。

- `zh_head.jinja2` / `en_head.jinja2` — 生成 `apps/_include/{appname}.md`
- `zh_app.jinja2` / `en_app.jinja2` — 生成 `apps/{appname}.md` 骨架
- `skip_file.json` — 排除不需要生成的应用列表
- `skip_applink.json` — 排除无路由的应用链接

> ⚠️ **`_include/` 目录下的文件由 CI 自动生成，不应手工修改。**

### 2. Quick Flow Prompt 模板（`template/docs/zh/`）

供贡献者使用 BMAD Barry（QD 模式）填充 App 文档内容时参考。详见「新增 App 文档标准流程」章节。

---

## CI/CD 工作流说明

| 工作流 | 触发条件 | 用途 |
|--------|----------|------|
| `ci.yml` | push to `dev`/`main`，PR to `dev`，`workflow_dispatch` | CI 主流程：外链检查（check job）+ 文档构建（build job）；main 分支额外部署到 Cloudflare Pages |
| `sync-contentful.yml` | `workflow_dispatch`（管理员手动触发）| 从 Contentful CMS 生成 App 元数据文档（`_include/`）和文档骨架 |
| `sync-catalog.yml` | `workflow_dispatch`，`repository_dispatch: applist_dev_event` | 从制品生成 App 目录列表（由主仓库 release 触发）|

**分支行为差异（`ci.yml`）：**

- `dev` 分支 / PR：先运行 `check` job（lychee 外链检查），通过后运行 `build` job（构建验证），**不部署**
- `main` 分支：跳过 `check` job，直接运行 `build` job + 部署到 Cloudflare Pages

> **注**：Docusaurus 依赖升级由 [Dependabot](https://docs.github.com/en/code-security/dependabot) 自动管理（每周一提 PR），无需手动触发。

---

## AI 辅助开发（BMAD Quick Flow）

本仓库已集成 [BMAD 方法](https://github.com/bmadcode/BMAD-METHOD)，提供 AI 驱动的文档开发加速工具。**BMAD 是本仓库专属内部工具**，适用于文档站内容贡献，不属于 `develop/` 多项目公共贡献区的内容。

### Quick Flow 三阶段流程

```mermaid
graph LR
    QS["QS 规格阶段\n(Barry Quick Spec)"]
    QD["QD 开发阶段\n(Barry Quick Dev)"]
    CR["CR 审查阶段\n(Code Review / Human)"]

    QS -->|生成 tech-spec| QD
    QD -->|实现 Tasks| CR
```

- **QS（Quick Spec）**：与 Barry 对话，输出结构化 tech-spec 文件，明确实现任务和验收标准
- **QD（Quick Dev）**：Barry 读取 tech-spec，自动执行所有实现任务（写文档、修 CI、创建文件等）  
- **CR（Code Review）**：人工审查 + PR Review，确认输出质量后 merge

### 如何启动 Quick Flow

在 VS Code Copilot Chat 中：

```
启动 quick dev
```

然后输入 `QS` 进入规格阶段，或 `QD` 直接进行实现（需提前有 tech-spec 文件）。

### 适用场景

- 新增或大幅重写 App 文档
- 批量修改多个文件（如 CI/CD 升级）
- 需要结构化任务跟踪的中型改动

---

## 新增 App 文档标准流程

新增一个 App 的完整文档需要**管理员前置操作 + 贡献者执行**两个阶段。

### Step 0：管理员前置操作

> **此步骤需要仓库 Write 权限 + `CONTENTFUL_ACCESS_TOKEN`，普通贡献者无法自行完成。**

1. 在 [Contentful CMS](https://app.contentful.com/) 中录入新 App 的产品数据
2. 在 GitHub Actions 页面手动触发 `sync-contentful.yml`
3. 确认以下两个文件已自动生成并 commit 到 `dev` 分支：
   - `versioned_docs/version-2.0/apps/_include/{appname}.md`
   - `i18n/en/docusaurus-plugin-content-docs/version-2.0/apps/_include/{appname}.md`

> ⚠️ **贡献者必须等管理员完成 Step 0 后才能开始。** 若 `_include/{appname}.md` 不存在，本地 `yarn build` 将因 `onBrokenLinks: throw` 报错。

### Step 1：拉取最新代码并生成骨架

```bash
git checkout dev
git pull origin dev

# 生成 App 文档骨架（根据现有模板创建文件）
python3 template/create_app.py --appname {appname} --trademark {AppTrademark} --i18n zh
```

生成的文件：

- `versioned_docs/version-2.0/apps/{appname}.md` — 中文主文档骨架
- `i18n/en/docusaurus-plugin-content-docs/version-2.0/apps/{appname}.md` — 英文文档骨架

### Step 2：使用 Quick Flow 填充文档内容

1. 在 VS Code Copilot Chat 启动 Barry：`启动 quick dev` → 输入 `QD`
2. 告知 Barry：`请帮我填充 {appname} 的 App 文档，参考模板：template/docs/zh/app.md`
3. Barry 将依据模板结构生成：
   - `## 入门指南` — 安装初始化、基本使用
   - `## 最佳实践` — 典型用例、集成方案
   - `## 配置选项` — 关键参数说明
   - `## 故障排除` — 常见问题

### Step 3：本地验证

```bash
# 验证中文版构建（_include 已存在，不会报错）
yarn build

# 或本地预览
npm run start -- --host 0.0.0.0 --port 3000
```

### Step 4：提交 PR

```bash
git checkout -b feat/{appname}-doc
git add versioned_docs/version-2.0/apps/{appname}.md
git add i18n/en/docusaurus-plugin-content-docs/version-2.0/apps/{appname}.md
git commit -m "docs: add {appname} documentation"
git push origin feat/{appname}-doc
```

向 `dev` 分支提 PR，等待 CI 检查通过后由 Owner Review。

### Step 5：英文翻译（可选但推荐）

如 Step 2 中英文文档尚未完整填充，可使用 [DeepL](https://www.deepl.com/) 翻译中文版本后补充。

---

## 参考资源

- [Docusaurus 官方文档](https://docusaurus.io/docs)
- [BMAD 方法仓库](https://github.com/bmadcode/BMAD-METHOD)
- App 文档参考样例：[`versioned_docs/version-2.0/apps/wordpress.md`](versioned_docs/version-2.0/apps/wordpress.md)
