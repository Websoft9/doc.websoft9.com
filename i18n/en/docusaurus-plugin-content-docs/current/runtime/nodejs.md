---
title: Node.js
slug: /nodejs
tags:
  - 运行环境
  - runtime
  - Node.js
---

import Meta from '../apps/_include/nodejs.md';

<Meta name="meta" />

## 配置选项{#configs}

- 版本号： `node -v`
- Node 应用根目录： */usr/src/app*  
- 包管理器：npm, yarn
- 命令行：`node`, `yarn`, `npm`
- 开发框架：Express, Vue, React, AngularJS, Nuxt, Next, Koa, Vuepress, Gatsby.js
- 进程管理：[pm2](https://pm2.io)
- 多版本管理工具：[nvm](https://github.com/nvm-sh/nvm) 

## 部署网站{#deploy}

### 手动部署

下面通过常见的 Node.js 应用 [docusaurus](https://docusaurus.io/docs) 为例，描述应用安装过程：

1. Websoft9 控制台安装 Node.js 运行环境

2. 进入 Node.js 容器，分别运行如下命令：
   ```
   #1 创建应用基本框架
   npx create-docusaurus@latest classic

   #2 安装应用所需的包
   cd classic && yarn install

   #3 直接运行程序或在后台运行程序（取其一）
   npm run start -- --host 0.0.0.0  --port 8080
   nohup npm run start -- --host 0.0.0.0  --port 8080 > output.log 2>&1 &
   ```

3. 此时，即可访问此 Web 程序 

### 自动部署

参考 Web Runtime 通用的文档章节：[自动部署指南](./runtime#auto)


## 管理维护{#administrator}

### 升级 Node 包

以升级 npm 自身为范例，升级node 包的命令为：`npm install npm -g`

### 安装 Node 全局包

以安装 pm2 为范例，安装 Node 全局包的命令为： `npm install -g pm2`

### 进程管理

使用 PM2，可以更好的管理 Node 程序环境中的进程

```
pm2 start app.js
```

## 问题与故障

#### NPM Prevent Permissions Errors？

参考：[Fix NPM permissions](https://www.npmjs.com.cn/getting-started/fixing-npm-permissions/)

#### NPM broken？

尝试运行 `npm cache clean` 命令，若仍然没有解决问题，需更新或重装 NPM

#### YARN vs NPM？

| npm | yarn |
| ---: | :--- |
| npm install | yarn |
| npm install react --save | yarn add react |
| npm uninstall react --save | yarn remove react |
| npm install react --save-dev | yarn add react --dev |
| npm update --save | yarn upgrade |