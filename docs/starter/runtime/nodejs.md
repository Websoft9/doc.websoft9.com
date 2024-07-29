---
title: Node.js
sidebar_position: 1.2
slug: /nodejs
tags:
  - 运行环境
  - runtime
  - Node.js
---


## 配置选项{#configs}

- 版本号： `node -v`
- Node 应用根目录： */usr/src/app*  
- 包管理器：npm, yarn
- 命令行：`node`, `yarn`, `npm`
- 开发框架：Express, Vue, React, AngularJS, Nuxt, Next, Koa, Vuepress, Gatsby.js
- 进程管理：[pm2](https://pm2.io)
- 多版本管理工具：[nvm](https://github.com/nvm-sh/nvm) 

## 部署网站{#deploy}

参考：[Web Runtime 入门指南](./runtime)

## 环境管理{#administrator}

- **升级 Node 包**：以升级 npm 自身为范例，命令为 `npm install npm -g`

- **全局安装 Node 包**：以安装 pm2 为范例，命令为 `npm install -g pm2`

- **进程管理**：使用 PM2，可以更好的管理 Node 程序环境中的进程 `pm2 start app.js`

## 问题与故障

#### NPM Prevent Permissions Errors？

参考：[Fix NPM permissions](https://www.npmjs.com.cn/getting-started/fixing-npm-permissions/)

#### NPM broken？

尝试运行 `npm cache clean` 命令，若仍然没有解决问题，需更新或重装 NPM