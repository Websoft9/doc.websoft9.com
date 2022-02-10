# Canary 版本

Docusaurus 提供 Canary 版本。

It permits you to **test new unreleased features** as soon as the pull requests are merged.

这有助于您**向维护者们提交反馈**，确保新实现的功能正常工作。

:::note

Using a canary release in production might seem risky, but in practice, it's not.

A canary release passes all automated tests and is used in production by the Docusaurus site itself.

:::

## Canary npm 版本标签

对于在` main`中的任何与代码相关的提交， 持续集成 (CI) 将通过 NPM 的 `@canary` 版本标签发布新版本。 这一般需要 10 分钟左右。

你可以在 [NPM](https://www.npmjs.com/package/@docusaurus/core?activeTab=versions) 上看到当前的版本标签：

- `latest`: stable releases (example: `2.0.0-beta.9`)
- `canary`: canary releases (example: `0.0.0-4222`)

:::tip

确保使用最新的金丝雀版本，并检查发行日期（有时发布过程可能会失败）。

:::

:::note

Canary versions follow the naming convention `0.0.0-commitNumber`.

:::

## 使用 Canary 版本

Take the latest version published under the [canary npm dist tag](https://www.npmjs.com/package/@docusaurus/core?activeTab=versions) (for example: `0.0.0-4222`).

用它替换你的 `package.json` 里的所有 `@docusaurus/*` 依赖项：

```diff
-  "@docusaurus/core": "^2.0.0-beta.9",
-  "@docusaurus/preset-classic": "^2.0.0-beta.9",
+  "@docusaurus/core": "0.0.0-4222",
+  "@docusaurus/preset-classic": "0.0.0-4222",
```

然后重新安装依赖，并启动你的网站：

```bash npm2yarn
npm install
npm start
```

You can also upgrade the `@docusaurus/*` packages with command line:

```bash npm2yarn
npm install --save-exact @docusaurus/core@canary @docusaurus/preset-classic@canary
```

:::caution

确保包含所有 `@docusaurus/*` 包。

对于金丝雀版本，建议使用精确版本，而不是语义版本范围（避免 `^` 前缀）。

:::
