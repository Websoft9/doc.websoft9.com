---
sidebar_position: 1.2
slug: /runtime/nodejs
tags:
  - 运行环境
  - runtime
  - Node.js
---

# For Node.js App

## Configuration options{#configs}

- Get Node version: `node -v`
- Node app root directory: `/usr/src/app`
- Node package tools: npm, yarn
- CLI: `node`, `yarn`, `npm`
- Web framework: Express, Vue, React, AngularJS, Nuxt, Next, Koa, Vuepress, Gatsby.js
- Process management tool: [pm2](https://pm2.io)

## Deploy a Nodejs application{#deploy}

Refer to: [App Runtime tutorials](../runtime#quick)

## Manage runtime{#administrator}

- **Upgrade Node package**: To upgrade npm itself, the command is `npm install npm -g`.

- **Install Node package**: `npm install -g pm2`

- **Use PM2 for startup**:  `pm2 start app.js`

## Troubleshoot

### NPM Prevent Permissions Errors？

Refer to: [Fix NPM permissions](https://www.npmjs.com.cn/getting-started/fixing-npm-permissions/)

### NPM broken？

Try `npm cache clean` or reinstall it again