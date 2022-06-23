# Website

This website is built using [Docusaurus 2](https://docusaurus.io/), a modern static website generator.

## How do use it?

```
# Install
git clone https://github.com/Websoft9/doc.websoft9.com
cd doc.websoft9.com	
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