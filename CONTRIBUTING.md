# 贡献指南（Contributing Guide）

感谢你为 [Websoft9 文档站](https://support.websoft9.com) 做出贡献！本文说明分支策略、PR 规范、i18n 要求和文档质量原则。

---

## 分支策略

| 分支 | 用途 | 说明 |
|------|------|------|
| `dev` | 开发分支 | **所有 PR 必须提交到此分支** |
| `main` | 生产分支 | 仅由 Owner 合并，触发 Cloudflare Pages 部署 |

> ⚠️ **Owner 不接受直接向 `main` 提交的 PR。**

---

## PR 流程

1. Fork 本仓库（外部贡献者）或新建 feature 分支（内部成员）
2. 在 `dev` 分支基础上创建工作分支，命名建议：`feat/appname-doc`、`fix/broken-link`
3. 完成修改后向 `dev` 分支提 PR
4. PR 会自动触发 `check.yml`（broken-links 检查）和 `build_doc.yml`（构建验证）
5. 通过 CI 检查 + Owner Review 后 merge

---

## 国际化（i18n）

本项目支持 **中文（默认）** 和 **英文** 两种语言：

| 内容类型 | 中文路径 | 英文路径 |
|----------|----------|----------|
| 版本文档 | `versioned_docs/version-2.0/` | `i18n/en/docusaurus-plugin-content-docs/version-2.0/` |
| 主题翻译 | — | `i18n/en/docusaurus-theme-classic/` |
| 插件翻译 | — | `i18n/en/code.json` |

**提交 App 或功能文档时，建议同步更新中英文两份文件。** 若英文翻译暂时缺失，可先提交中文版，后续补充英文。

推荐翻译工具：[DeepL](https://www.deepl.com/) + [DeepL Write](https://www.deepl.com/zh/write) 校对。

---

## 文档质量原则

好的文档应遵循以下 10 条原则：

1. **可维护优先**：文档进化的第一任务是可维护性，允许使用上存在"不直观"的情况
2. **组件化设计**：像编写程序一样设计文档的组件和接口
3. **三层技术体系**：文档满足入门、配置、运维三层结构
4. **通用方案复用**：通用方案参考 + 特殊要素清单 = 特殊解决方案（例：特殊 Nginx 配置只需列出配置文件模板，不重复步骤说明）
5. **路由扁平化**：路由层级不超过两层结构
6. **内容与结构分离**：`_include/` 片段由 CI 自动生成，不应手工维护
7. **锚点语义化**：标题锚点使用语义化英文（如 `{#guide}`、`{#wizard}`）
8. **截图规范**：截图命名格式 `{appname}-{feature}-websoft9.png`，存放于 `assets/` 目录
9. **链接健壮性**：避免使用绝对路径外链，内部链接使用相对路径
10. **中英文同步**：重要内容变更后及时同步英文版本

---

## 常见问题

#### 多层链接写法有哪些？

```
./../administrator/firewall#security
../
./
```

#### 异常有哪些参数类型？

```
Type: 'ignore' | 'log' | 'warn' | 'throw'
```

#### `app_from_contentful.yml` 自动生成文档需要排除哪些应用？

该 Action 根据 Contentful 产品数据自动在 `apps/` 生成中英文文档。以下类型应用需排除：

- 非 Docker 应用（如 BT、明道）
- 环境类应用（如 Python、Ruby，未放在 `apps/` 目录）

排除列表：[`template/meta/skip_file.json`](template/meta/skip_file.json)

#### `build_doc.yml` 因 `broken links` 失败？

若出现类似以下错误：

```
Broken link on source page path = /docs/apps:
  -> linking to ./phpfpmapache (resolved as: /docs/phpfpmapache)
```

说明有 App 文档路由缺失。排除列表：[`template/meta/skip_applink.json`](template/meta/skip_applink.json)

#### `json2md.yml`（Generate Apps list for docs）执行失败？

1. 下载最新制品 `media_latest.zip` 并解压
2. 在 `product_zh.json` 中找出 `"title": "产品"` 对应的 `appname`
3. 确保该 App 的父 catalog 不是一级目录
4. 重新更新 media 制品后重新触发 Action

---

## Docsearch 配置参考

如需更新 Algolia Docsearch 抓取配置，使用以下 scraper 配置：

```json
{
  "index_name": "websoft9",
  "start_urls": ["https://support.websoft9.com/"],
  "selectors": {
    "lvl0": {
      "selector": "(//ul[contains(@class,'menu__list')]//a[contains(@class,'menu__link menu__link--sublist menu__link--active')]/text() | //nav[contains(@class,'navbar')]//a[contains(@class,'navbar__link--active')]/text())[last()]",
      "type": "xpath",
      "global": true,
      "default_value": "Documentation"
    },
    "lvl1": "header h1",
    "lvl2": "article h2",
    "lvl3": "article h3",
    "lvl4": "article h4",
    "lvl5": "article h5,article td:first-child",
    "lvl6": "article h6",
    "text": "article p, article li, article td:last-child"
  },
  "strip_chars": " .,;:#",
  "custom_settings": {
    "separatorsToIndex": "_",
    "attributesForFaceting": ["language", "version", "type", "docusaurus_tag"],
    "attributesToRetrieve": ["hierarchy", "content", "anchor", "url", "url_without_anchor", "type"]
  },
  "conversation_id": ["833762294"],
  "nb_hits": 46250
}
```

