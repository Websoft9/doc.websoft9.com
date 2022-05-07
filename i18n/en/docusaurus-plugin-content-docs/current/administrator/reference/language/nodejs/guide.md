---
sidebar_position: 1
slug: /nodejs
---

# Guide

## Tutorial

### Enable remote access

```
npm run start -- --host 0.0.0.0  --port 3002
```

### Change Node version{#changeversion}

use `nvm` command to change Node version

### Framework{#framework}

#### Express{#express}
#### Vue{#vue}
#### React{#react}
#### AngularJS{#angular}
#### Nuxt{#nuxt}
#### Next{#next}
#### Koa{#koa}
#### Vuepress{#vuepress}
#### Gatsby.js{#gatsby}

## Troubleshoot{#troubleshoot}

#### NPM Prevent Permissions Errors？

Refer to: [Fix NPM permissions](https://www.npmjs.com.cn/getting-started/fixing-npm-permissions/)

#### NPM broken？

Try to run `npm cache clean` and you need to reinstall it if that not solved

## Parameters

### Path{#path}

Node.JS Global Modules Directory: */usr/lib/node_modules*    
Node.js applicaton root directory: */data/wwwroot*    
Express demo program: */data/wwwroot/express.example.com*    
Node.JS Log file: */root/.pm2/pm2.log*    
NVM directory: */opt/nvm*  

### Version{#checkversion}

```shell
# Node.js  Version
node -v

# PM2  Version
pm2 -V

# NPM version
npm -v

# yarn version
yarn --version
``````

### Service{#service}

```shell
# PM2
systemctl start pm2-root
systemctl stop pm2-root
systemctl restart pm2-root
systemctl status pm2-root
```

### CLI{#cmd}

* node
* nvm
* npm
* yarn
* pm2