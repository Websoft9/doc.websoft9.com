# Website

This website is built using [Docusaurus 2](https://docusaurus.io/), a modern static website generator.

## How do use it?

```
# Install
yarn install

# Development 
npm run start -- --host 0.0.0.0  --port 3002
npm run start -- --host 0.0.0.0  --port 3002  --locale en

# Build
yarn build
npm run serve -- --host 0.0.0.0  --port 3002

# Create i18n language
yarn run write-translations -- --locale zh-cn

# Upgrade Docusaurus 
yarn upgrade @docusaurus/core@latest @docusaurus/preset-classic@latest
```

## [Using-typesense-docsearch](https://docusaurus.io/zh-CN/docs/2.2.0/search#using-typesense-docsearch)

1. Install [typesense](https://github.com/Websoft9/docker-library/tree/main/apps/typesense) and configure it
2. Install [docusaurus-theme-search-typesense plugin](https://typesense.org/docs/guide/docsearch.html#step-2-add-a-search-bar-to-your-documentation-site) and [configure](https://github.com/Websoft9/doc.websoft9.com/blob/main/docusaurus.config.js) it

## Documentation system

[Divio 文档规范](https://documentation.divio.com/)
