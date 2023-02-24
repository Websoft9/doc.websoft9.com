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

## Search for Documentation Sites:
Step 1: Install docker and excute search servcice, as following:
```
git clone https://github.com/Websoft9/docker-library
cd docker-library/apps/typesense
docker compose up -d
```
Step 2: Add a Search Bar to your Documentation Site
use the docusaurus-theme-search-typesense plugin to add a search bar to your Docusaurus site:
```
npm install docusaurus-theme-search-typesense@next --save
or
yarn add docusaurus-theme-search-typesense@next
```
Add the following to your docusaurus.config.js file:
```
{
  themes: ['docusaurus-theme-search-typesense'],
  themeConfig: {
    typesense: {
      // Replace this with the name of your index/collection.
      // It should match the "index_name" entry in the scraper's "config.json" file.
      typesenseCollectionName: 'docusaurus-2',

      typesenseServerConfig: {
        nodes: [
          {
            host: 'xxx-1.a1.typesense.net',
            port: 443,
            protocol: 'https',
          }
        ],
        apiKey: 'xyz',
      },

      // Optional: Typesense search parameters: https://typesense.org/docs/0.24.0/api/search.html#search-parameters
      typesenseSearchParameters: {},

      // Optional
      contextualSearch: true,
    },
  }
}
```


## Documentation system

[Divio 文档规范](https://documentation.divio.com/)
