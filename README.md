# Website

This website is built using [Docusaurus 3](https://docusaurus.io/), a modern static website generator.

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

## Versioning

[Tutorials](https://docusaurus.io/docs/versioning)

You can use the versioning CLI to create a new documentation version based on the latest content in the ```docs``` directory. That specific set of documentation will then be preserved and accessible even as the documentation in the ```docs``` directory continues to evolve.

### Overview

A typical versioned doc site looks like below:

```
website
├── sidebars.json        # sidebar for the current docs version
├── docs                 # docs directory for the current docs version
│   ├── foo
│   │   └── bar.md       # https://mysite.com/docs/next/foo/bar
│   └── hello.md         # https://mysite.com/docs/next/hello
├── versions.json        # file to indicate what versions are available
├── versioned_docs
│   ├── version-1.1.0
│   │   ├── foo
│   │   │   └── bar.md   # https://mysite.com/docs/foo/bar
│   │   └── hello.md
│   └── version-1.0.0
│       ├── foo
│       │   └── bar.md   # https://mysite.com/docs/1.0.0/foo/bar
│       └── hello.md
├── versioned_sidebars
│   ├── version-1.1.0-sidebars.json
│   └── version-1.0.0-sidebars.json
├── docusaurus.config.js
└── package.json
```

### Tagging a new version

1. First, make sure the current docs version (the ./docs directory) is ready to be frozen.
2. Enter a new version number.

```
yarn docusaurus docs:version 2.0
```

### Configuring versioning behavior

```
docusaurus.config.js

export default {
  presets: [
    '@docusaurus/preset-classic',
    docs: {
      lastVersion: 'current',
      versions: {
        current: {
          label: '2.0',
          path: '2.0',
        },
      },
    },
  ],
};
```

## [Using-typesense-docsearch](https://docusaurus.io/zh-CN/docs/2.2.0/search#using-typesense-docsearch)

1. Install [typesense](https://github.com/Websoft9/docker-library/tree/main/apps/typesense) and configure it
2. Install [docusaurus-theme-search-typesense plugin](https://typesense.org/docs/guide/docsearch.html#step-2-add-a-search-bar-to-your-documentation-site) and [configure](https://github.com/Websoft9/doc.websoft9.com/blob/main/docusaurus.config.js) it

## Documentation system

[Divio 文档规范](https://documentation.divio.com/)
