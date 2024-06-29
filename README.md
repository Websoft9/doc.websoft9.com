# About

This is the documentation repository of [Websoft9](https://github.com/Websoft9/websoft9) which is a Multi-application Self-hosted PaaS platform.   

## Contribute for it

It based on [Docusaurus](https://docusaurus.io/) and you just need to edit markdown files for it.

### DevOps

You can only add PR to **dev branch**, don't accept any PR for main branch

### i18n

We only provide English and Chinese language support.

- **English files**: /i18n/docusaurus-plugin-content-docs/current
- **Chinese files**: /docs

If you want use tools for translation, we suggest you:

1. Use [DeepL](https://www.deepl.com/) and [Google Translate](https://translate.google.com/) to translate at first.
2. Then use [DeepL Write](https://www.deepl.com/zh/write) checking the results of translations

### Test it

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